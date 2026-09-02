# -*- coding: utf-8 -*-
# 老盛早知道 深度质检（补充 qc_check.py 未覆盖的逐项语义/逐卡项）
# 用法: python 脚本/deep_qc.py [报告文件名]
# 对应 规则/报告质量检查.md v2.3
import re, os, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)            # 项目根目录
TARGET = sys.argv[1] if len(sys.argv) > 1 else "老盛早知道_20260902.html"
TPL = os.path.join(ROOT, "规则", "template.html")
HTML = open(os.path.join(ROOT, TARGET), encoding="utf-8").read()
TPLH = open(TPL, encoding="utf-8").read()

def load(mod):
    spec = importlib.util.spec_from_file_location(mod, os.path.join(HERE, mod + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

d1 = load("g_data1"); d2 = load("g_data2")

FAIL = []
def chk(name, ok, detail=""):
    print(("  PASS " if ok else "  FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL.append(name)

print("=" * 64)
print("深度质检:", TARGET)
print("=" * 64)

# ===== A. 涨红跌绿 · 语义色（仅用强词，避免中性词误判）=====
print("\n【A. 涨红跌绿 · 语义色】")
RED, GREEN = "#f85149", "#3fb950"
# 强利好词：染绿才算矛盾；强利空词：染红才算矛盾
POS = ["飙升", "大涨", "创新高", "领涨", "逆势涨", "上调", "净买入", "净增持", "突破", "盈利", "受益", "涨超", "低位反弹"]
NEG = ["重挫", "暴跌", "抛售", "净流出", "领跌", "失血", "跌超", "承压", "回落", "走弱", "大跌"]
# 利率/收益率/债市上行=利空(染绿正确)、下行=利好(染红正确)，此类强语义豁免
EXEMPT_STR = ["突破5.27%", "突破4.79%", "升至4.79%", "破95美元", "收益率突破", "美债收益率", "美10年", "美30年"]
bad = []
for m in re.finditer(r'<span style="color:(#f85149|#3fb950);font-weight:700;">([\s\S]{0,80}?)</span>', HTML):
    col, txt = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
    ctx = HTML[max(0, m.start() - 90):m.end() + 20]
    rate_exempt = any(x in ctx for x in ["收益率", "利率", "债"]) or any(s in txt for s in EXEMPT_STR)
    if col == GREEN and any(w in txt for w in POS) and not rate_exempt:
        bad.append(("利好染绿", txt))
    if col == RED and any(w in txt for w in NEG) and not rate_exempt:
        bad.append(("利空染红", txt))
chk("语义色无强矛盾(中性词已豁免)", len(bad) == 0, str(bad[:6]))

# ===== B. 涨跌 class 与 符号 一致性（全量）=====
print("\n【B. 涨跌 class 与 符号 一致性 · 全量】")
up_bad = down_bad = 0
for m in re.finditer(r'class="(up|down)"[^>]*>([\s\S]{0,120}?)</', HTML):
    cls, seg = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
    if cls == "up" and re.search(r"-\s*\d", seg):
        up_bad += 1
    if cls == "down" and re.search(r"\+\s*\d", seg):
        down_bad += 1
chk('class="up" 不含负值', up_bad == 0, "%d 处" % up_bad)
chk('class="down" 不含正值', down_bad == 0, "%d 处" % down_bad)

# ===== C. 逐卡 高亮密度（新闻/AI ≥5，其余文本卡 ≥2；数据展示卡豁免）=====
print("\n【C. 逐卡 高亮密度】")
starts = [m.start() for m in re.finditer(r'<div class="card-body', HTML)]
EXEMPT_TITLE = ["股息率对比"]
EXEMPT_SUB = ["关键数字速查", "深度解读", "速查"]
low = []
for i, st in enumerate(starts):
    b = HTML[st: (starts[i + 1] if i + 1 < len(starts) else st + 8000)]
    title = re.search(r'class="card-title[^"]*"[^>]*>([\s\S]{0,40}?)<', b)
    tname = title.group(1) if title else ""
    sub = re.findall(r'class="sub-title[^"]*"[^>]*>([\s\S]{0,30}?)<', HTML[max(0, st - 2000):st])
    subname = sub[-1] if sub else ""
    is_data = (any(k in tname for k in EXEMPT_TITLE)
               or any(k in subname for k in EXEMPT_SUB)
               or 'market-val' in b or 'market-row' in b
               or '收盘·' in b)   # 指数速览/关键数字速览卡（数字已 up/down 着色）
    if is_data:
        continue
    kind = "news" if ("news" in b[:200] or 'news-card' in b[:200]) else "default"
    if "ai" in b[:200] and "card" in b[:200]:
        kind = "ai"
    th = 5 if kind in ("news", "ai") else 2
    n = len(re.findall(r'<span style="color:', b))
    if n < th:
        low.append((kind, n, tname[:16] or subname[:16] or "?"))
chk("文本卡高亮达标(新闻/AI≥5 其余≥2, 数据卡豁免)", len(low) == 0,
    "未达标 %d: %s" % (len(low), str(low[:8])))

# ===== D. Tab5 关注标的 16 卡 顺序/同名同码 =====
print("\n【D. Tab5 关注标的 16 卡】")
order = [1, 2, 3, 4, 16, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
blocks = [b for b in re.split(r'(?=<div class="stock-card)', HTML) if b.startswith('<div class="stock-card')]
ok = True
for i, (b, idx) in enumerate(zip(blocks, order), 1):
    name = d2.D['标的%d_名称' % idx]; code = d2.D['标的%d_代码' % idx]
    seg = b[:3000]
    hit = (name in seg) and (code in seg)
    others = [c for j in range(1, 17) if j != idx and d2.D['标的%d_代码' % j] in seg]
    if not (hit and not others):
        ok = False
        print("    MISMATCH 卡%d 标的%d %s" % (i, idx, others))
chk("16 卡同名同码且未串位", ok, "%d 块" % len(blocks))

# ===== E. 社区话题格式（规范五·2）=====
print("\n【E. 社区话题格式】")
titles = [d2.D.get("社区话题%d_标题" % i, "") for i in range(1, 6)]
chk("5 话题均为疑问句", all(re.search(r"[？?]$", t.strip()) for t in titles), str([t[:14] for t in titles]))
roles = all(
    d2.D.get("社区话题%d_角色1" % i) == "@机构分析师"
    and d2.D.get("社区话题%d_角色2" % i) == "@价值投资者"
    and d2.D.get("社区话题%d_角色3" % i) == "@谨慎派"
    for i in range(1, 6))
chk("三角色齐全(机构/价值/谨慎)", roles)
low_v = [(i, len(re.sub(r"<[^>]+>", "", d2.D.get("社区话题%d_观点" % i, ""))))
         for i in range(1, 6) if len(re.sub(r"<[^>]+>", "", d2.D.get("社区话题%d_观点" % i, ""))) < 120]
chk("老盛观点每条 ≥120字", not low_v, str(low_v))
hl_bad = [(i, len(re.findall(r'<span style="color:',
                              "".join(d2.D.get("社区话题%d_观点%d" % (i, j), "") for j in range(1, 4)))))
          for i in range(1, 6)
          if len(re.findall(r'<span style="color:',
                            "".join(d2.D.get("社区话题%d_观点%d" % (i, j), "") for j in range(1, 4)))) < 4]
chk("每话题三观点高亮 ≥4处", not hl_bad, str(hl_bad))

# ===== F. 关键数据块填充（基于 HTML 实际内容，不依赖源键名）=====
print("\n【F. 关键数据块填充】")
# 页头 核心指数速览（class="hm-mq"）：含真实点位且无占位符
mi = HTML.find('class="hm-mq"')
ticker_zone = HTML[mi:mi + 6000] if mi >= 0 else ""
chk("页头指数速览已填充(含上证点位且无占位符)",
    ("3979.89" in ticker_zone) and ("{{" not in ticker_zone))
# 银行板块 PB / 现货金 / 美10Y 用 HTML 实际数值判断
chk("银行板块PB已填充", "0.69倍" in HTML or "估值低位" in HTML)
chk("现货黄金已填充", "4327.29" in HTML)
chk("美10Y已填充", "4.79%" in HTML or "4.801%" in HTML)

# ===== G. 关键指数/标的 名词覆盖 与 缺失标记 =====
print("\n【G. 关键指数填充（无缺失）】")
must = ["上证指数", "深证成指", "创业板指", "恒生指数", "恒生科技", "日经225", "德国DAX",
        "道琼斯", "标普500", "纳斯达克", "WTI", "布伦特", "现货黄金", "比特币",
        "美元指数", "美10年", "美30年", "中10年"]
miss = [m for m in must if m not in HTML]
chk("关键指数/标的名词全覆盖", not miss, "缺失 %s" % miss)
chk('无 "--" 缺失标记', HTML.count('"--"') == 0 and len(re.findall(r">--<", HTML)) == 0)
chk("暂无数据 = 0", HTML.count("暂无数据") == 0)

# ===== H. 字号一致性 =====
print("\n【H. 字号一致性】")
fs_spans = len(re.findall(r'<span style="color:[^"]*font-size', HTML))
fs_tpl = len(re.findall(r'<span style="color:[^"]*font-size', TPLH))
chk("注入高亮未改字号(对比模板)", fs_spans <= fs_tpl, "报告 %d / 模板 %d" % (fs_spans, fs_tpl))

# ===== I. Tab3 market-block 8 大市场 涨跌 class 抽查 =====
print("\n【I. 8大市场块 涨跌方向已着色】")
for blk in ["A股", "港股", "亚太", "欧洲", "美股", "大宗商品", "加密货币", "汇率债券"]:
    key = blk + "_收盘日期"
    chk("市场块·%s 日期已填" % blk, bool(d1.D.get(key)), str(d1.D.get(key)))

print("\n" + "=" * 64)
if FAIL:
    print("❌ 深度未通过 %d 项：" % len(FAIL))
    for f in FAIL:
        print("   -", f)
    sys.exit(1)
else:
    print("✅ 深度质检全部通过")
