#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正 - Part3: Tab3 8个market-block"""

file_path = "/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260610.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# A股 market-block
old1 = """      <h4>🇨🇳 A股（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">上证指数</span><span class="market-val up">3987.26 +0.71%</span></div>
      <div class="market-row"><span class="market-name">深证成指</span><span class="market-val up">15082.45 +0.68%</span></div>
      <div class="market-row"><span class="market-name">创业板指</span><span class="market-val up">3884.62 +0.85%</span></div>
      <div class="market-row"><span class="market-name">科创50</span><span class="market-val up">涨1.12%</span></div>
      <div class="market-row"><span class="market-name">沪深300</span><span class="market-val up">涨0.94%</span></div>
      <div class="market-row"><span class="market-name">成交额</span><span class="market-val neutral" style="color:#f0b429;font-weight:700;">28562.40亿<span style="font-size:11px;"> (连续33日超2.5万亿)</span></span></div>
      <div class="market-row"><span class="market-name">涨跌家数</span><span class="market-val up">2865涨/2624跌</span></div>
      <div class="market-row"><span class="market-name">北向资金</span><span class="market-val up">连续9日净买入</span></div>"""
new1 = """      <h4>🇨🇳 A股（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">上证指数</span><span class="market-val down">3959.34 -1.70%</span></div>
      <div class="market-row"><span class="market-name">深证成指</span><span class="market-val down">14821.19 -3.22%</span></div>
      <div class="market-row"><span class="market-name">创业板指</span><span class="market-val down">3811.79 -3.69%</span></div>
      <div class="market-row"><span class="market-name">科创50</span><span class="market-val down">-4.30%</span></div>
      <div class="market-row"><span class="market-name">沪深300</span><span class="market-val down">-2.14%</span></div>
      <div class="market-row"><span class="market-name">成交额</span><span class="market-val neutral" style="color:#f0b429;font-weight:700;">27927.61亿<span style="font-size:11px;"> (连续31日超2.5万亿)</span></span></div>
      <div class="market-row"><span class="market-name">涨跌家数</span><span class="market-val down">898涨/4591跌</span></div>
      <div class="market-row"><span class="market-name">北向资金</span><span class="market-val up">连续8日净买入</span></div>"""

# 港股 market-block
old2 = """      <h4>🇭🇰 港股（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">恒生指数</span><span class="market-val up">25128.60 +0.85%</span></div>
      <div class="market-row"><span class="market-name">恒生科技指数</span><span class="market-val up">4892.35 +1.24%</span></div>
      <div class="market-row"><span class="market-name">国企指数</span><span class="market-val up">8512.48 +0.72%</span></div>
      <div class="market-row"><span class="market-name">南向资金</span><span class="market-val up">净买入96.85亿港元</span></div>"""
new2 = """      <h4>🇭🇰 港股（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">恒生指数</span><span class="market-val down">24657.06 -1.22%</span></div>
      <div class="market-row"><span class="market-name">恒生科技指数</span><span class="market-val down">4755.91 -2.71%</span></div>
      <div class="market-row"><span class="market-name">国企指数</span><span class="market-val down">8341.36 -1.13%</span></div>
      <div class="market-row"><span class="market-name">南向资金</span><span class="market-val up">净买入113.18亿港元</span></div>"""

# 美股 market-block
old3 = """      <h4>🇺🇸 美股（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">道琼斯</span><span class="market-val up">51142.30 +0.54%</span></div>
      <div class="market-row"><span class="market-name">标普500</span><span class="market-val up">7442.18 +0.79%</span></div>
      <div class="market-row"><span class="market-name">纳斯达克</span><span class="market-val up">25948.75 +0.93%</span></div>
      <div class="market-row"><span class="market-name">英伟达</span><span class="market-val up">$212.80 +3.76%</span></div>
      <div class="market-row"><span class="market-name">特斯拉</span><span class="market-val up">涨2.18%</span></div>
      <div class="market-row"><span class="market-name">ARM</span><span class="market-val up">涨4.52%</span></div>"""
new3 = """      <h4>🇺🇸 美股（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">道琼斯</span><span class="market-val down">50866.78 -1.35%</span></div>
      <div class="market-row"><span class="market-name">标普500</span><span class="market-val down">7383.74 -2.64%</span></div>
      <div class="market-row"><span class="market-name">纳斯达克</span><span class="market-val down">25709.43 -4.18%</span></div>
      <div class="market-row"><span class="market-name">英伟达</span><span class="market-val down">$205.10 -6.20%</span></div>
      <div class="market-row"><span class="market-name">特斯拉</span><span class="market-val down">跌6.56%</span></div>
      <div class="market-row"><span class="market-name">ARM</span><span class="market-val down">跌12.84%</span></div>"""

# 亚太 market-block
old4 = """      <h4>🌏 亚太市场（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">日经225</span><span class="market-val up">64856.20 +1.30%</span></div>
      <div class="market-row"><span class="market-name">韩国KOSPI</span><span class="market-val up">7685.20 +2.68%</span></div>
      <div class="market-row"><span class="market-name">台湾加权</span><span class="market-val up">涨1.85%</span></div>
      <div class="market-row"><span class="market-name">印度Sensex</span><span class="market-val up">跟随亚太上涨</span></div>
      <div class="market-row"><span class="market-name">澳洲ASX200</span><span class="market-val up">8712.60 +0.82%</span></div>"""
