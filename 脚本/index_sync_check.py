#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
index_sync_check.py —— 门户 index.html 与本地报告文件的一致性校验

背景：index.html 的 reports 数组按 date 拼文件名打开报告（老盛早知道_YYYYMMDD.html）。
若本地文件与 index 列表漂移（删了文件没改 index → 点击 404；本地有文件 index 没列 → 报告藏起来），
日常生成流程不会报错，只能靠人肉发现。本脚本做双向比对 + 元信息校验。

检查项：
  1. index 有、本地无     → 点击会 404（FAIL）
  2. 本地有、index 无     → 孤儿文件，门户打不开（FAIL）
  3. date 重复            → 门户重复条目（FAIL）
  4. weekday 与实际不符   → 元信息错误（FAIL）
  5. 排序非倒序           → 最新一期不在首位（WARN）
  6. 标题缺失/为空        → 门户标题空（FAIL）
  7. 三方数量（界面可见 / 数组 / 本地文件）→ 界面被 slice 截断导致有文件门户打不到（WARN）

说明第 7 项：门户 = 最新一期大卡(reports[0]) + 历史区(archive = reports.slice(a,b))。
若 archive 切片右界小于数组长度，靠后的条目在界面上被隐藏，
但本地文件还在 → 门户访问不到这些报告（看起来"本地比 index 多"）。

用法：  python3 脚本/index_sync_check.py
退出码：0 = 全部通过；1 = 存在 FAIL
"""
import os
import re
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INDEX = os.path.join(ROOT, "index.html")

WEEKDAY_CN = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


def load_index_reports():
    """解析 index.html 的 const reports = [...] 数组"""
    if not os.path.exists(INDEX):
        return None, ["index.html 不存在: %s" % INDEX]
    s = open(INDEX, encoding="utf-8").read()
    m = re.search(r"const\s+reports\s*=\s*\[([\s\S]*?)\];", s)
    if not m:
        return None, ["未找到 const reports = [...] 数组"]
    items = re.findall(r"\{[^{}]*\}", m.group(1))
    out = []
    for it in items:
        d = re.search(r'date:\s*"(\d{8})"', it)
        w = re.search(r'weekday:\s*"([^"]*)"', it)
        t = re.search(r'title:\s*"([^"]*)"', it)
        out.append({
            "date": d.group(1) if d else None,
            "weekday": w.group(1) if w else "",
            "title": t.group(1) if t else "",
        })
    return out, []


def local_files():
    """本地 老盛早知道_YYYYMMDD.html 的日期集合"""
    out = []
    for fn in os.listdir(ROOT):
        m = re.match(r"^老盛早知道_(\d{8})\.html$", fn)
        if m:
            out.append(m.group(1))
    return sorted(out)


def visible_count(idx_len):
    """解析门户实际可见条数 = 1(最新一期大卡) + 历史区 slice 长度

    常见写法：const archive = reports.slice(1, 7);
    若找不到显式切片，则默认历史区列出剩余全部。
    """
    s = open(INDEX, encoding="utf-8").read()
    m = re.search(r"reports\.slice\(\s*(\d+)\s*,\s*(\d+)\s*\)", s)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return 1 + max(0, min(b, idx_len) - a), "reports.slice(%d,%d)" % (a, b)
    m2 = re.search(r"reports\.slice\(\s*(\d+)\s*\)", s)
    if m2:
        a = int(m2.group(1))
        return 1 + max(0, idx_len - a), "reports.slice(%d)" % a
    return idx_len, "无切片(全部显示)"


def real_weekday(d):
    try:
        dt = datetime.date(int(d[:4]), int(d[4:6]), int(d[6:]))
    except ValueError:
        return "无效日期"
    return WEEKDAY_CN[dt.weekday()]


def main():
    reports, errs = load_index_reports()
    if reports is None:
        for e in errs:
            print("  FAIL %s" % e)
        return 1

    local = local_files()
    idx_dates = [r["date"] for r in reports if r["date"]]

    fails, warns = [], []

    # 1. index 有 → 本地无（点击 404）
    missing = [d for d in idx_dates if d not in local]
    if missing:
        fails.append("index 已列但本地文件缺失(点击会404): %s" % missing)

    # 2. 本地有 → index 无（孤儿）
    orphan = [d for d in local if d not in idx_dates]
    if orphan:
        fails.append("本地有文件但 index 未收录(门户打不到): %s" % orphan)

    # 3. date 重复
    dup = sorted({d for d in idx_dates if idx_dates.count(d) > 1})
    if dup:
        fails.append("index 存在重复 date: %s" % dup)

    # 4. weekday / 标题
    bad_wd = []
    bad_title = []
    for r in reports:
        if not r["date"]:
            continue
        rw = real_weekday(r["date"])
        if r["weekday"] and r["weekday"] != rw:
            bad_wd.append("%s(index=%s,实际=%s)" % (r["date"], r["weekday"], rw))
        if not r["title"].strip():
            bad_title.append(r["date"])
    if bad_wd:
        fails.append("weekday 与实际不符: %s" % bad_wd)
    if bad_title:
        fails.append("title 为空: %s" % bad_title)

    # 5. 排序（应倒序，最新在前）
    if idx_dates != sorted(idx_dates, reverse=True):
        warns.append("index 条目非倒序(最新一期不在首位): 当前顺序 %s" % idx_dates)

    # 7. 三方数量：界面可见 / 数组 / 本地文件
    vis, vis_rule = visible_count(len(idx_dates))
    if vis < len(local):
        warns.append(
            "门户界面只显示 %d 条(%s)，但本地有 %d 个文件 —— 末 %d 期(如 %s)门户打不到，"
            "要么删本地文件，要么放宽切片"
            % (vis, vis_rule, len(local), len(local) - vis, local[:len(local) - vis])
        )

    print("=" * 60)
    print("index.html ↔ 本地报告文件 一致性校验")
    print("=" * 60)
    print("index 条目 : %d 条" % len(idx_dates))
    print("界面可见   : %d 条  (%s)" % (vis, vis_rule))
    print("本地文件   : %d 个" % len(local))
    print("-" * 60)

    if len(idx_dates) != len(local):
        fails.append("数量不一致: index %d 条 vs 本地 %d 个" % (len(idx_dates), len(local)))
        print("  FAIL 数量不一致  index %d / 本地 %d" % (len(idx_dates), len(local)))
    else:
        print("  PASS 数量一致  index %d = 本地 %d" % (len(idx_dates), len(local)))

    if not missing:
        print("  PASS index 条目均有对应本地文件")
    if not orphan:
        print("  PASS 无本地孤儿文件")
    if not dup:
        print("  PASS index 无重复条目")
    if not bad_wd:
        print("  PASS weekday 全部正确")
    if not bad_title:
        print("  PASS title 全部非空")

    for w in warns:
        print("  WARN %s" % w)
    for f in fails:
        print("  FAIL %s" % f)

    print("=" * 60)
    if fails:
        print("❌ 未通过 %d 项" % len(fails))
        return 1
    print("✅ index 与本地文件完全一致")
    return 0


if __name__ == "__main__":
    sys.exit(main())
