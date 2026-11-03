#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按 规则/报告生成规范.md §1.5 的预算削减 g_data1/g_data2 里超上限的颜色标记。

规则：一般叙事卡 ≤3 处；Tab1 新闻卡 / Tab2 AI 卡 / 生物医学卡 5 处；社区话题 N _观点 4 处
（后三者同时是 cover_qc 的硬门槛，所以 cap 就等于门槛，不可再低）。削减时青色 prio 最低总是先摘，
带数字的红/绿最后摘。只动纯可见字数 ≥150 的键，短键保持原样。默认干跑，加 --write 才落盘。
"""
import re
import io
import sys

MARK = re.compile(r"\{(r|g|y|c|o)\|([^{}]*?)\}")
DIG = re.compile(r"\d")
LINE = re.compile(r'^(\s*"((?:[^"\\]|\\.)*)":\s*")(.*)(",?)$')
MIN_VISIBLE = 150


def is_news(k):
    return ("新闻" in k) or k.startswith("生物医学")


def cap_of(k):
    if is_news(k):
        return 5
    if re.match(r"社区话题\d_观点", k):
        return 4
    return 3


def prio(letter, txt):
    if letter in ("r", "g"):
        return 5 if DIG.search(txt) else 3
    if letter == "o":
        return 4
    if letter == "y":
        return 2
    return 1


def demark(k, v):
    if len(MARK.sub(r"\2", v)) < MIN_VISIBLE:
        return v, 0
    out, removed = v, 0
    while True:
        marks = list(MARK.finditer(out))
        if len(marks) <= cap_of(k):
            break
        worst = min(marks, key=lambda m: (prio(m.group(1), m.group(2)), -len(m.group(2)), m.start()))
        out = out[: worst.start()] + worst.group(2) + out[worst.end():]
        removed += 1
    return out, removed


def main():
    write = "--write" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("--")] or ["脚本/g_data1.py", "脚本/g_data2.py"]
    before = after = touched = 0
    for path in paths:
        lines = io.open(path, encoding="utf-8").read().split("\n")
        changed = False
        for i, line in enumerate(lines):
            m = LINE.match(line)
            if not m:
                continue
            nv, removed = demark(m.group(2), m.group(3))
            before += len(MARK.findall(m.group(3)))
            after += len(MARK.findall(nv))
            if removed:
                lines[i] = m.group(1) + nv + m.group(4)
                changed = True
                touched += 1
                print("%s:%d 超预算 %d 处 → %d 处" % (
                    path, i + 1, len(MARK.findall(m.group(3))), len(MARK.findall(nv))))
        if changed and write:
            io.open(path, "w", encoding="utf-8").write("\n".join(lines))
    print("标记 %d → %d ｜ 触及键 %d" % (before, after, touched))
    if not write and touched:
        print("未落盘；确认后用 --write")


if __name__ == "__main__":
    main()
