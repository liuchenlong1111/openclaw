#!/bin/bash
# OpenClaw 每日资讯推送脚本
# 每天8点执行，创建任务标记文件供 agent 检测

set -e

WORKSPACE="/Users/liuchenglong/.openclaw/workspace"
TASKS_DIR="$WORKSPACE/tasks"
DATE=$(date +%Y%m%d)
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
LOG_FILE="$WORKSPACE/logs/openclaw_cron_${DATE}.log"
TASK_FILE="$TASKS_DIR/openclaw_daily_${DATE}.json"

# 创建目录
mkdir -p "$TASKS_DIR"
mkdir -p "$WORKSPACE/logs"

echo "[$TIMESTAMP] 创建每日 OpenClaw 资讯推送任务" >> "$LOG_FILE"

# 创建任务文件
cat > "$TASK_FILE" << 'TASK_EOF'
{
  "task": "openclaw_daily_news",
  "created_at": "TIMESTAMP_PLACEHOLDER",
  "status": "pending",
  "instructions": "搜索 OpenClaw 相关最新资讯，整理并生成一篇精美的微信公众号文章。",
  "steps": [
    "使用 web_search 搜索 'OpenClaw' 最新资讯（近7天内）",
    "筛选2-3条最有价值的新闻/动态",
    "撰写一篇微信公众号风格的文章，包含：吸引人的标题、导语/摘要、正文内容、结尾总结",
    "保存文章到 wechat_articles/ 目录，文件名格式：openclaw_YYYYMMDD.md"
  ],
  "style_guide": {
    "tone": "专业但不枯燥",
    "audience": "技术/开发者",
    "length": "800-1500字"
  }
}
TASK_EOF

# 替换时间戳
sed -i '' "s/TIMESTAMP_PLACEHOLDER/$TIMESTAMP/" "$TASK_FILE"

echo "[$TIMESTAMP] 任务文件已创建: $TASK_FILE" >> "$LOG_FILE"
echo "[$TIMESTAMP] 等待 agent 处理..." >> "$LOG_FILE"

# 可选：发送通知到钉钉
# 如果有 webhook URL，可以在这里调用
# curl -s -X POST "DINGTALK_WEBHOOK_URL" -H "Content-Type: application/json" -d '{...}'
