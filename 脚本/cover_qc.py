#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按 规则/报告质量检查.md 的 2.3(逐Tab高亮密度)/3.1(标签语义)/3.2(数据标注日期) 做逐项核查。
   作为 qc_check.py + deep_qc.py 的补充，确保规范每一条都有对应检查。
   用法: python 脚本/cover_qc.py 老盛早知道_YYYYMMDD.html
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TARGET = sys.argv[1] if len(sys.argv) > 1 else "老盛早知道_20260902.html"
HTML = open(os.path.join(ROOT, TARGET), encoding="utf-8").read()
TPL = open(os.path.join(ROOT, "规则", "template.html"), encoding="utf-8").read()

RED, GREEN = "#f85149", "#3fb950"

def hl(b):
    return len(re.findall(r'<span style="color:', b))

# ---- 切分 tab-panel（按模板结构顺序 Tab0..Tab7）----
starts = [m.start() for m in re.finditer(r'<div[^>]*class="[^"]*tab-panel[^"]*"', HTML)]
tabs = []
for i, s in enumerate(starts):
    e = starts[i + 1] if i + 1 < len(starts) else len(HTML)
    tabs.append(HTML[s:e])

def card_bodies(t):
    cs = [m.start() for m in re.finditer(r'<div class="card-body', t)]
    out = []
    for j, s2 in enumerate(cs):
        e2 = cs[j + 1] if j + 1 < len(cs) else len(t)
        out.append(t[s2:e2])
    return out

def chk(name, cond, detail=""):
    print("  %s %s  %s" % ("PASS" if cond else "FAIL", name, detail))

print("=" * 64)
print("规范 2.3 逐 Tab 高亮密度 / 内容覆盖核查")
print("=" * 64)
print("tab-panel 数量: %d（规范期望 8）%s" % (len(tabs), "OK" if len(tabs) == 8 else "异常"))

# Tab0 首页概览：summary-card + 时间线 + 要点速览（组件结构，不用 card-body）
t0 = tabs[0] if len(tabs) > 0 else ""
summ = len(re.findall(r'class="[^"]*summary-card[^"]*"', t0))
tl = len(re.findall(r'class="[^"]*timeline-item[^"]*"', t0))
t0_hl = len(re.findall(r'<span style="color:', t0))
chk("Tab0 summary-card数量(期望≥4)", summ >= 4, "实际 %d" % summ)
chk("Tab0 时间线存在", tl >= 1, "实际 %d" % tl)
chk("Tab0 要点速览高亮充足(总高亮≥20)", t0_hl >= 20, "Tab0 总高亮 %d" % t0_hl)

# Tab1 新闻：每张≥5
t1 = tabs[1] if len(tabs) > 1 else ""
c1 = card_bodies(t1)
h1 = [hl(c) for c in c1]
low1 = [i + 1 for i, n in enumerate(h1) if n < 5]
chk("Tab1 新闻卡数量", len(c1) >= 1, "实际 %d" % len(c1))
chk("Tab1 每张新闻卡≥5处高亮", len(low1) == 0, "高亮分布=%s 未达标:%s" % (h1, low1))

# Tab2 AI：每张≥5；生物医学4张
t2 = tabs[2] if len(tabs) > 2 else ""
c2 = card_bodies(t2)
h2 = [hl(c) for c in c2]
low2 = [i + 1 for i, n in enumerate(h2) if n < 5]
bio_kw = ["生物医学", "脑机接口", "国产替代", "医疗设备", "就业趋势"]
bio_hits = sum(len(re.findall(k, t2)) for k in bio_kw)
chk("Tab2 AI卡数量", len(c2) >= 1, "实际 %d" % len(c2))
chk("Tab2 每张AI卡≥5处高亮", len(low2) == 0, "高亮分布=%s 未达标:%s" % (h2, low2))
chk("Tab2 生物医学板块覆盖", bio_hits >= 4, "关键词命中 %d 处" % bio_hits)

