#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正 - Part4: Tab3 市场综评4维度卡片"""

file_path = "/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260610.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

changes = []

# 维度1: A股行情
old1 = """        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🇨🇳</span>
          <span style="font-size:14px;font-weight:700;color:#f85149;">A股结构性反弹，银行高股息领涨</span>
          <span style="margin-left:auto;font-size:11px;color:#f85149;background:rgba(248,81,73,0.15);padding:2px 8px;border-radius:10px;">偏多</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">6月10日周三，A股三大指数全线收涨，上证指数涨<span style="color:#f85149;font-weight:600;">0.71%</span>报<span style="color:#f85149;font-weight:600;">3987.26</span>点，深证成指涨<span style="color:#f85149;font-weight:600;">0.68%</span>，创业板指涨<span style="color:#f85149;font-weight:600;">0.85%</span>，科创50涨<span style="color:#f85149;font-weight:600;">1.12%</span>。沪深300指数涨<span style="color:#f85149;font-weight:600;">0.94%</span>，市场呈现结构性修复特征。沪深两市成交额<span style="color:#f0b429;font-weight:600;">28562.40亿元</span>，连续<span style="color:#f0b429;font-weight:600;">33个交易日</span>超2.5万亿，交投维持活跃。</p>
          <p style="margin-bottom:8px;">全市场上涨<span style="color:#3fb950;font-weight:600;">2865只</span>，下跌<span style="color:#f85149;font-weight:600;">2624只</span>，涨跌比约<span style="color:#f85149;font-weight:600;">52:48</span>，显示市场情绪显著改善。银行、保险、电力等高股息板块表现强势，<span style="color:#f85149;font-weight:600;">中证银行指数涨1.85%</span>，工行、建行齐创阶段新高。科技股经历回调后企稳反弹，半导体、算力硬件板块小幅收涨。</p>
          <p style="font-size:12px;color:#8b95a5;">北向资金连续9日净买入，累计净买入规模持续扩大。技术面上，上证指数在3900点附近获得支撑，银行高股息板块成为市场稳定器，低估值防御策略获得资金共识。</p>"""
new1 = """        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🇨🇳</span>
          <span style="font-size:14px;font-weight:700;color:#f85149;">A股三大指数全线收跌，沪指失守4000点</span>
          <span style="margin-left:auto;font-size:11px;color:#8b95a5;background:rgba(139,149,165,0.15);padding:2px 8px;border-radius:10px;">偏空</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">6月9日周二，A股三大指数全线收跌，上证指数跌<span style="color:#f85149;font-weight:600;">1.70%</span>报<span style="color:#f85149;font-weight:600;">3959.34</span>点失守4000点关口，深证成指跌<span style="color:#f85149;font-weight:600;">3.22%</span>，创业板指跌<span style="color:#f85149;font-weight:600;">3.69%</span>，科创50大跌<span style="color:#f85149;font-weight:600;">4.30%</span>。沪深300指数跌<span style="color:#f85149;font-weight:600;">2.14%</span>，市场普跌。沪深两市成交额<span style="color:#f0b429;font-weight:600;">27927.61亿元</span>，连续<span style="color:#f0b429;font-weight:600;">31个交易日</span>超2.5万亿，较前一交易日缩量约9%。</p>
          <p style="margin-bottom:8px;">全市场上涨仅<span style="color:#3fb950;font-weight:600;">898只</span>，下跌<span style="color:#f85149;font-weight:600;">4591只</span>，涨跌比约<span style="color:#f85149;font-weight:600;">16:84</span>，市场恐慌情绪升温。仅北证50逆势上涨1.33%。银行、电力等高股息板块相对抗跌，科技成长板块遭集中抛售，半导体、算力硬件板块大幅下挫。内资主力净流出超<span style="color:#f85149;font-weight:600;">440亿元</span>。</p>
          <p style="font-size:12px;color:#8b95a5;">北向资金逆势净买入，连续8日净流入。技术面上，上证指数跌破4000点整数关口，短期形态承压。银行高股息板块成为资金避风港，低估值防御策略凸显价值。</p>"""

