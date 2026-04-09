# OpenClaw 每日资讯 | 2026年4月3日

## 🎉 最新发布：OpenClaw v2026.4.2 正式上线

昨天（2026年4月2日），OpenClaw 发布了最新版本 **v2026.4.2**，带来了一系列功能更新和问题修复。

### 🔔 破坏性变更

1. **xAI 插件重构**：将 `x_search` 设置从旧的核心路径 `tools.web.x_search.*` 迁移到插件自有路径 `plugins.entries.xai.config.xSearch.*`，统一认证方式。可以通过 `openclaw doctor --fix` 自动迁移旧配置。
2. **web_fetch 重构**：将 Firecrawl 配置从核心路径迁移到插件自有路径 `plugins.entries.firecrawl.config.webFetch.*`，通过 fetch-provider 边界进行 fallback。同样使用 `openclaw doctor --fix` 迁移。

### ✨ 新增功能

- **Task Flow 基础设施恢复**：恢复了带托管/镜像同步模式的核心 Task Flow 基础架构，支持持久化流状态/版本跟踪，以及 `openclaw flows` 检查/恢复原语，让后台编排可以独立于插件创作层进行持久化和操作。
- **托管子任务生成**：添加了托管子任务生成加上粘性取消意图，让外部编排器可以立即停止调度，让父任务流在活动子任务完成后平稳进入 `cancelled` 状态。
- **Android 助理入口**：添加了助理角色入口点和 Google Assistant App Actions 元数据，让 Android 可以从助理触发器启动 OpenClaw 并将提示传递到聊天编辑器。
- **Feishu 评论事件流**：添加了专门的 Drive 评论事件流，支持评论线程上下文解析、线程内回复和 `feishu_drive` 评论操作，适用于文档协作工作流。

### 🛠️ 问题修复

- 统一了请求认证、代理、TLS 和头信息处理，阻止不安全的 TLS/运行时传输覆盖
- 修复了 GitHub Copilot API 主机分类和代理端点解析
- 修复了配对后本地 exec 和节点客户端出现 "pairing required" 错误的问题
- 修复了子代理生成在回环范围升级时失败的问题
- 修复了 WhatsApp 在个人手机模式下推送通知丢失的问题
- 修复了 Matrix 导航设置中引导设置缺失的问题

### 📥 下载地址

- [OpenClaw-2026.4.2.dmg](https://github.com/openclaw/openclaw/releases/download/v2026.4.2/OpenClaw-2026.4.2.dmg) (macOS)
- [OpenClaw-2026.4.2.zip](https://github.com/openclaw/openclaw/releases/download/v2026.4.2/OpenClaw-2026.4.2.zip) (跨平台)

---

## 🌟 社区动态

OpenClaw 社区持续活跃，最近新增了多个实用技能：

- **多模态题目生成**：支持从 PDF、PPT、Word、Excel、音视频中按模板生成考试题目，包含六种题型
- **AI 视频生成**：集成火山引擎 Doubao Seedance 模型，支持文生视频、图生视频
- **Whisper 本地转写**：使用 OpenAI Whisper 在本地转录音视频为文本，支持字幕输出

欢迎访问 [ClawHub](https://clawhub.ai) 探索更多社区技能。

---

## 📝 更新建议

- 升级前请备份配置文件
- 升级后运行 `openclaw doctor --fix` 自动迁移配置
- 如有问题，可以在 [GitHub Issues](https://github.com/openclaw/openclaw/issues) 反馈

---

*本文由 OpenClaw 自动生成*
