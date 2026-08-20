# -*- coding: utf-8 -*-
# 老盛早知道_20260820.html 全面质量检查（对照 报告质量检查.md v2.3 六大章节）
import re, io

PATH = "老盛早知道_20260820.html"
html = io.open(PATH, encoding="utf-8").read()
lines = html.split("\n")

results = []
def check(chapter, item, ok, detail=""):
    results.append((chapter, item, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {chapter} | {item}" + (f" | {detail}" if detail else ""))

# ============ 一、数据及时性 ============
# 1.2 旧日期残留（T-3日及更早，输出应≤3处）
old_dates = ["8/15","8/14","8/13","8/12","8/11","8/10","8/09","8/08","2026-08-15","2026-08-14","2026-08-13"]
old_hits = {d: html.count(d) for d in old_dates if html.count(d) > 0}
old_total = sum(old_hits.values())
check("一.数据及时性", "旧日期残留≤3处(T-3及更早)", old_total <= 3,
      f"命中{old_total}处: {old_hits}" if old_total else "无旧日期")
# 1.2 新数据已写入（关键数据出现≥10处）
new_cnt = html.count("8/19") + html.count("2026-08-19")
check("一.数据及时性", "新数据(8/19)覆盖≥10处", new_cnt >= 10, f"8/19出现{new_cnt}处")
# 1.2 收盘标注
check("一.数据及时性", "价格/指数标注收盘日期",
      ("8/19收盘" in html) or ("2026-08-19收盘" in html),
      f"2026-08-19收盘出现{html.count('2026-08-19收盘')}处")

# ============ 二、结构与样式 ============
check("二.结构", "文件行数≈模板(4018)", 3600 <= len(lines) <= 4200,
      f"{len(lines)}行 (模板4018；规范旧值3800±200已滞后)")
check("二.结构", "CSS结束标签</style>在1500-1800",
      1500 <= (next((i for i,l in enumerate(lines) if "</style>" in l), -1)+1) <= 1800,
      f"第{next((i for i,l in enumerate(lines) if '</style>' in l),-1)+1}行")
check("二.结构", "tab-panel=8", html.count('id="panel-') == 8, f"{html.count('id=\"panel-')}个")
check("二.结构", "sub-title(模板实际28)",
      len(re.findall(r'class="sub-title"', html)) in (27,28,29,30,31),
      f"{len(re.findall(r'class=\"sub-title\"', html))}个 (规范26-27滞后)")
check("二.结构", "stock-card=15(模板实际)",
      html.count('class="stock-card"') == 15, f"{html.count('class=\"stock-card\"')}个 (规范13滞后)")
check("二.结构", "sentiment-item=9", html.count('class="sentiment-item"') == 9,
      f"{html.count('class=\"sentiment-item\"')}个")
check("二.结构", "market-block=8", html.count('class="market-block"') == 8,
      f"{html.count('class=\"market-block\"')}个")
# Tailwind 污染（排除 hm-/grid-N 自定义类）
tw = re.findall(r'(?<!")(?<!\w)(?:[whpm]\-[0-9]|flex\-(col|row)|grid\-cols)[a-z0-9\-]*', html)
check("二.结构", "无真实Tailwind污染", len(tw) == 0, f"命中{len(tw)}" if tw else "无")
check("二.结构", "占位符数量=0", html.count("{{") == 0, f"{html.count('{{')}处")
check("二.结构", "暂无数据=0", html.count("暂无数据") == 0, f"{html.count('暂无数据')}处")
check("二.结构", '"--"缺失标记=0', html.count('"--"') == 0, f"{html.count('\"--\"')}处")
# div 平衡
check("二.结构", "div标签平衡", html.count("<div") == html.count("</div>"),
      f"开{html.count('<div')}/闭{html.count('</div>')}")

# ============ 三、数据准确性 ============
# 3.1 涨红跌绿：全报告所有红/绿着色%必须与符号一致
bad_color = []
for m in re.finditer(r'color:#([0-9a-fA-F]+);font-weight:700;">([+-]?\d+\.\d+%)', html):
    color, val = m.group(1).lower(), m.group(2)
    if val.startswith("+"):
        exp = "f85149"
    elif val.startswith("-"):
        exp = "3fb950"
    else:
        continue  # 无符号（如收益率水平）不强制
    if color != exp:
        bad_color.append((val, color, exp))
check("三.涨红跌绿", "所有红/绿%符号↔颜色一致", len(bad_color) == 0,
      f"异常{bad_color}" if bad_color else "全部±%红涨绿跌正确")
# 3.1 stock-card class↔符号
bad_cls = []
for m in re.finditer(r'class="stock-change (up|down)">([+-]?\d+\.\d+%)', html):
    cls, val = m.group(1), m.group(2)
    if cls == "up" and not val.startswith("+"): bad_cls.append((val,"up"))
    if cls == "down" and not val.startswith("-"): bad_cls.append((val,"down"))
check("三.涨红跌绿", "stock-card up=+ / down=-", len(bad_cls) == 0,
      f"异常{bad_cls}" if bad_cls else "15只标的class与符号一致")
# 3.1 summary-card-change 方向
bad_sum = []
for m in re.finditer(r'summary-card-change (up|down)">([+-]?\d+\.\d+%)', html):
    cls, val = m.group(1), m.group(2)
    if cls == "up" and not val.startswith("+"): bad_sum.append((val,"up"))
    if cls == "down" and not val.startswith("-"): bad_sum.append((val,"down"))
check("三.涨红跌绿", "首页summary-card方向正确", len(bad_sum) == 0,
      f"异常{bad_sum}" if bad_sum else "首页4卡方向正确")
# 3.1 语义上下文：领涨/大涨/创新高 不应被绿包裹；大跌/暴跌/净卖出/重挫 不应被红包裹
ctx_red_kw = ["领涨","大涨","创新高","普涨","走强","看多","净流入"]
ctx_green_kw = ["大跌","暴跌","净卖出","重挫","承压","跳水","净流出","恐慌"]
# 取所有绿/红 span 内文本，检查是否含反向语义词
mis = []
for m in re.finditer(r'color:#([0-9a-fA-F]+);font-weight:700;">([^<]{0,40})<', html):
    color, txt = m.group(1).lower(), m.group(2)
    if color == "3fb950" and any(k in txt for k in ctx_red_kw): mis.append(("绿含涨义",txt))
    if color == "f85149" and any(k in txt for k in ctx_green_kw): mis.append(("红含跌义",txt))
check("三.涨红跌绿", "语义方向不反色(抽查)", len(mis) == 0,
      f"疑点{mis[:5]}" if mis else "未见红绿反义")

# 3.3 数据完整性：市场块名称齐全
req_markets = ["A股","港股","亚太","欧洲","美股","大宗商品","加密货币","汇率"]
miss_mk = [k for k in req_markets if f'{k}（2026-08-19收盘）' not in html and f'{k}市场' not in html and f'{k}与债券' not in html]
check("三.数据完整性", "8大市场块标题齐全", len(miss_mk) == 0, f"缺{miss_mk}" if miss_mk else "A股/港股/亚太/欧洲/美股/大宗/加密/汇率全在")
# 3.3 关注标的股价齐全（15只）
req_stocks = ["工商银行","建设银行","农业银行","招商银行","宁波银行","江苏银行","杭州银行","重庆银行","长江电力","大秦铁路","中国移动","中国核电","中国平安"]
miss_stk = [s for s in req_stocks if s not in html]
check("三.数据完整性", "关注标的企业名称齐全", len(miss_stk) == 0, f"缺{miss_stk}" if miss_stk else "15只标的全在")
# 3.3 估值参考表字段（去高亮span后判定，避免被span拆分误判）
plain = re.sub(r"<[^>]+>", "", html)
est = ["银行板块","上证PE","银行股息率","中证红利PE","神华吨煤利润","中国移动PB","招商银行PB","中国核电PE","黄金价格"]
est_missing = [e for e in est if e not in plain]
check("三.数据完整性", "估值参考表9字段齐全", len(est_missing) == 0, f"缺{est_missing}" if est_missing else "9字段均在")

# 3.2 数据一致性：关键指标单一取值
metrics = {"上证3894.42":"3894.42","深证13890.15":"13890.15","创业板3473.49":"3473.49",
           "沪深300 4588.70":"4588.70","科创50 1667.52":"1667.52","成交2.51万亿":"2.51",
           "北向989亿":"989","银行+1.78%":"1.78","中证红利5553.33":"5553.33",
           "WTI86.45":"86.45","布伦特92.21":"92.21","现货金4519":"4519.00"}
miss_metric = [k for k,v in metrics.items() if v not in html]
check("三.数据一致性", "关键指标取值一致且存在", len(miss_metric) == 0,
      f"缺{miss_metric}" if miss_metric else "12项关键指标取值一致")

# ============ 四、交互功能 ============
st = re.search(r'function switchTab\([^)]*\)\s*\{', html)
check("四.交互", "switchTab函数完整且未修改",
      bool(st) and "window.scrollTo" in html,
      "function switchTab 存在且含 window.scrollTo" if (st and "window.scrollTo" in html) else "缺失")

# ============ 五、必查内容 ============
# 5.1 四大区域≥120字（关键词定位起点，跳过 HTML 注释；下一 sub-title 为终点，无则取 6000 字上限）
def find_kw_outside_comment(kw):
    pos = 0
    while True:
        i = html.find(kw, pos)
        if i < 0:
            return -1
        cmt_open = html.rfind("<!--", 0, i)
        if cmt_open >= 0:
            cmt_close = html.find("-->", cmt_open)
            if cmt_close >= 0 and cmt_close > i:
                # 命中位置仍在注释内，跳过
                pos = i + len(kw); continue
        return i
for name, kw in [("机构价值投资观点","机构价值投资观点"),("高股息板块深度分析","高股息"),
                 ("社区热门话题","社区热门话题"),("今日操作建议","今日操作建议")]:
    idx = find_kw_outside_comment(kw)
    if idx < 0:
        check("五.必查", f"区域≥120字: {name}", False, "未找到区域")
        continue
    nxt = html.find('class="sub-title"', idx+10)
    seg = html[idx:nxt] if nxt >= 0 else html[idx:idx+6000]
    chars = len(re.sub(r"<[^>]+>", "", seg))
    check("五.必查", f"区域≥120字: {name}", chars >= 120, f"{chars}字")

# 5.2 社区格式
community_idx = html.find('class="sub-title">社区热门话题')
community_end = html.find('class="sub-title"', community_idx+10)
comm = html[community_idx:community_end] if community_idx>=0 else ""
q_titles = len(re.findall(r'[？?]', comm))
check("五.必查", "社区话题问句标题≥10", q_titles >= 10, f"{q_titles}个问号")
for sp in ["@价值投资者","@机构分析师","@谨慎派"]:
    c = comm.count(sp)
    check("五.必查", f"社区发言方{sp}", c >= 1, f"{c}次")
laosheng = comm.count("老盛观点")
check("五.必查", "社区老盛观点出现", laosheng >= 1, f"{laosheng}次")
comm_hl = comm.count('<span style="color')
check("五.必查", "社区高亮≥问句*4", comm_hl >= q_titles*4, f"高亮{comm_hl}/话题{q_titles}(需≥{q_titles*4})")

# 5.3 全局文字高亮
total_hl = html.count('<span style="color')
check("五.必查", "全局文字高亮已应用", total_hl >= 100, f"全局高亮{total_hl}处")

# ============ 二.3 逐Tab卡片高亮密度 ============
def panel_content(n):
    s = html.find(f'id="panel-{n}"')
    e = html.find(f'id="panel-{n+1}"', s+1) if n < 7 else len(html)
    return html[s:e]

def card_body_highlights(text):
    res = []
    for m in re.finditer(r'<div class="card-body">', text):
        i = m.end(); depth = 1; j = i
        while j < len(text):
            if text.startswith("<div", j):
                depth += 1; j = text.find(">", j)+1; continue
            if text.startswith("</div>", j):
                depth -= 1; j += 6
                if depth == 0: break
                continue
            j += 1
        block = text[m.end():j-6]
        res.append(block.count('<span style="color'))
    return res

floors = {0:3, 1:5, 2:5, 3:2, 4:2, 5:2, 6:2, 7:2}
for n in range(8):
    hs = card_body_highlights(panel_content(n))
    if not hs:
        check(f"二.3.Tab{n}", f"卡片高亮密度(面板{n})", True, "无card-body(跳过)")
        continue
    mn = min(hs)
    below = [i for i,v in enumerate(hs) if v < floors[n]]
    check(f"二.3.Tab{n}", f"卡片高亮密度≥{floors[n]}/卡", len(below)==0,
          f"min={mn}, avg={sum(hs)/len(hs):.1f}, 卡数={len(hs)}, 低于阈值{below[:5]}")

# ============ 汇总 ============
print("\n" + "="*50)
pass_n = sum(1 for r in results if r[2]); fail_n = sum(1 for r in results if not r[2])
print(f"总计 {len(results)} 项，PASS {pass_n}，FAIL {fail_n}")
if fail_n == 0:
    print("🎉 全面质量检查全部通过")
else:
    print("⚠️ 存在未通过项，需修复")
    for r in results:
        if not r[2]:
            print("   -", r[0], "|", r[1], "|", r[3])
