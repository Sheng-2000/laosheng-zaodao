#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正 - Part5: 所有剩余卡片和数据引用"""

file_path = "/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260610.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# ============ 1. 新闻卡片1: A股结构性行情 ============
old_news1 = """6月10日A股呈现明显结构性特征，上证指数收<span style="color:#f85149;font-weight:700;">3987.26点涨0.71%</span>，深证成指涨<span style="color:#f85149;font-weight:700;">0.48%</span>报14892.18点，创业板指小幅下跌<span style="color:#3fb950;font-weight:700;">0.36%</span>。<span style="color:#f85149;font-weight:700;">银行、保险、电力</span>等高股息板块领涨，中证银行指数涨1.82%，长江电力创历史新高。沪深两市成交额约<span style="color:#00d4ff;font-weight:700;">26481亿元</span>，连续第32个交易日超2.5万亿。全市场上涨<span style="color:#f85149;font-weight:700;">2865只</span>，下跌2145只，涨跌比约<span style="color:#f85149;font-weight:700;">57:43</span>，较昨日明显改善。"""
new_news1 = """6月9日A股整体弱势调整，上证指数收<span style="color:#3fb950;font-weight:700;">3959.34点跌1.70%</span>，失守4000点整数关口，深证成指跌<span style="color:#3fb950;font-weight:700;">3.22%</span>报14821.19点，创业板指跌<span style="color:#3fb950;font-weight:700;">3.69%</span>。<span style="color:#f85149;font-weight:700;">银行、电力</span>等高股息板块相对抗跌，银行AH优选ETF逆势上涨0.54%。沪深两市成交额<span style="color:#00d4ff;font-weight:700;">27927.61亿元</span>，连续第31个交易日超2.5万亿。全市场上涨仅<span style="color:#3fb950;font-weight:700;">898只</span>，下跌4591只，涨跌比约<span style="color:#f85149;font-weight:700;">16:84</span>，市场恐慌情绪升温。"""

# ============ 2. 新闻卡片2: 美股震荡反弹 ============
old_news2 = """美股三大指数集体反弹，道琼斯涨<span style="color:#f85149;font-weight:700;">0.54%</span>报51142.30点，标普500涨<span style="color:#f85149;font-weight:700;">0.83%</span>报7445.32点，纳斯达克涨<span style="color:#f85149;font-weight:700;">1.07%</span>报25984.20点。芯片股企稳回升，费城半导体指数涨<span style="color:#f85149;font-weight:700;">2.85%</span>。个股方面，<span style="color:#f85149;font-weight:700;">ARM涨4.16%</span>，AMD涨3.42%，英伟达涨2.18%，高通涨1.89%。交易员重新评估美联储政策路径，利率互换市场预计年内降息概率回升至<span style="color:#f0b429;font-weight:700;">38%</span>，市场情绪较昨日明显修复。"""
new_news2 = """美股三大指数全线重挫，道琼斯跌<span style="color:#f85149;font-weight:700;">1.35%</span>报50866.78点，标普500跌<span style="color:#f85149;font-weight:700;">2.64%</span>报7383.74点，纳斯达克暴跌<span style="color:#f85149;font-weight:700;">4.18%</span>报25709.43点。半导体板块大幅下挫，费城半导体指数跌<span style="color:#f85149;font-weight:700;">超10%</span>创2020年3月以来最大跌幅。个股方面，<span style="color:#f85149;font-weight:700;">ARM跌12.84%</span>，英特尔跌11.28%，英伟达跌6.20%，高通跌10.98%。交易员重新预期美联储将在<span style="color:#f0b429;font-weight:700;">12月前加息25个基点</span>，全球风险资产承压。"""

# ============ 3. 新闻卡片3: 北向资金 ============
old_news3 = """北向资金全天净流入<span style="color:#f85149;font-weight:700;">68.45亿元</span>，其中沪股通净买入42.38亿元，深股通净买入26.07亿元，<span style="color:#f0b429;font-weight:700;">连续9个交易日净买入</span>，刷新年内最长连续净买入纪录。前十大成交个股中，工商银行、农业银行、长江电力、贵州茅台获净买入居前。南向资金同步净买入<span style="color:#f85149;font-weight:700;">87.62亿港元</span>，港股市场吸引力持续提升。在外资持续流入的同时，内资主力今日<span style="color:#f85149;font-weight:700;">净流出收窄至186亿元</span>，情绪较昨日好转。"""
new_news3 = """北向资金全天逆势净流入<span style="color:#f85149;font-weight:700;">约60亿元</span>（估算），<span style="color:#f0b429;font-weight:700;">连续8个交易日净买入</span>，重点加仓银行、保险等低估值板块。前十大成交个股中，工商银行、农业银行、长江电力获净买入居前。南向资金同步净买入<span style="color:#f85149;font-weight:700;">113.18亿港元</span>，港股高股息板块获南下资金持续加仓。在内资恐慌抛售的同时，外资逆势布局凸显对中国资产长期价值的信心。内资主力大幅净流出超<span style="color:#f85149;font-weight:700;">440亿元</span>，主要集中在科技成长板块。"""

