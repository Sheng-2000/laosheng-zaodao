#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
老盛早知道报告质量检查脚本
"""
from bs4 import BeautifulSoup
import re
import sys

REPORT = "老盛早知道_20260621.html"
T_DATE = "20260621"  # 报告日期
T_1_DATE = "20260618"  # 数据日期（T-1，周末/假期取最近交易日）

# 读取报告
with open(REPORT, "r", encoding="utf-8") as f:
    raw = f.read()

soup = BeautifulSoup(raw, "html.parser")

errors = []
warnings = []

def check(name, condition, error_msg):
    if not condition:
        errors.append(f"❌ {name}: {error_msg}")
    else:
        print(f"✅ {name}")

print("=" * 70)
print(f"报告质量检查：{REPORT}")
print("=" * 70)

# 一、数据及时性检查
print("\n【一、数据及时性检查】")
# 日期可能有多种格式：20260621 / 2026年6月21日 / 6月21日
# 报告日期
report_date_patterns = [T_DATE, f"2026年{T_DATE[4:6].lstrip('0')}月{T_DATE[6:8].lstrip('0')}日", 
                        f"{T_DATE[4:6].lstrip('0')}月{T_DATE[6:8].lstrip('0')}日"]
data_date_patterns = [T_1_DATE, f"2026年{T_1_DATE[4:6].lstrip('0')}月{T_1_DATE[6:8].lstrip('0')}日",
                      f"{T_1_DATE[4:6].lstrip('0')}月{T_1_DATE[6:8].lstrip('0')}日"]

# 旧日期（T-3及更早）
old_date_numbers = ["20260615", "20260612", "20260611", "20260610", "20260609"]
old_date_patterns = []
for d in old_date_numbers:
    old_date_patterns.append(d)
    old_date_patterns.append(f"2026年{d[4:6].lstrip('0')}月{d[6:8].lstrip('0')}日")
    old_date_patterns.append(f"{d[4:6].lstrip('0')}月{d[6:8].lstrip('0')}日")

t_date_count = sum(raw.count(p) for p in report_date_patterns)
data_date_count = sum(raw.count(p) for p in data_date_patterns)
old_date_count = sum(raw.count(p) for p in old_date_patterns)

print(f"  报告日期({report_date_patterns[1]})出现次数: {t_date_count}")
print(f"  数据日期({data_date_patterns[1]})出现次数: {data_date_count}")
print(f"  旧日期(T-3及更早)出现次数: {old_date_count}")

if old_date_count > 3:
    warnings.append(f"旧日期残留较多: {old_date_count}处")
if data_date_count < 10:
    warnings.append(f"新数据覆盖不足: {data_date_count}处")

# 二、结构与样式检查
print("\n【二、结构与样式检查】")
line_count = len(raw.splitlines())
css_end_line = raw[:raw.find("</style>")].count("\n") + 1
print(f"  文件总行数: {line_count}")
print(f"  </style>结束行: {css_end_line}")

tab_panels = len(soup.find_all("div", class_="tab-panel"))
sub_titles = len(soup.find_all("div", class_="sub-title"))
stock_cards = len(soup.find_all("div", class_="stock-card"))
market_blocks = len(soup.find_all("div", class_="market-block"))
sentiment_items = len(soup.find_all("div", class_="sentiment-item"))

print(f"  tab-panel: {tab_panels}")
print(f"  sub-title: {sub_titles}")
print(f"  stock-card: {stock_cards}")
print(f"  market-block: {market_blocks}")
print(f"  sentiment-item: {sentiment_items}")

check("文件行数", 3600 <= line_count <= 4100, f"行数{line_count}不在3600-4100范围内")
check("CSS结束位置", 1300 <= css_end_line <= 1800, f"</style>在第{css_end_line}行，不在1300-1800范围内")
check("tab-panel数量", tab_panels == 8, f"应为8，实际{tab_panels}")
check("sub-title数量", 25 <= sub_titles <= 27, f"应为25-27，实际{sub_titles}")
check("stock-card数量", stock_cards == 13, f"应为13，实际{stock_cards}")
check("market-block数量", market_blocks == 8, f"应为8，实际{market_blocks}")
check("sentiment-item数量", sentiment_items == 9, f"应为9，实际{sentiment_items}")

# Tailwind类名污染
tailwind_patterns = [r'\bw-\d+', r'\bh-\d+', r'\bp-\d+', r'\bm-\d+', r'\btext-\w+-\d+', r'\bbg-\w+-\d+']
tailwind_found = []
for pattern in tailwind_patterns:
    matches = re.findall(pattern, raw)
    if matches:
        tailwind_found.extend(matches[:5])
if tailwind_found:
    warnings.append(f"疑似Tailwind类名: {tailwind_found}")
else:
    print("✅ 无Tailwind类名污染")

# 占位符和缺失数据
placeholders = re.findall(r'\{\{[^}]+\}\}', raw)
no_data = raw.count('"--"') + raw.count('>--<')
check("占位符数量", len(placeholders) == 0, f"剩余{len(placeholders)}个占位符: {placeholders[:5]}")
check("缺失数据", no_data == 0, f"发现{no_data}处缺失数据标记(--)")

# 三、数据准确性检查
print("\n【三、数据准确性检查】")

# 涨红跌绿检查：class="up"不能包含负值，class="down"不能包含正值
def check_up_down_consistency():
    up_elems = soup.find_all(class_=lambda x: x and "up" in x.split())
    down_elems = soup.find_all(class_=lambda x: x and "down" in x.split())
    
    up_errors = []
    down_errors = []
    
    for elem in up_elems:
        text = elem.get_text(strip=True)
        # 如果包含 - 号（不是 -- 无数据），且不含 + 号，可能有问题
        if "-" in text and "+" not in text and "--" not in text:
            # 排除某些语义，比如 "净流入" 等
            if not any(k in text for k in ["净流入", "上涨", "大涨", "反弹", "创新高", "高配"]):
                up_errors.append((text[:50], elem.get("class")))
    
    for elem in down_elems:
        text = elem.get_text(strip=True)
        if "+" in text and "-" not in text:
            down_errors.append((text[:50], elem.get("class")))
    
    return up_errors, down_errors

up_errors, down_errors = check_up_down_consistency()
check("涨红跌绿一致性", len(up_errors) == 0 and len(down_errors) == 0, 
      f"up含负值{len(up_errors)}处，down含正值{len(down_errors)}处")
if up_errors:
    for e in up_errors[:3]:
        print(f"    up异常: {e[0]}")
if down_errors:
    for e in down_errors[:3]:
        print(f"    down异常: {e[0]}")

# 四、4个必须丰富区域字数检查
print("\n【四、必须丰富区域字数检查（要求≥120字）】")

# 1. 机构观点
tab4 = soup.find("div", id="panel-4")
institute_items = []
if tab4:
    # 机构观点在 institute-card 容器内的 institute-body 中
    for card in tab4.find_all("div", class_="institute-card"):
        body = card.find("div", class_="institute-body")
        if body:
            text = body.get_text(strip=True)
            if any(name in text for name in ["中信证券", "高盛", "摩根士丹利", "野村", "瑞银", "兴业"]):
                institute_items.append(text)

print(f"  机构观点: {len(institute_items)}条")
for i, text in enumerate(institute_items, 1):
    status = "✅" if len(text) >= 120 else "❌"
    print(f"    {status} 机构{i}: {len(text)}字")
    if len(text) < 120:
        errors.append(f"机构观点{i}字数不足: {len(text)}字")

# 2. 高股息板块
value_cards = []
if tab4:
    for card in tab4.find_all("div", class_="card-body"):
        text = card.get_text(strip=True)
        if any(k in text for k in ["银行板块", "公用事业", "电力", "央企", "高股息"]):
            value_cards.append(text)

print(f"  高股息板块卡片: {len(value_cards)}张")
for i, text in enumerate(value_cards, 1):
    status = "✅" if len(text) >= 120 else "❌"
    print(f"    {status} 板块{i}: {len(text)}字")
    if len(text) < 120:
        errors.append(f"高股息板块{i}字数不足: {len(text)}字")

# 3. 社区热门话题
tab6 = soup.find("div", id="panel-6")
community_topics = []
if tab6:
    # 找到"社区热门话题"sub-title，然后找其后紧跟的flex column容器
    sub_title = tab6.find("div", class_="sub-title", string=lambda x: x and "社区热门话题" in x)
    if sub_title:
        # 下一个兄弟是 sub-section 或 div flex column
        container = sub_title.find_parent("div", class_="sub-section")
        if container:
            # 找到 flex column 容器
            flex_container = container.find("div", style=lambda x: x and "display:flex" in x and "flex-direction:column" in x)
            if flex_container:
                # 直接子div就是话题容器（padding:16px, border-radius:12px）
                community_topics = [div for div in flex_container.find_all("div", recursive=False) 
                                    if div.get("style") and "padding:16px" in div.get("style") and "border-radius:12px" in div.get("style")]

print(f"  社区话题: {len(community_topics)}个")
for i, topic in enumerate(community_topics, 1):
    text = topic.get_text(strip=True)
    spans = len(topic.find_all("span", style=re.compile(r"color")))
    status = "✅" if len(text) >= 120 else "❌"
    print(f"    {status} 话题{i}: {len(text)}字, {spans}处高亮")
    if len(text) < 120:
        errors.append(f"社区话题{i}字数不足: {len(text)}字")

# 4. 今日操作建议
tab7 = soup.find("div", id="panel-7")
op_cards = []
if tab7:
    # 找到今日操作建议grid
    grids = tab7.find_all("div", style=lambda x: x and "display:grid" in x)
    for grid in grids:
        items = grid.find_all("div", style=lambda x: x and "padding:16px" in x and "border-radius:12px" in x)
        if len(items) >= 4:
            op_cards = items
            break

print(f"  今日操作建议卡片: {len(op_cards)}张")
for i, card in enumerate(op_cards, 1):
    text = card.get_text(strip=True)
    spans = len(card.find_all("span", style=re.compile(r"color")))
    status = "✅" if len(text) >= 120 else "❌"
    print(f"    {status} 建议{i}: {len(text)}字, {spans}处高亮")
    if len(text) < 120:
        errors.append(f"操作建议{i}字数不足: {len(text)}字")

# 五、数据完整性检查
print("\n【五、数据完整性检查】")

# 检查关键数据是否都有填充
key_checks = [
    ("上证指数", "上证指数"),
    ("深证成指", "深证成指"),
    ("创业板指", "创业板指"),
    ("科创50", "科创50"),
    ("恒生指数", "恒生指数"),
    ("道琼斯", "道琼斯"),
    ("标普500", "标普500"),
    ("纳斯达克", "纳斯达克"),
    ("WTI原油", "WTI原油"),
    ("国际黄金", "国际黄金"),
    ("USD/CNY", "USD/CNY"),
    ("10年期", "10年期"),
    ("BTC", "BTC"),
    ("ETH", "ETH"),
]

for label, keyword in key_checks:
    count = raw.count(keyword)
    print(f"  {label}: {count}处")

# 六、交互功能检查
print("\n【六、交互功能检查】")
switchTab = "function switchTab" in raw
has_id_match = "panel-" in raw and "tab-" in raw
scroll_top = "scrollTo" in raw or "scrollTop" in raw
check("switchTab函数", switchTab, "未找到switchTab函数")
check("id匹配逻辑", has_id_match, "未找到panel-/tab- id匹配")
check("滚动到顶部", scroll_top, "未找到滚动到顶部逻辑")

# 七、总结
print("\n" + "=" * 70)
print("检查总结")
print("=" * 70)

if warnings:
    print("\n⚠️ 警告:")
    for w in warnings:
        print(f"  - {w}")

if errors:
    print(f"\n❌ 发现 {len(errors)} 个问题，报告未通过质量检查:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("\n✅ 全部检查通过，报告质量合格！")
    sys.exit(0)
