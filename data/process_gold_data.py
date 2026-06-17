"""
════════════════════════════════════════════════════════════════════════════════
黄金价格可视化项目 — 数据处理完整脚本
════════════════════════════════════════════════════════════════════════════════

【输入文件】（均放在 DATA_DIR 目录下）
  XAU_USD历史数据.csv        黄金现货价格（Investing.com 导出，月度）
  DFII10.csv                 TIPS 10年期真实利率（FRED，日度）
  FEDFUNDS.csv               美联储联邦基金利率（FRED，月度）
  CPIAUCSL.csv               美国 CPI 指数（FRED，月度）
  S_P_500.csv                标普500月度收盘价（FRED/stooq，xlsx格式）
  Cushing_OK_WTI_Spot_...csv WTI 原油现货价格（EIA，月度）
  美元指数历史数据.csv         美元指数 DXY（Investing.com 导出，日度）

【输出文件】
  gold_merged.csv            月度宽表（主文件，用于可视化）
  gold_merged_report.txt     数据质量报告

【时间范围】
  主范围：2004-01 ~ 2025-12（叙事核心）
  扩展保留：2026年数据作为附加列，不截断

【处理逻辑总览】
  - 统一时间精度为"月"（YYYY-MM 字符串），作为合并主键
  - 日度数据（TIPS、DXY）→ 取月均值：代表当月整体水平，去除日内噪声
  - 月度数据（其余）→ 直接使用
  - CPI 原始指数 → 额外计算同比增速（需要12个月历史，前12行为NaN属正常）
  - 以黄金数据的完整时间跨度为主键，左连接所有其他数据
  - 各指标缺失值保留为 NaN，不插值（让使用者清楚知道哪段有数据）
  - 额外输出归一化列（0~1），供多指标叠加对比图使用
════════════════════════════════════════════════════════════════════════════════
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ── 路径配置 ─────────────────────────────────────────────────────────────────
DATA_DIR   = Path("data")
OUTPUT_CSV = Path("outputs/gold_merged.csv")
OUTPUT_RPT = Path("outputs/gold_merged_report.txt")

# ── 全局时间边界 ──────────────────────────────────────────────────────────────
# 不做硬截断，保留所有数据；可视化层面再决定显示范围
CORE_START = "2004-01"   # 叙事核心起点
CORE_END   = "2025-12"   # 叙事核心终点（2025年黄金大涨，有代表性）
# 2026年数据保留但标记为"扩展区间"


# ════════════════════════════════════════════════════════════════════════════
# 工具函数
# ════════════════════════════════════════════════════════════════════════════

def to_month(series) -> pd.Series:
    """
    将任意日期序列转换为 'YYYY-MM' 字符串。
    统一作为合并主键，避免日度/月度混用导致的对齐问题。
    """
    return pd.to_datetime(series, errors="coerce").dt.to_period("M").astype(str)


def normalize_01(series: pd.Series) -> pd.Series:
    """
    Min-Max 归一化到 [0, 1]。
    用途：多指标叠加对比图（金价、标普、原油等量纲不同，归一化后可画在同一轴）。
    """
    mn, mx = series.min(), series.max()
    if mx == mn:
        return pd.Series(np.nan, index=series.index)
    return ((series - mn) / (mx - mn)).round(4)


def pct_change_yoy(series: pd.Series, periods: int = 12) -> pd.Series:
    """
    计算同比变化率（%）。
    periods=12 表示与12个月前比较，前12行必然为 NaN，属正常现象。
    """
    return series.pct_change(periods=periods).mul(100).round(2)


# ════════════════════════════════════════════════════════════════════════════
# 1. 黄金现货价格 XAU/USD
# ════════════════════════════════════════════════════════════════════════════
"""
来源：Investing.com 导出
格式：月度，含 BOM（\ufeff），数字含千位逗号（如 "4,571.99"）
列名：中文（日期/收盘/开盘/高/低/交易量/涨跌幅）
取值：月度收盘价作为当月金价代表值
      （Investing.com 月度数据的"收盘"即为该月最后一个交易日收盘价）
