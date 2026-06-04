#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将白底CSS应用到数据文件"""

import re

# 读取白底模板的CSS
with open('template.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# 找到CSS部分的起始和结束位置
style_start = template_content.find('<style>')
style_end = template_content.find('</style>')

if style_start == -1 or style_end == -1:
    print("ERROR: Cannot find style tags")
    exit(1)

white_css = template_content[style_start + 7:style_end]  # +7 to skip '<style>'
print(f"Found white CSS section: {len(white_css)} characters")

# 读取数据文件
with open('老盛早知道_20260604.html', 'r', encoding='utf-8') as f:
    data_content = f.read()

# 找到数据文件的CSS部分
data_style_start = data_content.find('<style>')
data_style_end = data_content.find('</style>')

if data_style_start == -1 or data_style_end == -1:
    print("ERROR: Cannot find style tags in data file")
    exit(1)

print(f"Found data file CSS section: {len(data_content[data_style_start:data_style_end+8])} characters")

# 替换CSS
new_content = data_content[:data_style_start] + white_css + data_content[data_style_end + 8:]

# 写回文件
with open('老盛早知道_20260604.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUCCESS: Applied white CSS to data file")
print(f"New file size: {len(new_content)} characters")
