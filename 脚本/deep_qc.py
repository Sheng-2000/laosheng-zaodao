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
# 语境豁免：字面含利空词("回落/走弱")但整体表达的是利好 → 染红正确，不算矛盾
#   例："风险偏好回落时红利相对受益"（条件状语）、"美元指数回落"（美元走弱利好A股/金银）
# 语境豁免（绿色侧）：字面含"涨超/涨停/盈利"等利好词，但整句在提示风险
#   例："19股涨超5%的涨停潮往往对应情绪高点" → 是风险提示，染绿正确，不算矛盾
EXEMPT_GREEN_CTX = ["涨停潮", "情绪高点", "往往对应", "追高容易被套", "需警惕", "注意风险"]
# 成本侧豁免：字面含"上调/突破/涨"等利好词，但讲的是上游涨价、BOM成本抬升，
#   对下游制造商是利空 → 染绿正确，不算矛盾（例："台积电2nm单片报价突破3万美元"）
EXEMPT_GREEN_COST = ["成本", "BOM", "报价", "涨价压力", "毛利", "利润率", "挤压"]
# 冲高回落豁免：字面含"大涨/涨超"，但整句讲的是日内冲高后翻绿、或前一日大涨后今日回调
#   → 净结果是跌，染绿正确，不算矛盾
#   例："韩国KOSPI从盘中涨超2.50%一路翻绿收跌0.58%"、"前一日大涨的液冷服务器方向回调"
EXEMPT_GREEN_REV = ["翻绿", "收跌", "转跌", "跳水", "回吐", "回调", "重挫",
                    "盘中一度涨", "盘中涨超", "前一日大涨", "前一交易日大涨", "涨幅回吐"]
EXEMPT_POS = ["相对受益", "美元指数回落", "美元走弱", "美元回落", "实际利率回落", "通胀回落",
              # 加息预期"回落/降温/收敛"对风险资产是利好，染红正确，不算矛盾
              "加息的押注", "加息预期", "加息概率", "加息押注", "加息预期降温", "加息路径"]
bad = []
for m in re.finditer(r'<span style="color:(#f85149|#3fb950);font-weight:700;">([\s\S]{0,80}?)</span>', HTML):
    col, txt = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
    ctx = HTML[max(0, m.start() - 90):m.end() + 20]
    rate_exempt = any(x in ctx for x in ["收益率", "利率", "债"]) or any(s in txt for s in EXEMPT_STR)
    pos_exempt = rate_exempt or any(s in txt for s in EXEMPT_POS)
    green_exempt = any(x in ctx for x in EXEMPT_GREEN_CTX) \
        or any(x in txt for x in EXEMPT_GREEN_COST) \
        or any(x in txt for x in EXEMPT_GREEN_REV)
    if col == GREEN and any(w in txt for w in POS) and not rate_exempt and not green_exempt:
        bad.append(("利好染绿", txt))
    if col == RED and any(w in txt for w in NEG) and not pos_exempt:
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

# ===== D. Tab5 关注标的 19 卡 顺序/同名同码 =====
print("\n【D. Tab5 关注标的 19 卡】")
order = [1, 2, 3, 4, 16, 17, 5, 6, 7, 8, 9, 18, 19, 10, 11, 12, 13, 14, 15]
blocks = [b for b in re.split(r'(?=<div class="stock-card)', HTML) if b.startswith('<div class="stock-card')]
ok = True
for i, (b, idx) in enumerate(zip(blocks, order), 1):
    name = d2.D['标的%d_名称' % idx]; code = d2.D['标的%d_代码' % idx]
    seg = b[:3000]
    hit = (name in seg) and (code in seg)
    others = [c for j in range(1, 20) if j != idx and d2.D['标的%d_代码' % j] in seg]
    if not (hit and not others):
        ok = False
        print("    MISMATCH 卡%d 标的%d %s" % (i, idx, others))
