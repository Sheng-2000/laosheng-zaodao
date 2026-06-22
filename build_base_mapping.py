#!/usr/bin/env python3
# Build base placeholder mapping from raw market data JSON
import json, re
from pathlib import Path

base = Path('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道')
raw = json.loads((base / 'data_market_20260622.json').read_text(encoding='utf-8'))
m = {}

# Header / meta
m['报告日期'] = raw.get('报告日期', '2026年06月22日')
m['YYYY/MM/DD'] = raw.get('YYYY/MM/DD', '2026/06/22')
m['星期'] = raw.get('星期', '星期一')
m['每日重点事件'] = raw.get('每日重点事件', '端午假期后首个交易日·A股港股开市')

m['ticker_上证_数值'] = raw.get('ticker_上证_数值', '4090.48')
m['ticker_上证_涨跌幅'] = raw.get('ticker_上证_涨跌幅', '-0.43%')
m['ticker_道指_数值'] = raw.get('ticker_道指_数值', '51492.55')
m['ticker_道指_涨跌幅'] = raw.get('ticker_道指_涨跌幅', '-0.98%')
m['ticker_黄金_数值'] = raw.get('ticker_黄金_数值', '4294.50')
m['ticker_黄金_涨跌幅'] = raw.get('ticker_黄金_涨跌幅', '+0.43%')

# Summary cards (Tab 0)
m['概览卡1_标题'] = 'A股成交额'
m['概览卡1_数值'] = raw.get('A股_成交额', '3.31万亿')
m['概览卡1_涨跌class'] = 'neutral'
m['概览卡1_涨跌幅'] = '放量2183亿'
m['概览卡1_描述'] = f"6月18日两市成交<span style=\"color:#f0b429;font-weight:700;\">{raw.get('A股_成交额','3.31万亿')}</span>，较昨日<span style=\"color:#f0b429;font-weight:700;\">放量2183亿</span>，连续5日站稳3万亿上方，科技主线交投活跃。"

m['概览卡2_标题'] = '北向资金'
m['概览卡2_数值'] = raw.get('A股_北向资金', '+42.68亿')
m['概览卡2_标签'] = '净流入'
m['概览卡2_描述'] = f"北向资金结束连续流出，净流入<span style=\"color:#f85149;font-weight:700;\">42.68亿元</span>，<span style=\"color:#f85149;font-weight:700;\">半导体、算力、光通信</span>获重点加仓。"

m['概览卡3_标题'] = '科创50'
m['概览卡3_数值'] = raw.get('A股_科创50_数据', '1911.51 +3.84%').split()[0]
m['概览卡3_标签'] = '+3.84%'
m['概览卡3_描述'] = '科创50 <span style="color:#f85149;font-weight:700;">大涨3.84%</span>创历史新高，硬科技全线爆发，算力、芯片、光模块领涨。'

m['概览卡4_标题'] = '美股道指'
m['概览卡4_数值'] = raw.get('ticker_道指_数值', '51492.55')
m['概览卡4_标签'] = '-0.98%'
m['概览卡4_描述'] = '美东6月18日道指<span style="color:#3fb950;font-weight:700;">下跌0.98%</span>，美联储点阵图偏鹰压制风险偏好，三大指数集体收跌。'

