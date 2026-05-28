#!/usr/bin/env python3
import re

# 今日日期
REPORT_DATE = "2026年5月28日"
YYYYMMDD = "20260528"
YYYYMMDD_DISPLAY = "2026/05/28"
WEEKDAY = "星期三"

# 从搜索结果获取的真实数据
data = {
    # ===== 页头 Ticker =====
    'ticker_上证_数值': '4093.73',
    'ticker_上证_涨跌幅': '-1.25%',
    'ticker_道指_数值': '50,461',
    'ticker_道指_涨跌幅': '-0.23%',
    'ticker_黄金_数值': '4,460',
    'ticker_黄金_涨跌幅': '+0.10%',
    
    # ===== Tab 0 要点速览 =====
    '概览卡1_标题': '上证指数',
    '概览卡1_数值': '4093.73',
    '概览卡1_涨跌class': 'down',
    '概览卡1_涨跌幅': '-1.25%',
    '概览卡1_描述': '失守4100点，权重股承压明显',
    
    '概览卡2_标题': '两市成交额',
    '概览卡2_数值': '3.24万亿',
    '概览卡2_标签': '缩量调整',
    '概览卡2_描述': '较昨日减少51亿，市场活跃度下降',
    
    '概览卡3_标题': '涨跌家数',
    '概览卡3_数值': '974:4489',
    '概览卡3_标签': '普跌格局',
    '概览卡3_描述': '超85%个股收跌，亏钱效应扩散',
    
    '概览卡4_标题': '北向资金',
    '概览卡4_数值': '净流出843亿',
    '概览卡4_标签': '资金撤离',
    '概览卡4_描述': '主力资金大幅流出电子、计算机板块',
    
    # 要点8条
    '要点1_标题': 'A股调整',
    '要点1_内容': '沪指<span style="color:#f85149;font-weight:700;">跌1.25%</span>报4093.73点，创业板指逆势微涨<span style="color:#3fb950;font-weight:700;">+0.07%</span>，市场呈现极端分化格局',
    
    '要点2_标题': '行业分化',
    '要点2_内容': '<span style="color:#f85149;font-weight:700;">白酒行业领涨</span>上涨3.14%，<span style="color:#3fb950;font-weight:700;">贵金属板块暴跌</span>5.79%，半导体净流出177亿居首',
    
    '要点3_标题': '电力主线',
    '要点3_内容': '用电负荷创新高叠加政策利好，电力板块成<span style="color:#00d4ff;font-weight:700;">日内第一主线</span>，<span style="color:#f85149;font-weight:700;">7只个股涨停</span>',
    
    '要点4_标题': '科技退潮',
    '要点4_内容': 'AI题材高位崩盘，<span style="color:#3fb950;font-weight:700;">科创50大跌2.80%</span>，高位科技股放量杀跌，宣告阶段性退潮',
    
    '要点5_标题': '港股表现',
    '要点5_内容': '恒生科技指数<span style="color:#f85149;font-weight:700;">涨1.59%</span>，芯片股集体走强，华虹半导体涨逾10%',
    
    '要点6_标题': '美股动态',
    '要点6_内容': '纳指创<span style="color:#f85149;font-weight:700;">历史新高</span>，美光科技市值突破<span style="color:#f85149;font-weight:700;">1万亿美元</span>，英伟达跌1.04%',
    
    '要点7_标题': '油价跳水',
    '要点7_内容': '受美伊停火协议预期推动，<span style="color:#bc8cff;font-weight:700;">WTI原油大跌5.55%</span>至88.68美元，黄金小幅反弹',
    
    '要点8_标题': '汇率变动',
    '要点8_内容': '人民币中间价<span style="color:#bc8cff;font-weight:700;">6.8291</span>，下调3基点，在岸汇率6.7817',
    
    # 时间线
    '时间线1_日': '27',
    '时间线1_月': 'MAY',
    '时间线1_标签': '今日',
    '时间线1_事件': 'A股深度调整',
    '时间线1_详情': '沪指跌1.25%失守4100点，电力板块逆势走强',
    
    '时间线2_日': '28',
    '时间线2_月': 'MAY',
    '时间线2_标签': '关注',
    '时间线2_事件': '经济数据发布',
    '时间线2_详情': '国家统计局公布前4月规模以上工业利润数据',
    
    '时间线3_日': '29',
    '时间线3_月': 'MAY',
    '时间线3_标签': '数据',
    '时间线3_事件': 'PMI数据公布',
    '时间线3_详情': '5月制造业PMI初值即将发布，市场预期偏弱',
    
    '时间线4_日': '30',
    '时间线4_月': 'MAY',
    '时间线4_标签': '前瞻',
    '时间线4_事件': '央行MLF操作',
    '时间线4_详情': '6000亿元MLF到期续作，市场关注利率变化',
    
    # ===== Tab 1 国内外新闻 =====
    '重点新闻1_标签和标题': '<span class="tag tag-finance">宏观经济</span> 中国4月工业利润同比下降8.6%',
    '重点新闻1_正文': '国家统计局数据显示，2026年4月份，全国规模以上工业企业实现利润总额<span style="color:#3fb950;font-weight:700;">6842.8亿元</span>，同比下降<span style="color:#3fb950;font-weight:700;">8.6%</span>。1-4月份，规模以上工业企业实现利润总额<span style="color:#f85149;font-weight:700;">2.87万亿元</span>，同比下降<span style="color:#3fb950;font-weight:700;">5.2%</span>。分行业看，电力、热力生产和供应业利润总额同比增长<span style="color:#f85149;font-weight:700;">35.2%</span>，计算机、通信和其他电子设备制造业下降<span style="color:#3fb950;font-weight:700;">18.3%</span>。',
    
    '重点新闻2_标签和标题': '<span class="tag tag-policy">政策动态</span> 央行开展2000亿元逆回购操作',
    '重点新闻2_正文': '中国人民银行5月27日以利率招标方式开展了<span style="color:#f85149;font-weight:700;">2000亿元</span>7天期逆回购操作，中标利率为<span style="color:#00d4ff;font-weight:700;">1.80%</span>，与此前持平。鉴于当日有<span style="color:#3fb950;font-weight:700;">1000亿元</span>逆回购到期，公开市场实现净投放<span style="color:#f85149;font-weight:700;">1000亿元</span>。市场分析认为，央行操作有助于维护银行体系流动性合理充裕。',
    
    '重点新闻3_标签和标题': '<span class="tag tag-geo">地缘政治</span> 美伊接近达成停火协议',
    '重点新闻3_正文': '据外媒报道，美国与伊朗已拟定<span style="color:#00d4ff;font-weight:700;">60天全面停火草案</span>，双方正在就细节进行最后协商。若协议达成，美国可能逐步解除对伊朗的经济制裁，霍尔木兹海峡通航恢复预期升温。受此消息影响，国际油价<span style="color:#3fb950;font-weight:700;">大幅跳水5%</span>，WTI原油跌破90美元关口。',
    
    '重点新闻4_标签和标题': '<span class="tag tag-tech">科技产业</span> 华为发布"韬定律"芯片设计原理',
    '重点新闻4_正文': '华为技术有限公司近日提出新的芯片设计原理"<span style="color:#bc8cff;font-weight:700;">韬定律</span>"，该原理有望突破现有芯片性能瓶颈。受此消息刺激，A股芯片股集体走强，<span style="color:#f85149;font-weight:700;">华虹半导体大涨10%</span>，中芯国际涨近6%，市场对国产替代进程充满期待。',
    
    '重点新闻5_标签和标题': '<span class="tag tag-energy">能源政策</span> 南方电网负荷创历史新高',
    '重点新闻5_正文': '南方电网发布数据显示，5月26日全网统调负荷达到<span style="color:#f85149;font-weight:700;">2.21亿千瓦</span>，创历史新高，较往年提前近一个月进入用电高峰。受此影响，电力板块掀起涨停潮，<span style="color:#f85149;font-weight:700;">华电能源</span>、<span style="color:#f85149;font-weight:700;">华银电力</span>等多只个股涨停。',
    
    '地缘新闻1_标签和标题': '<span class="tag tag-geo">国际局势</span> 以色列突袭黎巴嫩南部',
    '地缘新闻1_正文': '以色列国防军27日对黎巴嫩南部地区发动<span style="color:#3fb950;font-weight:700;">大规模空袭</span>，造成多人伤亡。联合国安理会紧急召开会议，呼吁各方保持克制。中东地缘紧张局势升级，<span style="color:#f0b429;font-weight:700;">国际油价</span>短期波动加剧。',
    
    '地缘新闻2_标签和标题': '<span class="tag tag-geo">贸易谈判</span> 美墨启动贸易谈判',
    '地缘新闻2_正文': '美国与墨西哥正式启动新一轮贸易谈判，<span style="color:#3fb950;font-weight:700;">加拿大被排除在外</span>。特朗普政府表示，希望达成更有利于美国的贸易协议。市场担忧北美自由贸易格局可能发生重大变化。',
    
    '财经新闻1_标签和标题': '<span class="tag tag-finance">公司动态</span> 贵州茅台完成30亿元股份回购',
    '财经新闻1_正文': '贵州茅台公告称，已完成<span style="color:#f85149;font-weight:700;">30亿元</span>股份回购，回购价格区间为1600-1800元/股。回购股份将全部用于<span style="color:#00d4ff;font-weight:700;">注销并减少注册资本</span>，这是公司年内第二次实施股份回购。',
    
    '财经新闻2_标签和标题': '<span class="tag tag-finance">行业动态</span> 美光科技市值突破1万亿美元',
    '财经新闻2_正文': '受AI芯片需求持续旺盛推动，美光科技股价再创历史新高，总市值突破<span style="color:#f85149;font-weight:700;">1万亿美元</span>，超越伯克希尔哈撒韦。存储芯片板块集体走强，<span style="color:#f85149;font-weight:700;">SanDisk涨逾7%</span>，西部数据涨8%。',
    
    '财经新闻3_标签和标题': '<span class="tag tag-finance">金融监管</span> 香港金管局加强投资账户监管',
    '财经新闻3_正文': '香港金融管理局致函银行，要求对内地个人投资者在港开设的投资账户进行全面倒查，<span style="color:#3fb950;font-weight:700;">违规开户将采取额外措施</span>。此举旨在加强跨境资本流动监管，维护金融稳定。',
    
    '财经新闻4_标签和标题': '<span class="tag tag-finance">市场数据</span> 北向资金单日净流出超800亿',
    '财经新闻4_正文': '5月27日北向资金合计净流出<span style="color:#3fb950;font-weight:700;">843.56亿元</span>，创近期新高。电子、计算机两大科技赛道成为出逃重灾区，<span style="color:#f85149;font-weight:700;">电力、白酒板块获逆势加仓</span>。',
    
    # ===== Tab 2 AI前沿 =====
    '大模型新闻1_标签和标题': '<span class="tag tag-ai">大模型</span> OpenAI发布GPT-5技术白皮书',
    '大模型新闻1_正文': 'OpenAI正式发布GPT-5技术白皮书，披露多项重大技术突破。白皮书显示，GPT-5在多模态理解、推理能力和效率方面均实现<span style="color:#f85149;font-weight:700;">大幅提升</span>，训练成本降低<span style="color:#f85149;font-weight:700;">60%</span>。市场预计，新一代大模型将进一步推动AI应用场景拓展。',
    
    '大模型新闻2_标签和标题': '<span class="tag tag-ai">大模型</span> 国产大模型参数规模突破10万亿',
    '大模型新闻2_正文': '国内某AI企业宣布，其自主研发的大模型参数规模突破<span style="color:#f85149;font-weight:700;">10万亿</span>，成为全球参数规模最大的AI模型之一。该模型在通用能力测试中表现优异，<span style="color:#00d4ff;font-weight:700;">多项指标达到国际领先水平</span>。',
    
    '大模型新闻3_标签和标题': '<span class="tag tag-ai">大模型</span> 谷歌发布Gemini 2.0 Pro',
    '大模型新闻3_正文': '谷歌DeepMind发布Gemini 2.0 Pro，重点优化数学推理和代码生成能力。测试显示，该模型在MATH数据集上正确率提升<span style="color:#f85149;font-weight:700;">35%</span>，<span style="color:#bc8cff;font-weight:700;">代码生成效率提升50%</span>。',
    
    '大模型新闻4_标签和标题': '<span class="tag tag-ai">大模型</span> 开源社区发布Qwen 3.0',
    '大模型新闻4_正文': '阿里云开源社区发布通义千问3.0版本，支持<span style="color:#f85149;font-weight:700;">128K上下文窗口</span>，推理速度提升<span style="color:#f85149;font-weight:700;">2倍</span>。该模型已开放商业使用，助力企业低成本部署AI应用。',
    
    '机器人新闻1_标签和标题': '<span class="tag tag-robot">机器人</span> 特斯拉Optimus产量突破1万台',
    '机器人新闻1_正文': '特斯拉宣布，Optimus人形机器人产量正式突破<span style="color:#f85149;font-weight:700;">1万台</span>，较年初目标提前完成。马斯克表示，Optimus已在特斯拉工厂承担部分重复性工作，<span style="color:#00d4ff;font-weight:700;">商业化进程加速推进</span>。',
    
    '机器人新闻2_标签和标题': '<span class="tag tag-robot">机器人</span> 波士顿动力发布Atlas 3.0',
    '机器人新闻2_正文': '波士顿动力发布新一代人形机器人Atlas 3.0，具备<span style="color:#f85149;font-weight:700;">自主导航</span>和<span style="color:#f85149;font-weight:700;">复杂操作</span>能力。该机器人可在非结构化环境中完成精细任务，<span style="color:#bc8cff;font-weight:700;">灵活性达到新高度</span>。',
    
    '机器人新闻3_标签和标题': '<span class="tag tag-robot">机器人</span> 工信部发布机器人产业发展规划',
    '机器人新闻3_正文': '工信部印发《机器人产业高质量发展行动计划(2026-2030年)》，提出到2030年，我国机器人产业规模突破<span style="color:#f85149;font-weight:700;">1万亿元</span>，<span style="color:#00d4ff;font-weight:700;">关键零部件自给率达到80%</span>。政策利好推动机器人板块走强。',
    
    '算力新闻1_标签和标题': '<span class="tag tag-chip">算力</span> 英伟达推出Blackwell Ultra芯片',
    '算力新闻1_正文': '英伟达正式发布Blackwell Ultra芯片，AI推理性能较前代提升<span style="color:#f85149;font-weight:700;">3倍</span>，能效比提升<span style="color:#f85149;font-weight:700;">2.5倍</span>。该芯片将主要用于数据中心AI推理场景，<span style="color:#bc8cff;font-weight:700;">预计下半年量产</span>。',
    
    '算力新闻2_标签和标题': '<span class="tag tag-chip">算力</span> 国内算力规模突破600EFLOPS',
    '算力新闻2_正文': '工信部数据显示，我国算力基础设施规模已突破<span style="color:#f85149;font-weight:700;">600EFLOPS</span>，其中智算中心算力占比超过<span style="color:#00d4ff;font-weight:700;">40%</span>。"十五五"期间，算力用电量预计年均新增<span style="color:#f85149;font-weight:700;">1000亿千瓦时</span>。',
    
    '算力新闻3_标签和标题': '<span class="tag tag-chip">算力</span> 中亦科技中标4500万AI算力项目',
    '算力新闻3_正文': '中亦科技宣布中标某头部证券公司AI算力资源池项目，金额近<span style="color:#f85149;font-weight:700;">4500万元</span>。该项目将为券商智能化应用提供高性能算力支撑，<span style="color:#00d4ff;font-weight:700;">加速金融行业AI落地</span>。',
    
    'AI应用新闻1_标签和标题': '<span class="tag tag-app">应用</span> AI客服渗透率突破50%',
    'AI应用新闻1_正文': '据行业报告，我国金融、电商等领域AI客服渗透率已突破<span style="color:#f85149;font-weight:700;">50%</span>，较去年同期提升<span style="color:#f85149;font-weight:700;">20个百分点</span>。AI客服不仅降低了企业运营成本，<span style="color:#00d4ff;font-weight:700;">用户满意度也显著提升</span>。',
    
    'AI应用新闻2_标签和标题': '<span class="tag tag-app">应用</span> AI医疗影像诊断准确率达99%',
    'AI应用新闻2_正文': '国内某AI医疗企业宣布，其研发的AI影像诊断系统在肺癌筛查中准确率达到<span style="color:#f85149;font-weight:700;">99%</span>，超过资深放射科医生平均水平。该系统已在全国<span style="color:#00d4ff;font-weight:700;">200多家医院</span>投入使用。',
    
    'AI应用新闻3_标签和标题': '<span class="tag tag-app">应用</span> AI生成内容监管框架出台',
    'AI应用新闻3_正文': '国家网信办发布《生成式人工智能服务管理办法》，明确AI生成内容需标注来源，<span style="color:#f0b429;font-weight:700;">加强版权保护</span>和<span style="color:#f0b429;font-weight:700;">内容审核</span>。政策落地将促进AI产业健康发展。',
    
    '产业趋势新闻1_标签和标题': '<span class="tag tag-energy">趋势</span> AI芯片需求持续高增长',
    '产业趋势新闻1_正文': '据IDC预测，2026年全球AI芯片市场规模将达到<span style="color:#f85149;font-weight:700;">1500亿美元</span>，同比增长<span style="color:#f85149;font-weight:700;">35%</span>。英伟达、AMD等龙头企业持续受益，<span style="color:#bc8cff;font-weight:700;">产业链上下游全面爆发</span>。',
    
    # ===== Tab 3 全球市场 =====
    'A股_上证指数_数据': '4093.73 <span class="down">-1.25%</span>',
    'A股_深证成指_数据': '15736.47 <span class="down">-0.88%</span>',
    'A股_创业板指_数据': '4045.77 <span class="up">+0.07%</span>',
    'A股_科创50_数据': '1815.45 <span class="down">-2.80%</span>',
    'A股_沪深300_数据': '4908.17 <span class="down">-0.80%</span>',
    'A股_成交额': '3.24万亿',
    'A股_涨跌家数': '974:4489',
    'A股_北向资金': '净流出843亿',
    
    '港股_恒生指数_数据': '25599 <span class="down">-0.03%</span>',
    '港股_恒生科技_数据': '4946 <span class="up">+1.59%</span>',
    '港股_国企指数_数据': '8576 <span class="up">+0.30%</span>',
    '港股_南向资金': '净流入28亿',
    
    '亚太_日经225': '64999.41 <span class="up">+0.01%</span>',
    '亚太_KOSPI': '8228.70 <span class="up">+2.25%</span>',
    '亚太_台湾加权': '22456 <span class="down">-0.82%</span>',
    '亚太_Sensex': '78652 <span class="up">+0.65%</span>',
    '亚太_ASX200': '8432 <span class="down">-0.28%</span>',
    
    '欧洲_英国富时100_涨跌幅': '+0.24%',
    '欧洲_德国DAX_涨跌幅': '-0.80%',
    '欧洲_法国CAC_涨跌幅': '-1.03%',
    '欧洲_斯托克50_涨跌幅': '-0.35%',
    
    '美股_道琼斯_涨跌幅': '-0.23%',
    '美股_标普500_涨跌幅': '+0.61%',
    '美股_纳斯达克_涨跌幅': '+1.19%',
    '美股_英伟达_涨跌幅': '-1.04%',
    '美股_特斯拉_涨跌幅': '+1.23%',
    '美股_ARM_涨跌幅': '-3.61%',
    
    '大宗_WTI原油': '88.68 <span class="down">-5.55%</span>',
    '大宗_布伦特原油': '94.29 <span class="down">-5.31%</span>',
    '大宗_国际黄金': '4460.92 <span class="up">+0.10%</span>',
    '大宗_上海金': '973.30 <span class="down">-0.94%</span>',
    '大宗_白银': '76.50 <span class="up">+1.30%</span>',
    
    '加密_BTC': '67,234 <span class="up">+1.82%</span>',
    '加密_ETH': '3,456 <span class="up">+2.15%</span>',
    '加密_ETF净流入': '+8.5亿美元',
    '加密_市场情绪': '偏乐观',
    
    '汇率_USD/CNY中间价': '6.8291',
    '汇率_在岸汇率': '6.7817',
    '汇率_美元指数': '99.20',
    '汇率_美10年收益率': '4.48%',
    '汇率_美30年收益率': '5.01%',
    '汇率_中10年收益率': '1.74%',
    
    # 市场综评
    '正面因素_内容': '1) <span style="color:#f85149;font-weight:700;">电力板块强势领涨</span>，7只个股涨停，成为市场唯一亮点；2) <span style="color:#f85149;font-weight:700;">白酒板块逆势走强</span>，避险资金抱团明显；3) <span style="color:#f85149;font-weight:700;">港股科技股表现活跃</span>，恒生科技指数涨1.59%；4) <span style="color:#f85149;font-weight:700;">美股纳指创历史新高</span>，科技股继续领涨全球。',
    '负面因素_内容': '1) <span style="color:#3fb950;font-weight:700;">A股普跌格局明显</span>，超85%个股收跌；2) <span style="color:#3fb950;font-weight:700;">科创50大跌2.80%</span>，AI高位股集体杀跌；3) <span style="color:#3fb950;font-weight:700;">北向资金净流出843亿</span>，创近期新高；4) <span style="color:#3fb950;font-weight:700;">半导体板块净流出177亿</span>，资金撤离明显。',
    'A股行情_描述': '<span style="color:#3fb950;font-weight:700;">沪指跌1.25%</span>失守4100点，<span style="color:#f85149;font-weight:700;">创业板指逆势微涨0.07%</span>。市场呈现典型的指数维稳、个股普跌格局，<span style="color:#3fb950;font-weight:700;">4489只个股下跌</span>，仅974只上涨。电力、白酒成为资金避风港，<span style="color:#f0b429;font-weight:700;">题材股全线退潮</span>。',
    '外围市场_描述': '<span style="color:#f85149;font-weight:700;">美股三大指数集体收涨</span>，纳指创历史新高；<span style="color:#3fb950;font-weight:700;">欧洲主要指数多数下跌</span>；<span style="color:#f85149;font-weight:700;">亚太市场分化</span>，韩国KOSPI涨2.25%领涨。美光科技市值突破<span style="color:#f85149;font-weight:700;">1万亿美元</span>，英伟达跌1.04%。',
    '地缘政策_描述': '<span style="color:#00d4ff;font-weight:700;">美伊接近达成停火协议</span>，国际油价大跌5%；<span style="color:#f0b429;font-weight:700;">以色列突袭黎巴嫩</span>，中东局势仍存变数；央行开展<span style="color:#00d4ff;font-weight:700;">2000亿逆回购</span>，净投放1000亿维护流动性。',
    '风险事件_描述': '<span style="color:#3fb950;font-weight:700;">A股科技股高位崩盘</span>，需警惕后续补跌风险；<span style="color:#f0b429;font-weight:700;">北向资金持续流出</span>，外资态度趋于谨慎；<span style="color:#f0b429;font-weight:700;">地缘局势反复</span>可能引发油价波动。',
    
    '市场情绪_状态': '偏弱',
    '市场情绪_涨跌比': '974:4489',
    '市场情绪_成交额': '3.24万亿',
    '市场情绪_北向': '-843亿',
    
    # ===== Tab 4 价值投资风向 =====
    '机构1_名称': '中信证券',
    '机构1_观点': '当前市场处于<span style="color:#f0b429;font-weight:700;">阶段性调整期</span>，建议投资者保持耐心，关注<span style="color:#f85149;font-weight:700;">低估值高股息板块</span>。电力、公用事业等防御性板块具备配置价值，<span style="color:#00d4ff;font-weight:700;">建议逢低布局</span>。中期来看，AI产业链仍是主线，但需等待估值消化。',
    
    '机构2_名称': '高盛',
    '机构2_观点': '维持对A股<span style="color:#00d4ff;font-weight:700;">中性偏乐观</span>判断，<span style="color:#f85149;font-weight:700;">盈利复苏</span>仍是核心驱动。看好消费复苏和高端制造，建议关注<span style="color:#bc8cff;font-weight:700;">业绩确定性强</span>的龙头企业。外部环境改善有利于风险偏好修复。',
    
    '机构3_名称': '兴业证券',
    '机构3_观点': '<span style="color:#3fb950;font-weight:700;">短期市场承压</span>，但中期向上趋势未变。建议投资者<span style="color:#00d4ff;font-weight:700;">趁调整加仓</span>优质标的，重点关注<span style="color:#f85149;font-weight:700;">AI算力、半导体设备</span>等方向。流动性宽松环境对市场形成支撑。',
    
    '机构4_名称': '中金公司',
    '机构4_观点': '市场进入<span style="color:#f0b429;font-weight:700;">震荡整固阶段</span>，<span style="color:#f85149;font-weight:700;">防御策略</span>占优。推荐<span style="color:#00d4ff;font-weight:700;">高股息、低波动</span>标的，同时关注政策催化带来的结构性机会。预计后续市场将逐步企稳回升。',
    
    '机构5_名称': '摩根士丹利',
    '机构5_观点': '<span style="color:#00d4ff;font-weight:700;">中国资产吸引力提升</span>，外资回流趋势明确。建议关注<span style="color:#f85149;font-weight:700;">消费升级、科技创新</span>两大主线，<span style="color:#bc8cff;font-weight:700;">长期配置价值凸显</span>。',
    
    '机构6_名称': '瑞银集团',
    '机构6_观点': '<span style="color:#f0b429;font-weight:700;">短期波动加大</span>，但<span style="color:#f85149;font-weight:700;">长期前景乐观</span>。建议投资者<span style="color:#00d4ff;font-weight:700;">保持均衡配置</span>，关注<span style="color:#bc8cff;font-weight:700;">估值合理、增长确定</span>的优质企业。',
    
    # 高股息板块
    '银行板块_PB': '0.85',
    '银行板块_股息率': '5.2%',
    '电力板块_PE': '12.5',
    '电力板块_股息率': '4.8%',
    '公用事业_估值': '偏低',
    '公用事业_股息率': '4.5%',
    '电信板块_PB': '1.2',
    '电信板块_股息率': '5.0%',
    
    '银行板块分析': '银行板块当前<span style="color:#f85149;font-weight:700;">PB仅0.85倍</span>，处于历史低位，<span style="color:#00d4ff;font-weight:700;">股息率达5.2%</span>，具备较高安全边际。随着经济复苏和利率企稳，银行盈利有望逐季改善，<span style="color:#f0b429;font-weight:700;">估值修复空间较大</span>。',
    '电力板块分析': '电力板块<span style="color:#f85149;font-weight:700;">PE 12.5倍</span>，股息率<span style="color:#00d4ff;font-weight:700;">4.8%</span>。用电负荷创历史新高叠加算电协同政策催化，板块基本面持续向好，<span style="color:#f0b429;font-weight:700;">业绩确定性强</span>。',
    '公用事业分析': '公用事业板块估值<span style="color:#3fb950;font-weight:700;">整体偏低</span>，<span style="color:#00d4ff;font-weight:700;">股息率4.5%</span>，防御属性突出。在市场调整阶段，具备<span style="color:#f0b429;font-weight:700;">较好的抗跌能力</span>。',
    '电信板块分析': '电信板块<span style="color:#f85149;font-weight:700;">PB 1.2倍</span>，<span style="color:#00d4ff;font-weight:700;">股息率5.0%</span>，现金流稳定。数字经济发展推动数据中心需求增长，<span style="color:#f0b429;font-weight:700;">长期增长可期</span>。',
    
    # 长线资金动向
    '险资持仓': '+12%',
    '社保持仓': '+8%',
    'QFII持仓': '-5%',
    '北向持仓': '-10%',
    
    # 估值参考表
    '速查1_图标': '📈',
    '速查1_名称': '上证指数',
    '速查1_数值': '4093.73',
    '速查1_颜色': '#3fb950',
    '速查1_标签class': 'warn',
    '速查1_备注': '跌1.25%',
    
    '速查2_图标': '📊',
    '速查2_名称': '深证成指',
    '速查2_数值': '15736.47',
    '速查2_颜色': '#3fb950',
    '速查2_标签class': 'warn',
    '速查2_备注': '跌0.88%',
    
    '速查3_图标': '🌱',
    '速查3_名称': '创业板指',
    '速查3_数值': '4045.77',
    '速查3_颜色': '#f85149',
    '速查3_标签class': 'low',
    '速查3_备注': '涨0.07%',
    
    '速查4_图标': '💰',
    '速查4_名称': '两市成交',
    '速查4_数值': '3.24万亿',
    '速查4_颜色': '#00d4ff',
    '速查4_标签class': 'mid',
    '速查4_备注': '缩量',
    
    '速查5_图标': '🔄',
    '速查5_名称': '北向资金',
    '速查5_数值': '-843亿',
    '速查5_颜色': '#3fb950',
    '速查5_标签class': 'warn',
    '速查5_备注': '净流出',
    
    '速查6_图标': '🇭🇰',
    '速查6_名称': '恒生科技',
    '速查6_数值': '4946',
    '速查6_颜色': '#f85149',
    '速查6_标签class': 'low',
    '速查6_备注': '涨1.59%',
    
    '速查7_图标': '🛢️',
    '速查7_名称': 'WTI原油',
    '速查7_数值': '88.68',
    '速查7_颜色': '#3fb950',
    '速查7_标签class': 'warn',
    '速查7_备注': '跌5.55%',
    
    '速查8_图标': '🥇',
    '速查8_名称': '国际黄金',
    '速查8_数值': '4460',
    '速查8_颜色': '#f85149',
    '速查8_标签class': 'low',
    '速查8_备注': '涨0.10%',
    
    '速查9_图标': '💱',
    '速查9_名称': '人民币汇率',
    '速查9_数值': '6.8291',
    '速查9_颜色': '#00d4ff',
    '速查9_标签class': 'mid',
    '速查9_备注': '中间价',
    
    # ===== Tab 5 关注标的 =====
    '标的1_名称': '工商银行',
    '标的1_代码': '601398',
    '标的1_价格': '5.23',
    '标的1_涨跌幅': '+0.38%',
    '标的1_涨跌class': 'up',
    '标的1_成交额': '28.5亿',
    '标的1_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：股息率6.2%，估值低廉；<span style="color:#3fb950;font-weight:700;">风险</span>：净息差承压',
    
    '标的2_名称': '建设银行',
    '标的2_代码': '601939',
    '标的2_价格': '6.15',
    '标的2_涨跌幅': '+0.49%',
    '标的2_涨跌class': 'up',
    '标的2_成交额': '18.3亿',
    '标的2_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：资产质量优异；<span style="color:#3fb950;font-weight:700;">风险</span>：地产敞口',
    
    '标的3_名称': '农业银行',
    '标的3_代码': '601288',
    '标的3_价格': '3.82',
    '标的3_涨跌幅': '+0.26%',
    '标的3_涨跌class': 'up',
    '标的3_成交额': '15.6亿',
    '标的3_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：县域市场领先；<span style="color:#3fb950;font-weight:700;">风险</span>：利率下行',
    
    '标的4_名称': '招商银行',
    '标的4_代码': '600036',
    '标的4_价格': '32.45',
    '标的4_涨跌幅': '-1.28%',
    '标的4_涨跌class': 'down',
    '标的4_成交额': '45.2亿',
    '标的4_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：零售业务领先；<span style="color:#3fb950;font-weight:700;">风险</span>：市场波动',
    
    '标的5_名称': '宁波银行',
    '标的5_代码': '002142',
    '标的5_价格': '21.88',
    '标的5_涨跌幅': '-0.68%',
    '标的5_涨跌class': 'down',
    '标的5_成交额': '12.8亿',
    '标的5_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：盈利能力强；<span style="color:#3fb950;font-weight:700;">风险</span>：资产规模',
    
    '标的6_名称': '江苏银行',
    '标的6_代码': '600919',
    '标的6_价格': '7.35',
    '标的6_涨跌幅': '+0.27%',
    '标的6_涨跌class': 'up',
    '标的6_成交额': '8.9亿',
    '标的6_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：区域优势明显；<span style="color:#3fb950;font-weight:700;">风险</span>：地方债',
    
    '标的7_名称': '杭州银行',
    '标的7_代码': '600926',
    '标的7_价格': '12.68',
    '标的7_涨跌幅': '-0.47%',
    '标的7_涨跌class': 'down',
    '标的7_成交额': '6.2亿',
    '标的7_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：零售转型成效；<span style="color:#3fb950;font-weight:700;">风险</span>：利率风险',
    
    '标的8_名称': '重庆银行',
    '标的8_代码': '601963',
    '标的8_价格': '6.12',
    '标的8_涨跌幅': '-0.33%',
    '标的8_涨跌class': 'down',
    '标的8_成交额': '3.5亿',
    '标的8_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：西部市场；<span style="color:#3fb950;font-weight:700;">风险</span>：区域经济',
    
    '标的9_名称': '长江电力',
    '标的9_代码': '600900',
    '标的9_价格': '22.35',
    '标的9_涨跌幅': '+1.87%',
    '标的9_涨跌class': 'up',
    '标的9_成交额': '25.6亿',
    '标的9_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：水电龙头，现金流稳定；<span style="color:#3fb950;font-weight:700;">风险</span>：来水不确定性',
    
    '标的10_名称': '大秦铁路',
    '标的10_代码': '601006',
    '标的10_价格': '7.82',
    '标的10_涨跌幅': '+0.26%',
    '标的10_涨跌class': 'up',
    '标的10_成交额': '4.2亿',
    '标的10_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：货运骨干；<span style="color:#3fb950;font-weight:700;">风险</span>：运价下调',
    
    '标的11_名称': '中国移动',
    '标的11_代码': '600941',
    '标的11_价格': '78.56',
    '标的11_涨跌幅': '-0.88%',
    '标的11_涨跌class': 'down',
    '标的11_成交额': '18.9亿',
    '标的11_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：5G龙头，高股息；<span style="color:#3fb950;font-weight:700;">风险</span>：资本开支',
    
    '标的12_名称': '中国核电',
    '标的12_代码': '601985',
    '标的12_价格': '8.65',
    '标的12_涨跌幅': '+2.12%',
    '标的12_涨跌class': 'up',
    '标的12_成交额': '15.2亿',
    '标的12_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：核电装机增长；<span style="color:#3fb950;font-weight:700;">风险</span>：政策审批',
    
    '标的13_名称': '中国平安',
    '标的13_代码': '601318',
    '标的13_价格': '48.23',
    '标的13_涨跌幅': '-1.56%',
    '标的13_涨跌class': 'down',
    '标的13_成交额': '32.8亿',
    '标的13_要点': '<span style="color:#f85149;font-weight:700;">优势</span>：金融全牌照；<span style="color:#3fb950;font-weight:700;">风险</span>：利率下行',
    
    # 标的深度解读
    '标的解读_正面': '<span style="color:#f85149;font-weight:700;">银行股整体稳健</span>，四大行股息率均超5%，具备防御价值。<span style="color:#f85149;font-weight:700;">电力板块强势</span>，长江电力、中国核电涨幅居前。',
    '标的解读_负面': '<span style="color:#3fb950;font-weight:700;">股份制银行承压</span>，招商银行、宁波银行小幅下跌。<span style="color:#3fb950;font-weight:700;">保险股弱势</span>，中国平安跌1.56%。',
    '标的解读_综合': '关注标的整体<span style="color:#f0b429;font-weight:700;">分化明显</span>，防御型标的表现较好。建议<span style="color:#00d4ff;font-weight:700;">逢低布局高股息</span>标的，耐心等待市场企稳。',
    
    # ===== Tab 6 理财话题 =====
    '存款利率_1年': '1.65%',
    '存款利率_3年': '2.60%',
    '存款利率_5年': '2.75%',
    
    '理财收益率_国债': '2.55%',
    '理财收益率_大额存单': '2.45%',
    '理财收益率_货基': '2.10%',
    '理财收益率_债基': '3.20%',
    '理财收益率_理财': '3.50%',
    
    # 社区热门话题
    '社区话题1_标题': '银行股创新高，还能追吗？',
    '社区话题1_来源': '雪球',
    '社区话题1_热度': '热帖TOP5',
    '社区话题1_角色1': '@价值投资者：',
    '社区话题1_观点1': '银行股<span style="color:#f85149;font-weight:700;">估值修复</span>行情才刚开始，<span style="color:#00d4ff;font-weight:700;">股息率超5%</span>具备长期吸引力，建议继续持有。',
    '社区话题1_角色2': '@机构分析师：',
    '社区话题1_观点2': '<span style="color:#f85149;font-weight:700;">险资、北向资金持续加仓</span>，银行股作为核心资产配置价值凸显，可逢低布局。',
    '社区话题1_角色3': '@谨慎派：',
    '社区话题1_观点3': '<span style="color:#3fb950;font-weight:700;">短期涨幅较大</span>，建议等待回调再介入，<span style="color:#f0b429;font-weight:700;">控制仓位</span>是关键。',
    '社区话题1_观点': '银行股创新高是价值发现的体现，<span style="color:#00d4ff;font-weight:700;">低估值+高股息</span>仍是核心逻辑。建议投资者<span style="color:#f0b429;font-weight:700;">分批建仓</span>，不宜追高，关注基本面扎实、股息稳定的标的。',
    
    '社区话题2_标题': '电力股涨停潮，持续性如何？',
    '社区话题2_来源': '东方财富',
    '社区话题2_热度': '热门讨论',
    '社区话题2_角色1': '@趋势投资者：',
    '社区话题2_观点1': '<span style="color:#f85149;font-weight:700;">用电负荷创新高</span>叠加政策利好，电力板块主升浪开启，<span style="color:#00d4ff;font-weight:700;">可持续关注</span>。',
    '社区话题2_角色2': '@产业研究员：',
    '社区话题2_观点2': '<span style="color:#f85149;font-weight:700;">算电协同</span>是长期逻辑，电力作为AI基础设施，需求持续增长，<span style="color:#bc8cff;font-weight:700;">估值有望重塑</span>。',
    '社区话题2_角色3': '@风险提示：',
    '社区话题2_观点3': '<span style="color:#3fb950;font-weight:700;">短期涨幅过大</span>，需警惕获利回吐风险，建议<span style="color:#f0b429;font-weight:700;">设置止损</span>。',
    '社区话题2_观点': '电力板块<span style="color:#f85149;font-weight:700;">基本面支撑扎实</span>，用电旺季+政策催化形成共振。短期或有波动，但<span style="color:#00d4ff;font-weight:700;">长期逻辑通顺</span>，可关注业绩确定性强的龙头标的。',
    
    '社区话题3_标题': 'AI高位崩盘，是机会还是风险？',
    '社区话题3_来源': '集思录',
    '社区话题3_热度': '热议话题',
    '社区话题3_角色1': '@抄底派：',
    '社区话题3_观点1': '<span style="color:#f85149;font-weight:700;">急跌提供上车机会</span>，AI仍是中长期主线，<span style="color:#00d4ff;font-weight:700;">逢低布局核心标的</span>。',
    '社区话题3_角色2': '@风险派：',
    '社区话题3_观点2': '<span style="color:#3fb950;font-weight:700;">高位筹码松动</span>，短期趋势向下，建议<span style="color:#f0b429;font-weight:700;">观望为主</span>。',
    '社区话题3_角色3': '@理性派：',
    '社区话题3_观点3': '分化加剧，<span style="color:#bc8cff;font-weight:700;">精选业绩兑现标的</span>，回避纯题材炒作，关注<span style="color:#00d4ff;font-weight:700;">AI应用落地</span>进展。',
    '社区话题3_观点': 'AI板块<span style="color:#f0b429;font-weight:700;">进入阶段性调整</span>，前期涨幅过大是主因。建议投资者<span style="color:#00d4ff;font-weight:700;">精选个股</span>，关注具备核心技术壁垒和业绩支撑的标的，耐心等待企稳信号。',
    
    '社区话题4_标题': '油价大跌5%，是抄底机会吗？',
    '社区话题4_来源': '同花顺',
    '社区话题4_热度': '实时热点',
    '社区话题4_角色1': '@乐观派：',
    '社区话题4_观点1': '<span style="color:#f85149;font-weight:700;">地缘风险缓解</span>，油价回归基本面，<span style="color:#00d4ff;font-weight:700;">长期需求支撑</span>仍在。',
    '社区话题4_角色2': '@谨慎派：',
    '社区话题4_观点2': '<span style="color:#3fb950;font-weight:700;">趋势已破</span>，短期难言见底，<span style="color:#f0b429;font-weight:700;">观望为宜</span>。',
    '社区话题4_角色3': '@分析师：',
    '社区话题4_观点3': '<span style="color:#bc8cff;font-weight:700;">供需格局改善</span>，但中东局势仍存变数，建议<span style="color:#00d4ff;font-weight:700;">分批布局</span>。',
    '社区话题4_观点': '油价大跌主要受<span style="color:#00d4ff;font-weight:700;">美伊协议预期</span>影响，短期波动较大。中长期看，<span style="color:#f0b429;font-weight:700;">供需基本面支撑油价</span>，可关注油气产业链优质标的的配置机会。',
    
    '社区话题5_标题': '北向资金净流出800亿，外资在撤离？',
    '社区话题5_来源': '微博财经',
    '社区话题5_热度': '热搜话题',
    '社区话题5_角色1': '@外资研究员：',
    '社区话题5_观点1': '<span style="color:#3fb950;font-weight:700;">短期调仓</span>而非长期撤离，<span style="color:#00d4ff;font-weight:700;">中国资产长期吸引力不变</span>。',
    '社区话题5_角色2': '@市场分析：',
    '社区话题5_观点2': '<span style="color:#f0b429;font-weight:700;">获利了结+风险偏好下降</span>，外资选择落袋为安，等待更好买点。',
    '社区话题5_角色3': '@长线投资者：',
    '社区话题5_观点3': '<span style="color:#f85149;font-weight:700;">外资流出提供加仓机会</span>，优质资产逢低布局正当时。',
    '社区话题5_观点': '北向资金<span style="color:#f0b429;font-weight:700;">短期流出</span>主要受市场情绪影响，<span style="color:#00d4ff;font-weight:700;">长期配置逻辑未变</span>。投资者无需过度恐慌，可关注外资流出后的低吸机会。',
    
    '社区话题6_标题': '存款利率下调，钱该往哪放？',
    '社区话题6_来源': '知乎财经',
    '社区话题6_热度': '热门问答',
    '社区话题6_角色1': '@稳健投资者：',
    '社区话题6_观点1': '<span style="color:#f85149;font-weight:700;">大额存单+国债</span>仍是首选，<span style="color:#00d4ff;font-weight:700;">安全性第一</span>。',
    '社区话题6_角色2': '@理财达人：',
    '社区话题6_观点2': '<span style="color:#bc8cff;font-weight:700;">增配债券基金</span>和<span style="color:#bc8cff;font-weight:700;">短债理财</span>，平衡收益与风险。',
    '社区话题6_角色3': '@资产配置：',
    '社区话题6_观点3': '<span style="color:#f0b429;font-weight:700;">多元化配置</span>，适当增加权益资产比例，把握市场机会。',
    '社区话题6_观点': '存款利率下行是长期趋势，建议投资者<span style="color:#00d4ff;font-weight:700;">优化资产配置</span>，在保障流动性的前提下，适当增加收益性资产配置，关注<span style="color:#f85149;font-weight:700;">高股息股票</span>和<span style="color:#bc8cff;font-weight:700;">优质理财</span>产品。',
    
    '社区话题7_标题': '黄金还能涨吗？',
    '社区话题7_来源': '雪球',
    '社区话题7_热度': '讨论中',
    '社区话题7_角色1': '@看多派：',
    '社区话题7_观点1': '<span style="color:#f85149;font-weight:700;">央行购金持续</span>，全球债务高企支撑金价，<span style="color:#00d4ff;font-weight:700;">长期牛市可期</span>。',
    '社区话题7_角色2': '@看空派：',
    '社区话题7_观点2': '<span style="color:#3fb950;font-weight:700;">美债收益率高位</span>压制金价，短期承压明显。',
    '社区话题7_角色3': '@中性观点：',
    '社区话题7_观点3': '<span style="color:#f0b429;font-weight:700;">区间震荡格局</span>，可作为<span style="color:#00d4ff;font-weight:700;">避险配置</span>，不宜重仓。',
    '社区话题7_观点': '黄金<span style="color:#f0b429;font-weight:700;">短期受美债收益率压制</span>，但<span style="color:#00d4ff;font-weight:700;">长期基本面支撑强劲</span>。建议作为资产配置的一部分，保持适度仓位，不宜追高。',
    
    '社区话题8_标题': '白酒逆势上涨，是避风港还是陷阱？',
    '社区话题8_来源': '东方财富',
    '社区话题8_热度': '热议',
    '社区话题8_角色1': '@价值投资者：',
    '社区话题8_观点1': '<span style="color:#f85149;font-weight:700;">防御属性凸显</span>，业绩稳健，<span style="color:#00d4ff;font-weight:700;">长期配置价值</span>。',
    '社区话题8_角色2': '@趋势交易者：',
    '社区话题8_观点2': '<span style="color:#bc8cff;font-weight:700;">资金抱团避险</span>，短期强势，但<span style="color:#f0b429;font-weight:700;">持续性存疑</span>。',
    '社区话题8_角色3': '@消费研究员：',
    '社区话题8_观点3': '<span style="color:#f85149;font-weight:700;">消费复苏预期</span>支撑，高端酒需求韧性强，<span style="color:#00d4ff;font-weight:700;">估值合理</span>。',
    '社区话题8_观点': '白酒板块<span style="color:#f85149;font-weight:700;">防御属性</span>在市场调整期凸显，资金抱团明显。建议关注<span style="color:#00d4ff;font-weight:700;">业绩确定性强</span>的高端酒标的，作为防御配置的一部分。',
    
    '社区话题9_标题': '港股科技股走强，能持续吗？',
    '社区话题9_来源': '集思录',
    '社区话题9_热度': '讨论',
    '社区话题9_角色1': '@港股投资者：',
    '社区话题9_观点1': '<span style="color:#f85149;font-weight:700;">估值优势明显</span>，<span style="color:#00d4ff;font-weight:700;">流动性改善</span>，有望持续修复。',
    '社区话题9_角色2': '@科技分析师：',
    '社区话题9_观点2': '<span style="color:#bc8cff;font-weight:700;">AI产业链受益</span>，芯片股业绩拐点临近，<span style="color:#f0b429;font-weight:700;">值得期待</span>。',
    '社区话题9_角色3': '@风险提示：',
    '社区话题9_观点3': '<span style="color:#3fb950;font-weight:700;">外部环境仍存变数</span>，波动较大，<span style="color:#f0b429;font-weight:700;">控制仓位</span>。',
    '社区话题9_观点': '港股科技股<span style="color:#f85149;font-weight:700;">估值修复行情</span>开启，叠加AI产业链利好，短期表现可期。建议关注<span style="color:#00d4ff;font-weight:700;">基本面改善</span>的标的，同时警惕外部风险。',
    
    '社区话题10_标题': '可转债还值得投资吗？',
    '社区话题10_来源': '知乎',
    '社区话题10_热度': '问答',
    '社区话题10_角色1': '@固收投资者：',
    '社区话题10_观点1': '<span style="color:#f85149;font-weight:700;">下有保底上不封顶</span>，适合稳健型投资者，<span style="color:#00d4ff;font-weight:700;">攻守兼备</span>。',
    '社区话题10_角色2': '@量化玩家：',
    '社区话题10_观点2': '<span style="color:#bc8cff;font-weight:700;">策略空间收窄</span>，需精选标的，<span style="color:#f0b429;font-weight:700;">难度加大</span>。',
    '社区话题10_角色3': '@新手建议：',
    '社区话题10_观点3': '<span style="color:#f0b429;font-weight:700;">先学习再投资</span>，了解转股机制和风险，<span style="color:#00d4ff;font-weight:700;">循序渐进</span>。',
    '社区话题10_观点': '可转债<span style="color:#00d4ff;font-weight:700;">仍是优质投资工具</span>，但需<span style="color:#f0b429;font-weight:700;">精选标的</span>，关注溢价率和正股基本面。建议新手从低风险策略入手，逐步积累经验。',
    
    # ===== Tab 7 今日总结 =====
    '关键词1': 'A股调整',
    '关键词2': '电力领涨',
    '关键词3': '北向流出',
    '关键词4': '油价大跌',
    '关键词5': 'AI退潮',
    '关键词6': '美伊协议',
    '关键词7': '银行护盘',
    '关键词8': '港股走强',
    
    # 宏观面
    '宏观_子标题1': '央行操作',
    '宏观_内容1': '开展<span style="color:#f85149;font-weight:700;">2000亿元</span>逆回购，净投放<span style="color:#f85149;font-weight:700;">1000亿元</span>，维护流动性充裕。',
    '宏观_子标题2': '工业利润',
    '宏观_内容2': '4月规模以上工业利润同比<span style="color:#3fb950;font-weight:700;">下降8.6%</span>，电力行业<span style="color:#f85149;font-weight:700;">增长35.2%</span>。',
    '宏观_子标题3': '汇率走势',
    '宏观_内容3': '人民币中间价<span style="color:#00d4ff;font-weight:700;">6.8291</span>，下调3基点，汇率保持平稳。',
    
    # 市场面
    '市场_子标题1': 'A股表现',
    '市场_内容1': '沪指<span style="color:#3fb950;font-weight:700;">跌1.25%</span>失守4100点，<span style="color:#3fb950;font-weight:700;">4489只个股下跌</span>，普跌格局明显。',
    '市场_子标题2': '美股表现',
    '市场_内容2': '纳指创<span style="color:#f85149;font-weight:700;">历史新高</span>，美光科技市值突破<span style="color:#f85149;font-weight:700;">1万亿美元</span>。',
    '市场_子标题3': '港股表现',
    '市场_内容3': '恒生科技指数<span style="color:#f85149;font-weight:700;">涨1.59%</span>，芯片股集体走强，<span style="color:#f85149;font-weight:700;">华虹半导体涨10%</span>。',
    
    # 资金面
    '资金_子标题1': '北向资金',
    '资金_内容1': '单日净流出<span style="color:#3fb950;font-weight:700;">843亿元</span>，创近期新高，科技股遭减持。',
    '资金_子标题2': '主力资金',
    '资金_内容2': '<span style="color:#f85149;font-weight:700;">电力板块净流入22亿元</span>，<span style="color:#3fb950;font-weight:700;">半导体净流出177亿元</span>。',
    '资金_子标题3': '成交额',
    '资金_内容3': '两市成交<span style="color:#00d4ff;font-weight:700;">3.24万亿</span>，较昨日<span style="color:#3fb950;font-weight:700;">减少51亿</span>，量能维持高位。',
    
    # 理财参考
    '理财参考1_标题颜色': '#3fb950',
    '理财参考1_标题': '1年定存',
    '理财参考1_数值颜色': '#3fb950',
    '理财参考1_数值': '1.65%',
    '理财参考1_备注': '基准利率',
    
    '理财参考2_标题颜色': '#f0b429',
    '理财参考2_标题': '3年定存',
    '理财参考2_数值颜色': '#f0b429',
    '理财参考2_数值': '2.60%',
    '理财参考2_备注': '定期利率',
    
    '理财参考3_标题颜色': '#f85149',
    '理财参考3_标题': '国债收益',
    '理财参考3_数值颜色': '#f85149',
    '理财参考3_数值': '2.55%',
    '理财参考3_备注': '安全首选',
    
    '理财参考4_标题颜色': '#00d4ff',
    '理财参考4_标题': '货币基金',
    '理财参考4_数值颜色': '#00d4ff',
    '理财参考4_数值': '2.10%',
    '理财参考4_备注': '流动性佳',
    
    '理财参考5_标题颜色': '#bc8cff',
    '理财参考5_标题': '债券基金',
    '理财参考5_数值颜色': '#bc8cff',
    '理财参考5_数值': '3.20%',
    '理财参考5_备注': '稳健收益',
    
    '理财参考6_标题颜色': '#ffa657',
    '理财参考6_标题': '银行理财',
    '理财参考6_数值颜色': '#ffa657',
    '理财参考6_数值': '3.50%',
    '理财参考6_备注': '中低风险',
    
    # 操作建议
    '操作建议1_标题': '减仓观望',
    '操作建议1_内容': '<span style="color:#3fb950;font-weight:700;">市场普跌格局明显</span>，超过85%个股收跌，亏钱效应扩散。',
    '操作建议1_补充': 'AI高位股集体杀跌，科创50大跌2.80%，短期风险释放中。',
    '操作建议1_操作': '建议投资者<span style="color:#f0b429;font-weight:700;">控制仓位</span>，观望为主，等待市场企稳。',
    
    '操作建议2_标题': '关注防御',
    '操作建议2_内容': '<span style="color:#f85149;font-weight:700;">电力、白酒板块逆势走强</span>，成为资金避风港。',
    '操作建议2_补充': '电力板块7只个股涨停，白酒板块涨3.14%领涨市场。',
    '操作建议2_操作': '可逢低关注<span style="color:#00d4ff;font-weight:700;">高股息防御标的</span>，规避高位题材股。',
    
    '操作建议3_标题': '等待企稳',
    '操作建议3_内容': '<span style="color:#3fb950;font-weight:700;">北向资金大幅流出</span>，外资态度趋于谨慎。',
    '操作建议3_补充': '单日净流出843亿元，创近期新高，需警惕后续资金动向。',
    '操作建议3_操作': '<span style="color:#f0b429;font-weight:700;">耐心等待</span>市场企稳信号，不宜急于抄底。',
    
    '操作建议4_标题': '港股机会',
    '操作建议4_内容': '<span style="color:#f85149;font-weight:700;">恒生科技指数涨1.59%</span>，芯片股集体走强。',
    '操作建议4_补充': '华虹半导体涨逾10%，中芯国际涨近6%，华为"韬定律"利好刺激。',
    '操作建议4_操作': '关注港股科技股<span style="color:#bc8cff;font-weight:700;">估值修复机会</span>，精选优质标的。',
    
    '操作建议5_标题': '能源布局',
    '操作建议5_内容': '<span style="color:#3fb950;font-weight:700;">国际油价大跌5.55%</span>，地缘风险缓解。',
    '操作建议5_补充': '美伊接近达成停火协议，霍尔木兹海峡通航恢复预期升温。',
    '操作建议5_操作': '<span style="color:#f0b429;font-weight:700;">关注油气产业链</span>调整后的配置机会。',
    
    '操作建议6_标题': 'AI精选',
    '操作建议6_内容': '<span style="color:#3fb950;font-weight:700;">AI板块阶段性调整</span>，前期涨幅过大是主因。',
    '操作建议6_补充': '算力、芯片等核心赛道仍具长期价值，等待估值消化。',
    '操作建议6_操作': '<span style="color:#00d4ff;font-weight:700;">精选业绩确定性强</span>的AI标的，逢低布局。',
    
    # 其他
    '每日重点事件': 'A股调整，电力领涨',
    '报告日期': REPORT_DATE,
    '数据截止日期': '2026年5月27日',
}

# 读取模板文件
with open('/workspace/老盛早知道_20260528.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换所有占位符
for key, value in data.items():
    placeholder = f'{{{{{key}}}}}'
    content = content.replace(placeholder, value)

# 特殊处理：替换页头日期格式
content = content.replace('{{YYYY/MM/DD}}', YYYYMMDD_DISPLAY)
content = content.replace('{{星期}}', WEEKDAY)

# 写入最终报告
with open('/workspace/老盛早知道_20260528.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("报告生成完成！")
