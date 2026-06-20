#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""老盛早知道 20260619 生成报告基础质量检查"""

import re

FILE_PATH = '老盛早知道_20260620.html'

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    content = ''.join(lines)

print('=' * 50)
print('基础质量检查报告')
print('=' * 50)
print(f'文件行数: {len(lines)}')
print(f'文件大小: {len(content)/1024:.1f} KB')
print(f'剩余占位符数量: {len(re.findall(r"\{\{[^}]+\}\}", content))}')
print(f'"--" 数量: {content.count("\"--\"") + content.count(">--<")}')
print(f'tab-panel 数量: {len(re.findall(r"class=\"tab-panel(?:\s+active)?\"", content))}')
print(f'sub-title 数量: {len(re.findall(r"class=\"sub-title\"", content))}')
print(f'stock-card 数量: {len(re.findall(r"class=\"stock-card\"", content))}')
print(f'market-block 数量: {len(re.findall(r"class=\"market-block\"", content))}')
print(f'switchTab 函数存在: {"function switchTab" in content}')

# Header ticker 检查
print()
print('Header Ticker 检查:')
ticker_sections = re.findall(r'<div class="ticker-item">(.*?)</div>', content, re.DOTALL)
for sec in ticker_sections:
    name_match = re.search(r'<span class="t-name">([^<]+)</span>', sec)
    cls_match = re.search(r'<span class="(up|down|neutral)">([+-]?\d+\.\d+%)</span>', sec)
    if name_match and cls_match:
        name = name_match.group(1)
        cls, chg = cls_match.group(1), cls_match.group(2)
        ok = (cls == 'up' and chg.startswith('+')) or (cls == 'down' and chg.startswith('-'))
        print(f'  {name}: class={cls}, chg={chg}, OK={ok}')

# 关注标的 class 检查
print()
print('关注标的涨跌 class 检查:')
stock_changes = re.findall(r'<div class="stock-change (up|down|neutral)">', content)
print(f'  stock-change 分布: up={stock_changes.count("up")}, down={stock_changes.count("down")}, neutral={stock_changes.count("neutral")}')

# market-row class 检查
print()
print('market-row class 检查:')
market_vals = re.findall(r'<span class="market-val (up|down|neutral)">', content)
print(f'  market-val 分布: up={market_vals.count("up")}, down={market_vals.count("down")}, neutral={market_vals.count("neutral")}')

# up/down 一致性检查
print()
print('up/down 类一致性检查:')
up_neg = len(re.findall(r'class="up"[^>]*>[^<]*-\d', content))
down_pos = len(re.findall(r'class="down"[^>]*>[^<]*\+\d', content))
print(f'  class="up" 含负值: {up_neg}')
print(f'  class="down" 含正值: {down_pos}')

# market-block border 颜色检查
print()
print('market-block border 颜色检查:')
borders = re.findall(r'border-top:2px solid (#[0-9a-fA-F]{6}|rgba\(255,255,255,0\.12\))', content)
print(f'  border 颜色分布: {dict((c, borders.count(c)) for c in sorted(set(borders)))}')

# 检查概览卡 class
print()
print('概览卡涨跌 class 检查:')
summary_changes = re.findall(r'<span class="summary-card-change (up|down|neutral)">', content)
print(f'  summary-card-change 分布: up={summary_changes.count("up")}, down={summary_changes.count("down")}, neutral={summary_changes.count("neutral")}')

print()
print('=' * 50)
