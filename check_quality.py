#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
质量检查脚本
"""
from bs4 import BeautifulSoup
import re

REPORT = "老盛早知道_20260621.html"

with open(REPORT, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

print("=" * 60)
print("结构检查")
print("=" * 60)
print(f"tab-panel 数量: {len(soup.find_all('div', class_='tab-panel'))} (期望 8)")
print(f"sub-title 数量: {len(soup.find_all('div', class_='sub-title'))} (期望 25-26)")
print(f"stock-card 数量: {len(soup.find_all('div', class_='stock-card'))} (期望 13)")
print(f"market-block 数量: {len(soup.find_all('div', class_='market-block'))} (期望 8)")
print(f"sentiment-item 数量: {len(soup.find_all('div', class_='sentiment-item'))} (期望 9)")

# 检查 card-body 中的 span 高亮数量
cards = soup.find_all("div", class_="card-body")
print("\n" + "=" * 60)
print(f"card-body 卡片数量: {len(cards)}")
print("=" * 60)
for i, card in enumerate(cards, 1):
    spans = card.find_all("span", style=re.compile(r"color"))
    text = card.get_text(strip=True)
    # 只统计有颜色的 span
    colored = [s for s in spans if "color" in s.get("style", "")]
    if len(colored) < 2:
        print(f"[低亮] card {i}: {len(colored)} 处高亮, {len(text)} 字")
    if i <= 20:
        print(f"card {i}: {len(colored)} 处高亮, {len(text)} 字")

# 检查4个必须丰富区域
print("\n" + "=" * 60)
print("4个必须丰富区域字数检查（要求每个占位符/段落 ≥120字）")
print("=" * 60)

# 机构观点：在 Tab 4 的机构观点卡片中
institute_cards = []
tab4 = soup.find("div", id="panel-4")
if tab4:
    # 找到所有机构卡片
    for card in tab4.find_all("div", class_="card-body"):
        text = card.get_text(strip=True)
        if any(name in text for name in ["中信证券", "高盛", "摩根士丹利", "野村", "瑞银", "兴业"]):
            institute_cards.append(text)
            print(f"机构观点卡片: {len(text)} 字")

# 高股息板块深度分析：Tab 4 中带有"高股息"等关键词的卡片
value_cards = []
if tab4:
    for card in tab4.find_all("div", class_="card-body"):
        text = card.get_text(strip=True)
        if any(k in text for k in ["银行板块", "公用事业", "电力", "央企"]):
            value_cards.append(text)
            print(f"高股息/价值卡片: {len(text)} 字")

# 社区热门话题：Tab 6
tab6 = soup.find("div", id="panel-6")
if tab6:
    community_cards = tab6.find_all("div", class_="card-body")
    print(f"\n社区话题卡片数量: {len(community_cards)}")
    for i, card in enumerate(community_cards[:12], 1):
        text = card.get_text(strip=True)
        spans = card.find_all("span", style=re.compile(r"color"))
        print(f"社区话题 card {i}: {len(text)} 字, {len(spans)} 处高亮")

# 今日操作建议：Tab 7
tab7 = soup.find("div", id="panel-7")
if tab7:
    op_cards = tab7.find_all("div", class_="card-body")
    print(f"\n今日总结/操作建议卡片数量: {len(op_cards)}")
    for i, card in enumerate(op_cards[:10], 1):
        text = card.get_text(strip=True)
        spans = card.find_all("span", style=re.compile(r"color"))
        print(f"总结/操作 card {i}: {len(text)} 字, {len(spans)} 处高亮")

# 检查占位符和缺失数据
with open(REPORT, "r", encoding="utf-8") as f:
    raw = f.read()
print("\n" + "=" * 60)
print("占位符/缺失数据检查")
print("=" * 60)
print(f"剩余 {{...}} 占位符: {len(re.findall(r'\\{\\{[^}]+\\}\\}', raw))}")
print(f'"--" 出现次数: {raw.count(chr(34)+chr(45)+chr(45)+chr(34))}')
print(f'">--<" 出现次数: {raw.count(">--<")}')