new4 = """      <h4>🌏 亚太市场（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">日经225</span><span class="market-val down">64024.60 -3.85%</span></div>
      <div class="market-row"><span class="market-name">韩国KOSPI</span><span class="market-val down">7484.41 -8.29% 触发熔断</span></div>
      <div class="market-row"><span class="market-name">台湾加权</span><span class="market-val down">跌约6%</span></div>
      <div class="market-row"><span class="market-name">印度Sensex</span><span class="market-val down">跟随亚太下跌</span></div>
      <div class="market-row"><span class="market-name">澳洲ASX200</span><span class="market-val down">8641 -1.00%</span></div>"""

# 欧洲 market-block
old5 = """      <h4>🇪🇺 欧洲市场（6月10日盘中）</h4>
      <div class="market-row"><span class="market-name">英国富时100</span><span class="market-val up">+0.62%</span></div>
      <div class="market-row"><span class="market-name">德国DAX30</span><span class="market-val up">+0.85%</span></div>
      <div class="market-row"><span class="market-name">法国CAC40</span><span class="market-val up">+0.76%</span></div>
      <div class="market-row"><span class="market-name">斯托克50</span><span class="market-val up">+0.72%</span></div>"""
new5 = """      <h4>🇪🇺 欧洲市场（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">英国富时100</span><span class="market-val up">微涨0.05%</span></div>
      <div class="market-row"><span class="market-name">德国DAX30</span><span class="market-val down">-0.47%</span></div>
      <div class="market-row"><span class="market-name">法国CAC40</span><span class="market-val down">随欧股调整</span></div>
      <div class="market-row"><span class="market-name">斯托克50</span><span class="market-val down">随欧股调整</span></div>"""

# 大宗商品 market-block
old6 = """      <h4>🏭 大宗商品（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">WTI原油</span><span class="market-val down">$89.25 -1.41%</span></div>
      <div class="market-row"><span class="market-name">布伦特原油</span><span class="market-val down">$92.80 -0.98%</span></div>
      <div class="market-row"><span class="market-name">国际黄金</span><span class="market-val up">$4318 +0.77%</span></div>
      <div class="market-row"><span class="market-name">上海金</span><span class="market-val up">952.48元/克</span></div>
      <div class="market-row"><span class="market-name">白银</span><span class="market-val up">68.92美元/盎司 +1.76%</span></div>"""
new6 = """      <h4>🏭 大宗商品（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">WTI原油</span><span class="market-val down">$90.53 -0.01%</span></div>
      <div class="market-row"><span class="market-name">布伦特原油</span><span class="market-val up">$93.72 +0.68%</span></div>
      <div class="market-row"><span class="market-name">国际黄金</span><span class="market-val down">$4285 -1.34%</span></div>
      <div class="market-row"><span class="market-name">上海金</span><span class="market-val down">随国际金价调整</span></div>
      <div class="market-row"><span class="market-name">白银</span><span class="market-val down">跟随黄金下行</span></div>"""

# 汇率债券 market-block
old7 = """      <h4>💱 汇率与债券（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">USD/CNY中间价</span><span class="market-val neutral">6.8215</span></div>
      <div class="market-row"><span class="market-name">在岸汇率</span><span class="market-val neutral">6.7825</span></div>
      <div class="market-row"><span class="market-name">美元指数</span><span class="market-val down">99.62 -0.44%</span></div>
      <div class="market-row"><span class="market-name">美10年期</span><span class="market-val down">4.48%</span></div>
      <div class="market-row"><span class="market-name">美30年期</span><span class="market-val down">4.62%</span></div>
      <div class="market-row"><span class="market-name">中10年期</span><span class="market-val neutral">约1.71%</span></div>"""
new7 = """      <h4>💱 汇率与债券（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">USD/CNY中间价</span><span class="market-val neutral">6.8198</span></div>
      <div class="market-row"><span class="market-name">在岸汇率</span><span class="market-val neutral">6.7794</span></div>
      <div class="market-row"><span class="market-name">美元指数</span><span class="market-val up">100.06 走强</span></div>
      <div class="market-row"><span class="market-name">美10年期</span><span class="market-val up">4.55%</span></div>
      <div class="market-row"><span class="market-name">美30年期</span><span class="market-val up">4.70%</span></div>
      <div class="market-row"><span class="market-name">中10年期</span><span class="market-val neutral">约1.71%</span></div>"""

# 加密货币 market-block
old8 = """      <h4>🪙 加密货币（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">比特币BTC</span><span class="market-val up">$65280</span></div>
      <div class="market-row"><span class="market-name">以太坊ETH</span><span class="market-val up">$1785</span></div>
      <div class="market-row"><span class="market-name">BTC ETF</span><span class="market-val neutral">小幅净流入</span></div>
      <div class="market-row"><span class="market-name">市场情绪</span><span class="market-val neutral">中性偏乐观（BTC箱体整理）</span></div>"""
new8 = """      <h4>🪙 加密货币（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">比特币BTC</span><span class="market-val down">$62956</span></div>
      <div class="market-row"><span class="market-name">以太坊ETH</span><span class="market-val down">$1666</span></div>
      <div class="market-row"><span class="market-name">BTC ETF</span><span class="market-val neutral">小幅净流出</span></div>
      <div class="market-row"><span class="market-name">市场情绪</span><span class="market-val neutral">避险情绪上升（BTC承压）</span></div>"""

# 执行替换
for i, (old, new, name) in enumerate([(old1,new1,"A股"),(old2,new2,"港股"),(old3,new3,"美股"),(old4,new4,"亚太"),(old5,new5,"欧洲"),(old6,new6,"大宗商品"),(old7,new7,"汇率债券"),(old8,new8,"加密货币")]):
    if old in html:
        html = html.replace(old, new)
        changes.append(f"✓ {name}")
    else:
        print(f"✗ {name} NOT FOUND")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

for c in changes:
    print(c)
print(f"\n成功: {len(changes)}/8")
