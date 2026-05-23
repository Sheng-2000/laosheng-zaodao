#!/bin/bash
# 自动同步到 GitHub Pages
# 用法: bash sync_github.sh "提交信息"

# 使用脚本所在目录作为工作目录
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# 检查是否是git仓库
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "📝 初始化git仓库..."
    git init
    git config user.email "laosheng@zaodao.com"
    git config user.name "老盛早知道"
fi

# 检查远程仓库
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 添加远程仓库..."
    git remote add origin https://github.com/sheng-2000/laosheng-zaodao.git
    git branch -m main
fi

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
git push -u origin main

echo "✅ 已同步到 GitHub Pages: https://sheng-2000.github.io/laosheng-zaodao/"
