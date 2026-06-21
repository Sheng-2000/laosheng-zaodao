#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

REPORT = "老盛早知道_20260621.html"

with open(REPORT, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 找到社区热门话题区域
tab6 = soup.find("div", id="panel-6")
if tab6:
    # 找到所有包含“老盛观点”的话题卡片
    topics = tab6.find_all("div", class_="laosheng-view")
    print(f"社区话题数量: {len(topics)}")
    for i, lv in enumerate(topics, 1):
        parent = lv.find_parent("div", style=lambda x: x and "padding:16px" in x)
        if parent:
            title = parent.find("div", style=lambda x: x and "font-size:15px" in x)
            title_text = title.get_text(strip=True) if title else f"话题{i}"
            all_text = parent.get_text(strip=True)
            spans = parent.find_all("span", style=re.compile(r"color"))
            print(f"\n话题{i}: {title_text}")
            print(f"  总字数: {len(all_text)}")
            print(f"  高亮数: {len(spans)}")

# 检查机构观点
print("\n" + "=" * 60)
print("机构观点字数")
tab4 = soup.find("div", id="panel-4")
if tab4:
    institutes = tab4.find_all("div", class_="institute-body")
    print(f"机构观点数量: {len(institutes)}")
    for i, inst in enumerate(institutes, 1):
        text = inst.get_text(strip=True)
        spans = inst.find_all("span", style=re.compile(r"color"))
        print(f"机构{i}: {len(text)}字, {len(spans)}处高亮")

# 检查今日操作建议
print("\n" + "=" * 60)
print("今日操作建议字数")
tab7 = soup.find("div", id="panel-7")
if tab7:
    # 找到今日操作建议区域
    op_section = None
    for div in tab7.find_all("div"):
        if "今日操作建议" in div.get_text(strip=True) and "display:grid" in div.get("style", ""):
            op_section = div
            break
    if op_section:
        op_items = op_section.find_all("div", style=lambda x: x and "padding:16px" in x and "border-radius:12px" in x)
        print(f"操作建议数量: {len(op_items)}")
        for i, item in enumerate(op_items, 1):
            text = item.get_text(strip=True)
            spans = item.find_all("span", style=re.compile(r"color"))
            print(f"建议{i}: {len(text)}字, {len(spans)}处高亮")