# 8 highlights (Tab 0) - programmatic
highlights = [
    ('A股结构性分化', '#f0b429',
     f"6月18日沪指<span style=\"color:#3fb950;font-weight:700;\">下跌0.43%</span>报4090.48点，深证成指<span style=\"color:#f85149;font-weight:700;\">上涨0.94%</span>，创业板指<span style=\"color:#f85149;font-weight:700;\">大涨2.05%</span>，<span style=\"color:#f85149;font-weight:700;\">科创50涨3.84%</span>领涨，超七成个股下跌。"),
    ('北向回流科技', '#f0b429',
     '北向资金净流入42.68亿元，<span style="color:#f85149;font-weight:700;">结束连续流出</span>，资金高度集中布局<span style="color:#f85149;font-weight:700;">半导体、算力、光通信硬件</span>，<span style="color:#f0b429;font-weight:700;">规避金融周期板块</span>。'),
    ('政策定调直融', '#00d4ff',
     '<span style="color:#f0b429;font-weight:700;">陆家嘴论坛</span>释放信号：<span style="color:#f85149;font-weight:700;">股债融资首超贷款</span>，<span style="color:#f85149;font-weight:700;">直接融资比重持续提升</span>，资本市场改革深化<span style="color:#f85149;font-weight:700;">利好长期资金面</span>。'),
    ('美联储放鹰', '#00d4ff',
     '6月18日美联储维持利率<span style="color:#00d4ff;font-weight:700;">3.50%-3.75%</span>不变，点阵图显示9位官员认为年内需加息一次，<span style="color:#3fb950;font-weight:700;">美股三大指数尾盘跳水收跌</span>。'),
    ('银行股息稳健', '#f85149',
     f"银行板块整体PB仅<span style=\"color:#00d4ff;font-weight:700;\">{raw.get('估值_银行PB','0.63')}倍</span>，股息率约<span style=\"color:#f85149;font-weight:700;\">{raw.get('估值_银行股息率','4.95%')}</span>，险资与长线资金持续加仓，<span style=\"color:#f85149;font-weight:700;\">高股息防御属性</span>凸显。"),
    ('AI硬科技爆发', '#f85149',
     '节前最后一个交易日，<span style="color:#f85149;font-weight:700;">半导体、PCB、MLCC、玻璃基板</span>等AI硬件方向全面爆发，寒武纪大涨超14%创历史新高，中际旭创总市值超越五粮液。'),
    ('港股受外围拖累', '#bc8cff',
     '港股6月18日<span style="color:#3fb950;font-weight:700;">恒指收跌1.59%</span>，恒生科技跌1.39%，南向资金净卖出67.92亿港元，受美联储鹰派信号与假期前避险情绪双重影响。'),
    ('大宗商品分化', '#bc8cff',
     f"国际黄金反弹至<span style=\"color:#f85149;font-weight:700;\">4294.50美元/盎司</span>，WTI原油<span style=\"color:#3fb950;font-weight:700;\">下跌0.25%</span>至74.82美元，白银<span style=\"color:#f85149;font-weight:700;\">上涨1.85%</span>，大宗整体呈现避险与工业需求博弈。")
]
for i,(title,color,body) in enumerate(highlights,1):
    m[f'要点{i}_标题'] = title
    m[f'要点{i}_内容'] = body

# Timeline (Tab 0)
timeline = [
    ('17','06','政策','陆家嘴论坛开幕','央行行长潘功胜宣布完善短端利率调控、创设境外央行回购工具等举措。'),
    ('18','06','市场','A股端午前收官','极致分化：科创50大涨3.84%创新高，上证收跌0.43%，成交3.31万亿。'),
    ('18','06','海外','美联储利率决议','维持3.50%-3.75%不变，点阵图偏鹰，美股三大指数跳水收跌。'),
    ('22','06','今日','A股港股恢复交易','端午假期后首个交易日，关注假期消息面消化与北向资金流向。')
]
for i,(day,mon,tag,event,detail) in enumerate(timeline,1):
    m[f'时间线{i}_日'] = day
    m[f'时间线{i}_月'] = mon
    m[f'时间线{i}_标签'] = tag
    m[f'时间线{i}_事件'] = event
    m[f'时间线{i}_详情'] = detail

# Market data (Tab 3)
m['A股_收盘日期'] = raw.get('A股_收盘日期','6月18日')
m['A股_上证指数_数据'] = raw.get('A股_上证指数_数据','4090.48 -0.43%')
m['A股_深证成指_数据'] = raw.get('A股_深证成指_数据','16030.70 +0.94%')
m['A股_创业板指_数据'] = raw.get('A股_创业板指_数据','4252.39 +2.05%')
m['A股_科创50_数据'] = raw.get('A股_科创50_数据','1911.51 +3.84%')
m['A股_沪深300_数据'] = raw.get('A股_沪深300_数据','4941.60 +0.21%')
m['A股_成交额'] = raw.get('A股_成交额','3.31万亿')
m['A股_成交额备注'] = raw.get('A股_成交额备注','较昨日放量2183亿')
m['A股_涨跌家数'] = raw.get('A股_涨跌家数','上涨1948家 / 下跌3443家')
m['A股_北向资金'] = raw.get('A股_北向资金','+42.68亿')

