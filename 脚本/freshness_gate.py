# -*- coding: utf-8 -*-
# 防照抄门禁：与上一期报告做句子级比对
import os, re, glob, datetime

def run(current_html):
    """Compare current report with previous day's report.
    Returns (ok, ratio, repeats). ok=False if narrative copy ratio > 40%."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cur_date = os.path.basename(current_html).replace("老盛早知道_", "").replace(".html", "")
    try:
        cur_d = datetime.date(int(cur_date[:4]), int(cur_date[4:6]), int(cur_date[6:8]))
    except:
        return (True, 0.0, [])

    prev_d = cur_d - datetime.timedelta(days=1)
    prev_file = os.path.join(root, "老盛早知道_%s.html" % prev_d.strftime("%Y%m%d"))
    if not os.path.exists(prev_file):
        # try 2 days back (weekend)
        for back in range(1, 5):
            alt = cur_d - datetime.timedelta(days=back)
            alt_file = os.path.join(root, "老盛早知道_%s.html" % alt.strftime("%Y%m%d"))
            if os.path.exists(alt_file):
                prev_file = alt_file
                break
        else:
            print("=== 防照抄门禁 ===")
            print("无历史报告可比对，跳过")
            return (True, 0.0, [])

    with open(current_html, encoding="utf-8") as f:
        cur_text = re.sub(r'<[^>]+>', ' ', f.read())
    with open(prev_file, encoding="utf-8") as f:
        prev_text = re.sub(r'<[^>]+>', ' ', f.read())

    # Split into sentences
    cur_sents = set(s.strip() for s in re.split(r'[。！？\n]', cur_text) if len(s.strip()) > 15)
    prev_sents = set(s.strip() for s in re.split(r'[。！？\n]', prev_text) if len(s.strip()) > 15)

    common = cur_sents & prev_sents
    # Filter out pure market data sentences (contain digits + dots)
    narrative_common = [s for s in common if not re.search(r'\d+\.\d+', s)]
    market_common = [s for s in common if re.search(r'\d+\.\d+', s)]

    total = len(cur_sents)
    repeats = len(common)
    ratio = repeats / total if total > 0 else 0

    print("=== 防照抄门禁 ===")
    print(f"新报告叙事句数: {total}  相同句: {repeats}  整体占比: {ratio:.1%}")
    print(f"  ├ 市场数据句(可接受,T-1共享): {len(market_common)}")
    print(f"  └ 叙事/分析句(照抄风险): {len(narrative_common)}")
    print(f"比对对象: {os.path.basename(prev_file)}")

    ok = ratio < 0.40
    if ok:
        print("判定: PASS ✅")
    else:
        print("判定: FAIL ❌")
    return (ok, ratio, list(common))
