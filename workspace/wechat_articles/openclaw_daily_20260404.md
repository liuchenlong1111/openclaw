# OpenClaw 每日资讯 | 2026年4月4日

## 📊 v2026.4.2 版本发布后数据观察

OpenClaw 最新版本 **v2026.4.2** 已于昨日（4月2日）正式发布，经过一天的时间，我们来看看下载数据和社区反馈：

### 📈 下载数据快报

- **OpenClaw-2026.4.2.dmg** (macOS): 5908 次下载
- **OpenClaw-2026.4.2.zip** (跨平台): 7605 次下载
- **OpenClaw-2026.4.2.dSYM.zip** (调试符号): 712 次下载

发布仅仅一天，总下载量已经突破一万次，感谢社区的热情支持！🚀

---

## 🔧 配置迁移指南

本次版本带来了两个重要的破坏性变更，涉及配置迁移。很多用户在升级过程中会问到具体如何操作，这里再给大家梳理一遍：

### xAI 插件配置迁移

**旧配置位置：**
```yaml
tools:
  web:
    x_search:
      apiKey: xxx
```

**新配置位置：**
```yaml
plugins:
  entries:
    xai:
      config:
        xSearch:
          apiKey: xxx
```

### Firecrawl web_fetch 配置迁移

**旧配置位置：**
```yaml
tools:
  web:
    fetch:
      firecrawl:
        apiKey: xxx
```

**新配置位置：**
```yaml
plugins:
  entries:
    firecrawl:
      config:
        webFetch:
          apiKey: xxx
```

### 🤖 自动迁移一键搞定

你不需要手动修改配置文件！OpenClaw 提供了自动迁移工具：

```bash
openclaw doctor --fix
```

运行这条命令，系统会自动识别旧配置并迁移到新位置，全程只需几秒钟。

---

## 💬 社区常见问题解答

Q: 升级后提示 `x_search not configured` 怎么办？
A: 运行 `openclaw doctor --fix` 即可自动迁移配置，如果还有问题，请检查环境变量 `XAI_API_KEY` 是否正确设置。

Q: 配置迁移后还需要保留旧配置吗？
A: 自动迁移完成后，旧配置会被自动注释掉，你可以选择保留或删除，不影响正常使用。

Q: 我没有使用 xAI 和 Firecrawl，需要做什么吗？
A: 不需要，不影响使用，直接正常升级即可。

---

## 🌟 新功能深度解析：Task Flow 基础设施恢复

本次版本恢复了核心 Task Flow 基础设施，带来了什么变化？

### 什么是 Task Flow？

Task Flow 是 OpenClaw 中用于管理后台编排任务的核心机制，支持：
- 持久化流状态
- 版本跟踪
- 检查和恢复原语

### 对于普通用户有什么好处？

- 后台任务更加稳定，即使重启也能继续执行
- 子任务可以更好地被管理和取消
- 支持更复杂的工作流编排，比如我们日常使用的每日资讯推送任务，就是基于 Task Flow 运行的

### 开发者可以获得什么？

- 插件可以创建和驱动托管 Task Flows
- 支持托管子任务生成加上粘性取消意图
- 外部编排器可以更好地控制任务流

---

## 📱 新功能：Android 助理入口

本次版本还新增了 Android 助理支持：

- 添加了助理角色入口点
- 支持 Google Assistant App Actions 元数据
- Android 可以从助理触发器启动 OpenClaw
- 自动将提示传递到聊天编辑器

这意味着你现在可以通过 Google Assistant 直接唤醒 OpenClaw，更加方便快捷！

---

## 📝 升级建议

1. **备份配置**：升级前建议备份 `~/.openclaw/config.yaml`
2. **升级版本**：下载并安装最新版本
3. **迁移配置**：运行 `openclaw doctor --fix`
4. **验证功能**：重启后检查常用功能是否正常

---

## 📥 下载地址

- [OpenClaw-2026.4.2.dmg](https://github.com/openclaw/openclaw/releases/download/v2026.4.2/OpenClaw-2026.4.2.dmg) (macOS)
- [OpenClaw-2026.4.2.zip](https://github.com/openclaw/openclaw/releases/download/v2026.4.2/OpenClaw-2026.4.2.zip) (跨平台)

---

## 🔗 相关链接

- GitHub 发布页面：https://github.com/openclaw/openclaw/releases/tag/v2026.4.2
- 官方文档：https://docs.openclaw.ai
- 社区技能商店：https://clawhub.ai
- 问题反馈：https://github.com/openclaw/openclaw/issues

---

*本文由 OpenClaw 自动生成*