m['港股_收盘日期'] = raw.get('港股_收盘日期','6月18日')
m['港股_恒生指数_数据'] = raw.get('港股_恒生指数_数据','23924.81 -1.59%')
m['港股_恒生科技_数据'] = raw.get('港股_恒生科技指数_数据','4604.35 -1.39%')
m['港股_国企指数_数据'] = raw.get('港股_国企指数_数据','7976.04 -2.06%')
m['港股_南向资金'] = '净卖出67.92亿港元'

m['美股_收盘日期'] = raw.get('美股_收盘日期','6月18日')
m['美股_道琼斯_涨跌幅'] = '51492.55 -0.98%'
m['美股_标普500_涨跌幅'] = '7420.10 -1.21%'
m['美股_纳斯达克_涨跌幅'] = '26021.66 -1.34%'
m['美股_英伟达_涨跌幅'] = '英伟达 -1.33%'
m['美股_特斯拉_涨跌幅'] = '特斯拉 -2.50%'
m['美股_ARM'] = 'ARM +5.00%'

m['亚太_收盘日期'] = raw.get('亚太_收盘日期','6月19日')
m['亚太_日经225'] = raw.get('亚太_日经225_数据','71250.06 +0.28%')
m['亚太_韩国KOSPI_状态'] = raw.get('亚太_韩国KOSPI_数据','9049.03 -0.16%')
m['亚太_台湾加权_状态'] = raw.get('亚太_台湾加权_数据','46465.20 +1.28%')
m['亚太_印度Sensex_状态'] = raw.get('亚太_印度Sensex_数据','76802.90 -0.79%')
m['亚太_澳洲ASX200_状态'] = raw.get('亚太_澳洲ASX200_数据','8828.70 -0.90%')

m['欧洲_收盘日期'] = raw.get('欧洲_收盘日期','6月19日')
m['欧洲_英国富时100_涨跌幅'] = raw.get('欧洲_英国富时100_数据','10363.27 -0.35%')
m['欧洲_德国DAX30_涨跌幅'] = raw.get('欧洲_德国DAX_数据','24985.82 -0.16%')
m['欧洲_法国CAC40_涨跌幅'] = raw.get('欧洲_法国CAC40_数据','8421.14 -0.55%')
m['欧洲_斯托克50_涨跌幅'] = raw.get('欧洲_欧洲斯托克50_数据','5717.65 -0.54%')

m['大宗商品_收盘日期'] = raw.get('大宗商品_收盘日期','6月18日')
m['大宗_WTI原油'] = raw.get('大宗商品_WTI原油_数据','74.82美元/桶 -0.25%')
m['大宗_布伦特原油'] = raw.get('大宗商品_布伦特原油_数据','78.16美元/桶 -0.50%')
m['大宗_国际黄金'] = raw.get('大宗商品_黄金_数据','4294.50美元/盎司 +0.43%')
m['大宗_上海金'] = raw.get('大宗商品_沪金_数据','938.92元/克 -0.46%')
m['大宗_白银'] = '69.22美元/盎司 +1.85%'

m['汇率债券_收盘日期'] = raw.get('汇率债券_收盘日期','6月18日')
m['汇率_USD/CNY中间价'] = raw.get('汇率债券_美元兑人民币中间价_数据','6.8130')
m['汇率_在岸汇率'] = raw.get('汇率债券_在岸人民币_数据','6.7569')
m['汇率_美元指数'] = raw.get('汇率债券_美元指数_数据','100.846 +0.75%')
m['汇率_美10年期'] = '4.489% +5.34BP'
m['汇率_美30年期'] = '4.929% -1.40BP'
m['汇率_中10年期'] = raw.get('汇率债券_中债10年_数据','1.7240% +0.10BP')