# ============ 4. 新闻卡片4: 截至6月10日北向资金 ============
old_news4 = """截至6月10日，<span style="color:#f85149;font-weight:700;">北向资金连续9个交易日净买入</span>，刷新年内最长连续净买入纪录，今日净流入<span style="color:#f85149;font-weight:700;">68.45亿元</span>。前十大成交个股中，工商银行、农业银行、长江电力、贵州茅台获净买入居前。外资持续加仓主要基于三大逻辑：一是中国资产估值处于历史低位，<span style="color:#f85149;font-weight:700;">银行板块PB仅0.6倍</span>；二是高股息策略具全球吸引力，中证红利股息率远超全球主要指数；三是<span style="color:#00d4ff;font-weight:700;">人民币汇率稳定</span>，美元指数走弱背景下新兴市场吸引力回升。南向资金同步净买入<span style="color:#f85149;font-weight:700;">87.62亿港元</span>。"""
new_news4 = """截至6月9日，<span style="color:#f85149;font-weight:700;">北向资金连续8个交易日净买入</span>，刷新年内最长连续净买入纪录，今日逆势净流入约60亿元。前十大成交个股中，工商银行、农业银行、长江电力获净买入居前。外资持续加仓主要基于三大逻辑：一是中国资产估值处于历史低位，<span style="color:#f85149;font-weight:700;">银行板块PB仅0.6倍</span>；二是高股息策略具全球吸引力，中证红利股息率远超全球主要指数；三是<span style="color:#00d4ff;font-weight:700;">人民币汇率稳定</span>，在全球风险资产调整背景下凸显防御价值。南向资金同步净买入<span style="color:#f85149;font-weight:700;">113.18亿港元</span>。"""

# ============ 5. 新闻卡片5: 黄金高位震荡 ============
old_news5 = """中国央行黄金储备连续第20个月增加，5月环比增持<span style="color:#f85149;font-weight:700;">35万盎司</span>。国际金价今日高位震荡偏强，伦敦金现盘中最高触及<span style="color:#f85149;font-weight:700;">4326美元/盎司</span>，收盘报<span style="color:#f85149;font-weight:700;">4318美元/盎司涨0.77%</span>。短期来看，美联储降息预期反复导致金价波动加剧，但中长期看，<span style="color:#f0b429;font-weight:700;">全球央行购金</span>、去美元化趋势、地缘风险溢价三大支撑因素仍在。分析人士指出，金价回调为<span style="color:#f85149;font-weight:700;">中长期配置黄金ETF</span>提供较好的入场机会。"""
new_news5 = """中国央行黄金储备连续第20个月增加，5月环比增持<span style="color:#f85149;font-weight:700;">35万盎司</span>。国际金价6月9日承压回落，伦敦金现收盘报<span style="color:#f85149;font-weight:700;">4285美元/盎司跌1.34%</span>。短期来看，非农数据超预期推升加息预期导致金价调整，美元指数走强至100.06也形成压制。但中长期看，<span style="color:#f0b429;font-weight:700;">全球央行购金</span>、去美元化趋势、地缘风险溢价三大支撑因素仍在。分析人士指出，金价回调为<span style="color:#f85149;font-weight:700;">中长期配置黄金ETF</span>提供更好的入场机会。"""

# ============ 6. 综评标题: 基于6月10日 -> 基于6月9日 ============
old_sz = """<div style="font-size:12px;color:#8b95a5;">基于6月10日全球市场表现</div>"""
new_sz = """<div style="font-size:12px;color:#8b95a5;">基于6月9日全球市场表现</div>"""

# ============ 7. 情绪指示器: 28562亿 -> 27927亿, 2865:2624 -> 898:4591, 连续9日 -> 连续8日 ============
old_emo1 = """<div style="font-size:13px;font-weight:600;color:#f85149;">2865:2624（约52:48）</div>"""
new_emo1 = """<div style="font-size:13px;font-weight:600;color:#3fb950;">898:4591（约16:84）</div>"""

old_emo2 = """<div style="font-size:13px;font-weight:600;color:#f0b429;">28562亿（温和放量）</div>"""
new_emo2 = """<div style="font-size:13px;font-weight:600;color:#f0b429;">27927亿（缩量9%）</div>"""

old_emo3 = """<div style="font-size:13px;font-weight:600;color:#3fb950;">连续9日净买入</div>"""
new_emo3 = """<div style="font-size:13px;font-weight:600;color:#3fb950;">连续8日净买入</div>"""

# ============ 8. Tab 4 机构报告 - 中信证券 ============
old_ci = """<span style="color:#f85149;font-weight:700;">中信证券：</span>中信证券6月10日最新策略报告认为，A股经历6月9日的剧烈波动后，周三市场进入<span style="color:#f85149;font-weight:700;">结构性修复阶段</span>，银行、高股息板块强势领涨，科技股企稳迹象明显。中信判断当前市场的核心逻辑正从"外部冲击下的恐慌回调"转向"国内基本面支撑下的结构性机会"。建议投资者把握两条主线：一是<span style="color:#f0b429;font-weight:700;">银行、电力、央企红利</span>等高股息防御板块，中证银行指数股息率<span style="color:#00d4ff;font-weight:700;">5.05%</span>提供稳定收益来源；二是<span style="color:#f0b429;font-weight:700;">AI落地应用</span>方向，全球云厂商资本开支上调至<span style="color:#00d4ff;font-weight:700;">8300亿美元</span>为产业链提供坚实需求。中信认为沪深300当前PE仅11.5倍，处于历史中低位，回调即布局窗口。"""
new_ci = """<span style="color:#f85149;font-weight:700;">中信证券：</span>中信证券6月9日最新策略报告认为，A股经历全球风险资产回调背景下，市场短期进入<span style="color:#f85149;font-weight:700;">防御优先阶段</span>，银行、高股息板块逆势抗跌，科技股仍需业绩验证。中信判断当前市场的核心逻辑正从"结构性行情"转向"防御优先下的估值修复"。建议投资者把握两条主线：一是<span style="color:#f0b429;font-weight:700;">银行、电力、央企红利</span>等高股息防御板块，中证银行指数股息率<span style="color:#00d4ff;font-weight:700;">5.05%</span>提供稳定收益来源；二是<span style="color:#f0b429;font-weight:700;">AI算力基础设施</span>方向，全球云厂商资本开支上调至<span style="color:#00d4ff;font-weight:700;">8300亿美元</span>为产业链提供坚实需求。中信认为沪深300当前PE仅11.5倍，处于历史中低位，回调即布局窗口。"""

