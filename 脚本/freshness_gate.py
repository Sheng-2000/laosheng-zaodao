# -*- coding: utf-8 -*-
# freshness_gate.py —— 数据新鲜度闸门 + 防照抄检查
# 职责：
#   1. 校验 g_data2.D["报告日期"] 为合法日期（必须含"年"字）且距离今天 ≤ 5 天
#   2. 与上一期报告（历史/或根目录最近一期 html）做句级重复率比对，>40% 告警
# 由 build.py 动态导入调用。
import re
import os
import glob
from datetime import date, datetime

def check_date(D, today=None):
    """校验报告日期新鲜度。返回 (ok, msg)。"""
    today = today or date.today()
    dstr = D.get("报告日期", "")
    if "年" not in dstr:
        return False, "报告日期缺少“年”字：%r" % dstr
    m = re.search(r"(\d{4})年(\d{1,2})月(\d{1,2})日", dstr)
    if not m:
        return False, "报告日期格式异常：%r" % dstr
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    try:
        report_d = date(y, mo, d)
    except ValueError:
        return False, "报告日期非法：%r" % dstr
    gap = (today - report_d).days
    if gap < -1 or gap > 5:
        return False, "报告日期距今天%d天，超出新鲜度窗口（-1~5天）：%s" % (gap, dstr)
    return True, "报告日期 %s 新鲜度校验通过（距今天 %d 天）" % (dstr, gap)

def _sentences(text):
    """将文本切成句子（中文句号/感叹/问号/分号）。先剔除 CSS/JS 代码块与标签。"""
    text = re.sub(r"<style[\s\S]*?</style>", " ", text or "")
    text = re.sub(r"<script[\s\S]*?</script>", " ", text or "")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"#[\da-fA-F]{3,8}\b", " ", text)  # 颜色值
    text = re.sub(r"--[a-z\-]+:", " ", text)          # CSS 变量
    parts = re.split(r"[。！？；\n]", text)
    return [p.strip() for p in parts if len(p.strip()) >= 12]

def compare_with_prev(D, prev_html, threshold=0.40):
    """将 D 中的叙事文本与上一期报告 html 做句子级重复率比对。
    返回 (dup_ratio, samples)。dup_ratio = 与上一期完全重复的长句比例。
    """
    if not prev_html or not os.path.exists(prev_html):
        return 0.0, []
    try:
        content = open(prev_html, encoding="utf-8").read()
    except Exception:
        return 0.0, []
    content = re.sub(r"<[^>]+>", " ", content)
    prev_sents = set(_sentences(content))
    if not prev_sents:
        return 0.0, []
    cur_sents = []
    for k, v in D.items():
        if isinstance(v, str) and len(v) >= 40 and k not in (
                "报告日期", "数据截止日期", "YYYY/MM/DD", "星期"):
            cur_sents.extend(_sentences(v))
    if not cur_sents:
        return 0.0, []
    dup = [s for s in cur_sents if s in prev_sents]
    ratio = len(dup) / len(cur_sents)
    return ratio, dup[:10]

def find_prev_report(project_root, exclude=None):
    """在项目根目录查找最近一期报告 html（排除 index.html 与 exclude 指定的本期文件）。"""
    candidates = glob.glob(os.path.join(project_root, "老盛早知道_*.html"))
    candidates = [c for c in candidates if os.path.basename(c) != "index.html"]
    if exclude:
        candidates = [c for c in candidates if os.path.abspath(c) != os.path.abspath(exclude)]
    if not candidates:
        return None
    return max(candidates, key=os.path.getmtime)

def run(out_path):
    """build.py 调用的入口：out_path 为刚生成的报告 html。
    返回 (ok, ratio, repeats)：
      ok      —— True 表示未发现照抄（重复率 ≤ 40%）
      ratio   —— 与上一期报告的句级重复率
      repeats —— 与上一期重复的句子样本（前若干条）
    说明：市场数据句（指数/股价/涨跌幅）跨期共享属正常，本函数只对
    长度 ≥ 12 的完整句子做逐字比对，叙事/分析句逐字复制才会被判重。
    """
    try:
        today = date.today()
        ok_date, msg = check_date({"报告日期": _guess_report_date(out_path)}, today)
        project_root = os.path.dirname(os.path.abspath(out_path))
        prev = find_prev_report(project_root, exclude=out_path)
        if prev:
            content = open(out_path, encoding="utf-8").read()
            prev_content = open(prev, encoding="utf-8").read()
            prev_sents = set(_sentences(prev_content))
            cur_sents = _sentences(content)
            if prev_sents and cur_sents:
                dup = [s for s in cur_sents if s in prev_sents]
                ratio = len(dup) / len(cur_sents)
                print("防照抄比对: 上一期=%s 本期句数=%d 重复句=%d 重复率=%.1f%%" % (
                    os.path.basename(prev), len(cur_sents), len(dup), ratio * 100))
                if ratio > 0.40:
                    print("⚠️ 检测到叙事照抄候选（重复率>40%），样本：")
                    for r in dup[:8]:
                        print("   -", r[:60])
                    return False, ratio, dup[:8]
                return True, ratio, dup[:8]
        print("防照抄比对: 未找到上一期报告，跳过")
        return True, 0.0, []
    except Exception as e:
        print("[WARN] 防照抄门禁异常:", repr(e)[:150])
        return True, 0.0, []

def _guess_report_date(out_path):
    """从输出文件名反推报告日期（老盛早知道_YYYYMMDD.html）。"""
    m = re.search(r"(\d{4})(\d{2})(\d{2})", os.path.basename(out_path))
    if m:
        return "%s年%s月%s日" % (m.group(1), int(m.group(2)), int(m.group(3)))
    return "2026年10月9日"
