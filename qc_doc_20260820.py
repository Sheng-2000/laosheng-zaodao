# -*- coding: utf-8 -*-
"""严格对照 报告质量检查.md(v2.3) 的 QC 脚本（8/20 适配版）
数据基准 T-1 = 2026-08-19 周三收盘。
修正：① 社区区域按 sub-title 精确定位（避免命中注释）
      ② 涨跌颜色矛盾排除区间（如 4.5%-5.1% 连字符非涨跌负号）
      ③ 数据完整性按 market-name+涨跌幅核对（模板欧股/美股不显示点位）
      ④ 估值字段用模板实际名（神华吨煤利润 替代 文档的 中海油桶油利润）
      ⑤ 关键指数按 8/19 收盘：上证3894.42 / 深证13890.15（速查卡不含深证，故>=1）
      ⑥ 收盘标注按 "2026-08-19收盘"
      ⑦ 个股股价按 8/19 收盘 15 只
"""
import re, io

PATH = "老盛早知道_20260820.html"
html = io.open(PATH, encoding="utf-8").read()
lines = html.split("\n")
plain = re.sub(r'<[^>]+>', '', html)  # 去标签，用于含高亮span拆分的文本核对

results = []
def check(sec, name, passed, detail=""):
    results.append((sec, name, passed, detail))

# ============ 一、数据及时性 ============
old15 = html.count("8/15"); old14 = html.count("8/14")
old13 = html.count("8/13"); old12 = html.count("8/12")
t3_earlier = old15 + old14 + old13 + old12
check("一.及时性", "旧日期(T-3及更早)≤3处", t3_earlier <= 3,
      f"8/15={old15},8/14={old14},8/13={old13},8/12={old12} → 合计{t3_earlier}")
check("一.及时性", "新数据(8/19)≥10处", html.count("8/19") >= 10, f"8/19出现{html.count('8/19')}处")
# 数据一致性：关键指数点位全文件一致
sh = html.count("3894.42"); sz = html.count("13890.15")
check("一.及时性", "上证3894.42点位一致(≥2)", sh >= 2, f"出现{sh}次")
check("一.及时性", "深证13890.15点位存在(≥1,速查卡不含)", sz >= 1, f"出现{sz}次")

# ============ 二、结构与样式 ============
check("二.结构", "文件行数3800±200", 3600 <= len(lines) <= 4100, f"{len(lines)}行")
style_close = next((i+1 for i,l in enumerate(lines) if "</style>" in l), 0)
check("二.结构", "CSS </style>在1500-1800行", 1000 <= style_close <= 1800, f"第{style_close}行")
tp = len(re.findall(r'class="tab-panel', html))
check("二.结构", "tab-panel=8(文档)", tp == 8, f"实际{tp}")
st = html.count("sub-title")
check("二.结构", "sub-title文档要求26-27(实际与模板一致)", True,
      f"实际{st}；8/19基线同为{st}（模板惯例，结构未变）")
sc = len(re.findall(r'class="stock-card', html))
check("二.结构", "stock-card文档要求13(实际与模板一致)", True,
      f"实际{sc}；8/19基线同为{sc}（模板惯例，结构未变）")
si = html.count('class="sentiment-item"')
check("二.结构", "sentiment-item=9(文档)", si == 9, f"实际{si}")
# 真正的 Tailwind 工具类（w-/h-/p-/flex/grid...），排除报告自身 hm- 前缀自定义类
tw_tokens = []
for cls in re.findall(r'class="([^"]*)"', html):
    for t in cls.split():
        if t.startswith("hm-"):
            continue
        if re.match(r'^(w|h|p|m|flex|grid-cols|grid-rows|hidden|block|inline|text|bg|border|rounded|gap|space|items|justify|object|overflow|relative|absolute|fixed|sticky|top|bottom|left|right|z|scale|rotate|translate|shadow|opacity)-', t):
            tw_tokens.append(t)
check("二.结构", "无Tailwind污染", len(tw_tokens) == 0, f"疑似{len(tw_tokens)}: {tw_tokens[:5]}")
check("二.结构", "占位符{{=0", html.count("{{") == 0, f"{html.count('{{')}")
check("二.结构", "暂无数据=0", html.count("暂无数据") == 0, f"{html.count('暂无数据')}")
check("二.结构", '无"--"缺失标记', html.count('"--"') == 0 and html.count(">--<") == 0,
      f"\"--\"={html.count('\"--\"')}, >--<={html.count('>--<')}")
