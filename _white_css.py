#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将白底CSS应用到老盛早知道报告
"""

# 白底新闻风格CSS
WHITE_CSS = ''':root {
    --bg-primary: #ffffff;
    --bg-secondary: #f9fafb;
    --bg-card: #ffffff;
    --bg-hover: #f3f4f6;
    --accent: #1e40af;
    --accent-dim: rgba(30,64,175,0.1);
    --accent-border: rgba(30,64,175,0.25);
    --green: #16a34a;
    --red: #dc2626;
    --yellow: #d97706;
    --purple: #7c3aed;
    --orange: #ea580c;
    --text-primary: #111827;
    --text-secondary: #4b5563;
    --text-muted: #9ca3af;
    --border: #e5e7eb;
    --radius: 12px;
    --radius-sm: 8px;
}
* { margin:0; padding:0; box-sizing:border-box; }
body {
    font-family: -apple-system, 'SF Pro Text', 'PingFang SC', 'Noto Sans SC', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    font-size: 15px;
    line-height: 1.7;
    min-height: 100vh;
}
.header {
    background: linear-gradient(180deg, #ffffff 0%, #f9fafb 100%);
    border-bottom: 1px solid var(--border);
    position: sticky; top: 0; z-index: 100;
    box-shadow: 0 2px 20px rgba(0,0,0,0.06);
}
.header::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, var(--accent) 0%, var(--purple) 100%);
}
.inner { max-width: 1200px; margin: 0 auto; padding: 0 40px; }
.header-inner { max-width: 1200px; margin: 0 auto; padding: 22px 40px 0; }
.header-top { display: grid; grid-template-columns: 72px 1fr auto; align-items: center; gap: 22px; padding-bottom: 16px; }
.brand-icon {
    width: 72px; height: 72px;
    background: linear-gradient(145deg, #eff6ff 0%, #dbeafe 100%);
    border: 1px solid rgba(30,64,175,0.2); border-radius: 18px;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 12px rgba(30,64,175,0.15);
    flex-shrink: 0; position: relative; overflow: hidden; align-self: center;
}
.brand-icon::after { content: ''; position: absolute; inset: 0; border-radius: 18px; background: linear-gradient(135deg, rgba(30,64,175,0.05) 0%, transparent 55%); pointer-events: none; }
.brand-icon svg { width:36px; height:36px; position:relative; z-index:1; }
.brand-title { display:flex; flex-direction:column; justify-content:center; gap:6px; line-height:1; }
.brand-en-row { display:flex; align-items:center; gap:8px; }
.brand-en { font-size: 9.5px; font-weight: 600; letter-spacing: 2.5px; color: var(--accent); opacity: 0.6; text-transform: uppercase; font-family: 'SF Mono','Fira Code','Consolas',monospace; }
.brand-main-row { display: flex; align-items: center; }
.brand-signal { position: relative; display: inline-flex; align-items: center; cursor: default; padding: 4px 0; }
.brand-signal::before { content: ''; position: absolute; inset: -8px -16px; border-radius: 10px; background: radial-gradient(ellipse at center, rgba(30,64,175,0.04) 0%, transparent 70%); animation: signal-pulse 5s ease-in-out infinite; pointer-events: none; }
.brand-name { font-size: 28px; font-weight: 900; letter-spacing: 5px; color: var(--text-primary); position: relative; }
.brand-sep { position: relative; width: 2px; height: 22px; background: rgba(30,64,175,0.2); margin: 0 10px; border-radius: 1px; align-self: center; overflow: visible; }
.brand-sep::after { content: ''; position: absolute; left: -1.5px; width: 5px; height: 5px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 8px rgba(30,64,175,0.6), 0 0 20px rgba(30,64,175,0.2); animation: sep-slide 3s ease-in-out infinite; }
.brand-zaodao { font-size: 28px; font-weight: 300; letter-spacing: 5px; color: var(--accent); }
@keyframes signal-pulse { 0%, 100% { opacity: 0.4; transform: scale(1); } 50% { opacity: 1; transform: scale(1.02); } }
@keyframes sep-slide { 0% { top: 0; opacity: 0; } 15% { opacity: 1; } 50% { top: calc(100% - 5px); opacity: 1; } 85% { opacity: 1; } 100% { top: 0; opacity: 0; } }
.brand-tag { font-size: 11px; font-weight: 400; letter-spacing: 2px; color: var(--text-secondary); margin-left: 12px; opacity: 0.5; white-space: nowrap; }
.brand-subtitle { font-size: 11.5px; color: var(--text-muted); letter-spacing: 0.5px; display:flex; align-items:center; margin-top:3px; }
.brand-subtitle .dot { color: var(--accent); opacity: 0.3; margin: 0 7px; }
.header-meta { display: flex; flex-direction: column; align-items: flex-end; gap: 8px; flex-shrink: 0; padding-left: 20px; border-left: 1px solid var(--border); }
.hm-date { font-size: 22px; font-weight: 700; letter-spacing: 2px; color: var(--accent); line-height: 1; font-family: 'SF Mono','Fira Code','Consolas',monospace; }
.hm-sub { font-size: 11px; color: var(--text-muted); display: flex; align-items: center; gap: 6px; flex-wrap: nowrap; overflow: hidden; }
.hm-sub span { white-space: nowrap; flex-shrink: 0; }
.hm-sub span:last-child { flex-shrink: 1; overflow: hidden; text-overflow: ellipsis; }
.hm-sub .sep { color: var(--border); }
.hm-tickers { display:flex; gap:8px; align-items:stretch; }
.hm-ticker { display: flex; flex-direction: column; align-items: center; background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 6px; padding: 5px 12px; min-width: 64px; gap: 1px; }
.hm-ticker .t-label { font-size: 9.5px; color: var(--text-muted); letter-spacing: 0.5px; font-family: 'SF Mono','Fira Code','Consolas',monospace; }
.hm-ticker .t-val { font-size: 15px; font-weight: 700; line-height: 1.2; }
.hm-ticker .t-chg { font-size: 10px; font-weight: 600; font-family: 'SF Mono','Fira Code','Consolas',monospace; }
.up   { color: #dc2626; }
.down { color: #16a34a; }
.gold { color: #d97706; }
.neutral { color: var(--text-secondary); }
.live-dot { display: inline-block; width:7px; height:7px; background: var(--green); border-radius: 50%; box-shadow: 0 0 6px var(--green); animation: pulse 2s ease-in-out infinite; vertical-align: middle; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(0.7)} }
.tab-nav-wrap { max-width: 1200px; margin: 0 auto; padding: 0 40px; }
.tab-nav { display:flex; gap:2px; overflow-x:auto; scrollbar-width:none; background: var(--bg-secondary); border-radius: var(--radius-sm) var(--radius-sm) 0 0; border: 1px solid var(--border); border-bottom: none; }
.tab-nav::-webkit-scrollbar { display:none; }
.tab-btn { flex-shrink: 0; padding: 11px 20px; border: none; background: transparent; color: var(--text-secondary); font-size: 13.5px; font-weight: 500; cursor: pointer; border-radius: var(--radius-sm) var(--radius-sm) 0 0; transition: all 0.22s ease; white-space: nowrap; position: relative; font-family: inherit; letter-spacing: 0.3px; }
.tab-btn:hover { color:var(--text-primary); background:rgba(30,64,175,0.05); }
.tab-btn.active { color: var(--accent); background: #fff; font-weight: 700; }
.tab-btn.active::after { content: ''; position: absolute; bottom:0; left:8px; right:8px; height:2px; background: var(--accent); border-radius: 2px 2px 0 0; }
.tab-icon { margin-right:5px; font-size:13px; }
.tab-panel { display: none; animation: fadeIn 0.3s ease; }
.tab-panel.active { display:block; }
.tab-panel .inner { padding-top: 32px; padding-bottom: 12px; }
@keyframes fadeIn { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }
.section-title { font-size: 20px; font-weight: 700; color: var(--text-primary); margin-bottom: 24px; padding-bottom: 12px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 10px; }
.section-title::after { content:''; flex:1; height:1px; background: linear-gradient(90deg, var(--accent-border), transparent); }
.card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 20px 24px; margin-bottom: 16px; transition: all 0.2s ease; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.card:hover { border-color: var(--accent-border); box-shadow: 0 4px 16px rgba(0,0,0,0.08); transform: translateY(-1px); }
.card-title { font-size: 15px; font-weight: 600; color: var(--text-primary); margin-bottom: 8px; display:flex; align-items:flex-start; gap:10px; }
.card-body { font-size:14px; color:var(--text-secondary); line-height:1.75; }
.tag { display:inline-block; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:600; letter-spacing:0.5px; flex-shrink:0; margin-top:1px; }
.tag-finance { background:rgba(30,64,175,0.1); color:var(--accent); }
.tag-tech    { background:rgba(124,58,237,0.1); color:var(--purple); }
.tag-geo     { background:rgba(234,88,12,0.1); color:var(--orange); }
.tag-policy  { background:rgba(22,163,74,0.1); color:var(--green); }
.tag-ai      { background:rgba(124,58,237,0.1); color:var(--purple); }
.tag-chip    { background:rgba(30,64,175,0.1); color:var(--accent); }
.tag-robot   { background:rgba(234,88,12,0.1); color:var(--orange); }
.tag-app     { background:rgba(22,163,74,0.1); color:var(--green); }
.tag-energy  { background:rgba(217,119,6,0.1); color:var(--yellow); }
.highlight-grid { display: grid; grid-template-columns: repeat(auto-fill,minmax(320px,1fr)); gap: 14px; margin-bottom: 28px; }
.highlight-item { background: var(--bg-card); border:1px solid var(--border); border-left: 3px solid var(--accent); border-radius: var(--radius); padding: 14px 18px; display:flex; gap:12px; align-items:flex-start; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.03); }
.highlight-item:hover { border-left-color: var(--purple); box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
.highlight-num { font-size:20px; font-weight:800; color:var(--accent); line-height:1; flex-shrink:0; min-width:28px; }
.highlight-text { font-size:14px; color:var(--text-secondary); line-height:1.65; }
.highlight-text strong { color:var(--text-primary); }
.market-grid { display: grid; grid-template-columns: repeat(auto-fill,minmax(280px,1fr)); gap: 14px; margin-bottom: 20px; }
.market-block { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding:16px 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); }
.market-block h4 { font-size:12px; color:var(--text-muted); letter-spacing:1px; text-transform:uppercase; margin-bottom:12px; border-bottom: 1px solid var(--border); padding-bottom:8px; }
.market-row { display:flex; justify-content:space-between; align-items:center; padding:5px 0; border-bottom:1px solid var(--border); font-size:13.5px; }
.market-row:last-child { border-bottom:none; }
.market-name { color:var(--text-secondary); }
.market-val { font-weight:600; }
.sentiment-bar-wrap { margin:6px 0 14px; }
.sentiment-label { font-size:12px; color:var(--text-muted); margin-bottom:4px; display:flex; justify-content:space-between; }
.sentiment-bar { height:8px; background:var(--bg-secondary); border-radius:4px; overflow:hidden; border:1px solid var(--border); }
.sentiment-fill { height:100%; border-radius:4px; background:linear-gradient(90deg,var(--accent),var(--purple)); }
.laosheng-view {
    margin-top: 10px;
    padding: 10px 14px;
    background: linear-gradient(135deg, rgba(30,64,175,0.08), rgba(124,58,237,0.05));
    border-left: 3px solid var(--accent);
    border-radius: 0 8px 8px 0;
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.75;
    animation: lvFadeIn 0.5s ease-out;
}
.laosheng-view .lv-label {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-weight: 700;
    color: var(--accent);
    font-size: 13px;
    margin-right: 4px;
}
.laosheng-view .lv-label::before {
    content: '💬';
    font-size: 13px;
    animation: lvBounce 1.5s ease-in-out infinite;
}
@keyframes lvFadeIn {
    from { opacity: 0; transform: translateX(-8px); }
    to { opacity: 1; transform: translateX(0); }
}
@keyframes lvBounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-2px); }
}
.stock-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); padding:20px 24px; margin-bottom:14px; transition: all 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.stock-card:hover { border-color: var(--accent-border); box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
.stock-header { display:flex; align-items:center; gap:14px; margin-bottom:12px; flex-wrap:wrap; }
.stock-name { font-size:16px; font-weight:700; color:var(--text-primary); }
.stock-code { font-size:12px; color:var(--text-muted); background:var(--bg-secondary); padding:2px 8px; border-radius:4px; }
.stock-price-area { margin-left:auto; text-align:right; }
.stock-price { font-size:18px; font-weight:700; }
.stock-change { font-size:12px; margin-top:2px; }
.stock-bullets { list-style:none; padding:0; }
.stock-bullets li { font-size:13.5px; color:var(--text-secondary); padding:4px 0 4px 16px; position:relative; line-height:1.65; }
.stock-bullets li::before { content:'▸'; color:var(--accent); position:absolute; left:0; font-size:11px; top:6px; }
.summary-card { background: linear-gradient(135deg, #ffffff, #f9fafb); border:1px solid var(--accent-border); border-radius:var(--radius); padding:28px 32px; margin-bottom:20px; box-shadow: 0 4px 16px rgba(30,64,175,0.08); }
.summary-card p { color:var(--text-secondary); font-size:14.5px; line-height:1.9; margin-bottom:14px; }
.summary-card p:last-child { margin-bottom: 0; }
.summary-card strong { color:var(--accent); }
.alert-bar { background: rgba(220,38,38,0.05); border: 1px solid rgba(220,38,38,0.2); border-left:3px solid var(--red); border-radius:var(--radius); padding:14px 20px; margin-bottom:20px; font-size:13.5px; color:var(--text-secondary); line-height:1.75; }
.alert-bar strong { color:var(--red); }
.hot-bar { background: rgba(217,119,6,0.05); border: 1px solid rgba(217,119,6,0.2); border-left:3px solid var(--yellow); border-radius:var(--radius); padding:14px 20px; margin-bottom:20px; font-size:13.5px; color:var(--text-secondary); line-height:1.75; }
.hot-bar strong { color:var(--yellow); }
.good-bar { background: rgba(22,163,74,0.05); border: 1px solid rgba(22,163,74,0.2); border-left:3px solid var(--green); border-radius:var(--radius); padding:14px 20px; margin-bottom:20px; font-size:13.5px; color:var(--text-secondary); line-height:1.75; }
.good-bar strong { color:var(--green); }
.footer { text-align:center; padding:28px 40px; color:var(--text-muted); font-size:12px; border-top:1px solid var(--border); margin-top:8px; background: var(--bg-secondary); }
.footer span { color:var(--accent); }
.sub-section { margin-bottom: 28px; }
.sub-title { font-size: 13px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); margin-bottom: 14px; padding-left: 10px; border-left: 3px solid var(--accent); }
.stock-info-row { display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
.grid-4 { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; }
.grid-3 { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }
.grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:16px; }
.grid-auto { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:12px; }
@media (max-width:768px) {
    .header-inner, .tab-nav-wrap, .inner { padding-left: 16px; padding-right: 16px; }
    .header-inner { padding-top: 14px; }
    .tab-panel .inner { padding-top: 20px; padding-bottom: 8px; }
    .highlight-grid, .market-grid { grid-template-columns: 1fr; }
    .header-top { grid-template-columns: 48px 1fr; gap: 10px; padding-bottom: 14px; }
    .brand-icon { width: 42px; height: 42px; border-radius: 10px; flex-shrink: 0; }
    .brand-icon svg { width: 22px; height: 22px; }
    .brand-name { font-size: 20px; letter-spacing: 2px; }
    .brand-zaodao { font-size: 20px; letter-spacing: 2px; }
    .brand-sep { margin: 0 6px; height: 16px; }
    .brand-tag { font-size: 10px; margin-left: 6px; }
    .brand-subtitle { font-size: 11px; flex-wrap: wrap; }
    .brand-en { font-size: 9px; letter-spacing: 1.5px; }
    .brand-en-row { flex-wrap: wrap; gap: 4px; }
    .brand-main-row { flex-wrap: wrap; }
    .hm-tickers { display: none; }
    .header-meta { border-left: none; padding-left: 0; flex-direction: row; flex-wrap: wrap; align-items: center; gap: 6px; grid-column: 1 / -1; padding-top: 0; }
    .hm-date { font-size: 14px; }
    .hm-sub { font-size: 10px; }
    .live-dot { width: 5px; height: 5px; }
    .tab-nav-wrap { position: relative; }
    .tab-btn { padding: 12px 14px; font-size: 12px; }
    .tab-icon { font-size: 12px; }
    .card { padding: 14px 16px; box-shadow: 0 1px 4px rgba(0,0,0,0.05); }
    .card:hover { transform: none; }
    .card-title { font-size: 14px; gap: 8px; }
    .card-body { font-size: 13px; line-height: 1.7; }
    .alert-bar, .hot-bar, .good-bar { padding: 12px 14px; font-size: 13px; }
    .highlight-item { padding: 12px 14px; }
    .market-block { padding: 12px 14px; }
    .stock-card { padding: 14px 16px; }
    .stock-card:hover { transform: none; }
    .stock-header { flex-direction: column; align-items: flex-start; gap: 4px; }
    .stock-name { font-size: 15px; }
    .stock-code { font-size: 11px; }
    .stock-header .tag { font-size: 10px; padding: 1px 6px; }
    .stock-price-area { margin-left: 0; text-align: left; }
    .stock-price { font-size: 15px; }
    .stock-change { font-size: 11px; }
    .summary-card { padding: 18px 16px; }
    .sentiment-label { flex-direction: column; gap: 2px; font-size: 11px; }
    .section-title { font-size: 17px; margin-bottom: 18px; padding-bottom: 10px; }
    .sub-section { margin-bottom: 20px; }
    .card-body table { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; font-size: 12px !important; }
    .card-body table td { padding: 5px 8px !important; }
    .card-body table td, .card-body table th { overflow-wrap: break-word !important; word-break: normal !important; }
    .card-body table td.td-label { white-space: nowrap !important; }
    .card-body table td.td-val { white-space: normal !important; }
    .footer { padding: 20px 16px; padding-bottom: calc(20px + env(safe-area-inset-bottom, 0px)); }
    .grid-4 { grid-template-columns: repeat(2,1fr); gap: 10px; }
    .grid-3 { grid-template-columns: 1fr; gap: 12px; }
    .grid-2 { grid-template-columns: 1fr; gap: 12px; }
    .grid-auto { grid-template-columns: 1fr; gap: 10px; }
    .insurance-flow { flex-direction: column; gap: 8px; }
    .insurance-flow .flow-arrow { transform: rotate(90deg); font-size: 16px; }
    .insurance-flow .insurance-card { width: 100%; max-width: 280px; padding: 14px 16px; display: flex; align-items: center; gap: 12px; text-align: left; }
    .insurance-flow .insurance-card > div:first-child { font-size: 28px; margin-bottom: 0; }
    .insurance-flow .insurance-card > div:nth-child(2) { flex: 1; }
    .rate-compare { flex-wrap: wrap; justify-content: center; gap: 8px; }
    .rate-compare .big-num { font-size: 26px; letter-spacing: -1px; }
    .rate-compare > div { flex: 0 0 auto; }
    .topic-card { padding: 12px 14px; gap: 12px; }
    .topic-card > div:first-child { width: 40px; height: 40px; }
    .gold-price-header { flex-direction: column; align-items: flex-start; gap: 8px; }
    .gold-price-header > div:last-child { text-align: left; }
}
'''

# 继续添加更多CSS...
MORE_CSS = '''
/* ===== Tab 0 新样式 ===== */
.summary-cards-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-bottom: 28px;
}
.summary-card-green,
.summary-card-blue,
.summary-card-yellow,
.summary-card-red {
    border-radius: 14px;
    padding: 20px;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    gap: 16px;
    align-items: flex-start;
}
.summary-card-green:hover,
.summary-card-blue:hover,
.summary-card-yellow:hover,
.summary-card-red:hover {
    transform: translateY(-2px);
}
.summary-card-green {
    background: linear-gradient(135deg, rgba(22,163,74,0.08), rgba(22,163,74,0.02));
    border: 1px solid rgba(22,163,74,0.2);
    box-shadow: 0 4px 12px rgba(22,163,74,0.08);
}
.summary-card-blue {
    background: linear-gradient(135deg, rgba(30,64,175,0.08), rgba(30,64,175,0.02));
    border: 1px solid rgba(30,64,175,0.2);
    box-shadow: 0 4px 12px rgba(30,64,175,0.08);
}
.summary-card-yellow {
    background: linear-gradient(135deg, rgba(217,119,6,0.08), rgba(217,119,6,0.02));
    border: 1px solid rgba(217,119,6,0.2);
    box-shadow: 0 4px 12px rgba(217,119,6,0.08);
}
.summary-card-red {
    background: linear-gradient(135deg, rgba(220,38,38,0.08), rgba(220,38,38,0.02));
    border: 1px solid rgba(220,38,38,0.2);
    box-shadow: 0 4px 12px rgba(220,38,38,0.08);
}
.summary-card-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    flex-shrink: 0;
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.summary-card-content {
    flex: 1;
    min-width: 0;
}
.summary-card-title {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-muted);
    margin-bottom: 6px;
    letter-spacing: 0.5px;
}
.summary-card-value {
    font-size: 22px;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 6px;
    letter-spacing: -0.5px;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
}
.summary-card-change {
    font-size: 13px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
}
.summary-card-change.up {
    color: #dc2626;
    background: rgba(220,38,38,0.1);
}
.summary-card-change.down {
    color: #16a34a;
    background: rgba(22,163,74,0.1);
}
.summary-card-tag {
    font-size: 11px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
    background: rgba(217,119,6,0.1);
    color: #d97706;
}
.summary-card-desc {
    font-size: 12px;
    color: var(--text-muted);
    line-height: 1.6;
}
'''

print("白底CSS已定义")
