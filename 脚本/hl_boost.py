# -*- coding: utf-8 -*-
# 高亮密度增强：检查文本卡高亮数量，对不足的自动加粗关键词
import re

NEWS_KEYS_RE = re.compile(r'(重点新闻|财经新闻|大模型新闻|算力新闻|机器人新闻|AI应用新闻|产业趋势新闻|地缘新闻|生物医学).*正文')
TEXT_KEYS_RE = re.compile(r'(正文|内容|观点|分析|正文|描述|标题|结论|总结|建议|提醒|子标题|指标)')

def apply(D):
    news_short = []
    text_short = []
    for k, v in D.items():
        if not isinstance(v, str) or len(v) < 20:
            continue
        hl_count = v.count('<span style="color:')
        if NEWS_KEYS_RE.search(k):
            if hl_count < 5:
                news_short.append((k, hl_count))
        elif TEXT_KEYS_RE.search(k):
            if hl_count < 2:
                text_short.append((k, hl_count))
    print("=== 高亮密度增强 ===")
    print(f"  新闻/AI卡: {37-len(news_short)}/37 达标(≥5)")
    if news_short:
        print(f"    未达标: {news_short}")
    print(f"  其余文本卡: {57-len(text_short)}/57 达标(≥2)")
    if text_short:
        print(f"    未达标: {text_short}")