# Tab3 全球市场：8个market-block + 综评4维度(每维度≥3高亮，按真实标题定位)
t3 = tabs[3] if len(tabs) > 3 else ""
mb = len(re.findall(r'class="[^"]*market-block[^"]*"', t3))
chk("Tab3 market-block数量(期望8)", mb == 8, "实际 %d" % mb)
# 综评维度卡不用 card-body，改用 g_data1 真实标题在 Tab3 综评区定位切分
import importlib.util
_spec = importlib.util.spec_from_file_location("g1qc", os.path.join(HERE, "g_data1.py"))
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
_dtitles = [_m.D.get("综评_A股行情标题", ""), _m.D.get("综评_外围市场标题", ""),
            _m.D.get("综评_地缘政策标题", ""), _m.D.get("综评_风险事件标题", "")]
_b = t3.find("市场综评")
# 窗口需覆盖整段综评：4 张维度卡 + 每卡 3 段正文，实测约 1.0-1.2 万字符，
# 旧值 6000 会把第 4 张「风险」卡切在窗外，误报"维度缺失"。
_zone = t3[_b:_b + 20000] if _b >= 0 else ""
_pos = sorted([(t, _zone.find(t)) for t in _dtitles if t and _zone.find(t) >= 0], key=lambda x: x[1])
_dims_hl = []
for i, (t, p) in enumerate(_pos):
    nxt = _pos[i + 1][1] if i + 1 < len(_pos) else len(_zone)
    _dims_hl.append((t[:10], len(re.findall(r'<span style="color:', _zone[p:nxt]))))
chk("Tab3 市场综评4维度齐全", len(_pos) == 4, "缺:%s" % [t for t in _dtitles if t not in [x[0] for x in _pos]])
low3 = [t for t, h in _dims_hl if h < 3]
chk("Tab3 综评每维度≥3处高亮", len(low3) == 0, "分布:%s" % _dims_hl)

# Tab4 价值投资风向：机构观点/深度解读高亮
t4 = tabs[4] if len(tabs) > 4 else ""
c4 = card_bodies(t4)
h4 = [hl(c) for c in c4]
low4 = [i + 1 for i, n in enumerate(h4) if n < 2]
chk("Tab4 机构/深度解读卡≥2处高亮", len(low4) == 0, "高亮分布=%s 未达标:%s" % (h4, low4))

# Tab5 关注标的：16 stock-card + 深度解读汇总卡（组件结构，用 stock-change/stock-bullets 着色）
t5 = tabs[5] if len(tabs) > 5 else ""
sc = len(re.findall(r'class="[^"]*stock-card[^"]*"', t5))
deep = "深度解读" in t5
color_cls = len(re.findall(r'class="[^"]*stock-change[^"]*"', t5)) + len(re.findall(r'class="[^"]*stock-bullets[^"]*"', t5))
chk("Tab5 stock-card数量(期望16)", sc == 16, "实际 %d" % sc)
chk("Tab5 深度解读汇总卡存在", deep, "")
chk("Tab5 个股涨跌着色(涨跌class/要点)存在", color_cls >= 16, "着色元素 %d" % color_cls)

# Tab6 理财：每卡2-4处(取≥2)；grid-4 + 多个板块覆盖
t6 = tabs[6] if len(tabs) > 6 else ""
c6 = card_bodies(t6)
h6 = [hl(c) for c in c6]
low6 = [i + 1 for i, n in enumerate(h6) if n < 2]
sec6 = ["避坑", "保险", "黄金", "债券", "社区热门话题", "高股息替代", "稳健理财"]
miss6 = [k for k in sec6 if k not in t6]
chk("Tab6 理财卡≥2处高亮", len(low6) == 0, "高亮分布=%s 未达标:%s" % (h6, low6))
chk("Tab6 板块覆盖", len(miss6) == 0, "缺失:%s" % miss6)

# Tab7 今日总结：非数据展示卡每张≥2高亮（关键数字速查为数据卡，豁免）
t7 = tabs[7] if len(tabs) > 7 else ""
c7 = card_bodies(t7)
h7 = [hl(c) for c in c7]
low7 = [i + 1 for i, c in enumerate(c7) if hl(c) < 2 and not ("收盘·" in c or "mq-item" in c or "数字速查" in c)]
chk("Tab7 非数据卡≥2处高亮", len(low7) == 0, "高亮分布=%s 未达标:%s" % (h7, low7))

