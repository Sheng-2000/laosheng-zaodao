#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成2026年4月17日老盛早知道 - 保持与4月16日完全相同的风格
"""

# 读取4月16日文件作为模板基础
with open('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/老盛的每日快讯/WorkBuddy版/老盛早知道_20260416.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 替换标题日期
template = template.replace('<title>老盛早知道 · 2026年4月16日</title>', '<title>老盛早知道 · 2026年4月17日</title>')

# 替换header中的日期和副标题
old_header = '''<div class="brand-title">
        <div class="brand-en-row">
          <span class="brand-en">LAO SHENG MORNING BRIEF</span>
          <span class="brand-issue">NO.20260416</span>
        </div>
        <div class="brand-main-row">
          <span class="brand-signal"><span class="brand-name">老盛</span></span>
          <span class="brand-sep"></span>
          <span class="brand-zaodao">早知道</span>
        </div>
      </div>'''

new_header = '''<div class="brand-title">
        <div class="brand-en-row">
          <span class="brand-en">LAO SHENG MORNING BRIEF</span>
          <span class="brand-issue">NO.20260417</span>
        </div>
        <div class="brand-main-row">
          <span class="brand-signal"><span class="brand-name">老盛</span></span>
          <span class="brand-sep"></span>
          <span class="brand-zaodao">早知道</span>
        </div>
      </div>'''

template = template.replace(old_header, new_header)

# 替换header-meta中的日期
old_meta = '''<div class="header-meta">
      <div class="header-date">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        2026年4月16日 · 星期三
      </div>
      <div class="header-tags">
        <span class="header-tag tag-blue">关税政策落地</span>
        <span class="header-tag tag-green">创业板+2.27%</span>
        <span class="header-tag tag-purple">宁德时代Q1超预期</span>
      </div>
    </div>'''

new_meta = '''<div class="header-meta">
      <div class="header-date">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        2026年4月17日 · 星期四
      </div>
      <div class="header-tags">
        <span class="header-tag tag-blue">美伊框架协议将达成</span>
        <span class="header-tag tag-green">创业板创11年新高</span>
        <span class="header-tag tag-purple">GPT-6发布催化</span>
      </div>
    </div>'''

template = template.replace(old_meta, new_meta)

# 替换footer中的日期
template = template.replace('老盛早知道 · 2026年4月16日 · 星期三', '老盛早知道 · 2026年4月17日 · 星期四 · 美伊框架协议将达成·创业板创11年新高')

print("基础模板替换完成")
print(f"当前文件长度: {len(template)} 字符")

# 保存中间结果
with open('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/老盛的每日快讯/WorkBuddy版/老盛早知道_20260417.html', 'w', encoding='utf-8') as f:
    f.write(template)

print("文件已保存")