# 维度2: 外围市场
old2 = """        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🌍</span>
          <span style="font-size:14px;font-weight:700;color:#3fb950;">全球股市震荡反弹，科技股企稳</span>
          <span style="margin-left:auto;font-size:11px;color:#3fb950;background:rgba(63,185,80,0.15);padding:2px 8px;border-radius:10px;">回暖</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">亚太市场普遍反弹，韩国KOSPI涨<span style="color:#f85149;font-weight:600;">2.68%</span>收复部分失地，日经225涨<span style="color:#f85149;font-weight:600;">1.30%</span>，台湾加权涨约<span style="color:#f85149;font-weight:600;">1.85%</span>。欧洲股市盘中全线上涨，英国富时100涨<span style="color:#f85149;font-weight:600;">0.62%</span>，德国DAX涨<span style="color:#f85149;font-weight:600;">0.85%</span>，法国CAC40涨<span style="color:#f85149;font-weight:600;">0.76%</span>。</p>
          <p style="margin-bottom:8px;">美股隔夜（6月9日）企稳反弹，道指涨<span style="color:#f85149;font-weight:600;">0.54%</span>，标普500涨<span style="color:#f85149;font-weight:600;">0.79%</span>，纳指涨<span style="color:#f85149;font-weight:600;">0.93%</span>。科技股止跌回升，英伟达反弹<span style="color:#f85149;font-weight:600;">3.76%</span>报$212.80，特斯拉涨<span style="color:#f85149;font-weight:600;">2.18%</span>，ARM涨<span style="color:#f85149;font-weight:600;">4.52%</span>。费城半导体指数反弹<span style="color:#f85149;font-weight:600;">2.85%</span>，缓解了市场对科技股泡沫破裂的担忧。</p>
          <p style="font-size:12px;color:#8b95a5;">全球风险资产从恐慌抛售中逐步企稳。以伊冲突缓和推动油价回落，布油跌破93美元。黄金受避险需求支撑回升至4318美元。美债收益率回落，10年期降至4.48%，市场重新定价美联储政策路径。</p>"""
new2 = """        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🌍</span>
          <span style="font-size:14px;font-weight:700;color:#3fb950;">全球风险资产遭遇集中抛售，科技股重挫</span>
          <span style="margin-left:auto;font-size:11px;color:#8b95a5;background:rgba(139,149,165,0.15);padding:2px 8px;border-radius:10px;">恐慌</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">亚太市场全线暴跌，韩国KOSPI暴跌<span style="color:#f85149;font-weight:600;">8.29%</span>触发熔断，三星电子、SK海力士均跌超10%。日经225跌<span style="color:#f85149;font-weight:600;">3.85%</span>报64024.60点，台湾加权指数跌约<span style="color:#f85149;font-weight:600;">6%</span>，台积电跌5.7%。澳洲ASX200下跌约1%报8641点。</p>
          <p style="margin-bottom:8px;">美股隔夜（6月9日）全线重挫，道指跌<span style="color:#f85149;font-weight:600;">1.35%</span>报50866.78点，标普500跌<span style="color:#f85149;font-weight:600;">2.64%</span>报7383.74点，纳指暴跌<span style="color:#f85149;font-weight:600;">4.18%</span>报25709.43点。半导体板块大幅下挫，费城半导体指数大跌超10%创2020年3月以来最大跌幅，<span style="color:#f85149;font-weight:600;">ARM跌12.84%，英伟达跌6.20%报$205.10</span>，特斯拉跌6.56%。</p>
          <p style="font-size:12px;color:#8b95a5;">非农数据超预期叠加以伊冲突升级，形成极强跟风杀跌氛围。市场重新预期美联储12月前加息25个基点。美债收益率上行，10年期升至4.55%，美元指数走强至100.06。</p>"""

# 维度3: 地缘政策
old3 = """        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🏛️</span>
          <span style="font-size:14px;font-weight:700;color:#f0b429;">以伊冲突缓和，超级央行周来临</span>
          <span style="margin-left:auto;font-size:11px;color:#f0b429;background:rgba(240,180,41,0.15);padding:2px 8px;border-radius:10px;">关注</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">特朗普公开呼吁以色列"只能接受美伊协议"，要求双方<span style="color:#f85149;font-weight:600;">立即停火</span>。伊朗方面表示愿意在联合国框架下进行谈判，霍尔木兹海峡航运压力显著缓解。布伦特原油从高点回落至<span style="color:#f0b429;font-weight:600;">92.80美元/桶</span>，地缘溢价明显收窄。</p>
          <p style="margin-bottom:8px;">本周迎来<span style="color:#f0b429;font-weight:600;">超级央行周</span>：美联储、欧央行、日央行相继召开议息会议。美联储6月12日凌晨公布决议，市场预期维持利率不变，关注点集中在鲍威尔讲话及点阵图是否调整年内降息预期。中国央行已率先续作<span style="color:#f85149;font-weight:600;">5000亿元MLF</span>，操作利率2.00%维持不变，释放稳定流动性信号。</p>
          <p style="font-size:12px;color:#8b95a5;">中东局势紧张度下降，但不确定性仍存。同时，中国央行<span style="color:#3fb950;font-weight:600;">连续20个月增持黄金储备</span>，黄金储备规模持续扩大，凸显官方对黄金作为储备资产的长期信心。</p>"""
