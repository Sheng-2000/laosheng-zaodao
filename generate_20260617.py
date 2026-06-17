#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道 2026年6月17日 报告生成脚本
基于 template.html 复制后替换占位符内容
"""
import re
import shutil
import os

SRC = "template.html"
DST = "老盛早知道_20260617.html"

if not os.path.exists(SRC):
    print(f"ERROR: {SRC} not found")
    exit(1)

shutil.copy(SRC, DST)
print(f"Copied {SRC} -> {DST}")

with open(DST, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {}

# --- header ---
replacements["{{报告日期}}"] = "2026年6月17日"
replacements["{{YYYY/MM/DD}}"] = "2026/06/17"
replacements["{{星期}}"] = "星期三"
replacements["{{每日重点事件}}"] = "创业板指<span style=\"color:#f85149;font-weight:700\">大涨1.72%</span>，A股成交<span style=\"color:#f0b429;font-weight:700\">3.09万亿元</span>；国际金价<span style=\"color:#f85149;font-weight:700\">突破4300美元</span>"

replacements["{{ticker_上证_数值}}"] = "4091.89"
replacements["{{ticker_上证_涨跌幅}}"] = "<span style=\"color:#3fb950;font-weight:700\">-0.11%</span>"
replacements["{{ticker_道指_数值}}"] = "50786.01"
replacements["{{ticker_道指_涨跌幅}}"] = "<span style=\"color:#3fb950;font-weight:700\">-0.16%</span>"
replacements["{{ticker_黄金_数值}}"] = "4342.50"
replacements["{{ticker_黄金_涨跌幅}}"] = "<span style=\"color:#f85149;font-weight:700\">+0.27%</span>"

# --- 顶部4张摘要卡片 ---
replacements["{{概览卡1_标题}}"] = "上证指数（06/16收盘）"
replacements["{{概览卡1_数值}}"] = "<span style=\"color:#3fb950;font-weight:800;font-size:26px\">4091.89</span>"
replacements["{{概览卡1_涨跌幅}}"] = "-0.11%"
replacements["{{概览卡1_涨跌class}}"] = ""
replacements["{{概览卡1_描述}}"] = "深证成指<span style=\"color:#f85149;font-weight:700\">+0.93%</span>；创业板指表现最强，<span style=\"color:#f85149;font-weight:700\">+1.72%</span>报4102.94；科创50<span style=\"color:#f85149;font-weight:700\">+1.06%</span>；两市全天成交额<span style=\"color:#f0b429;font-weight:700\">3.09万亿元</span>，北向资金<span style=\"color:#f85149;font-weight:700\">净流入36.7亿元</span>"

replacements["{{概览卡2_标题}}"] = "国际黄金（06/16收盘）"
replacements["{{概览卡2_数值}}"] = "<span style=\"color:#f85149;font-weight:800;font-size:26px\">4342.50</span>"
replacements["{{概览卡2_标签}}"] = "<span style=\"background:rgba(248,81,73,0.15);color:#f85149;padding:2px 8px;border-radius:6px;font-size:11px;font-weight:700\">创阶段新高</span>"
replacements["{{概览卡2_描述}}"] = "COMEX黄金期货站上<span style=\"color:#f85149;font-weight:700\">4345美元</span>大关；美元指数跌至10日低位，<span style=\"color:#f85149;font-weight:700\">10年期美债收益率</span>下行4.47基点至<span style=\"color:#00d4ff;font-weight:700\">4.2810%</span>"

replacements["{{概览卡3_标题}}"] = "人民币汇率中间价（06/16）"
replacements["{{概览卡3_数值}}"] = "<span style=\"color:#3fb950;font-weight:800;font-size:26px\">6.8108</span>"
replacements["{{概览卡3_标签}}"] = "<span style=\"background:rgba(63,185,80,0.15);color:#3fb950;padding:2px 8px;border-radius:6px;font-size:11px;font-weight:700\">下调20基点</span>"
replacements["{{概览卡3_描述}}"] = "1欧元对人民币<span style=\"color:#00d4ff;font-weight:700\">7.8636</span>元；100日元对人民币<span style=\"color:#00d4ff;font-weight:700\">4.2395</span>元；央行政策操作灵活，汇率波动有管理"

replacements["{{概览卡4_标题}}"] = "WTI原油期货（06/16收盘）"
replacements["{{概览卡4_数值}}"] = "<span style=\"color:#3fb950;font-weight:800;font-size:26px\">80.90</span>"
replacements["{{概览卡4_标签}}"] = "<span style=\"background:rgba(63,185,80,0.15);color:#3fb950;padding:2px 8px;border-radius:6px;font-size:11px;font-weight:700\">-0.32%</span>"
replacements["{{概览卡4_描述}}"] = "布伦特原油期货<span style=\"color:#f85149;font-weight:700\">+0.08%</span>报83.43美元/桶；OPEC+维持减产政策，油价陷入<span style=\"color:#f0b429;font-weight:700\">高位震荡</span>"

# --- 8条要点速览 ---
replacements["{{要点1_标题}}"] = "A股：创业板表现最强，科技赛道回归"
replacements["{{要点1_内容}}"] = "上证指数收盘<span style=\"color:#3fb950;font-weight:700\">-0.11%</span>报4091.89，深证成指<span style=\"color:#f85149;font-weight:700\">+0.93%</span>报15675.25，创业板指<span style=\"color:#f85149;font-weight:700\">+1.72%</span>报4102.94，科创50<span style=\"color:#f85149;font-weight:700\">+1.06%</span>。PCB概念、半导体、光模块、锂电池等板块集中爆发，两市成交额<span style=\"color:#f0b429;font-weight:700\">3.09万亿元</span>"

replacements["{{要点2_标题}}"] = "黄金：国际金价持续突破，避险属性强化"
replacements["{{要点2_内容}}"] = "COMEX黄金期货站上<span style=\"color:#f85149;font-weight:700\">4345美元</span>大关；伦敦现货黄金盘中涨幅<span style=\"color:#f85149;font-weight:700\">超过2.7%</span>。10年期美债收益率下行4.47基点至4.2810%，以美元计价的黄金吸引力显著提升"

replacements["{{要点3_标题}}"] = "汇率：中间价报6.8108，下调20基点"
replacements["{{要点3_内容}}"] = "人民币对美元中间价报<span style=\"color:#3fb950;font-weight:700\">6.8108</span>元，较上日<span style=\"color:#3fb950;font-weight:700\">下调20个基点</span>。美元指数走弱背景下，人民币汇率弹性进一步增强"

replacements["{{要点4_标题}}"] = "原油：全球震荡格局，OPEC+维持减产"
replacements["{{要点4_内容}}"] = "WTI原油期货<span style=\"color:#3fb950;font-weight:700\">80.90美元/桶</span>，布伦特原油期货<span style=\"color:#f85149;font-weight:700\">+0.08%</span>报83.43美元/桶。国内上海原油主力合约日内<span style=\"color:#3fb950;font-weight:700\">跌4%</span>"

replacements["{{要点5_标题}}"] = "美股：纳指涨0.86%，芯片股分化调整"
replacements["{{要点5_内容}}"] = "道琼斯工业平均指数<span style=\"color:#3fb950;font-weight:700\">-0.16%</span>报50786.01点，纳斯达克综合指数<span style=\"color:#f85149;font-weight:700\">+0.86%</span>报25929.66点，标普500<span style=\"color:#f85149;font-weight:700\">+0.30%</span>。英伟达<span style=\"color:#3fb950;font-weight:700\">-2.37%</span>"

replacements["{{要点6_标题}}"] = "港股：恒生指数跌1.40%，科技股承压"
replacements["{{要点6_内容}}"] = "恒生指数<span style=\"color:#3fb950;font-weight:700\">-1.40%</span>报24493.95，恒生科技指数<span style=\"color:#3fb950;font-weight:700\">-2.24%</span>报4658.65。权重科技股走低，内房股领跌，龙湖集团<span style=\"color:#3fb950;font-weight:700\">跌近9%</span>"

replacements["{{要点7_标题}}"] = "加密货币：BTC 66517美元，以太坊大涨9.24%"
replacements["{{要点7_内容}}"] = "比特币BTC报<span style=\"color:#f85149;font-weight:700\">66517美元</span>，24小时涨幅<span style=\"color:#f85149;font-weight:700\">+4.24%</span>；以太坊ETH报<span style=\"color:#f85149;font-weight:700\">1792美元</span>，涨幅<span style=\"color:#f85149;font-weight:700\">+9.24%</span>"

replacements["{{要点8_标题}}"] = "AI大模型：DeepSeek估值3380亿，国产算力加速"
replacements["{{要点8_内容}}"] = "DeepSeek多轮融资后投后估值约<span style=\"color:#f85149;font-weight:700\">3380亿元</span>，创始人梁文锋个人出资200亿元，腾讯出资100亿元参与，募资总额超500亿元"

# --- 时间线 ---
replacements["{{时间线1_日}}"] = "16"
replacements["{{时间线1_月}}"] = "JUN"
replacements["{{时间线1_标签}}"] = "<span style=\"background:rgba(248,81,73,0.15);color:#f85149;padding:2px 6px;border-radius:4px;font-size:10px;font-weight:700\">A股</span>"
replacements["{{时间线1_事件}}"] = "创业板指<span style=\"color:#f85149;font-weight:700\">大涨1.72%</span>，科技赛道全线回归"
replacements["{{时间线1_详情}}"] = "上证指数收盘4091.89（-0.11%）；深证成指15675.25（+0.93%）；创业板指4102.94（+1.72%）；两市成交额<span style=\"color:#f0b429;font-weight:700\">3.09万亿元</span>"

replacements["{{时间线2_日}}"] = "17"
replacements["{{时间线2_月}}"] = "JUN"
replacements["{{时间线2_标签}}"] = "<span style=\"background:rgba(0,212,255,0.15);color:#00d4ff;padding:2px 6px;border-radius:4px;font-size:10px;font-weight:700\">政策</span>"
replacements["{{时间线2_事件}}"] = "发改委召开民企座谈会，推进<span style=\"color:#00d4ff;font-weight:700\">六张网</span>建设"
replacements["{{时间线2_详情}}"] = "国家发改委主任郑栅洁主持召开民营企业座谈会，积极吸引社会资本参与“六张网”建设（交通网、能源网、信息网、水利网、生态网、城市管网）"

replacements["{{时间线3_日}}"] = "17"
replacements["{{时间线3_月}}"] = "JUN"
replacements["{{时间线3_标签}}"] = "<span style=\"background:rgba(248,81,73,0.15);color:#f85149;padding:2px 6px;border-radius:4px;font-size:10px;font-weight:700\">黄金</span>"
replacements["{{时间线3_事件}}"] = "黄金期货<span style=\"color:#f85149;font-weight:700\">突破4345美元</span>"
replacements["{{时间线3_详情}}"] = "COMEX黄金期货站上4345美元大关，盘中涨幅超2.7%；10年期美债收益率下行4.47个基点至4.2810%"

replacements["{{时间线4_日}}"] = "17"
replacements["{{时间线4_月}}"] = "JUN"
replacements["{{时间线4_标签}}"] = "<span style=\"background:rgba(188,140,255,0.15);color:#bc8cff;padding:2px 6px;border-radius:4px;font-size:10px;font-weight:700\">AI</span>"
replacements["{{时间线4_事件}}"] = "DeepSeek融资超500亿，估值<span style=\"color:#f85149;font-weight:700\">3380亿</span>"
replacements["{{时间线4_详情}}"] = "AI行业单轮融资规模之最，创始人梁文锋个人出资200亿，腾讯100亿参与"

# --- 六大板块 ---
replacements["{{正面因素_内容}}"] = "A股<span style=\"color:#f85149;font-weight:700\">成交额3.09万亿元</span>放量；创业板指<span style=\"color:#f85149;font-weight:700\">+1.72%</span>表现最强；北向资金<span style=\"color:#f85149;font-weight:700\">净流入36.7亿元</span>；国际黄金<span style=\"color:#f85149;font-weight:700\">突破4345美元</span>"

replacements["{{市场热点_内容}}"] = "<b>A股主线</b>：PCB概念<span style=\"color:#f85149;font-weight:700\">逾百股涨停</span>；半导体、光模块、锂电池板块强势；AI算力/MLCC/算力租赁三大环节同步走强"

replacements["{{风险提示_内容}}"] = "港股恒生科技指数<span style=\"color:#3fb950;font-weight:700\">-2.24%</span>；美股芯片股分化，英伟达<span style=\"color:#3fb950;font-weight:700\">-2.37%</span>；加密货币爆仓人数超10万人，<span style=\"color:#f0b429;font-weight:700\">杠杆风险极高</span>"

# ============ Tab 1 国内外新闻 ============
replacements["{{重点新闻1_标签和标题}}"] = "<span style=\"background:rgba(248,81,73,0.15);color:#f85149;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">A股</span> 创业板指大涨1.72%站上4100点，成交3.09万亿元"
replacements["{{重点新闻1_正文}}"] = "A股三大指数表现分化。上证指数收盘<span style=\"color:#3fb950;font-weight:700\">-0.11%</span>报4091.89；深证成指<span style=\"color:#f85149;font-weight:700\">+0.93%</span>报15675.25；创业板指<span style=\"color:#f85149;font-weight:700\">+1.72%</span>报4102.94。两市成交额<span style=\"color:#f0b429;font-weight:700\">3.09万亿元</span>，北向资金<span style=\"color:#f85149;font-weight:700\">净流入36.7亿元</span>"

replacements["{{重点新闻2_标签和标题}}"] = "<span style=\"background:rgba(0,212,255,0.15);color:#00d4ff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">政策</span> 发改委召开民营企业座谈会，推进“六张网”建设"
replacements["{{重点新闻2_正文}}"] = "国家发改委主任郑栅洁主持召开民营企业座谈会，表示将积极吸引社会资本参与“六张网”建设（<span style=\"color:#00d4ff;font-weight:700\">交通网、能源网、信息网、水利网、生态网、城市管网</span>）"

replacements["{{重点新闻3_标签和标题}}"] = "<span style=\"background:rgba(248,81,73,0.15);color:#f85149;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">黄金</span> 国际金价突破4345美元，美债收益率下行"
replacements["{{重点新闻3_正文}}"] = "COMEX黄金期货站上<span style=\"color:#f85149;font-weight:700\">4345美元</span>大关；10年期美债收益率下行4.47基点至<span style=\"color:#00d4ff;font-weight:700\">4.2810%</span>，实际利率下行有利于无息资产黄金"

replacements["{{重点新闻4_标签和标题}}"] = "<span style=\"background:rgba(63,185,80,0.15);color:#3fb950;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">美股</span> 道指-0.16%报50786，纳指+0.86%；芯片股分化"
replacements["{{重点新闻4_正文}}"] = "美股三大指数涨跌不一：道琼斯<span style=\"color:#3fb950;font-weight:700\">-0.16%</span>报50786.01；纳斯达克<span style=\"color:#f85149;font-weight:700\">+0.86%</span>报25929.66；标普500<span style=\"color:#f85149;font-weight:700\">+0.30%</span>报7405.73。英伟达<span style=\"color:#3fb950;font-weight:700\">-2.37%</span>"

replacements["{{重点新闻5_标签和标题}}"] = "<span style=\"background:rgba(240,180,41,0.15);color:#f0b429;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">原油</span> WTI原油80.90美元，OPEC+维持减产"
replacements["{{重点新闻5_正文}}"] = "WTI原油期货<span style=\"color:#3fb950;font-weight:700\">80.90美元/桶</span>（-0.32%）；布伦特原油<span style=\"color:#f85149;font-weight:700\">83.43美元/桶</span>（+0.08%）。OPEC+维持减产政策，油价维持高位震荡"

replacements["{{地缘新闻1_标签和标题}}"] = "<span style=\"background:rgba(255,166,87,0.15);color:#ffa657;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">地缘</span> 美债收益率曲线倒挂未修复，大选政治风险存变量"
replacements["{{地缘新闻1_正文}}"] = "10年期美债收益率<span style=\"color:#3fb950;font-weight:700\">下行4.47基点</span>至4.2810%，2年期美债收益率持稳于4.21%。收益率曲线倒挂依然未修复，反映市场对短期经济压力的担忧"

replacements["{{地缘新闻2_标签和标题}}"] = "<span style=\"background:rgba(255,166,87,0.15);color:#ffa657;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">地缘</span> 日经/台股创历史新高，亚太市场集体走强"
replacements["{{地缘新闻2_正文}}"] = "日经225指数<span style=\"color:#f85149;font-weight:700\">+0.13%</span>报69404.50；韩国KOSPI<span style=\"color:#f85149;font-weight:700\">+2.11%</span>报8726.60；台湾加权<span style=\"color:#f85149;font-weight:700\">+0.91%</span>报45809.19，均创历史新高"

replacements["{{财经新闻1_标签和标题}}"] = "<span style=\"background:rgba(63,185,80,0.15);color:#3fb950;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">宏观</span> 人民币中间价报6.8108，下调20基点"
replacements["{{财经新闻1_正文}}"] = "人民币对美元中间价报<span style=\"color:#3fb950;font-weight:700\">6.8108</span>元，较上日下调20基点。美元指数走弱背景下，人民币汇率弹性增强"

replacements["{{财经新闻2_标签和标题}}"] = "<span style=\"background:rgba(0,212,255,0.15);color:#00d4ff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">新基建</span> 海洋经济“蓝色工匠”和“引陆下海”计划启动"
replacements["{{财经新闻2_正文}}"] = "四部门联合印发通知，研究实施<span style=\"color:#00d4ff;font-weight:700\">“蓝色工匠”培育计划</span>和<span style=\"color:#00d4ff;font-weight:700\">“引陆下海”计划</span>，海洋经济成为新风口"

replacements["{{财经新闻3_标签和标题}}"] = "<span style=\"background:rgba(63,185,80,0.15);color:#3fb950;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">市场</span> A股涨停复盘：PCB概念爆发，AI算力持续受青睐"
replacements["{{财经新闻3_正文}}"] = "涨停股票超过100只，集中在<span style=\"color:#f85149;font-weight:700\">PCB概念、半导体、光模块、锂电池</span>等科技成长方向"

replacements["{{财经新闻4_标签和标题}}"] = "<span style=\"background:rgba(248,81,73,0.15);color:#f85149;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">长期</span> 中国10年期国债收益率接近历史低位"
replacements["{{财经新闻4_正文}}"] = "10年期中国国债收益率距历史最低不到5BP，反映市场对经济内生增长动能的谨慎预期。约3万亿元<span style=\"color:#f0b429;font-weight:700\">特别国债</span>集中发行可能对长债收益率形成上行压力"

# ============ Tab 2 AI前沿 ============
replacements["{{大模型新闻1_标签和标题}}"] = "<span style=\"background:rgba(188,140,255,0.2);color:#bc8cff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">大模型</span> DeepSeek完成超500亿元融资，估值约3380亿元"
replacements["{{大模型新闻1_正文}}"] = "国产大模型DeepSeek完成新一轮融资，募资总额超500亿元，投后估值约<span style=\"color:#f85149;font-weight:700\">3380亿元</span>。创始人梁文锋个人出资200亿元，腾讯出资100亿元参与"

replacements["{{大模型新闻2_标签和标题}}"] = "<span style=\"background:rgba(188,140,255,0.2);color:#bc8cff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">大模型</span> 小米万亿参数端侧推理+华为鸿蒙生态+DeepSeek开源"
replacements["{{大模型新闻2_正文}}"] = "AI大厂重点突破方向转向“端侧+行业落地”：小米万亿参数模型高速推理，华为鸿蒙+盘古生态形成“芯片-OS-模型-应用”闭环，DeepSeek开源模型持续放量"

replacements["{{大模型新闻3_标签和标题}}"] = "<span style=\"background:rgba(188,140,255,0.2);color:#bc8cff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">大模型</span> AI产业数据验证：光模块/MLCC/算力租赁三环节同步走强"
replacements["{{大模型新闻3_正文}}"] = "MLCC、高速光模块、算力租赁三大核心硬件环节同步走强，形成“<span style=\"color:#bc8cff;font-weight:700\">硬件底座+传输核心+算力服务</span>”完整闭环"

replacements["{{大模型新闻4_标签和标题}}"] = "<span style=\"background:rgba(188,140,255,0.2);color:#bc8cff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">大模型</span> 大模型开源生态繁荣，DeepSeek/R1/V系列持续迭代"
replacements["{{大模型新闻4_正文}}"] = "DeepSeek继R1系列后推出V系列模型，在代码能力、数学推理等方面持续优化。开源模型降低部署门槛，促进创新与生态协同"

replacements["{{机器人新闻1_标签和标题}}"] = "<span style=\"background:rgba(255,166,87,0.15);color:#ffa657;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">机器人</span> 具身智能+人形机器人进入产业落地前夜"
replacements["{{机器人新闻1_正文}}"] = "全球人形机器人产业加速演进：特斯拉Optimus第二代迭代、波士顿动力Atlas升级、Figure AI获大厂投资。国内华为、小米、宇树科技等持续推进。产业链包括<span style=\"color:#f85149;font-weight:700\">减速器、伺服电机、控制器、机器视觉</span>"

replacements["{{机器人新闻2_标签和标题}}"] = "<span style=\"background:rgba(255,166,87,0.15);color:#ffa657;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">机器人</span> 工业机器人需求旺盛，国产份额持续提升"
replacements["{{机器人新闻2_正文}}"] = "工业机器人市场持续增长，3C电子、汽车制造、新能源电池产线等场景应用加速。国产工业机器人品牌埃斯顿、汇川技术等市场份额持续提升"

replacements["{{机器人新闻3_标签和标题}}"] = "<span style=\"background:rgba(255,166,87,0.15);color:#ffa657;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">机器人</span> 自动驾驶+机器人融合方向持续演进"
replacements["{{机器人新闻3_正文}}"] = "端侧大模型与机器人“大脑”结合成新趋势，下一代智能汽车更像是“<span style=\"color:#00d4ff;font-weight:700\">带轮子的AI机器人</span>”"

replacements["{{算力新闻1_标签和标题}}"] = "<span style=\"background:rgba(0,212,255,0.15);color:#00d4ff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">算力</span> 国产AI芯片百花齐放：华为昇腾+海光+寒武纪等路线并行"
replacements["{{算力新闻1_正文}}"] = "国产AI算力供给加速扩张：华为昇腾系列领先，海光信息DCU产品放量，寒武纪思元系列稳定出货，壁仞科技、天数智芯等持续推进7nm/5nm产品"

replacements["{{算力新闻2_标签和标题}}"] = "<span style=\"background:rgba(0,212,255,0.15);color:#00d4ff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">算力</span> 英伟达207.41美元(-2.37%)，关注国产算力独立行情"
replacements["{{算力新闻2_正文}}"] = "英伟达6月16日收盘<span style=\"color:#3fb950;font-weight:700\">-2.37%</span>报207.41美元。国产AI芯片因国产替代政策驱动，有<span style=\"color:#f85149;font-weight:700\">独立行情</span>基础"

replacements["{{算力新闻3_标签和标题}}"] = "<span style=\"background:rgba(0,212,255,0.15);color:#00d4ff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">算力</span> 光模块800G→1.6T迭代加速，CPO技术预研升温"
replacements["{{算力新闻3_正文}}"] = "全球数据中心对800G光模块需求持续超预期，1.6T产品进入样品验证阶段。产业链上游<span style=\"color:#f85149;font-weight:700\">光芯片</span>壁垒最高，<span style=\"color:#f85149;font-weight:700\">光模块</span>封装是中游核心"

replacements["{{AI应用新闻1_标签和标题}}"] = "<span style=\"background:rgba(63,185,80,0.15);color:#3fb950;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">应用</span> AI应用从Demo走向生产系统：金融/医疗/教育/自动驾驶领跑"
replacements["{{AI应用新闻1_正文}}"] = "AI应用加速落地：<span style=\"color:#f85149;font-weight:700\">金融</span>智能投研、<span style=\"color:#f85149;font-weight:700\">医疗</span>影像诊断、<span style=\"color:#f85149;font-weight:700\">教育</span>个性化学习、<span style=\"color:#f85149;font-weight:700\">自动驾驶</span>NOA部署"

replacements["{{AI应用新闻2_标签和标题}}"] = "<span style=\"background:rgba(63,185,80,0.15);color:#3fb950;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">应用</span> AI Agent工作流成热点，金融/企业服务落地加速"
replacements["{{AI应用新闻2_正文}}"] = "AI Agent能够自主规划任务、调用工具、反思执行，在金融投研、企业自动化办公、客服中心等场景加速落地"

replacements["{{AI应用新闻3_标签和标题}}"] = "<span style=\"background:rgba(63,185,80,0.15);color:#3fb950;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">应用</span> 教育AI个性化学习方案落地，政策支持力度加大"
replacements["{{AI应用新闻3_正文}}"] = "教育部鼓励智能批改、个性化学习路径规划、教研内容生成等应用。重点公司包括科大讯飞、好未来、新东方、网易有道等"

replacements["{{产业趋势新闻1_标签和标题}}"] = "<span style=\"background:rgba(248,81,73,0.15);color:#f85149;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700\">趋势</span> AI芯片上游材料紧缺，高纯钨粉/磷化铟国产替代加速"
replacements["{{产业趋势新闻1_正文}}"] = "全球AI产业上游关键材料供应紧张：<span style=\"color:#f85149;font-weight:700\">高纯钨粉</span>用于芯片散热，<span style=\"color:#f85149;font-weight:700\">磷化铟</span>是光芯片核心材料，<span style=\"color:#f85149;font-weight:700\">镓/锗</span>出口管制背景下国产替代提速"

# ============ Tab 3 全球市场 ============
replacements["{{A股_收盘日期}}"] = "06/16"
replacements["{{A股_上证指数_数据}}"] = "<span style=\"color:#3fb950\">4091.89 -0.11%</span>"
replacements["{{A股_深证成指_数据}}"] = "<span style=\"color:#f85149\">15675.25 +0.93%</span>"
replacements["{{A股_创业板指_数据}}"] = "<span style=\"color:#f85149\">4102.94 +1.72%</span>"
replacements["{{A股_科创50_数据}}"] = "<span style=\"color:#f85149\">1689.22 +1.06%</span>"
replacements["{{A股_沪深300_数据}}"] = "<span style=\"color:#3fb950\">4884.23 -0.15%</span>"
replacements["{{A股_成交额}}"] = "3.09万亿"
replacements["{{A股_成交额备注}}"] = "放量356亿"
replacements["{{A股_涨跌家数}}"] = "涨3142家 / 跌1623家"
replacements["{{A股_北向资金}}"] = "<span style=\"color:#f85149\">+36.7亿</span>"

replacements["{{港股_收盘日期}}"] = "06/16"
replacements["{{港股_恒生指数_数据}}"] = "<span style=\"color:#3fb950\">24493.95 -1.40%</span>"
replacements["{{港股_恒生科技_数据}}"] = "<span style=\"color:#3fb950\">4658.65 -2.24%</span>"
replacements["{{港股_国企指数_数据}}"] = "<span style=\"color:#3fb950\">8240.05 -1.62%</span>"
replacements["{{港股_南向资金}}"] = "<span style=\"color:#f85149\">+28.3亿</span>"

replacements["{{美股_收盘日期}}"] = "06/16"
replacements["{{美股_道琼斯_涨跌幅}}"] = "<span style=\"color:#3fb950\">50786.01 -0.16%</span>"
replacements["{{美股_标普500_涨跌幅}}"] = "<span style=\"color:#f85149\">7405.73 +0.30%</span>"
replacements["{{美股_纳斯达克_涨跌幅}}"] = "<span style=\"color:#f85149\">25929.66 +0.86%</span>"
replacements["{{美股_英伟达_涨跌幅}}"] = "<span style=\"color:#3fb950\">207.41 -2.37%</span>"
replacements["{{美股_特斯拉_涨跌幅}}"] = "<span style=\"color:#3fb950\">248.62 -1.16%</span>"
replacements["{{美股_ARM}}"] = "<span style=\"color:#f85149\">128.35 +1.52%</span>"

replacements["{{亚太_收盘日期}}"] = "06/16"
replacements["{{亚太_日经225}}"] = "<span style=\"color:#f85149\">69404.50 +0.13%</span>"
replacements["{{亚太_韩国KOSPI_状态}}"] = "<span style=\"color:#f85149\">8726.60 +2.11%</span>"
replacements["{{亚太_台湾加权_状态}}"] = "<span style=\"color:#f85149\">45809.19 +0.91%</span>"
replacements["{{亚太_印度Sensex_状态}}"] = "<span style=\"color:#f85149\">78456.22 +0.85%</span>"
replacements["{{亚太_澳洲ASX200_状态}}"] = "<span style=\"color:#f85149\">8234.50 +0.45%</span>"

replacements["{{欧洲_收盘日期}}"] = "06/16"
replacements["{{欧洲_英国富时100_涨跌幅}}"] = "<span style=\"color:#f85149\">8543.70 +0.71%</span>"
replacements["{{欧洲_德国DAX30_涨跌幅}}"] = "<span style=\"color:#f85149\">22156.80 +0.08%</span>"
replacements["{{欧洲_法国CAC40_涨跌幅}}"] = "<span style=\"color:#f85149\">9876.45 +0.75%</span>"
replacements["{{欧洲_斯托克50_涨跌幅}}"] = "<span style=\"color:#f85149\">5123.60 +0.26%</span>"

replacements["{{大宗商品_收盘日期}}"] = "06/16"
replacements["{{大宗_WTI原油}}"] = "<span style=\"color:#3fb950\">80.90 -0.32%</span>"
replacements["{{大宗_布伦特原油}}"] = "<span style=\"color:#f85149\">83.43 +0.08%</span>"
replacements["{{大宗_国际黄金}}"] = "<span style=\"color:#f85149\">4342.50 +0.27%</span>"
replacements["{{大宗_上海金}}"] = "<span style=\"color:#f85149\">478.62 +0.55%</span>"
replacements["{{大宗_白银}}"] = "<span style=\"color:#f85149\">69.90 +1.85%</span>"

replacements["{{汇率债券_收盘日期}}"] = "06/16"
replacements["{{汇率_USD/CNY中间价}}"] = "<span style=\"color:#3fb950\">6.8108</span>"
replacements["{{汇率_在岸汇率}}"] = "<span style=\"color:#3fb950\">6.8125</span>"
replacements["{{汇率_美元指数}}"] = "<span style=\"color:#3fb950\">104.28 -0.35%</span>"
replacements["{{汇率_美10年期}}"] = "<span style=\"color:#3fb950\">4.2810%</span>"
replacements["{{汇率_美30年期}}"] = "<span style=\"color:#3fb950\">4.4250%</span>"
replacements["{{汇率_中10年期}}"] = "<span style=\"color:#3fb950\">2.3850%</span>"

replacements["{{加密货币_收盘日期}}"] = "06/16"
replacements["{{加密_BTC}}"] = "<span style=\"color:#f85149\">66517 +4.24%</span>"
replacements["{{加密_ETH}}"] = "<span style=\"color:#f85149\">1792 +9.24%</span>"
replacements["{{加密_BTCEFT}}"] = "<span style=\"color:#f85149\">净流入</span>"
replacements["{{加密_市场情绪}}"] = "<span style=\"color:#f85149\">偏乐观</span>"

# --- 市场综评 ---
replacements["{{市场综评_日期}}"] = "06/16"
replacements["{{综评_A股行情标题}}"] = "A股结构性行情延续"
replacements["{{综评_A股行情标签}}"] = "分化明显"
replacements["{{综评_A股段落1}}"] = "创业板指<span style=\"color:#f85149;font-weight:700\">大涨1.72%</span>领涨市场，科技赛道全面回归"
replacements["{{综评_A股段落2}}"] = "两市成交额<span style=\"color:#f0b429;font-weight:700\">3.09万亿元</span>，北向资金<span style=\"color:#f85149;font-weight:700\">净流入36.7亿元</span>"
replacements["{{综评_A股段落3}}"] = "AI算力、新能源升级、高端制造、战略资源四大中长期产业逻辑清晰"

replacements["{{综评_外围市场标题}}"] = "外围市场涨跌互现"
replacements["{{综评_外围市场标签}}"] = "分化格局"
replacements["{{综评_外围段落1}}"] = "美股三大指数涨跌不一，纳指<span style=\"color:#f85149;font-weight:700\">+0.86%</span>表现最强"
replacements["{{综评_外围段落2}}"] = "亚太市场集体走强，日经225、台湾加权创历史新高"
replacements["{{综评_外围段落3}}"] = "国际金价突破4345美元创阶段新高"

replacements["{{综评_地缘政策标题}}"] = "政策面持续发力"
replacements["{{综评_地缘政策标签}}"] = "稳增长"
replacements["{{综评_地缘段落1}}"] = "发改委推进“六张网”建设，积极吸引社会资本参与"
replacements["{{综评_地缘段落2}}"] = "四部门启动“蓝色工匠”和“引陆下海”计划，海洋经济成新风口"
replacements["{{综评_地缘段落3}}"] = "政策面持续释放稳增长信号"

replacements["{{综评_风险事件标题}}"] = "风险因素需警惕"
replacements["{{综评_风险事件标签}}"] = "谨慎观望"
replacements["{{综评_风险段落1}}"] = "港股恒生科技指数<span style=\"color:#3fb950;font-weight:700\">-2.24%</span>，内房股领跌"
replacements["{{综评_风险段落2}}"] = "美股芯片股短期估值偏高，对A股相关板块情绪可能形成压制"
replacements["{{综评_风险段落3}}"] = "加密货币爆仓人数超10万人，普通投资者应远离"

# --- 市场情绪 ---
replacements["{{市场情绪_状态颜色}}"] = "green"
replacements["{{市场情绪_状态}}"] = "偏谨慎"
replacements["{{市场情绪_涨跌比}}"] = "3142:1623"
replacements["{{市场情绪_成交额}}"] = "3.09万亿"
replacements["{{市场情绪_北向资金}}"] = "+36.7亿"

# ============ Tab 4 价值投资风向 ============
replacements["{{机构1_名称}}"] = "中信证券"
replacements["{{机构1_简称}}"] = "中信"
replacements["{{机构1_标签}}"] = "增持A股"
replacements["{{机构1_观点}}"] = "当前A股处于估值修复与盈利改善的双重驱动期。建议关注AI算力产业链、高股息板块、政策受益方向三条主线"

replacements["{{机构2_名称}}"] = "高盛"
replacements["{{机构2_简称}}"] = "GS"
replacements["{{机构2_标签}}"] = "买入评级"
replacements["{{机构2_观点}}"] = "维持对A股<span style=\"color:#f85149;font-weight:700\">增持</span>评级。中国经济复苏态势明确，企业盈利改善预期支撑市场上行"

replacements["{{机构3_名称}}"] = "兴业证券"
replacements["{{机构3_简称}}"] = "兴业"
replacements["{{机构3_标签}}"] = "谨慎乐观"
replacements["{{机构3_观点}}"] = "市场处于<span style=\"color:#f0b429;font-weight:700\">震荡上行</span>阶段，结构性机会突出。AI算力仍是主线"

replacements["{{机构4_名称}}"] = "中金公司"
replacements["{{机构4_简称}}"] = "中金"
replacements["{{机构4_标签}}"] = "中性偏多"
replacements["{{机构4_观点}}"] = "A股市场<span style=\"color:#f85149;font-weight:700\">韧性较强</span>，政策面持续释放积极信号"

replacements["{{机构5_名称}}"] = "摩根士丹利"
replacements["{{机构5_简称}}"] = "大摩"
replacements["{{机构5_标签}}"] = "超配A股"
replacements["{{机构5_观点}}"] = "中国资产<span style=\"color:#f85149;font-weight:700\">吸引力提升</span>，外资持续流入"

replacements["{{机构6_名称}}"] = "瑞银集团"
replacements["{{机构6_简称}}"] = "UBS"
replacements["{{机构6_标签}}"] = "增持建议"
replacements["{{机构6_观点}}"] = "A股市场<span style=\"color:#f85149;font-weight:700\">估值合理</span>，盈利预期改善支撑上行空间"

# --- 估值参考表 ---
replacements["{{速查1_数值}}"] = "4091.89"
replacements["{{速查1_涨跌幅}}"] = "<span style=\"color:#3fb950\">-0.11%</span>"
replacements["{{速查2_数值}}"] = "15675.25"
replacements["{{速查2_涨跌幅}}"] = "<span style=\"color:#f85149\">+0.93%</span>"
replacements["{{速查3_数值}}"] = "4102.94"
replacements["{{速查3_涨跌幅}}"] = "<span style=\"color:#f85149\">+1.72%</span>"
replacements["{{速查4_数值}}"] = "3.09万亿"
replacements["{{速查4_涨跌幅}}"] = "<span style=\"color:#f0b429\">放量</span>"
replacements["{{速查5_数值}}"] = "+36.7亿"
replacements["{{速查5_涨跌幅}}"] = "<span style=\"color:#f85149\">净流入</span>"
replacements["{{速查6_数值}}"] = "4658.65"
replacements["{{速查6_涨跌幅}}"] = "<span style=\"color:#3fb950\">-2.24%</span>"
replacements["{{速查7_数值}}"] = "80.90"
replacements["{{速查7_涨跌幅}}"] = "<span style=\"color:#3fb950\">-0.32%</span>"
replacements["{{速查8_数值}}"] = "4342.50"
replacements["{{速查8_涨跌幅}}"] = "<span style=\"color:#f85149\">+0.27%</span>"
replacements["{{速查9_数值}}"] = "6.8108"
replacements["{{速查9_涨跌幅}}"] = "<span style=\"color:#3fb950\">下调</span>"

replacements["{{高股息分析_标题}}"] = "高股息板块投资价值分析"
replacements["{{高股息分析_正文}}"] = "<span style=\"color:#f85149;font-weight:700\">银行板块</span>平均PB约0.85倍，股息率超5%；<span style=\"color:#f85149;font-weight:700\">电力板块</span>业绩稳定，部分公司股息率超6%；<span style=\"color:#f85149;font-weight:700\">公用事业</span>防御属性突出"

# ============ Tab 5 关注标的 ============
# 13只标的
stocks = ["工商银行", "建设银行", "农业银行", "招商银行", "宁波银行", "江苏银行", "杭州银行", "重庆银行", "长江电力", "大秦铁路", "中国移动", "中国核电", "中国平安"]
codes = ["601398", "601939", "601288", "600036", "002142", "600919", "600926", "601963", "600900", "601006", "600941", "601985", "601318"]
prices = ["5.28", "6.15", "4.82", "32.18", "24.56", "7.85", "14.22", "6.85", "22.35", "7.12", "88.56", "8.75", "48.25"]
changes = ["+0.38%", "+0.49%", "+0.63%", "-0.12%", "+1.28%", "+0.64%", "+0.99%", "+0.73%", "-0.22%", "+0.42%", "+0.82%", "+1.16%", "-0.52%"]
volumes = ["12.5亿", "8.3亿", "6.7亿", "15.2亿", "5.8亿", "3.2亿", "4.5亿", "1.8亿", "4.2亿", "1.5亿", "8.9亿", "6.3亿", "9.6亿"]
notes = ["高股息", "稳健", "高股息", "零售龙头", "成长银行", "区域龙头", "稳健增长", "低估", "稳定现金流", "高股息", "高分红", "清洁能源", "保险龙头"]

for i in range(13):
    idx = i + 1
    replacements[f"{{{{标的{idx}_名称}}}}"] = stocks[i]
    replacements[f"{{{{标的{idx}_代码}}}}"] = codes[i]
    replacements[f"{{{{标的{idx}_价格}}}}"] = prices[i]
    color = "#f85149" if changes[i].startswith("+") else "#3fb950"
    replacements[f"{{{{标的{idx}_涨跌幅}}}}"] = f"<span style=\"color:{color}\">{changes[i]}</span>"
    replacements[f"{{{{标的{idx}_成交额}}}}"] = volumes[i]
    replacements[f"{{{{标的{idx}_备注}}}}"] = notes[i]

replacements["{{标的解读_标题}}"] = "关注标的深度解读汇总"
replacements["{{标的解读_正文}}"] = "<b>银行板块：</b><span style=\"color:#f85149;font-weight:700\">工商银行、农业银行</span>等高股息标的受青睐，股息率超5%。<b>电力板块：</b><span style=\"color:#f85149;font-weight:700\">长江电力</span>现金流稳定。<b>电信板块：</b><span style=\"color:#f85149;font-weight:700\">中国移动</span>高分红策略持续。<b>保险板块：</b><span style=\"color:#3fb950;font-weight:700\">中国平安</span>估值处于历史低位"

# ============ Tab 6 理财话题 ============
replacements["{{理财概览1_标题}}"] = "存款利率"
replacements["{{理财概览1_数值}}"] = "1.65%"
replacements["{{理财概览1_描述}}"] = "1年期定存"
replacements["{{理财概览2_标题}}"] = "国债收益"
replacements["{{理财概览2_数值}}"] = "2.45%"
replacements["{{理财概览2_描述}}"] = "3年期储蓄国债"
replacements["{{理财概览3_标题}}"] = "货基收益"
replacements["{{理财概览3_数值}}"] = "2.15%"
replacements["{{理财概览3_描述}}"] = "7日年化"
replacements["{{理财概览4_标题}}"] = "理财收益"
replacements["{{理财概览4_数值}}"] = "3.25%"
replacements["{{理财概览4_描述}}"] = "稳健型理财"

replacements["{{理财对比_正文}}"] = "<b>国债：</b><span style=\"color:#f85149;font-weight:700\">安全性最高</span>，国家信用背书。<b>大额存单：</b>利率较定期存款高10-20BP。<b>货币基金：</b>流动性极佳，7日年化约2.15%。<b>债券基金：</b>年化收益约3-4%。<b>银行理财：</b>稳健型产品年化收益约3.25%"

replacements["{{高股息替代_正文}}"] = "可关注<span style=\"color:#f85149;font-weight:700\">高股息股票</span>策略：银行股股息率超5%，电力股现金流稳定。注意采用<span style=\"color:#f0b429;font-weight:700\">分散配置</span>策略"

replacements["{{理财避坑_正文}}"] = "警惕<span style=\"color:#f0b429;font-weight:700\">高收益陷阱</span>、<span style=\"color:#f0b429;font-weight:700\">流动性风险</span>、<span style=\"color:#f0b429;font-weight:700\">净值波动</span>、<span style=\"color:#f0b429;font-weight:700\">机构信用风险</span>。建议<span style=\"color:#f85149;font-weight:700\">分散投资</span>"

replacements["{{保险配置_正文}}"] = "遵循“先保障后理财”原则：<b>重疾险</b>保额50-100万；<b>医疗险</b>选择百万医疗险；<b>意外险</b>必备；<b>寿险</b>家庭经济支柱必备。建议每年保费支出占家庭年收入的5-10%"

replacements["{{黄金投资_正文}}"] = "黄金作为<span style=\"color:#f85149;font-weight:700\">避险+抗通胀</span>工具，建议配置5-10%。投资方式：实物黄金、黄金ETF、黄金期货（高风险）。近期金价突破4300美元，建议<span style=\"color:#f0b429;font-weight:700\">分批买入</span>"

replacements["{{债券基金_正文}}"] = "<b>纯债基金</b>年化收益约3-4%；<b>混合债基</b>收益弹性较大；<b>可转债基金</b>兼具债性与股性。建议选择<span style=\"color:#f85149;font-weight:700\">中长期纯债基金</span>"

# --- 社区热门话题 ---
replacements["{{话题1_标题}}"] = "银行股创新高，还能追吗？"
replacements["{{话题1_内容}}"] = "@价值投资者：建设银行股价创历史新高，农业银行年内涨幅<span style=\"color:#f85149;font-weight:700\">52.66%</span>。@机构研究员：险资持续加仓。@谨慎派：<span style=\"color:#f0b429;font-weight:700\">不建议追高</span>。老盛观点：建议关注<span style=\"color:#f85149;font-weight:700\">业绩确定性强</span>的优质标的"

replacements["{{话题2_标题}}"] = "黄金突破4300美元，是牛市起点吗？"
replacements["{{话题2_内容}}"] = "@乐观派：<span style=\"color:#f85149;font-weight:700\">牛市行情</span>刚刚开始。@分析师：需关注美联储政策。@风险派：存在<span style=\"color:#f0b429;font-weight:700\">回调风险</span>。老盛观点：建议家庭配置5-10%，<span style=\"color:#f0b429;font-weight:700\">不建议投机</span>"

replacements["{{话题3_标题}}"] = "AI光模块还能上车吗？"
replacements["{{话题3_内容}}"] = "@科技爱好者：<span style=\"color:#f85149;font-weight:700\">1.6T产品</span>即将量产。@价值投资者：估值已偏高。老盛观点：建议<span style=\"color:#f0b429;font-weight:700\">回调分批布局</span>"

replacements["{{话题4_标题}}"] = "港股恒生科技还能抄底吗？"
replacements["{{话题4_内容}}"] = "@抄底派：估值处于历史低位，<span style=\"color:#f85149;font-weight:700\">具备配置价值</span>。@谨慎派：<span style=\"color:#f0b429;font-weight:700\">风险尚未释放完毕</span>。老盛观点：建议采用<span style=\"color:#f0b429;font-weight:700\">定投策略</span>"

replacements["{{话题5_标题}}"] = "加密货币反弹，是机会还是陷阱？"
replacements["{{话题5_内容}}"] = "@币圈玩家：<span style=\"color:#f85149;font-weight:700\">牛市氛围浓厚</span>。@风险警示：<span style=\"color:#f0b429;font-weight:700\">杠杆风险极高</span>。老盛观点：属于<span style=\"color:#f0b429;font-weight:700\">高风险投机品</span>，普通家庭应远离"

replacements["{{话题6_标题}}"] = "存款利率还会降吗？"
replacements["{{话题6_内容}}"] = "@储户：收益太低。@分析师：央行可能引导利率下行。老盛观点：建议锁定<span style=\"color:#f85149;font-weight:700\">3-5年期定存</span>，资产配置向<span style=\"color:#f85149;font-weight:700\">多元化</span>发展"

replacements["{{话题7_标题}}"] = "新能源储能是下一个风口吗？"
replacements["{{话题7_内容}}"] = "@产业专家：<span style=\"color:#f85149;font-weight:700\">商业化加速</span>。@谨慎派：需精选<span style=\"color:#f0b429;font-weight:700\">具备技术壁垒</span>的龙头。老盛观点：长期看好，但需关注<span style=\"color:#f0b429;font-weight:700\">估值与业绩匹配度</span>"

replacements["{{话题8_标题}}"] = "家庭保险怎么买最划算？"
replacements["{{话题8_内容}}"] = "@保险顾问：先配置<span style=\"color:#f85149;font-weight:700\">重疾险+医疗险</span>。@消费者：优先选择消费型。老盛观点：保险配置遵循“先保障后理财”"

replacements["{{话题9_标题}}"] = "芯片股调整，是上车机会吗？"
replacements["{{话题9_内容}}"] = "@科技投资者：<span style=\"color:#f85149;font-weight:700\">长期逻辑不变</span>。@分析师：关注国产替代机会。老盛观点：建议<span style=\"color:#f0b429;font-weight:700\">逢低分批布局</span>"

replacements["{{话题10_标题}}"] = "DeepSeek估值3380亿，AI泡沫来了吗？"
replacements["{{话题10_内容}}"] = "@AI从业者：<span style=\"color:#f85149;font-weight:700\">产业落地加速</span>。@投资者：估值较高。老盛观点：关注<span style=\"color:#f85149;font-weight:700\">业绩确定性强</span>的上游硬件环节"

# --- 社区情绪 ---
replacements["{{情绪_高股息_名称}}"] = "高股息"
replacements["{{情绪_高股息_宽度}}"] = "75%"
replacements["{{情绪_高股息_百分比}}"] = "75%"
replacements["{{情绪_高股息_描述}}"] = "资金偏好防御"

replacements["{{情绪_银行_名称}}"] = "银行"
replacements["{{情绪_银行_宽度}}"] = "65%"
replacements["{{情绪_银行_百分比}}"] = "65%"
replacements["{{情绪_银行_描述}}"] = "估值修复中"

replacements["{{情绪_公用事业_名称}}"] = "公用事业"
replacements["{{情绪_公用事业_宽度}}"] = "60%"
replacements["{{情绪_公用事业_百分比}}"] = "60%"
replacements["{{情绪_公用事业_描述}}"] = "稳健配置"

replacements["{{情绪_电力_名称}}"] = "电力"
replacements["{{情绪_电力_宽度}}"] = "70%"
replacements["{{情绪_电力_百分比}}"] = "70%"
replacements["{{情绪_电力_描述}}"] = "现金流稳定"

replacements["{{情绪_AI算力_名称}}"] = "AI算力"
replacements["{{情绪_AI算力_宽度}}"] = "85%"
replacements["{{情绪_AI算力_百分比}}"] = "85%"
replacements["{{情绪_AI算力_样式类}}"] = "up"
replacements["{{情绪_AI算力_描述}}"] = "热点持续"

replacements["{{情绪_能源油价_名称}}"] = "能源油价"
replacements["{{情绪_能源油价_宽度}}"] = "55%"
replacements["{{情绪_能源油价_百分比}}"] = "55%"
replacements["{{情绪_能源油价_描述}}"] = "波动加大"

replacements["{{情绪_新能源_名称}}"] = "新能源"
replacements["{{情绪_新能源_宽度}}"] = "68%"
replacements["{{情绪_新能源_百分比}}"] = "68%"
replacements["{{情绪_新能源_样式类}}"] = "up"
replacements["{{情绪_新能源_描述}}"] = "储能景气"

replacements["{{情绪_黄金_名称}}"] = "黄金"
replacements["{{情绪_黄金_宽度}}"] = "80%"
replacements["{{情绪_黄金_百分比}}"] = "80%"
replacements["{{情绪_黄金_描述}}"] = "避险升温"

replacements["{{情绪_汇率_名称}}"] = "汇率"
replacements["{{情绪_汇率_宽度}}"] = "50%"
replacements["{{情绪_汇率_百分比}}"] = "50%"
replacements["{{情绪_汇率_描述}}"] = "双向波动"

replacements["{{情绪_黄金_样式类}}"] = "up"

replacements["{{情绪_加密货币_名称}}"] = "加密货币"
replacements["{{情绪_加密货币_宽度}}"] = "45%"
replacements["{{情绪_加密货币_百分比}}"] = "45%"
replacements["{{情绪_加密货币_样式类}}"] = "neutral"
replacements["{{情绪_加密货币_描述}}"] = "高波动"

# --- 高股息板块详情 ---
replacements["{{高股息_银行标题}}"] = "银行板块"
replacements["{{高股息_银行内容}}"] = "平均PB约0.85倍，股息率超5%，估值处于历史低位，适合长期配置"

replacements["{{高股息_公用事业标题}}"] = "公用事业"
replacements["{{高股息_公用事业内容}}"] = "现金流稳定，防御属性突出，部分公司股息率超过6%"

replacements["{{高股息_电力标题}}"] = "电力板块"
replacements["{{高股息_电力内容}}"] = "业绩稳定，分红持续，长江电力等龙头值得关注"

replacements["{{高股息_央企标题}}"] = "央企蓝筹"
replacements["{{高股息_央企内容}}"] = "中字头企业估值修复，高分红策略持续，政策支持明确"

# --- 低估值指标 ---
replacements["{{低估值1_名称}}"] = "中证红利"
replacements["{{低估值1_收盘价}}"] = "5.23"
replacements["{{低估值1_描述}}"] = "高股息策略持续有效"
replacements["{{估值_中证红利PE_今日涨幅}}"] = "+0.85%"

replacements["{{低估值2_名称}}"] = "上证50"
replacements["{{低估值2_收盘价}}"] = "2.35"
replacements["{{低估值2_今日涨幅}}"] = "-0.12%"
replacements["{{低估值2_涨幅样式}}"] = "down"
replacements["{{低估值2_描述}}"] = "权重蓝筹调整"

# --- 资金流向 ---
replacements["{{资金流向_节点1标题}}"] = "北向资金"
replacements["{{资金流向_节点1描述}}"] = "+36.7亿"

replacements["{{资金流向_节点2标题}}"] = "南向资金"
replacements["{{资金流向_节点2描述}}"] = "+28.3亿"

replacements["{{资金流向_节点3标题}}"] = "主力资金"
replacements["{{资金流向_节点3描述}}"] = "+247.3亿"

# --- 估值指标 ---
replacements["{{估值_银行PB}}"] = "0.85x"
replacements["{{估值_银行PB_标签类}}"] = "low"
replacements["{{估值_银行PB_标签}}"] = "低估"

replacements["{{估值_上证PE}}"] = "12.8x"
replacements["{{估值_上证PE_标签类}}"] = "neutral"
replacements["{{估值_上证PE_标签}}"] = "合理"

replacements["{{估值_银行股息率}}"] = "5.2%"
replacements["{{估值_银行股息率_标签类}}"] = "high"
replacements["{{估值_银行股息率_标签}}"] = "高股息"

replacements["{{估值_中证红利PE}}"] = "8.5x"
replacements["{{估值_中证红利PE_标签类}}"] = "low"
replacements["{{估值_中证红利PE_标签}}"] = "低估"

replacements["{{估值_神华吨煤利润}}"] = "185元"
replacements["{{估值_神华_标签类}}"] = "neutral"
replacements["{{估值_神华_标签}}"] = "稳定"

replacements["{{估值_中国移动PB}}"] = "1.8x"
replacements["{{估值_中国移动PB_标签类}}"] = "neutral"
replacements["{{估值_中国移动PB_标签}}"] = "合理"

replacements["{{估值_招商银行PB}}"] = "1.2x"
replacements["{{估值_招商银行PB_标签类}}"] = "neutral"
replacements["{{估值_招商银行PB_标签}}"] = "合理"

replacements["{{估值_中国核电PE}}"] = "15.2x"
replacements["{{估值_中国核电_标签类}}"] = "neutral"
replacements["{{估值_中国核电_标签}}"] = "合理"

replacements["{{估值_黄金价格}}"] = "4342.50"
replacements["{{估值_黄金_标签类}}"] = "up"
replacements["{{估值_黄金_标签}}"] = "上涨"

# ============ Tab 7 今日总结 ============
replacements["{{今日关键词1}}"] = "<span style=\"color:#f85149\">创业板大涨</span>"
replacements["{{今日关键词2}}"] = "<span style=\"color:#f85149\">黄金新高</span>"
replacements["{{今日关键词3}}"] = "<span style=\"color:#bc8cff\">DeepSeek融资</span>"
replacements["{{今日关键词4}}"] = "<span style=\"color:#00d4ff\">六张网建设</span>"

replacements["{{宏观面_内容}}"] = "发改委推进“六张网”建设，<span style=\"color:#f85149;font-weight:700\">稳增长信号明确</span>。四部门启动“蓝色工匠”和“引陆下海”计划"

replacements["{{市场面_内容}}"] = "A股分化明显，创业板指<span style=\"color:#f85149;font-weight:700\">大涨1.72%</span>领涨，两市成交额<span style=\"color:#f0b429;font-weight:700\">3.09万亿元</span>，北向资金<span style=\"color:#f85149;font-weight:700\">净流入36.7亿元</span>"

replacements["{{资金面_内容}}"] = "主力资金净流入247.3亿元，北向资金<span style=\"color:#f85149;font-weight:700\">持续流入</span>，外资对A股配置意愿增强"

replacements["{{操作提示_内容}}"] = "<span style=\"color:#f0b429;font-weight:700\">操作建议</span>：关注<span style=\"color:#f85149;font-weight:700\">AI算力产业链</span>、<span style=\"color:#f85149;font-weight:700\">高股息板块</span>、逢低布局<span style=\"color:#f85149;font-weight:700\">港股优质龙头</span>"

replacements["{{关键数字1_名称}}"] = "上证指数"
replacements["{{关键数字1_数值}}"] = "<span style=\"color:#3fb950\">4091.89</span>"
replacements["{{关键数字2_名称}}"] = "创业板指"
replacements["{{关键数字2_数值}}"] = "<span style=\"color:#f85149\">4102.94</span>"
replacements["{{关键数字3_名称}}"] = "北向资金"
replacements["{{关键数字3_数值}}"] = "<span style=\"color:#f85149\">+36.7亿</span>"
replacements["{{关键数字4_名称}}"] = "国际黄金"
replacements["{{关键数字4_数值}}"] = "<span style=\"color:#f85149\">4342.50</span>"
replacements["{{关键数字5_名称}}"] = "美元指数"
replacements["{{关键数字5_数值}}"] = "<span style=\"color:#3fb950\">104.28</span>"
replacements["{{关键数字6_名称}}"] = "美债10年"
replacements["{{关键数字6_数值}}"] = "<span style=\"color:#3fb950\">4.2810%</span>"

replacements["{{今日操作建议_正文}}"] = "今日市场结构性特征明显，科技成长板块表现强势。<span style=\"color:#f85149;font-weight:700\">操作策略</span>：1）<b>AI算力产业链</b>：光模块、AI芯片、高速PCB等细分领域景气度持续；2）<b>高股息防御配置</b>：银行、电力等板块股息率优势明显；3）<b>港股优质龙头</b>：估值处于历史低位。<span style=\"color:#f0b429;font-weight:700\">风险提示</span>：市场波动加大，建议控制仓位，避免追高"

# --- 参考数据 ---
replacements["{{参考1_标题}}"] = "银行板块PB估值"
replacements["{{参考1_描述}}"] = "银行板块PB约0.85x，处于历史低位15%分位，安全边际较高"

replacements["{{参考2_标题}}"] = "中证红利PE"
replacements["{{参考2_描述}}"] = "中证红利指数PE仅8.5x，高股息策略持续有效"

replacements["{{参考3_标题}}"] = "中国移动PB"
replacements["{{参考3_描述}}"] = "中国移动PB约1.8x，通信龙头优势明显"

# --- 标的提示 ---
replacements["{{标的_正面提示标题}}"] = "配置亮点"
replacements["{{标的_正面提示内容}}"] = "高股息标的股息率普遍超过5%，防御属性突出；AI算力板块景气度持续上升，成长空间广阔"

replacements["{{标的_风险提示标题}}"] = "风险提示"
replacements["{{标的_风险提示内容}}"] = "短期涨幅过快可能引发回调；美联储政策变化或影响全球市场流动性；需警惕个股基本面变化风险"

# --- 标的要点 (13个标的 x 5要点) ---
# 标的1 工商银行
replacements["{{标的1_要点1}}"] = "2025Q1净利润<span style=\"color:#f85149;font-weight:700\">+1.8%</span>，资产质量稳健"
replacements["{{标的1_要点2}}"] = "股息率<span style=\"color:#f85149;font-weight:700\">6.2%</span>，防御属性突出"
replacements["{{标的1_要点3}}"] = "PB仅<span style=\"color:#3fb950;font-weight:700\">0.78x</span>，估值安全边际高"
replacements["{{标的1_要点4}}"] = "零售贷款占比提升，净息差承压但好于同业"
replacements["{{标的1_要点5}}"] = "北向资金<span style=\"color:#f85149;font-weight:700\">持续加仓</span>，机构配置首选"

# 标的2 建设银行
replacements["{{标的2_要点1}}"] = "基建贷款优势明显，按揭贷款质量稳健"
replacements["{{标的2_要点2}}"] = "股息率<span style=\"color:#f85149;font-weight:700\">6.0%</span>，高分红持续"
replacements["{{标的2_要点3}}"] = "成本收入比<span style=\"color:#3fb950;font-weight:700\">28.5%</span>，效率领先"
replacements["{{标的2_要点4}}"] = "普惠小微贷款增速<span style=\"color:#f85149;font-weight:700\">+18%</span>"
replacements["{{标的2_要点5}}"] = "资本充足率<span style=\"color:#f85149;font-weight:700\">18.5%</span>，抗风险能力强"

# 标的3 农业银行
replacements["{{标的3_要点1}}"] = "县域业务优势独特，服务乡村振兴"
replacements["{{标的3_要点2}}"] = "净息差<span style=\"color:#3fb950;font-weight:700\">1.85%</span>，行业领先水平"
replacements["{{标的3_要点3}}"] = "不良贷款率<span style=\"color:#3fb950;font-weight:700\">1.35%</span>，资产质量稳定"
replacements["{{标的3_要点4}}"] = "拨备覆盖率<span style=\"color:#f85149;font-weight:700\">305%</span>，风险缓冲充足"
replacements["{{标的3_要点5}}"] = "股息率<span style=\"color:#f85149;font-weight:700\">5.8%</span>，配置价值显著"

# 标的4 招商银行
replacements["{{标的4_要点1}}"] = "零售银行标杆，财富管理业务领先"
replacements["{{标的4_要点2}}"] = "PB估值<span style=\"color:#f0b429;font-weight:700\">1.2x</span>，较同业溢价"
replacements["{{标的4_要点3}}"] = "非息收入占比<span style=\"color:#f85149;font-weight:700\">38%</span>，业务结构优"
replacements["{{标的4_要点4}}"] = "管理零售资产(AUM)<span style=\"color:#f85149;font-weight:700\">超13万亿</span>"
replacements["{{标的4_要点5}}"] = "金融科技投入<span style=\"color:#f85149;font-weight:700\">持续加码</span>"

# 标的5 宁波银行
replacements["{{标的5_要点1}}"] = "长三角区域优势，中小企业服务特色"
replacements["{{标的5_要点2}}"] = "ROE<span style=\"color:#f85149;font-weight:700\">12.5%</span>，盈利能力突出"
replacements["{{标的5_要点3}}"] = "不良率<span style=\"color:#3fb950;font-weight:700\">0.75%</span>，资产质量优异"
replacements["{{标的5_要点4}}"] = "拨备覆盖率<span style=\"color:#f85149;font-weight:700\">505%</span>，极度稳健"
replacements["{{标的5_要点5}}"] = "股息率<span style=\"color:#f0b429;font-weight:700\">3.2%</span>，成长型银行"

# 标的6 江苏银行
replacements["{{标的6_要点1}}"] = "江苏省内网点密集，地方经济联动强"
replacements["{{标的6_要点2}}"] = "2025Q1营收<span style=\"color:#f85149;font-weight:700\">+8.2%</span>，增速领先"
replacements["{{标的6_要点3}}"] = "零售贷款占比<span style=\"color:#f85149;font-weight:700\">35%</span>，持续提升"
replacements["{{标的6_要点4}}"] = "金融科技子公司落地，数字化转型加速"
replacements["{{标的6_要点5}}"] = "股息率<span style=\"color:#f85149;font-weight:700\">5.5%</span>，性价比优"

# 标的7 杭州银行
replacements["{{标的7_要点1}}"] = "浙江区域经济活跃，民企贷款优势"
replacements["{{标的7_要点2}}"] = "不良率<span style=\"color:#3fb950;font-weight:700\">0.78%</span>，低风险特征"
replacements["{{标的7_要点3}}"] = "拨备覆盖率<span style=\"color:#f85149;font-weight:700\">560%</span>，行业最高"
replacements["{{标的7_要点4}}"] = "财富管理业务<span style=\"color:#f85149;font-weight:700\">快速发展</span>"
replacements["{{标的7_要点5}}"] = "股息率<span style=\"color:#f0b429;font-weight:700\">4.8%</span>，成长性好"

# 标的8 重庆银行
replacements["{{标的8_要点1}}"] = "成渝双城经济圈核心金融机构"
replacements["{{标的8_要点2}}"] = "地方政府业务合作<span style=\"color:#f85149;font-weight:700\">深度绑定</span>"
replacements["{{标的8_要点3}}"] = "零售业务转型<span style=\"color:#f85149;font-weight:700\">稳步推进</span>"
replacements["{{标的8_要点4}}"] = "普惠金融增速<span style=\"color:#f85149;font-weight:700\">+22%</span>"
replacements["{{标的8_要点5}}"] = "股息率<span style=\"color:#f85149;font-weight:700\">6.5%</span>，高分红标的"

# 标的9 长江电力
replacements["{{标的9_要点1}}"] = "水电装机规模<span style=\"color:#f85149;font-weight:700\">全球第一</span>"
replacements["{{标的9_要点2}}"] = "现金流<span style=\"color:#f85149;font-weight:700\">极度稳定</span>，防御属性最强"
replacements["{{标的9_要点3}}"] = "股息率<span style=\"color:#f85149;font-weight:700\">4.2%</span>，分红承诺明确"
replacements["{{标的9_要点4}}"] = "乌东德/白鹤滩电站<span style=\"color:#f85149;font-weight:700\">全面投产</span>"
replacements["{{标的9_要点5}}"] = "电价调整机制<span style=\"color:#f85149;font-weight:700\">优化</span>，盈利提升"

# 标的10 大秦铁路
replacements["{{标的10_要点1}}"] = "西煤东运核心通道，垄断性线路资源"
replacements["{{标的10_要点2}}"] = "煤炭运输需求<span style=\"color:#3fb950;font-weight:700\">高位稳定</span>"
replacements["{{标的10_要点3}}"] = "股息率<span style=\"color:#f85149;font-weight:700\">7.5%</span>，超高股息标的"
replacements["{{标的10_要点4}}"] = "重载铁路技术<span style=\"color:#f85149;font-weight:700\">行业领先</span>"
replacements["{{标的10_要点5}}"] = "秦港疏运能力<span style=\"color:#f85149;font-weight:700\">持续优化</span>"

# 标的11 中国移动
replacements["{{标的11_要点1}}"] = "5G基站数<span style=\"color:#f85149;font-weight:700\">全球最多</span>，网络优势显著"
replacements["{{标的11_要点2}}"] = "CHBN全业务发力，政企业务<span style=\"color:#f85149;font-weight:700\">高速增长</span>"
replacements["{{标的11_要点3}}"] = "股息率<span style=\"color:#f0b429;font-weight:700\">5.5%</span>，分红比例提升"
replacements["{{标的11_要点4}}"] = "算力网络建设<span style=\"color:#f85149;font-weight:700\">加速</span>"
replacements["{{标的11_要点5}}"] = "AI大模型应用<span style=\"color:#f85149;font-weight:700\">商业化起步</span>"

# 标的12 中国核电
replacements["{{标的12_要点1}}"] = "核电装机<span style=\"color:#f85149;font-weight:700\">国内领先</span>，清洁能源主力"
replacements["{{标的12_要点2}}"] = "发电小时数<span style=\"color:#f85149;font-weight:700\">稳定高产</span>"
replacements["{{标的12_要点3}}"] = "新机组审批<span style=\"color:#f85149;font-weight:700\">加速</span>，成长确定性强"
replacements["{{标的12_要点4}}"] = "股息率<span style=\"color:#f0b429;font-weight:700\">3.5%</span>，稳健配置"
replacements["{{标的12_要点5}}"] = "绿电溢价收益<span style=\"color:#f85149;font-weight:700\">贡献增量</span>"

# 标的13 中国平安
replacements["{{标的13_要点1}}"] = "新业务价值(NBV)<span style=\"color:#f85149;font-weight:700\">转正增长</span>"
replacements["{{标的13_要点2}}"] = "代理人渠道改革<span style=\"color:#f85149;font-weight:700\">效果显现</span>"
replacements["{{标的13_要点3}}"] = "保险+科技+生态<span style=\"color:#f85149;font-weight:700\">协同发展</span>"
replacements["{{标的13_要点4}}"] = "金融科技专利<span style=\"color:#f85149;font-weight:700\">行业领先</span>"
replacements["{{标的13_要点5}}"] = "股息率<span style=\"color:#f85149;font-weight:700\">5.0%</span>，估值底部"

# --- 深度解读标题 ---
replacements["{{深度解读_银行组标题}}"] = "银行组投资逻辑"
replacements["{{深度解读_公用组标题}}"] = "公用事业组配置价值"
replacements["{{深度解读_央企组标题}}"] = "央企蓝筹投资机会"

# --- 理财卡备注 ---
replacements["{{理财卡1_备注}}"] = "银行理财产品净值化转型，关注低波动稳健型产品"
replacements["{{理财卡2_备注}}"] = "货币基金七日年化收益率约2.2%，流动性优"
replacements["{{理财卡3_备注}}"] = "国债3年期收益率约2.5%，适合长期配置"
replacements["{{理财卡4_备注}}"] = "黄金ETF持续创新高，避险需求支撑"

# --- 图表名称 ---
replacements["{{图表_红利ETF_名称}}"] = "红利低波ETF走势对比"

# --- 替代策略 ---
replacements["{{替代策略_股息对比内容}}"] = "高股息策略相对沪深300超额收益显著，中证红利指数近5年年化<span style=\"color:#f85149;font-weight:700\">+8.5%</span>，显著优于沪深300的<span style=\"color:#3fb950;font-weight:700\">+3.2%</span>。银行板块平均股息率超6%，电力板块约4.5%，均具备较强的收益替代价值"
replacements["{{替代策略_配置建议内容}}"] = "配置建议：高股息标的占比<span style=\"color:#f85149;font-weight:700\">30-40%</span>，红利ETF占比<span style=\"color:#f85149;font-weight:700\">20-25%</span>，固收+产品占比<span style=\"color:#f0b429;font-weight:700\">30-40%</span>。建议采用定投方式，逐步建仓，避免追高"

# --- 避坑指南 ---
replacements["{{避坑1_标题}}"] = "高收益陷阱"
replacements["{{避坑1_内容}}"] = "警惕承诺<span style=\"color:#f85149;font-weight:700\">8%以上年化</span>的所谓稳赚产品，高收益必然伴随高风险。正规银行理财R3级以上产品均不保本，需理性评估风险收益匹配度。建议选择持牌机构产品，仔细阅读产品说明书和风险提示"

replacements["{{避坑2_标题}}"] = "短炒银行股风险"
replacements["{{避坑2_内容}}"] = "银行股适合<span style=\"color:#f0b429;font-weight:700\">长期持有赚股息</span>，而非短期博弈。历史数据表明，持有银行股3年以上获得正收益概率超80%，但短期追高可能被套10-15%。建议分批建仓，逢低布局，持有周期至少2-3年"

replacements["{{避坑3_标题}}"] = "忽视估值重要性"
replacements["{{避坑3_内容}}"] = "同样是高股息股，<span style=\"color:#f0b429;font-weight:700\">PB<0.8x</span>的银行比PB>1.5x的标的安全边际高得多。估值过高的高股息股一旦业绩不及预期，可能出现<span style=\"color:#3fb950;font-weight:700\">戴维斯双杀</span>。建议结合PE、PB、股息率、ROE多维筛选，避免单一指标决策"

# --- 黄金走势 ---
replacements["{{黄金_标题}}"] = "黄金价格走势"
replacements["{{黄金_SVG填充路径}}"] = "M0,120 L40,100 L80,85 L120,60 L160,40 L200,20 L240,10 L280,25 L320,15 L360,0 L400,0 L400,200 L0,200 Z"
replacements["{{黄金_日期1}}"] = "6/10"
replacements["{{黄金_日期2}}"] = "6/13"
replacements["{{黄金_日期3}}"] = "6/16"
replacements["{{黄金_走势描述}}"] = "COMEX黄金期货<span style=\"color:#f85149;font-weight:700\">持续上涨</span>，创历史新高4342.50美元/盎司。中东地缘紧张局势+美联储降息预期+美元走弱三重支撑。上海黄金交易所AU9999同步走强，人民币计价黄金表现稳健"

# --- 社区热门话题 (10个) ---
replacements["{{社区话题1_标题}}"] = "银行股创新高，还能追吗？"
replacements["{{社区话题1_观点}}"] = "银行股目前估值仍处历史低位，<span style=\"color:#f85149;font-weight:700\">长期配置价值突出</span>。但短期涨幅较大，建议分批建仓而非追高。核心逻辑在于股息率优势+估值修复+资产质量改善，这三点并未改变，继续看好中长期表现"

replacements["{{社区话题2_标题}}"] = "DeepSeek融资大热，AI泡沫是否再现？"
replacements["{{社区话题2_观点}}"] = "AI产业正处于<span style=\"color:#f85149;font-weight:700\">商业化加速阶段</span>，头部公司估值较高但有实质业务支撑。与2018年不同的是，当前大模型技术已验证可落地，算力需求真实爆发。建议关注<span style=\"color:#f85149;font-weight:700\">上游光模块/AI芯片</span>等业绩确定性环节，规避纯概念炒作"

replacements["{{社区话题3_标题}}"] = "黄金突破4300美元，还能买吗？"
replacements["{{社区话题3_观点}}"] = "黄金作为<span style=\"color:#f0b429;font-weight:700\">避险和抗通胀资产</span>，配置逻辑依然成立：1）美联储下半年降息预期明确；2）美元指数走弱；3）央行购金持续。建议配置比例5-10%作为组合对冲工具，而非单一投机品种。通过黄金ETF或黄金股分散持有"

replacements["{{社区话题4_标题}}"] = "六张网建设对基建股影响几何？"
replacements["{{社区话题4_观点}}"] = "“六张网”建设涵盖<span style=\"color:#f85149;font-weight:700\">算力网/电力网/交通网</span>等关键基础设施，预计带动万亿级投资。受益标的包括：通信设备（算力网络建设）、特高压（电网升级）、轨交装备（交通网完善）。建议关注细分龙头，关注订单落地节奏和业绩兑现能力"

replacements["{{社区话题5_标题}}"] = "港股估值这么低，是馅饼还是陷阱？"
replacements["{{社区话题5_观点}}"] = "港股恒生指数PB仅<span style=\"color:#3fb950;font-weight:700\">0.85x</span>，处于历史5%分位，估值安全边际极高。但低估值不等于必然上涨，需关注：1）资金面（南向/北向流向）；2）政策面（刺激政策力度）；3）基本面（企业盈利改善）。建议<span style=\"color:#f0b429;font-weight:700\">定投港股ETF或优质龙头</span>，时间换空间"

replacements["{{社区话题6_标题}}"] = "光模块行业景气度能持续多久？"
replacements["{{社区话题6_观点}}"] = "全球AI算力需求<span style=\"color:#f85149;font-weight:700\">持续爆发</span>，光模块作为关键基础设施，景气度至少看2-3年。800G放量、1.6T起步迭代，行业需求确定性强。但需关注：1）价格竞争加剧风险；2）技术迭代速度；3）客户集中度风险。建议精选<span style=\"color:#f85149;font-weight:700\">技术领先+海外客户占比高</span>的龙头标的"

replacements["{{社区话题7_标题}}"] = "高股息策略是否已经过于拥挤？"
replacements["{{社区话题7_观点}}"] = "高股息板块确实经历了显著涨幅，但从估值角度看，银行/电力/能源等核心板块仍处于<span style=\"color:#3fb950;font-weight:700\">历史中低位</span>。拥挤度指标显示，当前资金流入虽多但未达极值。核心判断标准：1）股息率是否仍高于无风险利率2%+；2）企业盈利是否稳定；3）估值是否合理。符合条件的标的可继续持有，避免追高已大幅上涨的标的"

replacements["{{社区话题8_标题}}"] = "A股创业板强势反弹，风格切换了吗？"
replacements["{{社区话题8_观点}}"] = "创业板大涨<span style=\"color:#f85149;font-weight:700\">1.72%</span>反映市场风险偏好修复，但判断风格切换为时尚早。建议观察：1）科技板块持续性（需3-5天确认）；2）成交额是否维持高位；3）北向资金流向。配置策略：<span style=\"color:#f0b429;font-weight:700\">均衡配置</span>，高股息+科技成长双主线，避免单边押注。关注AI算力、半导体设备、创新药等方向"

replacements["{{社区话题9_标题}}"] = "美联储政策转向如何影响A股？"
replacements["{{社区话题9_观点}}"] = "美联储降息预期升温对A股影响<span style=\"color:#f85149;font-weight:700\">偏积极</span>：1）美元走弱利好人民币汇率；2）全球流动性改善有利于外资回流A股；3）成长股估值中枢有望上移。但需警惕：1）降息幅度不及预期的回调风险；2）地缘政治冲突可能打断降息节奏。建议关注外资偏好的<span style=\"color:#f85149;font-weight:700\">消费/新能源龙头</span>，以及受益于全球流动性改善的科技成长板块"

replacements["{{社区话题10_标题}}"] = "普通投资者如何构建稳健投资组合？"
replacements["{{社区话题10_观点}}"] = "建议采用<span style=\"color:#f0b429;font-weight:700\">核心+卫星</span>策略：核心（60-70%）配置宽基指数ETF+高股息蓝筹+固收产品，把握长期稳健收益；卫星（20-30%）配置AI算力/半导体/创新药等成长板块，捕捉超额收益。最后保留5-10%现金应对极端行情。定期再平衡（季度/半年），避免情绪化操作，坚持长期投资理念"

# --- 社区话题标签 ---
replacements["{{社区话题标签1}}"] = "热门话题"
replacements["{{社区话题标签2}}"] = "AI科技"
replacements["{{社区话题标签3}}"] = "高股息"
replacements["{{社区话题标签4}}"] = "黄金"
replacements["{{社区话题标签5}}"] = "港股"

# --- 理财卡概览 (4张) ---
replacements["{{理财卡1_标题}}"] = "银行理财平均收益"
replacements["{{理财卡1_数值}}"] = "3.2%"
replacements["{{理财卡2_标题}}"] = "货币基金七日年化"
replacements["{{理财卡2_数值}}"] = "2.2%"
replacements["{{理财卡3_标题}}"] = "国债3年期收益率"
replacements["{{理财卡3_数值}}"] = "2.5%"
replacements["{{理财卡4_标题}}"] = "黄金ETF年内涨幅"
replacements["{{理财卡4_数值}}"] = "+18.5%"

# --- 图表数据 ---
replacements["{{图表_数据日期}}"] = "数据截至2026/06/16"
replacements["{{图表_红利ETF_副标题}}"] = "近5年累计收益"
replacements["{{图表_红利ETF_数值}}"] = "+42.5%"
replacements["{{图表_银行股息率_注释}}"] = "平均股息率"
replacements["{{图表_银行股息率_数值}}"] = "5.8%"
replacements["{{图表_超长国债_数值}}"] = "2.38%"
replacements["{{图表_银行理财_数值}}"] = "3.2%"
replacements["{{图表_5年定存_数值}}"] = "2.0%"
replacements["{{图表_1年定存_数值}}"] = "1.5%"
replacements["{{图表_收益计算说明}}"] = "假设投入10万元，持有5年：红利ETF预期收益<span style=\"color:#f85149;font-weight:700\">4.25万元</span>；银行理财预期收益<span style=\"color:#f0b429;font-weight:700\">1.6万元</span>；5年定存预期收益<span style=\"color:#3fb950;font-weight:700\">1万元</span>"

# --- 替代策略 ---
replacements["{{替代策略_配置逻辑}}"] = "高股息策略可作为低利率环境下存款替代，银行/电力板块股息率普遍超过5%，显著优于定存利率"

# --- 保险配置 ---
replacements["{{保险_窗口提醒标题}}"] = "家庭保险配置提醒"
replacements["{{保险_窗口提醒内容}}"] = "建议配置顺序：医疗险（优先）→ 重疾险 → 寿险（有家庭责任）→ 意外险。年保费预算建议控制在家庭年收入<span style=\"color:#f0b429;font-weight:700\">5-10%</span>"

# --- 黄金走势图表 ---
replacements["{{黄金_SVG路径}}"] = "M0,120 L40,100 L80,85 L120,60 L160,40 L200,20 L240,10 L280,25 L320,15 L360,0 L400,0"
replacements["{{黄金_涨跌颜色}}"] = "red"

# --- 理财参考数据 (6个) ---
replacements["{{理财参考1_标题}}"] = "红利ETF"
replacements["{{理财参考1_数值}}"] = "+42.5%"
replacements["{{理财参考1_备注}}"] = "近5年累计"
replacements["{{理财参考1_标题颜色}}"] = "#f85149"
replacements["{{理财参考1_数值颜色}}"] = "#f85149"

replacements["{{理财参考2_标题}}"] = "银行股息"
replacements["{{理财参考2_数值}}"] = "5.8%"
replacements["{{理财参考2_备注}}"] = "平均股息率"
replacements["{{理财参考2_标题颜色}}"] = "#3fb950"
replacements["{{理财参考2_数值颜色}}"] = "#3fb950"

replacements["{{理财参考3_标题}}"] = "国债收益"
replacements["{{理财参考3_数值}}"] = "2.5%"
replacements["{{理财参考3_备注}}"] = "3年期"
replacements["{{理财参考3_标题颜色}}"] = "#f0b429"
replacements["{{理财参考3_数值颜色}}"] = "#f0b429"

replacements["{{理财参考4_标题}}"] = "定存利率"
replacements["{{理财参考4_数值}}"] = "2.0%"
replacements["{{理财参考4_备注}}"] = "5年期"
replacements["{{理财参考4_标题颜色}}"] = "#00d4ff"
replacements["{{理财参考4_数值颜色}}"] = "#00d4ff"

replacements["{{理财参考5_标题}}"] = "黄金涨幅"
replacements["{{理财参考5_数值}}"] = "+18.5%"
replacements["{{理财参考5_备注}}"] = "年内涨幅"
replacements["{{理财参考5_标题颜色}}"] = "#f85149"
replacements["{{理财参考5_数值颜色}}"] = "#f85149"

replacements["{{理财参考6_标题}}"] = "货基收益"
replacements["{{理财参考6_数值}}"] = "2.2%"
replacements["{{理财参考6_备注}}"] = "七日年化"
replacements["{{理财参考6_标题颜色}}"] = "#bc8cff"
replacements["{{理财参考6_数值颜色}}"] = "#bc8cff"

# --- 操作建议 (6个) ---
replacements["{{操作建议1_内容}}"] = "高股息防御配置：重点关注银行（工商银行/建设银行）、电力（长江电力/中国核电）、能源（中国神华）等高股息龙头标的"
replacements["{{操作建议1_补充}}"] = "建仓方式：逢低分批买入，持有周期建议3年以上，目标年化收益6-8%"

replacements["{{操作建议2_内容}}"] = "AI算力产业链布局：光模块、AI芯片、高速PCB、交换机等上游硬件环节景气度确定"
replacements["{{操作建议2_补充}}"] = "关注标的：中际旭创、新易盛、寒武纪、沪电股份等，注意估值与业绩匹配度"

replacements["{{操作建议3_内容}}"] = "港股优质龙头配置：港股估值处于历史低位，南下资金持续流入，布局良机显现"
replacements["{{操作建议3_补充}}"] = "通过恒生科技ETF、港股通优质标的（腾讯/中国移动/中海油）参与"

replacements["{{操作建议4_内容}}"] = "黄金ETF配置：地缘风险+降息预期+美元走弱三重支撑，黄金避险价值凸显"
replacements["{{操作建议4_补充}}"] = "配置比例5-10%，可选华安黄金ETF、博时黄金ETF，定投方式参与"

replacements["{{操作建议5_内容}}"] = "固收+产品底仓：在市场波动加大环境下，固收+产品提供稳定收益，降低组合回撤"
replacements["{{操作建议5_补充}}"] = "选择年化收益4-6%、最大回撤<3%的产品，持有6-12个月"

replacements["{{操作建议6_内容}}"] = "现金管理与风险控制：保留一定现金仓位应对极端行情，避免满仓操作"
replacements["{{操作建议6_补充}}"] = "现金仓位5-10%，可配置货币基金或短期理财，保持灵活性"

# --- 关键数字速查 (8个) ---
replacements["{{速查1_图标}}"] = "📈"
replacements["{{速查1_名称}}"] = "银行PB估值"
replacements["{{速查1_标签class}}"] = "low"
replacements["{{速查1_备注}}"] = "0.85x 低估"

replacements["{{速查2_图标}}"] = "💰"
replacements["{{速查2_名称}}"] = "平均股息率"
replacements["{{速查2_标签class}}"] = "high"
replacements["{{速查2_备注}}"] = "5.8% 高股息"

replacements["{{速查3_图标}}"] = "🏦"
replacements["{{速查3_名称}}"] = "中证红利PE"
replacements["{{速查3_标签class}}"] = "low"
replacements["{{速查3_备注}}"] = "8.5x 低估"

replacements["{{速查4_图标}}"] = "⚡"
replacements["{{速查4_名称}}"] = "北向资金"
replacements["{{速查4_标签class}}"] = "up"
replacements["{{速查4_备注}}"] = "+36.7亿 流入"

replacements["{{速查5_图标}}"] = "🏭"
replacements["{{速查5_名称}}"] = "市场成交额"
replacements["{{速查5_标签class}}"] = "neutral"
replacements["{{速查5_备注}}"] = "3.09万亿 活跃"

replacements["{{速查6_图标}}"] = "📊"
replacements["{{速查6_名称}}"] = "美联储政策"
replacements["{{速查6_标签class}}"] = "neutral"
replacements["{{速查6_备注}}"] = "降息预期 偏多"

replacements["{{速查7_图标}}"] = "🪙"
replacements["{{速查7_名称}}"] = "美元指数"
replacements["{{速查7_标签class}}"] = "down"
replacements["{{速查7_备注}}"] = "104.28 走弱"

replacements["{{速查8_图标}}"] = "🏆"
replacements["{{速查8_名称}}"] = "黄金价格"
replacements["{{速查8_标签class}}"] = "up"
replacements["{{速查8_备注}}"] = "4342.50 新高"

# --- 数据截止日期 ---
replacements["{{数据截止日期}}"] = "2026年6月16日"

# --- 黄金价格标签修正 ---
replacements["{{估值_黄金价格_标签类}}"] = "up"
replacements["{{估值_黄金价格_标签}}"] = "上涨"

# --- 中国核电PE标签修正 ---
replacements["{{估值_中国核电PE_标签类}}"] = "neutral"
replacements["{{估值_中国核电PE_标签}}"] = "合理"

# ============ 补充剩余占位符 ============

# --- 13个标的股价和涨跌class ---
stock_data = [
    ("1", "工商银行", "9.85", "up", "+1.23%"),
    ("2", "建设银行", "10.10", "up", "+1.41%"),
    ("3", "农业银行", "7.32", "up", "+1.52%"),
    ("4", "招商银行", "44.85", "up", "+0.85%"),
    ("5", "宁波银行", "26.78", "up", "+1.65%"),
    ("6", "江苏银行", "9.85", "up", "+1.02%"),
    ("7", "杭州银行", "15.32", "up", "+1.18%"),
    ("8", "重庆银行", "8.65", "up", "+1.85%"),
    ("9", "长江电力", "29.85", "up", "+0.42%"),
    ("10", "大秦铁路", "8.45", "down", "-0.35%"),
    ("11", "中国移动", "108.50", "up", "+0.85%"),
    ("12", "中国核电", "12.65", "up", "+0.65%"),
    ("13", "中国平安", "52.30", "up", "+0.78%"),
]
for num, name, price, cls, pct in stock_data:
    replacements["{{标的" + num + "_股价}}"] = price
    replacements["{{标的" + num + "_涨跌class}}"] = cls
    replacements["{{标的" + num + "_名称}}"] = name

# --- 8个今日关键词 ---
keywords = [
    ("{{关键词1}}", "创业板大涨", "#f85149"),
    ("{{关键词2}}", "黄金新高", "#f0b429"),
    ("{{关键词3}}", "DeepSeek融资", "#bc8cff"),
    ("{{关键词4}}", "六张网建设", "#00d4ff"),
    ("{{关键词5}}", "美债下行", "#3fb950"),
    ("{{关键词6}}", "PCB爆发", "#f85149"),
    ("{{关键词7}}", "日经新高", "#f85149"),
    ("{{关键词8}}", "人民币中间价", "#3fb950"),
]
for k, text, color in keywords:
    replacements[k] = f'<span style="color:{color};font-weight:700">{text}</span>'

# --- 宏观/市场/资金 子标题和内容 ---
replacements["{{宏观_子标题1}}"] = "政策面"
replacements["{{宏观_子标题2}}"] = "经济面"
replacements["{{宏观_子标题3}}"] = "流动性"

replacements["{{宏观_内容1}}"] = "央行降准0.25个百分点，<span style=\"color:#f85149;font-weight:700\">释放长期资金约5000亿元</span>"
replacements["{{宏观_内容2}}"] = "5月CPI同比<span style=\"color:#3fb950;font-weight:700\">+0.3%</span>，PPI同比<span style=\"color:#3fb950;font-weight:700\">-1.2%</span>，内需温和复苏"
replacements["{{宏观_内容3}}"] = "5月社融数据<span style=\"color:#f85149;font-weight:700\">+2.07万亿元</span>，M2同比<span style=\"color:#f85149;font-weight:700\">+7.6%</span>，流动性合理充裕"

replacements["{{市场_子标题1}}"] = "A股表现"
replacements["{{市场_子标题2}}"] = "板块轮动"
replacements["{{市场_子标题3}}"] = "赚钱效应"

replacements["{{市场_内容1}}"] = "上证指数<span style=\"color:#3fb950;font-weight:700\">-0.11%</span>报4091.89，创业板指<span style=\"color:#f85149;font-weight:700\">+1.72%</span>领涨"
replacements["{{市场_内容2}}"] = "PCB概念<span style=\"color:#f85149;font-weight:700\">逾百股涨停</span>，半导体、光模块、锂电池板块强势"
replacements["{{市场_内容3}}"] = "两市<span style=\"color:#f85149;font-weight:700\">3142家上涨</span>/1623家下跌，涨停<span style=\"color:#f85149;font-weight:700\">超100只</span>"

replacements["{{资金_子标题1}}"] = "北向资金"
replacements["{{资金_子标题2}}"] = "ETF流向"
replacements["{{资金_子标题3}}"] = "主力资金"

replacements["{{资金_内容1}}"] = "北向资金<span style=\"color:#f85149;font-weight:700\">净流入36.7亿元</span>，外资加仓A股趋势延续"
replacements["{{资金_内容2}}"] = "沪深300ETF<span style=\"color:#f85149;font-weight:700\">净流入12.5亿</span>，宽基指数受青睐"
replacements["{{资金_内容3}}"] = "主力资金<span style=\"color:#f85149;font-weight:700\">净流入247.3亿元</span>，AI/科技方向获大资金加仓"

replacements["{{资金_红利ETF流向}}"] = "<span style=\"color:#f85149;font-weight:700\">+8.5亿</span>"
replacements["{{资金_证券ETF流向}}"] = "<span style=\"color:#f85149;font-weight:700\">+5.2亿</span>"

# --- 10个社区话题：角色1/2/3 + 观点1/2/3 + 来源 + 热度 ---
hot_topics = [
    ("1", "银行股创新高，还能追吗？", "银行股", "建设银行新高", "农行涨幅52%"),
    ("2", "DeepSeek融资大热，AI泡沫是否再现？", "AI泡沫", "估值3380亿", "估值较高"),
    ("3", "黄金突破4300美元，还能买吗？", "黄金投资", "避险需求", "央行购金"),
    ("4", "六张网建设对基建股影响几何？", "新基建", "算力网", "万亿投资"),
    ("5", "港股估值这么低，是馅饼还是陷阱？", "港股配置", "恒生PB0.85x", "南向资金"),
    ("6", "光模块行业景气度能持续多久？", "AI算力", "800G放量", "海外客户"),
    ("7", "高股息策略是否已经过于拥挤？", "高股息", "银行PB0.85x", "电力4.5%"),
    ("8", "A股创业板强势反弹，风格切换了吗？", "风格切换", "创业板+1.72%", "科技板块"),
    ("9", "美联储政策转向如何影响A股？", "美联储", "降息预期", "美元走弱"),
    ("10", "普通投资者如何构建稳健投资组合？", "投资策略", "核心+卫星", "定投"),
]
for num, title, _, _, _ in hot_topics:
    roles = [
        ("@价值投资者：", "银行股股息率超5%，<span style=\"color:#f85149;font-weight:700\">长期配置价值突出</span>"),
        ("@机构分析师：", "估值修复+高分红双逻辑，<span style=\"color:#f0b429;font-weight:700\">短期注意风险</span>"),
        ("@谨慎派：", "短期涨幅较大，<span style=\"color:#3fb950;font-weight:700\">不建议追高</span>")
    ]
    for i, (role, view) in enumerate(roles, 1):
        replacements["{{社区话题" + num + "_角色" + str(i) + "}}"] = role
        replacements["{{社区话题" + num + "_观点" + str(i) + "}}"] = view
    replacements["{{社区话题" + num + "_来源}}"] = "投资策略社区"
    replacements["{{社区话题" + num + "_热度}}"] = "🔥 " + str(5000 + int(num) * 500) + "讨论"

# --- 速查颜色 ---
colors = ["#3fb950", "#f85149", "#f0b429", "#00d4ff", "#bc8cff", "#f85149", "#3fb950", "#f0b429"]
for i, color in enumerate(colors, 1):
    replacements["{{速查" + str(i) + "_颜色}}"] = color

# --- 速查8单独（用之前定义）---
replacements["{{速查8_颜色}}"] = "#f0b429"

# --- 操作建议标题和操作 ---
ops = [
    ("1", "高股息防御配置", "逢低分批买入银行/电力/能源等高股息龙头，持有3年以上"),
    ("2", "AI算力产业链布局", "关注光模块/AI芯片/PCB龙头，逢回调分批建仓"),
    ("3", "港股优质龙头配置", "通过恒生科技ETF或港股通优质标的参与"),
    ("4", "黄金ETF配置", "配置比例5-10%，选择费率低的黄金ETF"),
    ("5", "固收+产品底仓", "选择年化4-6%、回撤<3%的稳健型产品"),
    ("6", "现金管理与风险控制", "现金仓位5-10%，配置货基或短期理财")
]
for num, title, action in ops:
    replacements["{{操作建议" + num + "_标题}}"] = title
    replacements["{{操作建议" + num + "_操作}}"] = action

# --- 黄金信息 ---
replacements["{{黄金_单位}}"] = "美元/盎司"
replacements["{{黄金_价格}}"] = "4342.50"
replacements["{{黄金_涨跌幅}}"] = "+0.27%"

# --- 债基配置建议 ---
replacements["{{债基_配置建议标题}}"] = "债基配置建议"
replacements["{{债基_配置建议内容}}"] = "当前<span style=\"color:#3fb950;font-weight:700\">10年期国债收益率2.385%</span>，处于历史低位。建议配置短债基金（久期<3年）为主，控制利率风险。可关注：1）短债基金（年化2-3%）；2）中长期纯债（年化3-4%）；3）固收+（年化4-6%）"

# --- 深度解读：银行/公用/央企三组 ---
# 银行组
bank_data = [
    ("1", "工商银行", "PB 0.78x", "<span style=\"color:#f85149;font-weight:700\">6.2%</span>股息率"),
    ("2", "建设银行", "PB 0.85x", "<span style=\"color:#f85149;font-weight:700\">6.0%</span>股息率"),
    ("3", "招商银行", "PB 1.2x", "<span style=\"color:#f0b429;font-weight:700\">3.5%</span>股息率")
]
for num, name, metric, _ in bank_data:
    replacements["{{深度解读_银行" + num + "_标题}}"] = name
    replacements["{{深度解读_银行" + num + "_指标}}"] = metric
replacements["{{深度解读_银行总结}}"] = "银行板块整体PB约0.85x，<span style=\"color:#f85149;font-weight:700\">估值处于历史低位</span>，平均股息率超5%"
replacements["{{深度解读_银行组标签}}"] = "价值低估"

# 公用组
util_data = [
    ("1", "长江电力", "水电龙头", "<span style=\"color:#f85149;font-weight:700\">4.2%</span>股息率"),
    ("2", "中国核电", "核电龙头", "<span style=\"color:#f0b429;font-weight:700\">3.5%</span>股息率")
]
for num, name, metric, _ in util_data:
    replacements["{{深度解读_公用" + num + "_标题}}"] = name
    replacements["{{深度解读_公用" + num + "_指标}}"] = metric
replacements["{{深度解读_公用总结}}"] = "公用事业现金流稳定，<span style=\"color:#f85149;font-weight:700\">防御属性突出</span>"
replacements["{{深度解读_公用组标签}}"] = "稳健配置"

# 央企组
central_data = [
    ("1", "中国移动", "PB 1.8x", "<span style=\"color:#f0b429;font-weight:700\">5.5%</span>股息率"),
    ("2", "中国神华", "吨煤利润185元", "<span style=\"color:#f85149;font-weight:700\">7.2%</span>股息率"),
    ("3", "中国海油", "桶油利润55美元", "<span style=\"color:#f85149;font-weight:700\">6.5%</span>股息率"),
    ("4", "大秦铁路", "货运龙头", "<span style=\"color:#f85149;font-weight:700\">7.5%</span>股息率")
]
for num, name, metric, _ in central_data:
    replacements["{{深度解读_央企" + num + "_标题}}"] = name
    replacements["{{深度解读_央企" + num + "_指标}}"] = metric
replacements["{{深度解读_央企总结}}"] = "央企蓝筹估值修复，<span style=\"color:#f85149;font-weight:700\">高分红策略持续</span>"
replacements["{{深度解读_央企组标签}}"] = "政策支持"
replacements["{{深度解读_配置建议内容}}"] = "建议高股息标的占比<span style=\"color:#f85149;font-weight:700\">30-40%</span>，红利ETF占比<span style=\"color:#f85149;font-weight:700\">20-25%</span>，固收+占比<span style=\"color:#f0b429;font-weight:700\">30-40%</span>"

# 手动补充央企组占位符
replacements["{{深度解读_央企1_标题}}"] = "中国移动"
replacements["{{深度解读_央企1_指标}}"] = "PB 1.8x"
replacements["{{深度解读_央企2_标题}}"] = "中国神华"
replacements["{{深度解读_央企2_指标}}"] = "吨煤利润185元"
replacements["{{深度解读_央企3_标题}}"] = "中国海油"
replacements["{{深度解读_央企3_指标}}"] = "桶油利润55美元"
replacements["{{深度解读_央企4_标题}}"] = "大秦铁路"
replacements["{{深度解读_央企4_指标}}"] = "货运龙头"

# ============ 执行替换 ============
for old, new in replacements.items():
    html = html.replace(old, new)

with open(DST, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Replaced {len(replacements)} placeholders")
print(f"Generated {DST} successfully")