# HEARTBEAT.md - 定时任务检查

## 每日 OpenClaw 资讯推送任务检查

检查 `/Users/liuchenglong/.openclaw/workspace/tasks/` 目录下是否有待处理的任务文件。

### 任务处理流程

1. 查找所有 `status` 为 `pending` 的 JSON 任务文件
2. 如果找到任务：
   - 读取任务内容
   - 按照 instructions 和 steps 执行任务
   - 任务完成后更新 status 为 `completed`
   - 将结果保存到 `wechat_articles/` 目录
3. 如果没有任务，回复 `HEARTBEAT_OK`

### 当前任务类型

- `openclaw_daily_news`: 搜索 OpenClaw 资讯并生成微信公众号文章

### 任务文件格式

```json
{
  "task": "任务类型",
  "created_at": "创建时间",
  "status": "pending/completed/failed",
  "instructions": "任务说明",
  "steps": ["步骤1", "步骤2", ...]
}
```
