#!/bin/bash
# 自动同步到 GitHub Pages
# 用法: bash sync_github.sh "提交信息"

# 使用脚本所在目录作为工作目录
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

MSG="${1:-自动同步 $(date '+%Y-%m-%d %H:%M')}"

# 添加所有变更
git add -A

# 检查是否有变更
if git diff --cached --quiet; then
    echo "✅ 没有需要同步的变更"
    exit 0
fi

# 提交
git commit -m "$MSG"

# 推送
git push origin main

echo "✅ 已同步到 GitHub Pages: https://sheng-2000.github.io/laosheng-zaodao/"