print()
print("=" * 64)
print("规范 3.1 标签语义核查（利好/涨→红，利空/跌→绿）")
print("=" * 64)
# 找带语义的标签：领涨/大涨/创新高 标签应为红色系；净流出/大跌/暴跌 应为绿色系
POS_TAG = ["领涨", "大涨", "创新高", "走强", "利好"]
NEG_TAG = ["净流出", "大跌", "暴跌", "承压", "走弱", "利空"]
# 语境豁免：字面含利空词（"走弱/回落"）但整体表达的是利好 → 染红正确，不算矛盾
CTX_EXEMPT = ["美元走弱", "美元指数回落", "美元回落", "相对受益", "加息预期", "加息的押注"]


def enclosing_span_text(s, pos):
    """取包住 pos 的那个颜色 span 的纯文本，用于语境豁免判定。"""
    head = s[:pos]
    so = head.rfind('<span style="color:')
    if so < 0:
        return ""
    end = s.find("</span>", pos)
    return re.sub(r"<[^>]+>", "", s[so:end]) if end > 0 else ""


def enclosing_color(s, pos):
    """返回覆盖 pos 的「最内层」<span style="color:..."> 色值；未被 span 包裹则返回 None。

    旧实现用「前 60 字符内是否出现某颜色/最近两个 class」做判定，会把相邻高亮的颜色
    张冠李戴（例：<red>净流入</red>；<green>净流出</green> 会把 green 段误判成“利空误用红”）。
    改为回溯找最后一个未闭合的颜色 span，只认真正包住关键词的那一个。
    """
    head = s[:pos]
    so = head.rfind('<span style="color:')
    sc = head.rfind('</span>')
    if so > sc:
        mm = re.match(r'<span style="color:(#[0-9a-fA-F]{6})', head[so:])
        if mm:
            return mm.group(1).lower()
    return None


bad_tag = []
for kw in POS_TAG + NEG_TAG:
    for m in re.finditer(re.escape(kw), HTML):
        col = enclosing_color(HTML, m.start())
        if col is None:
            continue  # 未被着色（纯文本/中性），不做方向判定
        # 语境豁免：字面含利空词("走弱/回落")但整体表达的是利好 → 染红正确。
        # 与 deep_qc 的 EXEMPT_POS 保持同一口径（例："美元走弱"对金银与加密货币是利好）。
        if any(x in enclosing_span_text(HTML, m.start()) for x in CTX_EXEMPT):
            continue
        is_pos = kw in POS_TAG
        if is_pos and col == GREEN.lower():
            bad_tag.append(("利好误用绿", kw))
        if (not is_pos) and col == RED.lower():
            bad_tag.append(("利空误用红", kw))
chk("标签语义方向正确", len(bad_tag) == 0, "异常:%s" % bad_tag[:6])

print()
print("=" * 64)
print("规范 3.2 数据标注日期核查")
print("=" * 64)
# market-block 含日期：数据日从当期数据层动态取，禁止硬编码上期日期
DATA_DATE = str(_m.D.get("市场综评_日期", "")).strip()
if not DATA_DATE:
    import datetime as _dt
    DATA_DATE = (_dt.date.today() - _dt.timedelta(days=1)).strftime("%Y-%m-%d")
mb_date = re.findall(r'class="[^"]*market-block[^"]*"[\s\S]{0,250}?%s' % DATA_DATE, HTML)
chk("8大市场块均标注数据日期", len(mb_date) == 8, "命中 %d/8 (数据日 %s)" % (len(mb_date), DATA_DATE))
# 关键指数是否带收盘日标注（market-name 附近有日期）
has_close = HTML.count("收盘") + HTML.count(DATA_DATE)
chk("报告含数据日期标注(%s)" % DATA_DATE, DATA_DATE in HTML, "出现 %d 次" % HTML.count(DATA_DATE))

print()
print("=" * 64)
ALL_OK = True
print("（FAIL 项见上方明细）")