"""
gold_raw = pd.read_csv(
    DATA_DIR / "XAU_USD历史数据.csv",
    encoding="utf-8-sig",   # 处理 BOM
    thousands=",",           # 自动去除千位逗号
)
gold_raw.columns = ["date", "open", "high", "low", "close", "vol", "chg"]
gold_raw["date"]  = to_month(gold_raw["date"])
gold_raw["close"] = pd.to_numeric(gold_raw["close"], errors="coerce")

gold = (
    gold_raw[["date", "close"]]
    .rename(columns={"close": "gold_usd"})
    .dropna(subset=["date"])
    .drop_duplicates("date")          # 防止同一月出现两行
    .sort_values("date")
    .reset_index(drop=True)
)

print(f"✅ 黄金:     {len(gold):>3} 行  {gold['date'].min()} ~ {gold['date'].max()}")


# ════════════════════════════════════════════════════════════════════════════
# 2. TIPS 10年期真实利率（日度 → 月均）
# ════════════════════════════════════════════════════════════════════════════
"""
来源：FRED（DFII10 系列）
格式：日度，"." 表示节假日/缺失值
处理：pd.to_numeric(..., errors="coerce") 将 "." 转为 NaN
      再按月分组取均值，代表当月整体真实利率水平

为什么取月均而不是月末值？
  真实利率的月末单日值可能受到临时因素扰动（如月末流动性紧张）。
  月均更稳定，更能代表市场在这个月对真实利率的"共识定价"。
"""
tips_raw = pd.read_csv(DATA_DIR / "DFII10.csv")
tips_raw["date"]   = to_month(tips_raw["observation_date"])
tips_raw["DFII10"] = pd.to_numeric(tips_raw["DFII10"], errors="coerce")

tips = (
    tips_raw.groupby("date")["DFII10"]
    .mean()
    .round(3)
    .reset_index()
    .rename(columns={"DFII10": "tips_real_rate"})
)

print(f"✅ TIPS:     {len(tips):>3} 行  {tips['date'].min()} ~ {tips['date'].max()}")


# ════════════════════════════════════════════════════════════════════════════
# 3. 美联储联邦基金利率（月度，直接使用）
# ════════════════════════════════════════════════════════════════════════════
"""
来源：FRED（FEDFUNDS 系列）
格式：月度，已是月均值（FRED 处理过）
无需额外处理，直接读取即可
"""
fed_raw = pd.read_csv(DATA_DIR / "FEDFUNDS.csv")
fed_raw["date"] = to_month(fed_raw["observation_date"])

fed = (
    fed_raw[["date", "FEDFUNDS"]]
    .rename(columns={"FEDFUNDS": "fed_rate"})
    .dropna(subset=["date"])
)

print(f"✅ 美联储:   {len(fed):>3} 行  {fed['date'].min()} ~ {fed['date'].max()}")


# ════════════════════════════════════════════════════════════════════════════
# 4. CPI 通胀（月度指数 → 同比增速）
# ════════════════════════════════════════════════════════════════════════════
"""
来源：FRED（CPIAUCSL 系列）
格式：月度指数值（基准年=1982-1984=100）
处理：
  - 保留原始指数值（cpi_index）：用于精确计算真实利率
  - 计算同比增速（cpi_yoy，%）：直观反映通胀速度，用于可视化标注
  - 公式：(本月指数 - 12个月前指数) / 12个月前指数 × 100
  - 前12行 cpi_yoy 为 NaN 是正常的（缺少12个月前的基准值）
