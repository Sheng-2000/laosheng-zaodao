#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成「老盛早知道」2026年5月21日完整HTML报告
读取template.html，替换所有正文内容，保留CSS和HTML骨架
"""

import re

# 读取模板
with open('/sessions/6a0e68353d587e423c5d8d0d/workspace/template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. 替换 header 区域
# ============================================================

# title
html = html.replace(
    '<title>老盛早知道 · 2026年5月13日</title>',
    '<title>老盛早知道 · 2026年5月21日</title>'
)

# brand-issue
html = html.replace(
    '<span class="brand-issue">#20260513</span>',
    '<span class="brand-issue">#20260521</span>'
)

# hm-date
html = html.replace(
    '<div class="hm-date">2026 / 05 / 13</div>',
    '<div class="hm-date">2026 / 05 / 21</div>'
)

# hm-sub (星期和关键词)
html = html.replace(
    '<div class="hm-sub"><span>星期三</span><span class="sep">|</span><span>特朗普访华首日·美国CPI爆表·美伊冲突持续</span></div>',
    '<div class="hm-sub"><span>星期四</span><span class="sep">|</span><span>中俄元首会谈·长江存储IPO·黄金跌破4500·美股三连跌</span></div>'
)

# ticker 数据
old_tickers = '''<div class="hm-tickers">
          <div class="hm-ticker">
            <span class="t-label">上证</span>
            <span class="t-val down">4214.49</span>
            <span class="t-chg down">-0.25%</span>
          </div>
          <div class="hm-ticker">
            <span class="t-label">标普</span>
            <span class="t-val down">7400.96</span>
            <span class="t-chg down">-0.16%</span>
          </div>
          <div class="hm-ticker">
            <span class="t-label">BTC</span>
            <span class="t-val neutral">$81,400</span>
            <span class="t-chg neutral">震荡</span>
          </div>
        </div>'''

new_tickers = '''<div class="hm-tickers">
          <div class="hm-ticker">
            <span class="t-label">上证</span>
            <span class="t-val down">4162.18</span>
            <span class="t-chg down">-0.18%</span>
          </div>
          <div class="hm-ticker">
            <span class="t-label">标普</span>
            <span class="t-val down">7353</span>
            <span class="t-chg down">-0.67%</span>
          </div>
          <div class="hm-ticker">
            <span class="t-label">BTC</span>
            <span class="t-val down">$77,000</span>
            <span class="t-chg down">破位</span>
          </div>
        </div>'''

html = html.replace(old_tickers, new_tickers)

# ============================================================
# 2. 替换 Tab 0: 要点速览
# ============================================================

tab0_start = '<!-- TAB 0: 要点速览 -->'
tab0_end = '<!-- TAB 1: 国内外新闻 -->'

tab0_content = '''<!-- TAB 0: 要点速览 -->
<div class="tab-panel active" id="panel-0">
  <div class="inner">
  <div class="section-title">⚡ 本期要点速览</div>

  <!-- 顶部提示区 - 2×2网格卡片 -->
  <div class="summary-cards-grid">
    <!-- A股分化卡片 - 黄色 -->
    <div class="summary-card-yellow">
      <div class="summary-card-icon">📊</div>
      <div class="summary-card-content">
        <div class="summary-card-title">A股分化调整</div>
        <div class="summary-card-value">4162.18 <span class="summary-card-change down">-0.18%</span></div>
        <div class="summary-card-desc">上证微跌，科创50大涨3.2%创历史新高，两市成交2.95万亿放量670亿</div>
      </div>
    </div>
    <!-- 美股三连跌卡片 - 红色 -->
    <div class="summary-card-red">
      <div class="summary-card-icon">📉</div>
      <div class="summary-card-content">
        <div class="summary-card-title">美股三连跌</div>
        <div class="summary-card-value">7353 <span class="summary-card-change down">-0.67%</span></div>
        <div class="summary-card-desc">标普纳指三连跌，科技股承压，交易员预计年底前加息概率超80%</div>
      </div>
    </div>
    <!-- 中俄会谈卡片 - 绿色 -->
    <div class="summary-card-green">
      <div class="summary-card-icon">🤝</div>
      <div class="summary-card-content">
        <div class="summary-card-title">中俄元首会谈</div>
        <div class="summary-card-value">条约延期 <span class="summary-card-tag">外交利好</span></div>
        <div class="summary-card-desc">习近平与普京会谈，中俄睦邻友好合作条约继续延期，地缘格局深化</div>
      </div>
    </div>
    <!-- 黄金暴跌卡片 - 蓝色 -->
    <div class="summary-card-blue">
      <div class="summary-card-icon">🥇</div>
      <div class="summary-card-content">
        <div class="summary-card-title">黄金跌破4500美元</div>
        <div class="summary-card-value">~$4500 <span class="summary-card-change down">大幅下跌</span></div>
        <div class="summary-card-desc">国际黄金跌破关键位，国内AU9999跌破千元大关至约992元/克</div>
      </div>
    </div>
  </div>

  <!-- 8个要点卡片 -->
  <div class="highlight-grid-v2">
    <div class="highlight-item-v2">
      <div class="highlight-badge">01</div>
      <div class="highlight-text-v2"><strong>A股结构性分化：科创50大涨3.2%创历史新高：</strong>5/20收盘上证4162.18(-0.18%)微跌，深证成指15569.98平收，创业板指3921.79(+0.34%)收红。但科创50大涨3.2%约1841点创历史新高，半导体/存储芯片/集成电路封测板块掀涨停潮。两市成交2.95万亿放量670亿，但涨跌家数1638:3804跌多涨少，赚钱效应集中在科技方向。北向资金成交3532亿占两市11.96%。</div>
    </div>
    <div class="highlight-item-v2">
      <div class="highlight-badge">02</div>
      <div class="highlight-text-v2"><strong>习近平与普京会谈，中俄条约继续延期：</strong>中俄元首举行重要会谈，中俄睦邻友好合作条约继续延期，两国战略协作伙伴关系进一步深化。这一重大外交事件对全球地缘格局产生深远影响，中俄经贸合作预期升温，能源、基建等领域合作有望加速推进。</div>
    </div>
    <div class="highlight-item-v2">
      <div class="highlight-badge">03</div>
      <div class="highlight-text-v2"><strong>长江存储启动IPO辅导+长鑫科技更新招股书：</strong>长江存储正式启动IPO辅导（中信证券+中信建投联合保荐），长鑫科技更新科创板招股书。两大存储芯片龙头集中冲刺资本市场，叠加港股半导体大涨（兆易创新+17%、华虹半导体+13%、中芯国际+9%），半导体设备需求迎来强催化。</div>
    </div>
    <div class="highlight-item-v2">
      <div class="highlight-badge">04</div>
      <div class="highlight-text-v2"><strong>美股标普纳指三连跌，加息预期升温：</strong>美东5/19收盘，道指49363(-0.65%)，标普500 7353(-0.67%)三连跌，纳指25870(-0.84%)三连跌。科技股多数下跌，谷歌亚马逊跌超2%，高通跌近4%。美国长债收益率持续走高，交易员预计2026年底前加息概率超80%。中概股涨跌不一，拼多多京东涨超2%。</div>
    </div>
    <div class="highlight-item-v2">
      <div class="highlight-badge">05</div>
      <div class="highlight-text-v2"><strong>国际黄金跌破4500美元，国内金价跌破千元：</strong>国际黄金约4500美元/盎司大幅下跌跌破关键位，国内AU9999约992元/克跌破千元大关。白银同步大幅回调，白银T+D约18435元/千克。WTI原油104.03美元/桶，布伦特110.92美元/桶维持高位。避险资产集体承压，追高风险加大。</div>
    </div>
    <div class="highlight-item-v2">
      <div class="highlight-badge">06</div>
      <div class="highlight-text-v2"><strong>央行5/21开展1000亿逆回购，5月LPR即将出炉：</strong>央行5/21开展1000亿元7天期逆回购操作，利率1.40%。此前5/19开展5亿元7天期逆回购，5/15开展3000亿买断式逆回购（6个月期）。USD/CNY中间价6.8397较前日6.8475升值，在岸约6.8375。5月LPR即将公布，市场关注是否进一步调降。</div>
    </div>
    <div class="highlight-item-v2">
      <div class="highlight-badge">07</div>
      <div class="highlight-text-v2"><strong>中美两国元首同意开展人工智能政府间对话：</strong>中美在AI领域达成政府间对话机制，为全球AI治理与合作开辟新通道。叠加Google I/O 2026开发者大会本周召开，AI前沿动态密集。国内大模型持续迭代：DeepSeek V4（4/24发布）1.6T参数+100万token上下文，GPT-5.5（4/24发布）主打AI智能体原生能力。</div>
    </div>
    <div class="highlight-item-v2">
      <div class="highlight-badge">08</div>
      <div class="highlight-text-v2"><strong>理财参考：</strong>银行1年定存利率约1.65%，银行股息率工行约4.5%、招行约5.3-7%。中国10年期国债1.74%稳定。黄金跌破4500追高风险加大。BTC约77000跌破200日均线。特朗普称可能对伊朗"再予以一击"，地缘风险持续升温。西洽会5/21-24日在重庆举办。</div>
    </div>
  </div>

  <!-- 日历区域 - 垂直时间线 -->
  <div class="timeline-section">
    <div class="timeline-header">
      <span class="timeline-icon">📅</span>
      <span class="timeline-title">近期重要日历</span>
    </div>
    <div class="timeline-container">
      <!-- 今天 -->
      <div class="timeline-item today">
        <div class="timeline-date">
          <div class="timeline-day">21</div>
          <div class="timeline-month">5月</div>
          <div class="timeline-label">今天</div>
        </div>
        <div class="timeline-content">
          <div class="timeline-event">央行1000亿逆回购 · 西洽会开幕</div>
          <div class="timeline-detail">5月LPR即将公布 · Google I/O 2026持续</div>
        </div>
      </div>
      <!-- 重大事件 -->
      <div class="timeline-item future">
        <div class="timeline-date">
          <div class="timeline-day">21-24</div>
          <div class="timeline-month">5月</div>
          <div class="timeline-label">展会</div>
        </div>
        <div class="timeline-content">
          <div class="timeline-event">西洽会在重庆举办</div>
          <div class="timeline-detail">第五届中国西部国际投资贸易洽谈会</div>
        </div>
      </div>
      <!-- LPR -->
      <div class="timeline-item data">
        <div class="timeline-date">
          <div class="timeline-day">20</div>
          <div class="timeline-month">5月</div>
          <div class="timeline-label">数据公布</div>
        </div>
        <div class="timeline-content">
          <div class="timeline-event">5月LPR即将公布</div>
          <div class="timeline-detail">市场关注是否进一步调降 · 央行维持宽松基调</div>
        </div>
      </div>
      <!-- IPO -->
      <div class="timeline-item deadline">
        <div class="timeline-date">
          <div class="timeline-day">待定</div>
          <div class="timeline-month">2026</div>
          <div class="timeline-label">IPO</div>
        </div>
        <div class="timeline-content">
          <div class="timeline-event">长江存储IPO + 长鑫科技科创板上市</div>
          <div class="timeline-detail">中信证券+中信建投联合保荐 · 半导体设备需求催化</div>
        </div>
      </div>
      <!-- 分红险 -->
      <div class="timeline-item deadline">
        <div class="timeline-date">
          <div class="timeline-day">30</div>
          <div class="timeline-month">6月前</div>
          <div class="timeline-label">截止期限</div>
        </div>
        <div class="timeline-content">
          <div class="timeline-event">分红险老产品停售窗口期</div>
          <div class="timeline-detail">演示利率上限3.5%产品退市 · 预定利率降至1.25%</div>
        </div>
      </div>
    </div>
  </div>
  </div>
</div>'''

# 替换Tab 0
pattern_tab0 = re.compile(r'<!-- TAB 0: 要点速览 -->.*?<!-- TAB 1: 国内外新闻 -->', re.DOTALL)
html = pattern_tab0.sub(tab0_content + '\n\n<!-- TAB 1: 国内外新闻 -->', html)

print("Tab 0 replaced.")

# ============================================================
# 3. 替换 Tab 1: 国内外新闻
# ============================================================

tab1_content = '''<!-- TAB 1: 国内外新闻 -->
<div class="tab-panel" id="panel-1">
  <div class="inner">
  <div class="section-title">🌐 国内外新闻</div>
  <div class="sub-section">
    <div class="sub-title">📌 国内外重点新闻</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-geo">外交</span>习近平与普京会谈，中俄睦邻友好合作条约继续延期</div>
      <div class="card-body">习近平与普京举行重要会谈，中俄睦邻友好合作条约继续延期，两国战略协作伙伴关系进一步深化。此次会谈在当前复杂国际局势下具有重大战略意义，双方在能源、基建、科技等领域的合作预期升温。中俄经贸合作的深化将为相关产业链带来长期投资机会，能源合作、基础设施建设等领域有望率先受益。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">科技</span>中美两国元首同意开展人工智能政府间对话</div>
      <div class="card-body">中美两国元首达成重要共识，同意开展人工智能政府间对话，为全球AI治理与合作开辟新通道。这一突破性进展有望缓解此前中美在AI领域的紧张态势，为两国科技企业创造更稳定的合作环境。叠加Google I/O 2026开发者大会本周召开，AI前沿动态密集释放。国内AI产业持续加速：DeepSeek V4（4/24发布）拥有1.6T参数和100万token上下文窗口，GPT-5.5（4/24发布）主打AI智能体原生能力。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-chip">半导体</span>长江存储启动IPO辅导，长鑫科技更新科创板招股书</div>
      <div class="card-body">长江存储正式启动IPO辅导，由中信证券和中信建投联合保荐，标志着国内存储芯片龙头冲刺资本市场进入实质性阶段。长鑫科技同步更新科创板招股书。两大存储芯片龙头集中冲刺IPO，反映出国家对半导体自主可控的战略决心。港股半导体同步大涨：兆易创新涨超17%，华虹半导体涨超13%，中芯国际涨超9%。A股科创50大涨3.2%创历史新高，半导体设备需求迎来强催化。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">A股</span>A股结构性分化：科创50创历史新高，半导体掀涨停潮</div>
      <div class="card-body">5/20收盘：上证指数4162.18(-0.18%)微跌，深证成指15569.98平收，创业板指3921.79(+0.34%)收红。科创50大涨3.2%约1841点创历史新高，半导体/存储芯片/集成电路封测板块掀涨停潮。两市成交2.95万亿较前日放量670亿，但涨跌家数1638:3804跌多涨少，赚钱效应高度集中在科技方向。北向资金成交3532亿占两市11.96%。领跌板块为电力/贵金属/锂矿/电信，市场呈现明显的"科技强、传统弱"格局。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-geo">地缘</span>特朗普称可能对伊朗"再予以一击"，地缘风险升温</div>
      <div class="card-body">特朗普表示可能对伊朗"再予以一击"，中东地缘风险持续升温。WTI原油维持104.03美元/桶高位，布伦特110.92美元/桶。地缘局势的不确定性对全球能源供应链构成长期压力，同时也为上游能源企业带来业绩支撑。市场密切关注后续军事与外交动态，以及对中国能源进口的潜在影响。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">🌍 地缘政治</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-geo">中俄</span>中俄元首会谈深化战略协作，条约延期释放长期利好</div>
      <div class="card-body">习近平与普京会谈，中俄睦邻友好合作条约继续延期。两国在能源、基建、科技、金融等领域的合作将进一步深化。中俄战略协作的深化不仅有利于两国经济发展，也为全球多极化格局注入稳定性。对资本市场而言，中俄合作相关的能源、基建、军工等板块有望获得主题催化。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-geo">美伊</span>特朗普对伊朗强硬表态，中东局势持续紧张</div>
      <div class="card-body">特朗普称可能对伊朗"再予以一击"，中东地缘风险持续升温。WTI原油104.03美元/桶维持高位，布伦特110.92美元/桶。霍尔木兹海峡的地缘溢价仍在油价中充分反映。地缘局势走向存在高度不确定性，市场密切关注后续动态。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">政策</span>工信部组织开展2026年度道路机动车辆生产一致性监督检查</div>
      <div class="card-body">工信部组织开展2026年度道路机动车辆生产一致性监督检查，覆盖新能源汽车和传统燃油车。此举旨在加强汽车行业质量监管，推动产业高质量发展。对新能源汽车板块而言，监管趋严有利于行业出清和龙头集中度提升。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">💰 国内外财经</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">美股</span>美股标普纳指三连跌，科技股承压加息预期升温</div>
      <div class="card-body">美东5/19收盘：道指49363(-0.65%)，标普500 7353(-0.67%)三连跌，纳指25870(-0.84%)三连跌。科技股多数下跌，谷歌亚马逊跌超2%，高通跌近4%。美国长债收益率持续走高，10年期国债4.5577%尾盘跌10.46bp，交易员预计2026年底前加息概率超80%。中概股涨跌不一，拼多多京东涨超2%。美股从高位持续回调，科技股领跌反映市场对加息和估值压力的担忧。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-energy">黄金</span>国际黄金跌破4500美元！国内AU9999跌破千元大关</div>
      <div class="card-body">国际黄金约4500美元/盎司大幅下跌跌破关键位，国内AU9999约992元/克跌破千元大关。白银同步大幅回调，白银T+D约18435元/千克。避险资产集体承压，可能原因包括：美元指数走强、美债收益率飙升（10年期4.5577%）、以及市场资金从避险资产转向半导体等风险资产。追高风险显著加大，建议已有黄金配置的持有观望，未建仓者等待企稳信号。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-energy">原油</span>WTI 104.03美元/桶，布伦特110.92美元/桶维持高位</div>
      <div class="card-body">WTI原油104.03美元/桶，布伦特原油110.92美元/桶维持高位。特朗普对伊朗强硬表态持续支撑地缘溢价。油价高位运行对上游能源企业（中国海油等）形成直接利好，但对航空、化工等下游行业构成成本压力。需关注后续地缘局势变化对油价的边际影响。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">加密货币</span>BTC约77000跌破200日均线，ETH约2118低位震荡</div>
      <div class="card-body">BTC约77000美元，200日均线被拒后跌破77000关口，技术面转弱。ETH约2118美元持续低位震荡。加密货币市场整体承压，美股三连跌+美债收益率飙升+加息预期升温对风险资产形成全面压制。市场等待新的催化剂打破当前格局。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">展会</span>西洽会5/21-24日在重庆举办</div>
      <div class="card-body">第五届中国西部国际投资贸易洽谈会（西洽会）将于5月21日至24日在重庆举办。展会聚焦西部开放、产业合作、数字经济等议题，有望为西部地区的基建、科技、消费等板块带来主题催化。</div>
    </div>
  </div>
  </div>
</div>'''

pattern_tab1 = re.compile(r'<!-- TAB 1: 国内外新闻 -->.*?<!-- TAB 2: AI前沿 -->', re.DOTALL)
html = pattern_tab1.sub(tab1_content + '\n\n<!-- TAB 2: AI前沿 -->', html)

print("Tab 1 replaced.")

# ============================================================
# 4. 替换 Tab 2: AI前沿
# ============================================================

tab2_content = '''<!-- TAB 2: AI前沿 -->
<div class="tab-panel" id="panel-2">
  <div class="inner">
  <div class="section-title">🤖 AI前沿</div>
  <div class="sub-section">
    <div class="sub-title">🔥 大模型动态</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">中美AI</span>中美两国元首同意开展AI政府间对话，全球AI治理新篇章</div>
      <div class="card-body">中美两国元首达成重要共识，同意开展人工智能政府间对话。这一突破性进展有望缓解此前中美在AI领域的紧张态势，为全球AI治理与合作开辟新通道。在AI技术快速迭代的背景下，中美作为全球两大AI强国，政府间对话机制的建立对行业长期发展具有深远意义。对A股AI板块而言，合作预期有望提振市场情绪，但短期需关注具体合作细则的落地。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">DeepSeek</span>DeepSeek V4（4/24发布）：1.6T参数+100万token上下文</div>
      <div class="card-body">DeepSeek V4于4月24日正式发布，拥有1.6万亿参数规模和100万token上下文窗口，在多项基准测试中表现优异。DeepSeek作为中国AI大模型的核心代表之一，V4版本的发布标志着国产大模型在参数规模和上下文理解能力上达到新的里程碑。国产大模型在办公、编程、教育等场景的渗透率持续提升。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">OpenAI</span>GPT-5.5（4/24发布）：主打AI智能体原生能力</div>
      <div class="card-body">OpenAI于4月24日发布GPT-5.5，主打AI智能体（Agent）原生能力，标志着大模型从"对话工具"向"自主执行任务"的范式转变。GPT-5.5在复杂任务规划、多步骤推理、工具调用等方面实现重大突破。AI智能体原生能力的发展将加速AI在企业管理、软件开发、客户服务等场景的商业化落地。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">Claude</span>Claude 4系列已发布，Anthropic持续领跑AI安全赛道</div>
      <div class="card-body">Anthropic发布Claude 4系列模型，在推理能力、代码生成、多模态理解等方面实现全面提升。Claude系列以AI安全和可控性著称，在企业级应用场景中具有独特竞争优势。Anthropic持续领跑AI安全赛道，其"负责任AI"理念获得越来越多企业客户的认可。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">⚡ 半导体与算力</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-chip">存储芯片</span>长江存储IPO+长鑫科技科创板，半导体设备需求强催化</div>
      <div class="card-body">长江存储正式启动IPO辅导（中信证券+中信建投联合保荐），长鑫科技更新科创板招股书。两大存储芯片龙头集中冲刺资本市场，对半导体设备板块形成直接催化。A股5/20半导体/存储芯片/集成电路封测板块掀涨停潮，科创50大涨3.2%创历史新高。港股半导体同步大涨：兆易创新涨超17%，华虹半导体涨超13%，中芯国际涨超9%。存储芯片国产替代进程加速，设备供应商有望率先受益。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-chip">Google I/O</span>Google I/O 2026开发者大会本周召开</div>
      <div class="card-body">Google I/O 2026开发者大会本周召开，预计将发布新一代Gemini模型、Android系统更新、AI硬件产品等重要内容。Google作为全球AI领域的领军企业之一，其技术路线和产品发布对整个AI产业具有风向标意义。关注大会在AI Agent、多模态、端侧AI等方面的最新进展。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">📊 产业趋势</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-tech">趋势</span>AI产业三线并进：大模型迭代+存储芯片国产化+AI治理合作</div>
      <div class="card-body">大模型层面：DeepSeek V4（1.6T参数）、GPT-5.5（智能体原生）、Claude 4系列三强格局成型，中美AI政府间对话开辟合作新通道。半导体层面：长江存储IPO+长鑫科技科创板双重催化，科创50创历史新高，港股半导体大涨（兆易创新+17%、华虹+13%、中芯国际+9%）。应用层面：AI智能体从概念走向落地，企业级AI工具采购需求快速增长。AI产业已进入"技术迭代+国产替代+国际合作"三线并进的新阶段。</div>
    </div>
  </div>
  </div>
</div>'''

pattern_tab2 = re.compile(r'<!-- TAB 2: AI前沿 -->.*?<!-- TAB 3: 全球市场 -->', re.DOTALL)
html = pattern_tab2.sub(tab2_content + '\n\n<!-- TAB 3: 全球市场 -->', html)

print("Tab 2 replaced.")

# ============================================================
# 5. 替换 Tab 3: 全球市场
# ============================================================

tab3_content = '''<!-- TAB 3: 全球市场 -->
<div class="tab-panel" id="panel-3">
  <div class="inner">
  <div class="section-title">📈 全球市场行情</div>
  <div class="hot-bar" style="margin-bottom:20px;">
    <strong>🔥 科创50大涨3.2%创历史新高！半导体掀涨停潮！长江存储IPO催化！</strong>
  </div>
  <div class="alert-bar" style="margin-bottom:20px;">
    <strong>⚠️ 美股标普纳指三连跌！交易员预计年底前加息概率超80%！黄金跌破4500！</strong>
  </div>
  <div class="good-bar" style="margin-bottom:20px;">
    <strong>🤝 中俄元首会谈条约延期！中美AI政府间对话！外交利好频出！</strong>
  </div>
  <div class="market-grid">
    <div class="market-block" style="border-top:2px solid var(--yellow);">
      <h4>🇨🇳 A股（5/20收盘）结构性分化</h4>
      <div class="market-row"><span class="market-name">上证指数</span><span class="market-val down">4162.18 <small>-0.18%</small></span></div>
      <div class="market-row"><span class="market-name">深证成指</span><span class="market-val neutral">15569.98 <small>平收</small></span></div>
      <div class="market-row"><span class="market-name">创业板指</span><span class="market-val up">3921.79 <small>+0.34%</small></span></div>
      <div class="market-row"><span class="market-name">科创50</span><span class="market-val up">约1841 <small>+3.20%（创历史新高！）</small></span></div>
      <div class="market-row"><span class="market-name">沪深300</span><span class="market-val down">微跌0.04%</span></div>
      <div class="market-row"><span class="market-name">两市成交额</span><span class="market-val neutral">2.95万亿（放量670亿）</span></div>
      <div class="market-row"><span class="market-name">北向资金</span><span class="market-val neutral">成交3532亿，占两市11.96%</span></div>
      <div class="market-row"><span class="market-name">涨跌家数</span><span class="market-val down">上涨1638 / 下跌3804（跌多涨少）</span></div>
      <div class="market-row"><span class="market-name">涨停/跌停</span><span class="market-val neutral">涨停69家 / 跌停38家</span></div>
      <div class="market-row"><span class="market-name">领涨板块</span><span class="market-val up">半导体/存储芯片/集成电路封测</span></div>
      <div class="market-row"><span class="market-name">领跌板块</span><span class="market-val down">电力/贵金属/锂矿/电信</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid var(--green);">
      <h4>🇭🇰 港股（5/20收盘）半导体大涨</h4>
      <div class="market-row"><span class="market-name">恒生指数</span><span class="market-val down">跌0.57%</span></div>
      <div class="market-row"><span class="market-name">恒生科技</span><span class="market-val up">涨0.34%</span></div>
      <div class="market-row"><span class="market-name">领涨个股</span><span class="market-val up">兆易创新+17% · 华虹半导体+13% · 中芯国际+9%</span></div>
      <div class="market-row"><span class="market-name">领跌个股</span><span class="market-val down">珠峰黄金跌超9%</span></div>
      <div class="market-row"><span class="market-name">市场特征</span><span class="market-val neutral">半导体强势领涨，黄金板块下挫，内部分化显著</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid var(--yellow);">
      <h4>🌏 亚太市场（5/20）普遍走弱</h4>
      <div class="market-row"><span class="market-name">日经225</span><span class="market-val down">跌1.23%</span></div>
      <div class="market-row"><span class="market-name">韩国KOSPI</span><span class="market-val down">跌0.86%</span></div>
      <div class="market-row"><span class="market-name">印度孟买SENSEX</span><span class="market-val up">微涨0.21%</span></div>
      <div class="market-row"><span class="market-name">澳大利亚</span><span class="market-val down">走弱</span></div>
      <div class="market-row"><span class="market-name">新加坡</span><span class="market-val down">走弱</span></div>
      <div class="market-row"><span class="market-name">台湾加权</span><span class="market-val down">下跌</span></div>
      <div class="market-row"><span class="market-name">市场特征</span><span class="market-val neutral">亚太市场普遍走弱，仅印度微涨，风险偏好降温</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid var(--green);">
      <h4>🇪🇺 欧洲市场（5/19收盘）涨跌互现</h4>
      <div class="market-row"><span class="market-name">德国DAX</span><span class="market-val up">涨1.38%</span></div>
      <div class="market-row"><span class="market-name">英国富时100</span><span class="market-val up">涨0.99%</span></div>
      <div class="market-row"><span class="market-name">法国CAC40</span><span class="market-val neutral">持平</span></div>
      <div class="market-row"><span class="market-name">斯托克600</span><span class="market-val up">涨0.27%</span></div>
      <div class="market-row"><span class="market-name">市场特征</span><span class="market-val neutral">欧洲市场相对稳健，德国领涨，法国持平</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid var(--red);">
      <h4>🇺🇸 美股（5/19收盘）三连跌</h4>
      <div class="market-row"><span class="market-name">道琼斯</span><span class="market-val down">49363 <small>-0.65%</small></span></div>
      <div class="market-row"><span class="market-name">标普500</span><span class="market-val down">7353 <small>-0.67%（三连跌）</small></span></div>
      <div class="market-row"><span class="market-name">纳斯达克</span><span class="market-val down">25870 <small>-0.84%（三连跌）</small></span></div>
      <div class="market-row"><span class="market-name">领跌个股</span><span class="market-val down">谷歌-2%+ · 亚马逊-2%+ · 高通-4%</span></div>
      <div class="market-row"><span class="market-name">中概股</span><span class="market-val up">拼多多+2%+ · 京东+2%+</span></div>
      <div class="market-row"><span class="market-name">加息预期</span><span class="market-val down">交易员预计年底前加息概率超80%</span></div>
      <div class="market-row"><span class="market-name">市场情绪</span><span class="market-val down">科技股承压，长债收益率持续走高</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid var(--red);">
      <h4>🏭 大宗商品（5/20）黄金暴跌</h4>
      <div class="market-row"><span class="market-name">WTI原油</span><span class="market-val up">$104.03/桶</span></div>
      <div class="market-row"><span class="market-name">布伦特原油</span><span class="market-val up">$110.92/桶</span></div>
      <div class="market-row"><span class="market-name">国际黄金</span><span class="market-val down">约$4500/盎司 <small>（跌破关键位！）</small></span></div>
      <div class="market-row"><span class="market-name">国内AU9999</span><span class="market-val down">约992元/克 <small>（跌破千元大关！）</small></span></div>
      <div class="market-row"><span class="market-name">白银T+D</span><span class="market-val down">约18435元/千克 <small>（大幅回调）</small></span></div>
      <div class="market-row"><span class="market-name">核心驱动</span><span class="market-val down">美债收益率飙升+美元走强+避险资产集体承压</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid var(--purple);">
      <h4>🪙 加密货币（5/20）BTC破位</h4>
      <div class="market-row"><span class="market-name">比特币（BTC）</span><span class="market-val down">约$77,000 <small>（跌破200日均线）</small></span></div>
      <div class="market-row"><span class="market-name">以太坊（ETH）</span><span class="market-val down">约$2,118 <small>（低位震荡）</small></span></div>
      <div class="market-row"><span class="market-name">技术面</span><span class="market-val down">BTC 200日均线被拒后跌破77000，技术面转弱</span></div>
      <div class="market-row"><span class="market-name">市场情绪</span><span class="market-val neutral">美股三连跌+加息预期压制风险偏好</span></div>
      <div class="market-row"><span class="market-name">关注</span><span class="market-val neutral">等待新催化剂打破当前格局</span></div>
    </div>
    <div class="market-block" style="border-top:2px solid var(--accent);">
      <h4>💱 汇率与债券</h4>
      <div class="market-row"><span class="market-name">USD/CNY中间价</span><span class="market-val neutral">6.8397 <small>（较前日6.8475升值）</small></span></div>
      <div class="market-row"><span class="market-name">在岸人民币</span><span class="market-val neutral">约6.8375</span></div>
      <div class="market-row"><span class="market-name">美元指数</span><span class="market-val down">跌0.24%</span></div>
      <div class="market-row"><span class="market-name">中国10年期国债</span><span class="market-val neutral">1.74% <small>（稳定）</small></span></div>
      <div class="market-row"><span class="market-name">美国10年期国债</span><span class="market-val up">4.5577% <small>（尾盘跌10.46bp）</small></span></div>
      <div class="market-row"><span class="market-name">中美利差</span><span class="market-val down">约-282BP <small>（倒挂幅度大）</small></span></div>
      <div class="market-row"><span class="market-name">央行操作</span><span class="market-val neutral">5/21 1000亿逆回购 · 利率1.40%</span></div>
    </div>
  </div>
  <div class="card" style="border-left:3px solid var(--orange);">
    <div class="card-title">📊 市场综评（5月20日·周三）</div>
    <div class="card-body">
      <p style="margin-bottom:10px;padding:10px 12px;background:rgba(248,81,73,0.08);border-radius:8px;border-left:3px solid var(--red);"><strong style="color:var(--red);">🚀 科创50创历史新高</strong><br>科创50 <span class="up" style="font-weight:700;">约1841（+3.20%）</span> 创历史新高 · 半导体/存储芯片/集成电路封测涨停潮 · 长江存储IPO催化 · 港股半导体同步大涨</p>
      <p style="margin-bottom:10px;padding:10px 12px;background:rgba(0,212,255,0.08);border-radius:8px;border-left:3px solid var(--accent);"><strong style="color:var(--accent);">📉 美股三连跌</strong><br>标普 <span class="down" style="font-weight:700;">7353（-0.67%）</span> · 纳指 <span class="down" style="font-weight:700;">25870（-0.84%）</span> · 交易员预计年底前加息概率超80% · 10年期美债4.5577%</p>
      <p style="margin-bottom:10px;padding:10px 12px;background:rgba(255,166,87,0.08);border-radius:8px;border-left:3px solid var(--orange);"><strong style="color:var(--orange);">🥇 黄金暴跌</strong><br>国际黄金 <span class="down" style="font-weight:700;">约$4500（跌破关键位）</span> · 国内AU9999 <span class="down" style="font-weight:700;">约992元/克（跌破千元）</span> · 白银T+D约18435大幅回调</p>
      <p style="margin-bottom:0;padding:10px 12px;background:rgba(63,185,80,0.08);border-radius:8px;border-left:3px solid var(--green);"><strong style="color:var(--green);">🤝 外交利好</strong><br>中俄元首会谈条约延期 · 中美AI政府间对话 · 长江存储IPO+长鑫科技科创板</p>
    </div>
  </div>
  </div>
</div>'''

pattern_tab3 = re.compile(r'<!-- TAB 3: 全球市场 -->.*?<!-- TAB 4: 价值投资风向 -->', re.DOTALL)
html = pattern_tab3.sub(tab3_content + '\n\n<!-- TAB 4: 价值投资风向 -->', html)

print("Tab 3 replaced.")

# ============================================================
# 6. 替换 Tab 4: 价值投资风向
# ============================================================

tab4_content = '''<!-- TAB 4: 价值投资风向 -->
<div class="tab-panel" id="panel-4">
  <div class="inner">
  <div class="section-title">💡 价值投资风向</div>

  <!-- 一 · 机构价值投资观点 -->
  <div class="sub-section">
    <div class="sub-title">一 · 机构价值投资观点</div>
    <div class="institute-tabs">
      <div class="institute-card institute-cicc">
        <div class="institute-header">
          <div class="institute-logo">
            <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" fill="rgba(0,212,255,0.15)" stroke="rgba(0,212,255,0.5)" stroke-width="1.5"/><text x="20" y="25" text-anchor="middle" fill="#00d4ff" font-size="14" font-weight="700">中金</text></svg>
          </div>
          <div class="institute-info">
            <div class="institute-name">中金/中信证券</div>
            <div class="institute-tag">科技进攻+高股息防御</div>
          </div>
        </div>
        <div class="institute-body">
          科创50大涨3.2%创历史新高，半导体/存储芯片掀涨停潮，长江存储IPO+长鑫科技科创板双重催化。但上证4162微跌、涨跌家数1638:3804，市场结构性分化明显。策略上建议：进攻方向聚焦半导体设备/存储芯片/AI算力（长江存储IPO催化+中美AI对话），防御方向维持银行/公用事业高股息底仓。央行5/21开展1000亿逆回购、5月LPR即将公布，流动性环境保持宽松。美股三连跌+加息预期升温提醒外部风险未消，哑铃策略攻守兼备。
        </div>
      </div>
      <div class="institute-card institute-gs">
        <div class="institute-header">
          <div class="institute-logo">
            <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" fill="rgba(188,140,255,0.15)" stroke="rgba(188,140,255,0.5)" stroke-width="1.5"/><text x="20" y="25" text-anchor="middle" fill="#bc8cff" font-size="12" font-weight="700">GS</text></svg>
          </div>
          <div class="institute-info">
            <div class="institute-name">高盛/摩根</div>
            <div class="institute-tag">半导体国产替代加速</div>
          </div>
        </div>
        <div class="institute-body">
          长江存储IPO辅导（中信证券+中信建投）+长鑫科技更新科创板招股书，两大存储芯片龙头集中冲刺资本市场，这是中国半导体国产替代进程中的标志性事件。港股半导体同步大涨（兆易创新+17%、华虹+13%、中芯国际+9%），A股科创50创历史新高，中美AI政府间对话进一步提振科技合作预期。USD/CNY中间价6.8397较前日升值，人民币汇率稳定为外资流入创造条件。但美股三连跌+交易员预计年底前加息概率超80%，外部环境不确定性仍需警惕。
        </div>
      </div>
      <div class="institute-card institute-xy">
        <div class="institute-header">
          <div class="institute-logo">
            <svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="18" fill="rgba(63,185,80,0.15)" stroke="rgba(63,185,80,0.5)" stroke-width="1.5"/><text x="20" y="25" text-anchor="middle" fill="#3fb950" font-size="14" font-weight="700">兴业</text></svg>
          </div>
          <div class="institute-info">
            <div class="institute-name">兴业/华泰</div>
            <div class="institute-tag">避险资产重估+高股息底仓</div>
          </div>
        </div>
        <div class="institute-body">
          国际黄金跌破4500美元关键位，国内AU9999跌破千元大关至约992元/克，白银T+D约18435大幅回调。避险资产集体承压，"地缘冲突=买黄金"的传统逻辑短期失效。在这一背景下，高股息资产的相对吸引力进一步提升：银行股息率4.5-7%远超1年定存1.65%，长江电力/大秦铁路等公用事业提供确定性现金流。建议关注黄金暴跌后的超跌反弹机会（但不宜急于抄底），同时维持高股息底仓对冲市场波动。
        </div>
      </div>
    </div>
  </div>

  <!-- 二 · 社区情绪 -->
  <div class="sub-section">
    <div class="sub-title">二 · 雪球·集思录价值投资社区情绪</div>
    <div class="sentiment-dashboard">
      <div class="sentiment-main">
        <div class="sentiment-grid">
          <div class="sentiment-item">
            <div class="sentiment-emoji">📊</div>
            <div class="sentiment-info">
              <div class="sentiment-name">高股息整体仓位</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:70%;background:linear-gradient(90deg,#f0b429,var(--accent))"></div>
                </div>
                <span class="sentiment-percent">70%</span>
              </div>
              <div class="sentiment-desc">偏高 · 科创50新高但大盘微跌，底仓逻辑不变</div>
            </div>
          </div>
          <div class="sentiment-item">
            <div class="sentiment-emoji">🏦</div>
            <div class="sentiment-info">
              <div class="sentiment-name">银行板块讨论热度</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:62%"></div>
                </div>
                <span class="sentiment-percent">62%</span>
              </div>
              <div class="sentiment-desc">中性 · 资金追逐半导体，银行偏弱但股息优势突出</div>
            </div>
          </div>
          <div class="sentiment-item">
            <div class="sentiment-emoji">🛡️</div>
            <div class="sentiment-info">
              <div class="sentiment-name">公用事业防御需求</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:68%;background:linear-gradient(90deg,var(--green),var(--accent))"></div>
                </div>
                <span class="sentiment-percent">68%</span>
              </div>
              <div class="sentiment-desc">偏强 · 黄金暴跌+美股三连跌，确定性资产受青睐</div>
            </div>
          </div>
          <div class="sentiment-item">
            <div class="sentiment-emoji">⚡</div>
            <div class="sentiment-info">
              <div class="sentiment-name">电力板块情绪</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:45%;background:linear-gradient(90deg,#f0b429,var(--accent))"></div>
                </div>
                <span class="sentiment-percent low">45%</span>
              </div>
              <div class="sentiment-desc">偏弱 · 5/20电力板块领跌，长江电力跟跌</div>
            </div>
          </div>
          <div class="sentiment-item">
            <div class="sentiment-emoji">🤖</div>
            <div class="sentiment-info">
              <div class="sentiment-name">AI算力板块情绪</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:82%;background:linear-gradient(90deg,var(--purple),var(--accent))"></div>
                </div>
                <span class="sentiment-percent hot">82%</span>
              </div>
              <div class="sentiment-desc">高涨 · 科创50历史新高+半导体涨停潮+长江存储IPO</div>
            </div>
          </div>
          <div class="sentiment-item">
            <div class="sentiment-emoji">🛢️</div>
            <div class="sentiment-info">
              <div class="sentiment-name">能源/油价情绪</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:72%;background:linear-gradient(90deg,#f0b429,var(--accent))"></div>
                </div>
                <span class="sentiment-percent">72%</span>
              </div>
              <div class="sentiment-desc">偏多 · WTI $104+布伦特$111维持高位，中国海油+1.79%</div>
            </div>
          </div>
          <div class="sentiment-item">
            <div class="sentiment-emoji">🥇</div>
            <div class="sentiment-info">
              <div class="sentiment-name">黄金板块情绪</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:35%;background:linear-gradient(90deg,#f0b429,var(--accent))"></div>
                </div>
                <span class="sentiment-percent low">35%</span>
              </div>
              <div class="sentiment-desc">悲观 · 黄金跌破$4500，国内金价跌破千元，追高风险大</div>
            </div>
          </div>
          <div class="sentiment-item">
            <div class="sentiment-emoji">₿</div>
            <div class="sentiment-info">
              <div class="sentiment-name">加密货币情绪</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:42%;background:linear-gradient(90deg,#f0b429,var(--accent))"></div>
                </div>
                <span class="sentiment-percent low">42%</span>
              </div>
              <div class="sentiment-desc">偏弱 · BTC跌破77000和200日均线，ETH低位震荡</div>
            </div>
          </div>
          <div class="sentiment-item">
            <div class="sentiment-emoji">🔋</div>
            <div class="sentiment-info">
              <div class="sentiment-name">新能源板块情绪</div>
              <div class="sentiment-progress-wrap">
                <div class="sentiment-progress-bar">
                  <div class="sentiment-progress-fill" style="width:50%;background:linear-gradient(90deg,var(--green),var(--accent))"></div>
                </div>
                <span class="sentiment-percent">50%</span>
              </div>
              <div class="sentiment-desc">中性 · 锂矿领跌拖累，但半导体催化带动部分新能源标的</div>
            </div>
          </div>
        </div>
      </div>
      <div class="topic-cloud">
        <div class="topic-cloud-title">🔥 近24小时社区重点讨论</div>
        <div class="topic-tags">
          <span class="topic-tag hot">科创50历史新高</span>
          <span class="topic-tag hot">半导体涨停潮</span>
          <span class="topic-tag">长江存储IPO</span>
          <span class="topic-tag">中美AI对话</span>
          <span class="topic-tag warn">黄金跌破4500</span>
          <span class="topic-tag warn">美股三连跌</span>
          <span class="topic-tag">加息预期升温</span>
          <span class="topic-tag">央行逆回购</span>
          <span class="topic-tag">5月LPR</span>
          <span class="topic-tag">中俄会谈</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 三 · 高股息板块深度分析 -->
  <div class="sub-section">
    <div class="sub-title">三 · 高股息板块深度分析</div>
    <div class="dividend-grid">
      <div class="dividend-card">
        <div class="dividend-header bank-theme">
          <div class="dividend-icon">🏦</div>
          <div class="dividend-title">银行板块</div>
        </div>
        <div class="dividend-metrics">
          <div class="metric">
            <div class="metric-value">4.5-7%</div>
            <div class="metric-label">股息率</div>
          </div>
          <div class="metric">
            <div class="metric-value">0.66x</div>
            <div class="metric-label">PB估值</div>
          </div>
        </div>
        <div class="dividend-body">
          5/20A股结构性分化，资金追逐半导体等科技品种，银行板块相对偏弱。但银行板块PB约0.66x仍处历史低位，国有大行股息率高达4.5-7%，是一年定存（1.65%）的3-4倍。央行5/21开展1000亿逆回购、5月LPR即将公布，宽松政策环境对银行净息差压力可控。在美股三连跌+黄金暴跌的复杂环境下，银行板块"低波动+高分红+大市值"的压舱石价值不减反增。
        </div>
      </div>
      <div class="dividend-card">
        <div class="dividend-header energy-theme">
          <div class="dividend-icon">🛢️</div>
          <div class="dividend-title">能源板块</div>
        </div>
        <div class="dividend-metrics">
          <div class="metric">
            <div class="metric-value warn">$104.03</div>
            <div class="metric-label">WTI原油</div>
          </div>
          <div class="metric">
            <div class="metric-value warn">$110.92</div>
            <div class="metric-label">布伦特</div>
          </div>
        </div>
        <div class="dividend-body">
          WTI原油104.03美元/桶，布伦特110.92美元/桶维持高位。特朗普对伊朗强硬表态持续支撑地缘溢价。中国海油5/20收37.58元(+1.79%)，油价高位直接增厚业绩。但需注意特朗普对伊朗"再予以一击"的表态可能带来短期波动。建议已有底仓持有观望，密切关注地缘局势进展。
        </div>
      </div>
      <div class="dividend-card">
        <div class="dividend-header utility-theme">
          <div class="dividend-icon">⚡</div>
          <div class="dividend-title">公用事业</div>
        </div>
        <div class="dividend-metrics">
          <div class="metric">
            <div class="metric-value good">~4.2%</div>
            <div class="metric-label">长江电力股息率</div>
          </div>
          <div class="metric">
            <div class="metric-value">~5%</div>
            <div class="metric-label">大秦铁路股息率</div>
          </div>
        </div>
        <div class="dividend-body">
          5/20电力板块领跌，长江电力跟跌。但黄金跌破4500、美股三连跌的背景下，公用事业作为"不受地缘冲突影响、不受科技周期波动干扰"的纯内需防御板块，其确定性收益特征在复杂环境下尤为珍贵。长江电力承诺分红比例不低于70%，大秦铁路作为全国煤炭运输大动脉提供稳定现金流。短期回调或提供更好的建仓机会。
        </div>
      </div>
      <div class="dividend-card">
        <div class="dividend-header telecom-theme">
          <div class="dividend-icon">📡</div>
          <div class="dividend-title">通信/中国移动</div>
        </div>
        <div class="dividend-metrics">
          <div class="metric">
            <div class="metric-value">~5%</div>
            <div class="metric-label">A股股息率</div>
          </div>
          <div class="metric">
            <div class="metric-value hot">+50%</div>
            <div class="metric-label">算力收入增速</div>
          </div>
        </div>
        <div class="dividend-body">
          中国移动A股股息率约5%，H股约6.8%。算力及云/AI相关业务收入增速超过50%。5/20电信板块领跌，中国移动跟跌，但"高股息防御+算力成长"双属性在当前环境下尤为稀缺。中美AI政府间对话若推动科技合作，移动作为国内算力基础设施核心参与者将直接受益。
        </div>
      </div>
    </div>
  </div>

  <!-- 四 · 低估值板块 -->
  <div class="sub-section">
    <div class="sub-title">四 · 低估值板块</div>
    <div class="undervalued-grid">
      <div class="undervalued-card">
        <div class="undervalued-badge">低估值</div>
        <div class="undervalued-header">
          <div class="undervalued-icon">⚛️</div>
          <div class="undervalued-title-area">
            <div class="undervalued-name">中国核电</div>
            <div class="undervalued-tags">
              <span class="uv-tag">核电装机全球第一</span>
              <span class="uv-tag">清洁能源</span>
            </div>
          </div>
        </div>
        <div class="undervalued-metrics">
          <div class="uv-metric">
            <div class="uv-metric-value">18x</div>
            <div class="uv-metric-label">PE</div>
            <div class="uv-metric-percentile">45%分位</div>
          </div>
          <div class="uv-metric">
            <div class="uv-metric-value">1.25亿</div>
            <div class="uv-metric-label">装机(千瓦)</div>
            <div class="uv-metric-percentile good">全球首位</div>
          </div>
        </div>
        <div class="undervalued-desc">
          中国核电装机规模位居全球首位（达1.25亿千瓦），18倍PE对应历史45%分位。在特朗普对伊朗强硬表态推升全球能源安全担忧、油价维持$104高位的背景下，核电作为清洁、稳定、不受地缘冲突影响的能源形式，战略价值进一步凸显。AI数据中心耗电量持续攀升为核电板块提供中长期需求支撑。
        </div>
      </div>
      <div class="undervalued-card">
        <div class="undervalued-badge">低估值</div>
        <div class="undervalued-header">
          <div class="undervalued-icon">🛡️</div>
          <div class="undervalued-title-area">
            <div class="undervalued-name">中国平安</div>
            <div class="undervalued-tags">
              <span class="uv-tag">保险龙头</span>
              <span class="uv-tag">分红险切换红利</span>
            </div>
          </div>
        </div>
        <div class="undervalued-metrics">
          <div class="uv-metric">
            <div class="uv-metric-value">7.4x</div>
            <div class="uv-metric-label">PE</div>
            <div class="uv-metric-percentile good">历史低位</div>
          </div>
          <div class="uv-metric">
            <div class="uv-metric-value">0.98x</div>
            <div class="uv-metric-label">PB</div>
            <div class="uv-metric-percentile good">接近1倍</div>
          </div>
          <div class="uv-metric">
            <div class="uv-metric-value">~4.7%</div>
            <div class="uv-metric-label">股息率</div>
            <div class="uv-metric-percentile">双属性</div>
          </div>
        </div>
        <div class="undervalued-desc">
          中国平安当前PE约7.4倍，PB约0.98倍接近1倍，股息率约4.7%，估值处于历史低位。5/20收约54.11元。分红险演示利率上限3.5%，预定利率从1.75%降至1.25%，老产品须在6/30前退市——平安作为行业龙头将直接承接切换红利。在黄金暴跌+美股三连跌的背景下，兼具保险与高股息双重属性的配置价值凸显。
        </div>
      </div>
    </div>
  </div>

  <!-- 五 · 长线资金动向 -->
  <div class="sub-section">
    <div class="sub-title">五 · 长线资金动向</div>
    <div class="capital-flow-section">
      <div class="flow-visualization">
        <div class="flow-title">💰 长线资金入市路径</div>
        <div class="flow-diagram">
          <div class="flow-node">
            <div class="flow-node-icon">🏦</div>
            <div class="flow-node-label">银行存款</div>
            <div class="flow-node-value">110万亿</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-node highlight">
            <div class="flow-node-icon">📈</div>
            <div class="flow-node-label">到期转投</div>
            <div class="flow-node-value">~7万亿</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-node target">
            <div class="flow-node-icon">🎯</div>
            <div class="flow-node-label">A股市场</div>
            <div class="flow-node-value">高股息标的</div>
          </div>
        </div>
      </div>
      <div class="capital-cards">
        <div class="capital-card">
          <div class="capital-icon">🏛️</div>
          <div class="capital-content">
            <div class="capital-title">险资+社保</div>
            <div class="capital-stats">
              <span class="capital-stat">北向成交<span class="highlight-num">3532亿</span></span>
              <span class="capital-stat">占两市<span class="highlight-num">11.96%</span></span>
              <span class="capital-stat">预计入市<span class="highlight-num">1.2万亿</span></span>
            </div>
            <div class="capital-desc">北向资金成交3532亿占两市11.96%，外资参与度维持高位。摩根大通判断110万亿银行存款到期约7万亿或流入股市。2026年社保基金与保险资金合计新增入市规模预计可达1.2万亿元左右。央行5/21开展1000亿逆回购，流动性环境保持宽松，为长线资金提供充裕的市场环境。</div>
          </div>
        </div>
        <div class="capital-card">
          <div class="capital-icon">🌍</div>
          <div class="capital-content">
            <div class="capital-title">QFII外资</div>
            <div class="capital-stats">
              <span class="capital-stat">USD/CNY <span class="highlight-num">6.8397</span></span>
              <span class="capital-stat">人民币<span class="highlight-num">升值</span></span>
              <span class="capital-stat">窗口<span class="highlight-num">打开</span></span>
            </div>
            <div class="capital-desc">USD/CNY中间价6.8397较前日6.8475升值，在岸约6.8375，人民币汇率稳定为外资流入创造良好条件。中美AI政府间对话提振合作预期，QFII增配A股动力持续增强。两市成交2.95万亿，市场活跃度为外资提供了充裕的流动性环境。</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 六 · 估值参考表 -->
  <div class="sub-section">
    <div class="sub-title">六 · 价值投资估值参考表</div>
    <div class="valuation-cards">
      <div class="valuation-item">
        <div class="valuation-icon">🏦</div>
        <div class="valuation-info">
          <div class="valuation-name">银行板块PB</div>
          <div class="valuation-value">0.66x</div>
        </div>
        <div class="valuation-tag low">低位</div>
      </div>
      <div class="valuation-item">
        <div class="valuation-icon">📊</div>
        <div class="valuation-info">
          <div class="valuation-name">上证PE</div>
          <div class="valuation-value">14.5x</div>
        </div>
        <div class="valuation-tag mid">40%</div>
      </div>
      <div class="valuation-item">
        <div class="valuation-icon">💰</div>
        <div class="valuation-info">
          <div class="valuation-name">银行股息率</div>
          <div class="valuation-value">4.5-7%</div>
        </div>
        <div class="valuation-tag high">高位</div>
      </div>
      <div class="valuation-item">
        <div class="valuation-icon">📈</div>
        <div class="valuation-info">
          <div class="valuation-name">中证红利PE</div>
          <div class="valuation-value">7.2x</div>
        </div>
        <div class="valuation-tag low">24%</div>
      </div>
      <div class="valuation-item">
        <div class="valuation-icon">📡</div>
        <div class="valuation-info">
          <div class="valuation-name">中国移动PB</div>
          <div class="valuation-value">1.49x</div>
        </div>
        <div class="valuation-tag mid">偏高</div>
      </div>
      <div class="valuation-item">
        <div class="valuation-icon">🏛️</div>
        <div class="valuation-info">
          <div class="valuation-name">招商银行PB</div>
          <div class="valuation-value">0.83x</div>
        </div>
        <div class="valuation-tag low">低位</div>
      </div>
      <div class="valuation-item">
        <div class="valuation-icon">⚛️</div>
        <div class="valuation-info">
          <div class="valuation-name">中国核电PE</div>
          <div class="valuation-value">18x</div>
        </div>
        <div class="valuation-tag mid">45%</div>
      </div>
      <div class="valuation-item">
        <div class="valuation-icon">🛡️</div>
        <div class="valuation-info">
          <div class="valuation-name">中国平安PE</div>
          <div class="valuation-value">7.4x</div>
        </div>
        <div class="valuation-tag low">低位</div>
      </div>
      <div class="valuation-item">
        <div class="valuation-icon">🥇</div>
        <div class="valuation-info">
          <div class="valuation-name">黄金价格</div>
          <div class="valuation-value warn">~$4500</div>
        </div>
        <div class="valuation-tag warn">跌破关键位</div>
      </div>
    </div>
  </div>

  <!-- 附 · 精简参考板块 -->
  <div class="sub-section">
    <div class="sub-title">附 · 精简参考板块</div>
    <div class="reference-grid">
      <div class="reference-card">
        <div class="reference-risk low">低风险</div>
        <div class="reference-icon">🏢</div>
        <div class="reference-title">REITs·固收+</div>
        <div class="reference-desc">央行宽松+人民币稳定，固收资产配置价值不减</div>
        <div class="reference-detail">央行5/21开展1000亿逆回购，5月LPR即将公布，流动性环境保持合理充裕。10年期国债收益率1.74%维持稳定，债牛格局延续。人民币中间价6.8397升值，汇率稳定为固收资产提供良好环境。在A股结构性分化的背景下，固收类资产对保守型资金的吸引力依然稳固。</div>
      </div>
      <div class="reference-card">
        <div class="reference-risk high">高风险</div>
        <div class="reference-icon">💻</div>
        <div class="reference-title">半导体/存储芯片</div>
        <div class="reference-desc">科创50创历史新高+半导体涨停潮，但追高风险需警惕</div>
        <div class="reference-detail">5/20半导体/存储芯片/集成电路封测掀涨停潮，科创50大涨3.2%创历史新高。长江存储IPO+长鑫科技科创板双重催化，港股半导体同步大涨（兆易创新+17%、华虹+13%、中芯国际+9%）。中美AI政府间对话构成长期利好，但短期涨幅过大，半导体板块已积累大量获利盘。建议已有仓位持有观望，未建仓者等待回调后分批介入。</div>
      </div>
      <div class="reference-card">
        <div class="reference-risk mid">中风险</div>
        <div class="reference-icon">🛢️</div>
        <div class="reference-title">能源/原油链</div>
        <div class="reference-desc">WTI $104+布伦特$111高位，地缘溢价持续</div>
        <div class="reference-detail">WTI原油104.03美元/桶，布伦特110.92美元/桶维持高位。特朗普对伊朗强硬表态持续支撑地缘溢价。中国海油5/20收37.58元(+1.79%)直接受益。但需注意地缘局势变化可能带来的短期波动，以及特朗普表态对油价的边际影响。建议已有底仓持有观望。</div>
      </div>
    </div>
  </div>
  </div>
</div>'''

pattern_tab4 = re.compile(r'<!-- TAB 4: 价值投资风向 -->.*?<!-- TAB 5: 关注标的 -->', re.DOTALL)
html = pattern_tab4.sub(tab4_content + '\n\n<!-- TAB 5: 关注标的 -->', html)

print("Tab 4 replaced.")

# Save intermediate result
with open('/sessions/6a0e68353d587e423c5d8d0d/workspace/老盛早知道_20260521.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Tabs 0-4 saved. Continuing with Tabs 5-7...")
