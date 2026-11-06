# -*- coding: utf-8 -*-
# hl_boost.py —— 高亮密度增强器
# 作用：在 build.py 合并 D 之后、填充模板之前，为叙事类文本自动补充
#       涨红跌绿/关键词高亮，保证“重点突出展示”达标且不改变字体大小。
# 规则：
#   - 新闻/AI 卡（key 含“新闻”或“生物医学”）每处文本至少 5 处高亮
#   - 其余叙事卡（机构/话题/操作建议/要点/综评/持仓/深度解读等）至少 2 处高亮
#   - 只对包含正面/负面方向词或数值的句子做增强，不做重复包裹
import re

RED = "#f85149"     # 涨/利好/正面
GREEN = "#3fb950"   # 跌/利空/负面
YELLOW = "#f0b429"  # 警示/中性
BLUE = "#00d4ff"    # 关键数字/数据
ORANGE = "#ffa657"  # 老盛观点/建议

# 正向词（红色）
POS_WORDS = ["大涨", "领涨", "上涨", "走高", "反弹", "创新高", "净流入", "净买入",
             "增持", "利好", "提升", "上调", "增长", "盈利", "改善", "突破",
             "新高", "看多", "看好", "乐观", "信心", "提振", "逆势上涨",
             "放量上涨", "收涨", "跑赢", "超额", "分红", "股息", "稳健增长",
             "止跌回升", "普涨", "收红", "提速", "加速", "推进", "落地", "扩容",
             "走强", "上行", "放量", "回暖", "修复", "走红", "大涨4", "涨2"]
# 负向词（绿色）
NEG_WORDS = ["大跌", "领跌", "下跌", "走低", "回调", "新低", "净流出", "净卖出",
             "减持", "利空", "下调", "下滑", "亏损", "恶化", "跌破", "看空",
             "悲观", "恐慌", "谨慎", "拖累", "承压", "抛售", "收跌", "普跌",
             "暴跌", "重挫", "跑输", "失守", "回落", "缩量", "跌破", "波动",
             "风险", "冲击", "调整", "退潮", "回吐", "爆仓", "跌停", "蒸发",
             "趋紧", "收紧", "压制", "担忧", "高企", "回落", "恶化", "走弱",
             "下行", "降温", "疲软", "波折", "承压", "分化", "消退", "收敛",
             "不及预期", "低于预期", "放缓", "踩踏", "踩雷", "暴雷", "违约"]
# 中性关注词（黄色/蓝色补足用）
WARN_WORDS = ["关注", "注意", "警惕", "跟踪", "提示", "需注意", "留意"]
# 中性·青色（#00d4ff）可标注词：仅保留“价值投资/红利策略语境下真正关键”的术语，
# 用于补足高亮密度（新闻/AI≥5、其余≥2）而绝不触碰涨红跌绿语义。
# ⚠️ 适配（2026-11-06）：原先 60+ 通用名词（市场/政策/数据/公司/板块/指数…）泛滥成青色噪声，
#    失去重点；现收敛为约 40 个“真有关键信息量”的术语，避免满屏青色。
#    —— 红/绿（涨红跌绿+方向词）与关键数字才是真正要突出的“重点”，青色只做少量锚点。
KEY_TERMS = ["红利", "高股息", "股息率", "估值", "低估", "PB", "PE", "净资产",
             "ROE", "净息差", "分红", "分红率", "现金流", "再平衡", "避险",
             "防御", "护盘", "确定性", "复利", "央企", "央国企", "配置", "仓位",
             "安全边际", "宽基", "蓝筹", "龙头", "护城河", "国债", "货基", "ETF",
             "保费", "利差", "久期", "信用", "盈利", "营收", "净利", "回购",
             "成长", "景气", "利率", "收益率", "美债", "美联储", "通胀", "降息",
             "加息", "汇率", "美元", "油价", "金价", "流动性", "逆回购", "非农", "就业"]
# 关键数字（蓝色）
NUM_RE = re.compile(r"[+\-−]?\d+(?:\.\d+)?\s*(?:%|％|亿|万|点|倍|元|bp|pct|个)")

def _wrap(text, color, weight=700):
    return '<span style="color:%s;font-weight:%s;">%s</span>' % (color, weight, text)

def _is_wrapped(seg):
    return seg.startswith('<span') and 'style="color:' in seg


def _inside_span(out, p):
    """判断位置 p 是否落在某个颜色 span 内部（未闭合的 <span> 多于 </span>）。"""
    opens = out.count('<span style="color:', 0, p)
    closes = out.count('</span>', 0, p)
    return opens > closes

def _wrap_first(out, w, color):
    """包裹首个未被包裹的词（已在 span 内的跳过以免嵌套）。"""
    i = 0
    while True:
        p = out.find(w, i)
        if p < 0:
            return out
        if not _inside_span(out, p):
            return out[:p] + _wrap(w, color) + out[p + len(w):]
        i = p + len(w)

