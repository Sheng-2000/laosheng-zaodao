# -*- coding: utf-8 -*-
# 防照抄门禁：生成后与上一期做句子级比对
#   - 市场数据句（T-1 共享事实，如指数/收盘/涨跌幅/成交额/逆回购）→ 可接受，仅提示
#   - 叙事/分析句（含观点推理、逐字复制）→ 判定照抄，硬 FAIL
# 用法：python 脚本/freshness_gate.py <新报告.html>
# 作为 build.py 第 7 步被调用：freshness_gate.run(OUT) -> (passed, ratio, repeats)
import re, glob, os, sys

THRESH = 0.05        # 整体叙事相同句占比上限（仅作参考/粗筛）
NARR_CJK = 10        # 叙事句含中文字数 >= 此值且逐字复制 -> 判定照抄（抓单句复制）
#                 ↑ 原为 20，导致「操作建议：持有，不追加」等短句静默放行（20260917 盲区修复）
MIN_SENT = 10        # 切句最小字符长度（原 12，短句同样要接受审查）
MIN_SENT_CJK = 6     # 切句最小中文字数

_CODE = re.compile(r'[{}<>]|function|var |document|window|matchMedia|querySelector|'
                   r'addEventListener|=>|\bconst\b|\blet\b|\.style')
_CJK = re.compile(r'[\u4e00-\u9fff]')
_DIGIT = re.compile(r'\d')
# 行情滴答标记：仅当「命中标记 + 数字密度达标 + 无观点词」时才豁免为 T-1 共享数据句
#   （原实现只凭 _DATA 命中即豁免，且词表含 指数/个股/涨幅/跌幅/PE/PB 等宽词，
#    导致「股息率超4.6%居组合前列…适合持有收息」这类观点句被误判为数据句 → 20260917 盲区修复）
_TICK = re.compile(r'成交额|成交量|涨跌幅|收盘|报收|点位|主力资金|北向资金|净流入|净流出|'
                   r'逆回购|换手率|龙虎榜|融资融券|涨停|跌停|总市值|流通市值|净息差|'
                   r'股息率|贴水|升水')
# 观点/建议/判断词：一旦出现即认定为叙事句，不享受数据句豁免
_OPIN = re.compile(r'建议|宜|不宜|值得|看好|谨慎|风险|逻辑|框架|观点|判断|关注|维持|配置|'
                   r'持有|加仓|减仓|再平衡|性价比|确定性|护城河|受益|延续|凸显|结论|'
                   r'窗口|策略|纪律|节奏|耐心|成本|清醒|分位|估值|共振|未破|支撑|压舱石|'
                   r'底色|弹性|买点|退潮|拥挤|情绪|分批|定投|止损|溢出|阈值|锚定|比价|'
                   r'利差|偏离|集中度|健康|抽水|托底|旗手|补涨|防御')

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
    """是否为「T-1 共享行情事实」句（可豁免照抄判定）。
    收紧后的判定：数字极密集 → 数据句；
    否则须同时满足「命中行情标记 + 数字密度>=8% + 中文字数<=45 + 无观点词」。"""
    if len(s) == 0:
        return False
    ratio = len(_DIGIT.findall(s)) / len(s)
    if ratio > 0.35:
        return True
    if _OPIN.search(s):
        return False
    return bool(_TICK.search(s)) and ratio >= 0.08 and _cjk_len(s) <= 45

def _sents(text):
    # 只保留"有信息量的中文叙事句"：含中文、非代码片段、长度足够
    parts = re.split(r'[。！？；.!?;]', text)
    out = []
    for p in parts:
        p = p.strip()
        if len(p) < MIN_SENT:
            continue
        if not _CJK.search(p):
            continue
        if _cjk_len(p) < MIN_SENT_CJK:
            continue
        if _CODE.search(p):
            continue
        out.append(p)
    return out

def _norm(s):
    """归一化：只保留汉字，剔除数字/标点/emoji。
    模板固定文案里嵌有 {{占位符}}，填充后数字每期不同，精确串匹配会失效；
    归一化后即可识别"同一句模板文案"。"""
    return re.sub(r'[^一-鿿]', '', s)


def _tpl_sents(new_path):
    """模板静态文案：骨架里的固定句（如"险资动向/收益计算器/资产配置建议"等
    通用框架）在任意两期报告中必然相同，属结构性继承，不构成照抄。
    返回 (精确句集合, 归一化长串)——后者用于含占位符填充值的句子。"""
    here = os.path.dirname(os.path.abspath(__file__))
    tpl = os.path.join(os.path.dirname(here), '规则', 'template.html')
    if not os.path.exists(tpl):
        return set(), ''
    try:
        t = open(tpl, encoding='utf-8').read()
    except Exception:
        return set(), ''
    t2 = re.sub(r'\{\{[^}]*\}\}', ' ', t)     # 占位符位置无实义文本
    return set(_sents(_strip(t2))), _norm(_strip(t))


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
    tpl_s, tpl_norm = _tpl_sents(new_path)

    def _from_tpl(s):
        """该句是否源自模板固定文案（含仅数字被填充替换的情形）"""
        if s in tpl_s:
            return True
        n = _norm(s)
        return len(n) >= 12 and n in tpl_norm

    def _from_ui(s):
        """HTML 展平后，相邻的 UI 标签/数值会被 _strip 拼成一个"伪句子"
        （如「四 · 低估值板块 🏦 中证红利 今日涨幅 -0」）。
        特征：无句读标点（，。：）、中文字数少、且被非汉字分隔的每段汉字都短（<8字）
        → 属结构性标签拼接，不是照抄叙事。"""
        if re.search(r'[，。：]', s):
            return False
        runs = [r for r in re.split(r'[^\u4e00-\u9fff]+', s) if _cjk_len(r) >= 2]
        if not runs:
            return False
        return max(_cjk_len(r) for r in runs) < 8 and _cjk_len(s) < 20

    repeats = [s for s in sents_new
               if s in sents_prev and not _from_tpl(s) and not _from_ui(s)]
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
