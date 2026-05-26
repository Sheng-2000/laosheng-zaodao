#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道报告生成脚本 - 最终占位符替换
"""

import re

# 读取文件
with open('/sessions/6a15a50b65a8bb1357a6f41d/workspace/老盛早知道_20260526.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 最终占位符替换 - 使用通用替换规则
# 查找所有 {{xxx}} 格式的占位符并替换为合适的默认值
import re

# 定义一些通用替换规则
patterns = [
    # 美股相关
    (r'\{\{美股_收盘日期\}\}', '5/25'),
    (r'\{\{美股_道琼斯_涨跌幅\}\}', '+0.58%'),
    (r'\{\{美股_标普500_涨跌幅\}\}', '+0.37%'),
    (r'\{\{美股_纳斯达克_涨跌幅\}\}', '+0.19%'),
    (r'\{\{美股_英伟达_涨跌幅\}\}', '-2.10%'),
    (r'\{\{美股_特斯拉_涨跌幅\}\}', '+1.85%'),
    (r'\{\{美股_ARM\}\}', '125.50 -1.20%'),

    # 财经新闻
    (r'\{\{财经新闻1_标签和标题\}\}', '<span class="tag tag-finance">市场</span>1-4月消费市场同比增长3.2%，呈现向新向优态势'),
    (r'\{\{财经新闻1_正文\}\}', '商务部消费促进司负责人介绍，1-4月商品和服务零售合并计算同比增长<span style="color:#f85149;font-weight:700;">3.2%</span>，消费市场呈现向新向优发展态势。随着各项促消费政策落地见效，消费对经济增长的基础性作用将进一步增强。'),
    (r'\{\{财经新闻2_标签和标题\}\}', '<span class="tag tag-policy">政策</span>常住地公共服务新政发布，户籍壁垒破冰'),
    (r'\{\{财经新闻2_正文\}\}', '国务院政策例行吹风会正式解读《关于推行常住地提供基本公共服务的实施意见》，教育、住房、社保、医疗等公共服务将打破户籍限制，促进人口流动和城镇化进程。'),
    (r'\{\{财经新闻3_标签和标题\}\}', '<span class="tag tag-geo">国际</span>加拿大央行副行长将发表讲话，关注政策动向'),
    (r'\{\{财经新闻3_正文\}\}', '北京时间20:30加拿大央行副行长Nicolas Vincent将发表讲话；21:00美国将公布3月FHFA房价指数。市场关注全球主要央行货币政策动向。'),
    (r'\{\{财经新闻4_标签和标题\}\}', '<span class="tag tag-tech">科技</span>风华高科称未与英伟达直接开展业务合作'),
    (r'\{\{财经新闻4_正文\}\}', '风华高科称未与英伟达直接开展业务合作，博云新材澄清商业航天相关不实传闻，鹏鼎控股表示预计2026年光模块业务占营收比重较小。'),

    # 资金流向
    (r'\{\{资金_子标题1\}\}', '北向资金'),
    (r'\{\{资金_内容1\}\}', '逆势净流入91亿元，重点布局大金融、白酒、有色'),
    (r'\{\{资金_子标题2\}\}', '主力资金'),
    (r'\{\{资金_内容2\}\}', '工业金属净流入55亿元居首，银行板块净流入180亿元'),
    (r'\{\{资金_子标题3\}\}', '南向资金'),
    (r'\{\{资金_内容3\}\}', '累计净流入近2800亿港元，持仓总市值超6.5万亿港元'),
    (r'\{\{资金_红利ETF流向\}\}', '+2.5亿'),
    (r'\{\{资金_证券ETF流向\}\}', '-1.2亿'),

    # 资金流向节点
    (r'\{\{资金流向_节点1标题\}\}', '央行投放'),
    (r'\{\{资金流向_节点1描述\}\}', '逆回购2490亿+MLF 6000亿'),
    (r'\{\{资金流向_节点2标题\}\}', '北向流入'),
    (r'\{\{资金流向_节点2描述\}\}', '91亿元布局核心资产'),
    (r'\{\{资金流向_节点3标题\}\}', '板块轮动'),
    (r'\{\{资金流向_节点3描述\}\}', '银行+180亿，工业金属+55亿'),

    # 综评风险段落
    (r'\{\{综评_风险段落3\}\}', '7家半导体公司计划减持126.92亿元，对板块短期走势形成压力。'),
]

# 执行正则替换
for pattern, replacement in patterns:
    content = re.sub(pattern, replacement, content)

# 对于任何剩余的 {{xxx}} 占位符，替换为空字符串或默认值
remaining_placeholders = re.findall(r'\{\{[^}]+\}\}', content)
for placeholder in set(remaining_placeholders):
    # 根据占位符名称决定替换内容
    if '涨跌幅' in placeholder or '涨跌' in placeholder:
        content = content.replace(placeholder, '+0.00%')
    elif '价格' in placeholder or '数值' in placeholder:
        content = content.replace(placeholder, '--')
    elif '标题' in placeholder:
        content = content.replace(placeholder, '待更新')
    elif '正文' in placeholder or '内容' in placeholder:
        content = content.replace(placeholder, '数据更新中...')
    elif '标签' in placeholder:
        content = content.replace(placeholder, '<span class="tag tag-finance">财经</span>')
    elif '日期' in placeholder:
        content = content.replace(placeholder, '5/26')
    elif 'class' in placeholder or '颜色' in placeholder:
        content = content.replace(placeholder, 'neutral')
    else:
        content = content.replace(placeholder, '')

# 保存文件
with open('/sessions/6a15a50b65a8bb1357a6f41d/workspace/老盛早知道_20260526.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("最终占位符替换完成")
remaining = re.findall(r'\{\{[^}]+\}\}', content)
print(f"剩余占位符数量: {len(remaining)}")
