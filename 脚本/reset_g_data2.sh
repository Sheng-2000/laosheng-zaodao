#!/bin/bash
# reset_g_data2.sh —— 每天重置数据层，防止旧数据残留（第0步）
# 作用：
#   1. 备份当前 脚本/g_data2.py 到 历史/ 目录（带时间戳）
#   2. 从 脚本/g_data2_template.py 重置为空白模板
# 注意：g_data1.py 不需要重置，每天直接覆盖写入当天最新量化数据。
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPTS="$DIR/脚本"
HIST="$DIR/历史"

mkdir -p "$HIST"

if [ -f "$SCRIPTS/g_data2.py" ]; then
  TS=$(date +%Y%m%d_%H%M%S)
  cp "$SCRIPTS/g_data2.py" "$HIST/g_data2_${TS}.py"
  echo "[OK] 已备份 g_data2.py -> 历史/g_data2_${TS}.py"
else
  echo "[跳过] 当前不存在 g_data2.py"
fi

if [ -f "$SCRIPTS/g_data2_template.py" ]; then
  cp "$SCRIPTS/g_data2_template.py" "$SCRIPTS/g_data2.py"
  echo "[OK] 已从 g_data2_template.py 重置 g_data2.py（空白模板）"
else
  echo "[警告] g_data2_template.py 不存在，跳过重置"
fi
