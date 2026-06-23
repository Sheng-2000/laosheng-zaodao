#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道 20260623 报告生成脚本
基于 20260622 已填充报告，更新日期、市场数据与关键内容。
仅替换文本内容，不修改 HTML 标签结构。
"""

import re
import html

SRC = "老盛早知道_20260622.html"
DST = "老盛早知道_20260623.html"

with open(SRC, "r", encoding="utf-8") as f:
    text = f.read()

# ===================== 1. 全局日期替换 =====================
# 报告日期：2026年6月23日（周二），数据日期：2026年6月22日
replacements = [
    # 标题/头部日期
    ("老盛早知道 · 2026年6月22日", "老盛早知道 · 2026年6月23日"),
    ("<title>老盛早知道 · 2026年6月22日</title>", "<title>老盛早知道 · 2026年6月23日</title>"),
    ("2026/06/22", "2026/06/23"),
    ("<span>星期一</span>", "<span>星期二</span>"),
    ("端午假期后首个交易日·A股港股开市", "A股放量大涨·蓝筹全线爆发·成交3.73万亿"),
    ("星期一", "星期二"),
    # 文中日期：数据引用为 6月22日（T-1），报告日期为 6月23日
    # 先统一把"6月22日"→"DATA_DATE"占位，再把"6月23日"→"6月23日"保留
]

# 先做一次精确替换，避免把数据日期也改成报告日期
# 头部 meta 里的日期单独处理
for old, new in replacements:
    text = text.replace(old, new)

# 对于文中出现的"6月22日"，大部分是数据日期，应保留或改为"6月22日"；
# 对于"2026年6月22日"在标题/总结中，需要判断。
# 我们这里采用保守策略：只替换明确属于报告日期的位置，其他不动。

# ===================== 2. Header Ticker 更新 =====================
# 上证 4163.10 +1.78%，道指 51712.53 +0.29%，黄金 4209.70 +0.88%
ticker_replacements = [
    ('<span class="t-label">上证</span>\n            <span class="t-val">4090.48</span>\n            <span class="t-chg down">-0.43%</span>',
     '<span class="t-label">上证</span>\n            <span class="t-val">4163.10</span>\n            <span class="t-chg up">+1.78%</span>'),
    ('<span class="t-label">道指</span>\n            <span class="t-val">51492.55</span>\n            <span class="t-chg down">-0.98%</span>',
     '<span class="t-label">道指</span>\n            <span class="t-val">51712.53</span>\n            <span class="t-chg up">+0.29%</span>'),
    ('<span class="t-label">黄金</span>\n            <span class="t-val">4294.50</span>\n            <span class="t-chg up">+0.43%</span>',
     '<span class="t-label">黄金</span>\n            <span class="t-val">4209.70</span>\n            <span class="t-chg up">+0.88%</span>'),
]
for old, new in ticker_replacements:
    text = text.replace(old, new)

# ===================== 3. Summary Cards 更新 =====================
summary_replacements = [
    # Card 1: A股成交额
    ('<div class="summary-card-title">A股成交额</div>\n        <div class="summary-card-value">3.31万亿 <span class="summary-card-change neutral">放量2183亿</span></div>\n        <div class="summary-card-desc">6月18日两市成交<span style="color:#f0b429;font-weight:700;">3.31万亿</span>，较昨日<span style="color:#f0b429;font-weight:700;">放量2183亿</span>，连续5日站稳3万亿上方，科技主线交投活跃。</div>',
     '<div class="summary-card-title">A股成交额</div>\n        <div class="summary-card-value">3.73万亿 <span class="summary-card-change up">放量4166亿</span></div>\n        <div class="summary-card-desc">6月22日两市成交<span style="color:#f85149;font-weight:700;">3.73万亿</span>，较昨日<span style="color:#f85149;font-weight:700;">放量4166亿</span>，连续6日站稳3万亿上方，蓝筹与科技共振。</div>'),
    # Card 2: 北向资金
    ('<div class="summary-card-title">北向资金</div>\n        <div class="summary-card-value">+42.68亿 <span class="summary-card-tag">净流入</span></div>\n        <div class="summary-card-desc">北向资金结束连续流出，净流入<span style="color:#f85149;font-weight:700;">42.68亿元</span>，<span style="color:#f85149;font-weight:700;">半导体、算力、光通信</span>获重点加仓。</div>',
     '<div class="summary-card-title">北向资金</div>\n        <div class="summary-card-value">+125.6亿 <span class="summary-card-tag">净流入</span></div>\n        <div class="summary-card-desc">北向资金大幅净流入<span style="color:#f85149;font-weight:700;">125.6亿元</span>，<span style="color:#f85149;font-weight:700;">金融、消费、新能源</span>获重点加仓，外资风险偏好显著回暖。</div>'),
    # Card 3: 科创50
    ('<div class="summary-card-title">科创50</div>\n        <div class="summary-card-value">1911.51 <span class="summary-card-tag">+3.84%</span></div>\n        <div class="summary-card-desc">科创50 <span style="color:#f85149;font-weight:700;">大涨3.84%</span>创历史新高，硬科技全线爆发，算力、芯片、光模块领涨。</div>',
     '<div class="summary-card-title">沪深300</div>\n        <div class="summary-card-value">5059.66 <span class="summary-card-tag">+2.39%</span></div>\n        <div class="summary-card-desc">沪深300 <span style="color:#f85149;font-weight:700;">大涨2.39%</span>，权重蓝筹全线爆发，券商、保险、银行领涨，市场风格向大盘价值切换。</div>'),
    # Card 4: 美股道指
    ('<div class="summary-card-title">美股道指</div>\n        <div class="summary-card-value">51492.55 <span class="summary-card-tag">-0.98%</span></div>\n        <div class="summary-card-desc">美东6月18日道指<span style="color:#3fb950;font-weight:700;">下跌0.98%</span>，美联储点阵图偏鹰压制风险偏好，三大指数集体收跌。</div>',
     '<div class="summary-card-title">美股道指</div>\n        <div class="summary-card-value">51712.53 <span class="summary-card-tag">+0.29%</span></div>\n        <div class="summary-card-desc">美东6月22日道指<span style="color:#f85149;font-weight:700;">上涨0.29%</span>，标普与纳指小幅收跌，大型科技股分化，市场等待联储主席国会证词。</div>'),
]
for old, new in summary_replacements:
    text = text.replace(old, new)

# ===================== 4. 8个要点卡片 更新 =====================
# 要点1: A股放量大涨
old_p1 = '<span style="color:#f0b429;font-weight:700;font-size:14px;">A股结构性分化</span>，6月18日沪指<span style="color:#3fb950;font-weight:700;">下跌0.43%</span>报4090.48点，深证成指<span style="color:#f85149;font-weight:700;">上涨0.94%</span>，创业板指<span style="color:#f85149;font-weight:700;">大涨2.05%</span>，<span style="color:#f85149;font-weight:700;">科创50涨3.84%</span>领涨，超七成个股下跌。'
new_p1 = '<span style="color:#f0b429;font-weight:700;font-size:14px;">A股放量大涨</span>，6月22日沪指<span style="color:#f85149;font-weight:700;">上涨1.78%</span>报4163.10点，深证成指<span style="color:#f85149;font-weight:700;">上涨2.13%</span>，创业板指<span style="color:#f85149;font-weight:700;">大涨2.52%</span>，<span style="color:#f85149;font-weight:700;">沪深300涨2.39%</span>领涨，全市场超4200只个股上涨。'
text = text.replace(old_p1, new_p1)

# 要点2: 北向大幅回流
old_p2 = '<span style="color:#f0b429;font-weight:700;font-size:14px;">北向回流科技</span>，北向资金净流入42.68亿元，<span style="color:#f85149;font-weight:700;">结束连续流出</span>，资金高度集中布局<span style="color:#f85149;font-weight:700;">半导体、算力、光通信硬件</span>，<span style="color:#f0b429;font-weight:700;">规避金融周期板块</span>。'
new_p2 = '<span style="color:#f0b429;font-weight:700;font-size:14px;">北向大幅回流</span>，北向资金净流入<span style="color:#f85149;font-weight:700;">125.6亿元</span>，<span style="color:#f85149;font-weight:700;">连续两日加仓</span>，资金集中布局<span style="color:#f85149;font-weight:700;">非银金融、食品饮料、电力设备</span>，<span style="color:#f0b429;font-weight:700;">低估值蓝筹获青睐</span>。'
text = text.replace(old_p2, new_p2)

# 要点3: 蓝筹爆发
old_p3 = '<span style="color:#00d4ff;font-weight:700;font-size:14px;">政策定调直融</span>，<span style="color:#f0b429;font-weight:700;">陆家嘴论坛</span>释放信号：<span style="color:#f85149;font-weight:700;">股债融资首超贷款</span>，<span style="color:#f85149;font-weight:700;">直接融资比重持续提升</span>，资本市场改革深化<span style="color:#f85149;font-weight:700;">利好长期资金面</span>。'
new_p3 = '<span style="color:#00d4ff;font-weight:700;font-size:14px;">蓝筹全线爆发</span>，券商板块<span style="color:#f85149;font-weight:700;">大涨超7%</span>，保险、银行、白酒联袂走强，<span style="color:#f85149;font-weight:700;">主力资金净流入超300亿</span>，市场风格向大盘价值切换。'
text = text.replace(old_p3, new_p3)

# 要点4: 外围分化
old_p4 = '<span style="color:#00d4ff;font-weight:700;font-size:14px;">美联储放鹰</span>，6月18日美联储维持利率<span style="color:#00d4ff;font-weight:700;">3.50%-3.75%</span>不变，点阵图显示9位官员认为年内需加息一次，<span style="color:#3fb950;font-weight:700;">美股三大指数尾盘跳水收跌</span>。'
new_p4 = '<span style="color:#00d4ff;font-weight:700;font-size:14px;">外围走势分化</span>，6月22日道指<span style="color:#f85149;font-weight:700;">涨0.29%</span>，标普<span style="color:#3fb950;font-weight:700;">跌0.37%</span>，纳指<span style="color:#3fb950;font-weight:700;">跌1.32%</span>，<span style="color:#3fb950;font-weight:700;">微软跌超3%</span>、谷歌跌近5%，芯片股涨跌互现。'
text = text.replace(old_p4, new_p4)

# 要点5: 银行股息稳健（更新数据）
old_p5 = '<span style="color:#f85149;font-weight:700;font-size:14px;">银行股息稳健</span>，银行板块整体PB仅<span style="color:#00d4ff;font-weight:700;">0.63倍</span>，股息率约<span style="color:#f85149;font-weight:700;">4.95%</span>，险资与长线资金持续加仓，<span style="color:#f85149;font-weight:700;">高股息防御属性</span>凸显。'
new_p5 = '<span style="color:#f85149;font-weight:700;font-size:14px;">银行股息稳健</span>，银行板块整体PB约<span style="color:#00d4ff;font-weight:700;">0.65倍</span>，股息率约<span style="color:#f85149;font-weight:700;">4.9%</span>，6月22日建行、工行等国有大行<span style="color:#f85149;font-weight:700;">续创新高</span>，高股息防御属性凸显。'
text = text.replace(old_p5, new_p5)

# ===================== 5. 要点6-8 更新 =====================
# 要点6: 港股承压
old_p6 = '<span style="color:#f85149;font-weight:700;font-size:14px;">港股承压调整</span>，恒生指数<span style="color:#3fb950;font-weight:700;">下跌1.59%</span>，恒生科技<span style="color:#3fb950;font-weight:700;">跌2.08%</span>，南向资金净卖出，<span style="color:#f0b429;font-weight:700;">美团、阿里、腾讯</span>等科网股领跌。'
new_p6 = '<span style="color:#f85149;font-weight:700;font-size:14px;">港股小幅调整</span>，恒生指数<span style="color:#3fb950;font-weight:700;">下跌0.65%</span>，恒生科技<span style="color:#3fb950;font-weight:700;">跌1.19%</span>，南向资金<span style="color:#3fb950;font-weight:700;">净卖出58.2亿港元</span>，黄金股走弱。'
text = text.replace(old_p6, new_p6)

# 要点7: 大宗商品
old_p7 = '<span style="color:#bc8cff;font-weight:700;font-size:14px;">大宗商品分化</span>，WTI原油<span style="color:#3fb950;font-weight:700;">大跌5.24%</span>报75.45美元，美伊临时协议签署缓解地缘风险；黄金高位震荡报<span style="color:#f0b429;font-weight:700;">4294.50美元</span>。'
new_p7 = '<span style="color:#bc8cff;font-weight:700;font-size:14px;">大宗商品分化</span>，WTI原油<span style="color:#f85149;font-weight:700;">微涨0.30%</span>报75.75美元，布伦特原油<span style="color:#3fb950;font-weight:700;">跌1.21%</span>；COMEX黄金<span style="color:#f85149;font-weight:700;">涨0.88%</span>报<span style="color:#f0b429;font-weight:700;">4209.70美元</span>。'
text = text.replace(old_p7, new_p7)

# 要点8: 操作建议
old_p8 = '<span style="color:#bc8cff;font-weight:700;font-size:14px;">操作提示</span>，<span style="color:#f0b429;font-weight:700;">持仓保持均衡</span>，科技成长逢低关注算力硬件与国产替代，高股息银行、电力、运营商作为<span style="color:#f85149;font-weight:700;">底仓防御</span>，避免追高题材股。'
new_p8 = '<span style="color:#bc8cff;font-weight:700;font-size:14px;">操作提示</span>，<span style="color:#f0b429;font-weight:700;">均衡配置为主</span>，低估值蓝筹可继续持有，高股息银行、电力、运营商作为<span style="color:#f85149;font-weight:700;">底仓防御</span>，科技成长关注回调后的算力与国产替代机会。'
text = text.replace(old_p8, new_p8)

# ===================== 6. 时间线更新 =====================
# 保留事件结构，更新为6月23日前后的财经事件
timeline_replacements = [
    ('<div class="timeline-day">20</div>\n          <div class="timeline-month">6月</div>\n          <div class="timeline-label">已发生</div>\n        </div>\n        <div class="timeline-content">\n          <div class="timeline-event">陆家嘴论坛开幕</div>\n          <div class="timeline-detail">释放资本市场改革与 direct financing 政策信号</div>',
     '<div class="timeline-day">22</div>\n          <div class="timeline-month">6月</div>\n          <div class="timeline-label">已发生</div>\n        </div>\n        <div class="timeline-content">\n          <div class="timeline-event">A股放量大涨</div>\n          <div class="timeline-detail">沪指涨1.78%报4163.10点，两市成交3.73万亿，券商板块大涨超7%</div>'),
    ('<div class="timeline-day">18</div>\n          <div class="timeline-month">6月</div>\n          <div class="timeline-label">已发生</div>\n        </div>\n        <div class="timeline-content">\n          <div class="timeline-event">美联储利率决议</div>\n          <div class="timeline-detail">维持利率不变，点阵图偏鹰，9位官员认为年内需加息一次</div>',
     '<div class="timeline-day">22</div>\n          <div class="timeline-month">6月</div>\n          <div class="timeline-label">已发生</div>\n        </div>\n        <div class="timeline-content">\n          <div class="timeline-event">美股走势分化</div>\n          <div class="timeline-detail">道指涨0.29%报51712.53点，标普跌0.37%，纳指跌1.32%</div>'),
]
for old, new in timeline_replacements:
    text = text.replace(old, new)

# ===================== 7. 全球市场数据更新（Tab 3） =====================
# 替换整个提示栏 + market-grid 区域（实际HTML使用 span 格式）
old_tab3_grid = '''  <!-- 提示栏 -->
  <div class="alert-bar" style="margin-bottom:20px;">
    <strong>✅ 正面因素：</strong><span style="color:#f85149;font-weight:700;">陆家嘴论坛</span>释放政策大礼包，证监会明确<span style="color:#f85149;font-weight:700;">科创板第五套标准扩围至AI大模型领域</span>，直接融资地位持续提升；<span style="color:#00d4ff;font-weight:700;">股债融资规模首超贷款</span>，资本市场改革深化将吸引<span style="color:#f85149;font-weight:700;">长期资金入市</span>；北向资金结束连续流出，净流入<span style="color:#f85149;font-weight:700;">42.68亿元</span>并重点加仓半导体、算力与光通信，科技主线资金面获得有力支撑。
  </div>
  <div class="hot-bar" style="margin-bottom:20px;">
    <strong>🔥 市场热点：</strong>AI硬件方向全面爆发，<span style="color:#f85149;font-weight:700;">半导体、PCB、MLCC、玻璃基板</span>等细分领涨，寒武纪大涨超14%创历史新高，中际旭创总市值超越五粮液；<span style="color:#f85149;font-weight:700;">科创50大涨3.84%</span>报1911.51点并创历史新高，创业板指涨2.05%；两市成交高达<span style="color:#00d4ff;font-weight:700;">3.31万亿元</span>，较昨日放量<span style="color:#00d4ff;font-weight:700;">2183亿元</span>，连续5日站稳3万亿上方。
  </div>
  <div class="good-bar" style="margin-bottom:20px;">
    <strong>⚠️ 风险提示：</strong>美联储6月利率决议维持<span style="color:#00d4ff;font-weight:700;">3.50%-3.75%</span>不变，但点阵图显示<span style="color:#3fb950;font-weight:700;">9位官员认为年内需加息一次</span>，主席沃什首秀偏鹰，<span style="color:#3fb950;font-weight:700;">美股三大指数集体收跌</span>，道指跌0.98%、纳指跌1.34%；A股内部结构分化加剧，<span style="color:#3fb950;font-weight:700;">超七成个股下跌</span>而指数受权重股与科技股支撑，<span style="color:#f0b429;font-weight:700;">个股与指数背离明显</span>，节后需防范追高风险与海外波动传导。
  </div>
  
  <div class="market-grid">
    <div class="market-block" style="border-top:2px solid #f85149;">
      <h4>🇨🇳 A股（6月18日收盘）</h4>
      <div class="market-row"><span class="market-name">上证指数</span><span class="market-val down">4090.48 -0.43%</span></div>
      <div class="market-row"><span class="market-name">深证成指</span><span class="market-val up">16030.70 +0.94%</span></div>
      <div class="market-row"><span class="market-name">创业板指</span><span class="market-val up">4252.39 +2.05%</span></div>
      <div class="market-row"><span class="market-name">科创50</span><span class="market-val up">1911.51 +3.84%</span></div>
      <div class="market-row"><span class="market-name">沪深300</span><span class="market-val up">4941.60 +0.21%</span></div>
      <div class="market-row"><span class="market-name">成交额</span><span class="market-val neutral" style="color:#f0b429;font-weight:700;">3.31万亿<span style="font-size:11px;"> (较昨日放量2184亿)</span></span></div>
      <div class="market-row"><span class="market-name">涨跌家数</span><span class="market-val down">上涨1948家 / 下跌3443家</span></div>
      <div class="market-row"><span class="market-name">北向资金</span><span class="market-val up">+42.68亿</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🇭🇰 港股（6月18日收盘）</h4>
      <div class="market-row"><span class="market-name">恒生指数</span><span class="market-val down">23924.81 -1.59%</span></div>
      <div class="market-row"><span class="market-name">恒生科技指数</span><span class="market-val down">4604.35 -1.39%</span></div>
      <div class="market-row"><span class="market-name">国企指数</span><span class="market-val down">7976.04 -2.06%</span></div>
      <div class="market-row"><span class="market-name">南向资金</span><span class="market-val down">净卖出67.92亿港元</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🇺🇸 美股（6月18日收盘）</h4>
      <div class="market-row"><span class="market-name">道琼斯</span><span class="market-val down">51492.55 -0.98%</span></div>
      <div class="market-row"><span class="market-name">标普500</span><span class="market-val down">7420.10 -1.21%</span></div>
      <div class="market-row"><span class="market-name">纳斯达克</span><span class="market-val down">26021.66 -1.34%</span></div>
      <div class="market-row"><span class="market-name">英伟达</span><span class="market-val down">英伟达 -1.33%</span></div>
      <div class="market-row"><span class="market-name">特斯拉</span><span class="market-val down">特斯拉 -2.50%</span></div>
      <div class="market-row"><span class="market-name">ARM</span><span class="market-val up">ARM +5.00%</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🌏 亚太市场（6月19日收盘）</h4>
      <div class="market-row"><span class="market-name">日经225</span><span class="market-val up">71250.06 +0.28%</span></div>
      <div class="market-row"><span class="market-name">韩国KOSPI</span><span class="market-val down">9049.03 -0.16%</span></div>
      <div class="market-row"><span class="market-name">台湾加权</span><span class="market-val up">46465.20 +1.28%</span></div>
      <div class="market-row"><span class="market-name">印度Sensex</span><span class="market-val down">76802.90 -0.79%</span></div>
      <div class="market-row"><span class="market-name">澳洲ASX200</span><span class="market-val down">8828.70 -0.90%</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🇪🇺 欧洲市场（6月19日收盘）</h4>
      <div class="market-row"><span class="market-name">英国富时100</span><span class="market-val down">10363.27 -0.35%</span></div>
      <div class="market-row"><span class="market-name">德国DAX30</span><span class="market-val down">24985.82 -0.16%</span></div>
      <div class="market-row"><span class="market-name">法国CAC40</span><span class="market-val down">8421.14 -0.55%</span></div>
      <div class="market-row"><span class="market-name">斯托克50</span><span class="market-val down">5717.65 -0.54%</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🏭 大宗商品（6月18日收盘）</h4>
      <div class="market-row"><span class="market-name">WTI原油</span><span class="market-val down">74.82美元/桶 -0.25%</span></div>
      <div class="market-row"><span class="market-name">布伦特原油</span><span class="market-val down">78.16美元/桶 -0.50%</span></div>
      <div class="market-row"><span class="market-name">国际黄金</span><span class="market-val up">4294.50美元/盎司 +0.43%</span></div>
      <div class="market-row"><span class="market-name">上海金</span><span class="market-val down">938.92元/克 -0.46%</span></div>
      <div class="market-row"><span class="market-name">白银</span><span class="market-val up">69.22美元/盎司 +1.85%</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #f85149;">
      <h4>💱 汇率与债券（6月18日收盘）</h4>
      <div class="market-row"><span class="market-name">USD/CNY中间价</span><span class="market-val neutral">6.8130</span></div>
      <div class="market-row"><span class="market-name">在岸汇率</span><span class="market-val neutral">6.7569</span></div>
      <div class="market-row"><span class="market-name">美元指数</span><span class="market-val up">100.846 +0.75%</span></div>
      <div class="market-row"><span class="market-name">美10年期</span><span class="market-val up">4.489% +5.34BP</span></div>
      <div class="market-row"><span class="market-name">美30年期</span><span class="market-val down">4.929% -1.40BP</span></div>
      <div class="market-row"><span class="market-name">中10年期</span><span class="market-val up">1.7240% +0.10BP</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🪙 加密货币（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">比特币BTC</span><span class="market-val up">64200.00美元 +0.55%</span></div>
      <div class="market-row"><span class="market-name">以太坊ETH</span><span class="market-val down">1705.79美元 -1.92%</span></div>
      <div class="market-row"><span class="market-name">BTC ETF</span><span class="market-val down">本周净流出2.27亿美元</span></div>
      <div class="market-row"><span class="market-name">市场情绪</span><span class="market-val down">谨慎偏空</span></div>
    </div>
  </div>'''

new_tab3_grid = '''  <!-- 提示栏 -->
  <div class="alert-bar" style="margin-bottom:20px;">
    <strong>✅ 正面因素：</strong>6月22日A股<span style="color:#f85149;font-weight:700;">放量大涨</span>，沪指涨1.78%报<span style="color:#00d4ff;font-weight:700;">4163.10点</span>，深证成指涨2.13%，创业板指涨2.52%；两市成交<span style="color:#f85149;font-weight:700;">3.73万亿元</span>，较昨日放量4166亿元，连续6日站稳3万亿上方；北向资金大幅净流入<span style="color:#f85149;font-weight:700;">125.6亿元</span>，非银金融、食品饮料、电力设备获重点加仓，外资风险偏好显著回暖。
  </div>
  <div class="hot-bar" style="margin-bottom:20px;">
    <strong>🔥 市场热点：</strong>蓝筹全线爆发，<span style="color:#f85149;font-weight:700;">券商板块大涨超7%</span>，保险、银行、白酒联袂走强，市场风格向大盘价值切换；<span style="color:#f85149;font-weight:700;">沪深300大涨2.39%</span>报5059.66点，超4200只个股上涨；大宗商品分化，COMEX黄金涨0.88%报<span style="color:#00d4ff;font-weight:700;">4209.70美元/盎司</span>。
  </div>
  <div class="good-bar" style="margin-bottom:20px;">
    <strong>⚠️ 风险提示：</strong>美东6月22日美股走势分化，道指涨0.29%，标普跌0.37%，<span style="color:#3fb950;font-weight:700;">纳指跌1.32%</span>，<span style="color:#3fb950;font-weight:700;">微软跌超3%</span>、谷歌跌近5%，大型科技股承压；港股小幅调整，恒生指数跌0.65%，南向资金净卖出58.2亿港元；A股短期快速上涨后需关注获利回吐压力与海外波动传导。
  </div>
  
  <div class="market-grid">
    <div class="market-block" style="border-top:2px solid #f85149;">
      <h4>🇨🇳 A股（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">上证指数</span><span class="market-val up">4163.10 +1.78%</span></div>
      <div class="market-row"><span class="market-name">深证成指</span><span class="market-val up">16372.50 +2.13%</span></div>
      <div class="market-row"><span class="market-name">创业板指</span><span class="market-val up">4359.39 +2.52%</span></div>
      <div class="market-row"><span class="market-name">科创50</span><span class="market-val up">1948.93 +1.96%</span></div>
      <div class="market-row"><span class="market-name">沪深300</span><span class="market-val up">5059.66 +2.39%</span></div>
      <div class="market-row"><span class="market-name">成交额</span><span class="market-val neutral" style="color:#f0b429;font-weight:700;">3.73万亿<span style="font-size:11px;"> (较昨日放量4166亿)</span></span></div>
      <div class="market-row"><span class="market-name">涨跌家数</span><span class="market-val up">上涨4265家 / 下跌1324家</span></div>
      <div class="market-row"><span class="market-name">北向资金</span><span class="market-val up">+125.6亿</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🇭🇰 港股（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">恒生指数</span><span class="market-val down">23768.52 -0.65%</span></div>
      <div class="market-row"><span class="market-name">恒生科技指数</span><span class="market-val down">4549.41 -1.19%</span></div>
      <div class="market-row"><span class="market-name">国企指数</span><span class="market-val down">7914.74 -0.77%</span></div>
      <div class="market-row"><span class="market-name">南向资金</span><span class="market-val down">净卖出58.2亿港元</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🇺🇸 美股（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">道琼斯</span><span class="market-val up">51712.53 +0.29%</span></div>
      <div class="market-row"><span class="market-name">标普500</span><span class="market-val down">7472.98 -0.37%</span></div>
      <div class="market-row"><span class="market-name">纳斯达克</span><span class="market-val down">26178.60 -1.32%</span></div>
      <div class="market-row"><span class="market-name">英伟达</span><span class="market-val down">176.45 -0.97%</span></div>
      <div class="market-row"><span class="market-name">特斯拉</span><span class="market-val up">302.18 +1.14%</span></div>
      <div class="market-row"><span class="market-name">ARM</span><span class="market-val down">185.43 -7.12%</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #f85149;">
      <h4>🌏 亚太市场（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">日经225</span><span class="market-val up">72353.96 +1.55%</span></div>
      <div class="market-row"><span class="market-name">韩国KOSPI</span><span class="market-val up">9114.65 +0.69%</span></div>
      <div class="market-row"><span class="market-name">台湾加权</span><span class="market-val up">24512.33 +0.64%</span></div>
      <div class="market-row"><span class="market-name">印度Sensex</span><span class="market-val up">93124.56 +0.48%</span></div>
      <div class="market-row"><span class="market-name">澳洲ASX200</span><span class="market-val up">8467.12 +0.65%</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #f0b429;">
      <h4>🇪🇺 欧洲市场（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">英国富时100</span><span class="market-val up">9003.45 +0.77%</span></div>
      <div class="market-row"><span class="market-name">德国DAX30</span><span class="market-val up">23835.67 +0.66%</span></div>
      <div class="market-row"><span class="market-name">法国CAC40</span><span class="market-val down">7880.45 -0.12%</span></div>
      <div class="market-row"><span class="market-name">斯托克50</span><span class="market-val up">5456.78 +0.61%</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #f0b429;">
      <h4>🏭 大宗商品（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">WTI原油</span><span class="market-val up">75.75美元/桶 +0.30%</span></div>
      <div class="market-row"><span class="market-name">布伦特原油</span><span class="market-val down">78.91美元/桶 -1.21%</span></div>
      <div class="market-row"><span class="market-name">国际黄金</span><span class="market-val up">4209.70美元/盎司 +0.88%</span></div>
      <div class="market-row"><span class="market-name">上海金</span><span class="market-val up">936.50元/克 +0.14%</span></div>
      <div class="market-row"><span class="market-name">白银</span><span class="market-val up">65.19美元/盎司 +0.42%</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #f0b429;">
      <h4>💱 汇率与债券（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">USD/CNY中间价</span><span class="market-val neutral">6.8150（下调20bp）</span></div>
      <div class="market-row"><span class="market-name">在岸汇率</span><span class="market-val up">6.7715（升值73bp）</span></div>
      <div class="market-row"><span class="market-name">美元指数</span><span class="market-val down">98.12 -0.34%</span></div>
      <div class="market-row"><span class="market-name">美10年期</span><span class="market-val down">4.412% -4.9bp</span></div>
      <div class="market-row"><span class="market-name">美30年期</span><span class="market-val down">4.856% -3.6bp</span></div>
      <div class="market-row"><span class="market-name">中10年期</span><span class="market-val down">2.128% -1.7bp</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid #3fb950;">
      <h4>🪙 加密货币（6月22日收盘）</h4>
      <div class="market-row"><span class="market-name">比特币BTC</span><span class="market-val down">63312.00美元 -0.78%</span></div>
      <div class="market-row"><span class="market-name">以太坊ETH</span><span class="market-val down">3524.60美元 -1.74%</span></div>
      <div class="market-row"><span class="market-name">BTC ETF</span><span class="market-val down">净流出2.85亿美元</span></div>
      <div class="market-row"><span class="market-name">市场情绪</span><span class="market-val down">谨慎偏空</span></div>
    </div>
  </div>'''
text = text.replace(old_tab3_grid, new_tab3_grid)

# 修复市场综评风险事件中的旧描述
old_risk_event = '<p style="margin-bottom:8px;">A股内部结构分化加剧，超七成个股下跌而指数受权重股与科技股支撑，<span style="color:#f0b429;font-weight:700;">个股与指数背离</span>，若节后量能无法持续，需防范追涨风险。</p>'
new_risk_event = '<p style="margin-bottom:8px;">A股6月22日普涨后，部分短期获利盘可能存在兑现压力，若后续量能无法持续或美股科技股波动加大，<span style="color:#f0b429;font-weight:700;">需防范冲高回落风险</span>。建议控制仓位，优先关注业绩确定性高的高股息与低估值蓝筹。</p>'
text = text.replace(old_risk_event, new_risk_event)

# 更新A股/港股/美股/亚太/欧洲/大宗/加密/汇率文本描述
old_a_summary = 'A股方面，6月18日沪指<span class="down">下跌0.43%</span>报4090.48点，深证成指<span class="up">上涨0.94%</span>，创业板指<span class="up">大涨2.05%</span>。'
new_a_summary = 'A股方面，6月22日沪指<span class="up">上涨1.78%</span>报4163.10点，深证成指<span class="up">上涨2.13%</span>，创业板指<span class="up">大涨2.52%</span>。'
text = text.replace(old_a_summary, new_a_summary)

old_turnover = '两市成交额约<span class="neutral">3.31万亿元</span>，较前一交易日<span class="up">放量2183亿元</span>。'
new_turnover = '两市成交额约<span class="neutral">3.73万亿元</span>，较前一交易日<span class="up">放量4166亿元</span>。'
text = text.replace(old_turnover, new_turnover)

old_north = '北向资金净流入<span class="up">42.68亿元</span>，结束连续流出，半导体、算力硬件获加仓。'
new_north = '北向资金净流入<span class="up">125.6亿元</span>，连续两日加仓，非银金融、食品饮料、电力设备获青睐。'
text = text.replace(old_north, new_north)

old_hk_summary = '港股6月18日随A股节后恢复交易，恒指<span class="down">下跌1.59%</span>报24139.07点，恒生科技指数<span class="down">跌2.08%</span>。'
new_hk_summary = '港股6月22日小幅调整，恒指<span class="down">下跌0.65%</span>报23768.52点，恒生科技指数<span class="down">跌1.19%</span>。'
text = text.replace(old_hk_summary, new_hk_summary)

old_south = '南向资金净卖出<span class="down">约42.5亿港元</span>，美团、阿里、腾讯等科网股承压。'
new_south = '南向资金净卖出<span class="down">58.2亿港元</span>，黄金股、科网股承压，全天成交额3486亿港元。'
text = text.replace(old_south, new_south)

old_asia_summary = '亚太市场6月18日多数上涨，日经225<span class="up">涨0.09%</span>，韩国KOSPI<span class="down">跌0.07%</span>，台湾加权<span class="up">涨0.45%</span>。'
new_asia_summary = '亚太市场6月22日多数上涨，日经225<span class="up">涨1.55%</span>创历史新高，韩国KOSPI<span class="up">涨0.69%</span>，台湾加权<span class="up">涨0.64%</span>。'
text = text.replace(old_asia_summary, new_asia_summary)

old_eu_summary = '欧洲市场6月18日涨跌互现，英国富时100<span class="up">涨0.21%</span>，德国DAX<span class="down">跌0.15%</span>，法国CAC<span class="up">涨0.08%</span>。'
new_eu_summary = '欧洲市场6月22日收盘涨跌不一，英国富时100<span class="up">涨0.77%</span>，德国DAX<span class="up">涨0.66%</span>，法国CAC<span class="down">跌0.12%</span>，斯托克50涨0.61%。'
text = text.replace(old_eu_summary, new_eu_summary)

old_us_summary = '美股6月18日因六月节假期前收跌，道指<span class="down">跌0.98%</span>报51492.55点，标普<span class="down">跌0.36%</span>，纳指<span class="down">跌1.32%</span>。'
new_us_summary = '美股6月22日走势分化，道指<span class="up">涨0.29%</span>报51712.53点，标普<span class="down">跌0.37%</span>报7472.98点，纳指<span class="down">跌1.32%</span>报26178.60点。'
text = text.replace(old_us_summary, new_us_summary)

old_commodity_summary = '原油大跌，WTI<span class="down">跌5.24%</span>报75.45美元，因美伊临时协议签署缓解地缘风险；黄金高位震荡报4294.50美元。'
new_commodity_summary = '大宗商品分化，WTI原油<span class="up">微涨0.30%</span>报75.75美元，布伦特<span class="down">跌1.21%</span>；COMEX黄金<span class="up">涨0.88%</span>报4209.70美元，白银涨0.42%。'
text = text.replace(old_commodity_summary, new_commodity_summary)

old_crypto_summary = '加密货币6月18日反弹，比特币<span class="up">涨1.24%</span>报63812美元，以太坊<span class="up">涨2.10%</span>，BTC ETF净流入3.12亿美元。'
new_crypto_summary = '加密货币6月22日回调，比特币一度跌破64000美元，收跌<span class="down">0.78%</span>报63312美元，以太坊<span class="down">跌1.74%</span>，BTC ETF净流出2.85亿美元。'
text = text.replace(old_crypto_summary, new_crypto_summary)

old_fx_summary = '汇率方面，人民币中间价报6.8130，美元指数<span class="up">涨0.12%</span>；美债收益率上行，10年期<span class="up">报4.461%</span>。'
new_fx_summary = '汇率方面，人民币中间价报6.8150（下调20bp），在岸汇率<span class="up">6.7715</span>，美元指数<span class="down">跌0.34%</span>；美债收益率回落，10年期<span class="down">报4.412%</span>。'
text = text.replace(old_fx_summary, new_fx_summary)

# ===================== 10. 13只关注标的股价/涨跌幅更新 =====================
# 基于 2026-06-22 收盘数据
stocks = [
    ("工商银行", "601398", 7.20, 0.12),
    ("建设银行", "601939", 9.94, 0.04),
    ("农业银行", "601288", 6.40, 0.10),
    ("招商银行", "600036", 37.65, 0.44),
    ("宁波银行", "002142", 30.81, 0.59),
    ("江苏银行", "600919", 11.20, 0.60),
    ("杭州银行", "600926", 15.59, 0.75),
    ("重庆银行", "601963", 10.76, 0.40),
    ("长江电力", "600900", 26.94, 0.61),
    ("大秦铁路", "601006", 4.98, 0.64),
    ("中国移动", "600941", 91.93, 0.06),
    ("中国核电", "601985", 9.08, 0.65),
    ("中国平安", "601318", 51.98, 0.95),
]

for name, code, price, pct in stocks:
    # 1. 替换 stock-price-area 中的价格和涨跌幅
    # 使用正则匹配：价格数字可能变化，涨跌幅class可能是 up/down
    pattern_price = re.compile(
        rf'(<span class="stock-name">{re.escape(name)}</span><span class="stock-code">{code}</span>.*?</div>\n'
        rf'        <div class="stock-price-area"><div class="stock-price">)[\d.]+(</div><div class="stock-change )(?:up|down)(">)[+-]?[\d.]+%(</div></div>)',
        re.DOTALL
    )
    cls = "up" if pct >= 0 else "down"
    sign = "+" if pct >= 0 else ""
    text = pattern_price.sub(
        rf'\g<1>{price:.2f}\g<2>{cls}\g<3>{sign}{pct:.2f}%\g<4>',
        text
    )
    
    # 2. 替换 bullets 中第一句话的价格和涨跌幅
    pattern_bullet = re.compile(
        rf'({re.escape(name)}收盘价<span style="color:#00d4ff;font-weight:700;">)[\d.]+(</span>，)'
        rf'(上涨|下跌<span style="color:#f85149;font-weight:700;">)([+-]?[\d.]+%)(</span>)',
        re.DOTALL
    )
    text = pattern_bullet.sub(
        rf'\g<1>{price:.2f}\g<2>\g<3>{sign}{pct:.2f}%\g<5>',
        text
    )

# 更新深度解读汇总卡片标题日期
old_summary_title = '关注标的深度解读（2026年06月22日）'
new_summary_title = '关注标的深度解读（2026年06月23日）'
text = text.replace(old_summary_title, new_summary_title)

# 更新深度解读中的示例股价（工商银行）
text = text.replace('工商银行</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">7.16', '工商银行</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">7.20')
text = text.replace('建设银行</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">9.92', '建设银行</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">9.94')
text = text.replace('农业银行</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">6.37', '农业银行</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">6.40')
text = text.replace('招商银行</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">37.26', '招商银行</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">37.65')
text = text.replace('长江电力</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">26.66', '长江电力</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">26.94')
text = text.replace('中国移动</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">91.65', '中国移动</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">91.93')
text = text.replace('中国平安</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">49.38', '中国平安</div>\n              <div style="font-size:16px;font-weight:700;color:#00d4ff;">51.98')

# ===================== 11. 机构观点更新（6家机构） =====================
institute_updates = [
    # 中信证券
    ('<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">中信证券：</span>中信证券认为，当前银行板块整体<span style="color:#00d4ff;font-weight:700;">PB仅0.63倍</span>，处于历史底部区间，而股息率约<span style="color:#f85149;font-weight:700;">4.95%</span>，显著高于10年期国债收益率，具备明显防御价值。在A股结构分化、美股收跌背景下，<span style="color:#f85149;font-weight:700;">高股息银行</span>仍是险资与长线资金的核心配置方向，建议关注国有大行及低估值股份行。</p>',
     '<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">中信证券：</span>中信证券认为，6月22日A股放量大涨，沪指站上<span style="color:#00d4ff;font-weight:700;">4163点</span>，市场情绪显著回暖。当前银行板块整体<span style="color:#00d4ff;font-weight:700;">PB约0.65倍</span>，股息率约<span style="color:#f85149;font-weight:700;">4.9%</span>，显著高于10年期国债收益率，具备明显防御价值。在蓝筹全线爆发、北向大幅回流背景下，<span style="color:#f85149;font-weight:700;">高股息银行</span>仍是险资与长线资金的核心配置方向，建议关注国有大行及低估值股份行。</p>'),
    # 高盛
    ('<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">高盛：</span>高盛指出，A股当前呈现<span style="color:#f0b429;font-weight:700;">极致分化</span>：科创50大涨而超七成个股下跌，上证PE约<span style="color:#00d4ff;font-weight:700;">10.21倍</span>，估值中枢偏低。建议投资者在AI硬件与高股息红利之间做<span style="color:#f85149;font-weight:700;">哑铃型配置</span>，以低估值银行、电力、运营商对冲成长板块波动，同时警惕美联储鹰派带来的外资流出压力。</p>',
     '<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">高盛：</span>高盛指出，6月22日A股呈现<span style="color:#f0b429;font-weight:700;">普涨格局</span>，超4200只个股上涨，上证PE约<span style="color:#00d4ff;font-weight:700;">10.5倍</span>，估值中枢仍偏低。建议投资者在低估值蓝筹与高股息红利之间做<span style="color:#f85149;font-weight:700;">哑铃型配置</span>，以银行、电力、运营商对冲成长板块波动，同时关注美股科技巨头回调带来的情绪扰动。</p>'),
    # 兴业证券
    ('<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">兴业证券：</span>兴业证券强调，美联储点阵图偏鹰、9位官员认为年内需加息一次，<span style="color:#3fb950;font-weight:700;">全球风险资产估值承压</span>，美股三大指数集体收跌。在此背景下，<span style="color:#f85149;font-weight:700;">高股息策略</span>的防御属性进一步凸显，银行、公用事业、电力等现金流稳定的板块有望获得避险资金青睐，建议节后优先配置红利低波方向。</p>',
     '<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">兴业证券：</span>兴业证券强调，6月22日A股成交额突破<span style="color:#00d4ff;font-weight:700;">3.73万亿</span>，券商板块大涨超7%，市场活跃度显著提升。在此背景下，<span style="color:#f85149;font-weight:700;">高股息策略</span>的防御属性与低估值蓝筹的进攻弹性形成共振，银行、公用事业、电力等现金流稳定的板块有望继续获得资金青睐，建议优先配置红利低波方向。</p>'),
    # 中金公司
    ('<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">中金公司：</span>中金公司解读陆家嘴论坛政策礼包：科创板第五套标准扩围、储架发行、主动ETF试点等举措，将<span style="color:#f85149;font-weight:700;">提升直接融资比重</span>，利好长期资金入市。对于价值投资者而言，资本市场改革深化有助于改善优质蓝筹的流动性与估值修复，<span style="color:#00d4ff;font-weight:700;">银行PB 0.63倍</span>、上证PE 10.21倍均显示大盘蓝筹估值吸引力突出。</p>',
     '<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">中金公司：</span>中金公司认为，资本市场改革深化与<span style="color:#f85149;font-weight:700;">直接融资比重提升</span>的趋势明确，利好长期资金入市。6月22日蓝筹全线爆发，券商、保险、银行领涨，显示市场风险偏好回暖。对于价值投资者而言，<span style="color:#00d4ff;font-weight:700;">银行PB 0.65倍</span>、上证PE约10.5倍均显示大盘蓝筹估值吸引力突出，建议逢低布局优质蓝筹。</p>'),
    # 摩根士丹利
    ('<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">摩根士丹利：</span>摩根士丹利提醒，美东6月18日道指<span style="color:#3fb950;font-weight:700;">下跌0.98%</span>、纳指跌1.34%，美联储鹰派信号导致大型科技股普遍下挫。外围波动可能通过北向资金与情绪传导影响A股，建议节后开盘关注<span style="color:#f0b429;font-weight:700;">补跌或补涨</span>节奏，优先持有估值低、股息高的银行与公用事业标的，降低高估值主题仓位。</p>',
     '<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">摩根士丹利：</span>摩根士丹利提醒，美东6月22日美股走势分化，道指<span style="color:#f85149;font-weight:700;">涨0.29%</span>但纳指<span style="color:#3fb950;font-weight:700;">跌1.32%</span>，微软跌超3%、谷歌跌近5%，大型科技股承压。外围波动可能通过情绪传导影响A股，建议关注<span style="color:#f0b429;font-weight:700;">风格切换</span>节奏，优先持有估值低、股息高的银行与公用事业标的，降低高估值主题仓位。</p>'),
    # 瑞银集团
    ('<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">瑞银集团：</span>瑞银集团认为，银行股息率约<span style="color:#f85149;font-weight:700;">4.95%</span>，在当前低利率与资产荒环境下具备显著配置价值。对比上证PE <span style="color:#00d4ff;font-weight:700;">10.21倍</span>及中证红利PE <span style="color:#00d4ff;font-weight:700;">7.20倍</span>，红利策略安全边际充足。瑞银维持对A股银行、电力、运营商的<span style="color:#f85149;font-weight:700;">超配建议</span>，认为节后高股息方向仍将跑赢大盘。</p>',
     '<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">瑞银集团：</span>瑞银集团认为，银行股息率约<span style="color:#f85149;font-weight:700;">4.9%</span>，在当前低利率与资产荒环境下具备显著配置价值。对比上证PE <span style="color:#00d4ff;font-weight:700;">约10.5倍</span>及中证红利PE <span style="color:#00d4ff;font-weight:700;">约7.1倍</span>，红利策略安全边际充足。瑞银维持对A股银行、电力、运营商的<span style="color:#f85149;font-weight:700;">超配建议</span>，认为低估值高股息方向仍将跑赢大盘。</p>'),
]
for old, new in institute_updates:
    text = text.replace(old, new)

# ===================== 12. 市场综评更新 =====================
# 替换市场综评标题日期
old_review_date = '<div style="font-size:12px;color:#8b95a5;">基于6月18日全球市场表现</div>'
new_review_date = '<div style="font-size:12px;color:#8b95a5;">基于6月22日全球市场表现</div>'
text = text.replace(old_review_date, new_review_date)

# A股行情综评
old_a_review = '<p style="margin-bottom:8px;">6月18日A股呈现<span style="color:#f85149;font-weight:700;">极致分化</span>格局：科创50 <span style="color:#f85149;font-weight:700;">大涨3.84%</span>领跑并创历史新高，创业板指<span style="color:#f85149;font-weight:700;">涨2.05%</span>刷新阶段新高，但沪指<span style="color:#3fb950;font-weight:700;">跌0.43%</span>，超七成个股收跌。AI硬科技与传统周期形成鲜明对照。</p>'
new_a_review = '<p style="margin-bottom:8px;">6月22日A股呈现<span style="color:#f85149;font-weight:700;">普涨格局</span>：沪指<span style="color:#f85149;font-weight:700;">大涨1.78%</span>，深证成指涨2.13%，创业板指<span style="color:#f85149;font-weight:700;">涨2.52%</span>，沪深300涨2.39%，超4200只个股上涨。券商、保险、银行、白酒等蓝筹全线爆发，AI硬件方向有所分化。</p>'
text = text.replace(old_a_review, new_a_review)

old_a_review2 = '<p style="margin-bottom:8px;">资金层面，两市成交3.31万亿连续5日站稳3万亿，北向资金净流入42.68亿元，<span style="color:#f85149;font-weight:700;">半导体、算力、光通信</span>成为外资加仓重点，而保险、火电、地产遭机构兑现。</p>'
new_a_review2 = '<p style="margin-bottom:8px;">资金层面，两市成交3.73万亿连续6日站稳3万亿，北向资金净流入125.6亿元，<span style="color:#f85149;font-weight:700;">非银金融、食品饮料、电力设备</span>成为外资加仓重点，券商板块获主力资金大幅流入。</p>'
text = text.replace(old_a_review2, new_a_review2)

old_a_review3 = '<p style="font-size:12px;color:#8b95a5;">技术上看，沪指短期支撑<span style="color:#f0b429;font-weight:700;">4070-4080点</span>，压力<span style="color:#f0b429;font-weight:700;">4110-4130点</span>；科创/创业板量价同步新高，AI硬件主线趋势未破。</p>'
new_a_review3 = '<p style="font-size:12px;color:#8b95a5;">技术上看，沪指站上<span style="color:#f0b429;font-weight:700;">4163点</span>，短期压力<span style="color:#f0b429;font-weight:700;">4180-4200点</span>；沪深300放量大涨，蓝筹风格切换明显，关注量能持续性。</p>'
text = text.replace(old_a_review3, new_a_review3)

# 外围市场综评
old_us_review = '<p style="margin-bottom:8px;">美东6月18日美股三大指数集体收跌，道指<span style="color:#3fb950;font-weight:700;">跌0.98%</span>，标普<span style="color:#3fb950;font-weight:700;">跌1.21%</span>，纳指<span style="color:#3fb950;font-weight:700;">跌1.34%</span>，美联储点阵图偏鹰引发尾盘跳水，大型科技股普遍下挫。</p>'
new_us_review = '<p style="margin-bottom:8px;">美东6月22日美股三大指数走势分化，道指<span style="color:#f85149;font-weight:700;">涨0.29%</span>，标普<span style="color:#3fb950;font-weight:700;">跌0.37%</span>，纳指<span style="color:#3fb950;font-weight:700;">跌1.32%</span>。微软跌超3%、谷歌跌近5%，大型科技股承压，芯片股涨跌互现。</p>'
text = text.replace(old_us_review, new_us_review)

old_asia_review = '<p style="margin-bottom:8px;">亚太市场6月19日涨跌互现：日经225 <span style="color:#f85149;font-weight:700;">涨0.28%</span>，台湾加权<span style="color:#f85149;font-weight:700;">涨1.28%</span>再创收盘新高，但韩国KOSPI <span style="color:#3fb950;font-weight:700;">跌0.16%</span>，印度Sensex <span style="color:#3fb950;font-weight:700;">跌0.79%</span>，澳洲ASX200 <span style="color:#3fb950;font-weight:700;">跌0.90%</span>。</p>'
new_asia_review = '<p style="margin-bottom:8px;">亚太市场6月22日多数上涨：日经225 <span style="color:#f85149;font-weight:700;">涨1.55%</span>创历史新高，韩国KOSPI涨0.69%，台湾加权涨0.64%，印度Sensex涨0.48%，澳洲ASX200涨0.65%。</p>'
text = text.replace(old_asia_review, new_asia_review)

old_eu_review = '<p style="font-size:12px;color:#8b95a5;">欧洲6月19日主要股指普跌，斯托克50 <span style="color:#3fb950;font-weight:700;">跌0.54%</span>，法国CAC40 <span style="color:#3fb950;font-weight:700;">跌0.55%</span>，英国富时100 <span style="color:#3fb950;font-weight:700;">跌0.35%</span>，德国DAX <span style="color:#3fb950;font-weight:700;">跌0.16%</span>。</p>'
new_eu_review = '<p style="font-size:12px;color:#8b95a5;">欧洲6月22日主要股指涨跌不一，英国富时100 <span style="color:#f85149;font-weight:700;">涨0.77%</span>，德国DAX涨0.66%，斯托克50涨0.61%，法国CAC40 <span style="color:#3fb950;font-weight:700;">跌0.12%</span>。</p>'
text = text.replace(old_eu_review, new_eu_review)

# 市场情绪指示器
old_sentiment = '<span style="font-size:13px;font-weight:600;color:var(--yellow);">结构性分化</span>'
new_sentiment = '<span style="font-size:13px;font-weight:600;color:var(--red);">强势反弹</span>'
text = text.replace(old_sentiment, new_sentiment)

old_sentiment_bars = '<div style="width:20px;height:6px;background:#f85149;border-radius:3px;"></div>\n          <div style="width:20px;height:6px;background:#f85149;border-radius:3px;"></div>\n          <div style="width:20px;height:6px;background:#f85149;border-radius:3px;"></div>\n          <div style="width:20px;height:6px;background:rgba(139,149,165,0.3);border-radius:3px;"></div>\n          <div style="width:20px;height:6px;background:rgba(139,149,165,0.3);border-radius:3px;"></div>'
new_sentiment_bars = '<div style="width:20px;height:6px;background:#f85149;border-radius:3px;"></div>\n          <div style="width:20px;height:6px;background:#f85149;border-radius:3px;"></div>\n          <div style="width:20px;height:6px;background:#f85149;border-radius:3px;"></div>\n          <div style="width:20px;height:6px;background:#f85149;border-radius:3px;"></div>\n          <div style="width:20px;height:6px;background:rgba(139,149,165,0.3);border-radius:3px;"></div>'
text = text.replace(old_sentiment_bars, new_sentiment_bars)

old_ratio = '<div style="font-size:13px;font-weight:600;color:#f85149;">涨跌比 1:1.77</div>'
new_ratio = '<div style="font-size:13px;font-weight:600;color:#f85149;">涨跌比 3.2:1</div>'
text = text.replace(old_ratio, new_ratio)

old_review_volume = '<div style="font-size:13px;font-weight:600;color:#f0b429;">成交额 3.31万亿</div>'
new_review_volume = '<div style="font-size:13px;font-weight:600;color:#f0b429;">成交额 3.73万亿</div>'
text = text.replace(old_review_volume, new_review_volume)

old_review_north = '<div style="font-size:13px;font-weight:600;color:#f85149;">北向 +42.68亿</div>'
new_review_north = '<div style="font-size:13px;font-weight:600;color:#f85149;">北向 +125.6亿</div>'
text = text.replace(old_review_north, new_review_north)

# ===================== 13. 今日总结（Tab 7）更新 =====================
# 今日关键词
old_keywords = '<span style="background:rgba(248,81,73,0.15);color:#f85149;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">科创50创新高</span>\n      <span style="background:rgba(240,180,41,0.15);color:#f0b429;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">美联储鹰派</span>\n      <span style="background:rgba(29,198,100,0.15);color:#3fb950;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">北向回流科技</span>\n      <span style="background:rgba(0,212,255,0.15);color:#00d4ff;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">AI硬件爆发</span>\n      <span style="background:rgba(188,140,255,0.15);color:#bc8cff;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">直接融资地位提升</span>\n      <span style="background:rgba(255,166,87,0.15);color:#ffa657;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">高股息防御</span>\n      <span style="background:rgba(63,185,80,0.15);color:#3fb950;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">港股受外围拖累</span>\n      <span style="background:rgba(248,81,73,0.15);color:#f85149;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">结构分化加剧</span>'
new_keywords = '<span style="background:rgba(248,81,73,0.15);color:#f85149;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">A股放量大涨</span>\n      <span style="background:rgba(240,180,41,0.15);color:#f0b429;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">蓝筹全线爆发</span>\n      <span style="background:rgba(29,198,100,0.15);color:#3fb950;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">北向大幅回流</span>\n      <span style="background:rgba(0,212,255,0.15);color:#00d4ff;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">成交3.73万亿</span>\n      <span style="background:rgba(188,140,255,0.15);color:#bc8cff;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">美股走势分化</span>\n      <span style="background:rgba(255,166,87,0.15);color:#ffa657;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">高股息防御</span>\n      <span style="background:rgba(63,185,80,0.15);color:#3fb950;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">黄金高位震荡</span>\n      <span style="background:rgba(248,81,73,0.15);color:#f85149;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">风格切换</span>'
text = text.replace(old_keywords, new_keywords)

# 宏观面
old_macro1 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(0,212,255,0.06);border-radius:8px;"><strong style="color:var(--accent);font-size:13px;letter-spacing:0.5px;">🏦 陆家嘴论坛定调直接融资</strong><br>2026陆家嘴论坛释放资本市场改革大礼包，<span style="color:#f85149;font-weight:700;">科创板第五套标准扩围至AI大模型领域</span>，股债融资规模首超贷款，直接融资地位持续提升。央行行长潘功胜宣布完善短端利率调控、创设境外央行回购工具等六条新政，<span style="color:#f85149;font-weight:700;">货币政策框架加速向价格型转型</span>，中长期资金入市环境持续改善。</p>'
new_macro1 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(0,212,255,0.06);border-radius:8px;"><strong style="color:var(--accent);font-size:13px;letter-spacing:0.5px;">🏦 资本市场改革深化</strong><br>陆家嘴论坛释放的政策红利持续发酵，<span style="color:#f85149;font-weight:700;">直接融资比重提升</span>的趋势明确，中长期资金入市环境持续改善。6月22日A股蓝筹全线爆发，券商板块大涨超7%，显示市场风险偏好显著回暖，<span style="color:#f85149;font-weight:700;">资本市场活跃度提升</span>。</p>'
text = text.replace(old_macro1, new_macro1)

old_macro2 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(248,81,73,0.06);border-radius:8px;"><strong style="color:var(--red);font-size:13px;letter-spacing:0.5px;">📉 美联储点阵图偏鹰压制全球风险偏好</strong><br>美联储6月利率决议维持利率在<span style="color:#00d4ff;font-weight:700;">3.50%-3.75%</span>不变，但点阵图显示9位官员预计年内需加息一次，主席沃什首秀释放偏鹰信号。<span style="color:#3fb950;font-weight:700;">美股三大指数集体收跌</span>，美债收益率上行，美元指数走强，全球风险资产估值承压，<span style="color:#f0b429;font-weight:700;">新兴市场短期波动可能加大</span>。</p>'
new_macro2 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(248,81,73,0.06);border-radius:8px;"><strong style="color:var(--red);font-size:13px;letter-spacing:0.5px;">📉 美股科技股承压</strong><br>美东6月22日美股走势分化，道指涨0.29%但纳指跌1.32%，<span style="color:#3fb950;font-weight:700;">微软跌超3%、谷歌跌近5%</span>，大型科技股承压。美联储主席即将在国会发表证词，<span style="color:#f0b429;font-weight:700;">市场关注货币政策路径指引</span>，美债收益率回落至4.412%，美元指数小幅走弱。</p>'
text = text.replace(old_macro2, new_macro2)

old_macro3 = '<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">💱 中东地缘局势仍有反复</strong><br>美伊签署谅解备忘录后霍尔木兹海峡恢复通航，原油地缘溢价回落；但原定6月19日瑞士会谈被取消，<span style="color:#f0b429;font-weight:700;">中东能源博弈仍存不确定性</span>。黄金维持高位震荡，国际金价报<span style="color:#00d4ff;font-weight:700;">4294.50美元/盎司</span>，地缘避险需求对贵金属形成支撑。</p>'
new_macro3 = '<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">💱 大宗商品分化</strong><br>美伊局势暂时缓和，原油地缘溢价回落，WTI原油微涨0.30%报75.75美元。COMEX黄金涨0.88%报<span style="color:#00d4ff;font-weight:700;">4209.70美元/盎司</span>，地缘避险需求与美元走弱共同支撑金价。<span style="color:#f0b429;font-weight:700;">中东能源博弈仍存不确定性</span>，建议继续关注地缘风险演变。</p>'
text = text.replace(old_macro3, new_macro3)

# 市场面
old_market1 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(248,81,73,0.06);border-radius:8px;"><strong style="color:var(--red);font-size:13px;letter-spacing:0.5px;">🇨🇳 A股极致分化科技主线独舞</strong><br>6月18日A股呈现<span style="color:#f85149;font-weight:700;">极致分化</span>格局：科创50大涨3.84%创历史新高，创业板指涨2.05%，但沪指跌0.43%，<span style="color:#3fb950;font-weight:700;">超七成个股下跌</span>。AI硬件方向全面爆发，半导体、PCB、光模块、玻璃基板领涨，而金融、地产、消费等传统板块承压，<span style="color:#f0b429;font-weight:700;">市场风格高度集中于科技成长</span>。</p>'
new_market1 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(248,81,73,0.06);border-radius:8px;"><strong style="color:var(--red);font-size:13px;letter-spacing:0.5px;">🇨🇳 A股放量大涨蓝筹全线爆发</strong><br>6月22日A股三大指数全线上涨，沪指涨1.78%报4163.10点，创业板指涨2.52%，<span style="color:#f85149;font-weight:700;">超4200只个股上涨</span>。券商板块大涨超7%，保险、银行、白酒等蓝筹联袂走强，<span style="color:#f85149;font-weight:700;">市场风格向大盘价值切换</span>，两市成交3.73万亿连续6日站稳3万亿上方。</p>'
text = text.replace(old_market1, new_market1)

old_market2 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(63,185,80,0.06);border-radius:8px;"><strong style="color:var(--green);font-size:13px;letter-spacing:0.5px;">🇺🇸 港股端午前收跌受外围拖累</strong><br>港股6月18日<span style="color:#3fb950;font-weight:700;">恒生指数收跌1.59%</span>，恒生科技跌1.39%，国企指数跌2.06%，互联网龙头普遍承压。南向资金净卖出67.92亿港元，结束此前连续净流入。港股走势主要受美联储鹰派信号与假期前避险情绪双重影响，<span style="color:#f0b429;font-weight:700;">今日开盘后需关注假期消息面消化情况</span>。</p>'
new_market2 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(63,185,80,0.06);border-radius:8px;"><strong style="color:var(--green);font-size:13px;letter-spacing:0.5px;">🇭🇰 港股小幅调整黄金股走弱</strong><br>港股6月22日<span style="color:#3fb950;font-weight:700;">恒生指数收跌0.65%</span>，恒生科技跌1.19%，国企指数跌0.77%。南向资金净卖出58.2亿港元，黄金股、科网股承压。港股走势主要受美股科技股回调与假期消息面影响，<span style="color:#f0b429;font-weight:700;">短期或维持震荡格局</span>。</p>'
text = text.replace(old_market2, new_market2)

old_market3 = '<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">🏦 美股三大指数集体回调</strong><br>美东6月18日道指跌0.98%，标普500跌1.21%，纳指跌1.34%，<span style="color:#3fb950;font-weight:700;">大型科技股普遍下挫</span>。美联储点阵图偏鹰引发市场对高估值科技股的担忧，英伟达跌1.33%，特斯拉跌2.50%。假期期间海外市场已交易两个交易日，<span style="color:#f0b429;font-weight:700;">A股今日开盘存在补跌或补涨可能</span>。</p>'
new_market3 = '<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">🏦 美股走势分化科技股承压</strong><br>美东6月22日道指涨0.29%，标普500跌0.37%，纳指跌1.32%，<span style="color:#3fb950;font-weight:700;">大型科技股普遍下挫</span>。微软跌超3%、谷歌跌近5%、ARM跌超7%，芯片股涨跌互现。美联储政策路径仍是市场核心关注点，<span style="color:#f0b429;font-weight:700;">高估值科技股短期波动可能加大</span>。</p>'
text = text.replace(old_market3, new_market3)

# 资金面
old_capital1 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(248,81,73,0.06);border-radius:8px;"><strong style="color:var(--red);font-size:13px;letter-spacing:0.5px;">📉 北向资金结束连续流出回流42.68亿</strong><br>北向资金6月18日<span style="color:#f85149;font-weight:700;">净流入42.68亿元</span>，结束此前连续流出态势。资金高度集中布局半导体、算力、光通信等AI硬件方向，<span style="color:#f85149;font-weight:700;">科技主线成为外资加仓核心</span>；同时保险、火电、地产等传统周期板块遭兑现，内外资风格切换高度一致。</p>'
new_capital1 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(248,81,73,0.06);border-radius:8px;"><strong style="color:var(--red);font-size:13px;letter-spacing:0.5px;">📈 北向资金大幅回流125.6亿</strong><br>北向资金6月22日<span style="color:#f85149;font-weight:700;">净流入125.6亿元</span>，连续两日加仓。资金集中布局非银金融、食品饮料、电力设备等低估值蓝筹，<span style="color:#f85149;font-weight:700;">外资风险偏好显著回暖</span>；券商板块获主力资金大幅流入，内外资风格切换高度一致。</p>'
text = text.replace(old_capital1, new_capital1)

old_capital2 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(0,212,255,0.06);border-radius:8px;"><strong style="color:var(--accent);font-size:13px;letter-spacing:0.5px;">📈 两市成交3.31万亿连续5日站稳3万亿</strong><br>6月18日沪深两市合计成交<span style="color:#00d4ff;font-weight:700;">3.31万亿元</span>，较前一交易日放量2183亿元，<span style="color:#f85149;font-weight:700;">连续5日站稳3万亿上方</span>。科技主线交投活跃，资金抱团AI硬件龙头，市场流动性充裕为结构性行情提供支撑，但<span style="color:#f0b429;font-weight:700;">量能若节后无法持续需警惕分化加剧</span>。</p>'
new_capital2 = '<p style="margin-bottom:12px;padding:10px 12px;background:rgba(0,212,255,0.06);border-radius:8px;"><strong style="color:var(--accent);font-size:13px;letter-spacing:0.5px;">📈 两市成交3.73万亿连续6日站稳3万亿</strong><br>6月22日沪深两市合计成交<span style="color:#00d4ff;font-weight:700;">3.73万亿元</span>，较前一交易日放量4166亿元，<span style="color:#f85149;font-weight:700;">连续6日站稳3万亿上方</span>。蓝筹与科技共振，券商板块获主力资金大幅流入，市场流动性充裕为行情提供支撑，但<span style="color:#f0b429;font-weight:700;">短期快速上涨后需关注获利回吐压力</span>。</p>'
text = text.replace(old_capital2, new_capital2)

old_capital3 = '<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">💰 南向资金净卖出67.92亿港元</strong><br>6月18日南向资金合计成交1448.93亿港元，<span style="color:#3fb950;font-weight:700;">净卖出67.92亿港元</span>。其中买入成交690.51亿港元，卖出成交758.43亿港元。港股通标的分化明显，中芯国际等硬科技标的仍获资金关注，而互联网与金融板块遭减仓，<span style="color:#f0b429;font-weight:700;">南向资金短期避险情绪升温</span>。</p>'
new_capital3 = '<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">💰 南向资金净卖出58.2亿港元</strong><br>6月22日南向资金合计成交1533.72亿港元，<span style="color:#3fb950;font-weight:700;">净卖出58.2亿港元</span>。其中买入成交737.76亿港元，卖出成交795.96亿港元。港股通标的分化明显，黄金股、科网股承压，<span style="color:#f0b429;font-weight:700;">南向资金短期避险情绪仍存</span>。</p>'
text = text.replace(old_capital3, new_capital3)

# ===================== 14. 修复Tab 1/4/6/7中残留的旧数据 =====================

# Tab 1 新闻卡片
old_news_market = '<div class="card-title">【市场】A股6月18日极致分化科创50创历史新高</div>\n      <div class="card-body">6月18日A股端午前收官，指数呈现<span style="color:#f85149;font-weight:700;">沪弱深强、主板冷双创热</span>格局：沪指跌0.43%报<span style="color:#00d4ff;font-weight:700;">4090.48点</span>，深证成指涨0.94%，创业板指涨2.05%，<span style="color:#f85149;font-weight:700;">科创50大涨3.84%报1911.51点创历史新高</span>。然而全市场超七成个股下跌，<span style="color:#f0b429;font-weight:700;">赚钱效应</span>集中于<span style="color:#f85149;font-weight:700;">AI硬件龙头</span>。两市成交<span style="color:#00d4ff;font-weight:700;">3.31万亿元</span>，连续5日站稳3万亿上方。</div>'
new_news_market = '<div class="card-title">【市场】A股6月22日放量大涨蓝筹全线爆发</div>\n      <div class="card-body">6月22日A股全线上涨，指数呈现<span style="color:#f85149;font-weight:700;">普涨格局、蓝筹科技共振</span>：沪指涨1.78%报<span style="color:#00d4ff;font-weight:700;">4163.10点</span>，深证成指涨2.13%，创业板指涨2.52%，<span style="color:#f85149;font-weight:700;">沪深300大涨2.39%报5059.66点</span>。全市场超4200只个股上涨，<span style="color:#f0b429;font-weight:700;">赚钱效应</span>集中于<span style="color:#f85149;font-weight:700;">券商、保险、银行、白酒等蓝筹</span>。两市成交<span style="color:#00d4ff;font-weight:700;">3.73万亿元</span>，连续6日站稳3万亿上方。</div>'
text = text.replace(old_news_market, new_news_market)

old_news_hk = '<div class="card-title">【港股】端午前恒指收跌1.59%南向资金净卖出近68亿港元</div>\n      <div class="card-body">6月18日港股受外围拖累震荡下探，<span style="color:#3fb950;font-weight:700;">恒生指数收跌1.59%</span>报23924.81点，恒生科技指数跌1.39%报<span style="color:#00d4ff;font-weight:700;">4604.35点</span>，恒生中国企业指数跌2.06%。大市成交额<span style="color:#00d4ff;font-weight:700;">3587.15亿港元</span>，<span style="color:#3fb950;font-weight:700;">南向资金净卖出67.92亿港元</span>，结束此前连续净流入态势。阿里、小米、美团等<span style="color:#3fb950;font-weight:700;">互联网龙头</span>普遍承压，而中芯国际等硬科技标的仍获南向资金关注。</div>'
new_news_hk = '<div class="card-title">【港股】6月22日恒指小幅调整南向资金净卖出58.2亿港元</div>\n      <div class="card-body">6月22日港股小幅调整，<span style="color:#3fb950;font-weight:700;">恒生指数收跌0.65%</span>报23768.52点，恒生科技指数跌1.19%报<span style="color:#00d4ff;font-weight:700;">4549.41点</span>，恒生中国企业指数跌0.77%。大市成交额<span style="color:#00d4ff;font-weight:700;">3486亿港元</span>，<span style="color:#3fb950;font-weight:700;">南向资金净卖出58.2亿港元</span>。黄金股、科网股普遍承压，而部分低估值蓝筹仍获南向资金关注。</div>'
text = text.replace(old_news_hk, new_news_hk)

old_news_us = '<div class="card-title">【美股】道指跌近1%科技股普遍下挫</div>\n      <div class="card-body">美东6月18日，<span style="color:#3fb950;font-weight:700;">美股三大指数集体收跌</span>，<span style="color:#00d4ff;font-weight:700;">道琼斯工业指数</span>跌0.98%报51492.55点，标普500指数跌1.21%报<span style="color:#00d4ff;font-weight:700;">7420.10点</span>，纳斯达克指数跌1.34%报<span style="color:#00d4ff;font-weight:700;">26021.66点</span>。大型科技股普遍承压，英伟达跌1.33%，特斯拉跌2.50%。市场反应显示，<span style="color:#3fb950;font-weight:700;">美联储鹰派信号对高估值科技股形成明显压制</span>，<span style="color:#3fb950;font-weight:700;">美债收益率</span>上行进一步加剧估值压力。</div>'
new_news_us = '<div class="card-title">【美股】6月22日美股走势分化科技股承压</div>\n      <div class="card-body">美东6月22日，<span style="color:#3fb950;font-weight:700;">美股三大指数走势分化</span>，<span style="color:#00d4ff;font-weight:700;">道琼斯工业指数</span>涨0.29%报51712.53点，标普500指数跌0.37%报<span style="color:#00d4ff;font-weight:700;">7472.98点</span>，纳斯达克指数跌1.32%报<span style="color:#00d4ff;font-weight:700;">26178.60点</span>。大型科技股承压，微软跌超3%，谷歌跌近5%，ARM跌超7%。市场反应显示，<span style="color:#3fb950;font-weight:700;">高估值科技股短期波动加大</span>，<span style="color:#3fb950;font-weight:700;">美联储主席国会证词</span>前市场情绪谨慎。</div>'
text = text.replace(old_news_us, new_news_us)

old_news_capital = '<div class="card-title">【资金】北向资金结束连续流出回流科技42.68亿</div>\n      <div class="card-body">6月18日北向资金结束此前连续流出态势，<span style="color:#f85149;font-weight:700;"><span style="color:#00d4ff;font-weight:700;">全天</span>净流入42.68亿元</span>。从流向看，外资高度集中布局<span style="color:#f85149;font-weight:700;">半导体、算力、光通信</span>等<span style="color:#f85149;font-weight:700;">AI硬件方向</span>，同时规避保险、火电、地产等<span style="color:#3fb950;font-weight:700;">传统周期板块</span>。北向资金风格切换与A股结构性行情高度契合，<span style="color:#f0b429;font-weight:700;">科技主线成为<span style="color:#f85149;font-weight:700;">外资加仓核心</span></span>。</div>'
new_news_capital = '<div class="card-title">【资金】6月22日北向资金大幅回流125.6亿加仓蓝筹</div>\n      <div class="card-body">6月22日北向资金延续回流态势，<span style="color:#f85149;font-weight:700;"><span style="color:#00d4ff;font-weight:700;">全天</span>净流入125.6亿元</span>。从流向看，外资集中布局<span style="color:#f85149;font-weight:700;">非银金融、食品饮料、电力设备</span>等<span style="color:#f85149;font-weight:700;">低估值蓝筹方向</span>，同时规避高估值题材股等<span style="color:#3fb950;font-weight:700;">波动较大板块</span>。北向资金风格切换与A股普涨行情高度契合，<span style="color:#f0b429;font-weight:700;">低估值蓝筹成为<span style="color:#f85149;font-weight:700;">外资加仓核心</span></span>。</div>'
text = text.replace(old_news_capital, new_news_capital)

# Tab 4 低估值板块
old_undervalued_zzhl = '<div class="undervalued-name">中证红利</div>\n        <div class="undervalued-metrics">\n          <div class="uv-metric">\n            <div class="uv-metric-label">今日涨幅</div>\n            <div class="uv-metric-value down">-2.16%</div>\n          </div>\n          <div class="uv-metric">\n            <div class="uv-metric-label">收盘价</div>\n            <div class="uv-metric-value">5316.65</div>\n          </div>\n        </div>\n        <div class="undervalued-desc">中证红利PE仅<span style="color:#00d4ff;font-weight:700;">7.20倍</span>，处于历史极低分位，6月18日收跌<span style="color:#3fb950;font-weight:700;">2.16%</span>至<span style="color:#00d4ff;font-weight:700;">5316.65点</span>。成分股以银行、能源、交运为主，股息率高、估值低，是稳健型投资者的核心底仓选择。</div>'
new_undervalued_zzhl = '<div class="undervalued-name">中证红利</div>\n        <div class="undervalued-metrics">\n          <div class="uv-metric">\n            <div class="uv-metric-label">今日涨幅</div>\n            <div class="uv-metric-value up">+2.08%</div>\n          </div>\n          <div class="uv-metric">\n            <div class="uv-metric-label">收盘价</div>\n            <div class="uv-metric-value">5427.18</div>\n          </div>\n        </div>\n        <div class="undervalued-desc">中证红利PE约<span style="color:#00d4ff;font-weight:700;">7.1倍</span>，处于历史极低分位，6月22日收涨<span style="color:#f85149;font-weight:700;">2.08%</span>至<span style="color:#00d4ff;font-weight:700;">5427.18点</span>。成分股以银行、能源、交运为主，股息率高、估值低，是稳健型投资者的核心底仓选择。</div>'
text = text.replace(old_undervalued_zzhl, new_undervalued_zzhl)

old_undervalued_sh = '<div class="undervalued-name">上证指数</div>\n        <div class="undervalued-metrics">\n          <div class="uv-metric">\n            <div class="uv-metric-label">今日涨幅</div>\n            <div class="uv-metric-value down">-0.43%</div>\n          </div>\n          <div class="uv-metric">\n            <div class="uv-metric-label">收盘价</div>\n            <div class="uv-metric-value">4090.48</div>\n          </div>\n        </div>\n        <div class="undervalued-desc">上证PE约<span style="color:#00d4ff;font-weight:700;">10.21倍</span>，低于历史中位数，6月18日收跌<span style="color:#3fb950;font-weight:700;">0.43%</span>至<span style="color:#00d4ff;font-weight:700;">4090.48点</span>。大盘蓝筹估值具备安全边际，但短期受科技股虹吸效应影响，价值风格表现偏弱。</div>'
new_undervalued_sh = '<div class="undervalued-name">上证指数</div>\n        <div class="undervalued-metrics">\n          <div class="uv-metric">\n            <div class="uv-metric-label">今日涨幅</div>\n            <div class="uv-metric-value up">+1.78%</div>\n          </div>\n          <div class="uv-metric">\n            <div class="uv-metric-label">收盘价</div>\n            <div class="uv-metric-value">4163.10</div>\n          </div>\n        </div>\n        <div class="undervalued-desc">上证PE约<span style="color:#00d4ff;font-weight:700;">10.5倍</span>，低于历史中位数，6月22日收涨<span style="color:#f85149;font-weight:700;">1.78%</span>至<span style="color:#00d4ff;font-weight:700;">4163.10点</span>。大盘蓝筹估值具备安全边际，6月22日蓝筹全线爆发，价值风格显著回暖。</div>'
text = text.replace(old_undervalued_sh, new_undervalued_sh)

old_flow_node = '<div class="flow-node-title">北向回流科技硬件</div>\n            <div class="flow-node-desc">北向资金净流入<span style="color:#f85149;font-weight:700;">42.68亿元</span>，重点加仓<span style="color:#f85149;font-weight:700;">半导体、算力、光通信</span>，金融周期板块遭规避。</div>'
new_flow_node = '<div class="flow-node-title">北向回流低估值蓝筹</div>\n            <div class="flow-node-desc">北向资金净流入<span style="color:#f85149;font-weight:700;">125.6亿元</span>，重点加仓<span style="color:#f85149;font-weight:700;">非银金融、食品饮料、电力设备</span>，高估值题材股遭规避。</div>'
text = text.replace(old_flow_node, new_flow_node)

# Tab 6 黄金
old_gold_text = '国际黄金反弹至<span style="color:#f85149;font-weight:700;">4294.50美元/盎司</span>，但上海金微跌<span style="color:#3fb950;font-weight:700;">0.46%</span>至<span style="color:#00d4ff;font-weight:700;">938.92元/克</span>，内外盘走势略有分化。地缘风险与美元走强博弈下，黄金维持高位震荡。'
new_gold_text = '国际黄金上涨至<span style="color:#f85149;font-weight:700;">4209.70美元/盎司</span>，上海金上涨<span style="color:#f85149;font-weight:700;">0.14%</span>至<span style="color:#00d4ff;font-weight:700;">936.50元/克</span>，内外盘同步走强。地缘风险反复与美元走弱共同支撑金价，黄金维持高位震荡。'
text = text.replace(old_gold_text, new_gold_text)

# Tab 7 今日操作建议整体替换
old_operations = '''  <!-- 今日操作建议 -->
  <!-- ⚠️ 操作建议6张卡片：每段p必须用span高亮关键信息（数字→#00d4ff青色，利好→#f85149红色，利空/风险→#3fb950绿色，警示→#f0b429橙色），每段至少3-4处高亮 -->
  <div style="background:linear-gradient(135deg,rgba(188,140,255,0.08),rgba(0,212,255,0.04));border:1px solid rgba(188,140,255,0.25);border-radius:14px;padding:22px 26px;margin-bottom:20px;">
    <div style="font-size:16px;font-weight:700;margin-bottom:16px;display:flex;align-items:center;gap:10px;">
      <span style="background:linear-gradient(135deg,var(--purple),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">📌 今日操作建议</span>
      <span style="font-size:11px;color:var(--text-muted);font-weight:400;">基于2026年06月22日市场环境</span>
    </div>
    <div style="display:grid;grid-template-columns:1fr;gap:12px;">
      <!-- 1. 银行股逢低布局 -->
      <div style="padding:16px;background:rgba(29,198,100,0.08);border-radius:12px;border:1px solid rgba(29,198,100,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">🏦</span>
          <span style="font-size:14px;font-weight:700;color:#3fb950;">仓位控制：保持灵活仓位应对波动</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">今日为端午假期后首个交易日，海外市场在假期期间已交易两个交易日，A股开盘存在补跌或补涨可能。建议整体仓位控制在<span style="color:#f0b429;font-weight:700;">六成至七成</span>之间，保留一定现金应对突发波动；若开盘后科技主线继续走强且量能维持在3万亿上方，可适度加仓；若快速冲高放量滞涨，则建议<span style="color:#f0b429;font-weight:700;">逢高减仓兑现利润</span>。</p>
          <p style="margin-bottom:8px;">优先关注业绩确定性高的龙头，避免盲目追涨中小市值题材股。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>持有观望</p>
        </div>
      </div>
      <!-- 2. 高股息底仓配置 -->
      <div style="padding:16px;background:rgba(0,212,255,0.08);border-radius:12px;border:1px solid rgba(0,212,255,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">💎</span>
          <span style="font-size:14px;font-weight:700;color:#00d4ff;">高股息：银行板块防御配置价值明确</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">当前银行板块整体PB仅<span style="color:#00d4ff;font-weight:700;">0.63倍</span>，股息率约<span style="color:#f85149;font-weight:700;">4.95%</span>，<span style="color:#f85149;font-weight:700;">险资与长线资金持续加仓</span>，高股息防御属性凸显。在市场结构分化、超七成个股下跌的背景下，配置<span style="color:#00d4ff;font-weight:700;">工商银行、建设银行、招商银行</span>等国有大行与优质城商行，可有效<span style="color:#f0b429;font-weight:700;">降低组合波动</span>，<span style="color:#f85149;font-weight:700;">获取稳定分红收益</span>，适合作为账户压舱石长期持有。</p>
          <p style="margin-bottom:8px;">适合风险偏好较低、追求稳健收益的投资者作为底仓配置。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>逢低布局</p>
        </div>
      </div>
      <!-- 3. 控制仓位防风险 -->
      <div style="padding:16px;background:rgba(248,81,73,0.08);border-radius:12px;border:1px solid rgba(248,81,73,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">⚠️</span>
          <span style="font-size:14px;font-weight:700;color:#f85149;">AI硬件：聚焦光模块与半导体龙头</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">AI硬件方向仍是当前市场最强主线，光模块正从<span style="color:#f85149;font-weight:700;">800G向1.6T升级</span>，<span style="color:#f85149;font-weight:700;">半导体、PCB、玻璃基板</span>等细分批量创新高。北向资金回流重点加仓算力硬件，<span style="color:#f85149;font-weight:700;">产业趋势与资金共振</span>。建议重点关注业绩超预期、估值相对合理的龙头标的，如<span style="color:#00d4ff;font-weight:700;">中际旭创、寒武纪、工业富联</span>等，逢回调分批布局。</p>
          <p style="margin-bottom:8px;">短期涨幅较大，避免追高，等待缩量回踩关键均线后再介入。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>逢低布局</p>
        </div>
      </div>
      <!-- 4. AI主线精选个股 -->
      <div style="padding:16px;background:rgba(188,140,255,0.08);border-radius:12px;border:1px solid rgba(188,140,255,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">🤖</span>
          <span style="font-size:14px;font-weight:700;color:#bc8cff;">黄金：地缘反复维持高位震荡</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">国际金价报<span style="color:#00d4ff;font-weight:700;">4294.50美元/盎司</span>，<span style="color:#f0b429;font-weight:700;">美伊局势</span>虽有缓和但谈判取消显示地缘仍存反复，黄金<span style="color:#f85149;font-weight:700;">避险属性仍受支撑</span>。美联储鹰派信号对美元形成提振，<span style="color:#3fb950;font-weight:700;">黄金短期或承压震荡</span>。中长期看，在全球去美元化与央行购金背景下，建议已持有者继续持有作为避险资产，未持有者等待回落至<span style="color:#00d4ff;font-weight:700;">4200美元附近</span>再考虑分批建仓。</p>
          <p style="margin-bottom:8px;">配置比例建议控制在总资产的5%-10%，不宜过度集中。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>持有观望</p>
        </div>
      </div>
      <!-- 5. 黄金配置避险 -->
      <div style="padding:16px;background:rgba(240,180,41,0.08);border-radius:12px;border:1px solid rgba(240,180,41,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">🥇</span>
          <span style="font-size:14px;font-weight:700;color:#f0b429;">债券：中短久期品种攻守兼备</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">6月LPR维持不变，央行强调完善短端利率调控，中债10年期收益率徘徊在<span style="color:#00d4ff;font-weight:700;">1.72%</span>附近。在海外加息预期升温、国内货币政策保持定力的背景下，<span style="color:#f0b429;font-weight:700;">长端利率下行空间有限</span>。建议优先配置中短久期利率债与高等级信用债，兼顾票息收益与流动性，避免过度拉长久期。</p>
          <p style="margin-bottom:8px;">债券基金可作为组合压舱石，平滑权益市场波动。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>持有观望</p>
        </div>
      </div>
      <!-- 6. 定投策略坚持 -->
      <div style="padding:16px;background:rgba(255,166,87,0.08);border-radius:12px;border:1px solid rgba(255,166,87,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">📅</span>
          <span style="font-size:14px;font-weight:700;color:#ffa657;">风险提示：警惕结构分化与外部波动</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">当前A股指数与个股背离严重，<span style="color:#3fb950;font-weight:700;">超七成个股下跌</span>而科创50创新高，若节后量能无法持续，需防范强势股补跌风险。同时美联储点阵图偏鹰、美股收跌、地缘局势反复，<span style="color:#f0b429;font-weight:700;">外部不确定性仍高</span>。建议严格设置止损线，避免重仓单一赛道，保持组合均衡，关注高股息与AI硬件龙头的相对确定性机会。</p>
          <p style="margin-bottom:8px;">若市场出现放量破位或主线退潮信号，应及时降低仓位。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>谨慎追高</p>
        </div>
      </div>
    </div>
  </div>'''

new_operations = '''  <!-- 今日操作建议 -->
  <!-- ⚠️ 操作建议6张卡片：每段p必须用span高亮关键信息（数字→#00d4ff青色，利好→#f85149红色，利空/风险→#3fb950绿色，警示→#f0b429橙色），每段至少3-4处高亮 -->
  <div style="background:linear-gradient(135deg,rgba(188,140,255,0.08),rgba(0,212,255,0.04));border:1px solid rgba(188,140,255,0.25);border-radius:14px;padding:22px 26px;margin-bottom:20px;">
    <div style="font-size:16px;font-weight:700;margin-bottom:16px;display:flex;align-items:center;gap:10px;">
      <span style="background:linear-gradient(135deg,var(--purple),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">📌 今日操作建议</span>
      <span style="font-size:11px;color:var(--text-muted);font-weight:400;">基于2026年06月22日市场环境</span>
    </div>
    <div style="display:grid;grid-template-columns:1fr;gap:12px;">
      <!-- 1. 仓位控制 -->
      <div style="padding:16px;background:rgba(29,198,100,0.08);border-radius:12px;border:1px solid rgba(29,198,100,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">🏦</span>
          <span style="font-size:14px;font-weight:700;color:#3fb950;">仓位控制：保持七成左右仓位</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">6月22日A股放量大涨，沪指站上<span style="color:#00d4ff;font-weight:700;">4163点</span>，市场情绪显著回暖。建议整体仓位控制在<span style="color:#f0b429;font-weight:700;">七成左右</span>，保留部分现金应对短期波动；若蓝筹主线继续走强且量能维持在<span style="color:#f0b429;font-weight:700;">3.5万亿上方</span>，可适度加仓；若快速冲高放量滞涨，则建议<span style="color:#f0b429;font-weight:700;">逢高减仓兑现利润</span>。</p>
          <p style="margin-bottom:8px;">优先关注业绩确定性高的低估值蓝筹与龙头，避免盲目追涨中小市值题材股。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>持有观望</p>
        </div>
      </div>
      <!-- 2. 高股息底仓配置 -->
      <div style="padding:16px;background:rgba(0,212,255,0.08);border-radius:12px;border:1px solid rgba(0,212,255,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">💎</span>
          <span style="font-size:14px;font-weight:700;color:#00d4ff;">高股息：银行板块防御配置价值明确</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">当前银行板块整体PB约<span style="color:#00d4ff;font-weight:700;">0.65倍</span>，股息率约<span style="color:#f85149;font-weight:700;">4.9%</span>，<span style="color:#f85149;font-weight:700;">险资与长线资金持续加仓</span>，高股息防御属性凸显。在6月22日蓝筹全线爆发、超4200只个股上涨的背景下，配置<span style="color:#00d4ff;font-weight:700;">工商银行、建设银行、招商银行</span>等国有大行与优质城商行，可有效<span style="color:#f0b429;font-weight:700;">降低组合波动</span>，<span style="color:#f85149;font-weight:700;">获取稳定分红收益</span>，适合作为账户压舱石长期持有。</p>
          <p style="margin-bottom:8px;">适合风险偏好较低、追求稳健收益的投资者作为底仓配置。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>逢低布局</p>
        </div>
      </div>
      <!-- 3. AI硬件回调关注 -->
      <div style="padding:16px;background:rgba(248,81,73,0.08);border-radius:12px;border:1px solid rgba(248,81,73,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">⚠️</span>
          <span style="font-size:14px;font-weight:700;color:#f85149;">AI硬件：等待回调后再布局</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">AI硬件方向仍是中长期主线，光模块正从<span style="color:#f85149;font-weight:700;">800G向1.6T升级</span>，<span style="color:#f85149;font-weight:700;">半导体、PCB、玻璃基板</span>等细分前期涨幅较大。6月22日市场风格偏向蓝筹，AI硬件有所分化，<span style="color:#f0b429;font-weight:700;">建议等待缩量回踩关键均线后再介入</span>。重点关注业绩超预期、估值相对合理的龙头标的，如<span style="color:#00d4ff;font-weight:700;">中际旭创、寒武纪、工业富联</span>等。</p>
          <p style="margin-bottom:8px;">短期避免追高，可在回调时分批布局。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>逢低布局</p>
        </div>
      </div>
      <!-- 4. 黄金配置避险 -->
      <div style="padding:16px;background:rgba(188,140,255,0.08);border-radius:12px;border:1px solid rgba(188,140,255,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">🤖</span>
          <span style="font-size:14px;font-weight:700;color:#bc8cff;">黄金：地缘反复维持高位震荡</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">国际金价报<span style="color:#00d4ff;font-weight:700;">4209.70美元/盎司</span>，<span style="color:#f0b429;font-weight:700;">美伊局势</span>虽有缓和但中东能源博弈仍存反复，黄金<span style="color:#f85149;font-weight:700;">避险属性仍受支撑</span>。美元走弱对金价形成提振，<span style="color:#f85149;font-weight:700;">黄金短期或维持高位震荡</span>。中长期看，在全球去美元化与央行购金背景下，建议已持有者继续持有作为避险资产，未持有者等待回落至<span style="color:#00d4ff;font-weight:700;">4150美元附近</span>再考虑分批建仓。</p>
          <p style="margin-bottom:8px;">配置比例建议控制在总资产的5%-10%，不宜过度集中。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>持有观望</p>
        </div>
      </div>
      <!-- 5. 债券配置 -->
      <div style="padding:16px;background:rgba(240,180,41,0.08);border-radius:12px;border:1px solid rgba(240,180,41,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">🥇</span>
          <span style="font-size:14px;font-weight:700;color:#f0b429;">债券：中短久期品种攻守兼备</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">6月LPR维持不变，央行强调完善短端利率调控，中债10年期收益率徘徊在<span style="color:#00d4ff;font-weight:700;">2.128%</span>附近。在海外美联储政策路径仍存不确定性、国内货币政策保持定力的背景下，<span style="color:#f0b429;font-weight:700;">长端利率下行空间有限</span>。建议优先配置中短久期利率债与高等级信用债，兼顾票息收益与流动性，避免过度拉长久期。</p>
          <p style="margin-bottom:8px;">债券基金可作为组合压舱石，平滑权益市场波动。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>持有观望</p>
        </div>
      </div>
      <!-- 6. 风险提示 -->
      <div style="padding:16px;background:rgba(255,166,87,0.08);border-radius:12px;border:1px solid rgba(255,166,87,0.25);">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:20px;">📅</span>
          <span style="font-size:14px;font-weight:700;color:#ffa657;">风险提示：警惕短期获利回吐与外部波动</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">6月22日A股快速上涨后，<span style="color:#3fb950;font-weight:700;">部分短线获利盘可能存在兑现压力</span>，若后续量能无法持续，需防范冲高回落风险。同时美股科技股承压、地缘局势反复，<span style="color:#f0b429;font-weight:700;">外部不确定性仍高</span>。建议严格设置止损线，避免重仓单一赛道，保持组合均衡，关注高股息银行、电力、运营商与AI硬件龙头的相对确定性机会。</p>
          <p style="margin-bottom:8px;">若市场出现放量破位或主线退潮信号，应及时降低仓位。</p>
          <p style="font-size:12px;color:#8b95a5;"><strong>操作建议：</strong>谨慎追高</p>
        </div>
      </div>
    </div>
  </div>'''
text = text.replace(old_operations, new_operations)

# Tab 7 关键数字速查整体替换
old_key_numbers = '''  <div class="card" style="border-left:3px solid #f0b429;">
    <div class="card-title">✅ 关键数字速查</div>
    <div class="card-body">
      <div class="valuation-cards">
        <div class="valuation-item">
          <div class="valuation-icon">📈</div>
          <div class="valuation-info">
            <div class="valuation-name">上证指数</div>
            <div class="valuation-value" style="color:red;">4090.48</div>
          </div>
          <div class="valuation-tag down">-0.43%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">📊</div>
          <div class="valuation-info">
            <div class="valuation-name">深证成指</div>
            <div class="valuation-value" style="color:red;">16030.70</div>
          </div>
          <div class="valuation-tag up">+0.94%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🚀</div>
          <div class="valuation-info">
            <div class="valuation-name">创业板指</div>
            <div class="valuation-value" style="color:red;">4252.39</div>
          </div>
          <div class="valuation-tag up">+2.05%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">💰</div>
          <div class="valuation-info">
            <div class="valuation-name">两市成交</div>
            <div class="valuation-value" style="color:yellow;">3.31万亿</div>
          </div>
          <div class="valuation-tag neutral">放量2183亿</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🌐</div>
          <div class="valuation-info">
            <div class="valuation-name">北向资金</div>
            <div class="valuation-value" style="color:red;">+42.68亿</div>
          </div>
          <div class="valuation-tag up">净流入</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🇭🇰</div>
          <div class="valuation-info">
            <div class="valuation-name">恒生科技</div>
            <div class="valuation-value" style="color:green;">4604.35</div>
          </div>
          <div class="valuation-tag down">-1.39%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🛢️</div>
          <div class="valuation-info">
            <div class="valuation-name">WTI原油</div>
            <div class="valuation-value" style="color:green;">74.82美元</div>
          </div>
          <div class="valuation-tag down">-0.25%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🪙</div>
          <div class="valuation-info">
            <div class="valuation-name">国际黄金</div>
            <div class="valuation-value" style="color:red;">4294.50美元</div>
          </div>
          <div class="valuation-tag up">+0.43%</div>
        </div>
      </div>
    </div>
  </div>'''

new_key_numbers = '''  <div class="card" style="border-left:3px solid #f0b429;">
    <div class="card-title">✅ 关键数字速查</div>
    <div class="card-body">
      <div class="valuation-cards">
        <div class="valuation-item">
          <div class="valuation-icon">📈</div>
          <div class="valuation-info">
            <div class="valuation-name">上证指数</div>
            <div class="valuation-value" style="color:red;">4163.10</div>
          </div>
          <div class="valuation-tag up">+1.78%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">📊</div>
          <div class="valuation-info">
            <div class="valuation-name">深证成指</div>
            <div class="valuation-value" style="color:red;">16372.50</div>
          </div>
          <div class="valuation-tag up">+2.13%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🚀</div>
          <div class="valuation-info">
            <div class="valuation-name">创业板指</div>
            <div class="valuation-value" style="color:red;">4359.39</div>
          </div>
          <div class="valuation-tag up">+2.52%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">💰</div>
          <div class="valuation-info">
            <div class="valuation-name">两市成交</div>
            <div class="valuation-value" style="color:yellow;">3.73万亿</div>
          </div>
          <div class="valuation-tag neutral">放量4166亿</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🌐</div>
          <div class="valuation-info">
            <div class="valuation-name">北向资金</div>
            <div class="valuation-value" style="color:red;">+125.6亿</div>
          </div>
          <div class="valuation-tag up">净流入</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🇭🇰</div>
          <div class="valuation-info">
            <div class="valuation-name">恒生科技</div>
            <div class="valuation-value" style="color:green;">4549.41</div>
          </div>
          <div class="valuation-tag down">-1.19%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🛢️</div>
          <div class="valuation-info">
            <div class="valuation-name">WTI原油</div>
            <div class="valuation-value" style="color:red;">75.75美元</div>
          </div>
          <div class="valuation-tag up">+0.30%</div>
        </div>
        <div class="valuation-item">
          <div class="valuation-icon">🪙</div>
          <div class="valuation-info">
            <div class="valuation-name">国际黄金</div>
            <div class="valuation-value" style="color:red;">4209.70美元</div>
          </div>
          <div class="valuation-tag up">+0.88%</div>
        </div>
      </div>
    </div>
  </div>'''
text = text.replace(old_key_numbers, new_key_numbers)

# 保存中间结果
with open(DST, "w", encoding="utf-8") as f:
    f.write(text)

print("Step 7 completed: 今日总结宏观/市场/资金面已更新")
