/* ── INLINE DATA ───────────────────────────────────────────────── */
const DATES=["2004-01","2004-02","2004-03","2004-04","2004-05","2004-06","2004-07","2004-08","2004-09","2004-10","2004-11","2004-12","2005-01","2005-02","2005-03","2005-04","2005-05","2005-06","2005-07","2005-08","2005-09","2005-10","2005-11","2005-12","2006-01","2006-02","2006-03","2006-04","2006-05","2006-06","2006-07","2006-08","2006-09","2006-10","2006-11","2006-12","2007-01","2007-02","2007-03","2007-04","2007-05","2007-06","2007-07","2007-08","2007-09","2007-10","2007-11","2007-12","2008-01","2008-02","2008-03","2008-04","2008-05","2008-06","2008-07","2008-08","2008-09","2008-10","2008-11","2008-12","2009-01","2009-02","2009-03","2009-04","2009-05","2009-06","2009-07","2009-08","2009-09","2009-10","2009-11","2009-12","2010-01","2010-02","2010-03","2010-04","2010-05","2010-06","2010-07","2010-08","2010-09","2010-10","2010-11","2010-12","2011-01","2011-02","2011-03","2011-04","2011-05","2011-06","2011-07","2011-08","2011-09","2011-10","2011-11","2011-12","2012-01","2012-02","2012-03","2012-04","2012-05","2012-06","2012-07","2012-08","2012-09","2012-10","2012-11","2012-12","2013-01","2013-02","2013-03","2013-04","2013-05","2013-06","2013-07","2013-08","2013-09","2013-10","2013-11","2013-12","2014-01","2014-02","2014-03","2014-04","2014-05","2014-06","2014-07","2014-08","2014-09","2014-10","2014-11","2014-12","2015-01","2015-02","2015-03","2015-04","2015-05","2015-06","2015-07","2015-08","2015-09","2015-10","2015-11","2015-12","2016-01","2016-02","2016-03","2016-04","2016-05","2016-06","2016-07","2016-08","2016-09","2016-10","2016-11","2016-12","2017-01","2017-02","2017-03","2017-04","2017-05","2017-06","2017-07","2017-08","2017-09","2017-10","2017-11","2017-12","2018-01","2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02","2019-03","2019-04","2019-05","2019-06","2019-07","2019-08","2019-09","2019-10","2019-11","2019-12","2020-01","2020-02","2020-03","2020-04","2020-05","2020-06","2020-07","2020-08","2020-09","2020-10","2020-11","2020-12","2021-01","2021-02","2021-03","2021-04","2021-05","2021-06","2021-07","2021-08","2021-09","2021-10","2021-11","2021-12","2022-01","2022-02","2022-03","2022-04","2022-05","2022-06","2022-07","2022-08","2022-09","2022-10","2022-11","2022-12","2023-01","2023-02","2023-03","2023-04","2023-05","2023-06","2023-07","2023-08","2023-09","2023-10","2023-11","2023-12","2024-01","2024-02","2024-03","2024-04","2024-05","2024-06","2024-07","2024-08","2024-09","2024-10","2024-11","2024-12","2025-01","2025-02","2025-03","2025-04","2025-05","2025-06","2025-07","2025-08","2025-09","2025-10","2025-11","2025-12"];
const GOLD=[402.57,396.45,426.62,387.6,395.5,394.38,391.25,409.82,418.25,428.52,450.88,438.45,422.62,435.62,428.45,434.88,417.35,435.25,430.2,435.25,469.15,465.2,493.85,517.6,549.45,534.95,534.05,582.3,636.6,543.5,601.98,607.3,571.7,559.9,605.7,611.8,602.2,643.15,632.8,656.45,652.05,639.65,645.5,641.5,671.4,721.1,773.0,777.4,833.83,885.67,905.05,863.3,846.0,857.8,894.5,774.9,738.0,682.8,702.25,742.4,802.65,888.0,883.9,865.0,880.55,913.9,906.0,931.2,947.0,986.7,1040.65,1074.6,1074.25,1044.15,1085.85,1112.35,1157.7,1197.65,1157.4,1176.5,1236.7,1306.1,1324.04,1363.35,1308.38,1325.14,1382.9,1414.55,1464.4,1490.8,1478.51,1608.19,1534.99,1597.14,1666.48,1522.44,1564.91,1688.49,1628.29,1612.28,1529.0,1545.09,1554.95,1585.1,1685.62,1698.89,1672.74,1635.61,1626.4,1555.1,1561.18,1321.89,1339.58,1181.09,1207.88,1273.25,1291.83,1252.05,1227.86,1184.75,1199.29,1240.62,1282.54,1268.52,1242.24,1240.95,1281.06,1273.41,1204.65,1161.53,1132.13,1143.16,1168.75,1191.16,1143.18,1175.26,1170.64,1162.84,1077.45,1081.0,1098.75,1104.72,1052.84,1046.22,1060.74,1116.24,1208.55,1209.0,1199.88,1206.02,1310.8,1305.02,1302.33,1241.46,1170.72,1122.69,1145.99,1198.04,1194.89,1243.69,1214.18,1236.78,1204.73,1251.36,1277.6,1260.51,1265.49,1236.27,1302.6,1306.99,1302.76,1310.29,1282.0,1245.67,1211.48,1160.19,1180.68,1183.24,1196.19,1221.22,1276.58,1302.53,1281.1,1266.25,1266.18,1306.62,1381.84,1400.65,1464.42,1459.0,1445.61,1453.91,1517.12,1547.4,1451.5,1566.97,1670.06,1670.74,1757.68,1864.3,1848.45,1859.67,1764.69,1775.52,1810.46,1717.26,1676.7,1705.42,1765.91,1750.11,1765.47,1684.77,1721.07,1745.45,1758.45,1753.84,1779.88,1788.39,1890.03,1872.19,1786.95,1802.2,1680.78,1709.1,1614.35,1617.21,1616.18,1765.32,1823.85,1804.65,1809.4,1949.82,1932.08,1893.01,1902.68,1884.35,1846.34,1810.1,1931.73,1973.09,2001.91,1984.3,2038.55,2228.54,2277.47,2286.77,2318.55,2364.4,2471.95,2604.15,2536.9,2583.49,2614.6,2771.69,2855.63,2956.6,3120.52,3247.86,3268.15,3281.55,3436.8,3819.51,3928.66,4163.01];
const TIPS=[1.89,1.76,1.47,1.9,2.09,2.15,2.02,1.86,1.8,1.73,1.68,1.67,1.72,1.63,1.79,1.71,1.65,1.68,1.88,1.89,1.7,1.94,2.06,2.12,2.01,2.05,2.2,2.41,2.45,2.53,2.51,2.29,2.32,2.41,2.29,2.25,2.44,2.36,2.18,2.26,2.37,2.69,2.64,2.44,2.26,2.2,1.77,1.79,1.47,1.41,1.09,1.36,1.46,1.63,1.57,1.68,1.85,2.75,2.89,2.17,1.91,1.75,1.71,1.57,1.72,1.86,1.82,1.77,1.64,1.48,1.27,1.36,1.38,1.42,1.51,1.5,1.31,1.26,1.24,1.02,0.91,0.53,0.67,1.04,1.06,1.24,0.96,0.86,0.78,0.76,0.62,0.14,0.08,0.19,0.0,-0.03,-0.11,-0.25,-0.14,-0.21,-0.34,-0.5,-0.6,-0.59,-0.71,-0.75,-0.77,-0.76,-0.61,-0.57,-0.58,-0.65,-0.35,0.25,0.46,0.55,0.66,0.43,0.55,0.74,0.63,0.55,0.56,0.54,0.37,0.37,0.28,0.22,0.46,0.38,0.45,0.51,0.27,0.26,0.28,0.08,0.33,0.5,0.5,0.56,0.65,0.57,0.69,0.73,0.67,0.47,0.34,0.19,0.21,0.17,0.04,0.09,0.12,0.1,0.32,0.56,0.42,0.4,0.49,0.39,0.47,0.46,0.55,0.43,0.37,0.5,0.5,0.5,0.54,0.76,0.75,0.74,0.84,0.8,0.78,0.79,0.88,1.04,1.11,1.02,0.92,0.8,0.66,0.6,0.57,0.37,0.31,0.04,0.11,0.15,0.17,0.14,0.04,-0.11,-0.12,-0.45,-0.44,-0.55,-0.83,-1.01,-0.98,-0.92,-0.84,-0.98,-1.0,-0.92,-0.66,-0.71,-0.85,-0.82,-1.01,-1.06,-0.97,-0.95,-1.06,-0.99,-0.69,-0.52,-0.72,-0.14,0.21,0.53,0.53,0.39,1.14,1.59,1.52,1.36,1.29,1.41,1.36,1.19,1.36,1.55,1.6,1.83,2.04,2.41,2.2,1.84,1.79,1.93,1.9,2.15,2.15,2.05,1.97,1.76,1.62,1.81,2.04,2.09,2.23,2.03,1.95,2.04,2.11,2.09,2.01,1.88,1.75,1.76,1.83,1.9];