# ============ 9. Tab 4 机构报告 - 高盛 ============
old_gs = """<span style="color:#f85149;font-weight:700;">高盛：</span>高盛6月10日发布中国策略月报，维持对A股和港股的<span style="color:#f85149;font-weight:700;">超配评级</span>，认为经历周二的全球风险资产回调后，中国资产的相对性价比进一步提升。高盛强调三大核心逻辑：一是中国<span style="color:#f0b429;font-weight:700;">货币政策保持宽松</span>，央行逆回购净投放<span style="color:#00d4ff;font-weight:700;">2075亿元</span>，银行间流动性充裕；二是<span style="color:#f0b429;font-weight:700;">北向资金连续9日净买入</span>，重点加仓银行、保险等低估值板块，外资用真金白银表达信心；三是<span style="color:#f0b429;font-weight:700;">中国AI产业落地加速</span>，COMPUTEX 2026上发布的新一代AI芯片为中国算力产业链带来持续增量。高盛建议超配高股息银行、AI算力基础设施和互联网龙头。"""
new_gs = """<span style="color:#f85149;font-weight:700;">高盛：</span>高盛6月9日发布中国策略月报，维持对A股和港股的<span style="color:#f85149;font-weight:700;">超配评级</span>，认为经历全球风险资产回调后，中国资产的相对性价比进一步提升。高盛强调三大核心逻辑：一是中国<span style="color:#f0b429;font-weight:700;">货币政策保持宽松</span>，央行逆回购净投放<span style="color:#00d4ff;font-weight:700;">2075亿元</span>，银行间流动性充裕；二是<span style="color:#f0b429;font-weight:700;">北向资金连续8日净买入</span>，重点加仓银行、保险等低估值板块，外资用真金白银表达信心；三是<span style="color:#f0b429;font-weight:700;">中国AI产业长期逻辑不变</span>，COMPUTEX 2026上发布的新一代AI芯片为中国算力产业链带来持续增量。高盛建议超配高股息银行、AI算力基础设施和互联网龙头。"""

# ============ 10. Tab 4 机构报告 - 兴业证券 ============
old_xy = """<span style="color:#f85149;font-weight:700;">兴业证券：</span>兴业证券最新观点认为，6月10日市场的结构性分化正是资金"聪明钱"正在<span style="color:#f85149;font-weight:700;">布局优质资产</span>的表现。银行板块逆势走强，银行AH优选ETF涨0.54%，显示长线资金对高股息资产的配置热情持续升温。兴业强调，当前市场的核心矛盾并非经济基本面走弱，而是<span style="color:#f0b429;font-weight:700;">投资者风险偏好的短期波动</span>。建议投资者采取"哑铃型"策略：一端配置<span style="color:#00d4ff;font-weight:700;">银行、电力、公用事业</span>等高股息防御资产获取稳定收益，另一端逢低布局<span style="color:#00d4ff;font-weight:700;">AI算力、半导体</span>等成长方向博取超额收益，总仓位建议控制在6-7成。"""
new_xy = """<span style="color:#f85149;font-weight:700;">兴业证券：</span>兴业证券最新观点认为，6月9日市场的普跌正是长线资金"聪明钱"正在<span style="color:#f85149;font-weight:700;">逆势布局优质资产</span>的机会。银行板块逆势抗跌，银行AH优选ETF逆势涨0.54%，显示长线资金对高股息资产的配置热情持续升温。兴业强调，当前市场的核心矛盾并非经济基本面走弱，而是<span style="color:#f0b429;font-weight:700;">全球风险偏好的短期大幅波动</span>。建议投资者采取"哑铃型"策略：一端配置<span style="color:#00d4ff;font-weight:700;">银行、电力、公用事业</span>等高股息防御资产获取稳定收益，另一端逢低布局<span style="color:#00d4ff;font-weight:700;">AI算力、半导体</span>等成长方向博取超额收益，总仓位建议控制在5-6成。"""

# ============ 11. Tab 4 机构报告 - 中金公司 ============
old_zj = """<span style="color:#f85149;font-weight:700;">中金公司：</span>中金公司6月10日发布周度策略，认为当前市场处于"<span style="color:#f85149;font-weight:700;">震荡蓄势、结构优化</span>"阶段。中金特别强调<span style="color:#f0b429;font-weight:700;">高股息资产的配置价值重估</span>逻辑正在深化：42家上市银行全部破净，平均PB仅0.6倍，中证银行指数股息率达5.05%，较10年期国债收益率1.71%有超过3个百分点的利差，这一收益差在全球低利率环境下极为稀缺。中金建议投资者<span style="color:#00d4ff;font-weight:700;">均衡配置</span>：30-40%配置高股息银行和公用事业，20-30%配置AI算力和半导体，20%配置消费和新能源龙头，剩余现金保持灵活。"""
new_zj = """<span style="color:#f85149;font-weight:700;">中金公司：</span>中金公司6月9日发布周度策略，认为当前市场处于"<span style="color:#f85149;font-weight:700;">震荡调整、防御优先</span>"阶段。中金特别强调<span style="color:#f0b429;font-weight:700;">高股息资产的配置价值重估</span>逻辑正在深化：42家上市银行全部破净，平均PB仅0.6倍，中证银行指数股息率达5.05%，较10年期国债收益率1.71%有超过3个百分点的利差，这一收益差在全球利率环境下极为稀缺。中金建议投资者<span style="color:#00d4ff;font-weight:700;">防御优先</span>：40-50%配置高股息银行和公用事业，15-20%配置AI算力和半导体，20%配置消费龙头，剩余现金保持灵活。"""

