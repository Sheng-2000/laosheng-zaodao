#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道 2026年6月19日 报告生成脚本
数据基准：2026年6月18日（周四，A股端午节前最近收盘日）收盘数据
"""

import re
import shutil
from pathlib import Path

# ========== 路径配置 ==========
BASE_DIR = Path('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道')
TEMPLATE_FILE = BASE_DIR / 'template.html'
OUTPUT_FILE = BASE_DIR / '老盛早知道_20260619.html'

# ========== 日期配置 ==========
TODAY = "2026年6月19日"
DATE_FORMATTED = "2026/06/19"
WEEKDAY = "星期五"
DATA_DATE = "6月18日"
DATA_DATE_FULL = "2026年6月18日"

# ========== 颜色高亮工具 ==========
def color(text, color_type):
    """添加颜色高亮"""
    colors = {
        'red': '#f85149',      # 上涨/利好/正面
        'green': '#3fb950',    # 下跌/利空/负面
        'cyan': '#00d4ff',     # 数字/数据
        'yellow': '#f0b429',   # 警示/关注
        'purple': '#bc8cff',   # AI/科技
        'orange': '#ffa657',   # 地缘/政策
    }
    return f'<span style="color:{colors.get(color_type, color_type)};font-weight:700;">{text}</span>'


def span_class(text, cls):
    """生成带 up/down/neutral class 的 span"""
    return f'<span class="{cls}">{text}</span>'


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def replace_placeholder(content, placeholder, value):
    """替换占位符"""
    pattern = re.compile(re.escape(placeholder))
    return pattern.sub(str(value), content)


# ========== 核心市场数据（2026-06-18 收盘） ==========
# A股
SH_COMPONENT = "4090.48"
SH_CHANGE = "-0.43%"
SZ_COMPONENT = "16030.70"
SZ_CHANGE = "+0.94%"
CYB_INDEX = "4252.39"
CYB_CHANGE = "+2.05%"
KC50_INDEX = "1911.51"
KC50_CHANGE = "+3.84%"
HS300_INDEX = "4941.60"
HS300_CHANGE = "+0.21%"
A_SHARES_VOLUME = "3.11万亿"
A_SHARES_UP_DOWN = "跌多涨少（约3400家下跌）"
A_NORTHBOUND = "净流入42.68亿元"

# 美股
DJI_INDEX = "51492.55"
DJI_CHANGE = "-0.98%"
SPX_INDEX = "7420.10"
SPX_CHANGE = "-1.21%"
NDX_INDEX = "26021.66"
NDX_CHANGE = "-1.34%"
NVDA_CHANGE = "-1.33%"
TSLA_CHANGE = "-2.05%"
ARM_CHANGE = "+5.0%"

# 港股
HSI_INDEX = "23924.81"
HSI_CHANGE = "-1.59%"
HSTECH_INDEX = "4604.35"
HSTECH_CHANGE = "-1.39%"
HSCEI_INDEX = "7976.04"
HSCEI_CHANGE = "-2.06%"
H_SOUTHBOUND = "净卖出67.92亿元"

# 亚太
NI225_INDEX = "71250.06"
NI225_CHANGE = "+0.28%"
KOSPI_INDEX = "9097.95"
KOSPI_CHANGE = "+0.38%"
TAIWAN_INDEX = "46465.20"
TAIWAN_CHANGE = "+1.28%"
INDIA_INDEX = "76754.52"
INDIA_CHANGE = "-0.85%"
ASX_INDEX = "8821.70"
ASX_CHANGE = "-1.00%"

# 欧洲
UK100_INDEX = "10399.70"
UK100_CHANGE = "-1.04%"
DAX30_INDEX = "25026.80"
DAX30_CHANGE = "+0.37%"
CAC40_INDEX = "8467.98"
CAC40_CHANGE = "+0.44%"
STOXX50_INDEX = "6323.28"
STOXX50_CHANGE = "+0.37%"

# 大宗商品
WTI_OIL = "74.81"
WTI_CHANGE = "-0.27%"
BRENT_OIL = "78.16"
BRENT_CHANGE = "-0.50%"
GOLD_PRICE = "4297.65"
GOLD_CHANGE = "+0.47%"
SH_GOLD = "939"
SILVER_PRICE = "67.88"
SILVER_CHANGE = "-2.89%"

# 加密货币
BTC_PRICE = "64500"
BTC_CHANGE = "-4.2%"
ETH_PRICE = "2080"
ETH_CHANGE = "-6.0%"
BTC_ETF_FLOW = "净流出"
CRYPTO_SENTIMENT = "谨慎偏空"

# 汇率债券
USD_CNY_MID = "6.8130"
USD_CNY_ONSHORE = "6.77"
USD_INDEX = "100.38"
USD_INDEX_CHANGE = "+0.87%"
US_10Y = "4.46%"
US_30Y = "4.90%"
CN_10Y = "1.73%"

# 存款利率与理财
CD_1Y = "1.35%"
CD_3Y = "1.55%"
CD_5Y = "1.65%"
MMF_YIELD = "约1.0%"
PURE_BOND_YIELD = "正收益"

# ========== 关注标的（2026-06-18） ==========
STOCKS = [
    {"code": "601398", "name": "工商银行", "price": "7.16", "change": "+0.13%", "pb": "0.65"},
    {"code": "601939", "name": "建设银行", "price": "9.92", "change": "+0.04%", "pb": "0.73"},
    {"code": "601288", "name": "农业银行", "price": "6.37", "change": "+0.10%", "pb": "0.79"},
    {"code": "600036", "name": "招商银行", "price": "37.26", "change": "+0.40%", "pb": "0.83"},
    {"code": "002142", "name": "宁波银行", "price": "30.78", "change": "+0.63%", "pb": "0.87"},
    {"code": "600919", "name": "江苏银行", "price": "11.22", "change": "+0.61%", "pb": "0.78"},
    {"code": "600926", "name": "杭州银行", "price": "15.64", "change": "+0.57%", "pb": "0.81"},
    {"code": "601963", "name": "重庆银行", "price": "10.85", "change": "+0.35%", "pb": "0.66"},
    {"code": "600900", "name": "长江电力", "price": "26.66", "change": "+0.53%", "pb": "2.86"},
    {"code": "601006", "name": "大秦铁路", "price": "4.94", "change": "+0.37%", "pb": "0.60"},
    {"code": "600941", "name": "中国移动", "price": "91.65", "change": "+0.04%", "pb": "1.40"},
    {"code": "601985", "name": "中国核电", "price": "9.12", "change": "+0.81%", "pb": "1.56"},
    {"code": "601318", "name": "中国平安", "price": "49.38", "change": "+1.20%", "pb": "0.88"},
]


def change_class(change_str):
    """根据涨跌幅字符串返回 up/down/neutral"""
    if change_str.startswith('+'):
        return 'up'
    elif change_str.startswith('-'):
        return 'down'
    return 'neutral'


def market_block_border(rows):
    """根据 block 内多数涨跌决定边框颜色"""
    ups = sum(1 for r in rows if r.startswith('+'))
    downs = sum(1 for r in rows if r.startswith('-'))
    if ups > downs:
        return '#f85149'
    elif downs > ups:
        return '#3fb950'
    return 'rgba(255,255,255,0.12)'


# ========== 主生成流程 ==========
def main():
    # 1. 复制模板
    shutil.copy(TEMPLATE_FILE, OUTPUT_FILE)
    content = read_file(OUTPUT_FILE)

    # 2. Header 信息
    content = replace_placeholder(content, '{{报告日期}}', TODAY)
    content = replace_placeholder(content, '{{YYYY/MM/DD}}', DATE_FORMATTED)
    content = replace_placeholder(content, '{{星期}}', WEEKDAY)
    content = replace_placeholder(content, '{{每日重点事件}}', '美联储放鹰 | 算力链涨停 | 霍尔木兹重开')

    # Header ticker
    content = replace_placeholder(content, '{{ticker_上证_数值}}', SH_COMPONENT)
    content = replace_placeholder(content, '{{ticker_上证_涨跌幅}}', span_class(SH_CHANGE, 'down'))
    content = replace_placeholder(content, '{{ticker_道指_数值}}', DJI_INDEX)
    content = replace_placeholder(content, '{{ticker_道指_涨跌幅}}', span_class(DJI_CHANGE, 'down'))
    content = replace_placeholder(content, '{{ticker_黄金_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{ticker_黄金_涨跌幅}}', span_class(GOLD_CHANGE, 'up'))

    # 3. Tab 0: 要点速览
    content = replace_placeholder(content, '{{概览卡1_标题}}', 'A股分化调整')
    content = replace_placeholder(content, '{{概览卡1_数值}}', f'{SH_COMPONENT}点')
    content = replace_placeholder(content, '{{概览卡1_涨跌class}}', 'down')
    content = replace_placeholder(content, '{{概览卡1_涨跌幅}}', SH_CHANGE)
    content = replace_placeholder(content, '{{概览卡1_描述}}',
        f'上证{SH_CHANGE}，深证{SZ_CHANGE}，创业板{color(CYB_CHANGE, "red")}，科创50{color(KC50_CHANGE, "red")}，两市成交{color(A_SHARES_VOLUME, "cyan")}')

    content = replace_placeholder(content, '{{概览卡2_标题}}', '市场成交')
    content = replace_placeholder(content, '{{概览卡2_数值}}', A_SHARES_VOLUME)
    content = replace_placeholder(content, '{{概览卡2_标签}}', '量能充沛')
    content = replace_placeholder(content, '{{概览卡2_描述}}',
        f'创业板指{color("大涨2.05%", "red")}领涨，科创50飙升{color("3.84%", "red")}，算力硬件链批量涨停')

    content = replace_placeholder(content, '{{概览卡3_标题}}', '美股尾盘跳水')
    content = replace_placeholder(content, '{{概览卡3_数值}}', f'纳斯达克{NDX_CHANGE}')
    content = replace_placeholder(content, '{{概览卡3_标签}}', '科技股承压')
    content = replace_placeholder(content, '{{概览卡3_描述}}',
        f'道指{color(DJI_CHANGE, "green")}，标普500{color(SPX_CHANGE, "green")}，纳指{color(NDX_CHANGE, "green")}，英伟达跌1.33%')

    content = replace_placeholder(content, '{{概览卡4_标题}}', '黄金反弹')
    content = replace_placeholder(content, '{{概览卡4_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{概览卡4_标签}}', '震荡反弹')
    content = replace_placeholder(content, '{{概览卡4_描述}}',
        f'国际金价反弹{color(GOLD_CHANGE, "red")}，上海金约{color(SH_GOLD + "元/克", "cyan")}，白银{color(SILVER_CHANGE, "green")}')

    # 8张要点卡片
    content = replace_placeholder(content, '{{要点1_标题}}', 'A股极致分化')
    content = replace_placeholder(content, '{{要点1_内容}}',
        f'上证指数{color(SH_CHANGE, "green")}微跌，但创业板指{color(CYB_CHANGE, "red")}大涨，科创50{color(KC50_CHANGE, "red")}飙升，算力硬件链批量涨停，科技成长资金回流明显，而全市场约{color("3400家下跌", "green")}，结构性行情极致演绎。')

    content = replace_placeholder(content, '{{要点2_标题}}', '北向资金回流')
    content = replace_placeholder(content, '{{要点2_内容}}',
        f'6月18日北向资金{color(A_NORTHBOUND, "red")}，结束连续流出态势，加仓方向集中在{color("半导体、算力、光通信硬件", "purple")}等科技成长板块，显示外资对A股科技资产的偏好回升。')

    content = replace_placeholder(content, '{{要点3_标题}}', '美联储放鹰')
    content = replace_placeholder(content, '{{要点3_内容}}',
        f'美联储新任主席沃什释放{color("鹰派信号", "green")}，美股尾盘高台跳水，道指跌近1%，纳指跌1.34%。市场对美联储降息预期再度降温，美元指数{color(USD_INDEX_CHANGE, "red")}大涨至{color(USD_INDEX, "cyan")}。')

    content = replace_placeholder(content, '{{要点4_标题}}', '美伊签署临时协议')
    content = replace_placeholder(content, '{{要点4_内容}}',
        f'美伊签署临时协议，霍尔木兹海峡有望重开，原油、航运等地缘风险预期降温，WTI原油{color(WTI_CHANGE, "green")}，布伦特原油{color(BRENT_CHANGE, "green")}，全球能源供给预期改善。')

    content = replace_placeholder(content, '{{要点5_标题}}', 'AI IPO竞速')
    content = replace_placeholder(content, '{{要点5_内容}}',
        f'{color("OpenAI与Anthropic", "purple")}先后提交IPO申请，竞逐2026年秋季上市窗口，AI算力基础设施板块估值体系面临重塑，龙头公司融资能力提升。')

    content = replace_placeholder(content, '{{要点6_标题}}', '华为HDC 2026')
    content = replace_placeholder(content, '{{要点6_内容}}',
        f'华为HDC 2026大会召开，{color("HarmonyOS 7", "purple")}进入Agent时代，发布{color("openPangu 2.0", "purple")}，端侧AI、AI医疗、自动驾驶等应用场景持续落地，中国AI大模型连续六周全球调用量领先美国。')

    content = replace_placeholder(content, '{{要点7_标题}}', '高股息银行抗跌')
    content = replace_placeholder(content, '{{要点7_内容}}',
        f'市场调整中银行、电力等高股息板块逆势飘红，工商银行涨0.13%、招商银行涨0.40%、长江电力涨0.53%，低估值高股息配置价值在震荡市中进一步凸显。')

    content = replace_placeholder(content, '{{要点8_标题}}', '汇率与债市')
    content = replace_placeholder(content, '{{要点8_内容}}',
        f'USD/CNY中间价报{color(USD_CNY_MID, "cyan")}，美元/人民币{color("上调34个基点", "green")}；在岸汇率约{color(USD_CNY_ONSHORE, "cyan")}；中10年期国债收益率{color(CN_10Y, "cyan")}维持低位，纯债基金保持正收益。')

    # 时间线
    content = replace_placeholder(content, '{{时间线1_日}}', '19')
    content = replace_placeholder(content, '{{时间线1_月}}', '6月')
    content = replace_placeholder(content, '{{时间线1_标签}}', '今日')
    content = replace_placeholder(content, '{{时间线1_事件}}', '端午节假期')
    content = replace_placeholder(content, '{{时间线1_详情}}', 'A股休市，关注港股及海外市场波动，防范节日期间外围风险')

    content = replace_placeholder(content, '{{时间线2_日}}', '22')
    content = replace_placeholder(content, '{{时间线2_月}}', '6月')
    content = replace_placeholder(content, '{{时间线2_标签}}', '周一')
    content = replace_placeholder(content, '{{时间线2_事件}}', 'A股节后开盘')
    content = replace_placeholder(content, '{{时间线2_详情}}', '关注端午期间外围市场及霍尔木兹海峡进展对A股情绪影响')

    content = replace_placeholder(content, '{{时间线3_日}}', '23')
    content = replace_placeholder(content, '{{时间线3_月}}', '6月')
    content = replace_placeholder(content, '{{时间线3_标签}}', '数据')
    content = replace_placeholder(content, '{{时间线3_事件}}', 'LPR报价')
    content = replace_placeholder(content, '{{时间线3_详情}}', '贷款市场报价利率公布，降息预期持续受到关注')

    content = replace_placeholder(content, '{{时间线4_日}}', '30')
    content = replace_placeholder(content, '{{时间线4_月}}', '6月')
    content = replace_placeholder(content, '{{时间线4_标签}}', '月末')
    content = replace_placeholder(content, '{{时间线4_事件}}', '半年末考核')
    content = replace_placeholder(content, '{{时间线4_详情}}', '银行季末考核，市场流动性或阶段性收紧')

    # 4. Tab 1: 国内外新闻
    content = replace_placeholder(content, '{{重点新闻1_标签和标题}}',
        '<span class="tag tag-finance">📊 政策</span>OpenAI与Anthropic提交IPO申请')
    content = replace_placeholder(content, '{{重点新闻1_正文}}',
        f'{color("OpenAI", "purple")}与{color("Anthropic", "purple")}先后向美国SEC提交IPO申请，竞逐2026年秋季上市窗口。这标志着AI产业从融资驱动迈向公开市场，将重塑科技板块估值体系。机构认为，AI算力基础设施、光模块、半导体等硬件环节将直接受益于头部AI企业资本开支扩张，但短期也需警惕{color("估值透支", "green")}风险。')

    content = replace_placeholder(content, '{{重点新闻2_标签和标题}}',
        '<span class="tag tag-geo">🌍 地缘</span>美伊签署临时协议 霍尔木兹海峡有望重开')
    content = replace_placeholder(content, '{{重点新闻2_正文}}',
        f'美伊签署临时协议，霍尔木兹海峡有望在近期实现全面开放，原油、航运等地缘风险预期显著降温。消息公布后，WTI原油{color(WTI_CHANGE, "green")}至{color(WTI_OIL + "美元", "cyan")}，布伦特原油{color(BRENT_CHANGE, "green")}至{color(BRENT_OIL + "美元", "cyan")}。地缘缓和有助于降低全球通胀压力，但也意味着能源板块的{color("供给溢价", "green")}回落。')

    content = replace_placeholder(content, '{{重点新闻3_标签和标题}}',
        '<span class="tag tag-finance">🏦 市场</span>A股极致分化：创业板大涨2% 科创50飙升3.84%')
    content = replace_placeholder(content, '{{重点新闻3_正文}}',
        f'6月18日A股呈现极致分化格局：上证指数{color(SH_CHANGE, "green")}，深证成指{color(SZ_CHANGE, "red")}，创业板指{color(CYB_CHANGE, "red")}，科创50{color(KC50_CHANGE, "red")}。两市成交额约{color(A_SHARES_VOLUME, "cyan")}，算力硬件链批量涨停，但全市场约{color("3400家下跌", "green")}，结构性强弱分明。')

    content = replace_placeholder(content, '{{重点新闻4_标签和标题}}',
        '<span class="tag tag-finance">💰 资金</span>北向资金净流入42.68亿元')
    content = replace_placeholder(content, '{{重点新闻4_正文}}',
        f'6月18日北向资金{color(A_NORTHBOUND, "red")}，结束此前连续流出态势。从资金流向看，外资加仓方向集中在{color("半导体、算力、光通信硬件", "purple")}等科技成长板块，而对部分传统蓝筹维持减持。北向回流有助于提振市场风险偏好，但持续性仍需观察外围流动性环境。')

    content = replace_placeholder(content, '{{重点新闻5_标签和标题}}',
        '<span class="tag tag-finance">📉 宏观</span>美联储新任主席沃什释放鹰派信号')
    content = replace_placeholder(content, '{{重点新闻5_正文}}',
        f'美联储新任主席沃什（Warsh）释放{color("鹰派信号", "green")}，强调通胀仍高于目标，货币政策将保持谨慎。美股尾盘高台跳水，道指{color(DJI_CHANGE, "green")}，标普500{color(SPX_CHANGE, "green")}，纳斯达克{color(NDX_CHANGE, "green")}。美元指数{color(USD_INDEX_CHANGE, "red")}大涨至{color(USD_INDEX, "cyan")}，日元跌至2024年7月以来新低。')

    # 地缘新闻
    content = replace_placeholder(content, '{{地缘新闻1_标签和标题}}',
        '<span class="tag tag-geo">🛢️ 能源</span>霍尔木兹重开预期 油价承压')
    content = replace_placeholder(content, '{{地缘新闻1_正文}}',
        f'霍尔木兹海峡重开预期升温，全球能源运输风险大幅下降。WTI原油{color(WTI_CHANGE, "green")}报{color(WTI_OIL + "美元/桶", "cyan")}，布伦特原油{color(BRENT_CHANGE, "green")}报{color(BRENT_OIL + "美元/桶", "cyan")}。航运保险费回落，全球供应链稳定性提升，但能源股短期面临盈利预期下修压力。')

    content = replace_placeholder(content, '{{地缘新闻2_标签和标题}}',
        '<span class="tag tag-geo">🌐 中东</span>美元指数大涨 日元创新低')
    content = replace_placeholder(content, '{{地缘新闻2_正文}}',
        f'美联储鹰派信号推动美元指数{color(USD_INDEX_CHANGE, "red")}升至{color(USD_INDEX, "cyan")}，日元兑美元跌至2024年7月以来新低。地缘风险降温叠加美元走强，新兴市场货币普遍承压，全球资金流向避险资产和高股息防御板块。')

    # 财经新闻
    content = replace_placeholder(content, '{{财经新闻1_标签和标题}}',
        '<span class="tag tag-finance">📈 美股</span>三大指数集体收跌')
    content = replace_placeholder(content, '{{财经新闻1_正文}}',
        f'美股三大指数集体收跌：道指{color(DJI_CHANGE, "green")}报{color(DJI_INDEX, "cyan")}，标普500{color(SPX_CHANGE, "green")}报{color(SPX_INDEX, "cyan")}，纳斯达克{color(NDX_CHANGE, "green")}报{color(NDX_INDEX, "cyan")}。英伟达{color(NVDA_CHANGE, "green")}，特斯拉{color(TSLA_CHANGE, "green")}，ARM逆市{color(ARM_CHANGE, "red")}。科技股承压反映市场对高估值AI资产的担忧。')

    content = replace_placeholder(content, '{{财经新闻2_标签和标题}}',
        '<span class="tag tag-finance">🏦 银行</span>高股息银行逆势上涨')
    content = replace_placeholder(content, '{{财经新闻2_正文}}',
        f'市场调整中，高股息银行股展现防御属性：工商银行涨0.13%、建设银行涨0.04%、农业银行涨0.10%、招商银行涨0.40%。银行板块PB约{color("0.6-0.8倍", "cyan")}，股息率{color("4.5-5.5%", "red")}，在低利率环境下配置价值突出，险资与长线资金持续加仓。')

    content = replace_placeholder(content, '{{财经新闻3_标签和标题}}',
        '<span class="tag tag-finance">💱 汇率</span>人民币中间价下调34个基点')
    content = replace_placeholder(content, '{{财经新闻3_正文}}',
        f'银行间外汇市场人民币对美元中间价报{color(USD_CNY_MID, "cyan")}，美元/人民币{color("上调34个基点", "green")}（即人民币贬值）。在岸汇率约{color(USD_CNY_ONSHORE, "cyan")}。人民币贬值对出口企业形成一定利好，但可能加大进口成本和资本外流压力，需关注后续央行稳汇率信号。')

    content = replace_placeholder(content, '{{财经新闻4_标签和标题}}',
        '<span class="tag tag-energy">🥇 黄金</span>黄金震荡反弹0.47%')
    content = replace_placeholder(content, '{{财经新闻4_正文}}',
        f'国际金价震荡反弹，现货黄金报{color(GOLD_PRICE + "美元/盎司", "cyan")}，{color(GOLD_CHANGE, "red")}；上海金约{color(SH_GOLD + "元/克", "cyan")}；白银{color(SILVER_CHANGE, "green")}报{color(SILVER_PRICE + "美元/盎司", "cyan")}。美联储鹰派言论压制金价，但地缘避险需求和央行购金提供支撑，黄金短期或维持震荡。')

    # 5. Tab 2: AI前沿
    content = replace_placeholder(content, '{{大模型新闻1_标签和标题}}',
        '<span class="tag tag-ai">🏆 资本</span>OpenAI与Anthropic竞逐IPO')
    content = replace_placeholder(content, '{{大模型新闻1_正文}}',
        f'{color("OpenAI", "purple")}与{color("Anthropic", "purple")}先后提交IPO申请，竞逐2026年秋季上市窗口。两家公司的上市将为AI行业带来大规模资本增量，推动算力基础设施、数据标注、模型服务等产业链快速发展。市场预计，AI板块估值体系将因头部企业上市而重新定价。')

    content = replace_placeholder(content, '{{大模型新闻2_标签和标题}}',
        '<span class="tag tag-ai">📋 生态</span>华为HDC 2026：HarmonyOS 7进入Agent时代')
    content = replace_placeholder(content, '{{大模型新闻2_正文}}',
        f'华为HDC 2026大会正式发布{color("HarmonyOS 7", "purple")}，进入Agent时代，并推出{color("openPangu 2.0", "purple")}大模型。这标志着端侧AI与操作系统深度融合，AI Agent将在手机、车机、IoT设备上实现更自然的人机交互，带动端侧算力、应用生态和开发者活跃度全面提升。')

    content = replace_placeholder(content, '{{大模型新闻3_标签和标题}}',
        '<span class="tag tag-ai">🔓 数据</span>中国AI大模型调用量六周全球领先')
    content = replace_placeholder(content, '{{大模型新闻3_正文}}',
        f'最新统计显示，中国AI大模型连续六周全球调用量领先美国，反映国内AI应用渗透率快速提升。企业级AI办公助手、AI客服、代码助手等场景进入规模化落地阶段，{color("调用量", "cyan")}增长将带动上游算力需求和下游应用变现能力同步改善。')

    content = replace_placeholder(content, '{{大模型新闻4_标签和标题}}',
        '<span class="tag tag-ai">📊 预期</span>GPT-5.6本月发布预期升温')
    content = replace_placeholder(content, '{{大模型新闻4_正文}}',
        f'市场普遍预期{color("GPT-5.6", "purple")}将于本月发布，新模型在多模态理解、推理能力和Agent执行方面或有显著提升。大模型迭代加速将加剧AI应用竞争，具备数据、场景和工程化能力的厂商有望脱颖而出，纯模型公司面临更大商业化压力。')

    # 机器人新闻
    content = replace_placeholder(content, '{{机器人新闻1_标签和标题}}',
        '<span class="tag tag-robot">🤖 应用</span>端侧AI加速机器人落地')
    content = replace_placeholder(content, '{{机器人新闻1_正文}}',
        f'随着端侧大模型能力增强，人形机器人在工业巡检、物流分拣、家庭服务等场景的落地速度加快。AI模型的小型化与专用化降低了机器人对云端算力的依赖，{color("响应延迟", "cyan")}和{color("数据隐私", "cyan")}问题得到改善，机器人产业化进程明显提速。')

    content = replace_placeholder(content, '{{机器人新闻2_标签和标题}}',
        '<span class="tag tag-robot">🏭 产业</span>具身智能产业链热度提升')
    content = replace_placeholder(content, '{{机器人新闻2_正文}}',
        f'具身智能成为AI落地的下一重要方向，{color("减速器", "yellow")}、{color("伺服系统", "yellow")}、{color("力传感器", "yellow")}等核心零部件需求快速增长。国内厂商在谐波减速器、空心杯电机等领域取得突破，供应链成本有望持续下降，推动机器人整机价格进入可普及区间。')

    content = replace_placeholder(content, '{{机器人新闻3_标签和标题}}',
        '<span class="tag tag-robot">🔧 技术</span>AI医疗与自动驾驶持续推进')
    content = replace_placeholder(content, '{{机器人新闻3_正文}}',
        f'AI辅助诊断、AI影像分析在三级医院和基层医疗机构加速部署，自动驾驶城市NOA覆盖区域持续扩大。垂直场景的数据闭环和监管路径逐步清晰，AI应用正从{color("概念验证", "yellow")}走向{color("规模化商业化", "red")}。')

    # 算力新闻
    content = replace_placeholder(content, '{{算力新闻1_标签和标题}}',
        '<span class="tag tag-chip">⚡ 算力</span>算力硬件链批量涨停')
    content = replace_placeholder(content, '{{算力新闻1_正文}}',
        f'6月18日A股算力硬件链批量涨停，{color("光模块", "purple")}、{color("PCB", "purple")}、{color("服务器", "purple")}、{color("高速铜连接", "purple")}等方向领涨。OpenAI与Anthropic IPO预期强化市场对AI资本开支高增长的信心，算力基础设施作为AI产业核心底座，业绩确定性较高。')

    content = replace_placeholder(content, '{{算力新闻2_标签和标题}}',
        '<span class="tag tag-chip">💾 存储</span>HBM与存储芯片需求紧俏')
    content = replace_placeholder(content, '{{算力新闻2_正文}}',
        f'AI服务器需求爆发带动{color("HBM", "purple")}高带宽存储持续紧缺，主流产品价格上涨，韩系厂商订单排期已至2026年下半年。国内存储企业在技术追赶和产能扩张上持续投入，有望逐步切入AI供应链，分享算力建设红利。')

    content = replace_placeholder(content, '{{算力新闻3_标签和标题}}',
        '<span class="tag tag-chip">🌐 光模块</span>800G及以上产品国产替代加速')
    content = replace_placeholder(content, '{{算力新闻3_正文}}',
        f'高速光模块作为AI数据中心互联核心器件，需求持续井喷。国内头部企业在{color("800G", "purple")}及以上产品实现技术突破，{color("国产替代", "red")}进程加速，龙头公司产能利用率和毛利率有望持续改善，成为AI算力产业链中最具业绩弹性的环节之一。')

    # AI应用新闻
    content = replace_placeholder(content, '{{AI应用新闻1_标签和标题}}',
        '<span class="tag tag-app">🏥 医疗</span>AI辅助诊断规模化落地')
    content = replace_placeholder(content, '{{AI应用新闻1_正文}}',
        f'AI辅助诊断系统在三级医院加速部署，影像识别准确率突破{color("98%", "cyan")}。基层医疗机构通过AI工具提升诊疗能力，医疗资源分布不均问题有望逐步缓解。AI+医疗成为规模化落地最快的垂直应用之一，相关SaaS服务商和医疗AI公司受益明显。')

    content = replace_placeholder(content, '{{AI应用新闻2_标签和标题}}',
        '<span class="tag tag-app">🚗 智驾</span>自动驾驶向大众车型渗透')
    content = replace_placeholder(content, '{{AI应用新闻2_正文}}',
        f'城市NOA加速落地，一二线城市高精地图覆盖区域持续扩大。AI视觉算法迭代升级，接管里程指标持续优化。智能驾驶从高端车型向大众车型渗透，{color("激光雷达", "purple")}、{color("域控制器", "purple")}、{color("智能座舱", "purple")}等产业链充分受益。')

    content = replace_placeholder(content, '{{AI应用新闻3_标签和标题}}',
        '<span class="tag tag-app">💬 办公</span>AI办公助手企业端渗透加速')
    content = replace_placeholder(content, '{{AI应用新闻3_正文}}',
        f'AI办公助手在企业侧加速渗透，文档处理、会议纪要、数据分析等场景效率提升显著。AI Agent成为办公自动化的新范式，{color("降本增效", "red")}效果明显，看好具备垂直行业know-how和私有部署能力的AI应用龙头。')

    # 产业趋势
    content = replace_placeholder(content, '{{产业趋势新闻1_标签和标题}}',
        '<span class="tag tag-ai">🔮 趋势</span>端侧AI重塑硬件生态')
    content = replace_placeholder(content, '{{产业趋势新闻1_正文}}',
        f'端侧AI芯片加速迭代，NPU算力持续提升。AI手机、AI PC从概念走向普及，端侧大模型部署成为趋势。这一变革将重塑消费电子产业格局，{color("硬件+软件+服务", "purple")}一体化能力成为核心竞争壁垒，具备端侧模型优化能力的厂商将获得先发优势。')

    # 正面/热点/风险
    content = replace_placeholder(content, '{{正面因素_内容}}',
        f'创业板指{color(CYB_CHANGE, "red")}大涨，科创50{color(KC50_CHANGE, "red")}飙升；北向资金{color(A_NORTHBOUND, "red")}；算力硬件链批量涨停；黄金{color(GOLD_CHANGE, "red")}反弹；高股息银行股全线飘红。')
    content = replace_placeholder(content, '{{市场热点_内容}}',
        f'OpenAI/Anthropic IPO竞速；华为HDC 2026发布HarmonyOS 7与openPangu 2.0；霍尔木兹海峡重开预期；中国AI大模型调用量六周全球领先；算力硬件链批量涨停。')
    content = replace_placeholder(content, '{{风险提示_内容}}',
        f'美联储鹰派信号压制美股，道指{color(DJI_CHANGE, "green")}、纳指{color(NDX_CHANGE, "green")}；全市场约3400家下跌；港股{color(HSI_CHANGE, "green")}重挫；加密货币BTC{color(BTC_CHANGE, "green")}、ETH{color(ETH_CHANGE, "green")}大跌。')

    # 6. Tab 3: 全球市场 数据替换
    content = replace_placeholder(content, '{{A股_收盘日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{A股_上证指数_数据}}', f'{SH_COMPONENT} {SH_CHANGE}')
    content = replace_placeholder(content, '{{A股_深证成指_数据}}', f'{SZ_COMPONENT} {SZ_CHANGE}')
    content = replace_placeholder(content, '{{A股_创业板指_数据}}', f'{CYB_INDEX} {CYB_CHANGE}')
    content = replace_placeholder(content, '{{A股_科创50_数据}}', f'{KC50_INDEX} {KC50_CHANGE}')
    content = replace_placeholder(content, '{{A股_沪深300_数据}}', f'{HS300_INDEX} {HS300_CHANGE}')
    content = replace_placeholder(content, '{{A股_成交额}}', f'约{A_SHARES_VOLUME}')
    content = replace_placeholder(content, '{{A股_成交额备注}}', '量能充沛')
    content = replace_placeholder(content, '{{A股_涨跌家数}}', A_SHARES_UP_DOWN)
    content = replace_placeholder(content, '{{A股_北向资金}}', A_NORTHBOUND)

    content = replace_placeholder(content, '{{港股_收盘日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{港股_恒生指数_数据}}', f'{HSI_INDEX} {HSI_CHANGE}')
    content = replace_placeholder(content, '{{港股_恒生科技_数据}}', f'{HSTECH_INDEX} {HSTECH_CHANGE}')
    content = replace_placeholder(content, '{{港股_国企指数_数据}}', f'{HSCEI_INDEX} {HSCEI_CHANGE}')
    content = replace_placeholder(content, '{{港股_南向资金}}', H_SOUTHBOUND)

    content = replace_placeholder(content, '{{美股_收盘日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{美股_道琼斯_涨跌幅}}', DJI_CHANGE)
    content = replace_placeholder(content, '{{美股_标普500_涨跌幅}}', SPX_CHANGE)
    content = replace_placeholder(content, '{{美股_纳斯达克_涨跌幅}}', NDX_CHANGE)
    content = replace_placeholder(content, '{{美股_英伟达_涨跌幅}}', NVDA_CHANGE)
    content = replace_placeholder(content, '{{美股_特斯拉_涨跌幅}}', TSLA_CHANGE)
    content = replace_placeholder(content, '{{美股_ARM}}', f'{ARM_CHANGE}')

    content = replace_placeholder(content, '{{亚太_收盘日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{亚太_日经225}}', f'{NI225_INDEX} {NI225_CHANGE}')
    content = replace_placeholder(content, '{{亚太_韩国KOSPI_状态}}', f'{KOSPI_INDEX} {KOSPI_CHANGE}')
    content = replace_placeholder(content, '{{亚太_台湾加权_状态}}', f'{TAIWAN_INDEX} {TAIWAN_CHANGE}')
    content = replace_placeholder(content, '{{亚太_印度Sensex_状态}}', f'{INDIA_INDEX} {INDIA_CHANGE}')
    content = replace_placeholder(content, '{{亚太_澳洲ASX200_状态}}', f'{ASX_INDEX} {ASX_CHANGE}')

    content = replace_placeholder(content, '{{欧洲_收盘日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{欧洲_英国富时100_涨跌幅}}', f'{UK100_INDEX} {UK100_CHANGE}')
    content = replace_placeholder(content, '{{欧洲_德国DAX30_涨跌幅}}', f'{DAX30_INDEX} {DAX30_CHANGE}')
    content = replace_placeholder(content, '{{欧洲_法国CAC40_涨跌幅}}', f'{CAC40_INDEX} {CAC40_CHANGE}')
    content = replace_placeholder(content, '{{欧洲_斯托克50_涨跌幅}}', f'{STOXX50_INDEX} {STOXX50_CHANGE}')

    content = replace_placeholder(content, '{{大宗商品_收盘日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{大宗_WTI原油}}', f'{WTI_OIL}美元/桶 {WTI_CHANGE}')
    content = replace_placeholder(content, '{{大宗_布伦特原油}}', f'{BRENT_OIL}美元/桶 {BRENT_CHANGE}')
    content = replace_placeholder(content, '{{大宗_国际黄金}}', f'${GOLD_PRICE}/盎司 {GOLD_CHANGE}')
    content = replace_placeholder(content, '{{大宗_上海金}}', f'约{SH_GOLD}元/克')
    content = replace_placeholder(content, '{{大宗_白银}}', f'{SILVER_PRICE}美元/盎司 {SILVER_CHANGE}')

    content = replace_placeholder(content, '{{汇率债券_收盘日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{汇率_USD/CNY中间价}}', f'{USD_CNY_MID}（贬值/上调34基点）')
    content = replace_placeholder(content, '{{汇率_在岸汇率}}', f'约{USD_CNY_ONSHORE}')
    content = replace_placeholder(content, '{{汇率_美元指数}}', f'{USD_INDEX} {USD_INDEX_CHANGE}')
    content = replace_placeholder(content, '{{汇率_美10年期}}', US_10Y)
    content = replace_placeholder(content, '{{汇率_美30年期}}', US_30Y)
    content = replace_placeholder(content, '{{汇率_中10年期}}', CN_10Y)

    content = replace_placeholder(content, '{{加密货币_收盘日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{加密_BTC}}', f'约${BTC_PRICE} {BTC_CHANGE}')
    content = replace_placeholder(content, '{{加密_ETH}}', f'约${ETH_PRICE} {ETH_CHANGE}')
    content = replace_placeholder(content, '{{加密_BTCEFT}}', BTC_ETF_FLOW)
    content = replace_placeholder(content, '{{加密_市场情绪}}', CRYPTO_SENTIMENT)

    # 市场综评
    content = replace_placeholder(content, '{{市场综评_日期}}', DATA_DATE)
    content = replace_placeholder(content, '{{综评_A股行情标题}}', 'A股极致分化')
    content = replace_placeholder(content, '{{综评_A股行情标签}}', '成长领涨')
    content = replace_placeholder(content, '{{综评_A股段落1}}',
        f'上证指数{color(SH_CHANGE, "green")}，深证成指{color(SZ_CHANGE, "red")}，创业板指{color(CYB_CHANGE, "red")}，科创50{color(KC50_CHANGE, "red")}。两市成交约{color(A_SHARES_VOLUME, "cyan")}，算力硬件链批量涨停，但全市场约{color("3400家下跌", "green")}，结构性行情突出。')
    content = replace_placeholder(content, '{{综评_A股段落2}}',
        f'北向资金{color(A_NORTHBOUND, "red")}，结束连续流出，加仓半导体、算力、光通信硬件。创业板与科创50大涨显示市场风险偏好回升，但个股跌多涨少反映资金高度集中。')
    content = replace_placeholder(content, '{{综评_A股段落3}}', f'数据来源：{DATA_DATE_FULL} A股收盘')

    content = replace_placeholder(content, '{{综评_外围市场标题}}', '美股尾盘跳水')
    content = replace_placeholder(content, '{{综评_外围市场标签}}', '科技股承压')
    content = replace_placeholder(content, '{{综评_外围段落1}}',
        f'美联储新任主席沃什释放鹰派信号，美股三大指数集体收跌：道指{color(DJI_CHANGE, "green")}，标普500{color(SPX_CHANGE, "green")}，纳斯达克{color(NDX_CHANGE, "green")}。英伟达{color(NVDA_CHANGE, "green")}，特斯拉{color(TSLA_CHANGE, "green")}，ARM逆市{color(ARM_CHANGE, "red")}。')
    content = replace_placeholder(content, '{{综评_外围段落2}}',
        f'美元指数{color(USD_INDEX_CHANGE, "red")}大涨至{color(USD_INDEX, "cyan")}，10年期美债收益率{color(US_10Y, "cyan")}，30年期{color(US_30Y, "cyan")}。外围流动性预期收紧，对全球风险资产估值形成压制。')
    content = replace_placeholder(content, '{{综评_外围段落3}}', f'数据来源：{DATA_DATE_FULL} 美股收盘')

    content = replace_placeholder(content, '{{综评_地缘政策标题}}', '霍尔木兹重开预期')
    content = replace_placeholder(content, '{{综评_地缘政策标签}}', '油价降温')
    content = replace_placeholder(content, '{{综评_地缘段落1}}',
        f'美伊签署临时协议，霍尔木兹海峡有望重开，地缘风险预期降温。WTI原油{color(WTI_CHANGE, "green")}，布伦特原油{color(BRENT_CHANGE, "green")}，全球能源供给预期改善，通胀压力边际缓解。')
    content = replace_placeholder(content, '{{综评_地缘段落2}}',
        f'美元指数走强、日元跌至2024年7月以来新低，全球资金流向避险资产。地缘缓和利好航运和全球供应链，但能源股短期面临供给溢价回落压力。')
    content = replace_placeholder(content, '{{综评_地缘段落3}}', f'数据来源：{DATA_DATE_FULL} 地缘/财经动态')

    content = replace_placeholder(content, '{{综评_风险事件标题}}', '市场情绪')
    content = replace_placeholder(content, '{{综评_风险事件标签}}', '谨慎')
    content = replace_placeholder(content, '{{综评_风险段落1}}',
        f'A股结构分化加剧，约3400家下跌；港股{color(HSI_CHANGE, "green")}重挫；美股三大指数收跌；加密货币BTC{color(BTC_CHANGE, "green")}、ETH{color(ETH_CHANGE, "green")}大跌，市场情绪偏谨慎。')
    content = replace_placeholder(content, '{{综评_风险段落2}}',
        f'假期因素叠加美联储鹰派信号，短期波动可能放大。建议控制仓位，关注高股息防御和科技成长业绩确定性方向。')
    content = replace_placeholder(content, '{{综评_风险段落3}}', f'数据截至{DATA_DATE_FULL}')

    # 市场情绪指示器
    content = replace_placeholder(content, '{{市场情绪_状态颜色}}', 'yellow')
    content = replace_placeholder(content, '{{市场情绪_状态}}', '谨慎偏乐观')
    content = replace_placeholder(content, '{{市场情绪_涨跌比}}', '跌多涨少')
    content = replace_placeholder(content, '{{市场情绪_成交额}}', A_SHARES_VOLUME)
    content = replace_placeholder(content, '{{市场情绪_北向资金}}', A_NORTHBOUND)

    # 7. Tab 4: 价值投资风向
    # 机构观点（每家120字以上）
    INSTITUTES = [
        ("中信", "中信证券", "券商龙头",
         f'中信证券认为，美联储鹰派信号压制全球风险资产估值，美股科技股承压可能通过情绪和估值联动影响A股。但A股结构性行情仍在，创业板指{color(CYB_CHANGE, "red")}、科创50{color(KC50_CHANGE, "red")}大涨显示资金向科技成长集中。建议关注算力链、半导体等业绩确定性方向，同时配置高股息银行、电力作为防御底仓。'),
        ("高盛", "高盛", "外资投行",
         f'高盛指出，OpenAI与Anthropic IPO竞速将重塑科技板块估值体系，AI算力基础设施作为最确定性受益环节，资本开支有望持续高增长。维持对AI算力基础设施的看好，包括光模块、服务器、PCB、高速铜连接等环节，同时提醒关注估值过高和商业化进度不及预期的风险。'),
        ("兴业", "兴业证券", "本土券商",
         f'兴业证券表示，创业板指大涨{color(CYB_CHANGE, "red")}显示市场风险偏好回升，算力链涨停反映资金对AI产业趋势的认可。但外围市场波动加大，港股{color(HSI_CHANGE, "green")}重挫，美联储鹰派信号仍制约A股上行空间。建议均衡配置科技成长与高股息防御板块。'),
        ("中金", "中金公司", "顶级投行",
         f'中金公司认为，港股估值处于历史低位，恒生指数{color(HSI_CHANGE, "green")}调整后配置价值进一步凸显。建议关注高股息银行与科技龙头估值修复机会，内地居民财富向权益市场迁移的趋势未变，港股通高股息资产对长线资金具备吸引力。'),
        ("大摩", "摩根士丹利", "国际投行",
         f'摩根士丹利指出，全球资金流向避险资产，美元指数{color(USD_INDEX_CHANGE, "red")}大涨、日元创新低反映风险偏好下降。在此背景下，黄金、高股息防御配置价值提升。A股方面，建议关注现金流稳定、分红率高的公用事业和银行板块，降低高估值成长股的仓位暴露。'),
        ("瑞银", "瑞银集团", "瑞士银行",
         f'瑞银集团认为，A股科技成长资金回流，北向资金{color(A_NORTHBOUND, "red")}结束连续流出，加仓半导体、算力、光通信硬件。随着中报季临近，建议关注中报业绩确定性方向，规避纯概念炒作，重点配置有订单、有产能、有出口的AI硬件龙头。'),
    ]
    for i, (short, name, tag, view) in enumerate(INSTITUTES, 1):
        content = replace_placeholder(content, f'{{{{机构{i}_简称}}}}', short)
        content = replace_placeholder(content, f'{{{{机构{i}_名称}}}}', name)
        content = replace_placeholder(content, f'{{{{机构{i}_标签}}}}', tag)
        content = replace_placeholder(content, f'{{{{机构{i}_观点}}}}', view)

    # 情绪指标
    sentiment_items = [
        ("高股息", "80%", "80%", "hot", "银行、电力板块防御属性突出"),
        ("银行", "75%", "75%", "hot", "低估值高股息，逆势上涨"),
        ("公用事业", "70%", "70%", "hot", "稳定现金流，防御配置"),
        ("电力", "72%", "72%", "hot", "水电核电业绩确定"),
        ("AI算力", "92%", "92%", "hot", "IPO预期+政策利好"),
        ("能源油价", "40%", "40%", "low", "霍尔木兹重开，油价承压"),
        ("新能源", "75%", "75%", "hot", "能源转型持续推进"),
        ("黄金", "78%", "78%", "hot", "震荡反弹，避险需求"),
        ("加密货币", "35%", "35%", "low", "BTC大跌，情绪谨慎偏空"),
    ]
    for name, width, pct, cls, desc in sentiment_items:
        content = replace_placeholder(content, f'{{{{情绪_{name}_名称}}}}', name)
        content = replace_placeholder(content, f'{{{{情绪_{name}_宽度}}}}', width)
        content = replace_placeholder(content, f'{{{{情绪_{name}_百分比}}}}', pct)
        content = replace_placeholder(content, f'{{{{情绪_{name}_样式类}}}}', cls)
        content = replace_placeholder(content, f'{{{{情绪_{name}_描述}}}}', desc)

    # 社区话题标签
    content = replace_placeholder(content, '{{社区话题标签1}}', '算力链涨停')
    content = replace_placeholder(content, '{{社区话题标签2}}', '美联储鹰派')
    content = replace_placeholder(content, '{{社区话题标签3}}', '黄金反弹')
    content = replace_placeholder(content, '{{社区话题标签4}}', '高股息银行')
    content = replace_placeholder(content, '{{社区话题标签5}}', '港股低估值')

    # 高股息板块深度分析（每段120字以上）
    content = replace_placeholder(content, '{{高股息_银行标题}}', '银行板块：PB 0.6-0.8倍，股息率4.5-5.5%')
    content = replace_placeholder(content, '{{高股息_银行内容}}',
        f'银行板块当前PB约{color("0.6-0.8倍", "cyan")}，处于历史低位，股息率{color("4.5-5.5%", "red")}，显著高于10年期国债{color(CN_10Y, "cyan")}和货币基金{color(MMF_YIELD, "green")}。6月18日工商银行涨0.13%、建设银行涨0.04%、招商银行涨0.40%，在市场调整中展现防御属性。险资、北向资金持续加仓银行股，估值修复逻辑清晰，适合作为稳健型投资者的底仓配置。')
    content = replace_placeholder(content, '{{高股息_公用事业标题}}', '公用事业：稳定现金流，高股息防御强')
    content = replace_placeholder(content, '{{高股息_公用事业内容}}',
        f'水电、燃气等公用事业板块具备{color("稳定现金流", "cyan")}特征，不受经济周期影响。长江电力PB约{color("2.86倍", "cyan")}，股息率稳定，业绩确定性极强。在市场波动加大、美联储鹰派信号压制风险资产的背景下，公用事业板块的防御属性凸显，适合保守型投资者作为避险底仓。')
    content = replace_placeholder(content, '{{高股息_电力标题}}', '电力板块：PE 15-20倍，股息率3.5-4.5%')
    content = replace_placeholder(content, '{{高股息_电力内容}}',
        f'电力板块PE约{color("15-20倍", "cyan")}，股息率{color("3.5-4.5%", "red")}。受益于能源转型，核电、水电等清洁能源装机持续增长。中国核电PE约{color("20倍", "cyan")}，6月18日涨0.81%，业绩增速稳定，现金流良好，具备长期投资价值，是成长性与高股息兼具的标的。')
    content = replace_placeholder(content, '{{高股息_央企标题}}', '央企蓝筹：高股息+低估值，估值修复可期')
    content = replace_placeholder(content, '{{高股息_央企内容}}',
        f'中国移动PB约{color("1.40倍", "cyan")}，中国平安PB约{color("0.88倍", "cyan")}，大秦铁路PB约{color("0.60倍", "cyan")}，股息率普遍在{color("4%", "red")}以上。央企改革持续推进，ROE提升逻辑清晰，在中特估估值体系下，央企蓝筹估值修复空间较大，适合长线资金配置。')

    # 低估值板块
    content = replace_placeholder(content, '{{低估值1_名称}}', '中证红利')
    content = replace_placeholder(content, '{{估值_中证红利PE_今日涨幅}}', SH_CHANGE)
    content = replace_placeholder(content, '{{低估值1_收盘价}}', f'{SH_COMPONENT}点')
    content = replace_placeholder(content, '{{低估值1_描述}}',
        f'低估值高股息策略有效，中证红利指数跟随上证震荡。当前银行、电力等高股息板块PB处于历史低位，股息率{color("4.5-5.5%", "red")}，显著高于无风险收益率，适合稳健型投资者。')
    content = replace_placeholder(content, '{{低估值2_名称}}', '港股恒生科技')
    content = replace_placeholder(content, '{{低估值2_今日涨幅}}', HSTECH_CHANGE)
    content = replace_placeholder(content, '{{低估值2_涨幅样式}}', 'down')
    content = replace_placeholder(content, '{{低估值2_收盘价}}', f'{HSTECH_INDEX}点')
    content = replace_placeholder(content, '{{低估值2_描述}}',
        f'恒生科技指数{color(HSTECH_CHANGE, "green")}，估值处于历史低位，互联网龙头估值修复空间大。但短期受外围科技股承压和美联储鹰派信号影响，建议逢低分批布局。')

    # 资金流向
    content = replace_placeholder(content, '{{资金流向_节点1标题}}', '北向资金')
    content = replace_placeholder(content, '{{资金流向_节点1描述}}', A_NORTHBOUND)
    content = replace_placeholder(content, '{{资金流向_节点2标题}}', '南向资金')
    content = replace_placeholder(content, '{{资金流向_节点2描述}}', H_SOUTHBOUND)
    content = replace_placeholder(content, '{{资金流向_节点3标题}}', 'ETF流向')
    content = replace_placeholder(content, '{{资金流向_节点3描述}}', '科技ETF净流入')
    content = replace_placeholder(content, '{{资金_证券ETF流向}}', '稳定流入')
    content = replace_placeholder(content, '{{资金_红利ETF流向}}', '持续流入')

    # 估值数据
    content = replace_placeholder(content, '{{估值_银行PB}}', '0.6-0.8倍')
    content = replace_placeholder(content, '{{估值_银行PB_标签}}', '历史低位')
    content = replace_placeholder(content, '{{估值_银行PB_标签类}}', 'low')
    content = replace_placeholder(content, '{{估值_银行PB_说明}}', 'PB处于历史底部')
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
    content = replace_placeholder(content, '{{估值_中国移动PB}}', '1.40倍')
    content = replace_placeholder(content, '{{估值_中国移动PB_标签}}', '适中')
    content = replace_placeholder(content, '{{估值_中国移动PB_标签类}}', 'mid')
    content = replace_placeholder(content, '{{估值_招商银行PB}}', '0.83倍')
    content = replace_placeholder(content, '{{估值_招商银行PB_标签}}', '历史低位')
    content = replace_placeholder(content, '{{估值_招商银行PB_标签类}}', 'low')
    content = replace_placeholder(content, '{{估值_中国核电PE}}', '20倍')
    content = replace_placeholder(content, '{{估值_中国核电PE_标签}}', '适中')
    content = replace_placeholder(content, '{{估值_中国核电PE_标签类}}', 'mid')
    content = replace_placeholder(content, '{{估值_黄金价格}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{估值_黄金价格_标签}}', '震荡反弹')
    content = replace_placeholder(content, '{{估值_黄金价格_标签类}}', 'hot')

    # 8. Tab 5: 关注标的
    for i, stock in enumerate(STOCKS, 1):
        cls = change_class(stock['change'])
        content = replace_placeholder(content, f'{{{{标的{i}_代码}}}}', stock['code'])
        content = replace_placeholder(content, f'{{{{标的{i}_名称}}}}', stock['name'])
        content = replace_placeholder(content, f'{{{{标的{i}_价格}}}}', f'{stock["price"]}元')
        content = replace_placeholder(content, f'{{{{标的{i}_涨跌幅}}}}', span_class(stock['change'], cls))
        content = replace_placeholder(content, f'{{{{标的{i}_成交额}}}}', '正常')
        content = replace_placeholder(content, f'{{{{标的{i}_基本面}}}}', f'PB约{stock["pb"]}倍，{stock["name"]}基本面稳健')
        content = replace_placeholder(content, f'{{{{标的{i}_股价}}}}', f'{stock["price"]}元')
        content = replace_placeholder(content, f'{{{{标的{i}_涨跌class}}}}', cls)

    # 标的要点（每个5条）
    stock_points = [
        [f'{color("股息率约5%", "red")}，显著高于无风险收益率', f'{color("PB约0.65倍", "cyan")}，处于历史低位', f'{color("涨0.13%", "red")}，大行中表现稳健', f'{color("资产质量稳健", "green")}，不良贷款率可控', '长期配置价值凸显，适合险资和长线资金'],
        [f'{color("股息率约5%", "red")}，大行中较高', f'{color("PB约0.73倍", "cyan")}，估值历史低位', f'{color("涨0.04%", "red")}，防御属性明显', f'{color("基本面稳定", "green")}，业绩确定性较强', '高股息防御配置首选'],
        [f'{color("股息率约5.5%", "red")}，四大行最高', f'{color("PB约0.79倍", "cyan")}，破净状态', f'{color("涨0.10%", "red")}，走势稳健', f'{color("资产质量改善", "green")}，不良率持续下降', '高股息防御配置首选'],
        [f'{color("PB约0.83倍", "cyan")}，零售银行龙头', f'{color("涨0.40%", "red")}，成交活跃', f'{color("零售业务强劲", "red")}，资产质量优异', f'{color("股息率约4.5%", "red")}，长期分红稳定', '长期看好，短期注意板块轮动'],
        [f'{color("PB约0.87倍", "cyan")}，城商行中估值合理', f'{color("涨0.63%", "red")}，表现强于大行', f'{color("资产质量优异", "green")}，不良率控制良好', f'{color("区域经济活力强", "yellow")}，业务拓展空间大', '高成长性城商行代表'],
        [f'{color("PB约0.78倍", "cyan")}，估值较低', f'{color("涨0.61%", "red")}，城商行中表现活跃', f'{color("股息率较高", "red")}，高股息策略适用', f'{color("规模较大", "yellow")}，江苏省经济活力强', '低估值高股息配置价值突出'],
        [f'{color("PB约0.81倍", "cyan")}，城商行中估值合理', f'{color("涨0.57%", "red")}，走势强于板块', f'{color("业绩增长", "green")}，营收增速较快', f'{color("区域经济发达", "yellow")}，浙江民营经济活跃', '成长性突出的城商行'],
        [f'{color("PB约0.66倍", "cyan")}，估值较低', f'{color("股息率较高", "red")}，高股息特征明显', f'{color("涨0.35%", "red")}，调整幅度有限', f'{color("成渝地区双城", "yellow")}，受益于区域发展', '低估值高股息标的'],
        [f'{color("股息率约3.5%", "red")}，稳定现金牛', f'{color("PB约2.86倍", "cyan")}，水电龙头溢价', f'{color("涨0.53%", "red")}，防御属性显现', f'{color("现金流稳定", "green")}，不受经济周期影响', '长期投资者防御配置首选'],
        [f'{color("股息率约5%", "red")}，高股息代表', f'{color("PB约0.60倍", "cyan")}，估值极低', f'{color("涨0.37%", "red")}，走势稳健', f'{color("运煤专线", "yellow")}，区域垄断优势', '稳健收益类投资者适合'],
        [f'{color("股息率约4%", "red")}，运营商最高', f'{color("PB约1.40倍", "cyan")}，估值合理', f'{color("涨0.04%", "red")}，走势平稳', f'{color("5G龙头", "yellow")}，用户规模全球第一', '央企蓝筹，中特估受益标的'],
        [f'{color("PE约20倍", "cyan")}，清洁能源估值合理', f'{color("核电龙头", "yellow")}，技术壁垒高', f'{color("涨0.81%", "red")}，走势稳健', f'{color("能源转型受益", "green")}，政策支持明确', '成长性+高股息兼具'],
        [f'{color("PB约0.88倍", "cyan")}，保险龙头低估', f'{color("涨1.20%", "red")}，13只标的涨幅最大', f'{color("综合金融", "yellow")}，牌照齐全', f'{color("估值修复空间大", "red")}，ROE有望提升', '保险行业龙头，长期配置价值显现'],
    ]
    for i, points in enumerate(stock_points, 1):
        for j, pt in enumerate(points, 1):
            content = replace_placeholder(content, f'{{{{标的{i}_要点{j}}}}}', pt)

    # 深度解读
    content = replace_placeholder(content, '{{深度解读_银行组标题}}', '银行板块')
    content = replace_placeholder(content, '{{深度解读_银行组标签}}', '高股息+低估值')
    content = replace_placeholder(content, '{{深度解读_银行1_标题}}', '工商银行')
    content = replace_placeholder(content, '{{深度解读_银行1_指标}}', f'{STOCKS[0]["price"]}元 {STOCKS[0]["change"]}')
    content = replace_placeholder(content, '{{深度解读_银行2_标题}}', '建设银行')
    content = replace_placeholder(content, '{{深度解读_银行2_指标}}', f'{STOCKS[1]["price"]}元 {STOCKS[1]["change"]}')
    content = replace_placeholder(content, '{{深度解读_银行3_标题}}', '招商银行')
    content = replace_placeholder(content, '{{深度解读_银行3_指标}}', f'{STOCKS[3]["price"]}元 {STOCKS[3]["change"]}')
    content = replace_placeholder(content, '{{深度解读_银行总结}}',
        f'银行板块PB约{color("0.6-0.8倍", "cyan")}，股息率{color("4.5-5.5%", "red")}，处于历史估值底部。6月18日工商银行、建设银行、招商银行全线飘红，在市场调整中展现防御属性。险资、北向资金持续加仓银行股，估值修复逻辑未变，适合作为稳健底仓。')

    content = replace_placeholder(content, '{{深度解读_公用组标题}}', '公用事业')
    content = replace_placeholder(content, '{{深度解读_公用组标签}}', '稳定现金流')
    content = replace_placeholder(content, '{{深度解读_公用1_标题}}', '长江电力')
    content = replace_placeholder(content, '{{深度解读_公用1_指标}}', f'{STOCKS[8]["price"]}元 {STOCKS[8]["change"]}')
    content = replace_placeholder(content, '{{深度解读_公用2_标题}}', '中国核电')
    content = replace_placeholder(content, '{{深度解读_公用2_指标}}', f'{STOCKS[11]["price"]}元 {STOCKS[11]["change"]}')
    content = replace_placeholder(content, '{{深度解读_公用总结}}',
        f'公用事业板块具备{color("稳定现金流", "cyan")}特征，不受经济周期影响。长江电力PB约{color("2.86倍", "cyan")}，中国核电PE约{color("20倍", "cyan")}，股息率稳定，业绩确定性极强，是防御配置的理想选择。')

    content = replace_placeholder(content, '{{深度解读_央企组标题}}', '央企蓝筹')
    content = replace_placeholder(content, '{{深度解读_央企组标签}}', '中特估受益')
    content = replace_placeholder(content, '{{深度解读_央企1_标题}}', '中国移动')
    content = replace_placeholder(content, '{{深度解读_央企1_指标}}', f'{STOCKS[10]["price"]}元 {STOCKS[10]["change"]}')
    content = replace_placeholder(content, '{{深度解读_央企2_标题}}', '中国平安')
    content = replace_placeholder(content, '{{深度解读_央企2_指标}}', f'{STOCKS[12]["price"]}元 {STOCKS[12]["change"]}')
    content = replace_placeholder(content, '{{深度解读_央企3_标题}}', '中国核电')
    content = replace_placeholder(content, '{{深度解读_央企3_指标}}', f'{STOCKS[11]["price"]}元 {STOCKS[11]["change"]}')
    content = replace_placeholder(content, '{{深度解读_央企4_标题}}', '大秦铁路')
    content = replace_placeholder(content, '{{深度解读_央企4_指标}}', f'{STOCKS[9]["price"]}元 {STOCKS[9]["change"]}')
    content = replace_placeholder(content, '{{深度解读_央企总结}}',
        f'央企蓝筹PB约{color("0.6-1.4倍", "cyan")}，股息率{color("4%", "red")}以上。在中特估估值体系下，央企改革持续推进，ROE提升逻辑清晰，估值修复空间较大，适合长线资金配置。')

    content = replace_placeholder(content, '{{深度解读_配置建议内容}}',
        f'当前市场环境下，建议关注三条主线：{color("一", "yellow")}是科技成长，AI、半导体、算力等确定性较强的方向；{color("二", "yellow")}是高股息，银行、电力、公用事业等稳定现金流板块；{color("三", "yellow")}是风险控制，假期临近注意仓位管理。')

    # 正面/风险提示
    content = replace_placeholder(content, '{{标的_正面提示标题}}', '利好因素')
    content = replace_placeholder(content, '{{标的_正面提示内容}}',
        f'创业板指{color(CYB_CHANGE, "red")}大涨，科创50{color(KC50_CHANGE, "red")}飙升；北向资金{color(A_NORTHBOUND, "red")}；算力硬件链批量涨停；高股息银行股全线飘红；OpenAI/Anthropic IPO竞速。')
    content = replace_placeholder(content, '{{标的_风险提示标题}}', '风险提示')
    content = replace_placeholder(content, '{{标的_风险提示内容}}',
        f'上证指数{color(SH_CHANGE, "green")}收跌；港股{color(HSI_CHANGE, "green")}重挫；美股三大指数{color("集体收跌", "green")}；加密货币BTC{color(BTC_CHANGE, "green")}、ETH{color(ETH_CHANGE, "green")}大跌；端午假期外围波动风险。')

    # 9. Tab 6: 理财话题
    content = replace_placeholder(content, '{{存款利率_1年}}', CD_1Y)
    content = replace_placeholder(content, '{{存款利率_3年}}', CD_3Y)
    content = replace_placeholder(content, '{{存款利率_5年}}', CD_5Y)
    content = replace_placeholder(content, '{{大额存单_1年}}', '1.40%')
    content = replace_placeholder(content, '{{大额存单_3年}}', '1.55%')
    content = replace_placeholder(content, '{{货币基金_收益率}}', MMF_YIELD)
    content = replace_placeholder(content, '{{纯债基金_收益}}', PURE_BOND_YIELD)
    content = replace_placeholder(content, '{{10年国债收益率}}', CN_10Y)

    # 理财卡片
    content = replace_placeholder(content, '{{理财卡1_标题}}', '黄金')
    content = replace_placeholder(content, '{{理财卡1_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{理财卡1_备注}}', '震荡反弹')
    content = replace_placeholder(content, '{{理财卡2_标题}}', '银行股息率')
    content = replace_placeholder(content, '{{理财卡2_数值}}', '4.5-5.5%')
    content = replace_placeholder(content, '{{理财卡2_备注}}', '历史高位')
    content = replace_placeholder(content, '{{理财卡3_标题}}', '10年国债')
    content = replace_placeholder(content, '{{理财卡3_数值}}', CN_10Y)
    content = replace_placeholder(content, '{{理财卡3_备注}}', '低位运行')
    content = replace_placeholder(content, '{{理财卡4_标题}}', '货币基金')
    content = replace_placeholder(content, '{{理财卡4_数值}}', MMF_YIELD)
    content = replace_placeholder(content, '{{理财卡4_备注}}', '持续下行')

    # 稳健理财图表
    content = replace_placeholder(content, '{{图表_数据日期}}', DATA_DATE_FULL)
    content = replace_placeholder(content, '{{图表_红利ETF_名称}}', '红利ETF')
    content = replace_placeholder(content, '{{图表_红利ETF_副标题}}', '高股息策略')
    content = replace_placeholder(content, '{{图表_红利ETF_数值}}', '正收益')
    content = replace_placeholder(content, '{{图表_银行股息率_注释}}', '银行板块')
    content = replace_placeholder(content, '{{图表_银行股息率_数值}}', '4.5-5.5%')
    content = replace_placeholder(content, '{{图表_超长国债_数值}}', '低位')
    content = replace_placeholder(content, '{{图表_银行理财_数值}}', '3%左右')
    content = replace_placeholder(content, '{{图表_5年定存_数值}}', CD_5Y)
    content = replace_placeholder(content, '{{图表_1年定存_数值}}', CD_1Y)
    content = replace_placeholder(content, '{{图表_收益计算说明}}',
        f'100万配置：银行股息约{color("4.5-5.5万/年", "red")}，远超货币基金约{color("1万/年", "green")}，也高于5年定存约{color("1.65万/年", "yellow")}。高股息策略在低利率时代优势明显。')

    # 替代策略
    content = replace_placeholder(content, '{{替代策略_股息对比内容}}',
        f'股息率对比：银行股{color("4.5-5.5%", "red")} > 10年国债{color(CN_10Y, "yellow")} > 货币基金{color(MMF_YIELD, "green")} > 1年定存{color(CD_1Y, "cyan")}')
    content = replace_placeholder(content, '{{替代策略_配置逻辑}}',
        f'在当前低利率环境下，高股息资产配置价值凸显。银行、电力等高股息板块不仅提供稳定现金回报，还具备估值修复空间。')
    content = replace_placeholder(content, '{{替代策略_配置建议内容}}',
        f'建议稳健型投资者可将{color("50-60%", "cyan")}资金配置于高股息标的，兼顾收益与防御性。')

    # 避坑指南
    content = replace_placeholder(content, '{{避坑1_标题}}', '追高算力链')
    content = replace_placeholder(content, '{{避坑1_内容}}',
        f'算力硬件链批量涨停后短期情绪过热，部分个股估值已透支未来业绩。{color("盲目追高", "green")}风险巨大，建议关注有实际业绩支撑和订单兑现的龙头。')
    content = replace_placeholder(content, '{{避坑2_标题}}', '忽视假期风险')
    content = replace_placeholder(content, '{{避坑2_内容}}',
        f'端午节假期A股休市，但海外市场正常交易。{color("节假日期间", "yellow")}外围波动可能传导至节后开盘，建议控制仓位，避免长假期间敞口过大。')
    content = replace_placeholder(content, '{{避坑3_标题}}', '忽视汇率风险')
    content = replace_placeholder(content, '{{避坑3_内容}}',
        f'USD/CNY中间价{color("上调34个基点", "green")}，人民币贬值对进口成本和海外负债构成压力。配置外币资产需{color("注意对冲", "yellow")}，避免单一货币敞口过大。')

    # 保险窗口提醒
    content = replace_placeholder(content, '{{保险_窗口提醒标题}}', '6月保险配置窗口期')
    content = replace_placeholder(content, '{{保险_窗口提醒内容}}',
        f'6月是保险产品上半年的重要节点，部分产品可能{color("调整收益率", "yellow")}。有配置需求的投资者可关注，优先选择保障型产品，避免过度追求高收益储蓄险。')

    # 黄金
    content = replace_placeholder(content, '{{黄金_标题}}', '国际黄金')
    content = replace_placeholder(content, '{{黄金_单位}}', '美元/盎司')
    content = replace_placeholder(content, '{{黄金_价格}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{黄金_涨跌颜色}}', 'red')
    content = replace_placeholder(content, '{{黄金_涨跌幅}}', GOLD_CHANGE)
    content = replace_placeholder(content, '{{黄金_SVG路径}}', '')
    content = replace_placeholder(content, '{{黄金_SVG填充路径}}', '')
    content = replace_placeholder(content, '{{黄金_日期1}}', '6月16日')
    content = replace_placeholder(content, '{{黄金_日期2}}', '6月17日')
    content = replace_placeholder(content, '{{黄金_日期3}}', DATA_DATE)
    content = replace_placeholder(content, '{{黄金_走势描述}}',
        f'国际金价震荡反弹{color(GOLD_CHANGE, "red")}，报{color(GOLD_PRICE + "美元/盎司", "cyan")}。美联储鹰派信号压制金价，但地缘避险需求和央行购金提供支撑，白银{color(SILVER_CHANGE, "green")}跌幅较大，贵金属内部分化。')

    # 债基配置建议
    content = replace_placeholder(content, '{{债基_配置建议标题}}', '债基配置建议')
    content = replace_placeholder(content, '{{债基_配置建议内容}}',
        f'当前债市表现稳健，纯债基金持续正收益，中10年期国债收益率{color(CN_10Y, "cyan")}维持低位。在市场波动加大的环境下，{color("纯债基金", "cyan")}可作为稳健资产配置的一部分，建议配置比例{color("20-30%", "yellow")}。')

    # 社区热门话题（10个，每个120字以上，4-6处高亮）
    topics = [
        {
            "title": "创业板大涨2%算力链涨停，科技股能追吗？",
            "source": "雪球",
            "heat": "🔥 热议",
            "roles": ["科技多头", "谨慎派", "老盛观点"],
            "views": [
                f'科创50{color("飙升3.84%", "red")}，算力硬件链批量涨停，AI IPO竞速带来估值重塑，科技行情有望延续。',
                f'全市场约{color("3400家下跌", "green")}，资金高度集中，外围科技股承压，追高容易站岗。',
                f'科技成长方向逻辑通顺，但短期涨幅过大，建议等回调或分批布局有业绩兑现的龙头。'
            ],
            "opinion": f'创业板大涨{color(CYB_CHANGE, "red")}、科创50{color(KC50_CHANGE, "red")}显示科技成长资金回流，但结构性分化极端。建议关注算力、半导体中业绩确定性强的标的，避免盲目追高纯概念股。'
        },
        {
            "title": "美股跳水道指跌1%，节后A股会跟跌吗？",
            "source": "东方财富",
            "heat": "🔥 热议",
            "roles": ["悲观派", "乐观派", "老盛观点"],
            "views": [
                f'道指{color(DJI_CHANGE, "green")}，纳指{color(NDX_CHANGE, "green")}，美联储鹰派信号压制全球风险资产，A股节后大概率承压。',
                f'A股已提前分化，北向资金{color(A_NORTHBOUND, "red")}，科技股独立走强，可能走出独立行情。',
                f'外围波动会通过情绪和估值传导，但A股结构性机会仍在，关键看节后量能能否维持。'
            ],
            "opinion": f'美股三大指数集体收跌对A股情绪有短期冲击，但A股已处于结构分化状态，高股息银行和科技成长各有支撑。建议节前控制仓位，保留现金流应对节后波动。'
        },
        {
            "title": "黄金震荡反弹还能买吗？",
            "source": "集思录",
            "heat": "💰 关注",
            "roles": ["黄金多头", "技术派", "老盛观点"],
            "views": [
                f'国际金价{color(GOLD_CHANGE, "red")}反弹，地缘避险+央行购金逻辑仍在，长期看涨。',
                f'美元指数{color(USD_INDEX_CHANGE, "red")}大涨至{color(USD_INDEX, "cyan")}，美联储鹰派压制金价，短期或震荡。',
                f'黄金作为避险资产适合配置，但不宜重仓追高，注意控制比例。'
            ],
            "opinion": f'黄金反弹{color(GOLD_CHANGE, "red")}至{color(GOLD_PRICE + "美元", "cyan")}，但美元指数走强和美联储鹰派构成压制。建议将黄金作为资产配置的{color("5-10%", "cyan")}避险部分，逢低分批配置，不宜追涨。'
        },
        {
            "title": "高股息银行逆势上涨，还能配置吗？",
            "source": "同花顺",
            "heat": "💰 关注",
            "roles": ["价值投资者", "择时派", "老盛观点"],
            "views": [
                f'银行股息率{color("4.5-5.5%", "red")}，PB仅{color("0.6-0.8倍", "cyan")}，显著高于无风险收益，长期配置价值突出。',
                f'银行板块前期涨幅较大，短期或面临震荡，建议等回调再介入。',
                f'高股息银行适合作为底仓，短期波动不改长期逻辑。'
            ],
            "opinion": f'6月18日工商银行涨0.13%、招商银行涨0.40%，银行板块在市场调整中逆势飘红。当前股息率{color("4.5-5.5%", "red")}、PB{color("0.6-0.8倍", "cyan")}的配置性价比仍高，建议分批建仓，长期持有。'
        },
        {
            "title": "霍尔木兹海峡重开，原油是抄底还是回避？",
            "source": "雪球",
            "heat": "⚠️ 警示",
            "roles": ["抄底派", "风险提示", "老盛观点"],
            "views": [
                f'WTI原油{color(WTI_CHANGE, "green")}至{color(WTI_OIL + "美元", "cyan")}，短期超跌后或有技术性反弹。',
                f'供给改善预期下油价可能继续承压，能源股盈利预期面临下修。',
                f'原油受地缘和美元双重影响，波动较大，普通投资者不建议重仓。'
            ],
            "opinion": f'霍尔木兹海峡重开预期导致油价{color(WTI_CHANGE, "green")}，但这是短期事件冲击。能源股跟油价关联度高，在油价承压和美元走强背景下，{color("不建议盲目抄底", "green")}能源板块。'
        },
        {
            "title": "OpenAI与Anthropic IPO，AI股还能涨多久？",
            "source": "东方财富",
            "heat": "🔥 热议",
            "roles": ["政策解读", "分析师", "投资者"],
            "views": [
                f'头部AI企业上市将带来{color("大规模资本增量", "red")}，算力基础设施直接受益。',
                f'IPO预期强化AI资本开支高增长的确定性，光模块、服务器业绩弹性大。',
                f'需甄别真正有技术实力和订单兑现的公司，规避纯概念炒作。'
            ],
            "opinion": f'OpenAI与Anthropic竞逐IPO将重塑AI板块估值，算力硬件链已提前反应。中长期看好有业绩支撑的AI硬件龙头，但短期注意估值过高风险。'
        },
        {
            "title": "人民币中间价下调34基点，对投资有何影响？",
            "source": "集思录",
            "heat": "💰 关注",
            "roles": ["外汇分析师", "出口企业", "进口企业"],
            "views": [
                f'USD/CNY中间价{color(USD_CNY_MID, "cyan")}，人民币{color("下调34基点", "green")}，出口企业受益。',
                f'贬值利好出口订单，但可能加剧资本外流压力。',
                f'进口成本上升，有外债的企业需加强汇率对冲。'
            ],
            "opinion": f'人民币贬值对出口型企业构成利好，但对进口成本和海外负债形成压力。投资者可关注出口占比较高的制造业，同时避免重仓依赖进口原材料的行业。'
        },
        {
            "title": "美债收益率维持高位，债市还能持有吗？",
            "source": "同花顺",
            "heat": "📊 数据",
            "roles": ["债券分析师", "投资建议", "配置观点"],
            "views": [
                f'美10年期收益率{color(US_10Y, "cyan")}，30年期{color(US_30Y, "cyan")}，高位运行对全球债市有压力。',
                f'中债收益率{color(CN_10Y, "cyan")}低位，中美利差扩大，但国内债市相对独立。',
                f'纯债基金仍可作为稳健资产配置，但需控制久期。'
            ],
            "opinion": f'美债收益率维持高位对全球风险偏好构成压制，但国内中10年期国债收益率仅{color(CN_10Y, "cyan")}，纯债基金保持正收益。建议将债基作为防御底仓，配置比例20-30%。'
        },
        {
            "title": "两市成交约3.11万亿，行情能持续吗？",
            "source": "雪球",
            "heat": "🔥 热议",
            "roles": ["技术派", "谨慎派", "老盛观点"],
            "views": [
                f'成交约{color(A_SHARES_VOLUME, "cyan")}，量能充沛，是行情活跃的积极信号。',
                f'但个股跌多涨少，资金集中在少数热点，持续性存疑。',
                f'放量是必要条件，但能否持续还需看节后量能和热点轮动。'
            ],
            "opinion": f'两市成交约{color(A_SHARES_VOLUME, "cyan")}，量能充沛支撑结构性行情，但资金高度集中。节后需关注成交能否维持在3万亿附近，以及算力链等热点能否扩散。'
        },
        {
            "title": "加密货币BTC大跌4.2%，风险释放完了吗？",
            "source": "东方财富",
            "heat": "⚠️ 警示",
            "roles": ["抄底派", "风险派", "老盛观点"],
            "views": [
                f'BTC{color(BTC_CHANGE, "green")}，ETH{color(ETH_CHANGE, "green")}，短期跌幅较大，或存在超跌反弹。',
                f'BTC ETF净流出，市场情绪谨慎偏空，风险尚未释放完毕。',
                f'加密货币波动极大，普通投资者不建议重仓参与。'
            ],
            "opinion": f'加密货币BTC{color(BTC_CHANGE, "green")}、ETH{color(ETH_CHANGE, "green")}大跌，BTC ETF净流出显示机构情绪谨慎。加密资产风险极高，建议仅用小资金参与，或暂时回避。'
        },
    ]
    for i, topic in enumerate(topics, 1):
        content = replace_placeholder(content, f'{{{{社区话题{i}_标题}}}}', topic['title'])
        content = replace_placeholder(content, f'{{{{社区话题{i}_来源}}}}', topic['source'])
        content = replace_placeholder(content, f'{{{{社区话题{i}_热度}}}}', topic['heat'])
        for j in range(3):
            content = replace_placeholder(content, f'{{{{社区话题{i}_角色{j+1}}}}}', topic['roles'][j])
            content = replace_placeholder(content, f'{{{{社区话题{i}_观点{j+1}}}}}', topic['views'][j])
        content = replace_placeholder(content, f'{{{{社区话题{i}_观点}}}}', topic['opinion'])

    # 10. Tab 7: 今日总结
    content = replace_placeholder(content, '{{宏观面_内容}}',
        f'美联储新任主席沃什释放鹰派信号，美元指数{color(USD_INDEX_CHANGE, "red")}大涨；美伊签署临时协议，霍尔木兹海峡有望重开；人民币中间价{color(USD_CNY_MID, "cyan")}下调34基点。')
    content = replace_placeholder(content, '{{市场面_内容}}',
        f'A股极致分化，上证{color(SH_CHANGE, "green")}，创业板{color(CYB_CHANGE, "red")}，科创50{color(KC50_CHANGE, "red")}；两市成交约{color(A_SHARES_VOLUME, "cyan")}；港股{color(HSI_CHANGE, "green")}重挫；美股三大指数{color("集体收跌", "green")}。')
    content = replace_placeholder(content, '{{资金面_内容}}',
        f'北向资金{color(A_NORTHBOUND, "red")}，结束连续流出；南向资金{color(H_SOUTHBOUND, "green")}；资金从传统蓝筹流向算力、半导体等科技成长方向。')
    content = replace_placeholder(content, '{{操作建议}}',
        f'市场结构分化加剧，建议均衡配置科技成长与高股息防御板块，控制仓位应对端午假期外围波动。')

    # 速查数据（9行）
    quick_data = [
        ("上证指数", SH_COMPONENT, SH_CHANGE, "📈", "var(--green)", "down", "上证"),
        ("深证成指", SZ_COMPONENT, SZ_CHANGE, "📈", "var(--red)", "up", "深证"),
        ("创业板指", CYB_INDEX, CYB_CHANGE, "🚀", "var(--red)", "hot", "创业"),
        ("两市成交", A_SHARES_VOLUME, "放量", "💰", "var(--accent)", "accent", "放量"),
        ("北向资金", A_NORTHBOUND.split('流')[1] if '流入' in A_NORTHBOUND else A_NORTHBOUND, "净流入", "👆", "var(--red)", "up", "北向"),
        ("恒生科技", HSTECH_INDEX, HSTECH_CHANGE, "📊", "var(--green)", "down", "恒科"),
        ("WTI原油", f'${WTI_OIL}', WTI_CHANGE, "🛢️", "var(--green)", "down", "WTI"),
        ("国际黄金", f'${GOLD_PRICE}', GOLD_CHANGE, "🥇", "#f0b429", "hot", "黄金"),
        ("人民币汇率", USD_CNY_MID, "贬值", "💱", "var(--green)", "down", "汇率"),
    ]
    for i, (name, val, chg, icon, col, cls, note) in enumerate(quick_data, 1):
        content = replace_placeholder(content, f'{{{{速查{i}_名称}}}}', name)
        content = replace_placeholder(content, f'{{{{速查{i}_数值}}}}', val)
        content = replace_placeholder(content, f'{{{{速查{i}_涨跌幅}}}}', chg)
        content = replace_placeholder(content, f'{{{{速查{i}_图标}}}}', icon)
        content = replace_placeholder(content, f'{{{{速查{i}_颜色}}}}', col)
        content = replace_placeholder(content, f'{{{{速查{i}_标签class}}}}', cls)
        content = replace_placeholder(content, f'{{{{速查{i}_备注}}}}', note)

    # 宏观/市场/资金子项
    content = replace_placeholder(content, '{{宏观_子标题1}}', '美联储')
    content = replace_placeholder(content, '{{宏观_内容1}}', f'沃什释放鹰派信号，美元指数{color(USD_INDEX_CHANGE, "red")}大涨至{color(USD_INDEX, "cyan")}')
    content = replace_placeholder(content, '{{宏观_子标题2}}', '地缘')
    content = replace_placeholder(content, '{{宏观_内容2}}', '美伊签署临时协议，霍尔木兹海峡有望重开，油价承压')
    content = replace_placeholder(content, '{{宏观_子标题3}}', '汇率')
    content = replace_placeholder(content, '{{宏观_内容3}}', f'USD/CNY中间价{color(USD_CNY_MID, "cyan")}，下调34基点')

    content = replace_placeholder(content, '{{市场_子标题1}}', 'A股')
    content = replace_placeholder(content, '{{市场_内容1}}', f'创业板{color(CYB_CHANGE, "red")}领涨，科创50{color(KC50_CHANGE, "red")}，两市成交{color(A_SHARES_VOLUME, "cyan")}')
    content = replace_placeholder(content, '{{市场_子标题2}}', '美股')
    content = replace_placeholder(content, '{{市场_内容2}}', f'道指{color(DJI_CHANGE, "green")}，纳指{color(NDX_CHANGE, "green")}，科技股承压')
    content = replace_placeholder(content, '{{市场_子标题3}}', '港股')
    content = replace_placeholder(content, '{{市场_内容3}}', f'恒生指数{color(HSI_CHANGE, "green")}，恒生科技{color(HSTECH_CHANGE, "green")}')

    content = replace_placeholder(content, '{{资金_子标题1}}', '北向')
    content = replace_placeholder(content, '{{资金_内容1}}', A_NORTHBOUND)
    content = replace_placeholder(content, '{{资金_子标题2}}', '量能')
    content = replace_placeholder(content, '{{资金_内容2}}', f'两市成交约{color(A_SHARES_VOLUME, "cyan")}')
    content = replace_placeholder(content, '{{资金_子标题3}}', '板块')
    content = replace_placeholder(content, '{{资金_内容3}}', '资金流向算力、半导体等科技成长')

    # 今日操作建议（6条，每条120字以上）
    operations = [
        ("科技成长", f'创业板指{color(CYB_CHANGE, "red")}领涨，科创50{color(KC50_CHANGE, "red")}，算力硬件链批量涨停，北向资金加仓半导体、算力、光通信硬件。',
         'OpenAI/Anthropic IPO竞速提升AI资本开支确定性，但短期涨幅较大。',
         '关注有业绩兑现的算力、半导体龙头，分批布局，避免追高纯概念股。'),
        ("高股息银行", f'银行板块PB约{color("0.6-0.8倍", "cyan")}，股息率{color("4.5-5.5%", "red")}，显著高于10年国债{color(CN_10Y, "cyan")}和货币基金。',
         '6月18日高股息银行股全线飘红，防御属性突出。',
         '长期投资者可分批配置工商银行、招商银行、长江电力等高股息标的。'),
        ("黄金避险", f'国际金价反弹{color(GOLD_CHANGE, "red")}至{color(GOLD_PRICE + "美元", "cyan")}，地缘避险和央行购金提供支撑。',
         '但美元指数走强和美联储鹰派压制金价上行空间。',
         '适度配置5-10%黄金作为避险资产，逢低分批，不宜追涨。'),
        ("稳健理财", f'1年定存{color(CD_1Y, "cyan")}、3年{color(CD_3Y, "cyan")}、5年{color(CD_5Y, "cyan")}，货币基金{color(MMF_YIELD, "green")}，纯债基金正收益。',
         '低利率环境下高股息策略优势明显，银行股息率远超存款和货基。',
         '稳健型投资者可将50-60%资金配置于高股息和纯债基金组合。'),
        ("风险控制", f'全市场约{color("3400家下跌", "green")}，港股{color(HSI_CHANGE, "green")}重挫，美股三大指数{color("集体收跌", "green")}，BTC{color(BTC_CHANGE, "green")}大跌。',
         '端午假期A股休市，外围波动可能传导至节后开盘。',
         '节前控制仓位，保留现金流，避免重仓单一板块。'),
        ("港股低估值", f'恒生指数{color(HSI_CHANGE, "green")}，恒生科技{color(HSTECH_CHANGE, "green")}，港股估值处于历史低位。',
         '高股息银行和科技龙头估值修复空间大，但短期受外围拖累。',
         '关注港股通高股息银行和互联网龙头，逢低分批布局。'),
    ]
    for i, (title, content_line, supplement, action) in enumerate(operations, 1):
        content = replace_placeholder(content, f'{{{{操作建议{i}_标题}}}}', title)
        content = replace_placeholder(content, f'{{{{操作建议{i}_内容}}}}', content_line)
        content = replace_placeholder(content, f'{{{{操作建议{i}_补充}}}}', supplement)
        content = replace_placeholder(content, f'{{{{操作建议{i}_操作}}}}', action)

    # 关键词
    keywords = ['算力链涨停', '美联储鹰派', '黄金反弹', '高股息银行', 'AI IPO竞速', '霍尔木兹重开', '港股低估值', '科技成长']
    for i, kw in enumerate(keywords, 1):
        content = replace_placeholder(content, f'{{{{关键词{i}}}}}', kw)

    # 参考数据
    content = replace_placeholder(content, '{{参考1_标题}}', '涨红跌绿规则')
    content = replace_placeholder(content, '{{参考1_描述}}', '上涨显示红色，下跌显示绿色，与A股软件惯例一致')
    content = replace_placeholder(content, '{{参考2_标题}}', '颜色高亮')
    content = replace_placeholder(content, '{{参考2_描述}}', '重点数据使用彩色高亮显示')
    content = replace_placeholder(content, '{{参考3_标题}}', '数据来源')
    content = replace_placeholder(content, '{{参考3_描述}}', DATA_DATE_FULL + '收盘数据')

    # 理财参考数据
    content = replace_placeholder(content, '{{理财参考1_标题}}', '上证指数')
    content = replace_placeholder(content, '{{理财参考1_标题颜色}}', 'var(--green)')
    content = replace_placeholder(content, '{{理财参考1_数值}}', SH_COMPONENT)
    content = replace_placeholder(content, '{{理财参考1_数值颜色}}', 'var(--green)')
    content = replace_placeholder(content, '{{理财参考1_备注}}', SH_CHANGE)
    content = replace_placeholder(content, '{{理财参考2_标题}}', '深证成指')
    content = replace_placeholder(content, '{{理财参考2_标题颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{理财参考2_数值}}', SZ_COMPONENT)
    content = replace_placeholder(content, '{{理财参考2_数值颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{理财参考2_备注}}', SZ_CHANGE)
    content = replace_placeholder(content, '{{理财参考3_标题}}', '创业板指')
    content = replace_placeholder(content, '{{理财参考3_标题颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{理财参考3_数值}}', CYB_INDEX)
    content = replace_placeholder(content, '{{理财参考3_数值颜色}}', 'var(--red)')
    content = replace_placeholder(content, '{{理财参考3_备注}}', CYB_CHANGE)
    content = replace_placeholder(content, '{{理财参考4_标题}}', '两市成交')
    content = replace_placeholder(content, '{{理财参考4_标题颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考4_数值}}', A_SHARES_VOLUME)
    content = replace_placeholder(content, '{{理财参考4_数值颜色}}', 'var(--accent)')
    content = replace_placeholder(content, '{{理财参考4_备注}}', '量能充沛')
    content = replace_placeholder(content, '{{理财参考5_标题}}', '黄金')
    content = replace_placeholder(content, '{{理财参考5_标题颜色}}', '#f0b429')
    content = replace_placeholder(content, '{{理财参考5_数值}}', f'${GOLD_PRICE}')
    content = replace_placeholder(content, '{{理财参考5_数值颜色}}', '#f0b429')
    content = replace_placeholder(content, '{{理财参考5_备注}}', GOLD_CHANGE)
    content = replace_placeholder(content, '{{理财参考6_标题}}', '人民币汇率')
    content = replace_placeholder(content, '{{理财参考6_标题颜色}}', 'var(--green)')
    content = replace_placeholder(content, '{{理财参考6_数值}}', USD_CNY_MID)
    content = replace_placeholder(content, '{{理财参考6_数值颜色}}', 'var(--green)')
    content = replace_placeholder(content, '{{理财参考6_备注}}', '贬值34基点')

    content = replace_placeholder(content, '{{数据截止日期}}', DATA_DATE_FULL)

    # 11. 后处理：market-row class 与 market-block border 颜色
    BLOCK_START = '<div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">'

    def classify_row(match):
        """根据 market-row 内文本涨跌设置 class"""
        row_html = match.group(0)
        text = re.sub(r'<[^>]+>', ' ', row_html)
        m = re.search(r'([+-]\d+\.?\d*%)', text)
        if m:
            cls = change_class(m.group(1))
        else:
            if any(k in text for k in ['净流入', '净买入', '上涨', '反弹', '流入', '放量']):
                cls = 'up'
            elif any(k in text for k in ['净卖出', '下跌', '重挫', '大跌', '流出', '贬值']):
                cls = 'down'
            else:
                cls = 'neutral'
        return re.sub(r'class="market-val neutral"', f'class="market-val {cls}"', row_html, count=1)

    def find_block_end(html, start_idx):
        """从 market-block 起始位置找到匹配的结束 </div> 位置"""
        depth = 0
        i = start_idx
        while i < len(html):
            if html.startswith('<div', i):
                depth += 1
                i += 4
            elif html.startswith('</div>', i):
                depth -= 1
                i += 6
                if depth == 0:
                    return i
            else:
                i += 1
        return len(html)

    # 逐个处理 market-block
    pos = 0
    while True:
        start = content.find(BLOCK_START, pos)
        if start == -1:
            break
        end = find_block_end(content, start)
        block_html = content[start:end]

        # 处理 block 内每个 market-row
        new_block = re.sub(r'<div class="market-row">.*?</div>', classify_row, block_html, flags=re.DOTALL)

        # 统计 up/down 决定 border 颜色
        ups = new_block.count('class="market-val up"')
        downs = new_block.count('class="market-val down"')
        if ups > downs:
            border_color = '#f85149'
        elif downs > ups:
            border_color = '#3fb950'
        else:
            border_color = 'rgba(255,255,255,0.12)'
        new_block = new_block.replace('border-top:2px solid rgba(255,255,255,0.12);', f'border-top:2px solid {border_color};', 1)

        content = content[:start] + new_block + content[end:]
        pos = start + len(new_block)

    # 12. 写回文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 报告生成完成: {OUTPUT_FILE}")

    # 13. 质量检查统计
    remaining = len(re.findall(r'\{\{[^}]+\}\}', content))
    dash_count = content.count('"--"') + content.count('>--<')
    tab_panels = len(re.findall(r'class="tab-panel(?:\s+active)?"', content))
    sub_titles = len(re.findall(r'class="sub-title"', content))
    stock_cards = len(re.findall(r'class="stock-card"', content))
    market_blocks = len(re.findall(r'class="market-block"', content))
    up_class_neg = len(re.findall(r'class="up"[^>]*>[^<]*-\d', content))
    down_class_pos = len(re.findall(r'class="down"[^>]*>[^<]*\+\d', content))

    print(f"📊 剩余占位符数量: {remaining}")
    print(f"📊 '--' 缺失数据数量: {dash_count}")
    print(f"📊 tab-panel 数量: {tab_panels}")
    print(f"📊 sub-title 数量: {sub_titles}")
    print(f"📊 stock-card 数量: {stock_cards}")
    print(f"📊 market-block 数量: {market_blocks}")
    print(f"📊 class='up' 含负值: {up_class_neg}")
    print(f"📊 class='down' 含正值: {down_class_pos}")

    return remaining


if __name__ == '__main__':
    remaining = main()
    if remaining > 0:
        print(f"⚠️ 警告: 还有 {remaining} 个占位符未替换")
