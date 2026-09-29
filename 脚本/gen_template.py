# -*- coding: utf-8 -*-
"""
从已折叠的干净单日数据文件(g_data1.py / g_data2.py)重新生成完整模板：
  - 保留 R/G/Y/C/O 颜色函数
  - D 字典所有键保留，值清空为 ""
  - 按语义分节归类，便于每日填空
用法:
  python3 脚本/gen_template.py g_data1
  python3 脚本/gen_template.py g_data2
输出: 脚本/<name>_template.py (覆盖)
"""
import sys, os, json, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
COLOR_DEFS = '''def R(t): return '<span style="color:#f85149;font-weight:700;">%s</span>' % t
def G(t): return '<span style="color:#3fb950;font-weight:700;">%s</span>' % t
def Y(t): return '<span style="color:#f0b429;font-weight:700;">%s</span>' % t
def C(t): return '<span style="color:#00d4ff;font-weight:700;">%s</span>' % t
def O(t): return '<span style="color:#ffa657;font-weight:700;">%s</span>' % t
'''

SECTIONS = [
    ("元数据", ["报告日期", "星期", "YYYY/MM/DD", "每日重点事件", "数据截止", "近期日历"]),
    ("新闻/AI前沿", ["重点新闻", "财经新闻", "地缘新闻", "产业趋势", "大模型", "算力", "机器人", "AI应用", "生物医学", "新闻", "AI"]),
    ("机构观点", ["机构"]),
    ("社区话题", ["社区话题"]),
    ("高股息", ["高股息"]),
    ("关注标的", ["标的"]),
    ("操作建议/持仓", ["操作建议", "避坑", "持仓"]),
]

def categorize(k):
    for title, prefixes in SECTIONS:
        for p in prefixes:
            if k.startswith(p):
                return title
    return "市场数据/其他"

def main():
    name = sys.argv[1]
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    D = m.D
    # 分节
    buckets = {}
    for k in sorted(D.keys()):
        buckets.setdefault(categorize(k), []).append(k)
    # 固定输出顺序
    order = [s[0] for s in SECTIONS] + ["市场数据/其他"]
    lines = []
    for sec in order:
        keys = buckets.get(sec, [])
        if not keys:
            continue
        lines.append("    # ===== %s =====" % sec)
        for k in keys:
            lines.append('    %s: "",' % json.dumps(k, ensure_ascii=False))
    out = '''# -*- coding: utf-8 -*-
# 大福·老盛早知道 %s 叙事/数据模板（每日重置用）
# 用法: reset_%s.sh 会先备份当前 %s.py，再从本模板复制为新的 %s.py
# 然后基于当天搜索到的最新数据，填充下面所有 key
# 注意：不要使用 D.update() 叠加模式，直接在 D 字典中写全量内容
%s
D = {
%s
}
''' % (name, name, name, name, COLOR_DEFS, "\n".join(lines))
    tpl = os.path.join(HERE, name + "_template.py")
    with open(tpl, "w", encoding="utf-8") as f:
        f.write(out)
    print("[%s] 模板已生成: %d 键 -> %s" % (name, len(D), tpl))

if __name__ == "__main__":
    main()
