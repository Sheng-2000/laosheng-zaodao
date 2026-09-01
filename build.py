# -*- coding: utf-8 -*-
# 老盛早知道 生成器：合并数据 -> 填充模板 -> 涨跌后处理 -> QC
import re, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def load(modname):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(HERE, modname + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

d1 = load("g_data1")
d2 = load("g_data2")
D = {}
D.update(d1.D)
D.update(d2.D)

# 1) 高亮密度增强（必须合并后执行，两个数据文件的键都要覆盖）
hb = load("hl_boost")
hb.apply(D)

TPL = os.path.join(HERE, "template.html")
OUT = os.path.join(HERE, "老盛早知道_20260901.html")

html = open(TPL, encoding="utf-8").read()

# 1) 占位符替换
missing = []
for key, val in D.items():
    pat = r"\{\{" + re.escape(key) + r"\}\}"
    if re.search(pat, html):
        html = re.sub(pat, str(val), html)
    else:
        missing.append(key)  # key present in data but not in template (ok-ish)

# 2) 残留占位符
leftover = sorted(set(re.findall(r"\{\{[^{}]+\}\}", html)))
print("=== 残留占位符数量:", len(leftover))
for l in leftover[:60]:
    print("  残留:", l)

# 3) market-val 涨跌后处理 (模板默认 neutral)
def sign_class(val):
    if "收跌" in val or re.search(r"-\s*\d", val):
        return "down"
    if "收涨" in val or re.search(r"\+\s*\d", val):
        return "up"
    return "neutral"

def fix_block(m):
    val = m.group(1)
    cls = sign_class(val)
    return '<span class="market-val %s">%s</span>' % (cls, val)

html = re.sub(r'<span class="market-val neutral">([\s\S]*?)</span>', fix_block, html)

# 4) header ticker 额外保险：若 mq-chg 内无 class，按符号包一层（已在数据里包，这里补兜底）
# 5) 清理可能出现的 data-page-node-id 追踪属性
html = re.sub(r'\sdata-page-node-id="[^"]*"', "", html)

open(OUT, "w", encoding="utf-8").write(html)

# 6) QC
ph = len(re.findall(r"\{\{[^{}]+\}\}", html))
dash = len(re.findall(r'"--"', html)) + len(re.findall(r">--<", html))
none = html.count("暂无数据")
print("=== QC ===")
print("占位符残留:", ph)
print('"--" 数量:', dash)
print("暂无数据数量:", none)
print("文件行数:", html.count(chr(10))+1)
print("数据项填充数:", len(D))
print("模板中未使用的数据键(可忽略):", len(missing))
