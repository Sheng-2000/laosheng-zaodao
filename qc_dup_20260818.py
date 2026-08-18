import re

def text_blocks(fn):
    s = open(fn, encoding='utf-8').read()
    pats = {
        'card-body':   r'class="card-body">(.*?)</div>',
        'card-title':  r'class="card-title">(.*?)</div>',
        'section-desc':r'class="section-desc[^"]*">(.*?)</div>',
        'risk':        r'class="risk[^"]*">(.*?)</div>',
        'timeline-detail': r'class="timeline-detail">(.*?)</div>',
        'summary':     r'class="summary[^"]*">(.*?)</div>',
        'sentiment':   r'class="sentiment[^"]*">(.*?)</div>',
        'community':   r'class="community[^"]*">(.*?)</div>',
        'p':           r'<p[^>]*>(.*?)</p>',
        'desc':        r'class="[^"]*desc[^"]*">(.*?)</div>',
    }
    res = {}
    for typ, pat in pats.items():
        for m in re.finditer(pat, s, re.S):
            txt = re.sub(r'<[^>]+>', '', m.group(1))
            txt = re.sub(r'\s+', '', txt)
            if len(txt) > 18:
                line = s[:m.start()].count('\n') + 1
                res.setdefault(typ, []).append((line, txt))
    return res

b18 = text_blocks('老盛早知道_20260818.html')
b17 = text_blocks('老盛早知道_20260817.html')

set17 = {t for typ, items in b17.items() for _, t in items}
# 也把 8/17 中常见模板固定文案排除（这些本来就该相同）
TEMPLATE_FIXED = {
    '今日市场全景','全球市场速览','国内外要闻','AI前沿动态','机构价值投资观点',
    '高股息板块深度分析','社区热门话题','今日操作建议','市场热点','风险提示',
    '本日报由AI助手生成','数据来源','仅供研究参考','投资有风险',
}

print("==================== 8/18 中与 8/17 完全相同的文本块 ====================")
total = 0
by_type = {}
for typ, items in b18.items():
    for line, t in items:
        if t in set17:
            total += 1
            by_type[typ] = by_type.get(typ, 0) + 1
            print(f"[{typ:14s} L{line:4d}] {t[:78]}")
print("\n==================== 统计 ====================")
print("陈旧块总数:", total)
for k, v in sorted(by_type.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
print("\n8/18 内容块总数:", sum(len(v) for v in b18.values()))