new3 = """        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🏛️</span>
          <span style="font-size:14px;font-weight:700;color:#f0b429;">以伊冲突骤然升级，地缘风险急剧攀升</span>
          <span style="margin-left:auto;font-size:11px;color:#f0b429;background:rgba(240,180,41,0.15);padding:2px 8px;border-radius:10px;">关注</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">以色列对伊朗西部和中部军事目标实施打击，伊朗革命卫队称以色列开启<span style="color:#f85149;font-weight:600;">危险军事行动</span>。伊朗启动<span style="color:#f0b429;font-weight:600;">霍尔木兹海峡收费条例</span>起草，每艘船只收费150万至200万美元。也门胡塞武装宣布对以色列发动攻击。布伦特原油一度突破<span style="color:#f0b429;font-weight:600;">96美元/桶</span>，地缘溢价飙升。</p>
          <p style="margin-bottom:8px;">特朗普呼吁以伊双方<span style="color:#f85149;font-weight:600;">立即停火</span>，称以色列只能接受美伊协议。油价此后从高点回落，收盘布伦特约93.72美元，WTI约90.53美元。中国央行6月9日开展<span style="color:#f85149;font-weight:600;">2185亿元7天期逆回购</span>，操作利率1.40%，净投放2075亿元，维护市场流动性合理充裕。</p>
          <p style="font-size:12px;color:#8b95a5;">中东局势紧张度急剧上升，地缘溢价短期难以消退。中国央行<span style="color:#3fb950;font-weight:600;">连续20个月增持黄金储备</span>，黄金战略配置价值凸显。央行持续净投放呵护市场流动性，在A股调整背景下释放稳定信号。</p>"""

# 维度4: 风险事件
old4 = """        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">⚠️</span>
          <span style="font-size:14px;font-weight:700;color:#8b95a5;">结构性机会与风险并存，谨慎乐观</span>
          <span style="margin-left:auto;font-size:11px;color:#8b95a5;background:rgba(139,149,165,0.15);padding:2px 8px;border-radius:10px;">中性偏多</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">美联储利率决议窗口开启，市场高度关注点阵图变化。当前联邦基金利率维持高位，10年期美债收益率回落至<span style="color:#f85149;font-weight:600;">4.48%</span>，美元指数跌至<span style="color:#f85149;font-weight:600;">99.62</span>。若美联储释放鸽派信号，可能进一步推动风险资产反弹；反之，市场可能再度承压。</p>
          <p style="margin-bottom:8px;">AI板块经历估值回调后进入<span style="color:#f0b429;font-weight:600;">业绩兑现期</span>，COMPUTEX 2026展会释放的CPU+GPU协同计算趋势、国内大模型厂商CPU需求暴增5倍等信号，显示算力基础设施建设仍在加速。国产替代逻辑持续强化。</p>
          <p style="font-size:12px;color:#8b95a5;">国内方面，A股结构性分化明显。银行高股息板块（股息率<span style="color:#f85149;font-weight:600;">5.05%</span>）获得长线资金青睐，科技股企稳但仍需业绩验证。央行持续净投放维护流动性，北向资金连续<span style="color:#3fb950;font-weight:600;">9日</span>净买入。建议采取哑铃型策略，均衡配置高股息防御与AI算力成长方向。</p>"""
new4 = """        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">⚠️</span>
          <span style="font-size:14px;font-weight:700;color:#8b95a5;">全球风险资产集中调整，防御优先</span>
          <span style="margin-left:auto;font-size:11px;color:#8b95a5;background:rgba(139,149,165,0.15);padding:2px 8px;border-radius:10px;">中性偏空</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">美联储利率决议窗口临近，非农数据超预期推升加息预期。10年期美债收益率上行至<span style="color:#f85149;font-weight:600;">4.55%</span>，美元指数走强至<span style="color:#f85149;font-weight:600;">100.06</span>。若美联储释放鹰派信号，全球风险资产可能再度承压；反之则有望迎来喘息。</p>
          <p style="margin-bottom:8px;">AI板块估值回调加剧，费城半导体指数大跌超<span style="color:#f0b429;font-weight:600;">10%</span>创2020年3月以来最大跌幅，市场对AI交易过热担忧升温。但COMPUTEX 2026展示的CPU+GPU协同趋势表明算力基础设施需求仍强，短期回调不改变长期逻辑。</p>
          <p style="font-size:12px;color:#8b95a5;">国内方面，A股普跌凸显防御价值。银行高股息板块（股息率<span style="color:#f85149;font-weight:600;">5.05%</span>）逆势抗跌，获得长线资金青睐。央行持续净投放维护流动性，北向资金连续<span style="color:#3fb950;font-weight:600;">8日</span>净买入。建议优先防御，重点配置银行电力等高股息板块，科技成长方向等待情绪企稳后再布局。</p>"""

# 执行
for i, (old, new, name) in enumerate([(old1,new1,"A股行情"),(old2,new2,"外围市场"),(old3,new3,"地缘政策"),(old4,new4,"风险事件")]):
    if old in html:
        html = html.replace(old, new)
        changes.append(f"✓ {name}")
    else:
        print(f"✗ {name} NOT FOUND")
        # 调试
        idx = html.find(name[:4])
        if idx > 0:
            print(f"  '{name[:4]}' found at {idx}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

for c in changes:
    print(c)
print(f"\n成功: {len(changes)}/4")