/* ── HERO LIVE PRICE ──────────────────────────────────────────── */
(function initHeroLivePrice() {
  const priceEl = document.querySelector('.hero-price-value');
  const noteEl = document.querySelector('.hero-price-note');
  if (!priceEl || !noteEl) return;

  const fallbackPrice = priceEl.textContent.trim();
  const endpoint = 'https://api.gold-api.com/price/XAU';
  const priceFormat = new Intl.NumberFormat('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
  const timeFormat = new Intl.DateTimeFormat('zh-CN', {
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  });

  function normalizeTime(value) {
    if (!value) return new Date();
    if (typeof value === 'number') {
      return new Date(value < 1e12 ? value * 1000 : value);
    }
    const parsed = new Date(value);
    return Number.isNaN(parsed.getTime()) ? new Date() : parsed;
  }

  async function loadPrice() {
    try {
      const response = await fetch(endpoint, { cache: 'no-store' });
      if (!response.ok) throw new Error(`Gold price request failed: ${response.status}`);

      const quote = await response.json();
      const price = Number(quote.price ?? quote.ask ?? quote.bid);
      if (!Number.isFinite(price)) throw new Error('Gold price response missing price');

      const updatedAt = normalizeTime(quote.updatedAt ?? quote.updated_at ?? quote.timestamp);
      priceEl.textContent = priceFormat.format(price);
      noteEl.textContent = `${timeFormat.format(updatedAt)} 更新 · USD/oz`;
    } catch (error) {
      priceEl.textContent = fallbackPrice;
      noteEl.textContent = '实时价格获取失败 · 显示历史月末价';
      console.warn(error);
    }
  }

  loadPrice();
  window.setInterval(loadPrice, 5 * 60 * 1000);
})();

/* ── INTRO CHART ───────────────────────────────────────────────── */
(function initIntroChart() {
  const el = document.getElementById('chart-intro');
  if (!el) return;
  const chart = echarts.init(el, null, { renderer: 'svg' });

  // Build series data
  const data = DATES.map((d, i) => [d, GOLD[i]]);

  const option = {
    animation: true,
    animationDuration: 1800,
    animationEasing: 'cubicOut',
    grid: { top: 20, right: 0, bottom: 0, left: 0, containLabel: false },
    xAxis: {
      type: 'category',
      data: DATES,
      show: false,
      boundaryGap: false,
    },
    yAxis: {
      type: 'value',
      show: false,
      min: 'dataMin',
      max: 'dataMax',
    },
    series: [{
      type: 'line',
      data: GOLD,
      symbol: 'none',
      lineStyle: {
        color: '#b07a18',
        width: 2,
        shadowColor: 'rgba(176,122,24,0.34)',
        shadowBlur: 10,
      },
      smooth: 0.3,
    }],
    tooltip: { show: false },
  };

  chart.setOption(option);
  window.addEventListener('resize', () => chart.resize());
})();

/* ── SCROLL FADE-IN ────────────────────────────────────────────── */
(function initFadeIn() {
  const els = document.querySelectorAll('.fade-in');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
  els.forEach(el => obs.observe(el));
})();

/* ── ACTIVE NAV ────────────────────────────────────────────────── */
(function initStoryDeck() {
  const panelIds = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'epilogue'];
  const panels = panelIds.map(id => document.getElementById(id)).filter(Boolean);
  const tabs = document.querySelectorAll('.story-tab');
  const navLinks = document.querySelectorAll('.nav-links a');
  const progress = document.querySelector('.story-progress-bar');
  const controls = document.querySelectorAll('.deck-button');
  const initialHash = location.hash.replace('#', '');
  if (panelIds.includes(initialHash) && history.replaceState) {
    history.replaceState(null, '', location.pathname + location.search);
    window.scrollTo({ top: 0, left: 0, behavior: 'auto' });
  }
  let activeIndex = 0;

  function syncDeck(index, shouldScroll = true) {
    activeIndex = Math.max(0, Math.min(index, panels.length - 1));
    const activeId = panelIds[activeIndex];

    panels.forEach((panel, i) => {
      const isActive = i === activeIndex;
      panel.classList.toggle('active', isActive);
      panel.setAttribute('aria-hidden', String(!isActive));
      if (isActive) {
        panel.querySelectorAll('.fade-in').forEach(el => el.classList.add('visible'));
      }
    });

    tabs.forEach(tab => {
      const isActive = tab.dataset.target === activeId;
      tab.classList.toggle('active', isActive);
      tab.setAttribute('aria-selected', String(isActive));
    });

    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${activeId}`);
    });

    controls.forEach(button => {
      const step = Number(button.dataset.step || 0);
      button.disabled = (activeIndex === 0 && step < 0) || (activeIndex === panels.length - 1 && step > 0);
    });

    if (progress) {
      progress.style.width = `${((activeIndex + 1) / panels.length) * 100}%`;
    }

    if (shouldScroll) {
      document.querySelector('.story-deck')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => syncDeck(index));
  });

  controls.forEach(button => {
    button.addEventListener('click', () => syncDeck(activeIndex + Number(button.dataset.step || 0)));
  });

  navLinks.forEach(link => {
    link.addEventListener('click', event => {
      const target = link.getAttribute('href')?.replace('#', '');
      const index = panelIds.indexOf(target);
      if (index >= 0) {
        event.preventDefault();
        syncDeck(index);
      }
    });
  });

  window.addEventListener('hashchange', () => {
    const index = panelIds.indexOf(location.hash.replace('#', ''));
    if (index >= 0) syncDeck(index, false);
  });

  syncDeck(activeIndex, false);
})();

/* ── ACTIVE INTRO NAV ──────────────────────────────────────────── */
(function initActiveNav() {
  const links = document.querySelectorAll('.nav-links a');

  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting && e.target.id === 'intro') {
        links.forEach(l => l.classList.remove('active'));
        const active = document.querySelector(`.nav-links a[href="#${e.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { threshold: 0.3 });

  const intro = document.getElementById('intro');
  if (intro) obs.observe(intro);
})();