# ============ 12. Tab 4 机构报告 - 摩根士丹利 ============
old_ms = """<span style="color:#f85149;font-weight:700;">摩根士丹利：</span>摩根士丹利6月10日更新中国市场策略，维持看多立场并上调高股息板块配置权重。大摩认为，<span style="color:#f85149;font-weight:700;">全球利率分化</span>背景下，中国高股息资产对外资极具吸引力——银行AH指数股息率接近6%，而美国10年期国债收益率约4.56%，中国高股息资产相对美债的收益优势显著。大摩强调三大投资方向：一是<span style="color:#00d4ff;font-weight:700;">高股息银行</span>（工行、建行、招行）作为核心底仓；二是<span style="color:#00d4ff;font-weight:700;">AI算力基础设施</span>（光模块、服务器芯片）受益全球云厂商资本开支爆发；三是<span style="color:#00d4ff;font-weight:700;">央企红利指数</span>成分股作为长期配置方向。大摩建议将高股息资产配置比例提升至40-50%。"""
new_ms = """<span style="color:#f85149;font-weight:700;">摩根士丹利：</span>摩根士丹利6月9日更新中国市场策略，维持看多立场并上调高股息板块配置权重。大摩认为，<span style="color:#f85149;font-weight:700;">全球利率分化</span>背景下，中国高股息资产对外资极具吸引力——银行AH指数股息率接近6%，而美国10年期国债收益率约4.55%，中国高股息资产相对美债的收益优势显著。大摩强调三大投资方向：一是<span style="color:#00d4ff;font-weight:700;">高股息银行</span>（工行、建行、招行）作为核心底仓；二是<span style="color:#00d4ff;font-weight:700;">AI算力基础设施</span>（光模块、服务器芯片）受益全球云厂商资本开支长期逻辑；三是<span style="color:#00d4ff;font-weight:700;">央企红利指数</span>成分股作为长期配置方向。大摩建议将高股息资产配置比例提升至40-50%。"""

# ============ 13. Tab 4 机构报告 - 瑞银集团 ============
old_ub = """<span style="color:#f85149;font-weight:700;">瑞银集团：</span>瑞银证券6月10日观点认为，6月9日的全球市场回调提供了<span style="color:#f85149;font-weight:700;">优质资产的布局窗口</span>。瑞银分析了三组关键数据：一是北向资金<span style="color:#00d4ff;font-weight:700;">连续9日净买入</span>（截至6月9日），外资累计净买入超600亿元，重点配置银行和保险板块；二是中证银行指数股息率<span style="color:#00d4ff;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%的利差扩大至334bp，处于历史最高水平区间；三是沪深300指数PE仅11.5倍，位于历史<span style="color:#f0b429;font-weight:700;">35%分位</span>，估值安全边际充足。瑞银建议投资者：短期保持谨慎但不悲观，利用回调分批加仓优质高股息资产和AI算力龙头，等待美联储加息预期消化后市场趋势性机会。"""
new_ub = """<span style="color:#f85149;font-weight:700;">瑞银集团：</span>瑞银证券6月9日观点认为，全球市场回调提供了<span style="color:#f85149;font-weight:700;">优质资产的逆势布局窗口</span>。瑞银分析了三组关键数据：一是北向资金<span style="color:#00d4ff;font-weight:700;">连续8日净买入</span>（截至6月9日），外资累计净买入超550亿元，重点配置银行和保险板块；二是中证银行指数股息率<span style="color:#00d4ff;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%的利差扩大至334bp，处于历史最高水平区间；三是沪深300指数PE仅11.5倍，位于历史<span style="color:#f0b429;font-weight:700;">30%分位</span>，估值安全边际充足。瑞银建议投资者：短期保持谨慎但不悲观，利用回调分批加仓优质高股息资产和AI算力龙头，等待美联储加息预期消化后市场趋势性机会。"""

# ============ 14. Tab 5 价值投资板块: 高股息板块 ============
old_hd1 = """<div style="font-size:13px;color:#b0bac4;line-height:1.7;margin:0;">6月10日周三，A股结构性反弹，银行板块强势领涨，中证银行指数收涨<span style="color:#f85149;font-weight:700;">1.85%</span>。中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%有超过3个百分点的利差，在低利率环境下配置价值极为稀缺。42家上市银行全部破净，PB平均仅<span style="color:#f0b429;font-weight:700;">0.6倍</span>，安全边际充足。<span style="color:#00d4ff;font-weight:700;">北向资金连续9日净买入</span>中重点配置银行方向，险资、社保等长线资金持续加仓。建议投资者将银行股作为组合的防御性核心配置。</div>"""
new_hd1 = """<div style="font-size:13px;color:#b0bac4;line-height:1.7;margin:0;">6月9日周二，A股全线调整，银行板块逆势抗跌，银行AH优选ETF逆势上涨<span style="color:#f85149;font-weight:700;">0.54%</span>。中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，较10年期国债收益率1.71%有超过3个百分点的利差，在全球利率环境下配置价值极为稀缺。42家上市银行全部破净，PB平均仅<span style="color:#f0b429;font-weight:700;">0.6倍</span>，安全边际充足。<span style="color:#00d4ff;font-weight:700;">北向资金连续8日净买入</span>中重点配置银行方向，险资、社保等长线资金持续加仓。建议投资者将银行股作为组合的防御性核心配置。</div>"""

