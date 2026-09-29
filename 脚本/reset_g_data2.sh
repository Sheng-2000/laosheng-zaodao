#!/bin/bash
# 每天定时任务执行前调用此脚本：
# 1. 备份当前 g_data2.py 到 历史/
# 2. 从模板重置 g_data2.py
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"
DATE=$(date +%Y%m%d)

# 备份
if [ -f "$DIR/脚本/g_data2.py" ]; then
  mkdir -p "$DIR/历史"
  cp "$DIR/脚本/g_data2.py" "$DIR/历史/g_data2_${DATE}.py"
  echo "[reset] 已备份 g_data2.py -> 历史/g_data2_${DATE}.py"
fi

# 重置
cp "$DIR/脚本/g_data2_template.py" "$DIR/脚本/g_data2.py"
echo "[reset] 已从模板重置 g_data2.py"
