# -*- coding: utf-8 -*-
"""
fetch_news.py — 实时新闻 / AI / 社区 素材层（B 方案·叙事实时化）

设计目标
--------
定时任务每轮 build 时调用，从 akshare 拉取「当日真实、带日期、带信源」的财经新闻，
注入 g_data2 的新闻 / AI 区块，确保头条不再是烤死的硬编码。

- 所有注入文本均来自数据源真实返回（标题 / 摘要 / 发布时间 / 链接），**绝不编造**。
- 网络受限或取数失败时，记录 FALLBACK 并保留 g_data2 硬编码兜底，流水线不中断。
- 头条(标签和标题)实时覆盖；正文(分析)保留 g_data2 既有的、由 agent 每轮重写的版本，
  以维持高亮密度与报告风格（cover_qc 要求新闻/AI 卡 ≥5 处高亮）。
- 机构 / 社区 / 生物医学 为多角色结构化叙事，无法机械合成而不编造，
  故保留为 agent 维护（5步流程「搜→写 g_data2」），本模块仅提供 get_* 取数接口供 agent 使用。

依赖：akshare（隔离 venv 已装）。沙箱实测可用端点：
  stock_info_global_em  (东方财富全球财经快讯，200 条，含 标题/摘要/发布时间/链接)
  stock_news_em(symbol) (个股新闻)
  stock_hot_keyword_em  (实时热搜概念，含 时间/股票代码/概念名称/热度)
"""

import os as _os
import sys as _sys
import threading as _th
import re as _re
import json as _json
import tempfile as _tf
import time as _time

try:
    import akshare as ak
except Exception:
    ak = None

FALLBACK = []          # 走硬编码兜底的项
_NOTE = []             #  deliberate agent 维护、非取数失败的项
_CACHE = None          # 进程内缓存
_TIMEOUT = 12          # 单接口硬超时（秒）
_TTL = 600             # 磁盘缓存有效期（秒）


def _news_cache_path():
    return _os.path.join(_tf.gettempdir(),
                         "laosheng_news_%s.json" % _time.strftime("%Y%m%d"))


def _load_news_disk():
    try:
        p = _news_cache_path()
        if _os.path.exists(p) and (_time.time() - _os.path.getmtime(p)) < _TTL:
            with open(p, encoding="utf-8") as f:
                return _json.load(f)
    except Exception:
        return None
    return None


def _save_news_disk(data):
    try:
        with open(_news_cache_path(), "w", encoding="utf-8") as f:
            _json.dump(data, f)
    except Exception:
        pass

# ---- 分类关键词 ----
_CAT = {
    "geo":       ["伊朗", "霍尔木兹", "原油", "战争", "制裁", "地缘", "乌克兰", "俄罗斯",
                  "中东", "美军", "空袭", "海峡", "石油", "油价"],
    "bio":       ["脑机", "医药", "生物", "临床", "医保", "创新药", "医疗", "制药", "疫苗"],
    "ai":        ["AI", "大模型", "算力", "GPU", "芯片", "英伟达", "OpenAI", "机器人", "人形",
                  "智能体", "agent", "Meta", "谷歌", "微软", "半导体", "存储", "数据中心"],
    "industry":  ["产业", "制造", "新能源", "汽车", "房地产", "消费", "基建", "化工", "机械"],
    "macro":     ["央行", "利率", "美联储", "GDP", "通胀", "CPI", "降息", "加息", "债市", "国债",
                  "分红", "财报", "经济", "PMI", "A股", "港股", "美股", "股市", "创业板"],
}


def _run(fn, timeout=_TIMEOUT):
    """带硬超时的线程执行；超时/异常返回 None。"""
    res = [None]
    err = [None]

    def _go():
        try:
            res[0] = fn()
        except Exception as e:  # noqa: BLE001
            err[0] = e

    t = _th.Thread(target=_go, daemon=True)
    t.start()
    t.join(timeout)
    if t.is_alive() or err[0] is not None:
        return None
    return res[0]


def _cat_of(text):
    """按优先级归类：geo > bio > ai > industry > macro > None(综合top)。"""
    if not text:
        return None
    t = text
    for c in ("geo", "bio", "ai", "industry", "macro"):
        if any(k in t for k in _CAT[c]):
            return c
    return None


def _mmdd(dt):
    """从 '2026-09-02 13:35:45' 提取 '09/02'。"""
    if not dt:
        return ""
    m = _re.search(r"(\d{4})-(\d{2})-(\d{2})", str(dt))
    if m:
        return "%s/%s" % (m.group(2), m.group(3))
    return ""


# ---- 取数接口 ----

