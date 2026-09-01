# -*- coding: utf-8 -*-
import re, importlib.util, os

HERE = os.path.dirname(os.path.abspath(__file__))
def load(mn):
    spec = importlib.util.spec_from_file_location(mn, os.path.join(HERE, mn + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
d1 = load("g_data1"); d2 = load("g_data2")
D = {}; D.update(d1.D); D.update(d2.D)

def clean(s): return re.sub(r'<[^>]+>', '', str(s))

print("=== 四区字数 (>=120) ===")
# 机构
def lens(prefix, n, keys_fn):
    res=[]
    for i in range(1, n+1):
        for k in keys_fn(i):
            if k in D: res.append((k, len(clean(D[k]))))
    return res
ji = lens(6, 6, lambda i:[f"机构{i}_观点"])
for k,l in ji: print(" ", k, l, "OK" if l>=120 else "*** 不足120")
gd = lens(5, 5, lambda i:[f"高股息{i}_正文"])
for k,l in gd: print(" ", k, l, "OK" if l>=120 else "*** 不足120")
op = lens(6, 6, lambda i:[f"操作建议{i}_内容"])
for k,l in op: print(" ", k, l, "OK" if l>=120 else "*** 不足120")

print("=== 社区话题格式 ===")
for i in range(1,6):
    title=D.get(f"社区话题{i}_标题","")
    v1=D.get(f"社区话题{i}_观点1",""); v2=D.get(f"社区话题{i}_观点2",""); v3=D.get(f"社区话题{i}_观点3","")
    view=D.get(f"社区话题{i}_观点","")
    is_q = "？" in title or "?" in title
    roles = all([v1,v2,v3,view])
    # 高亮计数(span)
    hl = len(re.findall(r'<span', v1+v2+v3))
    print(f"  话题{i}: 问句={is_q} 三角色+老盛={roles} 高亮span数={hl} 标题={title[:24]}")

# 关键涨跌值抽查 (已知 8/31 收盘)
print("=== 已知涨跌抽查 (8/31) ===")
checks = {
 "A股_上证指数_数据":"+0.86%",  # 8/31 上证收涨
 "黄金_涨跌":"",  # 黄金大跌 -> down
}
for k,exp in checks.items():
    if k in D: print(" ", k, "=", clean(D[k])[:50])
# ticker 上证
for k in ["ticker_上证_数值","ticker_上证_涨跌幅","ticker_黄金_数值","ticker_黄金_涨跌幅","ticker_道指_涨跌幅"]:
    if k in D: print(" ", k, "=", clean(D[k]))