m['加密货币_收盘日期'] = raw.get('加密货币_收盘日期','6月22日')
m['加密_BTC'] = raw.get('加密货币_比特币_数据','64200.00美元 +0.55%')
m['加密_ETH'] = raw.get('加密货币_以太坊_数据','1705.79美元 -1.92%')
m['加密_BTCEFT'] = '本周净流出2.27亿美元'
m['加密_市场情绪'] = '谨慎偏空'

# Market review (Tab 3) placeholders - programmatic
m['市场综评_日期'] = '6月18日'
m['综评_A股行情标题'] = 'A股结构性行情'
m['综评_A股行情标签'] = '分化加剧'
m['综评_A股段落1'] = '6月18日A股呈现<span style="color:#f85149;font-weight:700;">极致分化</span>格局：科创50 <span style="color:#f85149;font-weight:700;">大涨3.84%</span>领跑并创历史新高，创业板指<span style="color:#f85149;font-weight:700;">涨2.05%</span>刷新阶段新高，但沪指<span style="color:#3fb950;font-weight:700;">跌0.43%</span>，超七成个股收跌。AI硬科技与传统周期形成鲜明对照。'
m['综评_A股段落2'] = '资金层面，两市成交3.31万亿连续5日站稳3万亿，北向资金净流入42.68亿元，<span style="color:#f85149;font-weight:700;">半导体、算力、光通信</span>成为外资加仓重点，而保险、火电、地产遭机构兑现。'
m['综评_A股段落3'] = '技术上看，沪指短期支撑<span style="color:#f0b429;font-weight:700;">4070-4080点</span>，压力<span style="color:#f0b429;font-weight:700;">4110-4130点</span>；科创/创业板量价同步新高，AI硬件主线趋势未破。'

m['综评_外围市场标题'] = '外围市场承压'
m['综评_外围市场标签'] = '鹰派压制'
m['综评_外围段落1'] = '美东6月18日美股三大指数集体收跌，道指<span style="color:#3fb950;font-weight:700;">跌0.98%</span>，标普<span style="color:#3fb950;font-weight:700;">跌1.21%</span>，纳指<span style="color:#3fb950;font-weight:700;">跌1.34%</span>，美联储点阵图偏鹰引发尾盘跳水，大型科技股普遍下挫。'
m['综评_外围段落2'] = '亚太市场6月19日涨跌互现：日经225 <span style="color:#f85149;font-weight:700;">涨0.28%</span>，台湾加权<span style="color:#f85149;font-weight:700;">涨1.28%</span>再创收盘新高，但韩国KOSPI <span style="color:#3fb950;font-weight:700;">跌0.16%</span>，印度Sensex <span style="color:#3fb950;font-weight:700;">跌0.79%</span>，澳洲ASX200 <span style="color:#3fb950;font-weight:700;">跌0.90%</span>。'
m['综评_外围段落3'] = '欧洲6月19日主要股指普跌，斯托克50 <span style="color:#3fb950;font-weight:700;">跌0.54%</span>，法国CAC40 <span style="color:#3fb950;font-weight:700;">跌0.55%</span>，英国富时100 <span style="color:#3fb950;font-weight:700;">跌0.35%</span>，德国DAX <span style="color:#3fb950;font-weight:700;">跌0.16%</span>。'

m['综评_地缘政策标题'] = '政策与地缘'
m['综评_地缘政策标签'] = '关注中东'
m['综评_地缘段落1'] = '2026陆家嘴论坛释放资本市场改革大礼包：科创板第五套标准扩围至AI大模型、推出储架发行、支持主动ETF，直接融资地位进一步提升，<span style="color:#f85149;font-weight:700;">利好科技股与长期资金入市</span>。'
m['综评_地缘段落2'] = '央行行长潘功胜宣布完善短端利率调控、创设境外央行回购工具、上海自贸区离岸人民币交易试点等，货币政策框架向价格型转型，<span style="color:#f85149;font-weight:700;">人民币汇率稳定机制再升级</span>。'
m['综评_地缘段落3'] = '地缘层面，美伊临时协议签署后霍尔木兹海峡重开，原油地缘溢价回落；但中东局势仍有反复，黄金维持高位震荡，需关注后续谈判进展。'

