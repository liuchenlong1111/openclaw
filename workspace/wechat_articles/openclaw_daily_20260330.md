# OpenClaw 每周进展 | 2026.3.30

各位 OpenClaw 开发者朋友们，大家好！👋

OpenClaw 项目持续快速迭代中，让我们一起来看看最近都有哪些重要更新吧！

---

## 🎉 最新版本：2026.3.28 正式发布

就在 3 月 29 日，OpenClaw 发布了最新版本，带来了多项重要功能更新和问题修复。

### 🔥 重要变更

**1. xAI Grok 集成增强**

xAI 提供的 Grok 模型现在获得了更好的支持：
- 将捆绑的 xAI 提供器迁移到 Responses API
- 新增一流的 `x_search` 网络搜索能力
- 自动启用 xAI 插件，配置好的认证搜索流程无需手动开启插件开关
-  onboard 过程中支持可选的 x_search 设置，包含模型选择器

**2. MiniMax 新增图像生成支持**

- 新增 `image-01` 模型的图像生成提供器
- 支持图像生成和图生图编辑，支持宽高比控制
- 模型目录已精简到仅保留 M2.7，移除了旧版 M2、M2.1、M2.5 和 VL-01 模型

**3. 插件钩子系统升级**

- 在 `before_tool_call` 钩子中新增异步 `requireApproval` 支持
- 允许插件暂停工具执行，通过执行批准覆盖层、Telegram 按钮、Discord 交互或 `/approve` 命令提示用户批准
- `/approve` 命令现在同时支持 exec 和插件批准，自动回退机制更完善

**4. ACP 绑定增强**

- 为 Discord、BlueBubbles 和 iMessage 增加了当前对话 ACP 绑定
- 现在可以使用 `/acp spawn codex --bind here` 将当前聊天转换为 Codex 支持的工作区，无需创建子线程

---

### 🚀 新增功能亮点

**1. Gemini CLI 后端支持**

- 将捆绑的 Claude CLI、Codex CLI 和 Gemini CLI 推理默认值移到插件表面
- 新增捆绑的 Gemini CLI 后端支持
- 统一了 CLI 后端日志标志，保持旧标志兼容性

**2. 自动加载捆绑插件**

- 从显式配置引用自动加载捆绑的提供器和 CLI 后端插件
- 捆绑的 Claude CLI、Codex CLI 和 Gemini CLI 消息提供器设置不再需要手动配置 `plugins.allow` 条目

**3. JSON Schema 配置支持**

- 新增 `openclaw config schema` 命令输出生成的 `openclaw.json` JSON Schema
- 方便开发者在编辑器中获得更好的自动补全和校验

**4. Podman 简化配置**

- 简化了无根用户的容器设置
- 在 `~/.local/bin` 下安装启动助手
- 更好地文档化了 `openclaw --container ...` 工作流

---

### 🐛 问题修复精选

这次版本修复了大量用户反馈的问题，重点包括：

1. **Google 模型修复**: 正确解析 Gemini 3.1 pro/flash/flash-lite 所有别名，修复了 flash-lite 前缀排序问题

2. **Telegram 多个问题修复**:
   - 修复了长消息分割算法，现在会在单词边界分割而不是切分单词
   - 防止空文本消息导致的 GrammyError 400 崩溃
   - 验证 `replyToMessageId` 格式，拒绝非数字值避免错误

3. **WhatsApp**: 修复了自聊天 DM 模式中的无限回显循环问题

4. **CLI/onboarding**: 恢复了 Moonshot 设置菜单中的 Kimi Code API 密钥选项，修复了 #54412

5. **zsh 补全**: 推迟 `compdef` 注册直到 `compinit` 可用，现在使用插件管理器和手动设置都能干净加载 zsh 补全

6. **Discord 重连**: 排干陈旧网关套接字，在强制重新连接前清除缓存的恢复状态，修复了中毒恢复状态下的无限循环

---

### 💔 不兼容变更

- **移除 Qwen portal-auth OAuth 集成**: portal.qwen.ai 的已弃用 qwen-portal-auth OAuth 集成已被移除，请迁移到 Model Studio，使用 `openclaw onboard --auth-choice modelstudio-api-key`

- **Config/Doctor**: 移除了超过两个月的旧自动配置迁移，非常旧的遗留密钥现在会验证失败，而不是在加载或 `openclaw doctor` 时被重写

---

## 📖 项目简介

对于还不了解 OpenClaw 的朋友：

OpenClaw 是一个开源的个人 AI 助手框架，让你在自己的基础设施上运行强大的 AI 代理，支持：

- 🔌 **丰富的模型提供器** - OpenAI、Anthropic、Google、xAI、Qwen、Moonshot 等全支持
- 🛠️ **完整的工具生态** - 文件操作、浏览器控制、搜索、技能市场一应俱全
- 🌐 **多渠道支持** - Discord、Telegram、Slack、WhatsApp、iMessage、钉钉等均可接入
- 🔒 **隐私优先** - 所有数据都在你自己掌控之中
- 🧩 **技能扩展** - 通过 ClawHub 轻松安装和分享技能

---

## 🚀 如何升级

如果你已经安装了 OpenClaw，可以通过以下方式升级：

```bash
git pull
npm install -g .
```

或者重新安装：

```bash
npm install -g openclaw
```

> 💡 首次安装？请参考官方文档：https://docs.openclaw.ai

---

## 🤝 贡献致谢

这个版本感谢以下社区贡献者的辛勤付出（按 PR 顺序）：

- [@pomelo-nwu](https://github.com/pomelo-nwu)
- [@huntharo](https://github.com/huntharo)
- [@liyuan97](https://github.com/liyuan97)
- [@vaclavbelak](https://github.com/vaclavbelak)
- [@joshavant](https://github.com/joshavant)
- [@Matthew19990919](https://github.com/Matthew19990919)
- [@kvokka](https://github.com/kvokka)
- [@loveyana](https://github.com/loveyana)
- [@jared596](https://github.com/jared596)
- [@afurm](https://github.com/afurm)
- [@velvet-shark](https://github.com/velvet-shark)
- [@lakshyaag-tavily](https://github.com/lakshyaag-tavily)
- [@neeravmakwana](https://github.com/neeravmakwana)
- [@MonkeyLeeT](https://github.com/MonkeyLeeT)
- [@joelnishanth](https://github.com/joelnishanth)
- [@ngutman](https://github.com/ngutman)
- [@mvanhorn](https://github.com/mvanhorn)
- [@KevInTheCloud5617](https://github.com/KevInTheCloud5617)
- [@sparkyrider](https://github.com/sparkyrider)
- 以及所有参与测试和反馈的社区朋友们！

---

## 🔗 相关链接

- 📖 **官方文档**: https://docs.openclaw.ai
- 🐙 **GitHub**: https://github.com/openclaw/openclaw
- 🧩 **技能市场**: https://clawhub.com
- 💬 **社区交流**: https://discord.com/invite/clawd

---

## 📮 写在最后

OpenClaw 项目正在持续快速发展中，每周都有新功能和改进。如果你喜欢这个项目，欢迎在 GitHub 上给我们点亮 ⭐️ Star 支持！

你在使用 OpenClaw 过程中有任何问题或建议，欢迎在评论区留言交流。

---

*📅 本文发布于：2026年3月30日*
*🔔 关注我们，获取 OpenClaw 最新进展*
