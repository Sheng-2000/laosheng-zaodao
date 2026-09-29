# -*- coding: utf-8 -*-
"""
合并归档脚本：把"基底 + 累积 _ov_* 覆盖块"的旧数据文件，解析为
【单日完整 D 字典】的干净新文件，彻底清除 D.update() 叠加模式。

用法：
    python3 脚本/consolidate_g_data.py g_data1
    python3 脚本/consolidate_g_data.py g_data2

输出：覆盖同名文件（先备份到 /tmp），新文件只包含：
    - R/G/Y/C/O 颜色函数定义
    - 单个完整 D = { ... }（覆盖该文件域的全部键，无叠加、无历史残留）

安全校验：
    - 导入原文件拿到"已解析的最终 D"
    - 写出新文件后重新导入，逐项比对 D 是否逐字一致（lossless）
    - 任一键非字符串或比对不一致 -> 中断并保留原文件
"""
import re, sys, os, json, shutil, importlib.util, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

COLOR_DEFS = '''def R(t): return '<span style="color:#f85149;font-weight:700;">%s</span>' % t
def G(t): return '<span style="color:#3fb950;font-weight:700;">%s</span>' % t
def Y(t): return '<span style="color:#f0b429;font-weight:700;">%s</span>' % t
def C(t): return '<span style="color:#00d4ff;font-weight:700;">%s</span>' % t
def O(t): return '<span style="color:#ffa657;font-weight:700;">%s</span>' % t
'''

def load_mod(name):
    path = os.path.join(HERE, name + ".py")
    spec = importlib.util.spec_from_file_location("src_" + name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def dump_d(D):
    """逐键写出，键/值均用 json.dumps(ensure_ascii=False) -> 合法 Python 字符串字面量。"""
    lines = []
    for k in sorted(D.keys()):
        v = D[k]
        if not isinstance(v, str):
            raise TypeError("非字符串值: %s -> %s" % (k, type(v).__name__))
        lines.append("    %s: %s," % (json.dumps(k, ensure_ascii=False),
                                      json.dumps(v, ensure_ascii=False)))
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("g_data1", "g_data2"):
        print("用法: consolidate_g_data.py g_data1|g_data2")
        sys.exit(2)
    name = sys.argv[1]
    src_path = os.path.join(HERE, name + ".py")
    if not os.path.exists(src_path):
        print("源文件不存在:", src_path); sys.exit(1)

    m = load_mod(name)
    D = dict(m.D)  # 已解析的最终 D（基底经所有 _ov 覆盖后的结果）
    print("[%s] 解析到最终 D 键数: %d" % (name, len(D)))

    # 1) 全部须为字符串
    bad = [(k, type(v).__name__) for k, v in D.items() if not isinstance(v, str)]
    if bad:
        print("❌ 发现非字符串值:", bad[:5]); sys.exit(1)

    # 2) 备份原文件
    stamp = datetime.date.today().strftime("%Y%m%d")
    bak = "/tmp/%s.pre_consolidate_%s.py" % (name, stamp)
    shutil.copy(src_path, bak)
    print("   已备份原文件 ->", bak)

    # 3) 写出干净新文件
    out = '''# -*- coding: utf-8 -*-
# 老盛早知道 数据文件（每日全量生成，无 D.update 叠加模式）
# 生成日期: %s
# 说明: 本文件为单日完整快照，每天由生成流程从头写出，不复用历史覆盖块。
%s
D = {
%s
}
''' % (stamp, COLOR_DEFS, dump_d(D))

    tmp_path = "/tmp/consolidate_%s_%s.py" % (name, stamp)
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(out)

    # 4) 重新导入新文件，逐项比对（lossless）
    spec2 = importlib.util.spec_from_file_location("new_" + name, tmp_path)
    m2 = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(m2)
    D2 = m2.D
    if set(D2.keys()) != set(D.keys()):
        print("❌ 键集合不一致"); sys.exit(1)
    mism = [(k, D[k], D2[k]) for k in D if D[k] != D2[k]]
    if mism:
        print("❌ 内容比对不一致条数:", len(mism))
        for k, a, b in mism[:5]:
            print("   键:", k)
            print("     原:", a[:80])
            print("     新:", b[:80])
        sys.exit(1)

    shutil.move(tmp_path, src_path)
    print("✅ [%s] 已合并归档为单日完整 D（%d 键），无叠加、无历史残留" % (name, len(D)))

if __name__ == "__main__":
    main()
