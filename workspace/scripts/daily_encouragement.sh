#!/bin/zsh
# 每日辛苦提醒 - 由龙龙仔创建 🐉
# 通过系统 crontab 调用，绕过 OpenClaw 内置 cron 的 Gateway 连接问题

export PATH="/Users/liuchenglong/.nvm/versions/node/v23.11.1/bin:$PATH"

# 发送钉钉消息
openclaw message send \
  --channel dingtalk-connector \
  --target "user:18963337352" \
  --message "工作辛苦了！早点休息 🐉" \
  2>&1 | tee -a /tmp/daily_encouragement.log

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 提醒任务执行完成" >> /tmp/daily_encouragement.log