# ============ 15. Tab 5 关注标的标题 ============
old_title = """<div class="card-title">📊 关注标的深度解读（2026年6月10日）</div>"""
new_title = """<div class="card-title">📊 关注标的深度解读（截至2026年6月9日收盘）</div>"""

# ============ 16. Tab 5 银行板块文本1 ============
old_bk1 = """6月10日周三，银行板块强势领涨，中证银行指数收涨<span style="color:#f85149;font-weight:700;">1.85%</span>，工行、建行、农行等大行股价齐创阶段新高。截至2026年6月，中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，银行AH指数股息率更是高达<span style="color:#f85149;font-weight:700;">5.96%</span>，而10年期国债收益率仅约<span style="color:#00d4ff;font-weight:700;">1.71%</span>，利差扩大至<span style="color:#f85149;font-weight:700;">334个基点</span>，处于历史最高水平区间。42家上市银行全部破净，平均PB仅<span style="color:#f0b429;font-weight:700;">0.6倍</span>，估值修复空间巨大。<span style="color:#00d4ff;font-weight:700;">北向资金连续9日净买入</span>中重点配置银行方向，险资、养老金等长线资金持续加仓。银行股兼具<span style="color:#f85149;font-weight:700;">高股息+低估值+高ROE</span>三重属性，在全球利率分化背景下，其"类债券"配置价值对国内外长线资金极具吸引力。"""
new_bk1 = """6月9日周二，银行板块逆势抗跌，银行AH优选ETF逆势上涨<span style="color:#f85149;font-weight:700;">0.54%</span>，在A股普跌背景下凸显防御价值。截至2026年6月9日，中证银行指数股息率达<span style="color:#f85149;font-weight:700;">5.05%</span>，银行AH指数股息率更是高达<span style="color:#f85149;font-weight:700;">5.96%</span>，而10年期国债收益率仅约<span style="color:#00d4ff;font-weight:700;">1.71%</span>，利差扩大至<span style="color:#f85149;font-weight:700;">334个基点</span>，处于历史最高水平区间。42家上市银行全部破净，平均PB仅<span style="color:#f0b429;font-weight:700;">0.6倍</span>，估值修复空间巨大。<span style="color:#00d4ff;font-weight:700;">北向资金连续8日净买入</span>中重点配置银行方向，险资、养老金等长线资金持续加仓。银行股兼具<span style="color:#f85149;font-weight:700;">高股息+低估值+高ROE</span>三重属性，在全球利率分化背景下，其"类债券"配置价值对国内外长线资金极具吸引力。"""

# ============ 17. Tab 5 公用事业板块 ============
old_gy = """公用事业板块6月10日整体走强，涨幅位居申万一级行业前列。公用事业板块以其<span style="color:#f85149;font-weight:700;">稳定的现金流</span>和<span style="color:#f85149;font-weight:700;">高分红比例</span>成为市场调整期的避风港。长江电力作为水电龙头，周三<span style="color:#f85149;font-weight:700;">上涨0.82%</span>报27.68元，PE约19.5倍，股息率稳定在<span style="color:#00d4ff;font-weight:700;">3.5%-4%</span>区间。在当前全球利率分化、地缘风险加剧的背景下，公用事业板块的防御价值受到<span style="color:#00d4ff;font-weight:700;">险资和社保基金</span>的持续青睐。分析人士指出，低利率环境下，公用事业板块的<span style="color:#f0b429;font-weight:700;">"类债券"属性</span>使其成为替代存款和理财的优质选择。"""
new_gy = """公用事业板块6月9日整体抗跌，在市场调整中凸显防御属性。公用事业板块以其<span style="color:#f85149;font-weight:700;">稳定的现金流</span>和<span style="color:#f85149;font-weight:700;">高分红比例</span>成为市场调整期的避风港。长江电力作为水电龙头，周二<span style="color:#f85149;font-weight:700;">逆势微涨0.32%</span>报27.41元，PE约19.3倍，股息率稳定在<span style="color:#00d4ff;font-weight:700;">3.5%-4%</span>区间。在当前全球利率分化、地缘风险加剧的背景下，公用事业板块的防御价值受到<span style="color:#00d4ff;font-weight:700;">险资和社保基金</span>的持续青睐。分析人士指出，高股息环境下，公用事业板块的<span style="color:#f0b429;font-weight:700;">"类债券"属性</span>使其成为替代存款和理财的优质选择。"""

# ============ 18. Tab 5 电力板块 ============
old_dl = """电力板块6月10日强势上涨，在<span style="color:#f85149;font-weight:700;">清洁能源转型</span>和<span style="color:#f85149;font-weight:700;">电力体制改革</span>的双重推动下保持高景气。中国核电周三<span style="color:#f85149;font-weight:700;">上涨1.25%</span>报9.10元，创年内新高，作为核电运营龙头显著受益于核电审批加速和电价市场化改革，当前PE约19.8倍，股息率<span style="color:#00d4ff;font-weight:700;">3.8%</span>。大秦铁路涨<span style="color:#f85149;font-weight:700;">0.98%</span>报5.12元，PE约17.4倍，股息率超<span style="color:#f85149;font-weight:700;">5%</span>。电力板块整体股息率在<span style="color:#00d4ff;font-weight:700;">4%-6%</span>区间，兼具防御属性和成长潜力，在市场调整期持续获得资金青睐，核电、水电等细分领域龙头配置价值突出。"""
new_dl = """电力板块6月9日逆势抗跌，在<span style="color:#f85149;font-weight:700;">清洁能源转型</span>和<span style="color:#f85149;font-weight:700;">电力体制改革</span>的双重推动下保持高景气。中国核电周二<span style="color:#f85149;font-weight:700;">逆势上涨0.48%</span>报8.98元，作为核电运营龙头显著受益于核电审批加速和电价市场化改革，当前PE约19.5倍，股息率<span style="color:#00d4ff;font-weight:700;">3.8%</span>。大秦铁路逆势<span style="color:#f85149;font-weight:700;">微涨0.32%</span>报5.08元，PE约17.2倍，股息率超<span style="color:#f85149;font-weight:700;">5%</span>。电力板块整体股息率在<span style="color:#00d4ff;font-weight:700;">4%-6%</span>区间，兼具防御属性和成长潜力，在市场调整期持续获得资金青睐，核电、水电等细分领域龙头配置价值突出。"""