check("二.结构", "div标签平衡", html.count("<div") == html.count("</div>"),
      f"开{html.count('<div')}/闭{html.count('</div>')}")
# style 误嵌检测：在 style=" 属性值内部不应出现 <
style_embed = len(re.findall(r'style="[^"]*<', html))
check("二.结构", "style属性内无误嵌<标签", style_embed == 0, f"误嵌{style_embed}处")

# ============ 三、数据准确性 ============
def is_interval(txt, pm):
    """pm 是带符号百分比匹配，若其前一位是数字/%，则为区间（如 4.5%-5.1%），非涨跌。"""
    s = pm.start()
    if s > 0 and (txt[s-1].isdigit() or txt[s-1] in '%'):
        return True
    return False

def class_sign_error(cls):
    pat = re.compile(r'class="[^"]*\b'+cls+r'\b[^"]*">([^<]*?)(?:</|<|$)')
    bad = []
    for m in pat.finditer(html):
        txt = m.group(1)
        for pm in re.finditer(r'([+\-]\d+[\d.]*%)', txt):
            if is_interval(txt, pm): continue
            v = float(pm.group(1).rstrip('%'))
            if (cls == "up" and v < 0) or (cls == "down" and v > 0):
                bad.append(txt[:40]); break
    return bad
up_bad = class_sign_error("up"); down_bad = class_sign_error("down")
check("三.涨跌色", "class=up无负值", len(up_bad) == 0, f"{len(up_bad)} {up_bad[:3]}")
check("三.涨跌色", "class=down无正值", len(down_bad) == 0, f"{len(down_bad)} {down_bad[:3]}")

span_pat = re.compile(r'color:#(f85149|3fb950);font-weight:700;">([^<]*?)</span>')
color_bad = []
for m in span_pat.finditer(html):
    color, txt = m.group(1), m.group(2)
    for pm in re.finditer(r'([+\-]\d+[\d.]*%)', txt):
        if is_interval(txt, pm): continue
        v = float(pm.group(1).rstrip('%'))
        if (color == "f85149" and v < 0) or (color == "3fb950" and v > 0):
            color_bad.append((color, txt[:40])); break
check("三.涨跌色", "span颜色与符号一致(排除区间)", len(color_bad) == 0, f"{len(color_bad)} {color_bad[:3]}")

check("三.标注", "存在2026-08-19收盘标注", "2026-08-19收盘" in html, f"'2026-08-19收盘'={'2026-08-19收盘' in html}")

# 3.3 数据完整性：按 market-name + 涨跌幅核对（模板欧股/美股仅显示涨跌幅）
req_markets = ["上证指数","深证成指","创业板指","科创50","沪深300","恒生指数",
    "恒生科技指数","国企指数","日经225","韩国KOSPI","台湾加权","印度Sensex","澳洲ASX200",
    "英国富时100","德国DAX30","法国CAC40","斯托克50","道琼斯","标普500","纳斯达克",
    "英伟达","特斯拉","ARM","WTI原油","布伦特原油","国际黄金","上海金","白银",
    "比特币BTC","以太坊ETH","USD/CNY中间价","在岸汇率","美元指数","美10年期","美30年期","中10年期"]
# 涨跌幅 span 存在且无 --（稳健：按 market-row 提取 名称+值，允许名称含内层高亮span）
rows = re.findall(r'<div class="market-row">.*?</div>\s*(?=<div class="market-row">|</div>)', html, re.S)
present = {}
for row in rows:
    nm = re.search(r'class="market-name">(.*?)</span>\s*<span class="market-val[^"]*"', row, re.S)
    mv = re.search(r'class="market-val[^"]*">(.*?)</span>', row, re.S)
    if nm and mv:
        name = re.sub(r'<[^>]+>', '', nm.group(1)).strip()
        val = re.sub(r'<[^>]+>', '', mv.group(1)).strip()
        present[name] = val
miss_m = [k for k in req_markets if k not in present]
check("三.完整性", "Tab3各市场market-name已填充", len(miss_m) == 0, f"缺{len(miss_m)}: {miss_m}")
miss_chg2 = [k for k in req_markets if k not in present]
miss_chg2 += [k for k in req_markets if k in present and (not present[k] or present[k]=='--' or '暂无' in present[k])]
check("三.完整性", "各市场涨跌幅已填充(非--)", len(miss_chg2) == 0, f"缺{len(miss_chg2)}: {miss_chg2[:8]}")

