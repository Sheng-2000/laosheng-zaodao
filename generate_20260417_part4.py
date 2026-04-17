#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成老盛早知道 2026年4月17日 HTML文件 - 第四部分：关注标的
13只标的：7只银行 + 6只公用事业/能源/通信
"""

html_content = '''
<div class="tab-panel" id="panel-5">
  <div class="inner">
    <div class="section-title">🏦 关注标的信息面</div>
    <div class="hot-bar" style="margin-bottom:16px;"><strong>📌 个股价格：</strong>以下为4月16日行情参考数据。今日最大变量：美伊框架协议接近达成，地缘风险降温；宁德时代超级科技日（4月21日）倒计时。</div>
    
    <!-- 银行股（7只） -->
    <div class="stock-card" style="border-color:rgba(240,180,41,0.5);">
      <div class="stock-header">
        <span class="stock-name">工商银行</span><span class="stock-code">601398 / 1398.HK</span><span class="tag tag-energy" style="margin-left:6px;">股息率4.08%</span>
        <div class="stock-price-area"><div class="stock-price neutral">7.31</div><div class="stock-change neutral">4/16收盘价</div></div>
      </div>
      <ul class="stock-bullets">
        <li><strong>2025年报核心数据</strong>：净利润3685.62亿元(+0.7%)，不良率1.31%(降0.03ppt)，核心一级资本充足率13.57%。</li>
        <li>年度分红3.103元/10股，当前A股股息率约4.08%；H股股息率约5.5%，持续吸引险资增配。</li>
        <li>中金首选标的之一，银行板块"配置红利"新阶段核心持仓。</li>
      </ul>
    </div>
    
    <div class="stock-card" style="border-color:rgba(0,212,255,0.3);">
      <div class="stock-header">
        <span class="stock-name">招商银行</span><span class="stock-code">600036 / 3968.HK</span><span class="tag tag-finance" style="margin-left:6px;">股息率5.22%</span>
        <div class="stock-price-area"><div class="stock-price neutral">39.21</div><div class="stock-change neutral">4/16收盘价</div></div>
      </div>
      <ul class="stock-bullets">
        <li><strong>2025年报：营收利润双增长</strong>，ROE继续领跑股份行，零售贷款质量改善。</li>
        <li>当前股息率5.22%，PB约0.9x，低于历史均值1.4x；中金目标价46元，隐含约17%上涨空间。</li>
        <li>城商行中零售业务最强标的，适合中长期核心仓位。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">农业银行</span><span class="stock-code">601288 / 1288.HK</span><span class="tag tag-finance" style="margin-left:6px;">股息率3.57%（A股）</span>
        <div class="stock-price-area"><div class="stock-price neutral">6.59</div><div class="stock-change neutral">4/16收盘价（A股）</div></div>
      </div>
      <ul class="stock-bullets">
        <li>平安人寿持H股超20%举牌门槛；H股股息率约7.2%，四大行H股最高，是险资配置首选。</li>
        <li>PB约0.60x，四大行最低，安全边际突出；"三农"政策背景下农村金融竞争壁垒稳固。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">宁波银行</span><span class="stock-code">002142</span><span class="tag tag-policy" style="margin-left:6px;">一季报窗口</span>
        <div class="stock-price-area"><div class="stock-price neutral">30.25</div><div class="stock-change neutral">4/16收盘价</div></div>
      </div>
      <ul class="stock-bullets">
        <li>ROE持续领先城商行同业（约15%），零售和小微信贷质量优异。</li>
        <li>一季报预计4月末前披露，核心关注净利润增速及分红政策。</li>
        <li>PB约0.91x，较历史均值有折价，城商行基本面最优质标的之一。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">江苏银行</span><span class="stock-code">600919</span><span class="tag tag-policy" style="margin-left:6px;">一季报窗口</span>
        <div class="stock-price-area"><div class="stock-price neutral">10.78</div><div class="stock-change neutral">4/16收盘价（股息率5.27%）</div></div>
      </div>
      <ul class="stock-bullets">
        <li>一季报预计4月中旬前披露，市场预期净利润增速约12%，资产规模有望突破4万亿。</li>
        <li>股息率5.27%，PB约0.65x低估显著；江苏省经济强劲，区域龙头地位稳固。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">杭州银行</span><span class="stock-code">600926</span><span class="tag tag-policy" style="margin-left:6px;">一季报窗口</span>
        <div class="stock-price-area"><div class="stock-price neutral">17.15</div><div class="stock-change neutral">4/16收盘价（股息率4.42%）</div></div>
      </div>
      <ul class="stock-bullets">
        <li>杭州银行深耕长三角，受益于数字经济、新制造业集聚；ROE约14%。</li>
        <li>股息率4.42%，PB约0.72x，处于历史低位区间；一季报催化有望推动估值修复。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">重庆银行</span><span class="stock-code">601963</span><span class="tag tag-policy" style="margin-left:6px;">一季报窗口</span>
        <div class="stock-price-area"><div class="stock-price neutral">约10.47</div><div class="stock-change neutral">4/16收盘价（股息率约4.7%）</div></div>
      </div>
      <ul class="stock-bullets">
        <li>重庆区域经济基本面稳健，城商行中西部代表性龙头；股息率约4.7%。</li>
        <li>PB处于历史低位；一季报预期稳健，若信贷增速超预期存在估值修复空间。</li>
      </ul>
    </div>
    
    <!-- 公用事业/央企高股息（6只） -->
    <div class="sub-title" style="margin:28px 0 18px;">公用事业 / 央企高股息</div>
    
    <div class="stock-card" style="border-color:rgba(0,212,255,0.45);">
      <div class="stock-header">
        <span class="stock-name">中国移动</span><span class="stock-code">600941 / 0941.HK</span><span class="tag tag-ai" style="margin-left:6px;">GPT-6最强催化</span>
        <div class="stock-price-area"><div class="stock-price neutral">重点关注</div><div class="stock-change up">算力云签单量激增</div></div>
      </div>
      <ul class="stock-bullets">
        <li><strong>GPT-6发布是最核心催化剂。</strong>算力需求加速放量，三大运营商2026年资本开支合计增长约43%。</li>
        <li>A股股息率约5.9%，H股约6.8%，算力（云/AI）收入增速超50%，PB约0.9x处历史低位。</li>
        <li>AI算力+高股息"双主线"交集标的，中长期逻辑最为清晰确定。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">长江电力</span><span class="stock-code">600900</span><span class="tag tag-policy" style="margin-left:6px;">股息率约4.5%</span>
        <div class="stock-price-area"><div class="stock-price neutral">约27-28</div><div class="stock-change neutral">稳健防御</div></div>
      </div>
      <ul class="stock-bullets">
        <li>分红承诺率≥70%，股息率约4.5%；AI用电需求高增是长期需求驱动力。</li>
        <li>本周一季度来水数据将公布，来水情况决定短期电量弹性。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">中国核电</span><span class="stock-code">601985</span><span class="tag tag-policy" style="margin-left:6px;">股息率约4.6%</span>
        <div class="stock-price-area"><div class="stock-price neutral">约11-12</div><div class="stock-change neutral">AI用电需求逻辑</div></div>
      </div>
      <ul class="stock-bullets">
        <li>中金DCF测算合理市值约2419亿，当前约1859亿，低估约30%；未来5年装机增速保持10%+。</li>
        <li>GPT-6发布进一步确认AI用电需求高增，核电作为基荷电力最受益。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">大秦铁路</span><span class="stock-code">601006</span><span class="tag tag-energy" style="margin-left:6px;">股息率约6%</span>
        <div class="stock-price-area"><div class="stock-price neutral">约9-10</div><div class="stock-change neutral">稳健分红资产</div></div>
      </div>
      <ul class="stock-bullets">
        <li>国内最重要的煤炭运输大动脉，运量稳健；PB约1.0x，PE约9x，股息率约6%。</li>
        <li>AI用电需求推动煤炭能源需求保持稳定，运量有望小幅回升。</li>
      </ul>
    </div>
    
    <div class="stock-card" style="border-color:rgba(240,180,41,0.4);">
      <div class="stock-header">
        <span class="stock-name">中国海油</span><span class="stock-code">600938 / 0883.HK</span><span class="tag tag-energy" style="margin-left:6px;">油价$93 盈利可观</span>
        <div class="stock-price-area"><div class="stock-price neutral">WTI $93</div><div class="stock-change neutral">美伊和谈预期</div></div>
      </div>
      <ul class="stock-bullets">
        <li><strong>当前油价约$93，</strong>中国海油桶油成本约$28，桶油利润约$65，盈利依然可观。</li>
        <li>美伊若达成框架协议，油价或回落至$75-80区间，届时需重新评估目标价。H股股息率预计超过6%。</li>
      </ul>
    </div>
    
    <div class="stock-card">
      <div class="stock-header">
        <span class="stock-name">中国平安</span><span class="stock-code">601318 / 2318.HK</span><span class="tag tag-finance" style="margin-left:6px;">股息率约5.5%</span>
        <div class="stock-price-area"><div class="stock-price neutral">约50-55</div><div class="stock-change neutral">险资举牌联动</div></div>
      </div>
      <ul class="stock-bullets">
        <li>2025年NBV增速超20%，寿险改革效果持续显现；股息率约5.5%，PE约9.1x，PB约0.78x。</li>
        <li>平安人寿持农行H股超20%举牌，权益法核算带来稳定投资收益。</li>
      </ul>
    </div>
  </div>
</div>
'''

# 追加到文件
with open('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/老盛的每日快讯/WorkBuddy版/老盛早知道_20260417.html', 'a', encoding='utf-8') as f:
    f.write(html_content)

print("第四部分（关注标的）写入完成")
