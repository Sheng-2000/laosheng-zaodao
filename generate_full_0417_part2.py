#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
追加TAB 4: 价值投资风向
"""

html_content = '''
<!-- TAB 4: 价值投资风向 -->
<div class="tab-panel" id="panel-4">
  <div class="inner">
  <div class="section-title">💡 价值投资风向</div>
  <div class="sub-section">
    <div class="sub-title">一 · 机构价值投资观点</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">券商研报</span>中金：银行股迎来黄金配置期，从"周期博弈"转向"配置红利"</div>
      <div class="card-body">中金公司最新报告指出，银行板块正从"周期博弈"转向"配置红利"新阶段。2026年银行业将呈现"高股息+新动能+顺周期"三大特征。银行板块整体股息率约4.8%，较中国10年期国债高出近295bps，对险资、养老金等长线资金具有极强吸引力。首选招商银行、宁波银行、工商银行。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-energy">国际机构</span>高盛：美伊和谈若达成，油价或回落至$75-80区间</div>
      <div class="card-body">高盛能源报告指出，若美伊框架性协议达成，布伦特原油可能回落至$75-80区间。中国海油（600938）桶油成本约$28，在$93油价下桶油利润约$65，盈利依然可观。H股股息率预计超过6%，具备高确定性的分红回报。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">兴业证券</span>兴业：AI算力+公用事业"双主线"，GPT-6强化算力需求确定性</div>
      <div class="card-body">兴业证券发布专题报告：GPT-6的发布确认了AI景气周期延续，算力需求加速放量，同步利好中国移动、中国电信算力云业务。AI用电需求高增驱动电力需求稳步扩张，长江电力、中国核电受益逻辑得到强化。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">二 · 雪球·集思录价值投资社区情绪</div>
    <div class="card">
      <div class="card-title">📊 社区情绪追踪（截至4月17日）</div>
      <div class="card-body">
        <div class="sentiment-bar-wrap">
          <div class="sentiment-label"><span>银行板块讨论热度</span><span style="color:var(--accent)">偏多 · 76%</span></div>
          <div class="sentiment-bar"><div class="sentiment-fill" style="width:76%"></div></div>
        </div>
        <div class="sentiment-bar-wrap">
          <div class="sentiment-label"><span>能源/油价情绪</span><span style="color:var(--yellow)">中性 · 58%</span></div>
          <div class="sentiment-bar"><div class="sentiment-fill" style="width:58%;background:linear-gradient(90deg,#f0b429,var(--accent))"></div></div>
        </div>
        <div class="sentiment-bar-wrap">
          <div class="sentiment-label"><span>AI算力板块情绪</span><span style="color:var(--purple)">强多 · 85%</span></div>
          <div class="sentiment-bar"><div class="sentiment-fill" style="width:85%;background:linear-gradient(90deg,var(--purple),var(--accent))"></div></div>
        </div>
        <div class="sentiment-bar-wrap">
          <div class="sentiment-label"><span>高股息整体仓位意愿</span><span style="color:var(--green)">中强 · 72%</span></div>
          <div class="sentiment-bar"><div class="sentiment-fill" style="width:72%;background:linear-gradient(90deg,var(--green),var(--accent))"></div></div>
        </div>
      </div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">三 · 高股息板块深度分析</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">银行</span>银行板块：股息率处于历史高吸引力区间</div>
      <div class="card-body">银行板块整体股息率约4.8%，工行4.08%、招行5.22%、江苏5.27%，相较中国10年国债（约1.85%）溢价约244-345bps，吸引力显著。城商行ROE领先，业绩增速更快；国有大行体量大、股息率稳定，适合险资等长线资金配置。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-energy">能源</span>中国海油：油价约$93，桶油利润约$65，盈利可观</div>
      <div class="card-body">中国海油桶油成本约$28，按当前$93油价计算桶油利润约$65，仍处于历史盈利较好水平。美伊若达成框架协议，油价或回落至$75-80区间，届时需重新评估目标价。H股股息率预计超过6%。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">公用事业</span>长江电力+中国核电：AI用电需求拉动电力景气</div>
      <div class="card-body">长江电力（600900）分红承诺率≥70%，股息率约4.5%，"现金奶牛"属性稳固。中国核电（601985）未来5年装机增速10%+，AI机房用电拉动景气，中金DCF测算存在约30%低估空间，股息率约4.6%。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-ai">通信</span>中国移动：GPT-6催化，算力云+高股息双重价值</div>
      <div class="card-body">GPT-6发布是中国移动2026年最核心的催化剂之一——算力需求爆发，三大运营商资本开支合计增长约43%。中国移动算力云收入增速超50%，A股股息率约5.9%，H股约6.8%，PB约0.9x，估值处于历史低位。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">四 · 低估值板块</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">城商行</span>城商行PB历史低位，一季报催化估值修复窗口</div>
      <div class="card-body">宁波银行PB约0.91x，江苏银行PB约0.65x，杭州银行PB约0.72x，均处于近5年较低分位。城商行ROE（约13-15%）远高于国有大行，基本面优势明显但估值折价显著。一季报披露窗口有望催化估值修复。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">大秦铁路</span>大秦铁路：运量稳健，高分红，低PB低PE估值洼地</div>
      <div class="card-body">大秦铁路（601006）PB约1.0x，PE约9x，2025年度股息率约6%+，属于典型的低估值高股息"价值洼地"标的。AI用电驱动能源需求高增，煤炭运输量保持稳定。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">五 · 长线资金动向</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">险资</span>险资举牌步伐不减，4月以来新增银行、公用事业举牌3次</div>
      <div class="card-body">4月以来险资举牌节奏维持，新增举牌3次，集中在银行H股和公用事业板块。平安人寿持农行H股超20%举牌门槛，中国人寿对工行H股持续增配。预计2026年险资新增配置高股息权益资产规模超1500亿元。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">社保</span>社保基金一季报持仓：重配国有大行，高股息策略贯穿全年</div>
      <div class="card-body">社保基金一季度持仓报告显示，继续重配工商银行、农业银行、中国移动等高股息国企。社保基金作为最重要的战略性长期投资者，其持仓方向具有强烈的风向标意义。</div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">六 · 价值投资估值参考表</div>
    <div class="card">
      <div class="card-title">📐 关键估值指标（截至4月17日）</div>
      <div class="card-body">
        <table style="width:100%;border-collapse:collapse;font-size:13.5px;">
          <thead><tr style="border-bottom:1px solid var(--border);color:var(--text-muted);font-size:12px;"><td style="padding:6px 10px;">指标</td><td style="padding:6px 10px;text-align:right;">数值</td><td style="padding:6px 10px;text-align:right;">历史分位 / 备注</td></tr></thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(48,54,61,0.4);"><td style="padding:7px 10px;color:var(--text-secondary)">银行板块PB（整体）</td><td style="padding:7px 10px;text-align:right;color:var(--accent)">约0.65x</td><td style="padding:7px 10px;text-align:right;color:var(--green)">历史低位区间</td></tr>
            <tr style="border-bottom:1px solid rgba(48,54,61,0.4);"><td style="padding:7px 10px;color:var(--text-secondary)">上证指数PE（TTM）</td><td style="padding:7px 10px;text-align:right;color:var(--accent)">约14x</td><td style="padding:7px 10px;text-align:right;color:var(--yellow)">历史中等偏低分位</td></tr>
            <tr style="border-bottom:1px solid rgba(48,54,61,0.4);"><td style="padding:7px 10px;color:var(--text-secondary)">银行股息率（整体均值）</td><td style="padding:7px 10px;text-align:right;color:var(--accent)">约4.8%</td><td style="padding:7px 10px;text-align:right;color:var(--green)">高于10Y国债约295bps</td></tr>
            <tr style="border-bottom:1px solid rgba(48,54,61,0.4);"><td style="padding:7px 10px;color:var(--text-secondary)">中证红利指数PE</td><td style="padding:7px 10px;text-align:right;color:var(--accent)">约8.5x</td><td style="padding:7px 10px;text-align:right;color:var(--green)">历史较低分位</td></tr>
            <tr style="border-bottom:1px solid rgba(48,54,61,0.4);"><td style="padding:7px 10px;color:var(--text-secondary)">中国海油（油价$93）</td><td style="padding:7px 10px;text-align:right;color:var(--yellow)">桶油利润约$65</td><td style="padding:7px 10px;text-align:right;color:var(--green)">盈利依然可观</td></tr>
            <tr style="border-bottom:1px solid rgba(48,54,61,0.4);"><td style="padding:7px 10px;color:var(--text-secondary)">中国移动（A股）</td><td style="padding:7px 10px;text-align:right;color:var(--accent)">PB约0.9x</td><td style="padding:7px 10px;text-align:right;color:var(--green)">股息率5.9%</td></tr>
            <tr style="border-bottom:1px solid rgba(48,54,61,0.4);"><td style="padding:7px 10px;color:var(--text-secondary)">招商银行</td><td style="padding:7px 10px;text-align:right;color:var(--accent)">PB约0.9x</td><td style="padding:7px 10px;text-align:right;color:var(--yellow)">低于历史均值1.4x</td></tr>
            <tr style="border-bottom:1px solid rgba(48,54,61,0.4);"><td style="padding:7px 10px;color:var(--text-secondary)">中国核电</td><td style="padding:7px 10px;text-align:right;color:var(--accent)">市值约1859亿</td><td style="padding:7px 10px;text-align:right;color:var(--green)">低于DCF合理值约30%</td></tr>
            <tr><td style="padding:7px 10px;color:var(--text-secondary)">黄金（AU9999）</td><td style="padding:7px 10px;text-align:right;color:#f0b429">约1035-1043元/克</td><td style="padding:7px 10px;text-align:right;color:var(--red)">历史高位区间</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="sub-section">
    <div class="sub-title">附 · 精简参考板块</div>
    <div class="card">
      <div class="card-title"><span class="tag tag-finance">REITs·固收+</span>公募REITs与固收+：低波动高分红，资产配置稳定器</div>
      <div class="card-body">国内公募REITs扩容持续，交通基础设施类REITs分红率稳定在5-7%区间，波动率远低于权益市场。适合保守型价值投资者配置10-15%仓位。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-chip">AI算力（液冷/光模块）</span>GPT-6发布催化，液冷散热+光模块是算力投资最确定方向</div>
      <div class="card-body">GPT-6 200万Token上下文对算力密度要求极高，液冷散热成为数据中心标配。光迅科技、中际旭创等光模块龙头订单能见度超12个月。</div>
    </div>
    <div class="card">
      <div class="card-title"><span class="tag tag-policy">白酒/消费</span>白酒低谷期配置窗口：贵州茅台估值历史较低</div>
      <div class="card-body">贵州茅台当前PE约25x，低于5年均值35x，股息率约2.5%，处于近年来估值较低区间。可作为"高股息核心仓位+消费复苏弹性"组合的补充方向。</div>
    </div>
  </div>
  </div>
</div>
'''

# 追加到文件
with open('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/老盛的每日快讯/WorkBuddy版/老盛早知道_20260417.html', 'a', encoding='utf-8') as f:
    f.write(html_content)

print("TAB 4 价值投资风向已追加")
