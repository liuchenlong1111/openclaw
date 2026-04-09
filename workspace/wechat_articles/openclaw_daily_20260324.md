# OpenClaw 每周资讯 - 2026年3月24日

## 📢 本周要闻

### 1. OpenClaw 开源项目持续演进

OpenClaw 作为一个开源的个人助理框架，一直在稳步发展中。项目目前托管在 GitHub 上，仓库地址为 [openclaw/openclaw](https://github.com/openclaw/openclaw)，欢迎社区开发者参与贡献。

### 2. ClawHub 技能仓库平台上线

[ClawHub](https://clawhub.ai/) 作为 OpenClaw 的技能仓库平台已经上线，提供以下功能：
- 上传 AgentSkills 技能包，像 npm 一样进行版本管理
- 支持向量搜索，快速找到你需要的技能
- 一键安装技能：`npx clawhub@latest install <skill-name>`
- 版本管理和回滚，确保稳定性

### 3. OpenClaw 核心特性回顾

OpenClaw 具有以下核心优势：

- **🔧 高度可扩展**：通过 Skill 系统轻松扩展功能
- **🧠 内置记忆管理**：自动维护日常记忆和长期记忆
- **🤖 支持多代理**：可以生成子代理处理复杂任务
- **🌐 多渠道支持**：支持 Telegram、Discord、Signal、钉钉等多种渠道
- **📦 本地优先**：大部分操作可以在本地完成，保护隐私
- **🔌 MCP 支持**：通过 mcporter 技能支持直接调用 MCP 服务器工具

## 🛠️ 技能生态动态

目前 OpenClaw 已经内置了丰富的技能，覆盖各种场景：

### 生产力工具
- **1password** - 1Password CLI 集成，管理密码和密钥
- **apple-notes** - Apple Notes 管理
- **apple-reminders** - Apple 提醒事项管理
- **obsidian** - Obsidian 笔记库自动化
- **gog** - Google Workspace CLI 集成（Gmail、日历、云端硬盘等）
- **himalaya** - CLI 邮件管理

### 媒体处理
- **camsnap** - RTSP/ONVIF 摄像头抓拍
- **video-frames** - 从视频提取帧/片段
- **nano-pdf** - 使用自然语言编辑 PDF
- **summarize** - 总结 URL、播客、本地文件内容
- **multimodal-quiz-generator** - 从多模态文件生成考试题
- **video-gen** - AI 视频生成与编辑（火山引擎 Doubao Seedance）

### 智能家居
- **openhue** - Philips Hue 灯光控制

### 开发工具
- **gh-issues** - GitHub Issue 管理，自动修复并提交 PR
- **github** - GitHub CLI 集成
- **skill-creator** - 创建和改进 AgentSkills
- **mcporter** - MCP 服务器调用工具

### 实用工具
- **weather** - 获取天气和预报
- **healthcheck** - 主机安全加固和风险配置
- **gifgrep** - 搜索和下载 GIF
- **peekaboo** - macOS UI 自动化捕获

## 💡 使用技巧

### 如何安装新技能

通过 ClawHub 一键安装：

```bash
npx clawhub@latest install <skill-name>
```

### 心跳检查机制

OpenClaw 支持心跳检查机制，可以定时：
- 检查邮件
- 查看日历
- 获取天气
- 执行自定义任务
- 维护内存

### 内存管理

OpenClaw 采用双层内存管理：
- **日常记忆**：`memory/YYYY-MM-DD.md` 记录每日原始日志
- **长期记忆**：`MEMORY.md` 存储重要事件、决策和经验

## 🔔 下周预告

OpenClaw 生态持续发展中，我们会持续关注：
- 新技能上线动态
- 核心功能更新
- 社区贡献进展

## 📝 结语

OpenClaw 致力于打造一个高度可定制、隐私友好的个人助理框架。如果你有兴趣参与贡献，或者想要添加新技能，欢迎访问 GitHub 仓库参与进来！

---

*本文由 OpenClaw 自动生成*
