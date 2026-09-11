# -*- coding: utf-8 -*-
"""
title_body_qc.py —— 标题 ⇄ 正文 一致性守门（第 4 套质检）

背景
----
2026-09-08 事故：fetch_news.apply() 把 akshare 真实头条覆盖到新闻卡标题位，
而正文是 agent 按主题撰写的结构化分析 → Tab1 16/16、Tab2 21 张标题与正文
**主题完全不相关**（标题"一线城市住宅租金六连涨"，正文"9月7日A股深强沪弱"）。

判定思路
--------
标题分两类，不能用同一把尺子：
  1. **提炼式/概括式标题**（"注资全景：3570亿怎么分"）——用词本就不必逐字出现在正文，
     覆盖率偏低属正常。
  2. **真错位**——标题讲的是 A 主题，正文通篇讲 B 主题，覆盖率趋近于 0。

因此本脚本**只抓硬错位**（覆盖率 < 阈值），不追求"标题被正文完整覆盖"。
同时跳过：短分区标题（"宏观面""市场面"这类分类标签，天然不与正文逐字重合）。

用法
----
    python 脚本/title_body_qc.py 老盛早知道_YYYYMMDD.html [--verbose]

退出码 0 = 通过；1 = 发现疑似错位。
"""

import io
import re
import sys
import datetime

# 覆盖率阈值：低于此值判为"疑似错位"。
# 实测：正确卡最低约 0.12（"中东·封锁升级与新导弹" vs 霍尔木兹正文）；
# 事故卡约 0.00~0.05（主题完全无关）。取 0.08 留足余量。
THRESHOLD = 0.08
# 有效标题最短长度（去标点/emoji 后）：短于此值视为分区标签，跳过检测
MIN_TITLE_LEN = 6
# 纯章节名白名单：这类是区块标题而非内容标题，正文不必与它逐字重合，跳过检测
SKIP_WORDS = [
    "深度解读", "配置建议", "今日复盘", "关键数字速查", "数字速查",
    "资产配置", "老盛复盘", "操作建议", "风险提示",
]

TARGET = sys.argv[1] if len(sys.argv) > 1 else "老盛早知道_%s.html" % datetime.date.today().strftime("%Y%m%d")
VERBOSE = "--verbose" in sys.argv


def clean_title(t):
    """去掉 emoji / 标点 / 空白，只保留中英数。"""
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"[^\u4e00-\u9fa5A-Za-z0-9]", "", t)
    return t


def grams(s, n):
    return {s[i:i + n] for i in range(len(s) - n + 1)}


def coverage(title, body):
    """标题 2/3-gram 在正文（全文，不截断）中的命中比例。"""
    t = clean_title(title)
    if len(t) < 2:
        return 1.0
    gs = grams(t, 2) | (grams(t, 3) if len(t) >= 3 else set())
    if not gs:
        return 1.0
    b = re.sub(r"\s+", "", body)
    return sum(1 for g in gs if g in b) / len(gs)


def main():
    html = io.open(TARGET, encoding="utf-8").read()
    pos = [(m.group(1), m.start()) for m in re.finditer(r'id="(panel-\d+)"', html)]
    pos.append(("END", len(html)))

    print("=" * 72)
    print("标题 ⇄ 正文 一致性检查   %s" % TARGET)
    print("阈值 %.2f ｜ 短标题(有效长度<%d)跳过" % (THRESHOLD, MIN_TITLE_LEN))
    print("=" * 72)

    total = skipped = 0
    suspects = []
    for k in range(len(pos) - 1):
        pid, st = pos[k]
        seg = html[st:pos[k + 1][1]]
        cards = re.findall(
            r'<div class="card-title">(.*?)</div>\s*<div class="card-body">(.*?)</div>',
            seg, re.S)
        if not cards:
            continue
        print("\n【%s】%d 张" % (pid, len(cards)))
        for n, (t, b) in enumerate(cards, 1):
            title = re.sub(r"<[^>]+>", "", t).strip()
            body = re.sub(r"<[^>]+>", "", b).strip()
            total += 1
            _ct = clean_title(title)
            if len(_ct) < MIN_TITLE_LEN:
                skipped += 1
                if VERBOSE:
                    print("  -[%02d] 跳过(短分区标题)  %s" % (n, title[:40]))
                continue
            if any(w in _ct for w in SKIP_WORDS):
                skipped += 1
                if VERBOSE:
                    print("  -[%02d] 跳过(章节名)  %s" % (n, title[:40]))
                continue
            r = coverage(title, body)
            flag = "OK " if r >= THRESHOLD else "⚠️ "
            if r < THRESHOLD:
                suspects.append((pid, n, title, round(r, 3)))
            if VERBOSE or r < THRESHOLD:
                print("  %s[%02d] %.3f  %s" % (flag, n, r, title[:52]))

    print("\n" + "=" * 72)
    print("卡片总数 %d ｜ 检测 %d ｜ 跳过(短分区标题) %d" % (total, total - skipped, skipped))
    if suspects:
        print("\n❌ 疑似「标题与正文主题不符」 %d 张：" % len(suspects))
        for pid, n, t, r in suspects:
            print("   %s[%02d] %.3f  %s" % (pid, n, r, t[:56]))
        print("\n处理：确认是标题写错 → 改标题使其贴合正文；"
              "确认是正文写错 → 改正文。二者必须同源。")
        return 1
    print("\n✅ 未发现标题与正文主题错位的卡片")
    return 0


if __name__ == "__main__":
    sys.exit(main())
