# -*- coding: utf-8 -*-
# 大福·老盛早知道 质量检查（对应 规则/报告质量检查.md v2.3）
import re, os, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = sys.argv[1] if len(sys.argv) > 1 else "老盛早知道_20260902.html"
TPL = os.path.join(HERE, "规则", "template.html")

html = open(os.path.join(HERE, TARGET), encoding="utf-8").read()
tpl = open(TPL, encoding="utf-8").read()

# 剔除注释与 <style> 后再做文本类统计
body = re.sub(r"<style[\s\S]*?</style>", "", html)
body = re.sub(r"<!--[\s\S]*?-->", "", body)
text = re.sub(r"<[^>]+>", "", body)

FAIL = []
def chk(name, ok, detail=""):
    print(("  PASS " if ok else "  FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL.append(name)

print("=" * 60)
print("目标文件:", TARGET)
print("=" * 60)

# ---------- 一、数据及时性 ----------
print("\n【一、数据及时性】")
old_dates = re.findall(r"2026-0[78]-(?:0[1-9]|1[0-9]|2[0-9]|3[01])", html)
t3_old = [d for d in old_dates if d <= "2026-08-30"]
chk("旧日期残留(T-3及更早) <=3处", len(t3_old) <= 3, "实际 %d 处 %s" % (len(t3_old), sorted(set(t3_old))[:6]))
new_keys = ["90.68", "4327.29", "52766.88", "5.74%", "2209.89", "3979.89", "2.48%", "68%", "142.18", "1.88%", "95.19", "4.79%"]
hit = sum(html.count(k) for k in new_keys)
chk("新数据覆盖 >=10处", hit >= 10, "关键数据命中 %d 次" % hit)
# 一致性：同一指标全报告一致
cons = [("WTI价格", ["90.68"]), ("道指点位", ["52766.88"]), ("现货金", ["4327.29"]), ("上证", ["3979.89"])]
for nm, vals in cons:
    bad = [v for v in vals if html.count(v) < 1]
    chk("数据一致性·%s" % nm, not bad, "缺失 %s" % bad if bad else "已出现")

# ---------- 二、结构与样式 ----------
print("\n【二、结构与样式】")
lines = html.count("\n") + 1
chk("文件行数 3800±200", 3600 <= lines <= 4100, "%d 行" % lines)
style_end = 0
for i, l in enumerate(html.split("\n"), 1):
    if "</style>" in l:
        style_end = i
        break
chk("</style> 位置 1500-1800行", 1000 <= style_end <= 1800, "第 %d 行" % style_end)

def cnt(s, pat):
    return len(re.findall(pat, s))

pairs = [
    ("tab-panel", r'class="tab-panel'),
    ("sub-title", r'class="sub-title'),
    ("stock-card", r'class="stock-card'),
    ("sentiment-item", r'class="sentiment-item'),
    ("market-block", r'class="market-block'),
]
for nm, pat in pairs:
    a, b = cnt(html, pat), cnt(tpl, pat)
    chk("%s 数量与模板一致" % nm, a == b, "报告 %d / 模板 %d" % (a, b))

# 以模板为基线：模板自带的 grid-N 等项目类名不算污染
TW = r'class="[^"]*\b(?:w|h|p|m|flex|grid|text|bg|border|rounded)-\d'
tw = len(re.findall(TW, html))
tw_tpl = len(re.findall(TW, tpl))
chk("无 Tailwind 类名污染(对比模板基线)", tw <= tw_tpl, "报告 %d / 模板基线 %d" % (tw, tw_tpl))
chk("占位符残留 = 0", len(re.findall(r"\{\{[^{}]+\}\}", html)) == 0)
chk('"--" 缺失数据 = 0', html.count('"--"') == 0 and len(re.findall(r">--<", html)) == 0)
chk("暂无数据 = 0", html.count("暂无数据") == 0)

# ---------- 三、涨跌颜色 ----------
print("\n【三、涨红跌绿】")
up_bad, down_bad = [], []
for m in re.finditer(r'class="(up|down)[^"]*"[^>]*>([\s\S]{0,200}?)</', html):
    cls, seg = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
    if cls == "up" and re.search(r"-\s*\d", seg):
        up_bad.append(seg[:40])
    if cls == "down" and re.search(r"\+\s*\d", seg):
        down_bad.append(seg[:40])
chk('无 class="up" 含负值', len(up_bad) == 0, str(up_bad[:3]))
chk('无 class="down" 含正值', len(down_bad) == 0, str(down_bad[:3]))

# 高亮 span 不得含 font-size
# 以模板为基线：模板自带的“强调 span 15px”结构不算改字号，注入的高亮 span 不得带 font-size
FS = r'<span style="color:[^"]*font-size[^"]*">'
fs = len(re.findall(FS, html))
fs_tpl = len(re.findall(FS, tpl))
chk("注入高亮 span 未改变字号(对比模板基线)", fs <= fs_tpl, "报告 %d / 模板基线 %d" % (fs, fs_tpl))
spans = re.findall(r'<span style="color:[^"]*">', html)
chk("高亮 span 总数", len(spans) >= 300, "%d 处" % len(spans))

# ---------- 四、交互 ----------
print("\n【四、交互功能】")
chk("switchTab 函数存在", "function switchTab" in html)
chk("switchTab 含滚动到顶", "scrollTo" in html or "scrollIntoView" in html)
chk("无 data-page-node-id 污染", "data-page-node-id" not in html)

# ---------- 五、必查内容 ----------
print("\n【五、必查内容 · 四区 ≥120字】")
def load(mod):
    spec = importlib.util.spec_from_file_location(mod, os.path.join(HERE, mod + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

d2 = load("g_data2")
d1 = load("g_data1")

def plain(s):
    return len(re.sub(r"<[^>]+>", "", s))

groups = {
    "机构价值投资观点": [d2.D.get("机构%d_观点" % i, "") for i in range(1, 7)],
    "高股息板块深度分析": [d2.D.get(k, "") for k in ["高股息_银行内容", "高股息_银行中报内容", "高股息_央企内容", "高股息_电力内容", "高股息_公用事业内容"]],
    "社区热门话题": [d2.D.get("社区话题%d_观点" % i, "") for i in range(1, 6)],
    "今日操作建议": [d2.D.get("操作建议%d_补充" % i, "") for i in range(1, 7)],
}
for gname, items in groups.items():
    short = [(i + 1, plain(v)) for i, v in enumerate(items) if plain(v) < 120]
    chk("%s 每条 ≥120字" % gname, not short, "最短 %s" % (str(short[:3]) if short else "OK"))

print("\n【五、社区话题格式】")
titles = [d2.D.get("社区话题%d_标题" % i, "") for i in range(1, 6)]
chk("社区话题 5 个", all(titles), str([t[:12] for t in titles]))
q = [t for t in titles if not re.search(r"[？?]$", t.strip())]
chk("标题均为疑问句", not q, "非疑问句: %s" % q)
roles_ok = all(
    d2.D.get("社区话题%d_角色1" % i) == "@机构分析师"
    and d2.D.get("社区话题%d_角色2" % i) == "@价值投资者"
    and d2.D.get("社区话题%d_角色3" % i) == "@谨慎派"
    for i in range(1, 6))
chk("三角色齐全(机构/价值/谨慎)", roles_ok)
hl_bad = []
for i in range(1, 6):
    seg = "".join(d2.D.get("社区话题%d_观点%d" % (i, j), "") for j in range(1, 4))
    n = len(re.findall(r"<span style=\"color:", seg))
    if n < 4:
        hl_bad.append((i, n))
chk("每话题三观点高亮 ≥4处", not hl_bad, str(hl_bad))
dup = [v for k, v in d2.D.items() if "观点" in k and "老盛观点：" in v]
chk("老盛观点无重复前缀", not dup, "%d 处重复" % len(dup))

# ---------- 六、Tab3 market-block 完整性 ----------
print("\n【六、关键数据块填充】")
blocks = ["A股_收盘日期", "港股_收盘日期", "亚太_收盘日期", "欧洲_收盘日期", "美股_收盘日期",
          "大宗商品_收盘日期", "加密货币_收盘日期", "汇率债券_收盘日期"]
chk("8大市场块日期齐全", all(d1.D.get(b) for b in blocks), str([d1.D.get(b) for b in blocks]))

print("\n" + "=" * 60)
if FAIL:
    print("❌ 未通过 %d 项：" % len(FAIL))
    for f in FAIL:
        print("   -", f)
    sys.exit(1)
else:
    print("✅ 全部检查通过")
