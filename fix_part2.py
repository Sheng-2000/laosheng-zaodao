#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正 - Part2: Tab0 要点卡片8张"""

file_path = "/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260610.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# Tab 0 要点卡片 - 一次性替换全部
old = """    <!-- 01 以伊冲突缓和 -->
    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(0,212,255,0.03));border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#00d4ff,#0099cc);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">01</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#00d4ff;font-weight:700;font-size:14px;">以伊冲突现缓和迹象</span>，特朗普公开呼吁以色列立即停火并接受美伊协议，伊朗方面表示愿意在联合国框架下谈判，霍尔木兹海峡航运压力有所缓解，布伦特原油自高点回落至约<span style="color:#f85149;font-weight:700;">92.80美元</span>。
      </div>
    </div>
    <!-- 02 超级央行周 -->
    <div style="background:linear-gradient(135deg,rgba(240,180,41,0.1),rgba(240,180,41,0.03));border:1px solid rgba(240,180,41,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f0b429,#d29922);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">02</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f0b429;font-weight:700;font-size:14px;">超级央行周正式开启</span>，美联储、欧央行、日央行本周相继议息。市场预期美联储按兵不动维持利率，但鲍威尔表态偏鹰，利率互换市场定价年内降息概率降至<span style="color:#3fb950;font-weight:700;">38%</span>。中国央行续作MLF，操作利率维持2.00%。
      </div>
    </div>
    <!-- 03 A股结构性行情 -->
    <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f85149,#cc0000);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">03</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f85149;font-weight:700;font-size:14px;">A股结构性行情凸显</span>，沪指收<span style="color:#f85149;font-weight:700;">3987.26点涨0.71%</span>，银行、保险、电力等高股息板块领涨，煤炭、石油石化同步走强。科技成长板块延续调整，科创50小幅下跌0.42%，两市成交额约<span style="color:#00d4ff;font-weight:700;">26481亿元</span>。
      </div>
    </div>
    <!-- 04 美股震荡反弹 -->
    <div style="background:linear-gradient(135deg,rgba(63,185,80,0.1),rgba(63,185,80,0.03));border:1px solid rgba(63,185,80,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#3fb950,#22c55e);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">04</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#3fb950;font-weight:700;font-size:14px;">美股震荡反弹</span>，道指涨<span style="color:#f85149;font-weight:700;">0.54%</span>报51142.30点，标普500涨<span style="color:#f85149;font-weight:700;">0.83%</span>，纳指涨<span style="color:#f85149;font-weight:700;">1.07%</span>。芯片股企稳回升，英伟达涨2.18%，AMD涨3.42%，ARM涨4.16%。市场情绪较昨日明显修复。
      </div>
    </div>
    <!-- 05 央行操作 -->
    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(0,212,255,0.03));border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#00d4ff,#0099cc);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">05</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#00d4ff;font-weight:700;font-size:14px;">央行续作MLF+逆回购</span>，中国人民银行开展<span style="color:#f85149;font-weight:700;">5000亿元</span>MLF操作和<span style="color:#f85149;font-weight:700;">2000亿元</span>7天期逆回购操作，利率均维持不变。本月MLF到期<span style="color:#3fb950;font-weight:700;">1500亿元</span>，实现中期流动性净投放<span style="color:#f85149;font-weight:700;">3500亿元</span>，呵护市场流动性。
      </div>
    </div>
    <!-- 06 北向资金 -->
    <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f85149,#cc0000);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">06</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f85149;font-weight:700;font-size:14px;">北向资金净买入68.45亿</span>，北向资金全天净流入<span style="color:#f85149;font-weight:700;">68.45亿元</span>，其中沪股通净买入42.38亿元，深股通净买入26.07亿元，<span style="color:#f0b429;font-weight:700;">连续9个交易日净买入</span>。前十大成交个股中，工商银行、农业银行、长江电力获净买入居前。
      </div>
    </div>
    <!-- 07 黄金高位震荡 -->
    <div style="background:linear-gradient(135deg,rgba(240,180,41,0.1),rgba(240,180,41,0.03));border:1px solid rgba(240,180,41,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f0b429,#d29922);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">07</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f0b429;font-weight:700;font-size:14px;">黄金高位震荡偏强</span>，伦敦金现盘中最高触及<span style="color:#f85149;font-weight:700;">4326美元/盎司</span>，收盘报<span style="color:#f85149;font-weight:700;">4318美元/盎司涨0.77%</span>。中国央行黄金储备连续第20个月增加，5月环比增持<span style="color:#00d4ff;font-weight:700;">35万盎司</span>。地缘风险叠加去美元化趋势，支撑金价长期上行。
      </div>
    </div>
    <!-- 08 比特币箱体整理 -->
    <div style="background:linear-gradient(135deg,rgba(188,140,255,0.1),rgba(188,140,255,0.03));border:1px solid rgba(188,140,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#bc8cff,#9a6de0);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">08</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#bc8cff;font-weight:700;font-size:14px;">比特币箱体整理</span>，BTC在<span style="color:#00d4ff;font-weight:700;">63000-65800美元</span>区间震荡，日内微涨0.68%报<span style="color:#f85149;font-weight:700;">63385美元</span>。以太坊涨1.85%至3412美元。美比特币现货ETF净买入<span style="color:#f85149;font-weight:700;">1.24亿美元</span>，结束连续两日净流出。
      </div>
    </div>"""

