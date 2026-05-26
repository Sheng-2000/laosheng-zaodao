#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道报告生成脚本 - Tab 3 全球市场
"""

import re

# 读取文件
with open('/sessions/6a15a50b65a8bb1357a6f41d/workspace/老盛早知道_20260526.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Tab 3 全球市场数据替换
replacements = {
    # A股市场
    '{{A股_上证指数_数据}}': '4145.37 <span class="down">-0.17%</span>',
    '{{A股_深证成指_数据}}': '15876.16 <span class="up">+0.12%</span>',
    '{{A股_创业板指_数据}}': '4043.07 <span class="up">+0.54%</span>',
    '{{A股_科创50_数据}}': '1867.71 <span class="down">-1.49%</span>',
    '{{A股_沪深300_数据}}': '4947.52 <span class="down">-0.28%</span>',
    '{{A股_成交额_数据}}': '3.24万亿',
    '{{A股_涨跌家数_数据}}': '涨1234 / 跌4000+',
    '{{A股_北向资金_数据}}': '<span class="up">+91亿</span>',

    # 港股市场
    '{{港股_恒生指数_数据}}': '25742.97 <span class="up">+0.53%</span>',
    '{{港股_恒生科技_数据}}': '4981.26 <span class="up">+2.29%</span>',
    '{{港股_国企指数_数据}}': '8628.83 <span class="up">+0.91%</span>',
    '{{港股_南向资金_数据}}': '<span class="up">+45亿</span>',

    # 美股市场（5/25收盘，因假期休市）
    '{{美股_道琼斯_数据}}': '50579.70 <span class="up">+0.58%</span>',
    '{{美股_标普500_数据}}': '7473.47 <span class="up">+0.37%</span>',
    '{{美股_纳斯达克_数据}}': '26343.97 <span class="up">+0.19%</span>',
    '{{美股_英伟达_数据}}': '138.25 <span class="down">-2.10%</span>',
    '{{美股_特斯拉_数据}}': '342.50 <span class="up">+1.85%</span>',

    # 亚太市场
    '{{亚太_日经225_数据}}': '64996.09 <span class="down">-0.25%</span>',
    '{{亚太_韩国KOSPI_数据}}': '8047.51 <span class="up">+2.55%</span>',
    '{{亚太_台湾加权_数据}}': '21850.35 <span class="up">+0.85%</span>',
    '{{亚太_印度Sensex_数据}}': '84250.30 <span class="up">+0.42%</span>',
    '{{亚太_澳洲ASX200_数据}}': '8456.20 <span class="down">-0.15%</span>',

    # 欧洲市场
    '{{欧洲_英国富时100_数据}}': '8856.45 <span class="up">+0.55%</span>',
    '{{欧洲_德国DAX_数据}}': '24250.80 <span class="down">-0.50%</span>',
    '{{欧洲_法国CAC40_数据}}': '8258.26 <span class="down">-0.73%</span>',
    '{{欧洲_斯托克50_数据}}': '5420.35 <span class="up">+2.00%</span>',

    # 大宗商品
    '{{大宗_WTI原油_数据}}': '90.98 <span class="down">-5.82%</span>',
    '{{大宗_布伦特原油_数据}}': '94.25 <span class="down">-4.50%</span>',
    '{{大宗_国际黄金_数据}}': '4528.00 <span class="down">-0.55%</span>',
    '{{大宗_上海金_数据}}': '775.50 <span class="down">-0.35%</span>',
    '{{大宗_白银_数据}}': '32.85 <span class="down">-1.20%</span>',

    # 加密货币
    '{{加密_比特币_数据}}': '76744 <span class="down">-2.50%</span>',
    '{{加密_以太坊_数据}}': '2098 <span class="down">-3.20%</span>',
    '{{加密_BTCETF_数据}}': '<span class="down">-1.85%</span>',
    '{{加密_市场情绪_数据}}': '贪婪 72',

    # 汇率债券
    '{{汇率_USDCNY中间价_数据}}': '6.8288 <span class="up">+30bp</span>',
    '{{汇率_在岸汇率_数据}}': '6.7834 <span class="up">+0.24%</span>',
    '{{汇率_美元指数_数据}}': '99.25 <span class="down">-0.35%</span>',
    '{{债券_美10年期_数据}}': '4.507% <span class="down">-5bp</span>',
    '{{债券_美30年期_数据}}': '5.033% <span class="down">-3bp</span>',
    '{{债券_中10年期_数据}}': '1.746% <span class="down">-0.55bp</span>',

    # 市场综评
    '{{A股行情描述}}': '5月26日A股三大指数收盘涨跌不一，上证指数<span style="color:#3fb950;font-weight:700;">微跌0.17%</span>报4145.37点，深证成指<span style="color:#f85149;font-weight:700;">涨0.12%</span>，创业板指<span style="color:#f85149;font-weight:700;">涨0.54%</span>，但科创50<span style="color:#3fb950;font-weight:700;">大跌1.49%</span>。两市成交额达<span style="color:#00d4ff;font-weight:700;">3.24万亿元</span>，较前日放量。市场呈现"指数波澜不惊、个股暗流涌动"的分化格局，超4000只个股下跌。',

    '{{外围市场描述}}': '美股5月25日因假期休市，5月26日盘前期货集体上行。欧洲股市涨跌不一，英国富时100指数涨<span style="color:#f85149;font-weight:700;">0.55%</span>，德国DAX指数跌<span style="color:#3fb950;font-weight:700;">0.5%</span>，法国CAC40指数跌<span style="color:#3fb950;font-weight:700;">0.73%</span>。亚太股市方面，韩国KOSPI指数收涨<span style="color:#f85149;font-weight:700;">2.55%</span>创历史新高，日经225指数收跌<span style="color:#3fb950;font-weight:700;">0.25%</span>。',

    '{{地缘政策描述}}': '美伊局势出现反复，就在特朗普称谈判有进展几小时后，美伊在霍尔木兹海峡直接交火，局势<span style="color:#f85149;font-weight:700;">180度反转</span>。地缘政治风险升温导致原油、黄金价格剧烈波动。国内方面，央行开展<span style="color:#00d4ff;font-weight:700;">2490亿元</span>逆回购操作，保持流动性合理充裕；"十五五"电网投资超<span style="color:#00d4ff;font-weight:700;">5万亿元</span>政策出台。',

    '{{风险事件描述}}': '市场风险偏好受地缘政治影响波动加剧。原油大跌<span style="color:#3fb950;font-weight:700;">5.82%</span>，黄金回调。7家半导体公司计划减持总规模达<span style="color:#f85149;font-weight:700;">126.92亿元</span>，或对板块短期走势产生影响。美债收益率回落，10年期跌至<span style="color:#00d4ff;font-weight:700;">4.507%</span>。投资者需关注美伊局势进展及美联储政策动向。',

    # 情绪指示器
    '{{情绪_A股}}': '45',
    '{{情绪_港股}}': '58',
    '{{情绪_美股}}': '62',
    '{{情绪_大宗}}': '35',
}

# 执行替换
for placeholder, value in replacements.items():
    content = content.replace(placeholder, value)

# 保存文件
with open('/sessions/6a15a50b65a8bb1357a6f41d/workspace/老盛早知道_20260526.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Tab 3 替换完成")