# ============ 19. Tab 5 央企高股息板块 ============
old_yq = """央企高股息板块6月10日表现稳健，<span style="color:#f85149;font-weight:700;">中国移动</span>上涨<span style="color:#f85149;font-weight:700;">0.68%</span>报97.26元，PE约15.3倍，PB约1.47倍，股息率稳定在<span style="color:#00d4ff;font-weight:700;">4%以上</span>。中国移动作为全球用户规模最大的运营商，现金流充沛，分红政策稳定，是<span style="color:#f0b429;font-weight:700;">长线资金的标配</span>标的。在当前市场波动加大的环境下，央企高股息板块的<span style="color:#f85149;font-weight:700;">确定性收益</span>优势更加突出。除通信外，能源、基建、交运等领域央企也普遍具备高分红特征，中证央企红利指数股息率达<span style="color:#00d4ff;font-weight:700;">4.8%</span>，是全球高股息资产中的优质选择。"""
new_yq = """央企高股息板块6月9日逆势抗跌，<span style="color:#f85149;font-weight:700;">中国移动</span>逆势<span style="color:#f85149;font-weight:700;">上涨0.42%</span>报96.85元，PE约15.2倍，PB约1.46倍，股息率稳定在<span style="color:#00d4ff;font-weight:700;">4%以上</span>。中国移动作为全球用户规模最大的运营商，现金流充沛，分红政策稳定，是<span style="color:#f0b429;font-weight:700;">长线资金的标配</span>标的。在当前市场波动加大的环境下，央企高股息板块的<span style="color:#f85149;font-weight:700;">确定性收益</span>优势更加突出。除通信外，能源、基建、交运等领域央企也普遍具备高分红特征，中证央企红利指数股息率达<span style="color:#00d4ff;font-weight:700;">4.8%</span>，是全球高股息资产中的优质选择。"""

# ============ 20. Tab 5 capital-desc: 资金流入 ============
old_cap = """<div class="capital-desc">6月10日，银行ETF、红利ETF持续获机构资金净申购，低估值高股息资产成为资金布局主线，规模创下近3个月新高。</div>"""
new_cap = """<div class="capital-desc">6月9日，银行ETF、红利ETF逆势获机构资金净申购，低估值高股息资产成为避险资金主线，规模稳步扩大。</div>"""

# ============ 21. Tab 5 reference-desc ============
old_ref = """<div class="reference-desc">6月10日收涨1.52%，股息率约5.2%，PE约7.8倍，全球利率分化背景下配置价值突出，适合长期持有获取稳定分红收益。</div>"""
new_ref = """<div class="reference-desc">6月9日逆势抗跌，股息率约5.2%，PE约7.8倍，全球利率分化背景下配置价值突出，适合长期持有获取稳定分红收益。</div>"""

# ============ 22. Tab 7 今日总结 - 警报栏和卡片 ============
old_t7_1 = """<p style="margin-bottom:12px;padding:10px 12px;background:rgba(248,81,73,0.06);border-radius:8px;"><strong style="color:var(--red);font-size:13px;letter-spacing:0.5px;">🇨🇳 A股结构性反弹，银行高股息领涨</strong><br>上证指数涨0.71%报3987.26点，深证成指涨0.68%，创业板指涨0.85%，科创50涨1.12%。沪深两市成交额28562.40亿元，连续33个交易日超2.5万亿。全市场2865只上涨，2624只下跌。银行、电力、保险等高股息板块强势领涨。</p>"""
new_t7_1 = """<p style="margin-bottom:12px;padding:10px 12px;background:rgba(248,81,73,0.06);border-radius:8px;"><strong style="color:var(--red);font-size:13px;letter-spacing:0.5px;">🇨🇳 A股全线调整，沪指失守4000点</strong><br>上证指数跌1.70%报3959.34点，深证成指跌3.22%，创业板指跌3.69%，科创50大跌4.30%。沪深两市成交额27927.61亿元，连续31个交易日超2.5万亿。全市场仅898只上涨，4591只下跌。银行、电力等高股息板块逆势抗跌。</p>"""

old_t7_2 = """<p style="margin-bottom:12px;padding:10px 12px;background:rgba(63,185,80,0.06);border-radius:8px;"><strong style="color:var(--green);font-size:13px;letter-spacing:0.5px;">🌍 全球股市震荡回升，科技股企稳</strong><br>美股隔夜（6月9日）企稳反弹，道指涨0.54%、标普500涨0.79%、纳指涨0.93%，英伟达反弹3.76%，费城半导体指数反弹2.85%。亚太市场普遍反弹，韩国KOSPI涨2.68%收复部分失地，日经225涨1.30%，香港恒生指数涨0.85%。</p>"""
new_t7_2 = """<p style="margin-bottom:12px;padding:10px 12px;background:rgba(63,185,80,0.06);border-radius:8px;"><strong style="color:var(--green);font-size:13px;letter-spacing:0.5px;">🌍 全球风险资产集中抛售，科技股重挫</strong><br>美股隔夜（6月9日）全线重挫，道指跌1.35%、标普500跌2.64%、纳指跌4.18%，英伟达跌6.20%，费城半导体指数大跌超10%。亚太市场全线暴跌，韩国KOSPI跌8.29%触发熔断，日经225跌3.85%，香港恒生指数跌1.22%。</p>"""

