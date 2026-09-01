# -*- coding: utf-8 -*-
import re

for f in ["template.html", "老盛早知道_20260901.html"]:
    h = open(f, encoding="utf-8").read()
    print("====", f)
    for cls in ["tab-panel", "tab-content", "summary-card", "highlight-item",
                "market-block", "stock-card", "sentiment-item", "sub-title",
                "overview-card", "grid-4", "card-body", "card-title"]:
        n = len(re.findall(r'class="[^"]*' + re.escape(cls), h))
        print("  %-16s %d" % (cls, n))
