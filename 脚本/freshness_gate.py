# -*- coding: utf-8 -*-
# 防照抄门禁：生成后与上一期做句子级比对
#   - 市场数据句（T-1 共享事实，如指数/收盘/涨跌幅/成交额/逆回购）→ 可接受，仅提示
#   - 叙事/分析句（含观点推理、逐字复制）→ 判定照抄，硬 FAIL
# 用法：python 脚本/freshness_gate.py <新报告.html>
# 作为 build.py 第 7 步被调用：freshness_gate.run(OUT) -> (passed, ratio, repeats)
import re, glob, os, sys

THRESH = 0.05        # 整体叙事相同句占比上限（仅作参考/粗筛）
NARR_CJK = 20        # 叙事句含中文字数 >= 此值且逐字复制 -> 判定照抄（抓单句复制）

_CODE = re.compile(r'[{}<>]|function|var |document|window|matchMedia|querySelector|'
                   r'addEventListener|=>|\bconst\b|\blet\b|\.style')
_CJK = re.compile(r'[\u4e00-\u9fff]')
_DIGIT = re.compile(r'\d')
# 市场数据句标记：含这些词的句子视为 T-1 共享行情事实，不算照抄
_DATA = re.compile(r'创历史新高|涨跌幅|收盘|成交额|主力资金|北向资金|逆回购|净息差|'
                    r'股息率|\bPE\b|\bPB\b|涨停|跌停|龙虎榜|融资融券|换手率|成交量|'
                    r'总市值|流通市值|盘中|涨幅|跌幅|指数|个股|板块成交')

def _strip(html):
    h = re.sub(r'<script.*?</script>', ' ', html, flags=re.S)
    h = re.sub(r'<style.*?</style>', ' ', html, flags=re.S)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'&[a-z]+;', ' ', h)
    h = re.sub(r'\s+', ' ', h)
    return h

def _cjk_len(s):
    return len(_CJK.findall(s))

def _is_data(s):
    if _DATA.search(s):
        return True
    if len(s) == 0:
        return False
    # 数字密集（>35%）视为数据滴答
    return len(_DIGIT.findall(s)) / len(s) > 0.35

def _sents(text):
    # 只保留"有信息量的中文叙事句"：含中文、非代码片段、长度足够
    parts = re.split(r'[。！？；.!?;]', text)
    out = []
    for p in parts:
        p = p.strip()
        if len(p) < 12:
            continue
        if not _CJK.search(p):
            continue
        if _CODE.search(p):
            continue
        out.append(p)
    return out

def run(new_path, prev_path=None):
    html_new = open(new_path, encoding='utf-8').read()
    sents_new = _sents(_strip(html_new))

    if prev_path is None:
        base = os.path.dirname(os.path.abspath(new_path))
        cands = sorted(glob.glob(os.path.join(base, '老盛早知道_*.html')))
        cands = [c for c in cands if os.path.basename(c) != os.path.basename(new_path)]
        prev_path = cands[-1] if cands else None

    if prev_path is None:
        print("[GATE] 无上一期可比对，跳过")
        return True, 0.0, []

    html_prev = open(prev_path, encoding='utf-8').read()
    sents_prev = set(_sents(_strip(html_prev)))
    repeats = [s for s in sents_new if s in sents_prev]
    ratio = (len(repeats) / len(sents_new)) if sents_new else 0.0

    data_repeats = [s for s in repeats if _is_data(s)]
    narr_repeats = [s for s in repeats if not _is_data(s)
                    and _cjk_len(s) >= NARR_CJK]
    passed = len(narr_repeats) == 0

    print("=== 防照抄门禁 ===")
    print("新报告叙事句数:", len(sents_new), " 相同句:", len(repeats),
          " 整体占比: %.1f%%" % (ratio * 100))
    print("  ├ 市场数据句(可接受,T-1共享):", len(data_repeats))
    print("  └ 叙事/分析句(照抄风险):", len(narr_repeats))
    print("比对对象:", os.path.basename(prev_path))
    if narr_repeats:
        print("⚠️ 照抄叙事句(须基于当天搜索重写):")
        for s in narr_repeats[:20]:
            print("  >", s[:90])
    elif data_repeats:
        print("提示：仅检测到 T-1 共享市场数据句（可接受），例如:")
        for s in data_repeats[:6]:
            print("  >", s[:80])
    print("判定:", "PASS ✅" if passed else "FAIL ❌ (检测到 %d 条叙事照抄)" % len(narr_repeats))
    return passed, ratio, repeats

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: freshness_gate.py <new_report.html>")
        sys.exit(2)
    ok, _, _ = run(sys.argv[1])
    sys.exit(0 if ok else 1)
