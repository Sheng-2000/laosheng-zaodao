#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道报告生成脚本 - Tab 2 AI前沿
"""

import re

# 读取文件
with open('/sessions/6a15a50b65a8bb1357a6f41d/workspace/老盛早知道_20260526.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Tab 2 AI新闻替换
replacements = {
    # AI新闻1 - 人工智能+全面升级
    '{{AI新闻1_标签和标题}}': '<span class="tag tag-ai">AI政策</span>中央定调！"人工智能+"行动升级为全面实施',
    '{{AI新闻1_正文}}': '2026年5月26日，中国AI产业迎来里程碑式双重官宣！中央政治局会议将"人工智能+"行动从"深入实施"升级为<span style="color:#f85149;font-weight:700;">全面实施</span>，AI正式迈入规模化、商业化落地黄金期。这意味着AI技术将在更多领域得到应用推广，相关产业链将迎来爆发式增长机遇。',

    # AI新闻2 - 阿里云Qwen大会
    '{{AI新闻2_标签和标题}}': '<span class="tag tag-ai">大模型</span>阿里云Qwen Conference 2026：迈向Agentic Ecosystem',
    '{{AI新闻2_正文}}': '阿里云Qwen Conference 2026于5月26日举行，主题方向是从基础模型走向完整的<span style="color:#f85149;font-weight:700;">Agentic Ecosystem</span>（智能体生态系统）。这标志着大模型技术正在从单纯的对话工具向能够自主决策、执行任务的智能体演进，将大幅提升AI在各行各业的应用价值。',

    # AI新闻3 - 工信部汽车AI标准
    '{{AI新闻3_标签和标题}}': '<span class="tag tag-chip">产业政策</span>工信部：系统布局汽车人工智能标准',
    '{{AI新闻3_正文}}': '工信部发布2026年汽车标准化工作要点，推进汽车人工智能技术应用、平台架构及<span style="color:#f85149;font-weight:700;">车用大模型能力评价</span>等国家标准制定。随着智能驾驶和车联网技术的发展，汽车AI标准将成为行业发展的重要支撑。',

    # AI新闻4 - 宇树科技过会
    '{{AI新闻4_标签和标题}}': '<span class="tag tag-robot">机器人</span>宇树科技6月1日科创板过会，人形机器人第一股',
    '{{AI新闻4_正文}}': '宇树科技<span style="color:#f85149;font-weight:700;">6月1日</span>科创板过会，成为人形机器人第一股，拟募资<span style="color:#00d4ff;font-weight:700;">42亿元</span>，助力工业母机与机器人产业链发展。宇树科技在人形机器人领域技术领先，此次上市将加速国产机器人产业化和商业化进程。',

    # AI新闻5 - 华为韬定律
    '{{AI新闻5_标签和标题}}': '<span class="tag tag-chip">芯片</span>华为"韬定律"突破制程，秋季麒麟芯片性能或提升300%',
    '{{AI新闻5_正文}}': '华为在IEEE会议提出<span style="color:#f85149;font-weight:700;">"时间缩微"</span>替代"几何缩微"，突破传统制程极限；秋季麒麟芯片性能或提升<span style="color:#f85149;font-weight:700;">300%</span>。这一技术突破将大幅提升国产芯片性能，降低对先进制程的依赖，对国产半导体产业链具有重要意义。',

    # AI新闻6 - 英伟达下一代平台
    '{{AI新闻6_标签和标题}}': '<span class="tag tag-chip">算力</span>英伟达下一代Vera Rubin平台就绪，推理成本降至1/10',
    '{{AI新闻6_正文}}': '英伟达下一代<span style="color:#f85149;font-weight:700;">Vera Rubin</span>平台已经Ready，推理Token成本是Blackwell的<span style="color:#3fb950;font-weight:700;">十分之一</span>，同规模模型训练所需GPU大幅减少。这将进一步降低AI训练和推理成本，推动大模型技术普及应用。',

    # AI新闻7 - 特斯拉FSD
    '{{AI新闻7_标签和标题}}': '<span class="tag tag-app">自动驾驶</span>特斯拉FSD在10个国家开放，中国已可使用',
    '{{AI新闻7_正文}}': '特斯拉宣布其监督版FSD（完全自动驾驶能力）已在包括<span style="color:#f85149;font-weight:700;">中国</span>在内的10个国家或地区开放使用。FSD入华将加速国内智能驾驶市场竞争，推动相关产业链技术升级。',

    # AI新闻8 - 半导体减持
    '{{AI新闻8_标签和标题}}': '<span class="tag tag-chip">市场</span>7家半导体公司计划减持，总规模达126.92亿元',
    '{{AI新闻8_正文}}': '7家公司计划减持总规模达<span style="color:#f85149;font-weight:700;">126.92亿元</span>。此前半导体板块大幅上涨，多只个股创下股价历史新高。此次减持引发市场关注，或对板块短期走势产生影响，投资者需关注相关风险。',
}

# 执行替换
for placeholder, value in replacements.items():
    content = content.replace(placeholder, value)

# 保存文件
with open('/sessions/6a15a50b65a8bb1357a6f41d/workspace/老盛早知道_20260526.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Tab 2 替换完成")
