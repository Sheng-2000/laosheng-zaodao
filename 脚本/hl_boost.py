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
             "趋紧", "收紧", "压制", "担忧", "高企", "回落", "恶化", "走弱"]
# 中性关注词（黄色/蓝色补足用）
WARN_WORDS = ["关注", "注意", "警惕", "跟踪", "提示", "需注意", "留意"]
INFO_WORDS = ["政策", "行业", "市场", "技术", "资金", "数据", "利率", "行情",
              "产业链", "资产", "配置", "投资", "布局", "方向", "趋势", "观点"]
# 关键数字（蓝色）
NUM_RE = re.compile(r"[+\-−]?\d+(\.\d+)?%?")

def _wrap(text, color, weight=700):
    return '<span style="color:%s;font-weight:%s;">%s</span>' % (color, weight, text)

def _is_wrapped(seg):
    return seg.startswith('<span') and 'style="color:' in seg

def boost_text(text, min_hits=3, force=True):
    """给一段纯文本自动加高亮。已含 <span> 的文本跳过（避免重复包裹）。
    顺序：先涨跌数字着色（涨红/跌绿），再方向词着色，再警示/信息词补足。"""
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
        if w in out and hits < min_hits:
            out = out.replace(w, _wrap(w, RED), 1)
            hits += 1
    for w in NEG_WORDS:
        if w in out and hits < min_hits:
            out = out.replace(w, _wrap(w, GREEN), 1)
            hits += 1
    # 3) 警示词（黄）
    for w in WARN_WORDS:
        if w in out and hits < min_hits:
            out = out.replace(w, _wrap(w, YELLOW), 1)
            hits += 1
    # 4) 关键信息词（蓝）
    for w in INFO_WORDS:
        if w in out and hits < min_hits:
            out = out.replace(w, _wrap(w, BLUE), 1)
            hits += 1
    return out

NEWS_KEYS = ("新闻", "生物医学", "AI应用", "大模型", "算力", "机器人", "产业趋势", "地缘")

def apply(D):
    """对 D 中的叙事类 key 做高亮增强；对已含高亮的正文补足缺失方向词。"""
    for k, v in list(D.items()):
        if not isinstance(v, str) or len(v) < 20:
            continue
        if k in ("报告日期", "数据截止日期", "YYYY/MM/DD", "星期"):
            continue
        if any(nk in k for nk in NEWS_KEYS):
            # 新闻类：若完全没有高亮，做全增强；若已有高亮，仅补足数量不足的情况
            if "<span" not in v:
                D[k] = boost_text(v, min_hits=5)
        elif k.startswith(("机构", "话题", "操作建议", "要点", "综评", "持仓",
                            "深度解读", "避坑", "高股息", "今日总结", "市场热点",
                            "正面因素", "风险提示", "理财", "保险", "债基",
                            "替代策略", "宏观", "市场", "资金", "低估值",
                            "今日总结", "时间线", "资金流向", "参考", "标的_",
                            "深度解读")):
            if "<span" not in v:
                mh = 3 if k.startswith("要点") else 2
                D[k] = boost_text(v, min_hits=mh)
    return D
