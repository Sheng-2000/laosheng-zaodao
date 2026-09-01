# -*- coding: utf-8 -*-
import re, importlib.util, os

HERE = os.path.dirname(os.path.abspath(__file__))
def load(mn):
    spec = importlib.util.spec_from_file_location(mn, os.path.join(HERE, mn + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
d1 = load("g_data1"); d2 = load("g_data2")
D = {}; D.update(d1.D); D.update(d2.D)

html = open("老盛早知道_20260901.html", encoding="utf-8").read()
T = open("template.html", encoding="utf-8").read()
def c(s): return re.sub(r'<[^>]+>', '', str(s))

print("=" * 60)
print("老盛早知道 20260901 全面质量检查")
print("=" * 60)

ok = True
def check(name, cond, detail=""):
    global ok
    if not cond: ok = False
    print(("  [OK] " if cond else "  [XX] ") + name + (("  -> " + detail) if detail else ""))

# ---------- 一、数据及时性 ----------
print("\n【一、数据及时性】")
dates = re.findall(r'(?<!\d)(\d{1,2})月(\d{1,2})日', html)
from collections import Counter
dc = Counter((int(m), int(d)) for m, d in dates)
stale = sum(n for (m, d), n in dc.items() if (m < 8) or (m == 8 and d <= 28))
check("无陈旧日期(<=8/28)", stale == 0, "陈旧%d处" % stale)
check("含报告日 9/1", sum(n for (m,d),n in dc.items() if m==9 and d==1) >= 1)
check("含收盘日 8/31", sum(n for (m,d),n in dc.items() if m==8 and d==31) >= 1)

# ---------- 二、结构样式 ----------
print("\n【二、结构与样式】")
def cnt(p, s=html): return len(re.findall(p, s))
check("tab-panel = 8 (模板一致)", cnt(r'class="[^"]*tab-panel') == 8, "=%d" % cnt(r'class="[^"]*tab-panel'))
check("summary-card = 29 (模板一致)", cnt(r'class="[^"]*summary-card') == cnt(r'class="[^"]*summary-card', T))
check("market-block = 8", cnt(r'class="[^"]*market-block') == 8)
check("stock-card = 16 (16标的)", cnt(r'class="[^"]*stock-card') == 16, "=%d" % cnt(r'class="[^"]*stock-card'))
check("sentiment-item = 9", cnt(r'class="[^"]*sentiment-item') == 9)
check("sub-title = 28 (模板一致)", cnt(r'class="[^"]*sub-title') == cnt(r'class="[^"]*sub-title', T))
check("无 Tailwind 污染", cnt(r'class="[^"]*\b(?:w-|h-|p-|m-|flex|grid-cols|text-|bg-)[^"]*"') == 0)
check("</style> 在1500-1800行", 1500 <= html[:html.index('</style>')].count('\n')+1 <= 1800, "行%d" % (html[:html.index('</style>')].count('\n')+1))
check("文件行数 3800±200", 3800 <= html.count('\n')+1 <= 4100, "%d行" % (html.count('\n')+1))

# ---------- 三、数据准确性 ----------
print("\n【三、数据准确性】")
check("占位符残留 = 0", len(re.findall(r'\{\{[^{}]+\}\}', html)) == 0, "%d" % len(re.findall(r'\{\{[^{}]+\}\}', html)))
check('"--" 缺失标记 = 0', len(re.findall(r'"--"', html)) + len(re.findall(r'>--<', html)) == 0)
check("暂无数据 = 0", html.count("暂无数据") == 0)

# 涨红跌绿 精确校验
spans = re.findall(r'<span class="([^"]*)">([\s\S]*?)</span>', html)
bad = []
for cls, inner in spans:
    txt = re.sub(r'<[^>]+>', '', inner).strip()
    hu = 'up' in cls and 'down' not in cls
    hd = 'down' in cls and 'up' not in cls
    if not (hu or hd): continue
    m = re.search(r'([+\-])\s*(\d+(?:\.\d+)?)\s*%', txt)
    if m:
        if hu and m.group(1) == '-': bad.append(("up含负", txt[:24]))
        if hd and m.group(1) == '+': bad.append(("down含正", txt[:24]))
    if hu and re.search(r'收跌|大跌|暴跌|净卖出|下挫|重挫', txt): bad.append(("up含跌词", txt[:24]))
    if hd and re.search(r'收涨|大涨|领涨|创新高|上扬|普涨', txt): bad.append(("down含涨词", txt[:24]))
check("涨红跌绿 无矛盾", len(bad) == 0, str(bad[:5]))

# ---------- 四、交互功能 ----------
print("\n【四、交互功能】")
check("switchTab 函数完整", "function switchTab" in html)
check("含滚动到顶部", "scrollTo" in html)

# ---------- 五、必查内容 ----------
print("\n【五、必查内容：四区字数≥120】")
areas = []
for i in range(1,7):
    k=f"机构{i}_观点"; areas.append((k, len(c(D[k]))))
for i in range(1,7):
    k=f"操作建议{i}_补充"; areas.append((k, len(c(D[k]))+len(c(D[f"操作建议{i}_内容"]))))
for k in ["高股息_银行内容","高股息_银行中报内容","高股息_央企内容","高股息_电力内容","高股息_公用事业内容"]:
    areas.append((k, len(c(D[k]))))
for name,l in areas:
    check(name+" ≥120字", l>=120, "%d字"%l)

print("\n【五、社区话题格式】")
for i in range(1,6):
    title=D.get(f"社区话题{i}_标题","")
    isq = ("？" in title or "?" in title)
    roles = all(D.get(f"社区话题{i}_观点{j}","") for j in (1,2,3)) and D.get(f"社区话题{i}_观点","")
    hl = sum(len(re.findall(r'<span', D[f"社区话题{i}_观点{j}"])) for j in (1,2,3))
    check(f"话题{i} 问句+三角色+老盛+高亮(≥4)", isq and roles and hl>=4, "问句=%s 三角色+老盛=%s 高亮=%d"%(isq, bool(roles), hl))

# ---------- 六、数据完整性（16标的） ----------
print("\n【六、关注标的(16)完整性】")
miss=0
for i in range(1,17):
    code=D.get(f"标的{i}_代码",""); price=D.get(f"标的{i}_股价",""); chg=D.get(f"标的{i}_涨跌幅","")
    if not(code and price and chg): miss+=1
check("16标的 代码/价格/涨跌幅 齐全", miss==0, "缺失%d"%miss)

# 关键指数一致性
print("\n【六、关键指数一致性】")
sz = c(D.get("A股_上证指数_数据",""))
check("上证指数含 8/31 收盘值", "3986.30" in sz and "+0.86%" in sz, sz[:30])

print("\n" + ("=" * 60))
print("总判定:", "全部通过 ✅" if ok else "存在未通过项 ❌")
print("=" * 60)
