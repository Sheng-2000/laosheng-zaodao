#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成老盛早知道 2026年4月17日 HTML文件 - 第二部分
"""

html_content = '''
<div class="tab-panel" id="panel-2">
  <div class="inner">
    <div class="section-title">🌍 国内外新闻</div>
    <div class="sub-section">
      <div class="sub-title">国际要闻</div>
      <div class="card">
        <div class="card-title"><span class="tag tag-energy">地缘</span>美伊接近达成框架性协议，全球地缘风险大幅降温</div>
        <div class="card-body">央视记者4月15日获悉，美伊谈判代表正逐步接近达成结束冲突的框架性协议。特朗普表示"很有可能"在4月下旬与伊朗达成协议。以色列与黎巴嫩启动为期10天临时停火。全球风险偏好大幅改善，油价承压，美股纳指再创历史新高。</div>
      </div>
      <div class="card">
        <div class="card-title"><span class="tag tag-policy">政策</span>特朗普：4月下旬或与伊朗达成协议</div>
        <div class="card-body">特朗普在白宫记者会上表示，美国与伊朗"很有可能"在4月下旬达成框架协议。若协议达成，将结束持续数月的地区紧张局势，全球能源供应风险将显著下降。</div>
      </div>
      <div class="card">
        <div class="card-title"><span class="tag tag-ai">科技</span>美股纳指十连阳创历史新高，科技股强势</div>
        <div class="card-body">4月16日美股纳斯达克实现连续第十个交易日上涨，创下自2023年以来的最长连涨纪录，标普500逼近7000点大关。科技股表现强势，算力巨头携手冲高，GPT-6发布持续催化AI板块。</div>
      </div>
    </div>
    <div class="sub-section">
      <div class="sub-title">国内要闻</div>
      <div class="card">
        <div class="card-title"><span class="tag tag-policy">宏观</span>A股强势延续：创业板涨3.17%创近11年新高</div>
        <div class="card-body">4月16日A股收盘：上证指数4055.55(+0.70%)；深证成指14796.33(+2.05%)；创业板指3626.27(+3.17%)，创2015年6月以来近11年新高！两市成交约23400亿元，超4300只个股上涨。AI与新能源主线集体爆发。</div>
      </div>
      <div class="card">
        <div class="card-title"><span class="tag tag-finance">市场</span>宁德时代跃居A股总市值第三</div>
        <div class="card-body">宁德时代4月16日大涨，市值跃升至A股第三。公司宣布将于4月21日举办"超级科技日"，预计展示全固态电池阶段性成果及麒麟电池迭代技术。新能源产业链4-5月排产同比增6成，行业景气度持续上行。</div>
      </div>
      <div class="card">
        <div class="card-title"><span class="tag tag-policy">政策</span>港股同步大涨，恒指涨1.72%收复两万六</div>
        <div class="card-body">4月16日港股收盘：恒生指数26394.26(+1.72%)，恒生科技指数6201.85(+2.55%)。南向资金净买入约85亿港元，科技股领涨，美团、小米、阿里巴巴涨幅显著。</div>
      </div>
    </div>
  </div>
</div>

<div class="tab-panel" id="panel-3">
  <div class="inner">
    <div class="section-title">🤖 AI前沿</div>
    <div class="sub-section">
      <div class="sub-title">AI大模型动态</div>
      <div class="card">
        <div class="card-title"><span class="tag tag-ai">GPT-6</span>OpenAI发布GPT-6，200万Token上下文+多模态能力全面升级</div>
        <div class="card-body">OpenAI正式发布GPT-6模型，核心升级包括：①上下文窗口扩展至200万Token；②多模态能力增强，支持视频理解与生成长达10分钟；③推理能力显著提升，数学与代码任务准确率提高40%。GPT-6的发布进一步确认AI算力需求高增趋势，利好算力云、液冷散热、光模块等产业链。</div>
      </div>
      <div class="card">
        <div class="card-title"><span class="tag tag-ai">算力</span>三大运营商2026年资本开支合计增长约43%</div>
        <div class="card-body">中国移动、中国电信、中国联通2026年资本开支预算合计增长约43%，主要用于AI算力基础设施建设。中国移动算力云收入增速超50%，GPT-6发布是最核心催化剂。</div>
      </div>
    </div>
    <div class="sub-section">
      <div class="sub-title">AI产业应用</div>
      <div class="card">
        <div class="card-title"><span class="tag tag-chip">液冷</span>液冷散热成为数据中心标配，订单能见度超12个月</div>
        <div class="card-body">GPT-6 200万Token上下文对算力密度要求极高，液冷散热成为数据中心标配。光迅科技、中际旭创等光模块龙头订单能见度超12个月，行业景气度持续上行。</div>
      </div>
      <div class="card">
        <div class="card-title"><span class="tag tag-policy">电力</span>AI用电需求高增，核电、水电受益逻辑强化</div>
        <div class="card-body">AI数据中心用电量呈指数级增长，长江电力、中国核电作为基荷电源最受益。中国核电未来5年装机增速保持10%+，中金DCF测算存在约30%低估空间。</div>
      </div>
    </div>
  </div>
</div>
'''

# 追加到文件
with open('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/老盛的每日快讯/WorkBuddy版/老盛早知道_20260417.html', 'a', encoding='utf-8') as f:
    f.write(html_content)

print("第二部分写入完成")