def _boost_core(text, min_hits=3, force=True):
    """给一段纯文本自动加高亮（标记已在外层保护）。顺序：先涨跌数字着色（涨红/跌绿），再方向词着色，再警示/信息词补足。"""
    if not text or '<span' in text:
        return text
    out = text
    hits = 0

    # 1) 数字着色：+红 / -绿 / 无符号看前导词（涨红跌绿）与位置
    def num_color(seg, before):
        if seg.startswith(("+", "−")):
            return RED
        if seg.startswith("-"):
            return GREEN
        if any(w in before for w in ("跌", "降", "负", "下", "回落", "下调", "跌破", "收跌")):
            return GREEN
        if any(w in before for w in ("涨", "升", "正", "上", "回升", "上调", "突破", "收涨", "走强")):
            return RED
        return BLUE

    num_hits = 0
    out2 = []
    last = 0
    for m in NUM_RE.finditer(out):
        s, e = m.span()
        if num_hits >= 6:
            break
        seg = out[s:e]
        if _is_wrapped(seg):
            continue
        before = out[max(0, s-4):s]
        c = num_color(seg, before)
        out2.append(out[last:s])
        out2.append(_wrap(seg, c))
        last = e
        num_hits += 1
        hits += 1
    out2.append(out[last:])
    out = "".join(out2)

    # 2) 方向词着色补足
    for w in POS_WORDS:
        if hits >= min_hits:
            break
        new = _wrap_first(out, w, RED)
        if new != out:
            out, hits = new, hits + 1
    for w in NEG_WORDS:
        if hits >= min_hits:
            break
        new = _wrap_first(out, w, GREEN)
        if new != out:
            out, hits = new, hits + 1
    # 3) 警示词（黄）
    for w in WARN_WORDS:
        if hits >= min_hits:
            break
        new = _wrap_first(out, w, YELLOW)
        if new != out:
            out, hits = new, hits + 1
    # 4) 关键信息词（蓝·仅 KEY_TERMS 真有关键信息量）
    for w in KEY_TERMS:
        if hits >= min_hits:
            break
        new = _wrap_first(out, w, BLUE)
        if new != out:
            out, hits = new, hits + 1
    # 5) 兜底：循环包裹所有「未包裹」的 KEY_TERMS 出现（蓝/中性，绝不触碰涨跌语义），
    #    直到达到 min_hits，保证新闻/AI 卡≥5、其余叙事卡≥2 的高亮密度；
    #    ⚠️ 适配：仅用收敛后的 KEY_TERMS（不再用 60+ 通用名词），避免青色泛滥失去重点。
    while hits < min_hits:
        wrapped_any = False
        for w in KEY_TERMS:
            if hits >= min_hits:
                break
            p = 0
            while True:
                p = out.find(w, p)
                if p < 0:
                    break
                if not _inside_span(out, p):
                    out = out[:p] + _wrap(w, BLUE) + out[p + len(w):]
                    hits += 1
                    wrapped_any = True
                    p += len(w) + 50  # 跳过刚插入的 span，避免重复命中同一处
                else:
                    p += len(w)
            if hits >= min_hits:
                break
        if not wrapped_any:
            break
    return out


def boost_text(text, min_hits=3, force=True):
    """给一段纯文本自动加高亮。已含 <span> 的文本跳过（避免重复包裹）。
    若含 build 期标记 {r|…}/{c|…} 等，先将其暂存为占位符、填充其余文本后再还原，
    既避免在标记内部二次包裹数字导致嵌套 span 错乱，仍对非标记部分补足高亮。
    使用 re.sub 回调统一处理，避免逐段替换时的偏移错位（曾导致占位符泄漏/嵌套错乱）。"""
    if not text or '<span' in text:
        return text
    protected = {}
    counter = [0]
    def _stash(m):
        ph = '\x00%d\x00' % counter[0]
        protected[ph] = m.group(0)
        counter[0] += 1
        return ph
    t = re.sub(r'\{[rgcyo]\|[^}]*\}', _stash, text)
    if not protected:
        return _boost_core(text, min_hits)
    out = _boost_core(t, min_hits)
    for ph, p in protected.items():
        out = out.replace(ph, p)
    return out

NEWS_KEYS = ("新闻", "生物医学", "AI应用", "大模型", "算力", "机器人", "产业趋势", "地缘")

def apply(D):
    """对 D 中的叙事类 key 做高亮增强；对已含高亮的正文补足缺失方向词。"""
    for k, v in list(D.items()):
        if not isinstance(v, str) or len(v) < 20:
            continue
        if k in ("报告日期", "数据截止日期", "YYYY/MM/DD", "星期"):
            continue
        # 标题/标签是短抬头，高亮由正文承载；包裹进标题会破坏质检脚本的字面比对
        if k.endswith(("标题", "标签")):
            continue
        if any(nk in k for nk in NEWS_KEYS):
            # 新闻类：若完全没有高亮，做全增强；若已有高亮，仅补足数量不足的情况
            if "<span" not in v:
                D[k] = boost_text(v, min_hits=3)
        elif k.startswith(("机构", "话题", "社区话题", "操作建议", "要点", "综评", "持仓",
                            "深度解读", "避坑", "高股息", "今日总结", "市场热点",
                            "正面因素", "风险提示", "理财", "保险", "债基",
                            "替代策略", "宏观", "市场", "资金", "低估值",
                            "时间线", "资金流向", "参考", "标的_")):
            if "<span" not in v:
                if k.startswith("社区话题") and re.search(r"_观点[123]$", k):
                    continue
                if k.startswith("社区话题"):
                    mh = 4
                elif k.startswith("要点"):
                    mh = 2
                else:
                    mh = 2
                D[k] = boost_text(v, min_hits=mh)
    return D