m['综评_风险事件标题'] = '风险事件'
m['综评_风险事件标签'] = '警惕波动'
m['综评_风险段落1'] = '美联储点阵图显示9位官员认为年内需加息一次，主席沃什首秀偏鹰，<span style="color:#3fb950;font-weight:700;">全球风险资产估值承压</span>，美债收益率上行，高估值科技股短期波动加大。'
m['综评_风险段落2'] = 'A股内部结构分化加剧，超七成个股下跌而指数受权重股与科技股支撑，<span style="color:#f0b429;font-weight:700;">个股与指数背离</span>，若节后量能无法持续，需防范追涨风险。'
m['综评_风险段落3'] = '假期期间海外市场已交易两个交易日，A股今日开盘存在<span style="color:#f0b429;font-weight:700;">补跌或补涨</span>可能，建议控制仓位，优先关注业绩确定性高的高股息与AI硬件龙头。'

# Market sentiment (Tab 3)
m['市场情绪_状态颜色'] = 'yellow'
m['市场情绪_状态'] = '结构性分化'
m['市场情绪_涨跌比'] = '涨跌比 1:1.77'
m['市场情绪_成交额'] = '成交额 3.31万亿'
m['市场情绪_北向资金'] = '北向 +42.68亿'

# 13 stocks (Tab 5) - fill numeric only
stock_order = ['工商银行','建设银行','农业银行','招商银行','宁波银行','江苏银行','杭州银行','重庆银行','长江电力','大秦铁路','中国移动','中国核电','中国平安']
for i,name in enumerate(stock_order,1):
    m[f'标的{i}_名称'] = raw.get(f'标的{i}_名称', name)
    m[f'标的{i}_代码'] = ['601398','601939','601288','600036','002142','600919','600926','601963','600900','601006','600941','601985','601318'][i-1]
    m[f'标的{i}_股价'] = raw.get(f'标的{i}_股价','--')
    chg = raw.get(f'标的{i}_涨跌幅','0.00%')
    m[f'标的{i}_涨跌幅'] = chg
    m[f'标的{i}_涨跌class'] = 'up' if float(chg.replace('%','').replace('+',''))>=0 else 'down'

# Valuation references
m['估值_银行PB'] = raw.get('估值_银行PB','0.63')
m['估值_上证PE'] = raw.get('估值_上证PE','10.21')
m['估值_银行股息率'] = raw.get('估值_银行股息率','4.95%')
m['估值_中证红利PE'] = raw.get('估值_中证红利PE','7.20')
m['估值_神华吨煤利润'] = raw.get('估值_神华吨煤利润','189元/吨')
m['估值_中国移动PB'] = raw.get('估值_中国移动PB','1.40')
m['估值_招商银行PB'] = raw.get('估值_招商银行PB','0.83')
m['估值_中国核电PE'] = raw.get('估值_中国核电PE','20.16')
m['估值_黄金价格'] = raw.get('估值_黄金价格','938.92元/克')

# Quick reference (Tab 7) - 8 items
refs = [
    ('📈','上证指数','red','4090.48','down','-0.43%'),
    ('📊','深证成指','red','16030.70','up','+0.94%'),
    ('🚀','创业板指','red','4252.39','up','+2.05%'),
    ('💰','两市成交','yellow','3.31万亿','neutral','放量2183亿'),
    ('🌐','北向资金','red','+42.68亿','up','净流入'),
    ('🇭🇰','恒生科技','green','4604.35','down','-1.39%'),
    ('🛢️','WTI原油','green','74.82美元','down','-0.25%'),
    ('🪙','国际黄金','red','4294.50美元','up','+0.43%'),
    ('💱','USD/CNY','neutral','6.8130','neutral','中间价')
]
for i,(icon,name,color,val,tagclass,tag) in enumerate(refs,1):
    m[f'速查{i}_图标'] = icon
    m[f'速查{i}_名称'] = name
    m[f'速查{i}_颜色'] = color
    m[f'速查{i}_数值'] = val
    m[f'速查{i}_标签class'] = tagclass
    m[f'速查{i}_备注'] = tag

m['数据截止日期'] = '2026年6月22日'

# Save
out = base / 'data_base_20260622.json'
out.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding='utf-8')
print('Saved', out, len(m), 'placeholders')
