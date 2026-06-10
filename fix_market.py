#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正老盛早知道_20260610.html - Part1: Header + Tab0 summary cards"""

file_path = "/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260610.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# 1. Header tickers
old1 = """            <span class="t-label">上证</span>
            <span class="t-val">3987.26</span>
            <span class="t-chg">+0.71%</span>
          </div>
          <div class="hm-ticker">
            <span class="t-label">道指</span>
            <span class="t-val">51142.30</span>
            <span class="t-chg">+0.54%</span>
          </div>
          <div class="hm-ticker">
            <span class="t-label">黄金</span>
            <span class="t-val">$4318</span>
            <span class="t-chg">+0.77%</span>"""
new1 = """            <span class="t-label">上证</span>
            <span class="t-val">3959</span>
            <span class="t-chg down">-1.70%</span>
          </div>
          <div class="hm-ticker">
            <span class="t-label">道指</span>
            <span class="t-val">50866</span>
            <span class="t-chg down">-1.35%</span>
          </div>
          <div class="hm-ticker">
            <span class="t-label">黄金</span>
            <span class="t-val">$4285</span>
            <span class="t-chg down">-1.34%</span>"""
if old1 in html:
    html = html.replace(old1, new1)
    changes.append("✓ Header tickers")
else:
    print("✗ Header tickers NOT FOUND")

# 2. Summary cards
old2 = """        <div class="summary-card-title">上证指数</div>
        <div class="summary-card-value">3987.26 <span class="summary-card-change up">+0.71%</span></div>
        <div class="summary-card-desc">结构性行情凸显，银行保险电力领涨</div>
      </div>
    </div>
    <div class="summary-card-blue">
      <div class="summary-card-icon">🏦</div>
      <div class="summary-card-content">
        <div class="summary-card-title">恒生指数</div>
        <div class="summary-card-value">24938.75 <span class="summary-card-tag">+1.14%</span></div>
        <div class="summary-card-desc">高股息板块反弹，南向资金净买入87.62亿</div>
      </div>
    </div>
    <div class="summary-card-yellow">
      <div class="summary-card-icon">💰</div>
      <div class="summary-card-content">
        <div class="summary-card-title">纳斯达克</div>
        <div class="summary-card-value">25984.20 <span class="summary-card-tag">+1.07%</span></div>
        <div class="summary-card-desc">科技股企稳反弹，英伟达AMD领涨芯片板块</div>
      </div>
    </div>
    <div class="summary-card-green">
      <div class="summary-card-icon">🤖</div>
      <div class="summary-card-content">
        <div class="summary-card-title">国际金价</div>
        <div class="summary-card-value">$4318/oz <span class="summary-card-tag">+0.77%</span></div>
        <div class="summary-card-desc">央行购金+地缘避险，高位震荡偏强</div>"""
new2 = """        <div class="summary-card-title">上证指数</div>
        <div class="summary-card-value">3959.34 <span class="summary-card-change down">-1.70%</span></div>
        <div class="summary-card-desc">失守4000点关口，全球风险资产承压</div>
      </div>
    </div>
    <div class="summary-card-blue">
      <div class="summary-card-icon">🏦</div>
      <div class="summary-card-content">
        <div class="summary-card-title">恒生指数</div>
        <div class="summary-card-value">24657.06 <span class="summary-card-tag">-1.22%</span></div>
        <div class="summary-card-desc">科技股集体回调，南向资金逆势净买入113亿</div>
      </div>
    </div>
    <div class="summary-card-yellow">
      <div class="summary-card-icon">💰</div>
      <div class="summary-card-content">
        <div class="summary-card-title">纳斯达克</div>
        <div class="summary-card-value">25709.43 <span class="summary-card-tag">-4.18%</span></div>
        <div class="summary-card-desc">芯片股遭大规模抛售，费城半导体指数跌超10%</div>
      </div>
    </div>
    <div class="summary-card-green">
      <div class="summary-card-icon">🤖</div>
      <div class="summary-card-content">
        <div class="summary-card-title">国际金价</div>
        <div class="summary-card-value">$4285/oz <span class="summary-card-tag">-1.34%</span></div>
        <div class="summary-card-desc">非农超预期推升加息预期，金价承压回落</div>"""
if old2 in html:
    html = html.replace(old2, new2)
    changes.append("✓ Summary cards")
else:
    print("✗ Summary cards NOT FOUND")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\n已完成替换:")
for c in changes:
    print(c)
if not changes:
    print("没有任何替换成功！")
