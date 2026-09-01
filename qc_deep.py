# -*- coding: utf-8 -*-
"""老盛早知道 深度质量检查（补充 qc_full.py 未覆盖项）
判定原则：与 template.html 对照，模板中同样存在的即为继承项，不算本次引入问题。
"""
import re, os
from collections import Counter

HTML = "老盛早知道_20260901.html"
TPL = "template.html"
html = open(HTML, encoding="utf-8").read()
tpl = open(TPL, encoding="utf-8").read()

res = []
def chk(name, ok, detail=""):
    res.append((ok, name, detail))

# ---------- 1. HTML 标签平衡 ----------
body = re.sub(r"<!--[\s\S]*?-->", "", html[html.index("<body"):])
for tag in ["div", "span", "ul", "li", "p", "nav", "section", "header", "footer", "main", "table", "tr", "td"]:
    o = len(re.findall(r"<" + tag + r"[\s>]", body))
    c = len(re.findall(r"</" + tag + r">", body))
    if o or c:
        chk(f"<{tag}> 开闭平衡", o == c, f"开{o} 闭{c}")

# ---------- 2. TAB 联动（用 panel-N 与 switchTab(N) 精确匹配）----------
btns = sorted(set(int(x) for x in re.findall(r"switchTab\((\d+)\)", html)))
panels = sorted(set(int(x) for x in re.findall(r'class="tab-panel[^"]*"\s+id="panel-(\d+)"', html)))
chk("TAB 按钮/面板数量=8", len(btns) == 8 and len(panels) == 8, f"按钮{btns} 面板{panels}")
chk("TAB 按钮与面板一一对应", btns == panels, "完全匹配" if btns == panels else f"不匹配 {btns} vs {panels}")
chk("switchTab 按 'panel-'+idx 匹配", ("'panel-' + idx" in html) or ("'panel-'+idx" in html), "")

# ---------- 3. 卡片高亮密度（平衡提取，数据展示卡豁免）----------
def balanced(text, start):
    depth = 0; i = start
    while i < len(text):
        m = re.compile(r"<div\b|</div>").search(text, i)
        if not m:
            break
        if m.group(0) == "</div>":
            depth -= 1
            if depth == 0:
                return text[start:m.end()]
            i = m.end()
        else:
            depth += 1; i = m.end()
    return text[start:start + 2000]

cards = [balanced(html, m.start()) for m in re.finditer(r'<div class="card[^"]*"[^>]*>', html)]
real = [cards[i] for i in range(0, len(cards), 3)]          # 每3个一层：整卡/标题/正文
EXEMPT = ["关注标的深度解读", "关键数字速查", "股息率对比"]     # 数据展示卡豁免
low = []
for i, c in enumerate(real, 1):
    n = len(re.findall(r'<span style="color:', c))
    title = re.search(r'class="card-title"[^>]*>([\s\S]*?)</div>', c)
    title = re.sub(r"<[^>]+>", "", title.group(1)).strip() if title else ""
    if n < 2 and not any(e in title for e in EXEMPT):
        low.append((i, title, n))
lst = [len(re.findall(r'<span style="color:', c)) for c in real]
chk(f"卡片高亮密度（{len(real)}卡，均值{sum(lst)/len(lst):.1f}）", not low,
    f"总数{sum(lst)} 最低{min(lst)}" + (f" 不足:{low}" if low else ""))

# ---------- 4. 高亮不改字号（与模板对照）----------
hl_fs_r = len(re.findall(r'<span style="color:[^"]*font-size', html))
hl_fs_t = len(re.findall(r'<span style="color:[^"]*font-size', tpl))
chk("高亮+字号数量与模板一致(继承项)", hl_fs_r == hl_fs_t, f"报告{hl_fs_r} 模板{hl_fs_t}")
fs_r = len(re.findall(r'<span style="font-size[^"]*"', html))
fs_t = len(re.findall(r'<span style="font-size[^"]*"', tpl))
chk("纯字号span与模板一致(继承项)", fs_r == fs_t, f"报告{fs_r} 模板{fs_t}")

