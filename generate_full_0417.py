#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整生成2026年4月17日老盛早知道
"""

html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>老盛早知道 · 2026年4月17日</title>
<style>
  :root {
    --bg-primary: #0d1117;
    --bg-secondary: #161b22;
    --bg-card: #1c2333;
    --bg-hover: #21273a;
    --accent: #00d4ff;
    --accent-dim: rgba(0,212,255,0.15);
    --accent-border: rgba(0,212,255,0.35);
    --green: #3fb950;
    --red: #f85149;
    --yellow: #d29922;
    --purple: #bc8cff;
    --orange: #ffa657;
    --text-primary: #e6edf3;
    --text-secondary: #b0bac4;
    --text-muted: #8b95a5;
    --border: rgba(48,54,61,0.8);
    --radius: 10px;
    --radius-sm: 6px;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    font-family: -apple-system, 'SF Pro Text', 'PingFang SC', 'Noto Sans SC', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    font-size: 15px;
    line-height: 1.7;
    min-height: 100vh;
    background-image:
      radial-gradient(ellipse 80% 40% at 50% -5%, rgba(0,80,160,0.14) 0%, transparent 60%),
      repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,212,255,0.008) 3px, rgba(0,212,255,0.008) 4px);
  }

  /* ══════════ HEADER ══════════ */
  .header {
    background: linear-gradient(180deg, #080e18 0%, #0a1422 100%);
    border-bottom: 1px solid rgba(0,212,255,0.18);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 40px rgba(0,0,0,0.7), 0 1px 0 rgba(0,212,255,0.12);
  }
  .header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent 0%, var(--accent) 25%, var(--purple) 75%, transparent 100%);
    box-shadow: 0 0 18px var(--accent), 0 0 36px rgba(0,212,255,0.25);
  }

  .inner {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 40px;
  }
  .header-inner {
    max-width: 1200px;
    margin: 0 auto;
    padding: 22px 40px 0;
  }
  .header-top {
    display: grid;
    grid-template-columns: 72px 1fr auto;
    align-items: center;
    gap: 22px;
    padding-bottom: 16px;
  }

  .brand-icon {
    width: 72px; height: 72px;
    background: linear-gradient(145deg, #0a1e35 0%, #0d2040 60%, #091828 100%);
    border: 1px solid rgba(0,212,255,0.38);
    border-radius: 18px;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 0 28px rgba(0,212,255,0.32), 0 0 8px rgba(0,212,255,0.12), inset 0 1px 0 rgba(255,255,255,0.08);
    flex-shrink: 0;
    position: relative;
    overflow: hidden;
    align-self: center;
  }
  .brand-icon::before {
    content: '';
    position: absolute; top: -4px; left: -4px;
    width: 32px; height: 32px;
    background: radial-gradient(circle, rgba(0,212,255,0.22) 0%, transparent 70%);
    pointer-events: none;
  }
  .brand-icon::after {
    content: '';
    position: absolute; inset: 0; border-radius: 18px;
    background: linear-gradient(135deg, rgba(0,212,255,0.08) 0%, transparent 55%);
    pointer-events: none;
  }
  .brand-icon svg { width:36px; height:36px; position:relative; z-index:1; }
  .brand-title { display:flex; flex-direction:column; justify-content:center; gap:6px; line-height:1; }
  .brand-en-row { display:flex; align-items:center; gap:8px; }
  .brand-en {
    font-size: 9.5px; font-weight: 600; letter-spacing: 2.5px;
    color: var(--accent); opacity: 0.4; text-transform: uppercase;
    font-family: 'SF Mono','Fira Code','Consolas',monospace;
  }
  .brand-issue {
    font-size: 9px; font-weight: 500; letter-spacing: 1px;
    color: var(--text-muted); font-family: 'SF Mono','Fira Code','Consolas',monospace;
    padding: 1px 6px; border: 1px solid rgba(0,212,255,0.12);
    border-radius: 3px; background: rgba(0,212,255,0.03);
  }
  .brand-main-row {
    display: flex;
    align-items: center;
  }
  .brand-signal {
    position: relative;
    display: inline-flex;
    align-items: center;
    cursor: default;
    padding: 4px 0;
  }
  .brand-signal::before {
    content: '';
    position: absolute;
    inset: -8px -16px;
    border-radius: 10px;
    background: radial-gradient(ellipse at center, rgba(0,212,255,0.06) 0%, transparent 70%);
    animation: signal-pulse 5s ease-in-out infinite;
    pointer-events: none;
  }
  .brand-name {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: 5px;
    color: #e6edf3;
    position: relative;
  }
  .brand-sep {
    position: relative;
    width: 2px;
    height: 22px;
    background: rgba(0,212,255,0.15);
    margin: 0 10px;
    border-radius: 1px;
    align-self: center;
    overflow: visible;
  }
  .brand-sep::after {
    content: '';
    position: absolute;
    left: -1.5px;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 8px rgba(0,212,255,0.8), 0 0 20px rgba(0,212,255,0.3);
    animation: sep-slide 3s ease-in-out infinite;
  }
  .brand-zaodao {
    font-size: 28px;
    font-weight: 300;
    letter-spacing: 5px;
    color: var(--accent);
    text-shadow: 0 0 20px rgba(0,212,255,0.35);
    position: relative;
  }
  @keyframes signal-pulse {
    0%, 100% { opacity: 0.4; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.02); }
  }
  @keyframes sep-slide {
    0%   { top: 0; opacity: 0; }
    15%  { opacity: 1; }
    50%  { top: calc(100% - 5px); opacity: 1; }
    85%  { opacity: 1; }
    100% { top: 0; opacity: 0; }
  }
  .brand-tag {
    font-size: 11px;
    font-weight: 400;
    letter-spacing: 2px;
    color: var(--text-primary);
    margin-left: 12px;
    opacity: 0.35;
    white-space: nowrap;
  }
  .brand-subtitle {
    font-size: 11.5px; color: var(--text-muted);
    letter-spacing: 0.5px; display:flex; align-items:center; margin-top:3px;
  }
  .brand-subtitle .dot { color: rgba(0,212,255,0.28); margin: 0 7px; }
  .header-meta {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 8px;
    flex-shrink: 0;
    padding-left: 20px;
    border-left: 1px solid rgba(0,212,255,0.1);
  }
  .header-date {
    display: flex; align-items: center; gap: 8px;
    font-size: 14px; font-weight: 500;
    color: var(--text-secondary);
    font-family: 'SF Mono','Fira Code','Consolas',monospace;
    letter-spacing: 0.3px;
  }
  .header-date svg { width: 16px; height: 16px; stroke: var(--accent); opacity: 0.7; }
  .header-tags { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
  .header-tag {
    font-size: 10.5px; font-weight: 500; letter-spacing: 0.3px;
    padding: 3px 8px; border-radius: 4px;
    font-family: 'SF Mono','Fira Code','Consolas',monospace;
    border: 1px solid;
  }
  .header-tag.tag-blue { color: var(--accent); background: rgba(0,212,255,0.08); border-color: rgba(0,212,255,0.25); }
  .header-tag.tag-green { color: var(--green); background: rgba(63,185,80,0.08); border-color: rgba(63,185,80,0.25); }
  .header-tag.tag-purple { color: var(--purple); background: rgba(188,140,255,0.08); border-color: rgba(188,140,255,0.25); }
  .header-tag.tag-orange { color: var(--orange); background: rgba(255,166,87,0.08); border-color: rgba(255,166,87,0.25); }

  /* ══════════ NAVIGATION ══════════ */
  .nav-bar {
    border-top: 1px solid rgba(0,212,255,0.08);
    padding: 12px 0;
  }
  .nav-tabs {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    scrollbar-width: none;
    -ms-overflow-style: none;
    padding-bottom: 2px;
  }
  .nav-tabs::-webkit-scrollbar { display: none; }
  .tab-btn {
    background: transparent;
    border: 1px solid transparent;
    color: var(--text-muted);
    font-size: 13px;
    font-weight: 500;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s ease;
    font-family: inherit;
    letter-spacing: 0.3px;
  }
  .tab-btn:hover {
    background: rgba(0,212,255,0.06);
    color: var(--text-secondary);
  }
  .tab-btn.active {
    background: rgba(0,212,255,0.12);
    border-color: rgba(0,212,255,0.35);
    color: var(--accent);
    box-shadow: 0 0 12px rgba(0,212,255,0.15), inset 0 1px 0 rgba(255,255,255,0.05);
  }

  /* ══════════ MAIN CONTENT ══════════ */
  .main-content { padding: 32px 0 60px; }
  .tab-panel { display: none; animation: fadeIn 0.3s ease; }
  .tab-panel.active { display: block; }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .section-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(0,212,255,0.15);
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: 0.5px;
  }
  .sub-section { margin-bottom: 32px; }
  .sub-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 14px;
    padding-left: 12px;
    border-left: 3px solid var(--accent);
    letter-spacing: 0.3px;
  }

  /* ══════════ CARDS ══════════ */
  .card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 18px 20px;
    margin-bottom: 14px;
    transition: all 0.2s ease;
  }
  .card:hover {
    border-color: rgba(0,212,255,0.25);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3), 0 0 0 1px rgba(0,212,255,0.08);
    transform: translateY(-1px);
  }
  .card-title {
    font-size: 15px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 10px;
    line-height: 1.5;
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }
  .card-body {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.8;
  }
  .card-body strong {
    color: var(--text-primary);
    font-weight: 600;
  }
  .tag {
    display: inline-block;
    font-size: 10.5px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    flex-shrink: 0;
  }
  .tag-finance { background: rgba(0,212,255,0.12); color: var(--accent); }
  .tag-policy { background: rgba(63,185,80,0.12); color: var(--green); }
  .tag-ai { background: rgba(188,140,255,0.12); color: var(--purple); }
  .tag-energy { background: rgba(255,166,87,0.12); color: var(--orange); }
  .tag-chip { background: rgba(242,201,76,0.12); color: #f2c94c; }

  /* ══════════ HIGHLIGHT CARDS ══════════ */
  .highlight-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }
  .highlight-card {
    background: linear-gradient(145deg, var(--bg-card) 0%, rgba(0,212,255,0.03) 100%);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: var(--radius);
    padding: 20px;
    position: relative;
    overflow: hidden;
  }
  .highlight-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent) 0%, var(--purple) 100%);
    opacity: 0.6;
  }
  .highlight-title {
    font-size: 13px;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 8px;
    letter-spacing: 0.5px;
  }
  .highlight-text {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.7;
  }
  .highlight-text strong {
    color: var(--text-primary);
    font-weight: 600;
  }

  /* ══════════ STOCK CARDS ══════════ */
  .stock-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: var(--radius);
    padding: 18px 20px;
    margin-bottom: 14px;
  }
  .stock-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
    flex-wrap: wrap;
  }
  .stock-name {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-primary);
  }
  .stock-code {
    font-size: 12px;
    color: var(--text-muted);
    font-family: 'SF Mono','Fira Code','Consolas',monospace;
    background: rgba(0,212,255,0.06);
    padding: 2px 8px;
    border-radius: 4px;
  }
  .stock-price-area {
    margin-left: auto;
    text-align: right;
  }
  .stock-price {
    font-size: 20px;
    font-weight: 700;
    font-family: 'SF Mono','Fira Code','Consolas',monospace;
  }
  .stock-price.up { color: var(--red); }
  .stock-price.down { color: var(--green); }
  .stock-price.neutral { color: var(--text-secondary); }
  .stock-change {
    font-size: 12px;
    font-family: 'SF Mono','Fira Code','Consolas',monospace;
    margin-top: 2px;
  }
  .stock-change.up { color: var(--red); }
  .stock-change.down { color: var(--green); }
  .stock-change.neutral { color: var(--text-muted); }
  .stock-bullets {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .stock-bullets li {
    font-size: 13.5px;
    color: var(--text-secondary);
    padding: 6px 0 6px 18px;
    position: relative;
    line-height: 1.7;
    border-bottom: 1px solid rgba(48,54,61,0.4);
  }
  .stock-bullets li:last-child { border-bottom: none; }
  .stock-bullets li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 13px;
    width: 6px;
    height: 6px;
    background: var(--accent);
    border-radius: 50%;
    opacity: 0.7;
  }
  .stock-bullets li strong {
    color: var(--text-primary);
    font-weight: 600;
  }

  /* ══════════ SUMMARY CARD ══════════ */
  .summary-card {
    background: linear-gradient(145deg, rgba(0,212,255,0.06) 0%, var(--bg-card) 100%);
    border: 1px solid rgba(0,212,255,0.2);
    border-radius: var(--radius);
    padding: 24px;
    margin-bottom: 20px;
  }
  .summary-card p {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.9;
    margin-bottom: 14px;
  }
  .summary-card p:last-child { margin-bottom: 0; }
  .summary-card p strong {
    color: var(--text-primary);
    font-weight: 600;
  }

  /* ══════════ HOT BAR ══════════ */
  .hot-bar {
    background: linear-gradient(90deg, rgba(255,166,87,0.1) 0%, rgba(255,166,87,0.05) 100%);
    border: 1px solid rgba(255,166,87,0.2);
    border-radius: var(--radius-sm);
    padding: 12px 16px;
    font-size: 13px;
    color: var(--text-secondary);
    margin-bottom: 20px;
  }
  .hot-bar strong { color: var(--orange); }

  /* ══════════ FOOTER ══════════ */
  .footer {
    text-align: center;
    padding: 30px 40px;
    border-top: 1px solid var(--border);
    font-size: 12px;
    color: var(--text-muted);
    background: var(--bg-secondary);
    letter-spacing: 0.3px;
  }
  .footer span { color: var(--accent); font-weight: 600; }

  /* ══════════ SENTIMENT BARS ══════════ */
  .sentiment-bar-wrap { margin-bottom: 14px; }
  .sentiment-bar-wrap:last-child { margin-bottom: 0; }
  .sentiment-label {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    color: var(--text-secondary);
    margin-bottom: 6px;
  }
  .sentiment-bar {
    height: 6px;
    background: rgba(48,54,61,0.6);
    border-radius: 3px;
    overflow: hidden;
  }
  .sentiment-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--accent) 0%, var(--purple) 100%);
    border-radius: 3px;
    transition: width 0.5s ease;
  }

  /* ══════════ RESPONSIVE ══════════ */
  @media (max-width: 768px) {
    .inner, .header-inner { padding: 0 16px; }
    .header-top {
      grid-template-columns: 48px 1fr;
      gap: 12px;
    }
    .brand-icon { width: 48px; height: 48px; border-radius: 12px; }
    .brand-icon svg { width: 26px; height: 26px; }
    .brand-name, .brand-zaodao { font-size: 20px; letter-spacing: 3px; }
    .brand-en { font-size: 8px; }
    .header-meta {
      grid-column: 1 / -1;
      border-left: none;
      padding-left: 0;
      flex-direction: row;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }
    .header-date { font-size: 12px; }
    .header-tags { justify-content: flex-start; }
    .nav-tabs { padding: 0 4px; }
    .tab-btn { padding: 6px 12px; font-size: 12px; }
    .highlight-grid { grid-template-columns: 1fr; }
    .stock-header { flex-direction: column; align-items: flex-start; gap: 6px; }
    .stock-price-area { margin-left: 0; text-align: left; }
  }

  /* ══════════ UTILITIES ══════════ */
  .up { color: var(--red) !important; }
  .down { color: var(--green) !important; }
  .neutral { color: var(--text-secondary) !important; }
</style>
</head>
<body>

<!-- HEADER -->
<div class="header">
  <div class="header-inner">
    <div class="header-top">
      <div class="brand-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="color:var(--accent);">
          <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path>
        </svg>
      </div>
      <div class="brand-title">
        <div class="brand-en-row">
          <span class="brand-en">LAO SHENG MORNING BRIEF</span>
          <span class="brand-issue">NO.20260417</span>
        </div>
        <div class="brand-main-row">
          <span class="brand-signal"><span class="brand-name">老盛</span></span>
          <span class="brand-sep"></span>
          <span class="brand-zaodao">早知道</span>
        </div>
      </div>
      <div class="header-meta">
        <div class="header-date">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          2026年4月17日 · 星期四
        </div>
        <div class="header-tags">
          <span class="header-tag tag-blue">美伊框架协议将达成</span>
          <span class="header-tag tag-green">创业板创11年新高</span>
          <span class="header-tag tag-purple">GPT-6发布催化</span>
        </div>
      </div>
    </div>

    <!-- NAVIGATION -->
    <div class="nav-bar">
      <div class="nav-tabs">
        <button class="tab-btn active" onclick="switchTab(0)">要点速览</button>
        <button class="tab-btn" onclick="switchTab(1)">国内外新闻</button>
        <button class="tab-btn" onclick="switchTab(2)">AI前沿</button>
        <button class="tab-btn" onclick="switchTab(3)">全球市场</button>
        <button class="tab-btn" onclick="switchTab(4)">价值投资风向</button>
        <button class="tab-btn" onclick="switchTab(5)">关注标的</button>
        <button class="tab-btn" onclick="switchTab(6)">今日总结</button>
      </div>
    </div>
  </div>
</div>

<!-- MAIN CONTENT -->
<div class="main-content">

<!-- TAB 0: 要点速览 -->
<div class="tab-panel active" id="panel-0">
  <div class="inner">
  <div class="section-title">⚡ 本期要点速览</div>

  <div class="highlight-grid">
    <div class="highlight-card">
      <div class="highlight-title">🌍 国际要闻</div>
      <div class="highlight-text">
        <strong>美伊框架协议即将达成：</strong>央视记者4月15日获悉，美伊谈判代表正逐步接近达成结束冲突的框架性协议。特朗普表示"很有可能"在4月下旬与伊朗达成协议。以色列与黎巴嫩启动为期10天临时停火。全球风险偏好大幅改善，油价承压，美股纳指再创历史新高。
      </div>
    </div>
    <div class="highlight-card">
      <div class="highlight-title">🇨🇳 国内要闻</div>
      <div class="highlight-text">
        <strong>创业板涨3.17%创近11年新高：</strong>4月16日A股收盘：上证指数4055.55(+0.70%)；深证成指14796.33(+2.05%)；创业板指3626.27(+3.17%)，创2015年6月以来近11年新高！两市成交约23400亿元，超4300只个股上涨。AI与新能源主线集体爆发。
      </div>
    </div>
    <div class="highlight-card">
      <div class="highlight-title">📈 市场热点</div>
      <div class="highlight-text">
        <strong>美股纳指十连阳创历史新高：</strong>4月16日美股纳斯达克实现连续第十个交易日上涨，创下自2023年以来的最长连涨纪录，标普500逼近7000点大关。科技股表现强势，算力巨头携手冲高，GPT-6发布持续催化AI板块。
      </div>
    </div>
    <div class="highlight-card">
      <div class="highlight-title">🔋 产业动态</div>
      <div class="highlight-text">
        <strong>宁德时代超级科技日4月21日举办：</strong>这将是公司成立以来技术密度最高的一场发布会，预计将展示全固态电池阶段性成果及麒麟电池迭代技术。新能源产业链4-5月排产同比增6成，行业景气度持续上行。
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-title">💡 核心逻辑</div>
    <div class="card-body">
      <strong>今日最大变量：美伊框架协议接近达成，全球地缘风险大幅降温。</strong>特朗普表示"很有可能"在4月下旬与伊朗达成协议。全球风险偏好大幅改善，美股纳指再创历史新高，A股创业板指创近11年新高。GPT-6发布催化AI算力板块，三大运营商资本开支增长约43%。<br><br>
      <strong>操作建议：</strong>①中国移动：GPT-6催化算力需求，可继续持有或逢回调加仓；②银行高股息底仓持有不动，一季报窗口是重要观察期；③中国海油：美伊若达成协议油价或回落，关注谈判进展；④长江电力、中国核电长期持有，AI用电逻辑确定；⑤宁德时代：超级科技日（4月21日）前关注预热行情。
    </div>
  </div>
  </div>
</div>

<!-- TAB 1: 国内外新闻 -->
<div class="tab-panel" id="panel-1">
  <div class="inner">
  <div class="section-title">🌍 国内外新闻</div>
  <div class="sub-section">
    <div class="sub-title">国际要闻</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-energy">地缘</span>美伊接近达成框架性协议，全球地缘风险大幅降温</div>
      <div class="card-body">央视记者4月15日获悉，美伊谈判代表正逐步接近达成结束冲突的框架性协议。特朗普表示"很有可能"在4月下旬与伊朗达成协议。以色列与黎巴嫩启动为期10天临时停火。全球风险偏好大幅改善，油价承压，美股纳指再创历史新高。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">政策</span>特朗普：4月下旬或与伊朗达成协议</div>
      <div class="card-body">特朗普在白宫记者会上表示，美国与伊朗"很有可能"在4月下旬达成框架协议。若协议达成，将结束持续数月的地区紧张局势，全球能源供应风险将显著下降。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">科技</span>美股纳指十连阳创历史新高，科技股强势</div>
      <div class="card-body">4月16日美股纳斯达克实现连续第十个交易日上涨，创下自2023年以来的最长连涨纪录，标普500逼近7000点大关。科技股表现强势，算力巨头携手冲高，GPT-6发布持续催化AI板块。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">国内要闻</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">宏观</span>A股强势延续：创业板涨3.17%创近11年新高</div>
      <div class="card-body">4月16日A股收盘：上证指数4055.55(+0.70%)；深证成指14796.33(+2.05%)；创业板指3626.27(+3.17%)，创2015年6月以来近11年新高！两市成交约23400亿元，超4300只个股上涨。AI与新能源主线集体爆发。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">市场</span>宁德时代跃居A股总市值第三</div>
      <div class="card-body">宁德时代4月16日大涨，市值跃升至A股第三。公司宣布将于4月21日举办"超级科技日"，预计展示全固态电池阶段性成果及麒麟电池迭代技术。新能源产业链4-5月排产同比增6成，行业景气度持续上行。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">政策</span>港股同步大涨，恒指涨1.72%收复两万六</div>
      <div class="card-body">4月16日港股收盘：恒生指数26394.26(+1.72%)，恒生科技指数6201.85(+2.55%)。南向资金净买入约85亿港元，科技股领涨，美团、小米、阿里巴巴涨幅显著。</div>
    </div>
  </div>
  </div>
</div>

<!-- TAB 2: AI前沿 -->
<div class="tab-panel" id="panel-2">
  <div class="inner">
  <div class="section-title">🤖 AI前沿</div>
  <div class="sub-section">
    <div class="sub-title">AI大模型动态</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">GPT-6</span>OpenAI发布GPT-6，200万Token上下文+多模态能力全面升级</div>
      <div class="card-body">OpenAI正式发布GPT-6模型，核心升级包括：①上下文窗口扩展至200万Token；②多模态能力增强，支持视频理解与生成长达10分钟；③推理能力显著提升，数学与代码任务准确率提高40%。GPT-6的发布进一步确认AI算力需求高增趋势，利好算力云、液冷散热、光模块等产业链。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">算力</span>三大运营商2026年资本开支合计增长约43%</div>
      <div class="card-body">中国移动、中国电信、中国联通2026年资本开支预算合计增长约43%，主要用于AI算力基础设施建设。中国移动算力云收入增速超50%，GPT-6发布是最核心催化剂。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">AI产业应用</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-chip">液冷</span>液冷散热成为数据中心标配，订单能见度超12个月</div>
      <div class="card-body">GPT-6 200万Token上下文对算力密度要求极高，液冷散热成为数据中心标配。光迅科技、中际旭创等光模块龙头订单能见度超12个月，行业景气度持续上行。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">电力</span>AI用电需求高增，核电、水电受益逻辑强化</div>
      <div class="card-body">AI数据中心用电量呈指数级增长，长江电力、中国核电作为基荷电源最受益。中国核电未来5年装机增速保持10%+，中金DCF测算存在约30%低估空间。</div>
    </div>
  </div>
  </div>
</div>

<!-- TAB 3: 全球市场 -->
<div class="tab-panel" id="panel-3">
  <div class="inner">
  <div class="section-title">🌐 全球市场</div>

  <div class="sub-section">
    <div class="sub-title">A股 · 港股</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">A股</span>创业板涨3.17%创近11年新高，AI与新能源主线爆发</div>
      <div class="card-body">
        <strong>4月16日收盘：</strong><br>
        • 上证指数：4055.55 <span class="up">+0.70%</span><br>
        • 深证成指：14796.33 <span class="up">+2.05%</span><br>
        • 创业板指：3626.27 <span class="up">+3.17%</span>（创2015年6月以来近11年新高！）<br>
        • 两市成交：约23400亿元<br>
        • 涨跌分布：超4300只个股上涨<br><br>
        <strong>板块表现：</strong>AI算力、新能源、半导体领涨；银行板块整体微跌。
      </div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">港股</span>恒指涨1.72%收复两万六，科技股领涨</div>
      <div class="card-body">
        <strong>4月16日收盘：</strong><br>
        • 恒生指数：26394.26 <span class="up">+1.72%</span><br>
        • 恒生科技指数：6201.85 <span class="up">+2.55%</span><br>
        • 南向资金：净买入约85亿港元<br><br>
        <strong>领涨个股：</strong>美团、小米、阿里巴巴涨幅显著。
      </div>
    </div>
  </div>

  <div class="sub-section">
    <div class="sub-title">美股 · 欧股</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">美股</span>纳指十连阳创历史新高，科技股强势</div>
      <div class="card-body">
        <strong>4月16日收盘：</strong><br>
        • 纳斯达克：十连阳 <span class="up">创历史新高</span><br>
        • 标普500：逼近7000点大关<br>
        • 道指：同步上涨<br><br>
        <strong>核心驱动：</strong>GPT-6发布催化AI板块，算力巨头携手冲高。这是纳指自2023年以来的最长连涨纪录。
      </div>
    </div>
  </div>

  <div class="sub-section">
    <div class="sub-title">大宗商品 · 外汇</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-energy">原油</span>WTI原油约$93，美伊和谈预期压制油价</div>
      <div class="card-body">
        <strong>当前油价：</strong>WTI原油约<span class="neutral">$93</span>（美伊和谈预期）<br><br>
        美伊若达成框架协议，高盛预计布伦特原油可能回落至$75-80区间。中国海油桶油成本约$28，当前桶油利润约$65，盈利依然可观。
      </div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">黄金</span>黄金高位震荡，AU9999约1035-1043元/克</div>
      <div class="card-body">
        <strong>当前金价：</strong>AU9999约<span style="color:#f0b429">1035-1043元/克</span><br><br>
        黄金处于历史高位区间，美伊和谈若达成可能带来短期回调压力。
      </div>
    </div>
  </div>
  </div>
</div>
'''

# 保存第一部分
with open('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/老盛的每日快讯/WorkBuddy版/老盛早知道_20260417.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("第一部分已保存")