old_t7_3 = """<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">🏦 商品与汇率分化</strong><br>黄金企稳回升至4318美元（+0.77%），以伊冲突缓和推动油价回落，WTI原油跌1.41%至89.25美元。人民币汇率保持稳定，USD/CNY中间价6.8215。比特币箱体震荡于65000美元附近，加密市场情绪中性偏乐观。</p>"""
new_t7_3 = """<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">🏦 商品与汇率调整</strong><br>黄金承压回落至4285美元（-1.34%），以伊冲突升级推升油价一度冲高后回落，WTI原油约90.53美元、布伦特约93.72美元。人民币汇率保持稳定，USD/CNY中间价6.8198。比特币承压于62956美元附近，加密市场避险情绪升温。</p>"""

# ============ 23. Tab 7 南向资金 ============
old_t7_nx = """<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">💰 南向资金加仓港股核心资产</strong><br>南向资金净买入96.85亿港元，重点配置互联网龙头和高股息蓝筹股。港股估值处于历史低位，南下资金持续抄底港股核心资产。</p>"""
new_t7_nx = """<p style="margin-bottom:0;padding:10px 12px;background:rgba(240,180,41,0.06);border-radius:8px;"><strong style="color:#f0b429;font-size:13px;letter-spacing:0.5px;">💰 南向资金逆势加仓港股</strong><br>南向资金净买入113.18亿港元，重点配置互联网龙头和高股息蓝筹股。港股估值处于历史低位，南下资金持续抄底港股核心资产。</p>"""

# ============ 24. Tab 7 黄金数据 $4318 -> $4285 ============
old_gold1 = """<div style="font-size:22px;font-weight:800;color:#f85149;">$4318</div>"""
new_gold1 = """<div style="font-size:22px;font-weight:800;color:#3fb950;">$4285</div>"""

old_gold2 = """国际金价企稳回升至<span style="color:#00d4ff;font-weight:700;">4318美元</span>（+0.77%），以伊冲突虽有缓和但不确定性仍存。<span style="color:#f85149;font-weight:700;">中国央行连续20个月增持黄金储备</span>，黄金战略配置价值凸显。</p>"""
new_gold2 = """国际金价承压回落至<span style="color:#00d4ff;font-weight:700;">4285美元</span>（-1.34%），以伊冲突升级叠加非农数据超预期推升加息预期。<span style="color:#f85149;font-weight:700;">中国央行连续20个月增持黄金储备</span>，黄金战略配置价值凸显。</p>"""

# ============ 25. Tab 7 操作建议日期 ============
old_adv = """<span style="font-size:11px;color:var(--text-muted);font-weight:400;">基于2026年6月10日市场环境</span>"""
new_adv = """<span style="font-size:11px;color:var(--text-muted);font-weight:400;">基于2026年6月9日市场环境</span>"""

# ============ 26. 关键数字速查 valuation-cards ============
old_v1 = """<div class="valuation-value" style="color:#f85149;">3987.26</div>
          </div>
          <div class="valuation-tag good">+0.71%</div>"""
new_v1 = """<div class="valuation-value" style="color:#3fb950;">3959.34</div>
          </div>
          <div class="valuation-tag warn">-1.70%</div>"""

old_v2 = """<div class="valuation-value" style="color:#f0b429;">28562亿</div>
          </div>
          <div class="valuation-tag mid">连续33日超2.5万亿</div>"""
new_v2 = """<div class="valuation-value" style="color:#f0b429;">27927亿</div>
          </div>
          <div class="valuation-tag mid">连续31日超2.5万亿</div>"""

old_v3 = """<div class="valuation-value" style="color:#bc8cff;">$65280</div>
          </div>
          <div class="valuation-tag mid">箱体整理</div>"""
new_v3 = """<div class="valuation-value" style="color:#3fb950;">$62956</div>
          </div>
          <div class="valuation-tag warn">避险调整</div>"""

old_v4 = """<div class="valuation-value" style="color:#f85149;">$4318</div>
          </div>
          <div class="valuation-tag good">+0.77%</div>"""
new_v4 = """<div class="valuation-value" style="color:#3fb950;">$4285</div>
          </div>
          <div class="valuation-tag warn">-1.34%</div>"""

old_v5 = """<div class="valuation-value" style="color:#f85149;">$4318/oz</div>
          </div>
          <div class="valuation-tag good">+0.77%</div>"""
new_v5 = """<div class="valuation-value" style="color:#3fb950;">$4285/oz</div>
          </div>
          <div class="valuation-tag warn">-1.34%</div>"""

old_v6 = """<div class="valuation-value" style="color:#f85149;">25128</div>
          </div>
          <div class="valuation-tag good">+0.85%</div>"""
new_v6 = """<div class="valuation-value" style="color:#3fb950;">24657</div>
          </div>
          <div class="valuation-tag warn">-1.22%</div>"""

old_v7 = """<div class="valuation-value" style="color:#f85149;">25949</div>
          </div>
          <div class="valuation-tag good">+0.93%</div>"""
new_v7 = """<div class="valuation-value" style="color:#3fb950;">25709</div>
          </div>
          <div class="valuation-tag warn">-4.18%</div>"""