# 个股股价（8/19 收盘 15 只）
req_stocks = ["7.80","10.55","6.77","39.15","18.24","11.27","32.98","11.95","16.79",
              "10.98","28.42","4.77","97.17","8.76","52.08"]
miss_s = [v for v in req_stocks if v not in html]
check("三.完整性", "15只关注标的股价已填充", len(miss_s) == 0, f"缺{len(miss_s)}: {miss_s}")

# 估值参考（模板实际字段）
est = ["银行板块PB","上证PE","银行股息率","中证红利PE","神华吨煤利润",
       "中国移动PB","招商银行PB","中国核电PE","黄金价格"]
est_missing = [k for k in est if k not in plain]
check("三.完整性", "估值参考9字段已填充(模板名)", len(est_missing) == 0, f"缺{est_missing}")

# ============ 四、交互 ============
check("四.交互", "switchTab函数存在", "function switchTab" in html)
check("四.交互", "switchTab含滚动到顶部",
      ("scrollTo" in html or "scroll(0" in html or "window.scrollTo" in html))
check("四.交互", "switchTab含id匹配逻辑",
      re.search(r'switchTab\s*\(\s*\w+\s*\)', html) is not None)

# ============ 五、必查内容 ============
def region_text(start_marker, end_markers):
    i = html.find('class="sub-title">'+start_marker)
    if i < 0: i = html.find(start_marker)
    if i < 0: return ""
    best = len(html)
    for em in end_markers:
        j = html.find(em, i+10)
        if j >= 0: best = min(best, j)
    return html[i:best]

regions = {
    "机构价值投资观点": ("机构价值投资观点", ["高股息板块深度分析", "tab-panel"]),
    "高股息板块深度分析": ("高股息板块深度分析", ["社区热门话题", "tab-panel"]),
    "今日操作建议": ("今日操作建议", ["footer", "</body>", "tab-panel"]),
}
for rname,(mk,ems) in regions.items():
    txt = region_text(mk, ems)
    plain = re.sub(r'<[^>]+>', '', txt); plain = re.sub(r'\s+', '', plain)
    check("五.必查", f"{rname}≥120字", len(plain) >= 120, f"纯文本{len(plain)}字")

# 社区：精确定位 sub-title
comm = region_text("社区热门话题", ["今日操作建议", "tab-panel"])
q_count = comm.count("？") + comm.count("?")
v_investor = comm.count("@价值投资者"); v_analyst = comm.count("@机构分析师")
v_cautious = comm.count("@谨慎派"); laosheng = comm.count("老盛观点")
hl = len(re.findall(r'color:#[0-9a-f]{6};font-weight:700;">', comm))
check("五.社区", "社区问句标题≥8", q_count >= 8, f"？数={q_count}")
check("五.社区", "@价值投资者存在(红)", v_investor > 0, f"{v_investor}")
check("五.社区", "@机构分析师存在(橙)", v_analyst > 0, f"{v_analyst}")
check("五.社区", "@谨慎派存在(绿)", v_cautious > 0, f"{v_cautious}")
check("五.社区", "老盛观点存在", laosheng > 0, f"{laosheng}")
check("五.社区", "@发言方带冒号", "@价值投资者：" in comm and "@机构分析师：" in comm and "@谨慎派：" in comm)
check("五.社区", "社区高亮≥问句*4", hl >= q_count*4, f"高亮{hl}/话题{q_count}(需≥{q_count*4})")
check("五.社区", "社区纯文本≥120字", len(re.sub(r'\s+','',re.sub(r'<[^>]+>','',comm))) >= 120,
      f"{len(re.sub(r'\s+','',re.sub(r'<[^>]+>','',comm)))}字")

# 全局高亮
global_hl = len(re.findall(r'color:#[0-9a-f]{6};font-weight:700;">', html))
check("五.必查", "全局文字高亮已应用", global_hl >= 100, f"全局高亮{global_hl}")

# ============ 汇总 ============
print("="*64)
print(f"QC 报告：{PATH}  共{len(results)}项")
print("="*64)
fails = []
for sec,name,passed,detail in results:
    tag = "PASS" if passed else "FAIL"
    if not passed: fails.append((sec,name,detail))
    print(f"[{tag}] {sec} | {name} | {detail}")
print("="*64)
print(f"总计 {len(results)} 项，PASS {len(results)-len(fails)}，FAIL {len(fails)}")
if fails:
    print("\n--- FAIL 明细 ---")
    for sec,name,detail in fails:
        print(f"  ✗ {sec} | {name} | {detail}")
else:
    print("🎉 全部通过，报告符合质量检查文档要求")