"""
cpi_raw = pd.read_csv(DATA_DIR / "CPIAUCSL.csv")
cpi_raw = cpi_raw.sort_values("observation_date").reset_index(drop=True)
cpi_raw["date"]    = to_month(cpi_raw["observation_date"])
cpi_raw["cpi_yoy"] = pct_change_yoy(cpi_raw["CPIAUCSL"])

cpi = (
    cpi_raw[["date", "CPIAUCSL", "cpi_yoy"]]
    .rename(columns={"CPIAUCSL": "cpi_index"})
    .dropna(subset=["date"])
)

print(f"✅ CPI:      {len(cpi):>3} 行  {cpi['date'].min()} ~ {cpi['date'].max()}")


# ════════════════════════════════════════════════════════════════════════════
# 5. 标普500（月度收盘，xlsx 格式）
# ════════════════════════════════════════════════════════════════════════════
"""
来源：FRED 或 stooq 导出
格式：xlsx，前3行是标题/注释，第4行起是数据
列结构：[日期, 收盘价]
注意：日期是月末日（如 2004-01-30），to_month() 会转换为 "2004-01"
"""
spx_raw = pd.read_excel(
    DATA_DIR / "S_P_500.csv",
    sheet_name="Sheet1",
    header=None,
    skiprows=3,                       # 跳过前3行标题
    names=["date", "spx"],
)
spx_raw["date"] = to_month(spx_raw["date"])

spx = (
    spx_raw[["date", "spx"]]
    .dropna()
    .drop_duplicates("date")
    .sort_values("date")
    .reset_index(drop=True)
)
spx["spx"] = pd.to_numeric(spx["spx"], errors="coerce")

print(f"✅ 标普500:  {len(spx):>3} 行  {spx['date'].min()} ~ {spx['date'].max()}")


# ════════════════════════════════════════════════════════════════════════════
# 6. 原油 WTI（月度，含注释头）
# ════════════════════════════════════════════════════════════════════════════
"""
来源：EIA（美国能源信息署）
格式：CSV，前4行是来源说明/注释，第5行是列名，第6行起是数据
日期格式：英文月份缩写 + 年份（如 "Mar 2026"），需用 format="%b %Y" 解析
编码：latin-1（含Windows换行符 \r\n）
"""
oil_raw = pd.read_csv(
    DATA_DIR / "Cushing_OK_WTI_Spot_Price_FOB.csv",
    encoding="latin-1",
    skiprows=4,                         # 跳过4行注释
    names=["date", "oil_wti"],
)
oil_raw["date"]    = pd.to_datetime(oil_raw["date"].str.strip(), format="%b %Y", errors="coerce")
oil_raw["date"]    = to_month(oil_raw["date"])
oil_raw["oil_wti"] = pd.to_numeric(oil_raw["oil_wti"], errors="coerce")

oil = (
    oil_raw[["date", "oil_wti"]]
    .dropna(subset=["date"])
    .sort_values("date")
    .reset_index(drop=True)
)

print(f"✅ 原油WTI: {len(oil):>3} 行  {oil['date'].min()} ~ {oil['date'].max()}")


# ════════════════════════════════════════════════════════════════════════════
# 7. 美元指数 DXY（日度 → 月均）
# ════════════════════════════════════════════════════════════════════════════
"""
来源：Investing.com 导出（重新下载完整历史版本）
格式：日度，含 BOM，数字含千位逗号，列名中文
日期格式：'YYYY-M-D'（无零填充，如 "2004-1-2"），pd.to_datetime() 可自动解析
处理：同 TIPS，取月均值去除日内噪声

注意：当前文件数据截止约 2023-04，2023-05 之后为 NaN
      这不影响 2004-2023 年段的完整分析
"""
dxy_raw = pd.read_csv(
    DATA_DIR / "美元指数历史数据.csv",
    encoding="utf-8-sig",
    thousands=",",
)
dxy_raw.columns = ["date", "close", "open", "high", "low", "vol", "chg"]
dxy_raw["date"]  = to_month(dxy_raw["date"])
dxy_raw["close"] = pd.to_numeric(dxy_raw["close"], errors="coerce")

dxy = (
    dxy_raw.groupby("date")["close"]
    .mean()
    .round(3)
    .reset_index()
    .rename(columns={"close": "dxy"})
)

print(f"✅ DXY:     {len(dxy):>3} 行  {dxy['date'].min()} ~ {dxy['date'].max()}")


# ════════════════════════════════════════════════════════════════════════════
# 合并：以黄金数据为主键，左连接所有指标
# ════════════════════════════════════════════════════════════════════════════
"""
为什么以黄金数据为主键？
  黄金价格是本项目的"主角"，其时间跨度最完整（2004-01 ~ 2026-05）。
  左连接确保：
    - 有金价数据的每个月都会出现在结果中
    - 其他数据有就填入，没有就留 NaN
    - 不会因为某个辅助数据缺失而丢失金价记录
"""
print("\n正在合并...")

merged = gold.copy()
for df, name in [
    (tips, "TIPS"),
    (fed,  "美联储"),
    (cpi,  "CPI"),
    (spx,  "标普500"),
    (oil,  "原油"),
    (dxy,  "DXY"),
]:
    merged = merged.merge(df, on="date", how="left")
    n_merged = merged[merged.columns[-1]].notna().sum()
    print(f"  合并 {name:<6}: {n_merged} 行有数据")


# ════════════════════════════════════════════════════════════════════════════
# 派生指标
# ════════════════════════════════════════════════════════════════════════════

# 简单真实利率（事后估算）= 美联储名义利率 - CPI同比
# 与 TIPS 的区别：TIPS 是市场预期的真实利率（前瞻性），
# 这个是事后统计的真实利率（滞后性），两者对比可以揭示"市场预期差"
merged["real_rate_simple"] = (merged["fed_rate"] - merged["cpi_yoy"]).round(2)

# 金价月度环比变化率（%）
# 用于识别"价格跳变"时刻，配合事件标注使用
merged["gold_mom_pct"] = merged["gold_usd"].pct_change(1).mul(100).round(2)

# 金价同比变化率（%）
# 反映年度涨跌幅，用于标题/摘要文字
merged["gold_yoy_pct"] = pct_change_yoy(merged["gold_usd"])

# 区间标记：区分核心叙事范围和扩展范围
merged["in_core_range"] = merged["date"].between(CORE_START, CORE_END)

# ── 归一化列（各指标独立归一化到 0~1）──────────────────────────────────────
"""
用途：多指标叠加对比图
问题：金价（400~3500）、标普（1000~5000）、原油（20~140）量纲完全不同，
      无法直接画在同一 Y 轴上
