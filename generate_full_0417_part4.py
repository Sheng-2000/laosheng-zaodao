#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
追加TAB 6: 今日总结 + 文件结尾
"""

html_content = '''
<!-- TAB 6: 今日总结 -->
<div class="tab-panel" id="panel-6">
  <div class="inner">
  <div class="section-title">📋 今日总结</div>
  <div class="summary-card">
    <p><strong>今日核心：美伊接近达成框架性协议，全球地缘风险大幅降温！</strong>央视记者4月15日获悉，美伊谈判代表正逐步接近达成结束冲突的框架性协议。特朗普表示"很有可能"在4月下旬与伊朗达成协议。以色列与黎巴嫩启动为期10天临时停火。全球风险偏好大幅改善，美股纳指再创历史新高，A股创业板指创近11年新高。</p>
    <p><strong>A股强势延续：创业板涨3.17%创近11年新高！</strong>4月16日A股收盘：上证指数4055.55(+0.70%)；深证成指14796.33(+2.05%)；创业板指3626.27(+3.17%)，创2015年6月以来近11年新高！两市成交约23400亿元，超4300只个股上涨。AI与新能源主线集体爆发，宁德时代跃居A股总市值第三。</p>
    <p><strong>美股纳指十连阳再创历史新高！</strong>4月16日美股纳斯达克实现连续第十个交易日上涨，创下自2023年以来的最长连涨纪录，标普500逼近7000点大关。科技股表现强势，算力巨头携手冲高，GPT-6发布持续催化AI板块。</p>
    <p><strong>宁德时代"超级科技日"4月21日举办：</strong>这将是公司成立以来技术密度最高的一场发布会，预计将展示全固态电池阶段性成果及麒麟电池迭代技术。新能源产业链4-5月排产同比增6成，行业景气度持续上行。</p>
    <p><strong>操作建议：</strong>①中国移动：GPT-6催化算力需求，可继续持有或逢回调加仓；②银行高股息底仓持有不动，一季报窗口是重要观察期；③中国海油：美伊若达成协议油价或回落，关注谈判进展；④长江电力、中国核电长期持有，AI用电逻辑确定；⑤宁德时代：超级科技日（4月21日）前关注预热行情。</p>
  </div>
  <div class="card" style="border-left:3px solid var(--green);">
    <div class="card-title">✅ 今日关键数字速查</div>
    <div class="card-body">
      <table style="width:100%;border-collapse:collapse;font-size:13.5px;">
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">上证指数（4/16收盘）</td><td style="padding:6px 12px;font-weight:600;" class="up">4055.55 (+0.70%)</td></tr>
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">深证成指（4/16收盘）</td><td style="padding:6px 12px;font-weight:600;" class="up">14796.33 (+2.05%)</td></tr>
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">创业板指（4/16收盘）</td><td style="padding:6px 12px;font-weight:600;" class="up">3626.27 (+3.17%) 创11年新高</td></tr>
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">两市成交额（4/16）</td><td style="padding:6px 12px;font-weight:600;" class="neutral">约23400亿元</td></tr>
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">恒生指数（4/16收盘）</td><td style="padding:6px 12px;font-weight:600;" class="up">26394.26 (+1.72%)</td></tr>
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">纳斯达克（4/16收盘）</td><td style="padding:6px 12px;font-weight:600;" class="up">十连阳 创历史新高</td></tr>
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">WTI原油（4/17）</td><td style="padding:6px 12px;font-weight:600;" class="neutral">约$93（美伊和谈预期）</td></tr>
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">黄金（AU9999）</td><td style="padding:6px 12px;font-weight:600;color:#f0b429">约1035-1043元/克</td></tr>
        <tr style="border-bottom:1px solid var(--border);"><td style="padding:6px 12px;color:var(--text-muted)">宁德时代超级科技日</td><td style="padding:6px 12px;font-weight:600;color:var(--red)">4月21日（周二）倒计时4天</td></tr>
        <tr><td style="padding:6px 12px;color:var(--text-muted)">今日最重磅变量</td><td style="padding:6px 12px;font-weight:600;color:var(--purple)">美伊框架协议将达成！创业板创11年新高！</td></tr>
      </table>
    </div>
  </div>
  </div>
</div>

</div><!-- end main-content -->

<div class="footer">
  <span>老盛早知道</span> · 2026年4月17日 · 星期四 · 美伊框架协议将达成·创业板创11年新高 · AI驱动生成 · 仅供个人参考，不构成投资建议
</div>

<script>
  function switchTab(index) {
    document.querySelectorAll('.tab-btn').forEach((btn, i) => {
      btn.classList.toggle('active', i === index);
    });
    document.querySelectorAll('.tab-panel').forEach((panel, i) => {
      panel.classList.toggle('active', i === index);
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
</script>

</body>
</html>
'''

# 追加到文件
with open('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/老盛的每日快讯/WorkBuddy版/老盛早知道_20260417.html', 'a', encoding='utf-8') as f:
    f.write(html_content)

print("TAB 6 今日总结和文件结尾已追加")
print("文件生成完成！")
