# OpenClaw 每日资讯 | 2026年3月26日

大家好，这里是 OpenClaw 每日资讯，为你带来最新的项目进展和社区动态。

## 🚀 最新版本发布：v2026.3.24

OpenClaw 在上周五发布了新版本 **v2026.3.24**，带来了多项新功能改进和问题修复。

### ✨ 主要更新内容

**新增功能：**
- **OpenAI 兼容性增强**：新增 `/v1/models` 和 `/v1/embeddings` 接口，为更广泛的客户端和 RAG 应用提供更好兼容性
- **Microsoft Teams 集成升级**：迁移到官方 Teams SDK，增加流式回复、欢迎卡片、消息编辑删除等功能
- **控制 UI 改进**：新增技能状态筛选标签页，优化技能详情展示，支持一键安装依赖
- **容器支持**：增加 `--container` 参数，支持在 Docker/Podman 容器中运行 OpenClaw 命令
- **Discord 自动线程命名**：支持使用 LLM 异步生成简洁标题

**开发者体验优化：**
- 将最低支持 Node 版本降低到 `22.14+`，兼容更多环境
- 更新前检查 Node 版本，提供清晰的升级提示
- 改进技能安装元数据，提供一键安装配方

### 🐛 问题修复

- 修复了多个渠道（WhatsApp/Telegram/Discord）的消息路由和发送问题
- 修复了媒体访问的安全绕过问题
- 改进了网关重启后的会话恢复机制
- 修复了 Docker 安装时的启动问题

### 📥 下载地址

- [OpenClaw-2026.3.24.dmg](https://github.com/openclaw/openclaw/releases/download/v2026.3.24/OpenClaw-2026.3.24.dmg) (macOS)
- [OpenClaw-2026.3.24.zip](https://github.com/openclaw/openclaw/releases/download/v2026.3.24/OpenClaw-2026.3.24.zip) (跨平台)

---

## 📝 近期代码提交（3月26日）

今天项目团队继续进行代码优化和测试改进，主要提交包括：

1. **测试框架优化** - 共享插件认证和 UI 存储测试装置，提升代码复用性
2. **文档更新** - 更新 parallels skill 文档，补充 guest openclaw shim 说明
3. **性能优化** - 隔离渠道运行与共享通道重叠执行，提升启动性能
4. **问题修复** - 修复重置会话后 CLI/ACP/渠道身份链接丢失的问题

查看所有提交：https://github.com/openclaw/openclaw/commits/main

---

## 📊 项目统计

- **GitHub Stars**: 持续增长中 ⭐
- **最新版本**: v2026.3.24 (2026-03-25)
- **下次发布预计**: 按项目节奏持续更新

---

## 🔗 相关链接

- 项目官网：https://openclaw.ai
- GitHub 仓库：https://github.com/openclaw/openclaw
- 社区 Discord：https://discord.com/invite/clawd
- ClawHub 技能商店：https://clawhub.com

---

*以上是今日 OpenClaw 资讯，感谢阅读！*