解决：各自归一化到 [0,1]，0=历史最低，1=历史最高
      这样可以直观看出各指标的相对走势和背离时刻
注意：归一化是基于各列的全部有效数据范围，NaN 不参与计算
"""
COLS_TO_NORMALIZE = ["gold_usd", "tips_real_rate", "spx", "oil_wti", "dxy", "cpi_yoy", "fed_rate"]
for col in COLS_TO_NORMALIZE:
    if col in merged.columns:
        merged[f"{col}_norm"] = normalize_01(merged[col])

print(f"\n最终宽表：{len(merged)} 行 × {len(merged.columns)} 列")


# ════════════════════════════════════════════════════════════════════════════
# 输出
# ════════════════════════════════════════════════════════════════════════════
merged.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
print(f"✅ 已保存：{OUTPUT_CSV}")


# ── 数据质量报告 ─────────────────────────────────────────────────────────────
report_lines = []
report_lines.append("=" * 60)
report_lines.append("黄金可视化项目 — 数据质量报告")
report_lines.append("=" * 60)
report_lines.append(f"\n总行数：{len(merged)}")
report_lines.append(f"时间跨度：{merged['date'].min()} ~ {merged['date'].max()}")
report_lines.append(f"核心叙事范围：{CORE_START} ~ {CORE_END}")
report_lines.append(f"核心范围行数：{merged['in_core_range'].sum()}")

report_lines.append("\n\n── 各列缺失值统计 ──────────────────────────────────")
null_counts = merged.isnull().sum()
for col, cnt in null_counts.items():
    pct = cnt / len(merged) * 100
    status = "✅" if cnt == 0 else ("⚠️ " if pct < 30 else "❌")
    note = ""
    if col == "cpi_yoy" and cnt <= 12:
        note = "（正常：同比计算需要12个月基准）"
    if col == "real_rate_simple" and cnt <= 12:
        note = "（正常：依赖 cpi_yoy）"
    if "dxy" in col:
        note = "（DXY 数据截止 2023-04）"
    report_lines.append(f"  {status} {col:<25} 缺失 {cnt:>3} 行 ({pct:5.1f}%) {note}")

report_lines.append("\n\n── 各指标有效数据范围 ───────────────────────────────")
key_cols = {
    "gold_usd":        "黄金价格（美元/盎司）",
    "tips_real_rate":  "TIPS真实利率（%）",
    "fed_rate":        "美联储利率（%）",
    "cpi_yoy":         "CPI同比（%）",
    "spx":             "标普500",
    "oil_wti":         "WTI原油（美元/桶）",
    "dxy":             "美元指数DXY",
}
for col, label in key_cols.items():
    if col in merged.columns:
        valid = merged[merged[col].notna()]
        if len(valid) > 0:
            report_lines.append(
                f"  {label:<20} {valid['date'].min()} ~ {valid['date'].max()}  "
                f"[{valid[col].min():.2f} ~ {valid[col].max():.2f}]"
            )

report_lines.append("\n\n── 列名说明 ─────────────────────────────────────────")
col_desc = {
    "date":              "年月（YYYY-MM），合并主键",
    "gold_usd":          "黄金现货收盘价（美元/盎司）",
    "tips_real_rate":    "TIPS 10年期真实利率（%），市场预期真实利率",
    "fed_rate":          "美联储联邦基金利率（%）",
    "cpi_index":         "CPI 原始指数值（1982-84=100）",
    "cpi_yoy":           "CPI 同比增速（%），通胀速度",
    "spx":               "标普500月度收盘价",
    "oil_wti":           "WTI 原油现货价格（美元/桶）",
    "dxy":               "美元指数（月均，2004-2023）",
    "real_rate_simple":  "简单真实利率 = 美联储利率 - CPI同比（%）",
    "gold_mom_pct":      "金价月环比变化率（%），用于识别价格跳变",
    "gold_yoy_pct":      "金价年同比变化率（%）",
    "in_core_range":     "是否在核心叙事范围内（True/False）",
    "*_norm":            "各指标0~1归一化值，用于多指标叠加对比图",
}
for col, desc in col_desc.items():
    report_lines.append(f"  {col:<22} {desc}")

report_text = "\n".join(report_lines)
print("\n" + report_text)

with open(OUTPUT_RPT, "w", encoding="utf-8") as f:
    f.write(report_text)

print(f"\n✅ 报告已保存：{OUTPUT_RPT}")
