#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成老盛早知道 2026年4月17日 HTML文件
"""

html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>老盛早知道 - 2026年4月17日</title>
<style>
:root {
  --bg-primary:#0d1117;--bg-secondary:#161b22;--bg-card:#1c2333;--bg-hover:#21273a;
  --accent:#00d4ff;--accent-dim:rgba(0,212,255,0.15);--accent-border:rgba(0,212,255,0.35);
  --green:#3fb950;--red:#f85149;--yellow:#d29922;--purple:#bc8cff;--orange:#ffa657;
  --text-primary:#e6edf3;--text-secondary:#8b949e;--text-muted:#6e7681;
  --border:rgba(48,54,61,0.8);--radius:10px;--radius-sm:8px;
}
* { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family:-apple-system,'SF Pro Text','PingFang SC','Noto Sans SC',sans-serif;
  background:var(--bg-primary); color:var(--text-primary); line-height:1.7;
  min-height:100vh;
  background-image:
    radial-gradient(ellipse 80% 40% at 50% -5%, rgba(0,80,160,0.14) 0%, transparent 60%),
    repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,212,255,0.008) 3px, rgba(0,212,255,0.008) 4px);
}
.header {
  background: linear-gradient(180deg, #080e18 0%, #0a1422 100%);
  border-bottom: 1px solid rgba(0,212,255,0.18);
  position: relative; z-index: 100;
  box-shadow: 0 2px 40px rgba(0,0,0,0.7), 0 1px 0 rgba(0,212,255,0.12);
}
.header::before {
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  background:linear-gradient(90deg,transparent 0%,var(--accent) 25%,var(--purple) 75%,transparent 100%);
  box-shadow:0 0 18px var(--accent);
}
.header-inner { max-width:1200px; margin:0 auto; padding:22px 40px 0; }
.header-top {
  display:grid; grid-template-columns:72px 1fr auto;
  align-items:center; gap:22px; padding-bottom:24px;
}
.brand-icon {
  width:72px; height:72px;
  background:linear-gradient(145deg,#0a1e35 0%,#0d2040 60%,#091828 100%);
  border:1px solid rgba(0,212,255,0.38); border-radius:18px;
  display:flex; align-items:center; justify-content:center;
  box-shadow:0 0 28px rgba(0,212,255,0.32),0 0 8px rgba(0,212,255,0.12),inset 0 1px 0 rgba(255,255,255,0.08);
  flex-shrink:0; position:relative; overflow:hidden; align-self:center;
}
.brand-icon svg { width:40px; height:40px; }
.brand-title { font-size:26px; font-weight:700; letter-spacing:2px; color:var(--text-primary); }
.brand-title span { color:var(--accent); }
.header-meta { display:flex; flex-direction:column; align-items:flex-end; gap:8px; flex-shrink:0; padding-left:20px; border-left:1px solid rgba(0,212,255,0.1); }
.hm-date { font-size:17px; font-weight:600; color:var(--accent); letter-spacing:1px; }
.hm-sub { font-size:12px; color:var(--text-muted); display:flex; align-items:center; gap:8px; }
.tab-bar { display:flex; gap:10px; border-top:1px solid var(--border); padding:14px 0; overflow-x:auto; }
.tab-btn { padding:10px 20px; border-radius:var(--radius-sm); border:1px solid transparent; background:transparent; color:var(--text-secondary); font-size:14px; font-weight:500; cursor:pointer; white-space:nowrap; transition:all 0.2s; }
.tab-btn:hover { color:var(--text-primary); background:var(--bg-hover); }
.tab-btn.active { background:var(--accent-dim); color:var(--accent); border-color:var(--accent-border); box-shadow:0 0 12px rgba(0,212,255,0.15); }
.tab-panel { display: none; animation: fadeIn 0.3s ease; }
.tab-panel.active { display:block; }
.tab-panel .inner { padding-top: 32px; padding-bottom: 32px; }
@keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:translateY(0); } }
.inner { max-width:1200px; margin:0 auto; padding:0 40px; }
.section-title { font-size:18px; font-weight:700; color:var(--accent); margin-bottom:20px; padding-bottom:10px; border-bottom:1px solid var(--border); display:flex; align-items:center; gap:10px; }
.sub-section { margin-bottom:28px; }
.sub-title { font-size:14px; font-weight:600; color:var(--text-secondary); margin-bottom:14px; padding-left:12px; border-left:3px solid var(--accent); }
.card { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:18px; margin-bottom:14px; transition:all 0.2s; }
.card:hover { border-color:rgba(0,212,255,0.25); transform:translateY(-1px); box-shadow:0 4px 20px rgba(0,0,0,0.3); }
.card-title { font-size:15px; font-weight:600; color:var(--text-primary); margin-bottom:10px; display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
.card-body { font-size:14px; color:var(--text-secondary); line-height:1.8; }
.tag { display:inline-flex; align-items:center; padding:3px 10px; border-radius:4px; font-size:11px; font-weight:600; }
.tag-finance { background:rgba(0,212,255,0.12); color:var(--accent); }
.tag-policy { background:rgba(63,185,80,0.12); color:var(--green); }
.tag-energy { background:rgba(242,201,76,0.12); color:var(--yellow); }
.tag-ai { background:rgba(188,140,255,0.12); color:var(--purple); }
.tag-chip { background:rgba(255,166,87,0.12); color:var(--orange); }
.hot-bar { background:linear-gradient(90deg, rgba(0,212,255,0.08), rgba(188,140,255,0.08)); border:1px solid var(--accent-border); border-radius:var(--radius-sm); padding:14px 18px; font-size:14px; color:var(--text-secondary); margin-bottom:20px; }
.hot-bar strong { color:var(--accent); }
.stock-card { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:16px 18px; margin-bottom:14px; }
.stock-header { display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; margin-bottom:12px; }
.stock-name { font-size:16px; font-weight:700; color:var(--text-primary); }
.stock-code { font-size:12px; color:var(--text-muted); margin-left:8px; }
.stock-price-area { display:flex; align-items:center; gap:12px; margin-left:auto; }
.stock-price { font-size:20px; font-weight:700; }
.stock-price.up { color:var(--red); }
.stock-price.down { color:var(--green); }
.stock-price.neutral { color:var(--accent); }
.stock-change { font-size:12px; padding:3px 8px; border-radius:4px; background:var(--bg-hover); }
.stock-change.up { color:var(--red); background:rgba(248,81,73,0.12); }
.stock-change.down { color:var(--green); background:rgba(63,185,80,0.12); }
.stock-change.neutral { color:var(--text-muted); }
.stock-bullets { list-style:none; padding:0; margin:0; }
.stock-bullets li { position:relative; padding-left:16px; margin-bottom:8px; font-size:13.5px; color:var(--text-secondary); line-height:1.7; }
.stock-bullets li::before { content:"•"; position:absolute; left:0; color:var(--accent); font-weight:bold; }
.sentiment-bar-wrap { margin-bottom:14px; }
.sentiment-label { display:flex; justify-content:space-between; font-size:13px; color:var(--text-secondary); margin-bottom:6px; }
.sentiment-bar { height:8px; background:var(--bg-hover); border-radius:4px; overflow:hidden; }
.sentiment-fill { height:100%; background:linear-gradient(90deg,var(--green),var(--accent)); border-radius:4px; transition:width 0.5s ease; }
.summary-card { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:20px; margin-bottom:20px; }
.summary-card p { margin-bottom:14px; font-size:14px; color:var(--text-secondary); line-height:1.9; }
.summary-card p:last-child { margin-bottom:0; }
.summary-card strong { color:var(--text-primary); }
.footer { text-align:center; padding:30px 20px; font-size:12px; color:var(--text-muted); border-top:1px solid var(--border); margin-top:20px; }
.up { color:var(--red); }
.down { color:var(--green); }
.neutral { color:var(--accent); }
@media(max-width:768px) {
  .inner { padding:0 16px; }
  .header-inner { padding:16px 16px 0; }
  .header-top { grid-template-columns:48px 1fr; gap:12px; padding-bottom:16px; }
  .brand-icon { width:48px; height:48px; border-radius:12px; }
  .brand-icon svg { width:28px; height:28px; }
  .brand-title { font-size:18px; }
  .header-meta { border-left:none; padding-left:0; flex-direction:row; flex-wrap:wrap; align-items:center; gap:6px; grid-column:1/-1; padding-top:0; }
  .hm-date { font-size:15px; letter-spacing:1px; }
  .hm-sub { font-size:10px; }
  .tab-bar { padding:10px 0; gap:6px; }
  .tab-btn { padding:8px 14px; font-size:13px; }
  .card { padding:14px; }
  .stock-header { flex-direction:column; align-items:flex-start; }
  .stock-price-area { margin-left:0; margin-top:8px; }
}
</style>
</head>
<body>
<header class="header">
  <div class="header-inner">
    <div class="header-top">
      <div class="brand-icon">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 2L2 7L12 12L22 7L12 2Z" fill="url(#grad1)" stroke="#00d4ff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M2 17L12 22L22 17" stroke="#00d4ff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M2 12L12 17L22 12" stroke="#00d4ff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <defs>
            <linearGradient id="grad1" x1="2" y1="2" x2="22" y2="22" gradientUnits="userSpaceOnUse">
              <stop stop-color="#00d4ff" stop-opacity="0.3"/>
              <stop offset="1" stop-color="#bc8cff" stop-opacity="0.1"/>
            </linearGradient>
          </defs>
        </svg>
      </div>
      <div class="brand-title">老盛<span>早知道</span></div>
      <div class="header-meta">
        <div class="hm-date">2026 / 04 / 17</div>
        <div class="hm-sub">
          <span>星期五</span>
          <span class="sep">·</span>
          <span>第 24 期</span>
        </div>
      </div>
    </div>
    <div class="tab-bar">
      <button class="tab-btn active" onclick="switchTab(0)">📋 要点速览</button>
      <button class="tab-btn" onclick="switchTab(1)">🌍 全球市场</button>
      <button class="tab-btn" onclick="switchTab(2)">📰 国内外新闻</button>
      <button class="tab-btn" onclick="switchTab(3)">🤖 AI前沿</button>
      <button class="tab-btn" onclick="switchTab(4)">💡 价值投资风向</button>
      <button class="tab-btn" onclick="switchTab(5)">🏦 关注标的</button>
      <button class="tab-btn" onclick="switchTab(6)">📊 今日总结</button>
    </div>
  </div>
</header>

<div class="tab-panel active" id="panel-0">
  <div class="inner">
    <div class="section-title">📋 今日要点速览</div>
    <div class="hot-bar"><strong>🔥 今日最重磅：</strong>美伊接近达成框架性协议，全球地缘风险大幅降温！特朗普表示"很有可能"在4月下旬与伊朗达成协议。美股纳指十连阳再创历史新高，A股创业板指涨3.17%创近11年新高！</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-energy">地缘</span>美伊框架协议即将达成</div>
      <div class="card-body">央视记者4月15日获悉，美伊谈判代表正逐步接近达成结束冲突的框架性协议。特朗普表示"很有可能"在4月下旬与伊朗达成协议。以色列与黎巴嫩启动为期10天临时停火。全球风险偏好大幅改善。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">A股</span>创业板涨3.17%创近11年新高</div>
      <div class="card-body">4月16日A股收盘：上证指数4055.55(+0.70%)；深证成指14796.33(+2.05%)；创业板指3626.27(+3.17%)，创2015年6月以来近11年新高！两市成交约23400亿元，超4300只个股上涨。AI与新能源主线集体爆发。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">美股</span>纳指十连阳创历史新高</div>
      <div class="card-body">4月16日美股纳斯达克实现连续第十个交易日上涨，创下自2023年以来的最长连涨纪录，标普500逼近7000点大关。科技股表现强势，算力巨头携手冲高，GPT-6发布持续催化AI板块。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-chip">新能源</span>宁德时代超级科技日4月21日举办</div>
      <div class="card-body">宁德时代宣布将于4月21日举办"超级科技日"，这将是公司成立以来技术密度最高的一场发布会，预计将展示全固态电池阶段性成果及麒麟电池迭代技术。新能源产业链4-5月排产同比增6成。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">港股</span>恒指涨1.72%收复两万六</div>
      <div class="card-body">4月16日港股收盘：恒生指数26394.26(+1.72%)，恒生科技指数6201.85(+2.55%)。南向资金净买入约85亿港元，科技股领涨，美团、小米、阿里巴巴涨幅显著。</div>
    </div>
  </div>
</div>

<div class="tab-panel" id="panel-1">
  <div class="inner">
    <div class="section-title">🌍 全球市场</div>
    <div class="sub-section">
      <div class="sub-title">A股 · 4月16日收盘</div>
      <div class="card">
        <div class="card-title">📊 A股主要指数</div>
        <div class="card-body">
          <table style="width:100%;border-collapse:collapse;font-size:14px;">
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">上证指数</td><td style="padding:10px;text-align:right;font-weight:600;" class="up">4055.55</td><td style="padding:10px;text-align:right;" class="up">+0.70%</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">深证成指</td><td style="padding:10px;text-align:right;font-weight:600;" class="up">14796.33</td><td style="padding:10px;text-align:right;" class="up">+2.05%</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">创业板指</td><td style="padding:10px;text-align:right;font-weight:600;" class="up">3626.27</td><td style="padding:10px;text-align:right;" class="up">+3.17% 创11年新高</td></tr>
            <tr><td style="padding:10px;">两市成交额</td><td style="padding:10px;text-align:right;font-weight:600;" colspan="2" class="neutral">约23400亿元</td></tr>
          </table>
        </div>
      </div>
      <div class="card">
        <div class="card-title">📈 市场特征</div>
        <div class="card-body">超4300只个股上涨，AI与新能源主线集体爆发，宁德时代跃居A股总市值第三。市场情绪高涨，创业板创2015年6月以来近11年新高。</div>
      </div>
    </div>
    <div class="sub-section">
      <div class="sub-title">港股 · 4月16日收盘</div>
      <div class="card">
        <div class="card-title">📊 港股主要指数</div>
        <div class="card-body">
          <table style="width:100%;border-collapse:collapse;font-size:14px;">
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">恒生指数</td><td style="padding:10px;text-align:right;font-weight:600;" class="up">26394.26</td><td style="padding:10px;text-align:right;" class="up">+1.72%</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">恒生科技指数</td><td style="padding:10px;text-align:right;font-weight:600;" class="up">6201.85</td><td style="padding:10px;text-align:right;" class="up">+2.55%</td></tr>
            <tr><td style="padding:10px;">南向资金净买入</td><td style="padding:10px;text-align:right;font-weight:600;" colspan="2" class="up">约85亿港元</td></tr>
          </table>
        </div>
      </div>
    </div>
    <div class="sub-section">
      <div class="sub-title">美股 · 4月16日收盘</div>
      <div class="card">
        <div class="card-title">📊 美股主要指数</div>
        <div class="card-body">
          <table style="width:100%;border-collapse:collapse;font-size:14px;">
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">道琼斯</td><td style="padding:10px;text-align:right;font-weight:600;" class="up">持续上涨</td><td style="padding:10px;text-align:right;" class="up">—</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">纳斯达克</td><td style="padding:10px;text-align:right;font-weight:600;" class="up">十连阳</td><td style="padding:10px;text-align:right;" class="up">创历史新高</td></tr>
            <tr><td style="padding:10px;">标普500</td><td style="padding:10px;text-align:right;font-weight:600;" class="up">逼近7000点</td><td style="padding:10px;text-align:right;" class="up">—</td></tr>
          </table>
        </div>
      </div>
      <div class="card">
        <div class="card-title">📈 市场特征</div>
        <div class="card-body">纳斯达克实现连续第十个交易日上涨，创下自2023年以来的最长连涨纪录。科技股表现强势，算力巨头携手冲高，GPT-6发布持续催化AI板块。</div>
      </div>
    </div>
    <div class="sub-section">
      <div class="sub-title">大宗商品</div>
      <div class="card">
        <div class="card-title">📊 大宗商品行情</div>
        <div class="card-body">
          <table style="width:100%;border-collapse:collapse;font-size:14px;">
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">WTI原油</td><td style="padding:10px;text-align:right;font-weight:600;" class="neutral">约$93</td><td style="padding:10px;text-align:right;color:var(--yellow)">美伊和谈预期</td></tr>
            <tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;">布伦特原油</td><td style="padding:10px;text-align:right;font-weight:600;" class="neutral">约$93-95</td><td style="padding:10px;text-align:right;color:var(--yellow)">—</td></tr>
            <tr><td style="padding:10px;">黄金(AU9999)</td><td style="padding:10px;text-align:right;font-weight:600;color:#f0b429">约1035-1043元/克</td><td style="padding:10px;text-align:right;color:var(--red)">历史高位区间</td></tr>
          </table>
        </div>
      </div>
      <div class="card">
        <div class="card-title">📊 今日市场综评（4月17日）</div>
        <div class="card-body">昨日A股延续强势：创业板指大涨3.17%创近11年新高（3626.27点），上证站稳4055点，两市成交约23400亿元，超4300只个股上涨。AI与新能源主线集体爆发，宁德时代跃居A股总市值第三。港股同步大涨，恒指涨1.72%收复两万六。美股纳指实现十连阳再创历史新高。美伊接近达成框架性协议，全球地缘风险大幅降温。今日A股大概率延续强势。</div>
      </div>
    </div>
  </div>
</div>
'''

# 写入文件第一部分
with open('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/老盛的每日快讯/WorkBuddy版/老盛早知道_20260417.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("第一部分写入完成")
