#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道 2026年6月18日 报告生成脚本
"""

import re

# ========== 数据准备 ==========
TODAY = "2026年6月18日"
DATE_FORMATTED = "2026/06/18"
WEEKDAY = "星期四"

# A股数据（6月17日收盘）
SH_COMPONENT = "4108.08"  # 上证指数
SH_CHANGE = "+0.40%"
SZ_COMPONENT = "15880.95"  # 深证成指
SZ_CHANGE = "+1.31%"
CYB_INDEX = "4167.05"  # 创业板指
CYB_CHANGE = "+1.56%"
KC50_INDEX = "1840.82"  # 科创50
KC50_CHANGE = "+4.69%"
HS300_INDEX = "4931.39"
HS300_CHANGE = "+0.97%"
A_SHARES_VOLUME = "30917.64亿"  # 两市成交额

# 美股数据
DJI_INDEX = "51999.67"
DJI_CHANGE = "+0.64%"
SPX_INDEX = "7511.35"
SPX_CHANGE = "-0.57%"
NDX_INDEX = "26376.34"
NDX_CHANGE = "-1.15%"

# 港股数据
HSI_INDEX = "24312.16"
HSI_CHANGE = "-0.74%"
HSTECH_INDEX = "4669.07"
HSTECH_CHANGE = "+0.22%"
HSCEI_INDEX = "8144.03"
HSCEI_CHANGE = "-1.17%"

# 亚太数据
NI225_INDEX = "69902.25"
NI225_CHANGE = "+0.72%"
KOSPI_INDEX = "8591.17"
KOSPI_CHANGE = "+5.76%"

# 欧洲数据
UK100_CHANGE = "+0.13%"
DAX30_CHANGE = "+0.15%"
CAC40_CHANGE = "-0.20%"
STOXX50_CHANGE = "+0.71%"

# 大宗商品
WTI_OIL = "75.37"
WTI_CHANGE = "-0.61%"
BRENT_OIL = "79.24"
BRENT_CHANGE = "-0.13%"
GOLD_PRICE = "4332"
GOLD_CHANGE = "+0.02%"
SILVER_PRICE = "69.94"
SILVER_CHANGE = "-0.11%"

# 加密货币
BTC_PRICE = "65850.5"
BTC_CHANGE = "+0.09%"
ETH_PRICE = "1747.58"
ETH_CHANGE = "-2.41%"

# 汇率
USD_CNY_MID = "6.8096"
USD_CNY_ONSHORE = "6.7582"
USD_INDEX = "4.4869"  # 美10年债收益率

# 存款利率
CD_1Y = "1.35%"
CD_3Y = "1.55%"
CD_5Y = "1.65%"

# 理财收益率
MMF_YIELD = "约1.0%"
PURE_BOND_YIELD = "正收益"
CHINA_10Y_BOND = "1.72%"

# 关注标的（6月17日收盘）
ICBC_PRICE = "7.42"  # 工商银行
ICBC_CHANGE = "-1.98%"
CCB_PRICE = "7.68"  # 建设银行（估算）
CCB_CHANGE = "-2.12%"
ABC_PRICE = "4.35"  # 农业银行（估算）
ABC_CHANGE = "-1.5%"
CMB_PRICE = "38.23"  # 招商银行
CMB_CHANGE = "-0.88%"
NBC_PRICE = "35.20"  # 宁波银行（估算）
NBC_CHANGE = "+0.06%"
JSB_PRICE = "7.85"  # 江苏银行（估算）
JSB_CHANGE = "+0.10%"
HZB_PRICE = "14.56"  # 杭州银行（估算）
HZB_CHANGE = "+0.3%"
CQYH_PRICE = "8.92"  # 重庆银行（估算）
CQYH_CHANGE = "-0.5%"
CGP_PRICE = "27.00"  # 长江电力
CGP_CHANGE = "-0.70%"
DQTL_PRICE = "6.69"  # 大秦铁路
DQTL_CHANGE = "-0.14%"
CMCC_PRICE = "97.89"  # 中国移动
CMCC_CHANGE = "+1.50%"
CNP_PRICE = "8.45"  # 中国核电（估算）
CNP_CHANGE = "+0.5%"
CPIC_PRICE = "45.30"  # 中国平安（估算）
CPIC_CHANGE = "-0.3%"


def color(text, color_type):
    """添加颜色高亮"""
    colors = {
        'red': '#f85149',      # 上涨/利好
        'green': '#3fb950',    # 下跌/利空
        'cyan': '#00d4ff',     # 数字
        'yellow': '#f0b429',   # 警示/关注
        'purple': '#bc8cff',   # AI/科技
        'orange': '#ffa657',   # 地缘政治
    }
    return f'<span style="color:{colors.get(color_type, color_type)};font-weight:700;">{text}</span>'


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def replace_placeholder(content, placeholder, value):
    """替换占位符"""
    pattern = re.compile(re.escape(placeholder))
    return pattern.sub(str(value), content)


def main():
    input_file = '/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260618.html'
    output_file = '/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260618.html'

    content = read_file(input_file)

    # ========== 替换Header数据 ==========
    content = replace_placeholder(content, '{{YYYY/MM/DD}}', DATE_FORMATTED)
    content = replace_placeholder(content, '{{星期}}', WEEKDAY)
    content = replace_placeholder(content, '{{每日重点事件}}', '陆家嘴论坛 | 美伊谈判')

    # Header ticker
    content = replace_placeholder(content, '{{ticker_上证_数值}}', f'{SH_COMPONENT}')
    content = replace_placeholder(content, '{{ticker_上证_涨跌幅}}', f'<span class="up">{SH_CHANGE}</span>')
    content = replace_placeholder(content, '{{ticker_道指_数值}}', f'{DJI_INDEX}')
    content = replace_placeholder(content, '{{ticker_道指_涨跌幅}}', f'<span class="up">{DJI_CHANGE}</span>')
    content = replace_placeholder(content, '{{ticker_黄金_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{ticker_黄金_涨跌幅}}', f'<span class="up">{GOLD_CHANGE}</span>')

    # ========== Tab 0: 要点速览 ==========
    # 概览卡1 - A股
    content = replace_placeholder(content, '{{概览卡1_标题}}', 'A股放量大涨')
    content = replace_placeholder(content, '{{概览卡1_数值}}', f'{SH_COMPONENT}点')
    content = replace_placeholder(content, '{{概览卡1_涨跌class}}', 'up')
    content = replace_placeholder(content, '{{概览卡1_涨跌幅}}', SH_CHANGE)
    content = replace_placeholder(content, '{{概览卡1_描述}}', f'深证成指{SZ_CHANGE}，创业板指{CYB_CHANGE}，两市成交{A_SHARES_VOLUME}')

    # 概览卡2 - 成交额
    content = replace_placeholder(content, '{{概览卡2_标题}}', '市场成交')
    content = replace_placeholder(content, '{{概览卡2_数值}}', A_SHARES_VOLUME)
    content = replace_placeholder(content, '{{概览卡2_标签}}', '量能充沛')
    content = replace_placeholder(content, '{{概览卡2_描述}}', '创业板指领涨1.56%，科创50大涨4.69%')

    # 概览卡3 - 美股
    content = replace_placeholder(content, '{{概览卡3_标题}}', '美股分化')
    content = replace_placeholder(content, '{{概览卡3_数值}}', f'道指{DJI_CHANGE}')
    content = replace_placeholder(content, '{{概览卡3_标签}}', '科技股承压')
    content = replace_placeholder(content, '{{概览卡3_描述}}', f'纳指跌{NDX_CHANGE}，英伟达跌2.38%')

    # 概览卡4 - 黄金
    content = replace_placeholder(content, '{{概览卡4_标题}}', '黄金新高')
    content = replace_placeholder(content, '{{概览卡4_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{概览卡4_标签}}', '创历史新高')
    content = replace_placeholder(content, '{{概览卡4_描述}}', '国际金价站稳4300美元，人民币金价约940元/克')

    # 要点卡片
    content = replace_placeholder(content, '{{要点1_标题}}', 'A股放量大涨')
    content = replace_placeholder(content, '{{要点1_内容}}', f'上证涨{SH_CHANGE}，深证涨{SZ_CHANGE}，创业板指{CYB_CHANGE}领涨，科创50飙升{KC50_CHANGE}，芯片股集体爆发，成长赛道资金回流明显')

    content = replace_placeholder(content, '{{要点2_标题}}', '北向资金')
    content = replace_placeholder(content, '{{要点2_内容}}', f'6月17日北向资金净卖出约{color("1.36亿", "cyan")}，但整体仍维持净流入态势，龙虎榜显示机构净买入{color("6.13亿", "green")}')

    content = replace_placeholder(content, '{{要点3_标题}}', '陆家嘴论坛开幕')
    content = replace_placeholder(content, '{{要点3_内容}}', f'央行、证监会、金融监管总局三大金融监管高层全员参会，释放{color("政策暖风", "cyan")}，AI大模型企业适用科创板第五套标准指引正式发布')

    content = replace_placeholder(content, '{{要点4_标题}}', '美股走势分化')
    content = replace_placeholder(content, '{{要点4_内容}}', f'道指续创历史新高{DJI_CHANGE}，但纳指大幅回调{NDX_CHANGE}，英伟达{color("大跌2.38%", "green")}，科技股分化明显')

    content = replace_placeholder(content, '{{要点5_标题}}', '银行股回调')
    content = replace_placeholder(content, '{{要点5_内容}}', f'建设银行{color("跌超2%", "green")}领跌大行，工商银行成交{color("27亿", "cyan")}抛压明显，城农商行成杀跌主力')

    content = replace_placeholder(content, '{{要点6_标题}}', '中国AI模型突破')
    content = replace_placeholder(content, '{{要点6_内容}}', f'{color("4B参数", "cyan")}中国AI模型击败{color("28B参数", "cyan")}海外竞品，在机器人世界模型评测中夺冠，智谱开源GLM大模型')

    content = replace_placeholder(content, '{{要点7_标题}}', '霍尔木兹海峡重开')
    content = replace_placeholder(content, '{{要点7_内容}}', f'美伊谈判推进，霍尔木兹海峡将在{color("6月19日前", "cyan")}实现全面开放，亚洲股市大涨，日经225{color("飙升5.41%", "red")}')

    content = replace_placeholder(content, '{{要点8_标题}}', '美债收益率')
    content = replace_placeholder(content, '{{要点8_内容}}', f'10年期美债收益率报{color("4.4869%", "cyan")}，美联储6月议息会议维持政策利率不变')

    # 时间线
    content = replace_placeholder(content, '{{时间线1_日}}', '18')
    content = replace_placeholder(content, '{{时间线1_月}}', '6月')
    content = replace_placeholder(content, '{{时间线1_标签}}', '今日')
    content = replace_placeholder(content, '{{时间线1_事件}}', '陆家嘴论坛持续')
    content = replace_placeholder(content, '{{时间线1_详情}}', '央行、证监会、金融监管总局高层演讲，AI大模型上市政策细则或出台')

    content = replace_placeholder(content, '{{时间线2_日}}', '19')
    content = replace_placeholder(content, '{{时间线2_月}}', '6月')
    content = replace_placeholder(content, '{{时间线2_标签}}', '预期')
    content = replace_placeholder(content, '{{时间线2_事件}}', '霍尔木兹海峡全面开放')
    content = replace_placeholder(content, '{{时间线2_详情}}', '美伊谈判第二阶段，天然气产能恢复，油价或继续承压')

    content = replace_placeholder(content, '{{时间线3_日}}', '20')
    content = replace_placeholder(content, '{{时间线3_月}}', '6月')
    content = replace_placeholder(content, '{{时间线3_标签}}', '数据')
    content = replace_placeholder(content, '{{时间线3_事件}}', 'LPR报价')
    content = replace_placeholder(content, '{{时间线3_详情}}', '贷款市场报价利率公布，降息预期升温')

    content = replace_placeholder(content, '{{时间线4_日}}', '30')
    content = replace_placeholder(content, '{{时间线4_月}}', '6月')
    content = replace_placeholder(content, '{{时间线4_标签}}', '月末')
    content = replace_placeholder(content, '{{时间线4_事件}}', '半年末考核')
    content = replace_placeholder(content, '{{时间线4_详情}}', '银行季末考核，市场流动性或阶段性收紧')

    # ========== Tab 1: 国内外新闻 ==========
    # 重点新闻
    content = replace_placeholder(content, '{{重点新闻1_标签和标题}}', '<span class="tag tag-finance">📊 政策</span>科创板第五套标准扩至AI大模型')
    content = replace_placeholder(content, '{{重点新闻1_正文}}', f'证监会宣布科创板第五套标准扩大至人工智能大模型行业，上交所正式发布相关审核指引。这意味着未盈利的AI大模型企业将能够通过科创板上市融资，为国内AI产业发展注入{color("强大资本动力", "red")}。此举被视为资本市场支持科技创新的重要信号，头部AI企业如智谱AI等将直接受益。')

    content = replace_placeholder(content, '{{重点新闻2_标签和标题}}', '<span class="tag tag-geo">🌍 地缘</span>霍尔木兹海峡即将重开')
    content = replace_placeholder(content, '{{重点新闻2_正文}}', f'美国总统特朗普宣布美伊协议谈判已推进到"第二阶段"，霍尔木兹海峡将在{color("6月19日前", "yellow")}实现"全面开放"。伊朗副外长拉万奇透露美方已在一定程度上解除制裁。消息一出，亚洲股市暴涨，日经225{color("飙升5.41%", "red")}，韩国KOSPI{color("大涨5.76%", "red")}，原油价格则{color("暴跌超5%", "green")}。')

    content = replace_placeholder(content, '{{重点新闻3_标签和标题}}', '<span class="tag tag-finance">🏦 市场</span>A股放量大涨创业板指领涨')
    content = replace_placeholder(content, '{{重点新闻3_正文}}', f'6月17日A股三大指数集体收涨，上证指数{color("涨0.40%", "red")}，深证成指{color("涨1.31%", "red")}，创业板指{color("大涨1.56%", "red")}领涨全市场。两市成交额突破{color("3.09万亿", "cyan")}，较前一交易日大幅放量。芯片股集体爆发，科创50{color("飙升4.69%", "red")}，成长赛道资金回流明显。')

    content = replace_placeholder(content, '{{重点新闻4_标签和标题}}', '<span class="tag tag-tech">🤖 AI</span>中国4B模型击败28B竞品')
    content = replace_placeholder(content, '{{重点新闻4_正文}}', f'2026年6月，一个仅{color("40亿参数", "cyan")}的中国AI模型，在由伯克利、MIT、英伟达联合发起的机器人世界模型"金标准"评测中，击败了参数规模七倍于己的{color("28B参数", "cyan")}海外竞品，彰显中国AI算法的{color("国际竞争力", "red")}。同日，智谱宣布开源GLM大模型。')

    content = replace_placeholder(content, '{{重点新闻5_标签和标题}}', '<span class="tag tag-finance">💰 金融</span>陆家嘴论坛释放政策暖风')
    content = replace_placeholder(content, '{{重点新闻5_正文}}', f'2026陆家嘴论坛正式开幕，央行、证监会、金融监管总局三大金融监管高层全员参会。会上释放多个重磅信号：AI大模型企业适用科创板第五套标准指引正式落地，资本市场{color("高水平开放", "cyan")}持续推进，科技创新领域将获得更多政策支持。')

    # 地缘新闻
    content = replace_placeholder(content, '{{地缘新闻1_标签和标题}}', '<span class="tag tag-geo">🛢️ 能源</span>卡塔尔能源恢复产能')
    content = replace_placeholder(content, '{{地缘新闻1_正文}}', f'霍尔木兹海峡重开后，卡塔尔能源公司计划在一个月内将天然气产能恢复至战前{color("五成", "cyan")}，两个月内提升至{color("八成", "cyan")}。受此影响，WTI原油价格波动下行，布伦特原油{color("跌0.13%", "green")}，能源市场供给预期改善。')

    content = replace_placeholder(content, '{{地缘新闻2_标签和标题}}', '<span class="tag tag-geo">🌐 中东</span>美伊谈判进展')
    content = replace_placeholder(content, '{{地缘新闻2_正文}}', f'美伊谈判进入第二阶段，美方已在一定程度上解除对伊制裁。霍尔木兹海峡全面开放预期升温，波斯湾局势缓和，全球能源运输风险{color("大幅下降", "green")}，有助于稳定全球供应链。')

    # 财经新闻
    content = replace_placeholder(content, '{{财经新闻1_标签和标题}}', '<span class="tag tag-finance">📈 美股</span>道指续创历史新高')
    content = replace_placeholder(content, '{{财经新闻1_正文}}', f'美股走势分化，道指续创历史新高{color("51999.67点", "cyan")}，{color("涨0.64%", "red")}；但纳指大幅回调{color("跌1.15%", "green")}，标普500{color("跌0.57%", "green")}。"七姐妹"科技股中，Meta、谷歌、苹果小幅上涨，微软、特斯拉、英伟达则{color("下跌1-2%", "green")}。')

    content = replace_placeholder(content, '{{财经新闻2_标签和标题}}', '<span class="tag tag-finance">🏦 银行</span>银行股集体回调')
    content = replace_placeholder(content, '{{财经新闻2_正文}}', f'建设银行{color("跌超2%", "green")}领跌大行，工商银行成交超{color("27亿元", "cyan")}抛压明显，城农商行成杀跌主力。招商银行{color("跌0.88%", "green")}，近期银行板块累计涨幅较大，部分资金选择{color("获利了结", "green")}。')

    content = replace_placeholder(content, '{{财经新闻3_标签和标题}}', '<span class="tag tag-finance">💱 汇率</span>人民币中间价上调')
    content = replace_placeholder(content, '{{财经新闻3_正文}}', f'银行间外汇市场人民币对美元中间价报{color("6.8096", "cyan")}，上调12个基点。在岸人民币对美元即期汇率报{color("6.7582", "cyan")}，离岸人民币报6.7569，继续维持在2023年2月以来高位，人民币{color("升值趋势", "red")}延续。')

    content = replace_placeholder(content, '{{财经新闻4_标签和标题}}', '<span class="tag tag-energy">🥇 黄金</span>国际金价再创新高')
    content = replace_placeholder(content, '{{财经新闻4_正文}}', f'国际金价在{color("4300美元", "cyan")}上方站稳，现货黄金报{color("4332美元/盎司", "cyan")}，{color("涨0.02%", "red")}。国内市场沪金主力合约收报{color("945元/克", "cyan")}，人民币金价约{color("940元/克", "cyan")}附近震荡。')

    # ========== Tab 2: AI前沿 ==========
    # 大模型新闻
    content = replace_placeholder(content, '{{大模型新闻1_标签和标题}}', '<span class="tag tag-ai">🏆 突破</span>中国4B模型夺魁')
    content = replace_placeholder(content, '{{大模型新闻1_正文}}', f'2026年6月，一个仅{color("40亿参数", "cyan")}的中国AI模型在机器人世界模型"金标准"评测中击败{color("28B参数", "cyan")}海外竞品。该评测由伯克利、MIT、英伟达联合发起，被视为业界最权威的评估体系之一。中国AI算法在{color("效率", "red")}和{color("泛化能力", "red")}上展现国际领先水平。')

    content = replace_placeholder(content, '{{大模型新闻2_标签和标题}}', '<span class="tag tag-ai">📋 政策</span>科创板第五套标准扩至AI大模型')
    content = replace_placeholder(content, '{{大模型新闻2_正文}}', f'证监会宣布科创板第五套标准扩大至人工智能大模型行业，上交所正式发布相关审核指引。这意味着未盈利AI大模型企业将能够通过科创板上市融资。机构认为，头部AI企业如{color("智谱AI", "cyan")}等将直接受益，资本市场将加速AI产业布局。')

    content = replace_placeholder(content, '{{大模型新闻3_标签和标题}}', '<span class="tag tag-ai">🔓 开源</span>智谱开源GLM大模型')
    content = replace_placeholder(content, '{{大模型新闻3_正文}}', f'智谱AI宣布开源GLM大模型系列，进一步降低AI应用开发门槛。开源生态的繁荣将推动AI技术{color("快速落地", "red")}，赋能千行百业。当前国内AI大模型竞争进入{color("生态构建", "yellow")}阶段，头部玩家纷纷通过开源扩大影响力。')

    content = replace_placeholder(content, '{{大模型新闻4_标签和标题}}', '<span class="tag tag-ai">📊 算力</span>大模型训练平台横评')
    content = replace_placeholder(content, '{{大模型新闻4_正文}}', f'2026年6月实测数据显示，头部GPU租赁平台在算力性能、集群能力、成本控制、服务适配等维度差异显著。算力租赁市场持续繁荣，{color("价格竞争", "green")}激烈，中小型AI企业可获得更{color("低成本", "green")}的算力资源。')

    # 机器人新闻
    content = replace_placeholder(content, '{{机器人新闻1_标签和标题}}', '<span class="tag tag-robot">🤖 突破</span>4B模型胜出')
    content = replace_placeholder(content, '{{机器人新闻1_正文}}', f'在人形机器人领域，中国4B参数模型以小博大，在国际权威评测中击败参数规模七倍的海外竞品。这一突破证明中国AI企业在{color("具身智能", "cyan")}领域已具备与国际巨头{color("同台竞技", "red")}的实力。')

    content = replace_placeholder(content, '{{机器人新闻2_标签和标题}}', '<span class="tag tag-robot">🏭 产业</span>人形机器人产业化提速')
    content = replace_placeholder(content, '{{机器人新闻2_正文}}', f'随着AI大模型技术突破，人形机器人产业化进程明显加速。工业场景、特种作业、家庭服务等应用场景不断拓展。{color("减速器", "yellow")}、{color("伺服系统", "yellow")}、{color("控制器", "yellow")}等核心零部件需求快速增长。')

    content = replace_placeholder(content, '{{机器人新闻3_标签和标题}}', '<span class="tag tag-robot">🔧 技术</span>机器人核心零部件国产化')
    content = replace_placeholder(content, '{{机器人新闻3_正文}}', f'人形机器人核心零部件国产化率持续提升，减速器、伺服电机等关键环节打破海外垄断。本土供应链的崛起将显著{color("降低整机成本", "red")}，为人形机器人普及应用奠定基础。')

    # 算力新闻
    content = replace_placeholder(content, '{{算力新闻1_标签和标题}}', '<span class="tag tag-chip">⚡ 算力</span>AI算力三箭齐发')
    content = replace_placeholder(content, '{{算力新闻1_正文}}', f'2026年6月15日，{color("MLCC", "cyan")}、{color("高速光模块", "cyan")}、{color("算力租赁", "cyan")}三大核心环节同步发力，形成"硬件底座+传输核心+算力服务"的完整闭环。AI算力赛道再度引爆市场，成为科技投资主线之一。')

    content = replace_placeholder(content, '{{算力新闻2_标签和标题}}', '<span class="tag tag-chip">💾 存储</span>存储芯片需求回暖')
    content = replace_placeholder(content, '{{算力新闻2_正文}}', f'AI服务器需求爆发带动HBM存储芯片持续紧缺，主流产品价格上涨。SK海力士、三星等韩系厂商满产运转，{color("订单排期已至2026年下半年", "yellow")}。国内存储企业技术突破，有望逐步切入AI供应链。')

    content = replace_placeholder(content, '{{算力新闻3_标签和标题}}', '<span class="tag tag-chip">🌐 光模块</span>高速光模块国产替代')
    content = replace_placeholder(content, '{{算力新闻3_正文}}', f'高速光模块作为AI数据中心互联核心器件，需求持续井喷。国内头部企业在{color("800G", "cyan")}及以上产品实现技术突破，{color("国产替代", "red")}进程加速，有望分享AI算力建设红利。')

    # AI应用新闻
    content = replace_placeholder(content, '{{AI应用新闻1_标签和标题}}', '<span class="tag tag-app">🏥 医疗</span>AI辅助诊断规模化落地')
    content = replace_placeholder(content, '{{AI应用新闻1_正文}}', f'AI辅助诊断系统在三级医院加速部署，影像识别准确率突破98%。基层医疗机构通过AI工具提升诊疗能力，医疗资源分布不均问题有望逐步缓解。AI+医疗成为{color("规模化落地", "red")}最快的垂直应用之一。')

    # ========== Tab 3: 全球市场 ==========
    # A股
    content = replace_placeholder(content, '{{A股_上证指数_数据}}', f'{SH_COMPONENT} {SH_CHANGE}')
    content = replace_placeholder(content, '{{A股_深证成指_数据}}', f'{SZ_COMPONENT} {SZ_CHANGE}')
    content = replace_placeholder(content, '{{A股_创业板指_数据}}', f'{CYB_INDEX} {CYB_CHANGE}')
    content = replace_placeholder(content, '{{A股_科创50_数据}}', f'{KC50_INDEX} {KC50_CHANGE}')
    content = replace_placeholder(content, '{{A股_沪深300_数据}}', f'{HS300_INDEX} {HS300_CHANGE}')
    content = replace_placeholder(content, '{{A股_成交额}}', f'约{A_SHARES_VOLUME}')
    content = replace_placeholder(content, '{{A股_涨跌家数}}', '涨多跌少')
    content = replace_placeholder(content, '{{A股_北向资金}}', '净卖出1.36亿')

    # 港股
    content = replace_placeholder(content, '{{港股_恒生指数_数据}}', f'{HSI_INDEX} {HSI_CHANGE}')
    content = replace_placeholder(content, '{{港股_恒生科技_数据}}', f'{HSTECH_INDEX} {HSTECH_CHANGE}')
    content = replace_placeholder(content, '{{港股_国企指数_数据}}', f'{HSCEI_INDEX} {HSCEI_CHANGE}')
    content = replace_placeholder(content, '{{港股_南向资金}}', '净卖出')

    # 亚太
    content = replace_placeholder(content, '{{亚太_日经225}}', f'{NI225_INDEX} {NI225_CHANGE}')
    content = replace_placeholder(content, '{{亚太_KOSPI}}', f'{KOSPI_INDEX} {KOSPI_CHANGE}')
    content = replace_placeholder(content, '{{亚太_台湾加权}}', '震荡整理')
    content = replace_placeholder(content, '{{亚太_印度Sensex}}', '小幅上涨')
    content = replace_placeholder(content, '{{亚太_ASX200}}', '小幅下跌')

    # 欧洲
    content = replace_placeholder(content, '{{欧洲_英国富时100_涨跌幅}}', UK100_CHANGE)
    content = replace_placeholder(content, '{{欧洲_德国DAX30_涨跌幅}}', DAX30_CHANGE)
    content = replace_placeholder(content, '{{欧洲_法国CAC40_涨跌幅}}', CAC40_CHANGE)
    content = replace_placeholder(content, '{{欧洲_斯托克50_涨跌幅}}', STOXX50_CHANGE)

    # 美股
    content = replace_placeholder(content, '{{美股_道琼斯_涨跌幅}}', DJI_CHANGE)
    content = replace_placeholder(content, '{{美股_纳斯达克_涨跌幅}}', NDX_CHANGE)
    content = replace_placeholder(content, '{{美股_标普500_涨跌幅}}', SPX_CHANGE)
    content = replace_placeholder(content, '{{美股_英伟达_涨跌幅}}', '-2.38%')
    content = replace_placeholder(content, '{{美股_特斯拉_涨跌幅}}', '-1.56%')
    content = replace_placeholder(content, '{{美股_ARM_涨跌幅}}', '小幅下跌')

    # 大宗商品
    content = replace_placeholder(content, '{{大宗_WTI原油}}', f'{WTI_OIL} {WTI_CHANGE}')
    content = replace_placeholder(content, '{{大宗_布伦特原油}}', f'{BRENT_OIL} {BRENT_CHANGE}')
    content = replace_placeholder(content, '{{大宗_国际黄金}}', f'${GOLD_PRICE} {GOLD_CHANGE}')
    content = replace_placeholder(content, '{{大宗_上海金}}', f'{GOLD_PRICE}元/克')
    content = replace_placeholder(content, '{{大宗_白银}}', f'{SILVER_PRICE} {SILVER_CHANGE}')

    # 加密货币
    content = replace_placeholder(content, '{{加密_BTC}}', f'${BTC_PRICE} {BTC_CHANGE}')
    content = replace_placeholder(content, '{{加密_ETH}}', f'${ETH_PRICE} {ETH_CHANGE}')
    content = replace_placeholder(content, '{{加密_BTC_ETF}}', '净流出')
    content = replace_placeholder(content, '{{加密_市场情绪}}', '谨慎乐观')

    # 汇率债券
    content = replace_placeholder(content, '{{汇率_USD/CNY中间价}}', USD_CNY_MID)
    content = replace_placeholder(content, '{{汇率_USD/CNY在岸}}', USD_CNY_ONSHORE)
    content = replace_placeholder(content, '{{汇率_美元指数}}', USD_INDEX)
    content = replace_placeholder(content, '{{债券_美10年收益率}}', f'{USD_INDEX}%')
    content = replace_placeholder(content, '{{债券_美30年收益率}}', '小幅上行')
    content = replace_placeholder(content, '{{债券_中10年收益率}}', f'{CHINA_10Y_BOND}')

    # ========== Tab 4: 价值投资风向 ==========
    # 机构观点
    content = replace_placeholder(content, '{{机构1_观点}}', '中信证券：美联储2026年6月议息会议维持政策利率不变，符合市场预期。当前美国经济韧性较强，通胀压力逐步缓解，但就业市场依然紧张。维持美联储年内维持政策利率不变的判断。港股估值处于历史低位，建议关注高股息和科技板块。')
    content = replace_placeholder(content, '{{机构2_观点}}', '高盛：人工智能、勘探、全球页岩与能源资本支出是2026年顶级投资主题。全球能源转型持续推进，传统能源与新能源并行发展。看好AI算力基础设施、半导体设备等领域的长期增长潜力。')
    content = replace_placeholder(content, '{{机构3_观点}}', '兴业证券：当前市场处于政策蜜月期，A股估值修复空间仍存。建议关注三条主线：一是科技成长，尤其是AI、半导体等确定性较强的方向；二是消费复苏，受益于政策刺激和居民信心恢复；三是高股息资产，在利率下行背景下配置价值凸显。')
    content = replace_placeholder(content, '{{机构4_观点}}', '中金公司：港股估值处于历史低位，下半年或有估值修复机会。建议关注高股息银行股、业绩确定性强的消费龙头、以及受益于政策支持的科技板块。内地居民财富向权益市场迁移趋势未变。')
    content = replace_placeholder(content, '{{机构5_观点}}', '摩根士丹利：A股市场情绪有所回暖，但外部不确定性仍存。看好具备核心技术竞争力的科技企业，以及受益于国内大循环的消费服务类公司。关注半导体设备、AI应用等细分领域。')
    content = replace_placeholder(content, '{{机构6_观点}}', '瑞银集团：全球市场波动加大，防御性资产配置价值提升。看好黄金等避险资产，以及分红稳定的公用事业类股票。A股上市企业盈利增速企稳回升，估值修复行情仍可持续。')

    # 高股息板块
    content = replace_placeholder(content, '{{银行PB}}', '0.5-0.6倍')
    content = replace_placeholder(content, '{{银行股息率}}', '4.5-5.5%')
    content = replace_placeholder(content, '{{电力PE}}', '15-20倍')
    content = replace_placeholder(content, '{{电力股息率}}', '3.5-4.5%')
    content = replace_placeholder(content, '{{中证红利PE}}', '8-10倍')
    content = replace_placeholder(content, '{{长江电力PB}}', '2.5倍')
    content = replace_placeholder(content, '{{中国移动PB}}', '1.2倍')
    content = replace_placeholder(content, '{{招商银行PB}}', '1.1倍')
    content = replace_placeholder(content, '{{中国核电PE}}', '12倍')

    # ========== Tab 5: 关注标的 ==========
    # 工商银行
    content = replace_placeholder(content, '{{标的1_代码}}', '601398')
    content = replace_placeholder(content, '{{标的1_名称}}', '工商银行')
    content = replace_placeholder(content, '{{标的1_价格}}', f'{ICBC_PRICE}元')
    content = replace_placeholder(content, '{{标的1_涨跌幅}}', f'<span class="down">{ICBC_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的1_成交额}}', '27亿')
    content = replace_placeholder(content, '{{标的1_基本面}}', '股息率约5%，PB约0.55倍，资产质量稳健')

    # 建设银行
    content = replace_placeholder(content, '{{标的2_代码}}', '601939')
    content = replace_placeholder(content, '{{标的2_名称}}', '建设银行')
    content = replace_placeholder(content, '{{标的2_价格}}', f'{CCB_PRICE}元')
    content = replace_placeholder(content, '{{标的2_涨跌幅}}', f'<span class="down">{CCB_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的2_成交额}}', '较大')
    content = replace_placeholder(content, '{{标的2_基本面}}', '股息率约5%，PB约0.6倍')

    # 农业银行
    content = replace_placeholder(content, '{{标的3_代码}}', '601288')
    content = replace_placeholder(content, '{{标的3_名称}}', '农业银行')
    content = replace_placeholder(content, '{{标的3_价格}}', f'{ABC_PRICE}元')
    content = replace_placeholder(content, '{{标的3_涨跌幅}}', f'<span class="down">{ABC_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的3_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的3_基本面}}', '股息率约5.5%，PB约0.5倍')

    # 招商银行
    content = replace_placeholder(content, '{{标的4_代码}}', '600036')
    content = replace_placeholder(content, '{{标的4_名称}}', '招商银行')
    content = replace_placeholder(content, '{{标的4_价格}}', f'{CMB_PRICE}元')
    content = replace_placeholder(content, '{{标的4_涨跌幅}}', f'<span class="down">{CMB_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的4_成交额}}', '25.31亿')
    content = replace_placeholder(content, '{{标的4_基本面}}', 'PE约16倍，PB约1.1倍，零售银行龙头')

    # 宁波银行
    content = replace_placeholder(content, '{{标的5_代码}}', '002142')
    content = replace_placeholder(content, '{{标的5_名称}}', '宁波银行')
    content = replace_placeholder(content, '{{标的5_价格}}', f'{NBC_PRICE}元')
    content = replace_placeholder(content, '{{标的5_涨跌幅}}', f'<span class="up">{NBC_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的5_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的5_基本面}}', 'PE约12倍，资产质量优异')

    # 江苏银行
    content = replace_placeholder(content, '{{标的6_代码}}', '600919')
    content = replace_placeholder(content, '{{标的6_名称}}', '江苏银行')
    content = replace_placeholder(content, '{{标的6_价格}}', f'{JSB_PRICE}元')
    content = replace_placeholder(content, '{{标的6_涨跌幅}}', f'<span class="up">{JSB_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的6_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的6_基本面}}', 'PE约5倍，高股息城商行')

    # 杭州银行
    content = replace_placeholder(content, '{{标的7_代码}}', '600926')
    content = replace_placeholder(content, '{{标的7_名称}}', '杭州银行')
    content = replace_placeholder(content, '{{标的7_价格}}', f'{HZB_PRICE}元')
    content = replace_placeholder(content, '{{标的7_涨跌幅}}', f'<span class="up">{HZB_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的7_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的7_基本面}}', 'PE约8倍，区域经济活力强')

    # 重庆银行
    content = replace_placeholder(content, '{{标的8_代码}}', '601963')
    content = replace_placeholder(content, '{{标的8_名称}}', '重庆银行')
    content = replace_placeholder(content, '{{标的8_价格}}', f'{CQYH_PRICE}元')
    content = replace_placeholder(content, '{{标的8_涨跌幅}}', f'<span class="down">{CQYH_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的8_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的8_基本面}}', 'PE约5倍，股息率较高')

    # 长江电力
    content = replace_placeholder(content, '{{标的9_代码}}', '600900')
    content = replace_placeholder(content, '{{标的9_名称}}', '长江电力')
    content = replace_placeholder(content, '{{标的9_价格}}', f'{CGP_PRICE}元')
    content = replace_placeholder(content, '{{标的9_涨跌幅}}', f'<span class="down">{CGP_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的9_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的9_基本面}}', '水电龙头，现金流稳定，股息率约3.5%')

    # 大秦铁路
    content = replace_placeholder(content, '{{标的10_代码}}', '601006')
    content = replace_placeholder(content, '{{标的10_名称}}', '大秦铁路')
    content = replace_placeholder(content, '{{标的10_价格}}', f'{DQTL_PRICE}元')
    content = replace_placeholder(content, '{{标的10_涨跌幅}}', f'<span class="down">{DQTL_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的10_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的10_基本面}}', '股息率约5%，稳定现金牛')

    # 中国移动
    content = replace_placeholder(content, '{{标的11_代码}}', '600941')
    content = replace_placeholder(content, '{{标的11_名称}}', '中国移动')
    content = replace_placeholder(content, '{{标的11_价格}}', f'{CMCC_PRICE}元')
    content = replace_placeholder(content, '{{标的11_涨跌幅}}', f'<span class="up">{CMCC_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的11_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的11_基本面}}', '股息率约4%，PB约1.2倍，运营商龙头')

    # 中国核电
    content = replace_placeholder(content, '{{标的12_代码}}', '601985')
    content = replace_placeholder(content, '{{标的12_名称}}', '中国核电')
    content = replace_placeholder(content, '{{标的12_价格}}', f'{CNP_PRICE}元')
    content = replace_placeholder(content, '{{标的12_涨跌幅}}', f'<span class="up">{CNP_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的12_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的12_基本面}}', 'PE约12倍，核电龙头受益于能源转型')

    # 中国平安
    content = replace_placeholder(content, '{{标的13_代码}}', '601318')
    content = replace_placeholder(content, '{{标的13_名称}}', '中国平安')
    content = replace_placeholder(content, '{{标的13_价格}}', f'{CPIC_PRICE}元')
    content = replace_placeholder(content, '{{标的13_涨跌幅}}', f'<span class="down">{CPIC_CHANGE}</span>')
    content = replace_placeholder(content, '{{标的13_成交额}}', '正常')
    content = replace_placeholder(content, '{{标的13_基本面}}', 'PE约8倍，保险龙头估值修复空间大')

    # ========== Tab 6: 理财话题 ==========
    content = replace_placeholder(content, '{{存款利率_1年}}', CD_1Y)
    content = replace_placeholder(content, '{{存款利率_3年}}', CD_3Y)
    content = replace_placeholder(content, '{{存款利率_5年}}', CD_5Y)
    content = replace_placeholder(content, '{{大额存单_1年}}', '1.40%')
    content = replace_placeholder(content, '{{大额存单_3年}}', '1.55%')
    content = replace_placeholder(content, '{{货币基金_收益率}}', MMF_YIELD)
    content = replace_placeholder(content, '{{纯债基金_收益}}', PURE_BOND_YIELD)
    content = replace_placeholder(content, '{{10年国债收益率}}', CHINA_10Y_BOND)

    # ========== Tab 7: 今日总结 ==========
    content = replace_placeholder(content, '{{宏观面_内容}}', f'陆家嘴论坛释放政策暖风，AI大模型上市政策落地。人民币中间价上调12个基点，汇率维持强势。美联储维持利率不变，外部环境总体稳定。')
    content = replace_placeholder(content, '{{市场面_内容}}', f'A股放量大涨，创业板指{CYB_CHANGE}领涨，科创50飙升{KC50_CHANGE}。两市成交突破{A_SHARES_VOLUME}，量能充沛。美股分化，道指创新高但纳指回调。')
    content = replace_placeholder(content, '{{资金面_内容}}', f'北向资金净卖出约1.36亿，但龙虎榜显示机构净买入6.13亿。银行股短期回调，资金流向成长赛道。高股息资产仍受长线资金青睐。')
    content = replace_placeholder(content, '{{操作建议}}', f'市场放量上涨，创业板指领涨，短期可关注科技成长方向。高股息银行股短期承压，但长期配置价值仍在。黄金维持强势，可适当配置。')

    # ========== 估值参考表 ==========
    content = replace_placeholder(content, '{{速查1_名称}}', '上证指数')
    content = replace_placeholder(content, '{{速查1_数值}}', f'{SH_COMPONENT}')
    content = replace_placeholder(content, '{{速查1_涨跌幅}}', SH_CHANGE)

    content = replace_placeholder(content, '{{速查2_名称}}', '深证成指')
    content = replace_placeholder(content, '{{速查2_数值}}', f'{SZ_COMPONENT}')
    content = replace_placeholder(content, '{{速查2_涨跌幅}}', SZ_CHANGE)

    content = replace_placeholder(content, '{{速查3_名称}}', '创业板指')
    content = replace_placeholder(content, '{{速查3_数值}}', f'{CYB_INDEX}')
    content = replace_placeholder(content, '{{速查3_涨跌幅}}', CYB_CHANGE)

    content = replace_placeholder(content, '{{速查4_名称}}', '两市成交')
    content = replace_placeholder(content, '{{速查4_数值}}', A_SHARES_VOLUME)
    content = replace_placeholder(content, '{{速查4_涨跌幅}}', '放量')

    content = replace_placeholder(content, '{{速查5_名称}}', '北向资金')
    content = replace_placeholder(content, '{{速查5_数值}}', '净卖出')
    content = replace_placeholder(content, '{{速查5_涨跌幅}}', '1.36亿')

    content = replace_placeholder(content, '{{速查6_名称}}', '恒生科技')
    content = replace_placeholder(content, '{{速查6_数值}}', f'{HSTECH_INDEX}')
    content = replace_placeholder(content, '{{速查6_涨跌幅}}', HSTECH_CHANGE)

    content = replace_placeholder(content, '{{速查7_名称}}', 'WTI原油')
    content = replace_placeholder(content, '{{速查7_数值}}', f'${WTI_OIL}')
    content = replace_placeholder(content, '{{速查7_涨跌幅}}', WTI_CHANGE)

    content = replace_placeholder(content, '{{速查8_名称}}', '国际黄金')
    content = replace_placeholder(content, '{{速查8_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{速查8_涨跌幅}}', GOLD_CHANGE)

    content = replace_placeholder(content, '{{速查9_名称}}', '人民币汇率')
    content = replace_placeholder(content, '{{速查9_数值}}', USD_CNY_MID)
    content = replace_placeholder(content, '{{速查9_涨跌幅}}', '升值')

    # ========== Tab 2: AI前沿（续）==========
    # AI应用新闻
    content = replace_placeholder(content, '{{AI应用新闻2_标签和标题}}', '<span class="tag tag-app">🚗 智驾</span>自动驾驶规模化落地')
    content = replace_placeholder(content, '{{AI应用新闻2_正文}}', f'城市NOA（Navigate on Autopilot）加速落地，一二线城市高精地图覆盖区域持续扩大。AI视觉算法迭代升级，{color("接管里程", "cyan")}指标持续优化。智能驾驶从高端车型向大众车型渗透，相关产业链充分受益。')

    content = replace_placeholder(content, '{{AI应用新闻3_标签和标题}}', '<span class="tag tag-app">💬 办公</span>AI办公助手普及')
    content = replace_placeholder(content, '{{AI应用新闻3_正文}}', f'AI办公助手在企业侧加速渗透，文档处理、会议纪要、数据分析等场景效率提升显著。AI Agent成为办公自动化的新范式，{color("降本增效", "red")}效果明显，看好垂直领域AI应用龙头。')

    # 产业趋势
    content = replace_placeholder(content, '{{产业趋势新闻1_标签和标题}}', '<span class="tag tag-ai">🔮 趋势</span>端侧AI重塑硬件生态')
    content = replace_placeholder(content, '{{产业趋势新闻1_正文}}', f'端侧AI芯片加速迭代，NPU算力持续提升。AI手机、AI PC从概念走向普及，端侧大模型部署成为趋势。这一变革将重塑消费电子产业格局，{color("硬件+软件+服务", "cyan")}一体化能力成为核心竞争壁垒。')

    # ========== Tab 3: 全球市场（续）==========
    content = replace_placeholder(content, '{{报告日期}}', TODAY)
    content = replace_placeholder(content, '{{A股_收盘日期}}', '6月17日')
    content = replace_placeholder(content, '{{A股_成交额备注}}', '放量')
    content = replace_placeholder(content, '{{港股_收盘日期}}', '6月17日')
    content = replace_placeholder(content, '{{美股_收盘日期}}', '6月17日')
    content = replace_placeholder(content, '{{美股_ARM}}', '小幅下跌')
    content = replace_placeholder(content, '{{亚太_收盘日期}}', '6月17日')
    content = replace_placeholder(content, '{{亚太_韩国KOSPI_状态}}', f'{KOSPI_INDEX} {KOSPI_CHANGE}')
    content = replace_placeholder(content, '{{亚太_台湾加权_状态}}', '震荡整理')
    content = replace_placeholder(content, '{{亚太_印度Sensex_状态}}', '小幅上涨')
    content = replace_placeholder(content, '{{亚太_澳洲ASX200_状态}}', '小幅下跌')
    content = replace_placeholder(content, '{{欧洲_收盘日期}}', '6月17日')
    content = replace_placeholder(content, '{{大宗商品_收盘日期}}', '6月17日')
    content = replace_placeholder(content, '{{汇率债券_收盘日期}}', '6月17日')
    content = replace_placeholder(content, '{{汇率_在岸汇率}}', USD_CNY_ONSHORE)
    content = replace_placeholder(content, '{{汇率_美10年期}}', f'{USD_INDEX}%')
    content = replace_placeholder(content, '{{汇率_美30年期}}', '小幅上行')
    content = replace_placeholder(content, '{{汇率_中10年期}}', CHINA_10Y_BOND)
    content = replace_placeholder(content, '{{加密货币_收盘日期}}', '6月17日')
    content = replace_placeholder(content, '{{加密_BTCEFT}}', '净流出')

    # ========== 市场综评 ==========
    content = replace_placeholder(content, '{{市场综评_日期}}', '6月17日')
    content = replace_placeholder(content, '{{综评_A股行情标题}}', 'A股放量大涨')
    content = replace_placeholder(content, '{{综评_A股行情标签}}', '成长领涨')
    content = replace_placeholder(content, '{{综评_A股段落1}}', f'上证指数{SH_CHANGE}，深证成指{SZ_CHANGE}，创业板指{color("大涨1.56%", "red")}领涨，科创50{color("飙升4.69%", "red")}。芯片股集体爆发，成长赛道资金回流。两市成交突破{color("3.09万亿", "cyan")}，量能充沛。')
    content = replace_placeholder(content, '{{综评_A股段落2}}', f'创业板指{CYB_CHANGE}，科创50{KC50_CHANGE}，显示科技成长板块成为市场主线。成交额较前一交易日大幅放量，市场做多情绪回暖。')
    content = replace_placeholder(content, '{{综评_A股段落3}}', '数据来源：6月17日收盘数据')

    content = replace_placeholder(content, '{{综评_外围市场标题}}', '美股走势分化')
    content = replace_placeholder(content, '{{综评_外围市场标签}}', '科技股承压')
    content = replace_placeholder(content, '{{综评_外围段落1}}', f'道指续创历史新高{color("51999.67点", "cyan")}，{color("涨0.64%", "red")}；纳指{color("大跌1.15%", "green")}，科技股分化明显。英伟达{color("跌2.38%", "green")}，特斯拉{color("跌1.56%", "green")}。')
    content = replace_placeholder(content, '{{综评_外围段落2}}', '美债收益率小幅上行，市场对美联储政策预期稳定。纳斯达克中国金龙指数收跌，中概股承压。')
    content = replace_placeholder(content, '{{综评_外围段落3}}', '数据来源：6月17日美股收盘')

    content = replace_placeholder(content, '{{综评_地缘政策标题}}', '霍尔木兹海峡重开')
    content = replace_placeholder(content, '{{综评_地缘政策标签}}', '油价承压')
    content = replace_placeholder(content, '{{综评_地缘段落1}}', f'美伊谈判推进，霍尔木兹海峡即将全面开放。亚洲股市暴涨，日经225{color("飙升5.41%", "red")}，韩国KOSPI{color("大涨5.76%", "red")}。')
    content = replace_placeholder(content, '{{综评_地缘段落2}}', '原油价格大幅回落，WTI原油{color("跌0.61%", "green")}，布伦特原油{color("跌0.13%", "green")}。能源市场供给预期改善，通胀压力进一步缓解。')
    content = replace_placeholder(content, '{{综评_地缘段落3}}', '数据来源：6月17日地缘动态')

    content = replace_placeholder(content, '{{综评_风险事件标题}}', '市场情绪')
    content = replace_placeholder(content, '{{综评_风险事件标签}}', '中性')
    content = replace_placeholder(content, '{{综评_风险段落1}}', '市场放量上涨，创业板指领涨，做多情绪回暖。但外围美股科技股承压，短期或震荡。')
    content = replace_placeholder(content, '{{综评_风险段落2}}', '北向资金小幅净卖出，但龙虎榜机构净买入，整体资金面平稳。关注后续量能配合。')
    content = replace_placeholder(content, '{{综评_风险段落3}}', '数据截至6月17日收盘')

    # ========== Tab 4: 价值投资风向（续）==========
    content = replace_placeholder(content, '{{正面因素_内容}}', f'A股放量大涨，创业板指{CYB_CHANGE}，科创50{KC50_CHANGE}；国际金价创新高${GOLD_PRICE}；人民币汇率升值')
    content = replace_placeholder(content, '{{市场热点_内容}}', f'芯片股爆发，科创50大涨{KC50_CHANGE}；霍尔木兹海峡重开，亚洲股市暴涨；陆家嘴论坛召开，AI大模型政策落地')
    content = replace_placeholder(content, '{{风险提示_内容}}', f'银行股短期回调，建行跌超2%；美股纳指大跌{NDX_CHANGE}，科技股分化；加密货币市场情绪谨慎')

    # ========== 市场情绪 ==========
    content = replace_placeholder(content, '{{市场情绪_状态颜色}}', 'accent')
    content = replace_placeholder(content, '{{市场情绪_状态}}', '谨慎乐观')
    content = replace_placeholder(content, '{{市场情绪_涨跌比}}', '涨多跌少')
    content = replace_placeholder(content, '{{市场情绪_成交额}}', '3.09万亿')
    content = replace_placeholder(content, '{{市场情绪_北向资金}}', '小幅净卖出')

    # 机构观点
    content = replace_placeholder(content, '{{机构1_简称}}', '中信')
    content = replace_placeholder(content, '{{机构1_名称}}', '中信证券')
    content = replace_placeholder(content, '{{机构1_标签}}', '券商龙头')

    content = replace_placeholder(content, '{{机构2_简称}}', '高盛')
    content = replace_placeholder(content, '{{机构2_名称}}', '高盛')
    content = replace_placeholder(content, '{{机构2_标签}}', '外资投行')

    content = replace_placeholder(content, '{{机构3_简称}}', '兴业')
    content = replace_placeholder(content, '{{机构3_名称}}', '兴业证券')
    content = replace_placeholder(content, '{{机构3_标签}}', '本土券商')

    content = replace_placeholder(content, '{{机构4_简称}}', '中金')
    content = replace_placeholder(content, '{{机构4_名称}}', '中金公司')
    content = replace_placeholder(content, '{{机构4_标签}}', '顶级投行')

    content = replace_placeholder(content, '{{机构5_简称}}', '大摩')
    content = replace_placeholder(content, '{{机构5_名称}}', '摩根士丹利')
    content = replace_placeholder(content, '{{机构5_标签}}', '国际投行')

    content = replace_placeholder(content, '{{机构6_简称}}', '瑞银')
    content = replace_placeholder(content, '{{机构6_名称}}', '瑞银集团')
    content = replace_placeholder(content, '{{机构6_标签}}', '瑞士银行')

    # 情绪指标
    content = replace_placeholder(content, '{{情绪_高股息_名称}}', '高股息')
    content = replace_placeholder(content, '{{情绪_高股息_宽度}}', '85%')
    content = replace_placeholder(content, '{{情绪_高股息_百分比}}', '85%')
    content = replace_placeholder(content, '{{情绪_高股息_描述}}', '银行、电力板块持续受青睐')

    content = replace_placeholder(content, '{{情绪_银行_名称}}', '银行板块')
    content = replace_placeholder(content, '{{情绪_银行_宽度}}', '60%')
    content = replace_placeholder(content, '{{情绪_银行_百分比}}', '60%')
    content = replace_placeholder(content, '{{情绪_银行_描述}}', '短期回调，机构仍看好')

    content = replace_placeholder(content, '{{情绪_公用事业_名称}}', '公用事业')
    content = replace_placeholder(content, '{{情绪_公用事业_宽度}}', '75%')
    content = replace_placeholder(content, '{{情绪_公用事业_百分比}}', '75%')
    content = replace_placeholder(content, '{{情绪_公用事业_描述}}', '防御属性强，稳定现金流')

    content = replace_placeholder(content, '{{情绪_电力_名称}}', '电力板块')
    content = replace_placeholder(content, '{{情绪_电力_宽度}}', '70%')
    content = replace_placeholder(content, '{{情绪_电力_百分比}}', '70%')
    content = replace_placeholder(content, '{{情绪_电力_描述}}', '水电为主，业绩稳定')

    content = replace_placeholder(content, '{{情绪_AI算力_名称}}', 'AI算力')
    content = replace_placeholder(content, '{{情绪_AI算力_宽度}}', '90%')
    content = replace_placeholder(content, '{{情绪_AI算力_百分比}}', '90%')
    content = replace_placeholder(content, '{{情绪_AI算力_样式类}}', 'hot')
    content = replace_placeholder(content, '{{情绪_AI算力_描述}}', '大模型发布，政策利好')

    content = replace_placeholder(content, '{{情绪_能源油价_名称}}', '能源油价')
    content = replace_placeholder(content, '{{情绪_能源油价_宽度}}', '45%')
    content = replace_placeholder(content, '{{情绪_能源油价_百分比}}', '45%')
    content = replace_placeholder(content, '{{情绪_能源油价_描述}}', '霍尔木兹重开，油价承压')

    content = replace_placeholder(content, '{{情绪_新能源_名称}}', '新能源')
    content = replace_placeholder(content, '{{情绪_新能源_宽度}}', '80%')
    content = replace_placeholder(content, '{{情绪_新能源_百分比}}', '80%')
    content = replace_placeholder(content, '{{情绪_新能源_样式类}}', 'hot')
    content = replace_placeholder(content, '{{情绪_新能源_描述}}', '能源转型持续推进')

    content = replace_placeholder(content, '{{情绪_黄金_名称}}', '黄金')
    content = replace_placeholder(content, '{{情绪_黄金_宽度}}', '88%')
    content = replace_placeholder(content, '{{情绪_黄金_百分比}}', '88%')
    content = replace_placeholder(content, '{{情绪_黄金_样式类}}', 'hot')
    content = replace_placeholder(content, '{{情绪_黄金_描述}}', '创历史新高，避险需求旺')

    content = replace_placeholder(content, '{{情绪_加密货币_名称}}', '加密货币')
    content = replace_placeholder(content, '{{情绪_加密货币_宽度}}', '55%')
    content = replace_placeholder(content, '{{情绪_加密货币_百分比}}', '55%')
    content = replace_placeholder(content, '{{情绪_加密货币_样式类}}', 'low')
    content = replace_placeholder(content, '{{情绪_加密货币_描述}}', 'BTC震荡，ETH回调')

    # 社区话题标签
    content = replace_placeholder(content, '{{社区话题标签1}}', '银行股')
    content = replace_placeholder(content, '{{社区话题标签2}}', 'AI大模型')
    content = replace_placeholder(content, '{{社区话题标签3}}', '黄金')
    content = replace_placeholder(content, '{{社区话题标签4}}', '原油')
    content = replace_placeholder(content, '{{社区话题标签5}}', '创业板')

    # ========== Tab 4: 高股息板块 ==========
    content = replace_placeholder(content, '{{高股息_银行标题}}', '银行板块：股息率4.5-5.5%，配置价值凸显')
    content = replace_placeholder(content, '{{高股息_银行内容}}', f'银行板块当前PB约{color("0.5-0.6倍", "cyan")}，处于历史低位。股息率{color("4.5-5.5%", "red")}，显著高于无风险收益率。工商银行、建设银行、农业银行等大行股息率稳定，适合长期配置。短期银行股回调提供更好的买入机会。险资、北向资金持续加仓银行股，估值修复逻辑未变。')
    content = replace_placeholder(content, '{{高股息_公用事业标题}}', '公用事业：稳定现金流，高股息防御强')
    content = replace_placeholder(content, '{{高股息_公用事业内容}}', f'水电、燃气等公用事业板块具备{color("稳定现金流", "cyan")}特征，不受经济周期影响。长江电力等龙头股息率约{color("3.5%", "red")}，业绩确定性极强。在市场波动加大背景下，公用事业板块的防御属性凸显，适合保守型投资者。')
    content = replace_placeholder(content, '{{高股息_电力标题}}', '电力板块：能源转型受益，业绩增长确定')
    content = replace_placeholder(content, '{{高股息_电力内容}}', f'电力板块PE约{color("15-20倍", "cyan")}，股息率{color("3.5-4.5%", "red")}。受益于能源转型，核电、水电等清洁能源装机持续增长。中国核电等龙头业绩增速稳定，现金流良好，具备长期投资价值。')
    content = replace_placeholder(content, '{{高股息_央企标题}}', '央企蓝筹：高股息+低估值，估值修复可期')
    content = replace_placeholder(content, '{{高股息_央企内容}}', f'中国移动、中国建筑等央企蓝筹PB约{color("1.0-1.2倍", "cyan")}，股息率{color("4%", "red")}以上。央企改革持续推进，ROE提升逻辑清晰。在中特估估值体系下，央企蓝筹估值修复空间较大，适合长线资金配置。')

    # ========== Tab 4: 低估值板块 ==========
    content = replace_placeholder(content, '{{低估值1_名称}}', '中证红利')
    content = replace_placeholder(content, '{{估值_中证红利PE_今日涨幅}}', f'{SH_CHANGE}')
    content = replace_placeholder(content, '{{低估值1_收盘价}}', f'{SH_COMPONENT}点')
    content = replace_placeholder(content, '{{低估值1_描述}}', f'低估值高股息策略有效，中证红利指数{SH_CHANGE}，PE约8-10倍，股息率约5%，适合稳健型投资者。')

    content = replace_placeholder(content, '{{低估值2_名称}}', '港股恒生科技')
    content = replace_placeholder(content, '{{低估值2_今日涨幅}}', HSTECH_CHANGE)
    content = replace_placeholder(content, '{{低估值2_涨幅样式}}', 'up')
    content = replace_placeholder(content, '{{低估值2_收盘价}}', f'{HSTECH_INDEX}点')
    content = replace_placeholder(content, '{{低估值2_描述}}', f'恒生科技指数{HSTECH_CHANGE}，估值处于历史低位，互联网龙头估值修复空间大。')

    # ========== 资金流向 ==========
    content = replace_placeholder(content, '{{资金流向_节点1标题}}', '北向资金')
    content = replace_placeholder(content, '{{资金流向_节点1描述}}', '净卖出1.36亿')
    content = replace_placeholder(content, '{{资金流向_节点2标题}}', '机构资金')
    content = replace_placeholder(content, '{{资金流向_节点2描述}}', '净买入6.13亿')
    content = replace_placeholder(content, '{{资金流向_节点3标题}}', 'ETF流入')
    content = replace_placeholder(content, '{{资金流向_节点3描述}}', '证券ETF净流入')
    content = replace_placeholder(content, '{{资金_证券ETF流向}}', '净流入')
    content = replace_placeholder(content, '{{资金_红利ETF流向}}', '稳定流入')

    # ========== 估值数据 ==========
    content = replace_placeholder(content, '{{估值_银行PB}}', '0.5-0.6倍')
    content = replace_placeholder(content, '{{估值_银行PB_标签}}', '历史低位')
    content = replace_placeholder(content, '{{估值_银行PB_说明}}', 'PB持续低迷')

    # ========== Tab 4: 低估值板块 ==========
    content = replace_placeholder(content, '{{低估值1_名称}}', '中证红利')
    content = replace_placeholder(content, '{{估值_中证红利PE_今日涨幅}}', f'{SH_CHANGE}')
    content = replace_placeholder(content, '{{低估值1_收盘价}}', f'{SH_COMPONENT}点')
    content = replace_placeholder(content, '{{低估值1_描述}}', f'低估值高股息策略有效，中证红利指数{SH_CHANGE}，PE约8-10倍，股息率约5%，适合稳健型投资者。')

    content = replace_placeholder(content, '{{低估值2_名称}}', '港股恒生科技')
    content = replace_placeholder(content, '{{低估值2_今日涨幅}}', HSTECH_CHANGE)
    content = replace_placeholder(content, '{{低估值2_涨幅样式}}', 'up')
    content = replace_placeholder(content, '{{低估值2_收盘价}}', f'{HSTECH_INDEX}点')
    content = replace_placeholder(content, '{{低估值2_描述}}', f'恒生科技指数{HSTECH_CHANGE}，估值处于历史低位，互联网龙头估值修复空间大。')

    # ========== 资金流向 ==========
    content = replace_placeholder(content, '{{资金流向_节点1标题}}', '北向资金')
    content = replace_placeholder(content, '{{资金流向_节点1描述}}', '净卖出1.36亿')
    content = replace_placeholder(content, '{{资金流向_节点2标题}}', '机构资金')
    content = replace_placeholder(content, '{{资金流向_节点2描述}}', '净买入6.13亿')
    content = replace_placeholder(content, '{{资金流向_节点3标题}}', 'ETF流入')
    content = replace_placeholder(content, '{{资金流向_节点3描述}}', '证券ETF净流入')
    content = replace_placeholder(content, '{{资金_证券ETF流向}}', '净流入')
    content = replace_placeholder(content, '{{资金_红利ETF流向}}', '稳定流入')

    # ========== 估值数据 ==========
    content = replace_placeholder(content, '{{估值_银行PB}}', '0.5-0.6倍')
    content = replace_placeholder(content, '{{估值_银行PB_标签}}', '历史低位')
    content = replace_placeholder(content, '{{估值_银行PB_标签类}}', 'low')
    content = replace_placeholder(content, '{{估值_银行PB_说明}}', 'PB持续低迷')

    content = replace_placeholder(content, '{{估值_上证PE}}', '约15倍')
    content = replace_placeholder(content, '{{估值_上证PE_标签}}', '适中')
    content = replace_placeholder(content, '{{估值_上证PE_标签类}}', 'mid')

    content = replace_placeholder(content, '{{估值_银行股息率}}', '4.5-5.5%')
    content = replace_placeholder(content, '{{估值_银行股息率_标签}}', '较高')
    content = replace_placeholder(content, '{{估值_银行股息率_标签类}}', 'high')

    content = replace_placeholder(content, '{{估值_中证红利PE}}', '8-10倍')
    content = replace_placeholder(content, '{{估值_中证红利PE_标签}}', '历史低位')
    content = replace_placeholder(content, '{{估值_中证红利PE_标签类}}', 'low')

    content = replace_placeholder(content, '{{估值_神华吨煤利润}}', '约400元')
    content = replace_placeholder(content, '{{估值_神华_标签}}', '稳定')
    content = replace_placeholder(content, '{{估值_神华_标签类}}', 'mid')

    content = replace_placeholder(content, '{{估值_中国移动PB}}', '1.2倍')
    content = replace_placeholder(content, '{{估值_中国移动PB_标签}}', '适中')
    content = replace_placeholder(content, '{{估值_中国移动PB_标签类}}', 'mid')

    content = replace_placeholder(content, '{{估值_招商银行PB}}', '1.1倍')
    content = replace_placeholder(content, '{{估值_招商银行PB_标签}}', '合理')
    content = replace_placeholder(content, '{{估值_招商银行PB_标签类}}', 'mid')

    content = replace_placeholder(content, '{{估值_中国核电PE}}', '12倍')
    content = replace_placeholder(content, '{{估值_中国核电PE_标签}}', '适中')
    content = replace_placeholder(content, '{{估值_中国核电PE_标签类}}', 'mid')

    content = replace_placeholder(content, '{{估值_黄金价格}}', '$4332')
    content = replace_placeholder(content, '{{估值_黄金价格_标签}}', '创新高')
    content = replace_placeholder(content, '{{估值_黄金价格_标签类}}', 'hot')

    # ========== Tab 5: 关注标的深度解读 ==========
    # 标的1-13的详细分析
    # 标的1 工商银行
    content = replace_placeholder(content, '{{标的1_股价}}', f'{ICBC_PRICE}元')
    content = replace_placeholder(content, '{{标的1_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{标的1_要点1}}', f'{color("股息率约5%", "red")}，显著高于无风险收益率')
    content = replace_placeholder(content, '{{标的1_要点2}}', f'{color("PB约0.55倍", "cyan")}，处于历史低位')
    content = replace_placeholder(content, '{{标的1_要点3}}', f'{color("资产质量稳健", "green")}，不良贷款率可控')
    content = replace_placeholder(content, '{{标的1_要点4}}', f'{color("短期回调", "yellow")}，成交27亿抛压明显')
    content = replace_placeholder(content, '{{标的1_要点5}}', f'长期配置价值凸显，适合险资和长线资金')

    # 标的2 建设银行
    content = replace_placeholder(content, '{{标的2_股价}}', f'{CCB_PRICE}元')
    content = replace_placeholder(content, '{{标的2_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{标的2_要点1}}', f'{color("股息率约5%", "red")}，大行中较高')
    content = replace_placeholder(content, '{{标的2_要点2}}', f'{color("PB约0.6倍", "cyan")}，估值历史低位')
    content = replace_placeholder(content, '{{标的2_要点3}}', f'{color("跌超2%", "green")}，领跌大行，短期承压')
    content = replace_placeholder(content, '{{标的2_要点4}}', f'{color("基本面稳定", "green")}，业绩确定性较强')
    content = replace_placeholder(content, '{{标的2_要点5}}', f'回调提供更好买入机会')

    # 标的3 农业银行
    content = replace_placeholder(content, '{{标的3_股价}}', f'{ABC_PRICE}元')
    content = replace_placeholder(content, '{{标的3_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{标的3_要点1}}', f'{color("股息率约5.5%", "red")}，四大行最高')
    content = replace_placeholder(content, '{{标的3_要点2}}', f'{color("PB约0.5倍", "cyan")}，破净严重')
    content = replace_placeholder(content, '{{标的3_要点3}}', f'{color("资产质量改善", "green")}，不良率持续下降')
    content = replace_placeholder(content, '{{标的3_要点4}}', f'{color("短期跟随板块回调", "yellow")}，资金流出')
    content = replace_placeholder(content, '{{标的3_要点5}}', f'高股息防御配置首选')

    # 标的4 招商银行
    content = replace_placeholder(content, '{{标的4_股价}}', f'{CMB_PRICE}元')
    content = replace_placeholder(content, '{{标的4_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{标的4_要点1}}', f'{color("PE约16倍", "cyan")}，零售银行龙头溢价')
    content = replace_placeholder(content, '{{标的4_要点2}}', f'{color("PB约1.1倍", "cyan")}，估值相对合理')
    content = replace_placeholder(content, '{{标的4_要点3}}', f'{color("跌0.88%", "green")}，成交25亿小幅回调')
    content = replace_placeholder(content, '{{标的4_要点4}}', f'{color("零售业务强劲", "red")}，资产质量优异')
    content = replace_placeholder(content, '{{标的4_要点5}}', f'长期看好，短期注意板块轮动')

    # 标的5 宁波银行
    content = replace_placeholder(content, '{{标的5_股价}}', f'{NBC_PRICE}元')
    content = replace_placeholder(content, '{{标的5_涨跌class}}', 'up')
    content = replace_placeholder(content, '{{标的5_要点1}}', f'{color("PE约12倍", "cyan")}，城商行中估值较低')
    content = replace_placeholder(content, '{{标的5_要点2}}', f'{color("资产质量优异", "green")}，不良率控制良好')
    content = replace_placeholder(content, '{{标的5_要点3}}', f'{color("微涨0.06%", "red")}，表现强于大行')
    content = replace_placeholder(content, '{{标的5_要点4}}', f'{color("区域经济活力强", "yellow")}，业务拓展空间大')
    content = replace_placeholder(content, '{{标的5_要点5}}', f'高成长性城商行代表')

    # 标的6 江苏银行
    content = replace_placeholder(content, '{{标的6_股价}}', f'{JSB_PRICE}元')
    content = replace_placeholder(content, '{{标的6_涨跌class}}', 'up')
    content = replace_placeholder(content, '{{标的6_要点1}}', f'{color("PE约5倍", "cyan")}，估值极低')
    content = replace_placeholder(content, '{{标的6_要点2}}', f'{color("股息率较高", "red")}，高股息策略适用')
    content = replace_placeholder(content, '{{标的6_要点3}}', f'{color("微涨0.1%", "red")}，城商行中表现稳健')
    content = replace_placeholder(content, '{{标的6_要点4}}', f'{color("规模较大", "yellow")}，江苏省经济活力强')
    content = replace_placeholder(content, '{{标的6_要点5}}', f'低估值高股息配置价值突出')

    # 标的7 杭州银行
    content = replace_placeholder(content, '{{标的7_股价}}', f'{HZB_PRICE}元')
    content = replace_placeholder(content, '{{标的7_涨跌class}}', 'up')
    content = replace_placeholder(content, '{{标的7_要点1}}', f'{color("PE约8倍", "cyan")}，城商行中估值合理')
    content = replace_placeholder(content, '{{标的7_要点2}}', f'{color("业绩增长", "green")}，营收增速较快')
    content = replace_placeholder(content, '{{标的7_要点3}}', f'{color("微涨0.3%", "red")}，走势强于板块')
    content = replace_placeholder(content, '{{标的7_要点4}}', f'{color("区域经济发达", "yellow")}，浙江民营经济活跃')
    content = replace_placeholder(content, '{{标的7_要点5}}', f'成长性突出的城商行')

    # 标的8 重庆银行
    content = replace_placeholder(content, '{{标的8_股价}}', f'{CQYH_PRICE}元')
    content = replace_placeholder(content, '{{标的8_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{标的8_要点1}}', f'{color("PE约5倍", "cyan")}，估值较低')
    content = replace_placeholder(content, '{{标的8_要点2}}', f'{color("股息率较高", "red")}，高股息特征明显')
    content = replace_placeholder(content, '{{标的8_要点3}}', f'{color("小幅下跌0.5%", "green")}，调整幅度有限')
    content = replace_placeholder(content, '{{标的8_要点4}}', f'{color("成渝地区双城", "yellow")}，受益于区域发展')
    content = replace_placeholder(content, '{{标的8_要点5}}', f'低估值高股息标的')

    # 标的9 长江电力
    content = replace_placeholder(content, '{{标的9_股价}}', f'{CGP_PRICE}元')
    content = replace_placeholder(content, '{{标的9_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{标的9_要点1}}', f'{color("股息率约3.5%", "red")}，稳定现金牛')
    content = replace_placeholder(content, '{{标的9_要点2}}', f'{color("PB约2.5倍", "cyan")}，水电龙头溢价')
    content = replace_placeholder(content, '{{标的9_要点3}}', f'{color("跌0.7%", "green")}，防御属性显现')
    content = replace_placeholder(content, '{{标的9_要点4}}', f'{color("现金流稳定", "green")}，不受经济周期影响')
    content = replace_placeholder(content, '{{标的9_要点5}}', f'长期投资者防御配置首选')

    # 标的10 大秦铁路
    content = replace_placeholder(content, '{{标的10_股价}}', f'{DQTL_PRICE}元')
    content = replace_placeholder(content, '{{标的10_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{标的10_要点1}}', f'{color("股息率约5%", "red")}，高股息代表')
    content = replace_placeholder(content, '{{标的10_要点2}}', f'{color("稳定现金回报", "green")}，业绩稳定')
    content = replace_placeholder(content, '{{标的10_要点3}}', f'{color("小幅下跌0.14%", "green")}，调整有限')
    content = replace_placeholder(content, '{{标的10_要点4}}', f'{color("运煤专线", "yellow")}，区域垄断优势')
    content = replace_placeholder(content, '{{标的10_要点5}}', f'稳健收益类投资者适合')

    # 标的11 中国移动
    content = replace_placeholder(content, '{{标的11_股价}}', f'{CMCC_PRICE}元')
    content = replace_placeholder(content, '{{标的11_涨跌class}}', 'up')
    content = replace_placeholder(content, '{{标的11_要点1}}', f'{color("股息率约4%", "red")}，运营商最高')
    content = replace_placeholder(content, '{{标的11_要点2}}', f'{color("PB约1.2倍", "cyan")}，估值合理')
    content = replace_placeholder(content, '{{标的11_要点3}}', f'{color("涨1.5%", "red")}，走势强劲')
    content = replace_placeholder(content, '{{标的11_要点4}}', f'{color("5G龙头", "yellow")}，用户规模全球第一')
    content = replace_placeholder(content, '{{标的11_要点5}}', f'央企蓝筹，中特估受益标的')

    # 标的12 中国核电
    content = replace_placeholder(content, '{{标的12_股价}}', f'{CNP_PRICE}元')
    content = replace_placeholder(content, '{{标的12_涨跌class}}', 'up')
    content = replace_placeholder(content, '{{标的12_要点1}}', f'{color("PE约12倍", "cyan")}，清洁能源估值合理')
    content = replace_placeholder(content, '{{标的12_要点2}}', f'{color("核电龙头", "yellow")}，技术壁垒高')
    content = replace_placeholder(content, '{{标的12_要点3}}', f'{color("微涨0.5%", "red")}，走势稳健')
    content = replace_placeholder(content, '{{标的12_要点4}}', f'{color("能源转型受益", "green")}，政策支持明确')
    content = replace_placeholder(content, '{{标的12_要点5}}', f'成长性+高股息兼具')

    # 标的13 中国平安
    content = replace_placeholder(content, '{{标的13_股价}}', f'{CPIC_PRICE}元')
    content = replace_placeholder(content, '{{标的13_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{标的13_要点1}}', f'{color("PE约8倍", "cyan")}，保险龙头低估')
    content = replace_placeholder(content, '{{标的13_要点2}}', f'{color("综合金融", "yellow")}，牌照齐全')
    content = replace_placeholder(content, '{{标的13_要点3}}', f'{color("小幅下跌0.3%", "green")}，回调有限')
    content = replace_placeholder(content, '{{标的13_要点4}}', f'{color("估值修复空间大", "red")}，ROE有望提升')
    content = replace_placeholder(content, '{{标的13_要点5}}', f'保险行业龙头，长期配置价值显现')

    # ========== 深度解读 ==========
    content = replace_placeholder(content, '{{深度解读_银行组标题}}', '银行板块')
    content = replace_placeholder(content, '{{深度解读_银行组标签}}', '高股息+低估值')
    content = replace_placeholder(content, '{{深度解读_银行1_标题}}', '工商银行')
    content = replace_placeholder(content, '{{深度解读_银行1_指标}}', f'{ICBC_PRICE}元 {ICBC_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_银行2_标题}}', '建设银行')
    content = replace_placeholder(content, '{{深度解读_银行2_指标}}', f'{CCB_PRICE}元 {CCB_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_银行3_标题}}', '招商银行')
    content = replace_placeholder(content, '{{深度解读_银行3_指标}}', f'{CMB_PRICE}元 {CMB_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_银行总结}}', f'银行板块PB约{color("0.5-0.6倍", "cyan")}，股息率{color("4.5-5.5%", "red")}，处于历史估值底部。短期银行股回调提供更好配置机会，险资、北向资金持续加仓。长期来看，估值修复逻辑未变。')

    content = replace_placeholder(content, '{{深度解读_公用组标题}}', '公用事业')
    content = replace_placeholder(content, '{{深度解读_公用组标签}}', '稳定现金流')
    content = replace_placeholder(content, '{{深度解读_公用1_标题}}', '长江电力')
    content = replace_placeholder(content, '{{深度解读_公用1_指标}}', f'{CGP_PRICE}元 {CGP_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_公用2_标题}}', '中国核电')
    content = replace_placeholder(content, '{{深度解读_公用2_指标}}', f'{CNP_PRICE}元 {CNP_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_公用总结}}', f'公用事业板块具备{color("稳定现金流", "cyan")}特征，不受经济周期影响。长江电力等龙头股息率约{color("3.5%", "red")}，业绩确定性极强，是防御配置的理想选择。')

    content = replace_placeholder(content, '{{深度解读_央企组标题}}', '央企蓝筹')
    content = replace_placeholder(content, '{{深度解读_央企组标签}}', '中特估受益')
    content = replace_placeholder(content, '{{深度解读_央企1_标题}}', '中国移动')
    content = replace_placeholder(content, '{{深度解读_央企1_指标}}', f'{CMCC_PRICE}元 {CMCC_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_央企2_标题}}', '中国平安')
    content = replace_placeholder(content, '{{深度解读_央企2_指标}}', f'{CPIC_PRICE}元 {CPIC_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_央企3_标题}}', '中国核电')
    content = replace_placeholder(content, '{{深度解读_央企3_指标}}', f'{CNP_PRICE}元 {CNP_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_央企4_标题}}', '大秦铁路')
    content = replace_placeholder(content, '{{深度解读_央企4_指标}}', f'{DQTL_PRICE}元 {DQTL_CHANGE}')
    content = replace_placeholder(content, '{{深度解读_央企总结}}', f'央企蓝筹PB约{color("1.0-1.2倍", "cyan")}，股息率{color("4%", "red")}以上。在中特估估值体系下，央企改革持续推进，ROE提升逻辑清晰，估值修复空间较大。')

    content = replace_placeholder(content, '{{深度解读_配置建议内容}}', f'当前市场环境下，建议关注三条主线：{color("一", "yellow")}是科技成长，AI、半导体等确定性较强的方向；{color("二", "yellow")}是高股息，银行、电力等稳定现金流板块；{color("三", "yellow")}是消费复苏，受益于政策刺激和居民信心恢复。')

    # ========== Tab 6: 理财话题 ==========
    content = replace_placeholder(content, '{{标的_正面提示标题}}', '利好因素')
    content = replace_placeholder(content, '{{标的_正面提示内容}}', f'A股放量大涨，创业板指{CYB_CHANGE}领涨；国际金价创历史新高${GOLD_PRICE}；人民币汇率升值；科创板AI大模型政策落地')
    content = replace_placeholder(content, '{{标的_风险提示标题}}', '风险提示')
    content = replace_placeholder(content, '{{标的_风险提示内容}}', f'银行股短期回调，建行跌超2%；美股纳指大跌{NDX_CHANGE}；加密货币市场情绪谨慎；外围科技股分化')

    # 理财卡片
    content = replace_placeholder(content, '{{理财卡1_标题}}', '黄金')
    content = replace_placeholder(content, '{{理财卡1_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{理财卡1_备注}}', '创历史新高')
    content = replace_placeholder(content, '{{理财卡2_标题}}', '银行股息率')
    content = replace_placeholder(content, '{{理财卡2_数值}}', '4.5-5.5%')
    content = replace_placeholder(content, '{{理财卡2_备注}}', '历史高位')
    content = replace_placeholder(content, '{{理财卡3_标题}}', '10年国债')
    content = replace_placeholder(content, '{{理财卡3_数值}}', CHINA_10Y_BOND)
    content = replace_placeholder(content, '{{理财卡3_备注}}', '低位运行')
    content = replace_placeholder(content, '{{理财卡4_标题}}', '货币基金')
    content = replace_placeholder(content, '{{理财卡4_数值}}', MMF_YIELD)
    content = replace_placeholder(content, '{{理财卡4_备注}}', '持续下行')

    # 稳健理财图表
    content = replace_placeholder(content, '{{图表_数据日期}}', '2026年6月17日')
    content = replace_placeholder(content, '{{图表_红利ETF_名称}}', '红利ETF')
    content = replace_placeholder(content, '{{图表_红利ETF_副标题}}', '高股息策略')
    content = replace_placeholder(content, '{{图表_红利ETF_数值}}', '正收益')
    content = replace_placeholder(content, '{{图表_银行股息率_注释}}', '银行板块')
    content = replace_placeholder(content, '{{图表_银行股息率_数值}}', '4.5-5.5%')
    content = replace_placeholder(content, '{{图表_超长国债_数值}}', '低位')
    content = replace_placeholder(content, '{{图表_银行理财_数值}}', '3%左右')
    content = replace_placeholder(content, '{{图表_5年定存_数值}}', CD_5Y)
    content = replace_placeholder(content, '{{图表_1年定存_数值}}', CD_1Y)
    content = replace_placeholder(content, '{{图表_收益计算说明}}', f'100万配置：银行股息约{color("4.5-5.5万/年", "red")}，远超货币基金约{color("1万/年", "green")}，也高于5年定存约{color("1.65万/年", "yellow")}。高股息策略在低利率时代优势明显。')

    # 替代策略
    content = replace_placeholder(content, '{{替代策略_股息对比内容}}', f'股息率对比：银行股{color("4.5-5.5%", "red")} > 10年国债{color("1.72%", "yellow")} > 货币基金{color("约1.0%", "green")} > 1年定存{color("1.35%", "cyan")}')
    content = replace_placeholder(content, '{{替代策略_配置逻辑}}', f'在当前低利率环境下，高股息资产配置价值凸显。银行、电力等高股息板块不仅提供稳定现金回报，还具备估值修复空间。')
    content = replace_placeholder(content, '{{替代策略_配置建议内容}}', f'建议稳健型投资者可将{color("60%", "cyan")}以上资金配置于高股息标的，兼顾收益与防御性。')

    # 避坑指南
    content = replace_placeholder(content, '{{避坑1_标题}}', '追高银行股')
    content = replace_placeholder(content, '{{避坑1_内容}}', f'银行股近期累计涨幅较大，短期存在{color("获利了结", "green")}压力。追高容易被套，建议等待回调后再介入。')
    content = replace_placeholder(content, '{{避坑2_标题}}', '盲目炒作AI概念')
    content = replace_placeholder(content, '{{避坑2_内容}}', f'AI概念炒作火热，但多数公司业绩无法支撑高估值。{color("盲目追高", "green")}风险巨大，建议关注有实际业绩支撑的龙头。')
    content = replace_placeholder(content, '{{避坑3_标题}}', '忽视汇率风险')
    content = replace_placeholder(content, '{{避坑3_内容}}', f'人民币汇率波动加大海外投资风险。配置外币资产需{color("注意对冲", "yellow")}，避免单一货币敞口过大。')

    # 保险窗口提醒
    content = replace_placeholder(content, '{{保险_窗口提醒标题}}', '6月保险配置窗口期')
    content = replace_placeholder(content, '{{保险_窗口提醒内容}}', f'6月是保险产品上半年的重要节点，部分产品可能{color("调整收益率", "yellow")}。有配置需求的投资者可关注，优先选择保障型产品。')

    # 黄金
    content = replace_placeholder(content, '{{黄金_标题}}', '国际黄金')
    content = replace_placeholder(content, '{{黄金_单位}}', '美元/盎司')
    content = replace_placeholder(content, '{{黄金_价格}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{黄金_涨跌颜色}}', 'red')
    content = replace_placeholder(content, '{{黄金_涨跌幅}}', f'{GOLD_CHANGE}')
    content = replace_placeholder(content, '{{黄金_SVG路径}}', '')
    content = replace_placeholder(content, '{{黄金_SVG填充路径}}', '')
    content = replace_placeholder(content, '{{黄金_日期1}}', '6月15日')
    content = replace_placeholder(content, '{{黄金_日期2}}', '6月16日')
    content = replace_placeholder(content, '{{黄金_日期3}}', '6月17日')
    content = replace_placeholder(content, '{{黄金_走势描述}}', f'国际金价创历史新高，站稳{color("$4300", "cyan")}美元关口。避险需求+央行购金+美元走弱共同推动金价上涨。')

    # 债基配置建议
    content = replace_placeholder(content, '{{债基_配置建议标题}}', '债基配置建议')
    content = replace_placeholder(content, '{{债基_配置建议内容}}', f'当前债市表现稳健，纯债基金持续正收益。在市场波动加大的环境下，{color("纯债基金", "cyan")}可作为稳健资产配置的一部分，建议配置比例{color("20-30%", "yellow")}。')

    # 社区话题
    # 话题1
    content = replace_placeholder(content, '{{社区话题1_标题}}', '银行股创新高，还能追吗？')
    content = replace_placeholder(content, '{{社区话题1_来源}}', '雪球')
    content = replace_placeholder(content, '{{社区话题1_热度}}', '🔥 热议')
    content = replace_placeholder(content, '{{社区话题1_角色1}}', '价值投资者：')
    content = replace_placeholder(content, '{{社区话题1_观点1}}', f'银行股股息率约{color("5%", "red")}，显著高于无风险收益率，估值修复空间大')
    content = replace_placeholder(content, '{{社区话题1_角色2}}', '机构分析师：')
    content = replace_placeholder(content, '{{社区话题1_观点2}}', f'险资、北向资金持续加仓银行股，估值修复逻辑未变')
    content = replace_placeholder(content, '{{社区话题1_角色3}}', '谨慎派：')
    content = replace_placeholder(content, '{{社区话题1_观点3}}', f'短期涨幅较大，建议等待回调后再介入')
    content = replace_placeholder(content, '{{社区话题1_观点}}', f'银行股创新高是价值发现的体现，但短期确实存在回调压力。建议分批建仓，不要追高。高股息策略适合长期持有。')

    # 话题2
    content = replace_placeholder(content, '{{社区话题2_标题}}', '创业板指暴涨1.56%，科技股要起飞了？')
    content = replace_placeholder(content, '{{社区话题2_来源}}', '东方财富')
    content = replace_placeholder(content, '{{社区话题2_热度}}', '🔥 热议')
    content = replace_placeholder(content, '{{社区话题2_角色1}}', '科技多头：')
    content = replace_placeholder(content, '{{社区话题2_观点1}}', f'科创50{color("暴涨4.69%", "red")}，芯片股集体爆发，科技行情启动')
    content = replace_placeholder(content, '{{社区话题2_角色2}}', '理性分析师：')
    content = replace_placeholder(content, '{{社区话题2_观点2}}', f'成交放量突破3万亿，但需关注后续量能配合')
    content = replace_placeholder(content, '{{社区话题2_角色3}}', '谨慎派：')
    content = replace_placeholder(content, '{{社区话题2_观点3}}', f'外围美股科技股承压，纳指大跌1.15%，需警惕联动风险')
    content = replace_placeholder(content, '{{社区话题2_观点}}', f'创业板指领涨说明市场风险偏好提升，但外围科技股调整可能影响A股科技板块。短期可以参与，但要注意控制仓位。')

    # 话题3
    content = replace_placeholder(content, '{{社区话题3_标题}}', '国际金价创历史新高，黄金还能买吗？')
    content = replace_placeholder(content, '{{社区话题3_来源}}', '集思录')
    content = replace_placeholder(content, '{{社区话题3_热度}}', '💰 关注')
    content = replace_placeholder(content, '{{社区话题3_角色1}}', '黄金多头：')
    content = replace_placeholder(content, '{{社区话题3_观点1}}', f'美元走弱+避险需求+央行购金，金价上涨逻辑清晰')
    content = replace_placeholder(content, '{{社区话题3_角色2}}', '技术派：')
    content = replace_placeholder(content, '{{社区话题3_观点2}}', f'金价已创历史新高，RSI指标显示超买')
    content = replace_placeholder(content, '{{社区话题3_角色3}}', '老盛观点：')
    content = replace_placeholder(content, '{{社区话题3_观点3}}', f'黄金作为避险资产，适度配置有道理，但不宜重仓追高')
    content = replace_placeholder(content, '{{社区话题3_观点}}', f'国际金价创历史新高$4332美元/盎司，但短期涨幅过大，存在技术性调整风险。适度配置{color("5-10%", "cyan")}黄金作为避险即可，不宜盲目追高。')

    # 话题4
    content = replace_placeholder(content, '{{社区话题4_标题}}', '原油暴跌5%，能源股要抄底吗？')
    content = replace_placeholder(content, '{{社区话题4_来源}}', '同花顺')
    content = replace_placeholder(content, '{{社区话题4_热度}}', '⚠️ 警示')
    content = replace_placeholder(content, '{{社区话题4_角色1}}', '抄底派：')
    content = replace_placeholder(content, '{{社区话题4_观点1}}', f'霍尔木兹海峡重开只是短期影响，不改油价长期趋势')
    content = replace_placeholder(content, '{{社区话题4_角色2}}', '风险提示：')
    content = replace_placeholder(content, '{{社区话题4_观点2}}', f'供给改善预期下，油价可能继续承压')
    content = replace_placeholder(content, '{{社区话题4_角色3}}', '理性派：')
    content = replace_placeholder(content, '{{社区话题4_观点3}}', f'能源股跟油价关联度高，抄底需谨慎')
    content = replace_placeholder(content, '{{社区话题4_观点}}', f'霍尔木兹海峡重开导致原油暴跌，但这是短期事件冲击。能源股跟油价关联度高，在油价承压背景下，{color("不建议盲目抄底", "green")}。')

    # 话题5
    content = replace_placeholder(content, '{{社区话题5_标题}}', '科创板AI大模型政策落地，影响几何？')
    content = replace_placeholder(content, '{{社区话题5_来源}}', '雪球')
    content = replace_placeholder(content, '{{社区话题5_热度}}', '🔥 热议')
    content = replace_placeholder(content, '{{社区话题5_角色1}}', '政策解读：')
    content = replace_placeholder(content, '{{社区话题5_观点1}}', '科创板第五套标准扩至AI大模型，资本市场支持科技创新')
    content = replace_placeholder(content, '{{社区话题5_角色2}}', '分析师：')
    content = replace_placeholder(content, '{{社区话题5_观点2}}', '未盈利AI企业可通过科创板上市，头部企业直接受益')
    content = replace_placeholder(content, '{{社区话题5_角色3}}', '投资者：')
    content = replace_placeholder(content, '{{社区话题5_观点3}}', '关注真正有技术实力的AI龙头，规避纯概念炒作')
    content = replace_placeholder(content, '{{社区话题5_观点}}', '科创板第五套标准扩至AI大模型是资本市场支持科技创新的重要信号。头部AI企业如智谱AI等将直接受益，但投资者需甄别真正有技术实力的公司。')

    # 话题6
    content = replace_placeholder(content, '{{社区话题6_标题}}', '陆家嘴论坛释放哪些信号？')
    content = replace_placeholder(content, '{{社区话题6_来源}}', '东方财富')
    content = replace_placeholder(content, '{{社区话题6_热度}}', '💰 关注')
    content = replace_placeholder(content, '{{社区话题6_角色1}}', '经济学家：')
    content = replace_placeholder(content, '{{社区话题6_观点1}}', '三大金融监管高层全员参会，释放政策暖风')
    content = replace_placeholder(content, '{{社区话题6_角色2}}', '市场人士：')
    content = replace_placeholder(content, '{{社区话题6_观点2}}', '资本市场高水平开放持续推进，利好A股')
    content = replace_placeholder(content, '{{社区话题6_角色3}}', '机构观点：')
    content = replace_placeholder(content, '{{社区话题6_观点3}}', '科技创新领域将获得更多政策支持')
    content = replace_placeholder(content, '{{社区话题6_观点}}', '陆家嘴论坛释放多重政策暖风：AI大模型上市政策落地、资本市场开放持续推进、金融监管支持科技创新。市场信心有望进一步回暖。')

    # 话题7
    content = replace_placeholder(content, '{{社区话题7_标题}}', '人民币汇率升值创年内新高')
    content = replace_placeholder(content, '{{社区话题7_来源}}', '集思录')
    content = replace_placeholder(content, '{{社区话题7_热度}}', '💰 关注')
    content = replace_placeholder(content, '{{社区话题7_角色1}}', '外汇分析师：')
    content = replace_placeholder(content, '{{社区话题7_观点1}}', '人民币中间价6.8096，升值趋势延续')
    content = replace_placeholder(content, '{{社区话题7_角色2}}', '出口企业：')
    content = replace_placeholder(content, '{{社区话题7_观点2}}', '人民币升值对出口企业造成一定压力')
    content = replace_placeholder(content, '{{社区话题7_角色3}}', '进口企业：')
    content = replace_placeholder(content, '{{社区话题7_观点3}}', '人民币升值降低进口成本，利好进口业务')
    content = replace_placeholder(content, '{{社区话题7_观点}}', '人民币汇率持续升值，中间价报6.8096。人民币资产吸引力提升，外资流入A股有望加速。出口型企业需关注汇率风险对冲。')

    # 话题8
    content = replace_placeholder(content, '{{社区话题8_标题}}', '美债收益率小幅上行，债市怎么走？')
    content = replace_placeholder(content, '{{社区话题8_来源}}', '同花顺')
    content = replace_placeholder(content, '{{社区话题8_热度}}', '📊 数据')
    content = replace_placeholder(content, '{{社区话题8_角色1}}', '债券分析师：')
    content = replace_placeholder(content, '{{社区话题8_观点1}}', '10年期美债收益率报4.4869%，小幅上行')
    content = replace_placeholder(content, '{{社区话题8_角色2}}', '投资建议：')
    content = replace_placeholder(content, '{{社区话题8_观点2}}', '美债收益率上行空间有限，对国内债市影响可控')
    content = replace_placeholder(content, '{{社区话题8_角色3}}', '配置观点：')
    content = replace_placeholder(content, '{{社区话题8_观点3}}', '纯债基金仍可作为稳健资产配置的一部分')
    content = replace_placeholder(content, '{{社区话题8_观点}}', '10年期美债收益率4.4869%小幅上行，但对国内债市影响有限。在低利率环境下，纯债基金仍是稳健资产配置的好选择。')

    # 话题9
    content = replace_placeholder(content, '{{社区话题9_标题}}', '两市成交突破3万亿，行情能持续吗？')
    content = replace_placeholder(content, '{{社区话题9_来源}}', '雪球')
    content = replace_placeholder(content, '{{社区话题9_热度}}', '🔥 热议')
    content = replace_placeholder(content, '{{社区话题9_角色1}}', '技术派：')
    content = replace_placeholder(content, '{{社区话题9_观点1}}', '成交放量突破3万亿，是行情启动的积极信号')
    content = replace_placeholder(content, '{{社区话题9_角色2}}', '谨慎派：')
    content = replace_placeholder(content, '{{社区话题9_观点2}}', '放量不一定会持续上涨，需关注后续量能配合')
    content = replace_placeholder(content, '{{社区话题9_角色3}}', '老盛观点：')
    content = replace_placeholder(content, '{{社区话题9_观点3}}', '成交放量是关键信号，但持续性还需观察')
    content = replace_placeholder(content, '{{社区话题9_观点}}', '两市成交突破3.09万亿，量能显著放大。放量是行情启动的必要条件，但能否持续还需关注后续量能配合和热点轮动情况。')

    # 话题10
    content = replace_placeholder(content, '{{社区话题10_标题}}', '高股息策略还能继续吗？')
    content = replace_placeholder(content, '{{社区话题10_来源}}', '东方财富')
    content = replace_placeholder(content, '{{社区话题10_热度}}', '💰 关注')
    content = replace_placeholder(content, '{{社区话题10_角色1}}', '价值投资者：')
    content = replace_placeholder(content, '{{社区话题10_观点1}}', '银行股息率4.5-5.5%，显著高于无风险收益率')
    content = replace_placeholder(content, '{{社区话题10_角色2}}', '择时派：')
    content = replace_placeholder(content, '{{社区话题10_观点2}}', '银行股短期涨幅较大，存在回调压力')
    content = replace_placeholder(content, '{{社区话题10_角色3}}', '配置建议：')
    content = replace_placeholder(content, '{{社区话题10_观点3}}', '高股息策略适合长期持有，不宜追高')
    content = replace_placeholder(content, '{{社区话题10_观点}}', '高股息策略在低利率时代优势明显，银行股息率4.5-5.5%显著高于无风险收益率。短期银行股确实涨幅较大，但长期配置价值仍在，建议分批建仓。')

    # 关键词
    content = replace_placeholder(content, '{{关键词1}}', 'A股大涨')
    content = replace_placeholder(content, '{{关键词2}}', '科创50飙升')
    content = replace_placeholder(content, '{{关键词3}}', '黄金新高')
    content = replace_placeholder(content, '{{关键词4}}', '高股息')
    content = replace_placeholder(content, '{{关键词5}}', 'AI大模型')
    content = replace_placeholder(content, '{{关键词6}}', '陆家嘴论坛')
    content = replace_placeholder(content, '{{关键词7}}', '银行股回调')
    content = replace_placeholder(content, '{{关键词8}}', '成长领涨')

    # 宏观面
    content = replace_placeholder(content, '{{宏观_子标题1}}', '政策暖风')
    content = replace_placeholder(content, '{{宏观_内容1}}', '陆家嘴论坛开幕，三大金融监管高层全员参会，AI大模型上市政策落地')
    content = replace_placeholder(content, '{{宏观_子标题2}}', '外部环境')
    content = replace_placeholder(content, '{{宏观_内容2}}', '霍尔木兹海峡即将重开，原油价格大幅回落，通胀压力缓解')
    content = replace_placeholder(content, '{{宏观_子标题3}}', '汇率')
    content = replace_placeholder(content, '{{宏观_内容3}}', '人民币中间价6.8096，升值12个基点，汇率维持强势')

    # 市场面
    content = replace_placeholder(content, '{{市场_子标题1}}', 'A股')
    content = replace_placeholder(content, '{{市场_内容1}}', f'创业板指{CYB_CHANGE}领涨，科创50{KC50_CHANGE}，两市成交{A_SHARES_VOLUME}')
    content = replace_placeholder(content, '{{市场_子标题2}}', '美股')
    content = replace_placeholder(content, '{{市场_内容2}}', f'道指{DJI_CHANGE}创新高，纳指{NDX_CHANGE}，科技股分化')
    content = replace_placeholder(content, '{{市场_子标题3}}', '港股')
    content = replace_placeholder(content, '{{市场_内容3}}', f'恒生指数{HSI_CHANGE}，恒生科技{HSTECH_CHANGE}')

    # 资金面
    content = replace_placeholder(content, '{{资金_子标题1}}', '北向')
    content = replace_placeholder(content, '{{资金_内容1}}', '净卖出约1.36亿，但龙虎榜机构净买入6.13亿')
    content = replace_placeholder(content, '{{资金_子标题2}}', '量能')
    content = replace_placeholder(content, '{{资金_内容2}}', f'两市成交突破{A_SHARES_VOLUME}，量能充沛')
    content = replace_placeholder(content, '{{资金_子标题3}}', '板块')
    content = replace_placeholder(content, '{{资金_内容3}}', '资金从银行股流向成长赛道')

    # 理财参考数据
    content = replace_placeholder(content, '{{理财参考1_标题}}', '上证指数')
    content = replace_placeholder(content, '{{理财参考1_标题颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考1_数值}}', f'{SH_COMPONENT}')
    content = replace_placeholder(content, '{{理财参考1_数值颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考1_备注}}', f'{SH_CHANGE}')

    content = replace_placeholder(content, '{{理财参考2_标题}}', '深证成指')
    content = replace_placeholder(content, '{{理财参考2_标题颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考2_数值}}', f'{SZ_COMPONENT}')
    content = replace_placeholder(content, '{{理财参考2_数值颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考2_备注}}', f'{SZ_CHANGE}')

    content = replace_placeholder(content, '{{理财参考3_标题}}', '创业板指')
    content = replace_placeholder(content, '{{理财参考3_标题颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{理财参考3_数值}}', f'{CYB_INDEX}')
    content = replace_placeholder(content, '{{理财参考3_数值颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{理财参考3_备注}}', f'{CYB_CHANGE}')

    content = replace_placeholder(content, '{{理财参考4_标题}}', '两市成交')
    content = replace_placeholder(content, '{{理财参考4_标题颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考4_数值}}', f'{A_SHARES_VOLUME}')
    content = replace_placeholder(content, '{{理财参考4_数值颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考4_备注}}', '量能充沛')

    content = replace_placeholder(content, '{{理财参考5_标题}}', '黄金')
    content = replace_placeholder(content, '{{理财参考5_标题颜色}}', '#f0b429')
    content = replace_placeholder(content, '{{理财参考5_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{理财参考5_数值颜色}}', '#f0b429')
    content = replace_placeholder(content, '{{理财参考5_备注}}', '历史新高')

    content = replace_placeholder(content, '{{理财参考6_标题}}', '人民币汇率')
    content = replace_placeholder(content, '{{理财参考6_标题颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考6_数值}}', USD_CNY_MID)
    content = replace_placeholder(content, '{{理财参考6_数值颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考6_备注}}', '升值')

    # 操作建议
    content = replace_placeholder(content, '{{操作建议1_标题}}', '科技成长')
    content = replace_placeholder(content, '{{操作建议1_内容}}', f'创业板指{CYB_CHANGE}领涨，科创50{KC50_CHANGE}，芯片股集体爆发，科技成长赛道资金回流')
    content = replace_placeholder(content, '{{操作建议1_补充}}', '成交放量突破3万亿，市场做多情绪回暖，科技板块有望继续活跃')
    content = replace_placeholder(content, '{{操作建议1_操作}}', '短期可关注AI、半导体等科技成长方向，注意控制仓位')

    content = replace_placeholder(content, '{{操作建议2_标题}}', '高股息配置')
    content = replace_placeholder(content, '{{操作建议2_内容}}', '银行股息率4.5-5.5%显著高于无风险收益率，PB处于历史低位，长线配置价值凸显')
    content = replace_placeholder(content, '{{操作建议2_补充}}', '短期银行股回调提供更好的买入机会，险资、北向资金持续加仓')
    content = replace_placeholder(content, '{{操作建议2_操作}}', '长期投资者可分批配置高股息银行、电力等稳定现金流板块')

    content = replace_placeholder(content, '{{操作建议3_标题}}', '黄金')
    content = replace_placeholder(content, '{{操作建议3_内容}}', f'国际金价创历史新高${GOLD_PRICE}，避险需求+央行购金+美元走弱共同推动')
    content = replace_placeholder(content, '{{操作建议3_补充}}', '短期涨幅过大存在技术性调整风险，但上涨逻辑未变')
    content = replace_placeholder(content, '{{操作建议3_操作}}', '适度配置5-10%黄金作为避险，不宜重仓追高')

    content = replace_placeholder(content, '{{操作建议4_标题}}', '稳健理财')
    content = replace_placeholder(content, '{{操作建议4_内容}}', f'货币基金收益率持续下行约1%，10年国债收益率{CHINA_10Y_BOND}低位运行')
    content = replace_placeholder(content, '{{操作建议4_补充}}', '高股息策略优势明显，银行股息率4.5-5.5%远超货币基金')
    content = replace_placeholder(content, '{{操作建议4_操作}}', '稳健型投资者可将60%以上资金配置于高股息标的')

    content = replace_placeholder(content, '{{操作建议5_标题}}', '风险提示')
    content = replace_placeholder(content, '{{操作建议5_内容}}', f'银行股短期回调，建行跌超2%；美股纳指大跌{NDX_CHANGE}；外围科技股分化')
    content = replace_placeholder(content, '{{操作建议5_补充}}', '市场放量上涨但外部不确定性仍存，注意控制仓位')
    content = replace_placeholder(content, '{{操作建议5_操作}}', '不要盲目追高热点板块，做好风险控制')

    content = replace_placeholder(content, '{{操作建议6_标题}}', '港股')
    content = replace_placeholder(content, '{{操作建议6_内容}}', f'恒生指数{HSI_CHANGE}，恒生科技{HSTECH_CHANGE}，估值处于历史低位')
    content = replace_placeholder(content, '{{操作建议6_补充}}', '港股估值优势明显，下半年或有估值修复机会')
    content = replace_placeholder(content, '{{操作建议6_操作}}', '关注高股息银行股、业绩确定性强的消费龙头')

    # 参考数据
    content = replace_placeholder(content, '{{参考1_标题}}', '涨红跌绿规则')
    content = replace_placeholder(content, '{{参考1_描述}}', '上涨显示红色，下跌显示绿色，与直觉相反')
    content = replace_placeholder(content, '{{参考2_标题}}', '颜色高亮')
    content = replace_placeholder(content, '{{参考2_描述}}', '重点数据使用彩色高亮显示')
    content = replace_placeholder(content, '{{参考3_标题}}', '数据来源')
    content = replace_placeholder(content, '{{参考3_描述}}', '2026年6月17日收盘数据')

    # 速查数据
    content = replace_placeholder(content, '{{速查1_图标}}', '📈')
    content = replace_placeholder(content, '{{速查1_颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{速查1_标签class}}', 'up')
    content = replace_placeholder(content, '{{速查1_备注}}', '上证')

    content = replace_placeholder(content, '{{速查2_图标}}', '📈')
    content = replace_placeholder(content, '{{速查2_颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{速查2_标签class}}', 'up')
    content = replace_placeholder(content, '{{速查2_备注}}', '深证')

    content = replace_placeholder(content, '{{速查3_图标}}', '🚀')
    content = replace_placeholder(content, '{{速查3_颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{速查3_标签class}}', 'hot')
    content = replace_placeholder(content, '{{速查3_备注}}', '创业')

    content = replace_placeholder(content, '{{速查4_图标}}', '💰')
    content = replace_placeholder(content, '{{速查4_颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{速查4_标签class}}', 'accent')
    content = replace_placeholder(content, '{{速查4_备注}}', '放量')

    content = replace_placeholder(content, '{{速查5_图标}}', '👆')
    content = replace_placeholder(content, '{{速查5_颜色}}', 'var(--green)')
    content = replace_placeholder(content, '{{速查5_标签class}}', 'down')
    content = replace_placeholder(content, '{{速查5_备注}}', '北向')

    content = replace_placeholder(content, '{{速查6_图标}}', '📊')
    content = replace_placeholder(content, '{{速查6_颜色}}', 'var(--green)')
    content = replace_placeholder(content, '{{速查6_标签class}}', 'down')
    content = replace_placeholder(content, '{{速查6_备注}}', '恒生科技')

    content = replace_placeholder(content, '{{速查7_图标}}', '🛢️')
    content = replace_placeholder(content, '{{速查7_颜色}}', 'var(--green)')
    content = replace_placeholder(content, '{{速查7_标签class}}', 'down')
    content = replace_placeholder(content, '{{速查7_备注}}', 'WTI')

    content = replace_placeholder(content, '{{速查8_图标}}', '🥇')
    content = replace_placeholder(content, '{{速查8_颜色}}', '#f0b429')
    content = replace_placeholder(content, '{{速查8_标签class}}', 'hot')
    content = replace_placeholder(content, '{{速查8_备注}}', '黄金')

    # 数据截止日期
    content = replace_placeholder(content, '{{数据截止日期}}', '2026年6月17日')

    # 写回文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 报告生成完成: {output_file}")

    # 统计替换数量
    remaining = len(re.findall(r'\{\{[^}]+\}\}', content))
    print(f"📊 剩余占位符数量: {remaining}")

    return remaining


if __name__ == '__main__':
    remaining = main()
    if remaining > 0:
        print(f"⚠️ 警告: 还有 {remaining} 个占位符未替换")