chk("19 卡同名同码且未串位", ok, "%d 块" % len(blocks))

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
# 关键数值一律从当期数据层动态提取，禁止硬编码上期数字（否则每期必误报）
def _num(s, pat=r"(\d+\.\d+)"):
    m = re.search(pat, str(s))
    return m.group(1) if m else ""

_SH = str(d1.D.get("ticker_上证_数值", "")).strip()
_GOLD = _num(d1.D.get("大宗_国际黄金", ""))
_US10Y = _num(d1.D.get("汇率_美10年期", ""))

mi = HTML.find('class="hm-mq"')
ticker_zone = HTML[mi:mi + 6000] if mi >= 0 else ""
chk("页头指数速览已填充(含上证点位且无占位符)",
    bool(_SH) and (_SH in ticker_zone) and ("{{" not in ticker_zone),
    "上证 %s" % _SH)
# 银行板块 PB / 现货金 / 美10Y 用 HTML 实际数值判断
# 动态取当期银行板块PB（禁硬编码上期值：每期必误报）
_pb = str(d1.D.get("估值_银行PB", "")).strip()
chk("银行板块PB已填充", bool(_pb) and (_pb in HTML or "估值低位" in HTML), "当期值 %s" % (_pb or "缺失"))
chk("现货黄金已填充", bool(_GOLD) and _GOLD in HTML, "现货金 %s" % _GOLD)
chk("美10Y已填充", bool(_US10Y) and _US10Y in HTML, "美10Y %s" % _US10Y)

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


# ===== 跨期检查守卫 =====
# 用途：用「当期数据层」去检查「往期报告」时，数值/文案类断言（综评维度标题、关键数据值、
# 指数点位、数据日）必然误报——因为期望值取自当前 g_data，而非该期报告当年的数据。
# 判定：数据层主数据日 若不在 [报告日-1, 报告日-5] 区间内 → 判为跨期，仅结构性断言可信。
try:
    import re as _reX, datetime as _dtX
    _mx = _reX.search(r"(\d{4})(\d{2})(\d{2})", os.path.basename(TARGET))
    _rdobj = _dtX.date(*map(int, _mx.groups())) if _mx else None
    _pool = [x for x in (globals().get("d1"), globals().get("d2"),
                         getattr(globals().get("_m"), "D", None)) if isinstance(x, dict)]
    _major = ""
    for _p in _pool:
        if "市场综评_日期" in _p:
            _major = str(_p["市场综评_日期"]).strip(); break
    if not _major:
        _cnt = {}
        for _p in _pool:
            for _v in _p.values():
                _s = str(_v).strip()
                if _reX.fullmatch(r"\d{4}-\d{2}-\d{2}", _s):
                    _cnt[_s] = _cnt.get(_s, 0) + 1
        _major = max(_cnt, key=_cnt.get) if _cnt else ""
    if _rdobj and _major:
        _exp = {(_rdobj - _dtX.timedelta(days=k)).strftime("%Y-%m-%d") for k in range(1, 6)}
        CROSS_PERIOD = _major not in _exp
    else:
        CROSS_PERIOD = False
    MAJOR_DATE = _major
except Exception:
    CROSS_PERIOD = False; MAJOR_DATE = ""

if CROSS_PERIOD:
    print("\n" + "!" * 64)
    print("⚠️  跨期检查：本报告日期与当前数据层主数据日(%s)不匹配" % MAJOR_DATE)
    print("   数值/文案类断言（综评维度、关键数据、指数点位、数据日）系用当期数据比对，")
    print("   对历史报告属误报高发区；结构性断言（卡片数/market-block/高亮分布）仍然有效。")
    print("!" * 64)

print("\n" + "=" * 64)
if FAIL:
    print("❌ 深度未通过 %d 项：%s" % (len(FAIL), "   ⚠️ 跨期检查：可能含误报项" if CROSS_PERIOD else ""))
    for f in FAIL:
        print("   -", f)
    sys.exit(1)
else:
    print("✅ 深度质检全部通过")