# ============ 27. Tab 7 alert bar ============
old_alert = """<strong>✅ 正面因素：</strong>6月10日周三，A股结构性反弹，银行、保险、电力等高股息板块强势领涨，北向资金连续9日净买入，长线资金持续加码低估值价值股。央行续作5000亿MLF，维护流动性充裕。"""
new_alert = """<strong>✅ 正面因素：</strong>6月9日周二，A股全线调整，银行、保险、电力等高股息板块逆势抗跌，北向资金连续8日净买入逆势加仓低估值价值股。央行2185亿逆回购净投放2075亿，维护流动性充裕。"""

# ============ 28. 关键词标签 ============
old_kw = """    <div style="display:flex;flex-wrap:wrap;gap:8px;">
      <span style="background:rgba(248,81,73,0.15);color:#f85149;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">以伊缓和</span>
      <span style="background:rgba(240,180,41,0.15);color:#f0b429;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">超级央行周</span>
      <span style="background:rgba(29,198,100,0.15);color:#3fb950;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">A股结构性反弹</span>
      <span style="background:rgba(0,212,255,0.15);color:#00d4ff;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">银行高股息领涨</span>
      <span style="background:rgba(188,140,255,0.15);color:#bc8cff;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">科技股企稳</span>
      <span style="background:rgba(255,166,87,0.15);color:#ffa657;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">央行续作MLF</span>
      <span style="background:rgba(63,185,80,0.15);color:#3fb950;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">北向9日净买</span>
      <span style="background:rgba(248,81,73,0.15);color:#f85149;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">美股震荡回升</span>
    </div>"""
new_kw = """    <div style="display:flex;flex-wrap:wrap;gap:8px;">
      <span style="background:rgba(248,81,73,0.15);color:#f85149;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">以伊冲突升级</span>
      <span style="background:rgba(240,180,41,0.15);color:#f0b429;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">韩国KOSPI熔断</span>
      <span style="background:rgba(29,198,100,0.15);color:#3fb950;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">A股全线调整</span>
      <span style="background:rgba(0,212,255,0.15);color:#00d4ff;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">银行高股息抗跌</span>
      <span style="background:rgba(188,140,255,0.15);color:#bc8cff;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">科技股重挫</span>
      <span style="background:rgba(255,166,87,0.15);color:#ffa657;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">央行逆回购</span>
      <span style="background:rgba(63,185,80,0.15);color:#3fb950;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">北向8日净买</span>
      <span style="background:rgba(248,81,73,0.15);color:#f85149;padding:6px 12px;border-radius:20px;font-size:13px;font-weight:600;">美股全线重挫</span>
    </div>"""

# ============ 执行替换 ============
replacements = [
    (old_news1, new_news1, "新闻卡片1: A股结构性行情"),
    (old_news2, new_news2, "新闻卡片2: 美股震荡反弹"),
    (old_news3, new_news3, "新闻卡片3: 北向资金"),
    (old_news4, new_news4, "新闻卡片4: 截至6月10日北向资金"),
    (old_news5, new_news5, "新闻卡片5: 黄金高位震荡"),
    (old_sz, new_sz, "综评标题日期"),
    (old_emo1, new_emo1, "情绪指示器: 涨跌比"),
    (old_emo2, new_emo2, "情绪指示器: 成交额"),
    (old_emo3, new_emo3, "情绪指示器: 北向资金"),
    (old_ci, new_ci, "机构报告: 中信证券"),
    (old_gs, new_gs, "机构报告: 高盛"),
    (old_xy, new_xy, "机构报告: 兴业证券"),
    (old_zj, new_zj, "机构报告: 中金公司"),
    (old_ms, new_ms, "机构报告: 摩根士丹利"),
    (old_ub, new_ub, "机构报告: 瑞银集团"),
    (old_hd1, new_hd1, "Tab5 价值投资: 银行板块"),
    (old_title, new_title, "Tab5 关注标的标题"),
    (old_bk1, new_bk1, "Tab5 银行板块文本"),
    (old_gy, new_gy, "Tab5 公用事业板块"),
    (old_dl, new_dl, "Tab5 电力板块"),
    (old_yq, new_yq, "Tab5 央企高股息"),
    (old_cap, new_cap, "Tab5 资金流入描述"),
    (old_ref, new_ref, "Tab5 reference-desc"),
    (old_t7_1, new_t7_1, "Tab7 今日总结: A股"),
    (old_t7_2, new_t7_2, "Tab7 今日总结: 全球股市"),
    (old_t7_3, new_t7_3, "Tab7 今日总结: 商品与汇率"),
    (old_t7_nx, new_t7_nx, "Tab7 今日总结: 南向资金"),
    (old_gold1, new_gold1, "Tab7 黄金价格 $4318"),
    (old_gold2, new_gold2, "Tab7 黄金描述"),
    (old_adv, new_adv, "Tab7 操作建议日期"),
    (old_v1, new_v1, "估值卡片: 上证指数"),
    (old_v2, new_v2, "估值卡片: 成交额"),
    (old_v3, new_v3, "估值卡片: BTC"),
    (old_v4, new_v4, "估值卡片: 黄金"),
    (old_v5, new_v5, "估值卡片: 黄金/oz"),
    (old_v6, new_v6, "估值卡片: 恒生指数"),
    (old_v7, new_v7, "估值卡片: 纳斯达克"),
    (old_alert, new_alert, "Tab7 alert bar"),
    (old_kw, new_kw, "Tab7 关键词标签"),
]

for old, new, name in replacements:
    if old in html:
        html = html.replace(old, new)
        changes.append(f"✓ {name}")
    else:
        print(f"✗ {name} NOT FOUND")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

for c in changes:
    print(c)
print(f"\n总计成功: {len(changes)}/{len(replacements)}")
