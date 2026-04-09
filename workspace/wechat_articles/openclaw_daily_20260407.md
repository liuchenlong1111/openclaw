# OpenClaw 每日资讯 | 2026年4月7日

各位开发者早上好！今天为大家带来 OpenClaw 最新的开发动态：

## 🐛 问题修复：Browser 插件方法注册问题已确认

上周社区开发者 @BurgersXV 提交了一个有趣的 Bug 报告：在 macOS 本地安装中，`openclaw browser` CLI 存在，插件也显示已加载，但网关始终返回 `unknown method: browser.request` 错误。

**问题详情：**
- 现象：浏览器插件显示加载，但所有浏览器命令都失败
- 环境：OpenClaw 2026.3.28 (f9b1079)，macOS 26.2 arm64，Node 22.22.2
- 已排除：配置问题、配对问题、重启/重载插件无效
- 推测：插件/运行时注册不匹配或打包问题

目前这个 Issue 已经被标记为 `triage:bug` 和 `plugin/browser`，正在等待核心开发团队进一步调查。如果你也遇到了类似问题，可以在 [Issue #58222](https://github.com/openclaw/openclaw/issues/58222) 关注进展。

## 🚀 近期合并的 Pull Requests

### 1. feat(sessions): add detached head option to Codex ACP sessions [#58276](https://github.com/openclaw/openclaw/pull/58276)

这个 PR 为 Codex ACP 会话添加了 detached head 选项，允许在特定 commit 上启动开发会话，而不影响当前分支，非常适合代码评审和调试。

### 2. chore(deps): update multiple dependencies [#58266](https://github.com/openclaw/openclaw/pull/58266)

例行的依赖更新，包括多个 npm 包版本升级，提升稳定性和安全性。

### 3. fix(clawhub): correct skill metadata parsing in clawhub sync [#58242](https://github.com/openclaw/openclaw/pull/58242)

修复了 ClawHub 技能同步时元数据解析的问题，现在可以正确同步社区分享的技能了。

## 📊 项目数据

- Star 数量：350k+ ⭐
- Fork 数量：70.3k 🍴
- 开放 Issue：5k+ 📝
- 开放 PR：5k+ 🔀

## 📝 开发者语录

> "这看起来像是浏览器插件/运行时注册不匹配或打包/运行时 bug，不是用户配置问题。"
> — @BurgersXV

## 🔗 相关链接

- [问题 #58222](https://github.com/openclaw/openclaw/issues/58222)
- [OpenClaw GitHub 仓库](https://github.com/openclaw/openclaw)
- [ClawHub 技能社区](https://clawhub.ai)

---

*如果你也想参与 OpenClaw 开发，欢迎前往 GitHub 提交 PR 或 Issue！*

---

**今日编辑：** 龙龙仔 🐉
**发布日期：** 2026年4月7日
