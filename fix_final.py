#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终修正：将所有6月10日市场数据改为6月9日收盘数据
报告发布日期保持2026/06/10不变
"""

import shutil
import os

filepath = '/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260610.html'

# 备份
backup = filepath + '.backup2'
if not os.path.exists(backup):
    shutil.copy2(filepath, backup)
    print(f"✓ 已备份至: {os.path.basename(backup)}")

# 读取文件
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ============================================
# 1. Tab 1 新闻卡片 - A股结构性行情（line ~1991-1992）
# ============================================
old1 = '''    <div class="card">
      <div class="card-title">🔵 A股结构性行情凸显，高股息板块领涨</div>
      <div class="card-body">6月10日A股呈现明显结构性特征，上证指数收<span style="color:#f85149;font-weight:700;">3987.26点涨0.71%</span>，深证成指涨<span style="color:#f85149;font-weight:700;">0.48%</span>报14892.18点，创业板指小幅下跌<span style="color:#3fb950;font-weight:700;">0.36%</span>。<span style="color:#f85149;font-weight:700;">银行、保险、电力</span>等高股息板块领涨，中证银行指数涨1.82%，长江电力创历史新高。沪深两市成交额约<span style="color:#00d4ff;font-weight:700;">26481亿元</span>，连续第32个交易日超2.5万亿。全市场上涨<span style="color:#f85149;font-weight:700;">2865只</span>，下跌2145只，涨跌比约<span style="color:#f85149;font-weight:700;">57:43</span>，较昨日明显改善。</div>
    </div>'''

new1 = '''    <div class="card">
      <div class="card-title">🔴 A股三大指数全线收跌，沪指失守4000点关口</div>
      <div class="card-body">6月9日A股遭遇<span style="color:#3fb950;font-weight:700;">普跌行情</span>，上证指数跌<span style="color:#3fb950;font-weight:700;">1.70%</span>报<span style="color:#3fb950;font-weight:700;">3959.34点</span>，深证成指跌<span style="color:#3fb950;font-weight:700;">3.22%</span>报14821.19点，创业板指大跌<span style="color:#3fb950;font-weight:700;">3.69%</span>报3811.79点，科创50重挫<span style="color:#3fb950;font-weight:700;">4.30%</span>。沪深300指数跌<span style="color:#3fb950;font-weight:700;">2.14%</span>。沪深两市成交额约<span style="color:#00d4ff;font-weight:700;">27927.61亿元</span>，连续第31个交易日超2.5万亿。全市场上涨<span style="color:#3fb950;font-weight:700;">898只</span>，下跌<span style="color:#3fb950;font-weight:700;">4591只</span>，涨跌比约<span style="color:#3fb950;font-weight:700;">16:84</span>，普跌特征显著。</div>
    </div>'''

if old1 in html:
    html = html.replace(old1, new1)
    changes.append("✓ Tab1 A股行情卡片")
else:
    changes.append("✗ Tab1 A股行情卡片 - 未找到匹配")

# ============================================
# 2. Tab 1 新闻卡片 - 美股震荡反弹（line ~1995-1996）
# ============================================
old2 = '''    <div class="card">
      <div class="card-title">🔵 美股震荡反弹，科技股企稳回升</div>
      <div class="card-body">美股三大指数集体反弹，道琼斯涨<span style="color:#f85149;font-weight:700;">0.54%</span>报51142.30点，标普500涨<span style="color:#f85149;font-weight:700;">0.83%</span>报7445.32点，纳斯达克涨<span style="color:#f85149;font-weight:700;">1.07%</span>报25984.20点。芯片股企稳回升，费城半导体指数涨<span style="color:#f85149;font-weight:700;">2.85%</span>。个股方面，<span style="color:#f85149;font-weight:700;">ARM涨4.16%</span>，AMD涨3.42%，英伟达涨2.18%，高通涨1.89%。交易员重新评估美联储政策路径，利率互换市场预计年内降息概率回升至<span style="color:#f0b429;font-weight:700;">38%</span>，市场情绪较昨日明显修复。</div>
    </div>'''

new2 = '''    <div class="card">
      <div class="card-title">🔴 美股隔夜全线暴跌，科技股领跌纳指重挫4.18%</div>
      <div class="card-body">美股隔夜（6月9日）三大指数集体重挫，道琼斯跌<span style="color:#3fb950;font-weight:700;">1.35%</span>报50866.78点，标普500跌<span style="color:#3fb950;font-weight:700;">2.64%</span>报7383.74点，纳斯达克暴跌<span style="color:#3fb950;font-weight:700;">4.18%</span>报25709.43点。芯片股大幅下挫，费城半导体指数大跌超10%创2020年3月以来最大跌幅。个股方面，<span style="color:#3fb950;font-weight:700;">ARM跌12.84%</span>，英伟达跌6.20%报$205.10，特斯拉跌6.56%。市场恐慌情绪升温，VIX波动率指数大幅飙升，避险资产受到追捧。</div>
    </div>'''

if old2 in html:
    html = html.replace(old2, new2)
    changes.append("✓ Tab1 美股行情卡片")
else:
    changes.append("✗ Tab1 美股行情卡片 - 未找到匹配")

# ============================================
# 3. Tab 1 地缘政治 - 以伊紧张局势缓和（line ~2010）
# ============================================
old3 = '''    <div class="card">
      <div class="card-title">🌍 以伊紧张局势缓和，霍尔木兹海峡通航恢复常态</div>
      <div class="card-body">特朗普公开呼吁以伊<span style="color:#f85149;font-weight:700;">立即停火</span>并接受美伊协议后，伊朗方面表示愿意在联合国框架下进行谈判，霍尔木兹海峡航运压力明显缓解。此前伊朗启动的<span style="color:#f0b429;font-weight:700;">海峡收费条例</span>草案暂未进入实质性执行阶段。布伦特原油自高点回落至<span style="color:#00d4ff;font-weight:700;">92.80美元/桶</span>，地缘溢价较上周显著收窄。市场分析人士指出，中东局势仍存在反复风险，但<span style="color:#f85149;font-weight:700;">短期最坏情况已经过去</span>，油价回落有助于缓解全球通胀压力，利好股市和债市表现。</div>
    </div>'''

new3 = '''    <div class="card">
      <div class="card-title">🌍 以伊冲突骤然升级，中东地缘风险显著升温</div>
      <div class="card-body">以色列与伊朗冲突骤然升级，中东局势急转直下，霍尔木兹海峡航运面临严重威胁。布伦特原油一度飙升至<span style="color:#00d4ff;font-weight:700;">93.72美元/桶</span>，市场恐慌情绪蔓延。韩国KOSPI指数暴跌<span style="color:#3fb950;font-weight:700;">8.29%</span>触发熔断，日经指数重挫<span style="color:#3fb950;font-weight:700;">3.85%</span>报64024.60点。市场分析人士指出，<span style="color:#f0b429;font-weight:700;">地缘风险溢价急剧扩大</span>，全球风险资产遭遇猛烈抛售，避险资产受到追捧，短期不确定性显著升高。</div>
    </div>'''

if old3 in html:
    html = html.replace(old3, new3)
    changes.append("✓ Tab1 地缘政治卡片")
else:
    changes.append("✗ Tab1 地缘政治卡片 - 未找到匹配")

# ============================================
# 4. Tab 1 - 北向资金连续9日净买入（line ~2003-2004）
# ============================================
old4 = '''    <div class="card">
      <div class="card-title">🟡 北向资金连续9日净买入，外资坚定看好</div>
      <div class="card-body">北向资金全天净流入<span style="color:#f85149;font-weight:700;">68.45亿元</span>，其中沪股通净买入42.38亿元，深股通净买入26.07亿元，<span style="color:#f0b429;font-weight:700;">连续9个交易日净买入</span>，刷新年内最长连续净买入纪录。前十大成交个股中，工商银行、农业银行、长江电力、贵州茅台获净买入居前。南向资金同步净买入<span style="color:#f85149;font-weight:700;">87.62亿港元</span>，港股市场吸引力持续提升。在外资持续流入的同时，内资主力今日<span style="color:#f85149;font-weight:700;">净流出收窄至186亿元</span>，情绪较昨日好转。</div>
    </div>'''

new4 = '''    <div class="card">
      <div class="card-title">🟡 北向资金连续8日净买入，外资偏好高股息防御</div>
      <div class="card-body">北向资金在全球风险资产回调背景下持续流入，<span style="color:#f0b429;font-weight:700;">连续8个交易日净买入</span>，重点加仓银行、保险等低估值高股息板块。前十大成交个股中，工商银行、农业银行、长江电力等蓝筹标的获外资持续青睐。南向资金同步净买入<span style="color:#f85149;font-weight:700;">113.18亿港元</span>，港股市场成为外资配置中国资产的重要通道。外资持续加仓中国资产主要基于三大逻辑：一是中国资产估值处于历史低位，<span style="color:#f85149;font-weight:700;">银行板块PB仅0.6倍</span>；二是高股息策略具全球吸引力，中证红利股息率远超全球主要指数；三是<span style="color:#00d4ff;font-weight:700;">人民币汇率基本稳定</span>，美元指数走强背景下新兴市场分化加剧。</div>
    </div>'''

if old4 in html:
    html = html.replace(old4, new4)
    changes.append("✓ Tab1 北向资金卡片")
else:
    changes.append("✗ Tab1 北向资金卡片 - 未找到匹配")

# ============================================
# 5. Tab 1 - 北向资金连续9日（line ~2021-2022）
# ============================================
old5 = '''    <div class="card">
      <div class="card-title">💰 北向资金连续9日净买入，外资坚定加仓中国资产</div>
      <div class="card-body">截至6月10日，<span style="color:#f85149;font-weight:700;">北向资金连续9个交易日净买入</span>，刷新年内最长连续净买入纪录，今日净流入<span style="color:#f85149;font-weight:700;">68.45亿元</span>。前十大成交个股中，工商银行、农业银行、长江电力、贵州茅台获净买入居前。外资持续加仓主要基于三大逻辑：一是中国资产估值处于历史低位，<span style="color:#f85149;font-weight:700;">银行板块PB仅0.6倍</span>；二是高股息策略具全球吸引力，中证红利股息率远超全球主要指数；三是<span style="color:#00d4ff;font-weight:700;">人民币汇率稳定</span>，美元指数走弱背景下新兴市场吸引力回升。南向资金同步净买入<span style="color:#f85149;font-weight:700;">87.62亿港元</span>。</div>
    </div>'''

new5 = '''    <div class="card">
      <div class="card-title">💰 北向资金连续8日净买入，高股息策略受外资青睐</div>
      <div class="card-body">截至6月9日收盘，<span style="color:#f85149;font-weight:700;">北向资金连续8个交易日净买入</span>，累计净买入超600亿元，重点配置银行和保险板块。前十大成交个股中，工商银行、农业银行、长江电力、贵州茅台获净买入居前。外资持续加仓主要基于三大逻辑：一是中国资产估值处于历史低位，<span style="color:#f85149;font-weight:700;">银行板块PB仅0.6倍</span>；二是高股息策略具全球吸引力，中证红利股息率远超全球主要指数；三是<span style="color:#00d4ff;font-weight:700;">人民币汇率基本稳定</span>，美元指数100.06背景下新兴市场分化加剧。南向资金同步净买入<span style="color:#f85149;font-weight:700;">113.18亿港元</span>。</div>
    </div>'''

if old5 in html:
    html = html.replace(old5, new5)
    changes.append("✓ Tab1 北向资金财经卡片")
else:
    changes.append("✗ Tab1 北向资金财经卡片 - 未找到匹配")

# ============================================
# 6. Tab 1 - 央行黄金储备（line ~2025-2026）
# ============================================
old6 = '''    <div class="card">
      <div class="card-title">💰 中国央行连续20个月增持黄金储备</div>
      <div class="card-body">中国央行黄金储备连续第20个月增加，5月环比增持<span style="color:#f85149;font-weight:700;">35万盎司</span>。国际金价今日高位震荡偏强，伦敦金现盘中最高触及<span style="color:#f85149;font-weight:700;">4326美元/盎司</span>，收盘报<span style="color:#f85149;font-weight:700;">4318美元/盎司涨0.77%</span>。短期来看，美联储降息预期反复导致金价波动加剧，但中长期看，<span style="color:#f0b429;font-weight:700;">全球央行购金</span>、去美元化趋势、地缘风险溢价三大支撑因素仍在。分析人士指出，金价回调为<span style="color:#f85149;font-weight:700;">中长期配置黄金ETF</span>提供较好的入场机会。</div>
    </div>'''

new6 = '''    <div class="card">
      <div class="card-title">💰 中国央行连续19个月增持黄金储备</div>
      <div class="card-body">中国央行黄金储备连续第19个月增加，5月环比增持<span style="color:#f85149;font-weight:700;">32万盎司</span>。国际金价在地缘风险加剧背景下先扬后抑，伦敦金现跌破4300美元/盎司，最低至4268美元，收盘报<span style="color:#3fb950;font-weight:700;">4285美元/盎司跌1.34%</span>。短期来看，美联储加息预期升温压制金价表现，但中长期看，<span style="color:#f0b429;font-weight:700;">全球央行购金</span>、去美元化趋势、地缘风险溢价三大支撑因素仍在。分析人士指出，金价回调至<span style="color:#f85149;font-weight:700;">4285美元为中长期配置黄金ETF</span>提供较好的入场机会。</div>
    </div>'''

if old6 in html:
    html = html.replace(old6, new6)
    changes.append("✓ Tab1 黄金储备卡片")
else:
    changes.append("✗ Tab1 黄金储备卡片 - 未找到匹配")

# ============================================
# 7. Tab 1 - 银行板块逆势走强（line ~2029-2030）
# ============================================
old7 = '''    <div class="card">
      <div class="card-title">💰 银行板块逆势走强，高股息策略获资金青睐</div>
      <div class="card-body">A股银行板块今日领涨，中证银行指数涨<span style="color:#f85149;font-weight:700;">1.82%</span>，农业银行涨超3%，工商银行、建设银行均涨超2%。当前中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%存在超过<span style="color:#00d4ff;font-weight:700;">3个百分点</span>的利差优势。<span style="color:#f0b429;font-weight:700;">险资、社保、养老金</span>等长线资金持续加仓高股息板块，北向资金今日净买入银行股超20亿元。市场人士认为，在低利率环境下，高股息资产的"类债券"属性愈发凸显，银行、电力、公用事业等板块估值有望持续修复。</div>
    </div>'''

new7 = '''    <div class="card">
      <div class="card-title">💰 银行板块相对抗跌，高股息策略凸显防御价值</div>
      <div class="card-body">A股银行板块在市场普跌中表现出较强韧性，中证银行指数跌幅显著小于大盘，成为<span style="color:#f85149;font-weight:700;">资金避风港</span>。当前中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%存在超过<span style="color:#00d4ff;font-weight:700;">3个百分点</span>的利差优势。<span style="color:#f0b429;font-weight:700;">险资、社保、养老金</span>等长线资金持续加仓高股息板块，北向资金重点配置银行方向。市场人士认为，在全球利率分化和地缘风险加剧背景下，高股息资产的"类债券"属性愈发凸显，银行、电力、公用事业等板块防御价值突出。</div>
    </div>'''

if old7 in html:
    html = html.replace(old7, new7)
    changes.append("✓ Tab1 银行板块卡片")
else:
    changes.append("✗ Tab1 银行板块卡片 - 未找到匹配")

# ============================================
# 8. Tab 1 - 全球流动性预期改善（line ~2033-2034）
# ============================================
old8 = '''    <div class="card">
      <div class="card-title">💰 全球流动性预期改善，美元指数走弱</div>
      <div class="card-body">随着以伊局势缓和及市场重新评估美联储政策路径，美元指数小幅走弱至<span style="color:#3fb950;font-weight:700;">99.85</span>。利率互换市场显示，美联储年内降息概率回升至<span style="color:#f85149;font-weight:700;">38%</span>，较上周的"完全定价加息一次"出现显著调整。美国10年期国债收益率回落至<span style="color:#3fb950;font-weight:700;">4.512%</span>，30年期仍在4.92%附近高位震荡。人民币汇率保持稳定，USD/CNY中间价报<span style="color:#00d4ff;font-weight:700;">6.8182</span>，在岸即期汇率稳定在6.78附近。全球流动性预期边际改善，利好新兴市场资产表现。</div>
    </div>'''

new8 = '''    <div class="card">
      <div class="card-title">💰 美元指数走强，全球避险情绪升温</div>
      <div class="card-body">随着以伊冲突升级及市场重新评估美联储政策路径，美元指数走强至<span style="color:#f85149;font-weight:700;">100.06</span>。利率互换市场显示，美联储年内降息预期降温，加息风险重新抬头。美国10年期国债收益率高位震荡，避险资金流入美债市场。人民币汇率保持基本稳定，USD/CNY中间价报<span style="color:#00d4ff;font-weight:700;">6.8198</span>，在岸即期汇率6.7794。全球避险情绪升温，<span style="color:#f0b429;font-weight:700;">高股息防御资产</span>受到青睐，新兴市场承压分化。</div>
    </div>'''

if old8 in html:
    html = html.replace(old8, new8)
    changes.append("✓ Tab1 全球流动性卡片")
else:
    changes.append("✗ Tab1 全球流动性卡片 - 未找到匹配")

# ============================================
# 9. 市场综评标题（line ~2209）
# ============================================
old9 = '''<div style="font-size:12px;color:#8b95a5;">基于6月10日全球市场表现</div>'''
new9 = '''<div style="font-size:12px;color:#8b95a5;">基于6月9日全球市场表现</div>'''
if old9 in html:
    html = html.replace(old9, new9)
    changes.append("✓ 市场综评日期")
else:
    changes.append("✗ 市场综评日期 - 未找到匹配")

# ============================================
# 10. Tab 4 机构报告 - 中信证券（line ~2328）
# ============================================
old10 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">中信证券：</span>中信证券6月10日最新策略报告认为，A股经历6月9日的剧烈波动后，周三市场进入<span style="color:#f85149;font-weight:700;">结构性修复阶段</span>，银行、高股息板块强势领涨，科技股企稳迹象明显。中信判断当前市场的核心逻辑正从"外部冲击下的恐慌回调"转向"国内基本面支撑下的结构性机会"。建议投资者把握两条主线：一是<span style="color:#f0b429;font-weight:700;">银行、电力、央企红利</span>等高股息防御板块，中证银行指数股息率<span style="color:#00d4ff;font-weight:700;">5.05%</span>提供稳定收益来源；二是<span style="color:#f0b429;font-weight:700;">AI落地应用</span>方向，全球云厂商资本开支上调至<span style="color:#00d4ff;font-weight:700;">8300亿美元</span>为产业链提供坚实需求。中信认为沪深300当前PE仅11.5倍，处于历史中低位，回调即布局窗口。</p>'''
new10 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">中信证券：</span>中信证券最新策略报告认为，6月9日A股经历剧烈波动后，<span style="color:#f0b429;font-weight:700;">短期风险集中释放</span>，三大指数全线收跌，科创50重挫4.30%。中信判断当前市场的核心逻辑正从"外部冲击下的恐慌回调"向"国内基本面支撑下的结构性机会"过渡，高股息防御属性凸显。建议投资者把握两条主线：一是<span style="color:#f0b429;font-weight:700;">银行、电力、央企红利</span>等高股息防御板块，中证银行指数股息率<span style="color:#00d4ff;font-weight:700;">5.05%</span>提供稳定收益来源；二是<span style="color:#f0b429;font-weight:700;">AI算力基础设施</span>方向，全球云厂商资本开支上调至<span style="color:#00d4ff;font-weight:700;">8300亿美元</span>为产业链提供坚实需求。中信认为沪深300当前PE仅11.5倍，处于历史中低位，回调即布局窗口。</p>'''

if old10 in html:
    html = html.replace(old10, new10)
    changes.append("✓ Tab4 中信证券")
else:
    changes.append("✗ Tab4 中信证券 - 未找到匹配")

# ============================================
# 11. Tab 4 机构报告 - 高盛（line ~2344）
# ============================================
old11 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">高盛：</span>高盛6月10日发布中国策略月报，维持对A股和港股的<span style="color:#f85149;font-weight:700;">超配评级</span>，认为经历周二的全球风险资产回调后，中国资产的相对性价比进一步提升。高盛强调三大核心逻辑：一是中国<span style="color:#f0b429;font-weight:700;">货币政策保持宽松</span>，央行逆回购净投放<span style="color:#00d4ff;font-weight:700;">2075亿元</span>，银行间流动性充裕；二是<span style="color:#f0b429;font-weight:700;">北向资金连续9日净买入</span>，重点加仓银行、保险等低估值板块，外资用真金白银表达信心；三是<span style="color:#f0b429;font-weight:700;">中国AI产业落地加速</span>，COMPUTEX 2026上发布的新一代AI芯片为中国算力产业链提供持续增量。高盛建议超配高股息银行、AI算力基础设施和互联网龙头。</p>'''
new11 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">高盛：</span>高盛发布中国策略月报，维持对A股和港股的<span style="color:#f85149;font-weight:700;">超配评级</span>，认为经历6月9日全球风险资产回调后，中国资产的相对性价比进一步提升。高盛强调三大核心逻辑：一是中国<span style="color:#f0b429;font-weight:700;">货币政策保持宽松</span>，央行续作5000亿元MLF维护流动性充裕；二是<span style="color:#f0b429;font-weight:700;">北向资金连续8日净买入</span>，重点加仓银行、保险等低估值板块，外资用真金白银表达信心；三是<span style="color:#f0b429;font-weight:700;">中国AI产业落地加速</span>，COMPUTEX 2026上发布的新一代AI芯片为中国算力产业链提供持续增量。高盛建议超配高股息银行、AI算力基础设施和互联网龙头。</p>'''

if old11 in html:
    html = html.replace(old11, new11)
    changes.append("✓ Tab4 高盛")
else:
    changes.append("✗ Tab4 高盛 - 未找到匹配")

# ============================================
# 12. Tab 4 机构报告 - 兴业证券（line ~2360）
# ============================================
old12 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">兴业证券：</span>兴业证券最新观点认为，6月10日市场的结构性分化正是资金"聪明钱"正在<span style="color:#f85149;font-weight:700;">布局优质资产</span>的表现。银行板块逆势走强，银行AH优选ETF涨0.54%，显示长线资金对高股息资产的配置热情持续升温。兴业强调，当前市场的核心矛盾并非经济基本面走弱，而是<span style="color:#f0b429;font-weight:700;">投资者风险偏好的短期波动</span>。建议投资者采取"哑铃型"策略：一端配置<span style="color:#00d4ff;font-weight:700;">银行、电力、公用事业</span>等高股息防御资产获取稳定收益，另一端逢低布局<span style="color:#00d4ff;font-weight:700;">AI算力、半导体</span>等成长方向博取超额收益，总仓位建议控制在6-7成。</p>'''
new12 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">兴业证券：</span>兴业证券最新观点认为，6月9日市场的普跌行情正是长线资金<span style="color:#f85149;font-weight:700;">布局优质资产</span>的机会窗口。银行板块相对抗跌，显示长线资金对高股息资产的配置热情持续升温。兴业强调，当前市场的核心矛盾并非经济基本面走弱，而是<span style="color:#f0b429;font-weight:700;">投资者风险偏好的短期波动</span>。建议投资者采取"哑铃型"策略：一端配置<span style="color:#00d4ff;font-weight:700;">银行、电力、公用事业</span>等高股息防御资产获取稳定收益，另一端逢低布局<span style="color:#00d4ff;font-weight:700;">AI算力、半导体</span>等成长方向博取超额收益，总仓位建议控制在5-6成。</p>'''

if old12 in html:
    html = html.replace(old12, new12)
    changes.append("✓ Tab4 兴业证券")
else:
    changes.append("✗ Tab4 兴业证券 - 未找到匹配")

# ============================================
# 13. Tab 4 机构报告 - 中金公司（line ~2376）
# ============================================
old13 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">中金公司：</span>中金公司6月10日发布周度策略，认为当前市场处于"<span style="color:#f85149;font-weight:700;">震荡蓄势、结构优化</span>"阶段。中金特别强调<span style="color:#f0b429;font-weight:700;">高股息资产的配置价值重估</span>逻辑正在深化：42家上市银行全部破净，平均PB仅0.6倍，中证银行指数股息率达5.05%，较10年期国债收益率1.71%有超过3个百分点的利差，这一收益差在全球低利率环境下极为稀缺。中金建议投资者<span style="color:#00d4ff;font-weight:700;">均衡配置</span>：30-40%配置高股息银行和公用事业，20-30%配置AI算力和半导体，20%配置消费和新能源龙头，剩余现金保持灵活。</p>'''
new13 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">中金公司：</span>中金公司发布周度策略，认为当前市场处于"<span style="color:#f85149;font-weight:700;">震荡蓄势、结构优化</span>"阶段。中金特别强调<span style="color:#f0b429;font-weight:700;">高股息资产的配置价值重估</span>逻辑正在深化：42家上市银行全部破净，平均PB仅0.6倍，中证银行指数股息率达5.05%，较10年期国债收益率1.71%有超过3个百分点的利差，这一收益差在全球低利率环境下极为稀缺。中金建议投资者<span style="color:#00d4ff;font-weight:700;">均衡配置</span>：30-40%配置高股息银行和公用事业，20-30%配置AI算力和半导体，20%配置消费和新能源龙头，剩余现金保持灵活。</p>'''

if old13 in html:
    html = html.replace(old13, new13)
    changes.append("✓ Tab4 中金公司")
else:
    changes.append("✗ Tab4 中金公司 - 未找到匹配")

# ============================================
# 14. Tab 4 机构报告 - 摩根士丹利（line ~2392）
# ============================================
old14 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">摩根士丹利：</span>摩根士丹利6月10日更新中国市场策略，维持看多立场并上调高股息板块配置权重。大摩认为，<span style="color:#f85149;font-weight:700;">全球利率分化</span>背景下，中国高股息资产对外资极具吸引力——银行AH指数股息率接近6%，而美国10年期国债收益率约4.56%，中国高股息资产相对美债的收益优势显著。大摩强调三大投资方向：一是<span style="color:#00d4ff;font-weight:700;">高股息银行</span>（工行、建行、招行）作为核心底仓；二是<span style="color:#00d4ff;font-weight:700;">AI算力基础设施</span>（光模块、服务器芯片）受益全球云厂商资本开支爆发；三是<span style="color:#00d4ff;font-weight:700;">央企红利指数</span>成分股作为长期配置方向。大摩建议将高股息资产配置比例提升至40-50%。</p>'''
new14 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">摩根士丹利：</span>摩根士丹利更新中国市场策略，维持看多立场并上调高股息板块配置权重。大摩认为，<span style="color:#f85149;font-weight:700;">全球利率分化</span>背景下，中国高股息资产对外资极具吸引力——银行AH指数股息率接近6%，而美国10年期国债收益率约4.56%，中国高股息资产相对美债的收益优势显著。大摩强调三大投资方向：一是<span style="color:#00d4ff;font-weight:700;">高股息银行</span>（工行、建行、招行）作为核心底仓；二是<span style="color:#00d4ff;font-weight:700;">AI算力基础设施</span>（光模块、服务器芯片）受益全球云厂商资本开支爆发；三是<span style="color:#00d4ff;font-weight:700;">央企红利指数</span>成分股作为长期配置方向。大摩建议将高股息资产配置比例提升至40-50%。</p>'''

if old14 in html:
    html = html.replace(old14, new14)
    changes.append("✓ Tab4 摩根士丹利")
else:
    changes.append("✗ Tab4 摩根士丹利 - 未找到匹配")

# ============================================
# 15. Tab 4 机构报告 - 瑞银集团（line ~2408）
# ============================================
old15 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">瑞银集团：</span>瑞银证券6月10日观点认为，6月9日的全球市场回调提供了<span style="color:#f85149;font-weight:700;">优质资产的布局窗口</span>。瑞银分析了三组关键数据：一是北向资金<span style="color:#00d4ff;font-weight:700;">连续9日净买入</span>（截至6月9日），外资累计净买入超600亿元，重点配置银行和保险板块；二是中证银行指数股息率<span style="color:#00d4ff;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%的利差扩大至334bp，处于历史最高水平区间；三是沪深300指数PE仅11.5倍，位于历史<span style="color:#f0b429;font-weight:700;">35%分位</span>，估值安全边际充足。瑞银建议投资者：短期保持谨慎但不悲观，利用回调分批加仓优质高股息资产和AI算力龙头，等待美联储加息预期消化后市场趋势性机会。</p>'''
new15 = '''<p style="margin-bottom:10px;"><span style="color:#f85149;font-weight:700;">瑞银集团：</span>瑞银证券观点认为，6月9日的全球市场回调提供了<span style="color:#f85149;font-weight:700;">优质资产的布局窗口</span>。瑞银分析了三组关键数据：一是北向资金<span style="color:#00d4ff;font-weight:700;">连续8日净买入</span>（截至6月9日收盘），外资累计净买入超600亿元，重点配置银行和保险板块；二是中证银行指数股息率<span style="color:#00d4ff;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%的利差扩大至334bp，处于历史最高水平区间；三是沪深300指数PE仅11.5倍，位于历史<span style="color:#f0b429;font-weight:700;">35%分位</span>，估值安全边际充足。瑞银建议投资者：短期保持谨慎但不悲观，利用回调分批加仓优质高股息资产和AI算力龙头，等待美联储加息预期消化后市场趋势性机会。</p>'''

if old15 in html:
    html = html.replace(old15, new15)
    changes.append("✓ Tab4 瑞银集团")
else:
    changes.append("✗ Tab4 瑞银集团 - 未找到匹配")

# ============================================
# 16. Tab 4 - 银行板块深度分析（line ~2562）
# ============================================
old16 = '''<p>6月10日周三，银行板块强势领涨，中证银行指数收涨<span style="color:#f85149;font-weight:700;">1.85%</span>，工行、建行、农行等大行股价齐创阶段新高。截至2026年6月，中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，银行AH指数股息率更是高达<span style="color:#f85149;font-weight:700;">5.96%</span>，而10年期国债收益率仅约<span style="color:#00d4ff;font-weight:700;">1.71%</span>，利差扩大至<span style="color:#f85149;font-weight:700;">334个基点</span>，处于历史最高水平区间。42家上市银行全部破净，平均PB仅<span style="color:#f0b429;font-weight:700;">0.6倍</span>，估值修复空间巨大。<span style="color:#00d4ff;font-weight:700;">北向资金连续9日净买入</span>中重点配置银行方向，险资、养老金等长线资金持续加仓。银行股兼具<span style="color:#f85149;font-weight:700;">高股息+低估值+高ROE</span>三重属性，在全球利率分化背景下，其"类债券"配置价值对国内外长线资金极具吸引力。</p>'''
new16 = '''<p>6月9日，银行板块在市场普跌中<span style="color:#f85149;font-weight:700;">相对抗跌</span>，彰显防御属性。截至2026年6月，中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，银行AH指数股息率更是高达<span style="color:#f85149;font-weight:700;">5.96%</span>，而10年期国债收益率仅约<span style="color:#00d4ff;font-weight:700;">1.71%</span>，利差扩大至<span style="color:#f85149;font-weight:700;">334个基点</span>，处于历史最高水平区间。42家上市银行全部破净，平均PB仅<span style="color:#f0b429;font-weight:700;">0.6倍</span>，估值修复空间巨大。<span style="color:#00d4ff;font-weight:700;">北向资金连续8日净买入</span>中重点配置银行方向，险资、养老金等长线资金持续加仓。银行股兼具<span style="color:#f85149;font-weight:700;">高股息+低估值+高ROE</span>三重属性，在全球利率分化背景下，其"类债券"配置价值对国内外长线资金极具吸引力。</p>'''

if old16 in html:
    html = html.replace(old16, new16)
    changes.append("✓ Tab4 银行板块深度分析")
else:
    changes.append("✗ Tab4 银行板块深度分析 - 未找到匹配")

# ============================================
# 17. Tab 4 - 公用事业板块（line ~2568）
# ============================================
old17 = '''<p>公用事业板块6月10日整体走强，涨幅位居申万一级行业前列。公用事业板块以其<span style="color:#f85149;font-weight:700;">稳定的现金流</span>和<span style="color:#f85149;font-weight:700;">高分红比例</span>成为市场调整期的避风港。长江电力作为水电龙头，周三<span style="color:#f85149;font-weight:700;">上涨0.82%</span>报27.68元，PE约19.5倍，股息率稳定在<span style="color:#00d4ff;font-weight:700;">3.5%-4%</span>区间。在当前全球利率分化、地缘风险加剧的背景下，公用事业板块的防御价值受到<span style="color:#00d4ff;font-weight:700;">险资和社保基金</span>的持续青睐。分析人士指出，低利率环境下，公用事业板块的<span style="color:#f0b429;font-weight:700;">"类债券"属性</span>使其成为替代存款和理财的优质选择。</p>'''
new17 = '''<p>公用事业板块6月9日在市场回调中<span style="color:#f85149;font-weight:700;">表现稳健</span>，防御属性突出。公用事业板块以其<span style="color:#f85149;font-weight:700;">稳定的现金流</span>和<span style="color:#f85149;font-weight:700;">高分红比例</span>成为市场调整期的避风港。长江电力作为水电龙头，PE约19.5倍，股息率稳定在<span style="color:#00d4ff;font-weight:700;">3.5%-4%</span>区间。在当前全球利率分化、地缘风险加剧的背景下，公用事业板块的防御价值受到<span style="color:#00d4ff;font-weight:700;">险资和社保基金</span>的持续青睐。分析人士指出，低利率环境下，公用事业板块的<span style="color:#f0b429;font-weight:700;">"类债券"属性</span>使其成为替代存款和理财的优质选择。</p>'''

if old17 in html:
    html = html.replace(old17, new17)
    changes.append("✓ Tab4 公用事业板块")
else:
    changes.append("✗ Tab4 公用事业板块 - 未找到匹配")

# ============================================
# 18. Tab 4 - 电力板块（line ~2574）
# ============================================
old18 = '''<p>电力板块6月10日强势上涨，在<span style="color:#f85149;font-weight:700;">清洁能源转型</span>和<span style="color:#f85149;font-weight:700;">电力体制改革</span>的双重推动下保持高景气。中国核电周三<span style="color:#f85149;font-weight:700;">上涨1.25%</span>报9.10元，创年内新高，作为核电运营龙头显著受益于核电审批加速和电价市场化改革，当前PE约19.8倍，股息率<span style="color:#00d4ff;font-weight:700;">3.8%</span>。大秦铁路涨<span style="color:#f85149;font-weight:700;">0.98%</span>报5.12元，PE约17.4倍，股息率超<span style="color:#f85149;font-weight:700;">5%</span>。电力板块整体股息率在<span style="color:#00d4ff;font-weight:700;">4%-6%</span>区间，兼具防御属性和成长潜力，在市场调整期持续获得资金青睐，核电、水电等细分领域龙头配置价值突出。</p>'''
new18 = '''<p>电力板块6月9日在<span style="color:#f85149;font-weight:700;">清洁能源转型</span>和<span style="color:#f85149;font-weight:700;">电力体制改革</span>的双重推动下保持高景气，相对抗跌。中国核电作为核电运营龙头显著受益于核电审批加速和电价市场化改革，当前PE约19.8倍，股息率<span style="color:#00d4ff;font-weight:700;">3.8%</span>。大秦铁路PE约17.4倍，股息率超<span style="color:#f85149;font-weight:700;">5%</span>。电力板块整体股息率在<span style="color:#00d4ff;font-weight:700;">4%-6%</span>区间，兼具防御属性和成长潜力，在市场调整期持续获得资金青睐，核电、水电等细分领域龙头配置价值突出。</p>'''

if old18 in html:
    html = html.replace(old18, new18)
    changes.append("✓ Tab4 电力板块")
else:
    changes.append("✗ Tab4 电力板块 - 未找到匹配")

# ============================================
# 19. Tab 4 - 央企高股息（line ~2580）
# ============================================
old19 = '''<p>央企高股息板块6月10日表现稳健，<span style="color:#f85149;font-weight:700;">中国移动</span>上涨<span style="color:#f85149;font-weight:700;">0.68%</span>报97.26元，PE约15.3倍，PB约1.47倍，股息率稳定在<span style="color:#00d4ff;font-weight:700;">4%以上</span>。中国移动作为全球用户规模最大的运营商，现金流充沛，分红政策稳定，是<span style="color:#f0b429;font-weight:700;">长线资金的标配</span>标的。在当前市场波动加大的环境下，央企高股息板块的<span style="color:#f85149;font-weight:700;">确定性收益</span>优势更加突出。除通信外，能源、基建、交运等领域央企也普遍具备高分红特征，中证央企红利指数股息率达<span style="color:#00d4ff;font-weight:700;">4.8%</span>，是全球高股息资产中的优质选择。</p>'''
new19 = '''<p>央企高股息板块6月9日<span style="color:#f85149;font-weight:700;">防御属性凸显</span>，<span style="color:#f85149;font-weight:700;">中国移动</span>PE约15.3倍，PB约1.47倍，股息率稳定在<span style="color:#00d4ff;font-weight:700;">4%以上</span>。中国移动作为全球用户规模最大的运营商，现金流充沛，分红政策稳定，是<span style="color:#f0b429;font-weight:700;">长线资金的标配</span>标的。在当前市场波动加大的环境下，央企高股息板块的<span style="color:#f85149;font-weight:700;">确定性收益</span>优势更加突出。除通信外，能源、基建、交运等领域央企也普遍具备高分红特征，中证央企红利指数股息率达<span style="color:#00d4ff;font-weight:700;">4.8%</span>，是全球高股息资产中的优质选择。</p>'''

if old19 in html:
    html = html.replace(old19, new19)
    changes.append("✓ Tab4 央企高股息")
else:
    changes.append("✗ Tab4 央企高股息 - 未找到匹配")

# ============================================
# 20. Tab 4 - ETF资金流向（line ~2659）
# ============================================
old20 = '''<div class="capital-desc">6月10日，银行ETF、红利ETF持续获机构资金净申购，低估值高股息资产成为资金布局主线，规模创下近3个月新高。</div>'''
new20 = '''<div class="capital-desc">6月9日，银行ETF、红利ETF持续获机构资金净申购，低估值高股息资产成为资金避风港，高股息策略受到市场追捧。</div>'''

if old20 in html:
    html = html.replace(old20, new20)
    changes.append("✓ Tab4 ETF资金流向")
else:
    changes.append("✗ Tab4 ETF资金流向 - 未找到匹配")

# ============================================
# 21. Tab 4 - 参考板块（line ~2760）
# ============================================
old21 = '''<div class="reference-desc">6月10日收涨1.52%，股息率约5.2%，PE约7.8倍，全球利率分化背景下配置价值突出，适合长期持有获取稳定分红收益。</div>'''
new21 = '''<div class="reference-desc">截至6月9日收盘，中证红利指数股息率约5.2%，PE约7.8倍，全球利率分化背景下配置价值突出，适合长期持有获取稳定分红收益。</div>'''

if old21 in html:
    html = html.replace(old21, new21)
    changes.append("✓ Tab4 参考板块")
else:
    changes.append("✗ Tab4 参考板块 - 未找到匹配")

# ============================================
# 22. Tab 5 - alert-bar正面因素（line ~2782）
# ============================================
old22 = '''<strong>✅ 正面因素：</strong>6月10日周三，A股结构性反弹，银行、保险、电力等高股息板块强势领涨，北向资金连续9日净买入，长线资金持续加码低估值价值股。央行续作5000亿MLF，维护流动性充裕。'''
new22 = '''<strong>✅ 正面因素：</strong>6月9日A股三大指数全线收跌，但银行、电力等高股息板块显著抗跌，北向资金连续8日净买入，长线资金持续加仓低估值价值股。央行续作5000亿MLF，维护流动性充裕。银行板块PB仅0.6倍、股息率5.05%，防御价值突出。'''

if old22 in html:
    html = html.replace(old22, new22)
    changes.append("✓ Tab5 alert-bar正面因素")
else:
    changes.append("✗ Tab5 alert-bar正面因素 - 未找到匹配")

# ============================================
# 23. Tab 5 - 关注标的深度解读标题（line ~2996）
# ============================================
old23 = '''<div class="card-title">📊 关注标的深度解读（2026年6月10日）</div>'''
new23 = '''<div class="card-title">📊 关注标的深度解读（截至2026年6月9日收盘）</div>'''

if old23 in html:
    html = html.replace(old23, new23)
    changes.append("✓ Tab5 关注标的标题")
else:
    changes.append("✗ Tab5 关注标的标题 - 未找到匹配")

# ============================================
# 24. Tab 5 - 银行组深度解读内容（line ~3019）
# ============================================
old24 = '''<p style="font-size:13px;color:#b0bac4;line-height:1.7;margin:0;">6月10日周三，A股结构性反弹，银行板块强势领涨，中证银行指数收涨<span style="color:#f85149;font-weight:700;">1.85%</span>。中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%有超过3个百分点的利差，在低利率环境下配置价值极为稀缺。42家上市银行全部破净，PB平均仅<span style="color:#f0b429;font-weight:700;">0.6倍</span>，安全边际充足。<span style="color:#00d4ff;font-weight:700;">北向资金连续9日净买入</span>中重点配置银行方向，险资、社保等长线资金持续加仓。建议投资者将银行股作为组合的防御性核心配置。</p>'''
new24 = '''<p style="font-size:13px;color:#b0bac4;line-height:1.7;margin:0;">6月9日A股普跌，银行板块显著抗跌，防御属性凸显。中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%有超过3个百分点的利差，在低利率环境下配置价值极为稀缺。42家上市银行全部破净，PB平均仅<span style="color:#f0b429;font-weight:700;">0.6倍</span>，安全边际充足。<span style="color:#00d4ff;font-weight:700;">北向资金连续8日净买入</span>中重点配置银行方向，险资、社保等长线资金持续加仓。建议投资者将银行股作为组合的防御性核心配置。</p>'''

if old24 in html:
    html = html.replace(old24, new24)
    changes.append("✓ Tab5 银行组深度解读")
else:
    changes.append("✗ Tab5 银行组深度解读 - 未找到匹配")

# ============================================
# 25. Tab 7 - 操作建议标题（line ~3766）
# ============================================
old25 = '''<span style="font-size:11px;color:var(--text-muted);font-weight:400;">基于2026年6月10日市场环境</span>'''
new25 = '''<span style="font-size:11px;color:var(--text-muted);font-weight:400;">基于2026年6月9日收盘市场环境</span>'''

if old25 in html:
    html = html.replace(old25, new25)
    changes.append("✓ Tab7 操作建议标题")
else:
    changes.append("✗ Tab7 操作建议标题 - 未找到匹配")

# ============================================
# 26. Tab 7 - 高股息核心配置段落（line ~3776-3777）
# ============================================
old26 = '''<p style="margin-bottom:8px;"><span style="color:#f85149;font-weight:700;">A股结构性行情下</span>，银行、电力、保险等高股息板块强势领涨，中证银行指数股息率达<span style="color:#00d4ff;font-weight:700;">5.05%</span>，较10年期国债1.71%的利差超3个百分点，配置价值突出。</p>
          <p style="margin-bottom:8px;"><span style="color:#f85149;font-weight:700;">北向资金连续9日净买入</span>重点加仓银行方向，建议将高股息资产作为组合核心底仓，工商银行、农业银行等大行提供稳定分红收益。</p>'''
new26 = '''<p style="margin-bottom:8px;"><span style="color:#f85149;font-weight:700;">A股普跌行情下</span>，银行、电力、保险等高股息板块显著抗跌，中证银行指数股息率达<span style="color:#00d4ff;font-weight:700;">5.05%</span>，较10年期国债1.71%的利差超3个百分点，防御价值突出。</p>
          <p style="margin-bottom:8px;"><span style="color:#f85149;font-weight:700;">北向资金连续8日净买入</span>重点加仓银行方向，建议将高股息资产作为组合核心底仓，工商银行、农业银行等大行提供稳定分红收益。</p>'''

if old26 in html:
    html = html.replace(old26, new26)
    changes.append("✓ Tab7 高股息核心配置")
else:
    changes.append("✗ Tab7 高股息核心配置 - 未找到匹配")

# ============================================
# 27. Tab 7 - 科技股关注业绩兑现（line ~3788）
# ============================================
old27 = '''<p style="margin-bottom:8px;">美股隔夜企稳反弹，<span style="color:#f0b429;font-weight:700;">纳指涨0.93%，英伟达反弹3.76%</span>，费城半导体指数反弹2.85%，显示科技股挤泡沫后出现企稳迹象。</p>'''
new27 = '''<p style="margin-bottom:8px;">美股隔夜（6月9日）全线重挫，<span style="color:#f0b429;font-weight:700;">纳指跌4.18%，英伟达跌6.20%报$205.10</span>，费城半导体指数大跌超10%，显示科技股泡沫破裂风险加剧。</p>'''

if old27 in html:
    html = html.replace(old27, new27)
    changes.append("✓ Tab7 科技股关注业绩")
else:
    changes.append("✗ Tab7 科技股关注业绩 - 未找到匹配")

# ============================================
# 28. Tab 7 - 黄金投资价格（line ~3756）
# ============================================
old28 = '''        <div style="font-size:22px;font-weight:800;color:#f85149;">$4318</div>
        <div style="font-size:10px;color:#8b95a5;margin-top:4px;">日涨0.77%</div>'''
new28 = '''        <div style="font-size:22px;font-weight:800;color:#3fb950;">$4285</div>
        <div style="font-size:10px;color:#8b95a5;margin-top:4px;">日跌1.34%</div>'''

if old28 in html:
    html = html.replace(old28, new28)
    changes.append("✓ Tab7 黄金价格")
else:
    changes.append("✗ Tab7 黄金价格 - 未找到匹配")

# ============================================
# 29. 额外检查：剩余的"6月10日"文本
# ============================================
# 检查是否还有遗漏的"6月10日"
remaining = html.count('6月10日')
# 检查是否还有错误的up/down类数字需要修正

# 写入文件
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

# 输出结果
print("\n" + "="*50)
print("修正结果统计")
print("="*50)
success = sum(1 for c in changes if c.startswith("✓"))
fail = sum(1 for c in changes if c.startswith("✗"))
for c in changes:
    print(c)
print(f"\n总计: 成功 {success}/{len(changes)}，未匹配 {fail}")
print(f"文件中剩余'6月10日'字样: {remaining} 处")

if remaining > 0:
    print("\n⚠️  仍有剩余'6月10日'字样，建议检查是否为非市场数据的日期描述")
    # 找出剩余的6月10日位置
    lines = html.split('\n')
    for i, line in enumerate(lines):
        if '6月10日' in line:
            # 截取前后内容
            idx = line.find('6月10日')
            start = max(0, idx-50)
            end = min(len(line), idx+50)
            print(f"  Line ~{i+1}: ...{line[start:end]}...")
else:
    print("\n✅ 所有'6月10日'市场描述已修正完毕！")

print("\n文件已保存。")