def get_news(limit=80):
    """返回真实新闻列表：{title, summary, date, url, cat, source}。复用当日磁盘缓存。"""
    global _CACHE
    if _CACHE is not None:
        return _CACHE[:limit] if limit else _CACHE
    cached = _load_news_disk()
    if cached:
        _CACHE = cached
        return _CACHE[:limit] if limit else _CACHE
    df = _run(lambda: ak.stock_info_global_em() if ak else None)
    out = []
    if df is None or not hasattr(df, "empty") or df.empty:
        FALLBACK.append("新闻_stock_info_global_em")
        return out
    for _, row in df.iterrows():
        title = _str(row.get("标题", ""))
        if not title:
            continue
        summary = _str(row.get("摘要", "")) or title
        date = _mmdd(row.get("发布时间", ""))
        out.append({
            "title": title,
            "summary": summary,
            "date": date,
            "url": _str(row.get("链接", "")),
            "cat": _cat_of(title + " " + summary),
            "source": "东方财富",
        })
        if len(out) >= 200:
            break
    _CACHE = out
    _save_news_disk(out)
    return out[:limit] if limit else out


def get_stock_news(code, limit=4):
    """个股真实新闻：{title, date, url}。"""
    df = _run(lambda: ak.stock_news_em(symbol=code) if ak else None)
    if df is None or getattr(df, "empty", True):
        FALLBACK.append("个股新闻_%s" % code)
        return []
    out = []
    for _, row in df.head(limit).iterrows():
        title = _str(row.get("新闻标题", row.get("标题", "")))
        if not title:
            continue
        out.append({
            "title": title[:80],
            "date": _mmdd(row.get("发布时间", row.get("日期", ""))),
            "url": _str(row.get("新闻链接", row.get("链接", ""))),
        })
    return out


def get_hot_keywords():
    """实时热搜概念：{time, code, name, heat}（社区话题种子）。"""
    df = _run(lambda: ak.stock_hot_keyword_em() if ak else None)
    if df is None or getattr(df, "empty", True):
        FALLBACK.append("热搜词_stock_hot_keyword_em")
        return []
    out = []
    for _, row in df.head(8).iterrows():
        out.append({
            "time": _str(row.get("时间", "")),
            "code": _str(row.get("股票代码", "")),
            "name": _str(row.get("概念名称", "")),
            "heat": _str(row.get("热度", "")),
        })
    return out


def get_ai_news(limit=20):
    """AI / 算力 / 机器人 / 生物 相关真实新闻。"""
    return [x for x in get_news() if x["cat"] in ("ai", "bio")][:limit]


def _str(v):
    if v is None:
        return ""
    return str(v).strip()


# ---- 注入（每轮 build 调用） ----

# 新闻卡映射：(前缀, 卡片数, 分类 or None=综合top)
_NEWS_CARDS = [
    ("重点新闻", 8, None),
    ("财经新闻", 6, "macro"),
    ("地缘新闻", 2, "geo"),
    ("产业趋势新闻", 1, "industry"),
    ("大模型新闻", 4, "ai"),
    ("算力新闻", 5, "ai"),
    ("机器人新闻", 3, "ai"),
    ("AI应用新闻", 3, "ai"),
]


def apply(D):
    """把真实头条注入 g_data2 新闻卡（覆盖 标签和标题，保留 正文）。
    仅当取到该分类真实条目才覆盖；否则保留硬编码（记 FALLBACK）。
    机构 / 社区 / 生物医学 为多角色叙事，保留 agent 维护（记 _NOTE）。"""
    news = get_news(limit=120)
    if not news:
        print("[fetch_news] 取数失败，新闻头条沿用硬编码兜底")
        return
    used = set()
    for prefix, n, cat in _NEWS_CARDS:
        pool = [x for x in news if (cat is None or x["cat"] == cat) and id(x) not in used]
        if not pool:
            FALLBACK.append("新闻_%s" % prefix)
            continue
        for i, x in enumerate(pool[:n], 1):
            used.add(id(x))
            d = ("（%s）" % x["date"]) if x["date"] else ""
            D["%s%d_标签和标题" % (prefix, i)] = (x["title"] + d)[:48]
    # 生物医学：多角色叙事，按规范保留 agent 维护（g_data2 硬编码 5 主题 tag+正文），
    # 不覆盖——新闻源 bio 分类不纯净，曾将"辽宁中考减负"等教育/社会新闻误归入生物医学。
    _NOTE.append("生物医学(agent维护)")
    # 机构 / 社区 保留 agent 维护，本模块仅提供取数接口
    _NOTE.append("机构观点(agent维护)")
    _NOTE.append("社区话题(agent维护)")
    if FALLBACK:
        print("[fetch_news] 以下项使用硬编码兜底(非实时):", ", ".join(FALLBACK[:8]),
              "…(共%d项)" % len(FALLBACK))
    if _NOTE:
        print("[fetch_news] agent维护(非取数失败):", ", ".join(_NOTE))


if __name__ == "__main__":
    # 自测：打印取到的新闻分类分布
    n = get_news(limit=120)
    print("取到新闻 %d 条" % len(n))
    from collections import Counter
    c = Counter(x["cat"] for x in n)
    print("分类分布:", dict(c))
    print("热搜:", [h["name"] for h in get_hot_keywords()])
    print("工行新闻:", [x["title"] for x in get_stock_news("601398")])