# ---------- 5. 高亮颜色合规 ----------
colors = Counter(c.strip().lower() for c in re.findall(r'<span style="color:\s*([^;"]+)', html))
allowed = {"#f85149", "#3fb950", "#00d4ff", "#f0b429", "#ffa657", "#8b949e", "#e6edf3", "#c9d1d9"}
weird = {k: v for k, v in colors.items() if k not in allowed}
chk("高亮颜色均在语义色板内", not weird, f"分布:{dict(colors)}" + (f" 越界:{weird}" if weird else ""))

# ---------- 6. 页眉规则 ----------
chk("页眉每日重点事件已填充", "{{每日重点事件}}" not in html, "")
hd = re.search(r"\{\{[^}]+\}\}", html)
chk("无残留占位符", hd is None, f"{hd.group(0) if hd else ''}")
ticker = re.search(r'class="ticker[^"]*"[\s\S]{0,4000}', html)
if ticker:
    t = ticker.group(0)
    nu = len(re.findall(r'class="[^"]*\bup\b', t)); nd = len(re.findall(r'class="[^"]*\bdown\b', t))
    na = len(re.findall(r"[▲▼]", t))
    chk("页眉ticker已做涨跌后处理", nu + nd > 0, f"up={nu} down={nd} 箭头={na}")
    chk("页眉ticker涨跌class数≥箭头数", nu + nd >= na, f"class={nu+nd} 箭头={na}")

# ---------- 7. 文案规则 ----------
chk("老盛观点前缀无重复", not re.findall(r"老盛观点：\s*老盛观点", re.sub(r"<[^>]+>", "", html)), "")
chk("近期日历 6 条", len(re.findall(r'class="timeline-item', html)) == 6,
    f'{len(re.findall(r"class=\"timeline-item", html))}')
for code, name in [("601988", "中国银行"), ("601398", "工商银行"), ("601939", "建设银行"), ("601288", "农业银行")]:
    chk(f"关注标的含{name}({code})", code in html, "")

# ---------- 8. 数据完整性 ----------
chk("无 undefined / None / NaN 泄漏", not re.search(r">\s*(undefined|None|NaN)\s*<", html), "")
chk('无 "--" 缺失标记', '"--"' not in html and ">--<" not in html, "")
chk("无 暂无数据", "暂无数据" not in html, "")
chk("无 data-page-* 追踪属性", len(re.findall(r"data-page-", html)) == 0,
    f'{len(re.findall(r"data-page-", html))}处')

# ---------- 9. 与模板一致性 ----------
css_h = html[html.index("<style"):html.index("</style>")]
css_t = tpl[tpl.index("<style"):tpl.index("</style>")]
chk("CSS 与模板完全一致", css_h == css_t, "一致" if css_h == css_t else "存在差异")
for cls in ["tab-panel", "stock-card", "sentiment-item", "sub-title", "market-block", "summary-card"]:
    a = len(re.findall(r'class="[^"]*' + cls, html)); b = len(re.findall(r'class="[^"]*' + cls, tpl))
    chk(f"{cls} 数量与模板一致({a})", a == b, f"报告{a} 模板{b}")

# ---------- 10. 涨跌分布 ----------
nu = len(re.findall(r'class="[^"]*\bup\b', html))
nd = len(re.findall(r'class="[^"]*\bdown\b', html))
chk("涨跌class分布合理", nu > 10 and nd > 5, f"up={nu} down={nd}")

# ---------- 输出 ----------
print("=" * 64)
print("老盛早知道 20260901 深度质量检查（补充项）")
print("=" * 64)
for ok, name, detail in res:
    print(f"  [{'OK' if ok else 'XX'}] {name}" + (f"  -> {detail}" if detail else ""))
bad = [r for r in res if not r[0]]
print("=" * 64)
print(f"深度检查: 共 {len(res)} 项，通过 {len(res) - len(bad)} 项，失败 {len(bad)} 项")
if bad:
    print("--- 未通过明细 ---")
    for _, n, d in bad:
        print(f"  XX {n}: {d}")
print("=" * 64)
