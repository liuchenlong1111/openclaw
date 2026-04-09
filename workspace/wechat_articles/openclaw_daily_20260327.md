# OpenClaw 项目更新周报 | 2026年3月27日

---

## 最新版本发布：v2026.3.24

OpenClaw 于3月25日发布了最新版本 **v2026.3.24**，带来了多项功能增强和问题修复，进一步提升了项目的稳定性和用户体验。

### 🎯 主要功能更新

#### 1. Gateway 兼容性增强
- 新增 `/v1/models` 和 `/v1/embeddings` 端点支持
- 在 `/v1/chat/completions` 和 `/v1/responses` 中支持显式模型覆盖
- 提升了与更广泛的客户端和 RAG 系统的兼容性

#### 2. 全新技能管理界面
- Control UI 新增状态筛选标签页（全部 / 就绪 / 需要配置 / 禁用）
- 点击技能卡片可展开详情对话框，显示需求、安装操作、API 密钥输入等
- 为捆绑技能添加了一键安装配方，当依赖缺失时 CLI 和 Control UI 可提供安装选项
- 感谢 @BunsDev 的贡献

#### 3. Microsoft Teams 集成升级
- 迁移至官方 Teams SDK，采用 AI 代理最佳实践
- 支持流式 1:1 回复、欢迎卡片、提示模板、反馈功能等
- 添加消息编辑和删除支持
- 感谢社区贡献 #51808 #49925

#### 4. Docker/容器支持
- CLI 新增 `--container` 和 `OPENCLAW_CONTAINER` 环境变量支持
- 支持在运行中的 Docker 或 Podman OpenClaw 容器内执行命令
- 感谢 @sallyom 的贡献 #52651

#### 5. 多平台 UI 优化
- **macOS 应用**：配置界面改用可折叠树形侧边栏，替代原有的水平标签导航
- **Control UI**：代理工作区文件行改为可展开 `<details>` 预览，支持懒加载
- 集成 `@create-markdown/preview` v2 主题系统，自适应应用明暗主题
- 感谢 @BunsDev 的多项贡献

#### 6. 其他亮点
- Discord 自动帖子支持异步生成简洁标题 #43366
- 插件新增 `before_dispatch` 钩子，支持规范入站元数据路由处理 #50444
- 降低 Node.js 版本要求至 `22.14+`，同时仍推荐使用 Node 24
- CLI 更新前会预检查目标包的 Node 版本要求，提供清晰升级提示

### 🔧 问题修复精选

- **安全**：修复 `mediaUrl`/`fileUrl` 沙箱绕过漏洞，确保出站媒体访问符合配置的文件系统策略 #54034
- **网关**：修复网关重启后中断会话唤醒问题，保持线程/主题路由正确 #53940
- **Docker**：避免预启动共享网络命名空间循环，修复全新 Docker 安装启动失败问题 #53385
- **WhatsApp**：修复群组回显抑制和回复检测问题，确保命令能正确送达 #53624
- **Telegram**：修复论坛话题路由和照片尺寸验证问题 #53699 #52545
- **Discord**：统一网关错误处理分类，避免超时导致进程崩溃 #53823

### 📥 下载地址

- macOS DMG: [OpenClaw-2026.3.24.dmg](https://github.com/openclaw/openclaw/releases/download/v2026.3.24/OpenClaw-2026.3.24.dmg)
- 跨平台 Zip: [OpenClaw-2026.3.24.zip](https://github.com/openclaw/openclaw/releases/download/v2026.3.24/OpenClaw-2026.3.24.zip)

### 📊 版本统计

- 本次版本累计合并了超过 20 项 Pull Request
- 来自社区 9 位贡献者的参与
- 当前 GitHub 下载量累计已超过 1.5 万次

---

## 社区动态

作为一个开源项目，OpenClaw 持续保持着活跃的开发节奏，每周都有新功能和问题修复发布。项目欢迎社区贡献，无论是代码贡献、文档改进还是问题反馈都非常欢迎。

如果你对 OpenClaw 感兴趣，可以通过以下链接关注项目：
- GitHub: https://github.com/openclaw/openclaw
- 官方文档: https://docs.openclaw.ai
- ClawHub 技能市场: https://clawhub.com
- Discord 社区: https://discord.com/invite/clawd

---

*本文由 OpenClaw 自动生成，内容来源于 GitHub 最新发布信息*
