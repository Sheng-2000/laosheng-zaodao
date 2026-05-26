#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道报告生成脚本 - Tab 1 国内外新闻
"""

import re

# 读取文件
with open('/sessions/6a15a50b65a8bb1357a6f41d/workspace/老盛早知道_20260526.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Tab 1 新闻替换
replacements = {
    # 重点新闻1 - 央行操作
    '{{重点新闻1_标签和标题}}': '<span class="tag tag-policy">政策</span>央行开展2490亿元逆回购操作，保持流动性合理充裕',
    '{{重点新闻1_正文}}': '5月26日，中国人民银行以固定利率、数量招标方式开展了<span style="color:#00d4ff;font-weight:700;">2490亿元</span>7天期逆回购操作，全额满足了一级交易商需求。昨日央行开展<span style="color:#00d4ff;font-weight:700;">6000亿元</span>MLF操作，实现净投放<span style="color:#f85149;font-weight:700;">3570亿元</span>，保持银行体系流动性合理充裕。市场分析人士认为，央行近期持续加大流动性投放力度，体现了货币政策的前瞻性和灵活性，有助于稳定市场预期，支持实体经济融资需求。',

    # 重点新闻2 - 十五五电网投资
    '{{重点新闻2_标签和标题}}': '<span class="tag tag-policy">政策</span>十五五电网投资超5万亿，重点投向绿电直连、储能、特高压',
    '{{重点新闻2_正文}}': '发改委明确2026—2030年新型电网投资超<span style="color:#00d4ff;font-weight:700;">5万亿元</span>，重点投向绿电直连、储能、特高压等领域。这是继"十四五"后，国家再次加码电网基础设施建设，将有力推动能源结构转型和新能源产业发展。相关产业链上市公司有望持续受益，特别是特高压设备、储能系统、智能电网等领域龙头企业。',

    # 重点新闻3 - 数智供应链
    '{{重点新闻3_标签和标题}}': '<span class="tag tag-policy">政策</span>八部门发文推进数智供应链，培育100家领军企业',
    '{{重点新闻3_正文}}': '商务部等八部门发文，到2030年培育<span style="color:#00d4ff;font-weight:700;">100家</span>数智供应链领军企业，降低物流成本、推进智能仓储。政策将推动供应链数字化转型，提升产业链协同效率，对物流、仓储、供应链管理软件等相关板块形成利好。',

    # 重点新闻4 - 跨境资金监管
    '{{重点新闻4_标签和标题}}': '<span class="tag tag-policy">监管</span>跨境资金监管升级，严控非法资金外流',
    '{{重点新闻4_正文}}': '多部门联合整治跨境证券活动，严控非法资金外流，引导增量资金入A股核心资产。此举有助于规范资本市场秩序，防范金融风险，同时引导长期资金入市，对A股核心资产形成支撑。',

    # 重点新闻5 - 高铁票价调整
    '{{重点新闻5_标签和标题}}': '<span class="tag tag-geo">民生</span>京沪高铁票价优化，最高上浮20%',
    '{{重点新闻5_正文}}': '5月26日起，京沪、合蚌高铁执行票价优化，最高上浮<span style="color:#f85149;font-weight:700;">20%</span>，市场化定价深化。这是铁路客运价格改革的又一重要举措，有助于提升铁路运营效率和服务质量，相关铁路运营企业有望受益。',

    # 重点新闻6 - 常住地公共服务新政
    '{{重点新闻6_标签和标题}}': '<span class="tag tag-policy">政策</span>常住地公共服务新政发布，户籍壁垒破冰',
    '{{重点新闻6_正文}}': '国务院政策例行吹风会正式解读《关于推行常住地提供基本公共服务的实施意见》，教育、住房、社保、医疗等公共服务将打破户籍限制。这一政策将促进人口流动和城镇化进程，对房地产、教育、医疗等相关板块形成长期利好。',

    # 国际新闻1 - 美伊局势
    '{{国际新闻1_标签和标题}}': '<span class="tag tag-geo">地缘</span>美伊在霍尔木兹海峡直接交火，局势180度反转',
    '{{国际新闻1_正文}}': '就在特朗普称谈判有进展几小时后，美伊在霍尔木兹海峡直接交火，局势<span style="color:#f85149;font-weight:700;">180度反转</span>。地缘政治风险升温导致原油、黄金价格剧烈波动，WTI原油一度大跌<span style="color:#3fb950;font-weight:700;">5.82%</span>至90.98美元/桶，国际黄金现价约<span style="color:#00d4ff;font-weight:700;">4528美元</span>。市场需密切关注局势发展对全球能源和金融市场的影响。',

    # 国际新闻2 - 欧洲股市
    '{{国际新闻2_标签和标题}}': '<span class="tag tag-finance">市场</span>欧洲股市多数下跌，英国富时100逆势上涨',
    '{{国际新闻2_正文}}': '北京时间5月26日，欧洲主要股指多数下跌，英国富时100指数涨<span style="color:#f85149;font-weight:700;">0.55%</span>，法国CAC40指数跌<span style="color:#3fb950;font-weight:700;">0.73%</span>，德国DAX指数跌<span style="color:#3fb950;font-weight:700;">0.5%</span>。欧洲斯托克50指数抹去自伊朗战争爆发以来的所有跌幅，收盘涨<span style="color:#f85149;font-weight:700;">2%</span>。',

    # 国际新闻3 - 美债收益率
    '{{国际新闻3_标签和标题}}': '<span class="tag tag-finance">债市</span>美债收益率全线回落，10年期跌至4.507%',
    '{{国际新闻3_正文}}': '受美伊谈判进展提振风险偏好，美债收益率全线回落。10年期美债收益率下跌近<span style="color:#3fb950;font-weight:700;">5个基点</span>至<span style="color:#00d4ff;font-weight:700;">4.507%</span>，30年期美债收益率下跌约3个基点至<span style="color:#00d4ff;font-weight:700;">5.033%</span>。作为全球资产定价之锚，美债收益率走势对全球资本市场具有重要影响。',

    # 国际新闻4 - 亚太股市
    '{{国际新闻4_标签和标题}}': '<span class="tag tag-finance">市场</span>韩国KOSPI创历史新高，日经225小幅收跌',
    '{{国际新闻4_正文}}': '5月26日，亚太股市涨跌不一。韩国KOSPI指数收涨<span style="color:#f85149;font-weight:700;">2.55%</span>报<span style="color:#00d4ff;font-weight:700;">8047.51点</span>，创收盘历史新高；日经225指数收跌<span style="color:#3fb950;font-weight:700;">0.25%</span>报64996.09点。韩国股市大涨主要受半导体板块带动，华虹半导体涨近<span style="color:#f85149;font-weight:700;">11%</span>，中芯国际涨超<span style="color:#f85149;font-weight:700;">8%</span>。',
}

# 执行替换
for placeholder, value in replacements.items():
    content = content.replace(placeholder, value)

# 保存文件
with open('/sessions/6a15a50b65a8bb1357a6f41d/workspace/老盛早知道_20260526.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Tab 1 替换完成")
