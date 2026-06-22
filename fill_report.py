#!/usr/bin/env python3
"""Fill template placeholders and adjust up/down classes/borders."""
import json, re
from pathlib import Path
from collections import Counter

base = Path('/Users/sheng/Sheng/MyData/02-任务空间/家庭生活/理财支撑/大福・老盛早知道')

# Load mappings
m = {}
for name in ['data_base_20260622.json', 'data_content_a_20260622.json', 'data_content_b_20260622.json']:
    p = base / name
    if p.exists():
        d = json.loads(p.read_text(encoding='utf-8'))
        m.update(d)
        print(f'Loaded {name}: {len(d)} keys')
    else:
        print(f'Missing {name}')
print('Total merged keys:', len(m))

# Load template
tmpl = (base / 'template.html').read_text(encoding='utf-8')

# Replace placeholders
missing = set()
def repl(match):
    key = match.group(1)
    if key in m:
        return str(m[key])
    missing.add(key)
    return match.group(0)

text = re.sub(r'\{\{([^}]+)\}\}', repl, tmpl)
print('Missing placeholders:', len(missing))
if missing:
    for k in sorted(missing)[:50]:
        print(' ', k)

# Classify sign
def classify_sign(val):
    v = val.strip()
    # explicit chinese sell/outflow
    if any(x in v for x in ['净卖出','净流出','流出','谨慎偏空','偏空','下跌','跌','负']):
        # but if it also has explicit + pct and no -, keep up
        if re.search(r'\+\d+\.?\d*%', v) and not re.search(r'-\d+\.?\d*%', v):
            return 'up'
        return 'down'
    if any(x in v for x in ['净流入','净买入','买入','上涨','涨','偏多']):
        if re.search(r'-\d+\.?\d*%', v) and not re.search(r'\+\d+\.?\d*%', v):
            return 'down'
        return 'up'
    # percentage / BP sign
    pct = re.search(r'([+-])\d+\.?\d*(?:%|BP|bp)', v)
    if pct:
        return 'up' if pct.group(1) == '+' else 'down'
    # signed numbers with units like 亿/万/港元
    signed = re.search(r'^([+-])\d+\.?\d*', v)
    if signed:
        return 'up' if signed.group(1) == '+' else 'down'
    # compare up/down counts in 涨跌家数 style
    up_m = re.search(r'上涨\s*(\d+)', v)
    down_m = re.search(r'下跌\s*(\d+)', v)
    if up_m and down_m:
        return 'up' if int(up_m.group(1)) >= int(down_m.group(1)) else 'down'
    return 'neutral'

# Update header ticker t-chg classes
def ticker_repl(match):
    val = match.group(1)
    cls = classify_sign(val)
    return f'<span class="t-chg {cls}">{val}</span>'
text = re.sub(r'<span class="t-chg">([^<]+)</span>', ticker_repl, text)

# Update uv-metric-value classes (some templates hardcode 'up')
def uv_repl(match):
    val = match.group(1)
    cls = classify_sign(val)
    return f'<div class="uv-metric-value {cls}">{val}</div>'
text = re.sub(r'<div class="uv-metric-value up">([^<]+)</div>', uv_repl, text)

# Update market-val spans and block borders
block_open = re.compile(r'<div class="market-block" style="border-top:2px solid rgba\(255,255,255,0\.12\);">')

# Process block by block
parts = block_open.split(text)
out_parts = [parts[0]]
for part in parts[1:]:
    # find end of block (next </div> matching this block). We'll use a simple count.
    # part starts with block content until its closing </div>
    depth = 0
    end = 0
    in_tag = False
    for i,ch in enumerate(part):
        if part[i:i+5] == '<div ':
            depth += 1
        elif part[i:i+6] == '</div>':
            if depth == 0:
                end = i
                break
            depth -= 1
    if end == 0:
        end = len(part)
    block_content = part[:end]
    rest = part[end:]
    # update market-val classes within block
    sign_counts = Counter()
    def mv_repl(match):
        val = match.group(1)
        cls = classify_sign(val)
        sign_counts[cls] += 1
        return f'<span class="market-val {cls}">{val}</span>'
    block_content_new = re.sub(r'<span class="market-val neutral">([^<]+)</span>', mv_repl, block_content)
    # handle rows with nested span like 成交额 (keep neutral if no clear sign)
    # determine border color: if any up, red; if any down and no up, green; else gray
    if sign_counts.get('up',0) > 0 and sign_counts.get('down',0) == 0:
        border = '#f85149'
    elif sign_counts.get('down',0) > 0 and sign_counts.get('up',0) == 0:
        border = '#3fb950'
    else:
        # mixed: use majority
        if sign_counts.get('up',0) >= sign_counts.get('down',0):
            border = '#f85149'
        else:
            border = '#3fb950'
    out_parts.append(f'<div class="market-block" style="border-top:2px solid {border};">')
    out_parts.append(block_content_new)
    out_parts.append(rest)
text = ''.join(out_parts)

# Output file
out_file = base / '老盛早知道_20260622.html'
out_file.write_text(text, encoding='utf-8')
print('Wrote', out_file, 'lines', text.count('\n'))

# Verify placeholders left
left = set(re.findall(r'\{\{([^}]+)\}\}', text))
print('Leftover placeholders:', len(left))
for k in sorted(left)[:50]:
    print(' ', k)
