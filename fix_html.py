#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道 HTML 修正脚本
将6月10日报告中的市场数据修正为6月9日收盘数据
"""

filepath = '/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道/老盛早知道_20260610.html'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. Header 区域 hm-tickers 数据修正
# ============================================================
# 上证: 3987.26 +0.71% up → 3959 -1.70% down
html = html.replace(
    '''        <div class="hm-ticker">
            <span class="t-label">上证</span>
            <span class="t-val">3987.26</span>
            <span class="t-chg up">+0.71%</span>
          </div>''',
    '''        <div class="hm-ticker">
            <span class="t-label">上证</span>
            <span class="t-val">3959</span>
            <span class="t-chg down">-1.70%</span>
          </div>'''
)

# 道指: 51142.30 +0.54% up → 50866 -1.35% down
html = html.replace(
    '''        <div class="hm-ticker">
            <span class="t-label">道指</span>
            <span class="t-val">51142.30</span>
            <span class="t-chg up">+0.54%</span>
          </div>''',
    '''        <div class="hm-ticker">
            <span class="t-label">道指</span>
            <span class="t-val">50866</span>
            <span class="t-chg down">-1.35%</span>
          </div>'''
)

# 黄金: $4318 +0.77% up → $4285 -1.34% down
html = html.replace(
    '''        <div class="hm-ticker">
            <span class="t-label">黄金</span>
            <span class="t-val">$4318</span>
            <span class="t-chg up">+0.77%</span>
          </div>''',
    '''        <div class="hm-ticker">
            <span class="t-label">黄金</span>
            <span class="t-val">$4285</span>
            <span class="t-chg down">-1.34%</span>
          </div>'''
)

# ============================================================
# 2. Tab 0 要点速览 - 顶部 summary-cards 修正
# ============================================================

# summary-card 1 - 上证指数: 3987.26 +0.71% up → 3959.34 -1.70% down
html = html.replace(
    '''    <div class="summary-card-red">
      <div class="summary-card-icon">📊</div>
      <div class="summary-card-content">
        <div class="summary-card-title">上证指数</div>
        <div class="summary-card-value">3987.26 <span class="summary-card-change up">+0.71%</span></div>
        <div class="summary-card-desc">结构性行情凸显，银行保险电力领涨</div>
      </div>
    </div>''',
    '''    <div class="summary-card-red">
      <div class="summary-card-icon">📊</div>
      <div class="summary-card-content">
        <div class="summary-card-title">上证指数</div>
        <div class="summary-card-value">3959.34 <span class="summary-card-change down">-1.70%</span></div>
        <div class="summary-card-desc">科技成长板块回调，银行保险电力高股息板块抗跌</div>
      </div>
    </div>'''
)

# summary-card 2 - 恒生指数: 24938.75 +1.14% → 24657.06 -1.22%
html = html.replace(
    '''    <div class="summary-card-blue">
      <div class="summary-card-icon">🏦</div>
      <div class="summary-card-content">
        <div class="summary-card-title">恒生指数</div>
        <div class="summary-card-value">24938.75 <span class="summary-card-tag">+1.14%</span></div>
        <div class="summary-card-desc">高股息板块反弹，南向资金净买入87.62亿</div>
      </div>
    </div>''',
    '''    <div class="summary-card-blue">
      <div class="summary-card-icon">🏦</div>
      <div class="summary-card-content">
        <div class="summary-card-title">恒生指数</div>
        <div class="summary-card-value">24657.06 <span class="summary-card-change down">-1.22%</span></div>
        <div class="summary-card-desc">科技股承压，南向资金净买入113.18亿港元</div>
      </div>
    </div>'''
)

# summary-card 3 - 纳斯达克: 25984.20 +1.07% → 25709.43 -4.18%
html = html.replace(
    '''    <div class="summary-card-yellow">
      <div class="summary-card-icon">💰</div>
      <div class="summary-card-content">
        <div class="summary-card-title">纳斯达克</div>
        <div class="summary-card-value">25984.20 <span class="summary-card-tag">+1.07%</span></div>
        <div class="summary-card-desc">科技股企稳反弹，英伟达AMD领涨芯片板块</div>
      </div>
    </div>''',
    '''    <div class="summary-card-yellow">
      <div class="summary-card-icon">💰</div>
      <div class="summary-card-content">
        <div class="summary-card-title">纳斯达克</div>
        <div class="summary-card-value">25709.43 <span class="summary-card-change down">-4.18%</span></div>
        <div class="summary-card-desc">科技股大幅回调，英伟达AMD领跌芯片板块</div>
      </div>
    </div>'''
)

# summary-card 4 - 黄金: $4318/oz +0.77% → $4285 -1.34%
html = html.replace(
    '''    <div class="summary-card-green">
      <div class="summary-card-icon">🤖</div>
      <div class="summary-card-content">
        <div class="summary-card-title">国际金价</div>
        <div class="summary-card-value">$4318/oz <span class="summary-card-tag">+0.77%</span></div>
        <div class="summary-card-desc">央行购金+地缘避险，高位震荡偏强</div>
      </div>
    </div>''',
    '''    <div class="summary-card-green">
      <div class="summary-card-icon">🤖</div>
      <div class="summary-card-content">
        <div class="summary-card-title">国际金价</div>
        <div class="summary-card-value">$4285/oz <span class="summary-card-change down">-1.34%</span></div>
        <div class="summary-card-desc">美元走强+风险偏好回升，高位回调震荡</div>
      </div>
    </div>'''
)

# ============================================================
# 3. Tab 0 要点卡片 - 日期与数据内容修正
# ============================================================

# 要点卡片01 - 以伊冲突缓和（保持内容，但将后续日期相关描述调整）
html = html.replace(
    '''    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(0,212,255,0.03));border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#00d4ff,#0099cc);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">01</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#00d4ff;font-weight:700;font-size:14px;">以伊冲突现缓和迹象</span>，特朗普公开呼吁以色列立即停火并接受美伊协议，伊朗方面表示愿意在联合国框架下谈判，霍尔木兹海峡航运压力有所缓解，布伦特原油自高点回落至约<span style="color:#f85149;font-weight:700;">92.80美元</span>。
      </div>
    </div>''',
    '''    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(0,212,255,0.03));border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#00d4ff,#0099cc);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">01</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#00d4ff;font-weight:700;font-size:14px;">以伊冲突现缓和迹象</span>，特朗普公开呼吁以色列立即停火并接受美伊协议，伊朗方面表示愿意在联合国框架下谈判，霍尔木兹海峡航运压力有所缓解，布伦特原油自高点回落至约<span style="color:#3fb950;font-weight:700;">93.72美元</span>。
      </div>
    </div>'''
)

# 要点卡片02 - 超级央行周（保持）
html = html.replace(
    '''    <div style="background:linear-gradient(135deg,rgba(240,180,41,0.1),rgba(240,180,41,0.03));border:1px solid rgba(240,180,41,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f0b429,#d29922);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">02</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f0b429;font-weight:700;font-size:14px;">超级央行周正式开启</span>，美联储、欧央行、日央行本周相继议息。市场预期美联储按兵不动维持利率，但鲍威尔表态偏鹰，利率互换市场定价年内降息概率降至<span style="color:#3fb950;font-weight:700;">38%</span>。中国央行续作MLF，操作利率维持2.00%。
      </div>
    </div>''',
    '''    <div style="background:linear-gradient(135deg,rgba(240,180,41,0.1),rgba(240,180,41,0.03));border:1px solid rgba(240,180,41,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f0b429,#d29922);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">02</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f0b429;font-weight:700;font-size:14px;">超级央行周正式开启</span>，美联储、欧央行、日央行本周相继议息。市场预期美联储按兵不动维持利率，但鲍威尔表态偏鹰，利率互换市场定价年内降息概率降至<span style="color:#f0b429;font-weight:700;">38%</span>。中国央行续作MLF，操作利率维持2.00%。
      </div>
    </div>'''
)

# 要点卡片03 - A股结构性行情 → 改为A股大幅回调
html = html.replace(
    '''    <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f85149,#cc0000);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">03</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f85149;font-weight:700;font-size:14px;">A股结构性行情凸显</span>，沪指收<span style="color:#f85149;font-weight:700;">3987.26点涨0.71%</span>，银行、保险、电力等高股息板块领涨，煤炭、石油石化同步走强。科技成长板块延续调整，科创50小幅下跌0.42%，两市成交额约<span style="color:#00d4ff;font-weight:700;">26481亿元</span>。
      </div>
    </div>''',
    '''    <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f85149,#cc0000);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">03</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f85149;font-weight:700;font-size:14px;">A股6月9日大幅回调</span>，沪指收<span style="color:#3fb950;font-weight:700;">3959.34点跌1.70%</span>，深证成指跌<span style="color:#3fb950;font-weight:700;">3.22%</span>，创业板指跌<span style="color:#3fb950;font-weight:700;">3.69%</span>，科创50大跌<span style="color:#3fb950;font-weight:700;">4.30%</span>，沪深300跌<span style="color:#3fb950;font-weight:700;">2.14%</span>。银行、保险、电力等高股息板块相对抗跌，两市成交额约<span style="color:#00d4ff;font-weight:700;">27927.61亿元</span>，涨跌家数896涨/4591跌。
      </div>
    </div>'''
)

# 要点卡片04 - 美股震荡反弹 → 改为美股大幅回调
html = html.replace(
    '''    <div style="background:linear-gradient(135deg,rgba(63,185,80,0.1),rgba(63,185,80,0.03));border:1px solid rgba(63,185,80,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#3fb950,#22c55e);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">04</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#3fb950;font-weight:700;font-size:14px;">美股震荡反弹</span>，道指涨<span style="color:#f85149;font-weight:700;">0.54%</span>报51142.30点，标普500涨<span style="color:#f85149;font-weight:700;">0.83%</span>，纳指涨<span style="color:#f85149;font-weight:700;">1.07%</span>。芯片股企稳回升，英伟达涨2.18%，AMD涨3.42%，ARM涨4.16%。市场情绪较昨日明显修复。
      </div>
    </div>''',
    '''    <div style="background:linear-gradient(135deg,rgba(63,185,80,0.1),rgba(63,185,80,0.03));border:1px solid rgba(63,185,80,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#3fb950,#22c55e);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">04</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#3fb950;font-weight:700;font-size:14px;">美股6月9日大幅回调</span>，道指跌<span style="color:#3fb950;font-weight:700;">1.35%</span>报50866.78点，标普500跌<span style="color:#3fb950;font-weight:700;">2.64%</span>，纳指跌<span style="color:#3fb950;font-weight:700;">4.18%</span>。芯片股同步下跌，英伟达跌6.20%报$205.10，市场情绪承压。
      </div>
    </div>'''
)

# 要点卡片05 - 央行操作（保持内容略调）
html = html.replace(
    '''    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(0,212,255,0.03));border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#00d4ff,#0099cc);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">05</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#00d4ff;font-weight:700;font-size:14px;">央行续作MLF+逆回购</span>，中国人民银行开展<span style="color:#f85149;font-weight:700;">5000亿元</span>MLF操作和<span style="color:#f85149;font-weight:700;">2000亿元</span>7天期逆回购操作，利率均维持不变。本月MLF到期<span style="color:#3fb950;font-weight:700;">1500亿元</span>，实现中期流动性净投放<span style="color:#f85149;font-weight:700;">3500亿元</span>，呵护市场流动性。
      </div>
    </div>''',
    '''    <div style="background:linear-gradient(135deg,rgba(0,212,255,0.1),rgba(0,212,255,0.03));border:1px solid rgba(0,212,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#00d4ff,#0099cc);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">05</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#00d4ff;font-weight:700;font-size:14px;">央行续作MLF+逆回购</span>，中国人民银行开展<span style="color:#00d4ff;font-weight:700;">5000亿元</span>MLF操作和<span style="color:#00d4ff;font-weight:700;">2000亿元</span>7天期逆回购操作，利率均维持不变。本月MLF到期<span style="color:#00d4ff;font-weight:700;">1500亿元</span>，实现中期流动性净投放<span style="color:#00d4ff;font-weight:700;">3500亿元</span>，呵护市场流动性。
      </div>
    </div>'''
)

# 要点卡片06 - 北向资金
html = html.replace(
    '''    <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f85149,#cc0000);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">06</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f85149;font-weight:700;font-size:14px;">北向资金净买入68.45亿</span>，北向资金全天净流入<span style="color:#f85149;font-weight:700;">68.45亿元</span>，其中沪股通净买入42.38亿元，深股通净买入26.07亿元，<span style="color:#f0b429;font-weight:700;">连续9个交易日净买入</span>。前十大成交个股中，工商银行、农业银行、长江电力获净买入居前。
      </div>
    </div>''',
    '''    <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f85149,#cc0000);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">06</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f85149;font-weight:700;font-size:14px;">北向资金连续8日净买入</span>，截至6月9日收盘，北向资金<span style="color:#f85149;font-weight:700;">连续8个交易日净买入</span>，外资持续加仓A股核心资产。前十大成交个股中，工商银行、农业银行、长江电力等高股息标的获净买入居前。
      </div>
    </div>'''
)

# 要点卡片07 - 黄金高位震荡
html = html.replace(
    '''    <div style="background:linear-gradient(135deg,rgba(240,180,41,0.1),rgba(240,180,41,0.03));border:1px solid rgba(240,180,41,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f0b429,#d29922);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">07</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f0b429;font-weight:700;font-size:14px;">黄金高位震荡偏强</span>，伦敦金现盘中最高触及<span style="color:#f85149;font-weight:700;">4326美元/盎司</span>，收盘报<span style="color:#f85149;font-weight:700;">4318美元/盎司涨0.77%</span>。中国央行黄金储备连续第20个月增加，5月环比增持<span style="color:#00d4ff;font-weight:700;">35万盎司</span>。地缘风险叠加去美元化趋势，支撑金价长期上行。
      </div>
    </div>''',
    '''    <div style="background:linear-gradient(135deg,rgba(240,180,41,0.1),rgba(240,180,41,0.03));border:1px solid rgba(240,180,41,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#f0b429,#d29922);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">07</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#f0b429;font-weight:700;font-size:14px;">黄金高位回调</span>，伦敦金现6月9日收盘报<span style="color:#3fb950;font-weight:700;">$4285/盎司跌1.34%</span>。中国央行黄金储备连续第20个月增加，5月环比增持<span style="color:#00d4ff;font-weight:700;">35万盎司</span>。短期美元走强压制金价，长期央行购金+去美元化趋势仍支撑金价。
      </div>
    </div>'''
)

# 要点卡片08 - 比特币箱体整理
html = html.replace(
    '''    <div style="background:linear-gradient(135deg,rgba(188,140,255,0.1),rgba(188,140,255,0.03));border:1px solid rgba(188,140,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#bc8cff,#9a6de0);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">08</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#bc8cff;font-weight:700;font-size:14px;">比特币箱体整理</span>，BTC在<span style="color:#00d4ff;font-weight:700;">63000-65800美元</span>区间震荡，日内微涨0.68%报<span style="color:#f85149;font-weight:700;">63385美元</span>。以太坊涨1.85%至3412美元。美比特币现货ETF净买入<span style="color:#f85149;font-weight:700;">1.24亿美元</span>，结束连续两日净流出。
      </div>
    </div>''',
    '''    <div style="background:linear-gradient(135deg,rgba(188,140,255,0.1),rgba(188,140,255,0.03));border:1px solid rgba(188,140,255,0.25);border-radius:12px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;">
      <div style="min-width:28px;height:28px;background:linear-gradient(135deg,#bc8cff,#9a6de0);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff;">08</div>
      <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
        <span style="color:#bc8cff;font-weight:700;font-size:14px;">比特币箱体震荡</span>，BTC在6月9日报<span style="color:#3fb950;font-weight:700;">$62956</span>，以太坊报<span style="color:#3fb950;font-weight:700;">$1666</span>。加密货币随全球风险资产回调，市场情绪偏谨慎。
      </div>
    </div>'''
)

# ============================================================
# 4. Tab 3: 全球市场 - 标题栏 alert-bar 修正
# ============================================================

# Tab 3 顶部正面因素栏
html = html.replace(
    '''  <div class="alert-bar" style="margin-bottom:20px;">
    <strong>✅ 正面因素：</strong>北向资金连续9日净买入，长线外资坚定布局；银行、保险、电力等高股息板块逆势走强；特朗普呼吁以伊停火地缘紧张局势缓和；超级央行周来临，美联储决议在即。
  </div>''',
    '''  <div class="alert-bar" style="margin-bottom:20px;">
    <strong>✅ 正面因素：</strong>北向资金连续8日净买入，长线外资坚定布局；银行、保险、电力等高股息板块相对抗跌；特朗普呼吁以伊停火地缘紧张局势缓和；超级央行周来临，美联储决议在即，央行续作MLF净投放3500亿呵护流动性。
  </div>'''
)

# Tab 3 市场热点栏
html = html.replace(
    '''  <div class="hot-bar" style="margin-bottom:20px;">
    <strong>🔥 市场热点：</strong>银行板块领涨（工行建行创阶段新高，中证银行指数股息率5.05%；AI大模型双雄纳入恒生科技指数；COMPUTEX 2026新品持续催化算力产业链；黄金高位震荡比特币箱体整理。
  </div>''',
    '''  <div class="hot-bar" style="margin-bottom:20px;">
    <strong>🔥 市场热点：</strong>6月9日全球风险资产集中回调，A股沪指失守4000点，韩股暴跌8.29%熔断；高股息板块相对抗跌（中证银行指数股息率5.05%）；黄金高位回落；COMPUTEX 2026催化算力产业链。
  </div>'''
)

# Tab 3 风险提示栏
html = html.replace(
    '''  <div class="good-bar" style="margin-bottom:20px;">
    <strong>⚠️ 风险提示：</strong>全球科技股仍处估值回调阶段需关注美联储利率决议窗口；以伊局势虽缓和但不确定性仍存；A股结构性分化明显结构性机会与风险并存，科技股企稳仍需关注业绩兑现。
  </div>''',
    '''  <div class="good-bar" style="margin-bottom:20px;">
    <strong>⚠️ 风险提示：</strong>全球科技股大幅回调需关注美联储利率决议窗口；以伊局势虽缓和但不确定性仍存；6月9日A股涨跌比896:4591，市场恐慌情绪升温；短期波动加剧需控制仓位、远离杠杆操作。
  </div>'''
)

# ============================================================
# 5. Tab 3: 全球市场 - 8个 market-block 数据修正
# ============================================================

# A股 market block
html = html.replace(
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🇨🇳 A股（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">上证指数</span><span class="market-val up">3987.26 +0.71%</span></div>
      <div class="market-row"><span class="market-name">深证成指</span><span class="market-val up">15082.45 +0.68%</span></div>
      <div class="market-row"><span class="market-name">创业板指</span><span class="market-val up">3884.62 +0.85%</span></div>
      <div class="market-row"><span class="market-name">科创50</span><span class="market-val up">涨1.12%</span></div>
      <div class="market-row"><span class="market-name">沪深300</span><span class="market-val up">涨0.94%</span></div>
      <div class="market-row"><span class="market-name">成交额</span><span class="market-val neutral" style="color:#f0b429;font-weight:700;">28562.40亿<span style="font-size:11px;"> (连续33日超2.5万亿)</span></span></div>
      <div class="market-row"><span class="market-name">涨跌家数</span><span class="market-val up">2865涨/2624跌</span></div>
      <div class="market-row"><span class="market-name">北向资金</span><span class="market-val up">连续9日净买入</span></div>
    </div>''',
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🇨🇳 A股（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">上证指数</span><span class="market-val down">3959.34 -1.70%</span></div>
      <div class="market-row"><span class="market-name">深证成指</span><span class="market-val down">14821.19 -3.22%</span></div>
      <div class="market-row"><span class="market-name">创业板指</span><span class="market-val down">3811.79 -3.69%</span></div>
      <div class="market-row"><span class="market-name">科创50</span><span class="market-val down">-4.30%</span></div>
      <div class="market-row"><span class="market-name">沪深300</span><span class="market-val down">-2.14%</span></div>
      <div class="market-row"><span class="market-name">成交额</span><span class="market-val neutral" style="color:#f0b429;font-weight:700;">27927.61亿<span style="font-size:11px;"> (连续超2.5万亿)</span></span></div>
      <div class="market-row"><span class="market-name">涨跌家数</span><span class="market-val down">896涨/4591跌</span></div>
      <div class="market-row"><span class="market-name">北向资金</span><span class="market-val up">连续8日净买入</span></div>
    </div>'''
)

# 港股 market block
html = html.replace(
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🇭🇰 港股（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">恒生指数</span><span class="market-val up">25128.60 +0.85%</span></div>
      <div class="market-row"><span class="market-name">恒生科技指数</span><span class="market-val up">4892.35 +1.24%</span></div>
      <div class="market-row"><span class="market-name">国企指数</span><span class="market-val up">8512.48 +0.72%</span></div>
      <div class="market-row"><span class="market-name">南向资金</span><span class="market-val up">净买入96.85亿港元</span></div>
    </div>''',
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🇭🇰 港股（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">恒生指数</span><span class="market-val down">24657.06 -1.22%</span></div>
      <div class="market-row"><span class="market-name">恒生科技指数</span><span class="market-val down">4755.91 -2.71%</span></div>
      <div class="market-row"><span class="market-name">国企指数</span><span class="market-val down">8341.36 -1.13%</span></div>
      <div class="market-row"><span class="market-name">南向资金</span><span class="market-val up">净买入113.18亿港元</span></div>
    </div>'''
)

# 美股 market block
html = html.replace(
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🇺🇸 美股（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">道琼斯</span><span class="market-val up">51142.30 +0.54%</span></div>
      <div class="market-row"><span class="market-name">标普500</span><span class="market-val up">7442.18 +0.79%</span></div>
      <div class="market-row"><span class="market-name">纳斯达克</span><span class="market-val up">25948.75 +0.93%</span></div>
      <div class="market-row"><span class="market-name">英伟达</span><span class="market-val up">$212.80 +3.76%</span></div>
      <div class="market-row"><span class="market-name">特斯拉</span><span class="market-val up">涨2.18%</span></div>
      <div class="market-row"><span class="market-name">ARM</span><span class="market-val up">涨4.52%</span></div>
    </div>''',
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🇺🇸 美股（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">道琼斯</span><span class="market-val down">50866.78 -1.35%</span></div>
      <div class="market-row"><span class="market-name">标普500</span><span class="market-val down">7383.74 -2.64%</span></div>
      <div class="market-row"><span class="market-name">纳斯达克</span><span class="market-val down">25709.43 -4.18%</span></div>
      <div class="market-row"><span class="market-name">英伟达</span><span class="market-val down">$205.10 -6.20%</span></div>
      <div class="market-row"><span class="market-name">特斯拉</span><span class="market-val down">跌3.15%</span></div>
      <div class="market-row"><span class="market-name">ARM</span><span class="market-val down">跌5.82%</span></div>
    </div>'''
)

# 亚太市场 market block
html = html.replace(
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🌏 亚太市场（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">日经225</span><span class="market-val up">64856.20 +1.30%</span></div>
      <div class="market-row"><span class="market-name">韩国KOSPI</span><span class="market-val up">7685.20 +2.68%</span></div>
      <div class="market-row"><span class="market-name">台湾加权</span><span class="market-val up">涨1.85%</span></div>
      <div class="market-row"><span class="market-name">印度Sensex</span><span class="market-val up">跟随亚太上涨</span></div>
      <div class="market-row"><span class="market-name">澳洲ASX200</span><span class="market-val up">8712.60 +0.82%</span></div>
    </div>''',
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🌏 亚太市场（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">日经225</span><span class="market-val down">64024.60 -3.85%</span></div>
      <div class="market-row"><span class="market-name">韩国KOSPI</span><span class="market-val down">7484.41 -8.29%熔断</span></div>
      <div class="market-row"><span class="market-name">台湾加权</span><span class="market-val down">跌4.12%</span></div>
      <div class="market-row"><span class="market-name">印度Sensex</span><span class="market-val down">跟随亚太回调</span></div>
      <div class="market-row"><span class="market-name">澳洲ASX200</span><span class="market-val down">跌2.86%</span></div>
    </div>'''
)

# 欧洲市场 market block
html = html.replace(
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🇪🇺 欧洲市场（6月10日盘中）</h4>
      <div class="market-row"><span class="market-name">英国富时100</span><span class="market-val up">+0.62%</span></div>
      <div class="market-row"><span class="market-name">德国DAX30</span><span class="market-val up">+0.85%</span></div>
      <div class="market-row"><span class="market-name">法国CAC40</span><span class="market-val up">+0.76%</span></div>
      <div class="market-row"><span class="market-name">斯托克50</span><span class="market-val up">+0.72%</span></div>
    </div>''',
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🇪🇺 欧洲市场（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">英国富时100</span><span class="market-val up">微涨0.05%</span></div>
      <div class="market-row"><span class="market-name">德国DAX30</span><span class="market-val down">-0.47%</span></div>
      <div class="market-row"><span class="market-name">法国CAC40</span><span class="market-val down">-0.92%</span></div>
      <div class="market-row"><span class="market-name">斯托克50</span><span class="market-val down">-0.68%</span></div>
    </div>'''
)

# 大宗商品 market block
html = html.replace(
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🏭 大宗商品（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">WTI原油</span><span class="market-val down">$89.25 -1.41%</span></div>
      <div class="market-row"><span class="market-name">布伦特原油</span><span class="market-val down">$92.80 -0.98%</span></div>
      <div class="market-row"><span class="market-name">国际黄金</span><span class="market-val up">$4318 +0.77%</span></div>
      <div class="market-row"><span class="market-name">上海金</span><span class="market-val up">952.48元/克</span></div>
      <div class="market-row"><span class="market-name">白银</span><span class="market-val up">68.92美元/盎司 +1.76%</span></div>
    </div>''',
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🏭 大宗商品（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">WTI原油</span><span class="market-val down">$90.53 -0.01%</span></div>
      <div class="market-row"><span class="market-name">布伦特原油</span><span class="market-val up">$93.72 +0.68%</span></div>
      <div class="market-row"><span class="market-name">国际黄金</span><span class="market-val down">$4285 -1.34%</span></div>
      <div class="market-row"><span class="market-name">上海金</span><span class="market-val down">948.20元/克</span></div>
      <div class="market-row"><span class="market-name">白银</span><span class="market-val down">65.42美元/盎司 -2.18%</span></div>
    </div>'''
)

# 汇率与债券 market block
html = html.replace(
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>💱 汇率与债券（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">USD/CNY中间价</span><span class="market-val neutral">6.8215</span></div>
      <div class="market-row"><span class="market-name">在岸汇率</span><span class="market-val neutral">6.7825</span></div>
      <div class="market-row"><span class="market-name">美元指数</span><span class="market-val down">99.62 -0.44%</span></div>
      <div class="market-row"><span class="market-name">美10年期</span><span class="market-val down">4.48%</span></div>
      <div class="market-row"><span class="market-name">美30年期</span><span class="market-val down">4.62%</span></div>
      <div class="market-row"><span class="market-name">中10年期</span><span class="market-val neutral">约1.71%</span></div>
    </div>''',
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>💱 汇率与债券（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">USD/CNY中间价</span><span class="market-val neutral">6.8198</span></div>
      <div class="market-row"><span class="market-name">在岸汇率</span><span class="market-val neutral">6.7794</span></div>
      <div class="market-row"><span class="market-name">美元指数</span><span class="market-val up">100.06 +0.45%</span></div>
      <div class="market-row"><span class="market-name">美10年期</span><span class="market-val up">4.52%</span></div>
      <div class="market-row"><span class="market-name">美30年期</span><span class="market-val up">4.68%</span></div>
      <div class="market-row"><span class="market-name">中10年期</span><span class="market-val neutral">约1.71%</span></div>
    </div>'''
)

# 加密货币 market block
html = html.replace(
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🪙 加密货币（6月10日收盘）</h4>
      <div class="market-row"><span class="market-name">比特币BTC</span><span class="market-val up">$65280</span></div>
      <div class="market-row"><span class="market-name">以太坊ETH</span><span class="market-val up">$1785</span></div>
      <div class="market-row"><span class="market-name">BTC ETF</span><span class="market-val neutral">小幅净流入</span></div>
      <div class="market-row"><span class="market-name">市场情绪</span><span class="market-val neutral">中性偏乐观（BTC箱体整理）</span></div>
    </div>''',
    '''    <div class="market-block" style="border-top:2px solid rgba(255,255,255,0.12);">
      <h4>🪙 加密货币（6月9日收盘）</h4>
      <div class="market-row"><span class="market-name">比特币BTC</span><span class="market-val down">$62956</span></div>
      <div class="market-row"><span class="market-name">以太坊ETH</span><span class="market-val down">$1666</span></div>
      <div class="market-row"><span class="market-name">BTC ETF</span><span class="market-val neutral">小幅净流出</span></div>
      <div class="market-row"><span class="market-name">市场情绪</span><span class="market-val neutral">偏谨慎（全球风险资产回调）</span></div>
    </div>'''
)

# ============================================================
# 6. Tab 3: 市场综评 - 4维度卡片修正
# ============================================================

# 综评维度 01 - A股
html = html.replace(
    '''      <!-- A股行情 -->
      <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.2);border-radius:12px;padding:16px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🇨🇳</span>
          <span style="font-size:14px;font-weight:700;color:#f85149;">A股结构性反弹，银行高股息领涨</span>
          <span style="margin-left:auto;font-size:11px;color:#f85149;background:rgba(248,81,73,0.15);padding:2px 8px;border-radius:10px;">偏多</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">6月10日周三，A股三大指数全线收涨，上证指数涨<span style="color:#f85149;font-weight:600;">0.71%</span>报<span style="color:#f85149;font-weight:600;">3987.26</span>点，深证成指涨<span style="color:#f85149;font-weight:600;">0.68%</span>，创业板指涨<span style="color:#f85149;font-weight:600;">0.85%</span>，科创50涨<span style="color:#f85149;font-weight:600;">1.12%</span>。沪深300指数涨<span style="color:#f85149;font-weight:600;">0.94%</span>，市场呈现结构性修复特征。沪深两市成交额<span style="color:#f0b429;font-weight:600;">28562.40亿元</span>，连续<span style="color:#f0b429;font-weight:600;">33个交易日</span>超2.5万亿，交投维持活跃。</p>
          <p style="margin-bottom:8px;">全市场上涨<span style="color:#3fb950;font-weight:600;">2865只</span>，下跌<span style="color:#f85149;font-weight:600;">2624只</span>，涨跌比约<span style="color:#f85149;font-weight:600;">52:48</span>，显示市场情绪显著改善。银行、保险、电力等高股息板块表现强势，<span style="color:#f85149;font-weight:600;">中证银行指数涨1.85%</span>，工行、建行齐创阶段新高。科技股经历回调后企稳反弹，半导体、算力硬件板块小幅收涨。</p>
          <p style="font-size:12px;color:#8b95a5;">北向资金连续9日净买入，累计净买入规模持续扩大。技术面上，上证指数在3900点附近获得支撑，银行高股息板块成为市场稳定器，低估值防御策略获得资金共识。</p>
        </div>
      </div>''',
    '''      <!-- A股行情 -->
      <div style="background:linear-gradient(135deg,rgba(248,81,73,0.1),rgba(248,81,73,0.03));border:1px solid rgba(248,81,73,0.2);border-radius:12px;padding:16px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🇨🇳</span>
          <span style="font-size:14px;font-weight:700;color:#f85149;">A股6月9日大幅回调，沪指失守4000点</span>
          <span style="margin-left:auto;font-size:11px;color:#3fb950;background:rgba(63,185,80,0.15);padding:2px 8px;border-radius:10px;">偏空</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">6月9日周一，A股三大指数全线收跌，上证指数跌<span style="color:#3fb950;font-weight:600;">1.70%</span>报<span style="color:#3fb950;font-weight:600;">3959.34</span>点，深证成指跌<span style="color:#3fb950;font-weight:600;">3.22%</span>，创业板指跌<span style="color:#3fb950;font-weight:600;">3.69%</span>，科创50大跌<span style="color:#3fb950;font-weight:600;">4.30%</span>。沪深300指数跌<span style="color:#3fb950;font-weight:600;">2.14%</span>，市场呈现恐慌性抛售特征。沪深两市成交额<span style="color:#f0b429;font-weight:600;">27927.61亿元</span>，交投维持活跃。</p>
          <p style="margin-bottom:8px;">全市场上涨<span style="color:#f85149;font-weight:600;">896只</span>，下跌<span style="color:#3fb950;font-weight:600;">4591只</span>，涨跌比约<span style="color:#3fb950;font-weight:600;">16:84</span>，显示市场情绪极度悲观。银行、保险、电力等高股息板块相对抗跌，中证银行指数跌幅较小。科技成长板块领跌，半导体、算力硬件板块大幅下挫。</p>
          <p style="font-size:12px;color:#8b95a5;">北向资金连续8日净买入，外资长线布局不受短期波动影响。技术面上，上证指数跌破4000点整数关口，银行高股息板块成为市场稳定器，低估值防御策略在回调中凸显韧性。</p>
        </div>
      </div>'''
)

# 综评维度 02 - 外围市场
html = html.replace(
    '''      <!-- 外围市场 -->
      <div style="background:linear-gradient(135deg,rgba(63,185,80,0.1),rgba(63,185,80,0.03));border:1px solid rgba(63,185,80,0.2);border-radius:12px;padding:16px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🌍</span>
          <span style="font-size:14px;font-weight:700;color:#3fb950;">全球股市震荡反弹，科技股企稳</span>
          <span style="margin-left:auto;font-size:11px;color:#3fb950;background:rgba(63,185,80,0.15);padding:2px 8px;border-radius:10px;">回暖</span>
        </div>
        <div style="font-size:13px;color:#b0bac4;line-height:1.7;">
          <p style="margin-bottom:8px;">亚太市场普遍反弹，韩国KOSPI涨<span style="color:#f85149;font-weight:600;">2.68%</span>收复部分失地，日经225涨<span style="color:#f85149;font-weight:600;">1.30%</span>，台湾加权涨约<span style="color:#f85149;font-weight:600;">1.85%</span>。欧洲股市盘中全线上涨，英国富时100涨<span style="color:#f85149;font-weight:600;">0.62%</span>，德国DAX涨<span style="color:#f85149;font-weight:600;">0.85%</span>，法国CAC40涨<span style="color:#f85149;font-weight:600;">0.76%</span>。</p>
          <p style="margin-bottom:8px;">美股隔夜（6月9日）企稳反弹，道指涨<span style="color:#f85149;font-weight:600;">0.54%</span>，标普500涨<span style="color:#f85149;font-weight:600;">0.79%</span>，纳指涨<span style="color:#f85149;font-weight:600;">0.93%</span>。科技股止跌回升，英伟达反弹<span style="color:#f85149;font-weight:600;">3.76%</span>报$212.80，特斯拉涨<span style="color:#f85149;font-weight:600;">2.18%</span>，ARM涨<span style="color:#f85149;font-weight:600;">4.52%</span>。费城半导体指数反弹<span style="color:#f85149;font-weight:600;">2.85%</span>，缓解了市场对科技股泡沫破裂的担忧。</p>
          <p style="font-size:12px;color:#8b95a5;">全球风险资产从恐慌抛售中逐步企稳。以伊冲突缓和推动油价回落，布油跌破93美元。黄金受避险需求支撑回升至4318美元。美债收益率回落，10年期降至4.48%，市场重新定价美联储政策路径。</p>
        </div>
      </div>''',
    '''      <!-- 外围市场 -->
      <div style="background:linear-gradient(135deg,rgba(63,185,80,0.1),rgba(63,185,80,0.03));border:1px solid rgba(63,185,80,0.2);border-radius:12px;padding:16px;">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
          <span style="font-size:18px;">🌍