new = """    <!-- 01 以伊冲突骤然升级 -->
    <div style="background:linear-gradient(135deg,rgba(240,180,41,0.1),rgba(240,180,41,0.03));border:1px solid rgba(240,180,41,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f0b429,#d29922);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">01</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f0b429;font-weight:700;font-size:14px;">以伊冲突骤然升级</span>，以色列打击伊朗西部和中部军事目标，伊朗革命卫队称以色列开启危险行动，也门胡塞武装宣布对以色列发动攻击，中东地缘风险急剧升温，全球市场避险情绪飙升。
      </div>
    </div>
    <!-- 02 韩国KOSPI熔断 -->
    <div style="background:linear-gradient(135deg,rgba(240,180,41,0.1),rgba(240,180,41,0.03));border:1px solid rgba(240,180,41,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f0b429,#d29922);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">02</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f0b429;font-weight:700;font-size:14px;">韩国KOSPI触发熔断</span>，韩国综合指数暴跌8.29%报7484.41点，盘中跌幅超8%触发熔断机制交易暂停20分钟，三星电子和SK海力士均跌超10%，为2026年内第三次熔断。
      </div>
    </div>
    <!-- 03 央行逆回购 -->
    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(0,212,255,0.03));border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#00d4ff,#0099cc);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">03</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#00d4ff;font-weight:700;font-size:14px;">央行2185亿逆回购</span>，中国人民银行开展2185亿元7天期逆回购操作，操作利率1.40%，全额满足一级交易商需求，6月9日有110亿元逆回购到期，实现净投放2075亿元，维护流动性合理充裕。
      </div>
    </div>
    <!-- 04 英伟达Vera Rubin -->
    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(0,212,255,0.03));border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#00d4ff,#0099cc);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">04</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#00d4ff;font-weight:700;font-size:14px;">英伟达发布Vera Rubin</span>，COMPUTEX 2026展会上英伟达发布全新PC端CPU芯片，同时宣布Vera Rubin加速器计划，三大存储芯片制造商已通过HBM认证，黄仁勋称行业仍处于AI基础设施修建早期阶段。
      </div>
    </div>
    <!-- 05 北向资金连续8日净买入 -->
    <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f85149,#cc0000);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">05</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f85149;font-weight:700;font-size:14px;">北向资金连续8日净买入</span>，截至6月9日北向资金连续8个交易日净买入，刷新今年以来最长连续净买入纪录，外资用真金白银表达对中国资产的信心，重点加仓银行、保险等低估值板块。
      </div>
    </div>
    <!-- 06 银行股逆势抗跌 -->
    <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f85149,#cc0000);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">06</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f85149;font-weight:700;font-size:14px;">银行股逆势抗跌</span>，在A股全线大跌的背景下，银行板块整体抗跌，银行AH优选ETF逆势上涨0.54%，中证银行指数股息率达5.05%，远超10年期国债收益率1.71%，高股息优势凸显。
      </div>
    </div>
    <!-- 07 全球半导体板块崩跌 -->
    <div style="background:linear-gradient(135deg,rgba(188,140,255,0.1),rgba(188,140,255,0.03));border:1px solid rgba(188,140,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#bc8cff,#9a6de0);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">07</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#bc8cff;font-weight:700;font-size:14px;">全球半导体板块崩跌</span>，费城半导体指数大跌超10%创2020年3月以来最大跌幅，ARM跌12.84%，英特尔跌11.28%，高通跌10.98%，AMD跌10.86%，AI交易过热担忧引发全球科技股集中抛售。
      </div>
    </div>
    <!-- 08 油价地缘溢价飙升 -->
    <div style="background:linear-gradient(135deg,rgba(188,140,255,0.1),rgba(188,140,255,0.03));border:1px solid rgba(188,140,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#bc8cff,#9a6de0);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">08</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#bc8cff;font-weight:700;font-size:14px;">油价地缘溢价飙升</span>，受以伊冲突升级影响，布伦特原油一度突破96美元/桶涨幅3.6%，WTI原油逼近94美元，此后因特朗普表态有所回落，收盘WTI约90.53美元，布伦特约93.72美元。
      </div>
    </div>"""

if old in html:
    html = html.replace(old, new)
    changes.append("✓ Tab0 要点卡片8张")
else:
    print("✗ Tab0 要点卡片 NOT FOUND")
    # 调试：打印前100字符看看文件当前状态
    idx = html.find("<!-- 01")
    print(f"找到 <!-- 01 位置: {idx}")
    if idx > 0:
        print(html[idx:idx+200])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

for c in changes:
    print(c)
if not changes:
    print("没有任何替换成功！")
