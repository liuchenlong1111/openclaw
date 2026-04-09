---
name: dws
description: 管理钉钉产品能力(AI表格/日历/通讯录/文档/机器人/待办/邮箱/听记/AI应用/审批/日志/钉盘等)。当用户需要操作表格数据、管理日程会议、查询通讯录、发送消息通知、处理审批流程、查看听记摘要、创建应用/系统/管理后台/业务工具、查看或提交日报周报（钉钉日志模版）、管理钉盘文件时使用、钉钉技能市场搜索及下载。
cli_version: ">=0.2.14"
---

# 钉钉全产品 Skill

通过 `dws` 命令管理钉钉产品能力。

## 严格禁止 (NEVER DO)
- 不要使用 dws 命令以外的方式操作（禁止 curl、HTTP API、浏览器）
- 不要编造 UUID、ID 等标识符，必须从命令返回中提取
- 不要编造 URL、Email、手机号等结构化信息，禁止猜测
- 不要猜测字段名/参数值，操作前必须先查询确认

## 严格要求 (MUST DO)
- 所有命令必须加 `--format json` 以获取可解析输出
- 危险操作必须先向用户确认，用户同意后才加 `--yes` 执行
- 单次批量操作不超过 30 条记录
- 所有命令必须**严格遵循**对应产品参考文档里面规定的参数格式（如：如果有参数值，则参数和参数值之间至少用一个空格隔开）
- URL 必须从产品参考文件或 [链接规范](./references/url-patterns.md) 中查找模板，或使用命令返回的完整链接，无法获取时告知用户无法提供
- Email/手机号必须从命令返回中提取或由用户明确提供，无法获取时主动询问用户


## 产品总览

| 产品                | 用途                                                   | 参考文件                                                           |
|-------------------|------------------------------------------------------|----------------------------------------------------------------|
| `aitable`         | AI表格：表格/数据表/字段/记录增删改查/模板搜索                           | [aitable.md](./references/products/aitable.md)                 |
| `calendar`        | 日历：日程/参与者/会议室/闲忙查询                                   | [calendar.md](./references/products/calendar.md)               |
| `contact`         | 通讯录：用户查询(当前用户/搜索/详情)/部门查询(搜索/子部门/成员列表)               | [contact.md](./references/products/contact.md)                 |
| `doc`             | 文档：搜索/浏览/读取/创建/更新文档/文件夹管理/块级编辑                       | [doc.md](./references/products/doc.md)                         |
| `chat`            | 群聊：群管理(建群/搜索/成员增删/改群名)/消息(拉取/发送/机器人群发/Webhook)/机器人搜索 | [chat.md](./references/products/chat.md)                       |
| `todo`            | 待办：创建(含优先级/截止时间)/查询/修改/标记完成/删除                       | [todo.md](./references/products/todo.md)                       |
| `mail`            | 邮箱：查询邮箱/搜索/查看/发送邮件                                   | [mail.md](./references/products/mail.md)                       |
| `minutes`         | AI听记：列表/摘要/转写/关键字/标题修改                               | [minutes.md](./references/products/minutes.md)                 |
| `report`          | 日志：按模版创建/收件箱/已发送/模版查看/详情/已读统计                         | [report.md](./references/products/report.md)                   |
| `drive`           | 钉盘：浏览文件/元数据/下载/创建文件夹/上传文件                            | [drive.md](./references/products/drive.md)                     |
| `ding`            | DING消息：发送/撤回（应用内/短信/电话）                              | [ding.md](./references/products/ding.md)                       |
| `devdoc`          | 开放平台文档：搜索开发文档                                        | [simple.md](./references/products/simple.md)                   |
| `conference`      | 视频会议：预约会议                                            | [simple.md](./references/products/simple.md)                   |
| `aiapp`           | AI应用：创建/查询/修改AI应用                                    | [aiapp.md](./references/products/aiapp.md)                     |
| `live`            | 直播：查看直播列表                                            | [simple.md](./references/products/simple.md)                   |
| `oa`              | OA审批：待处理/详情/同意/拒绝/撤销/记录/已发起/任务                       | [oa.md](./references/products/oa.md)                           |
| `attendance`      | 考勤：打卡记录/排班查询                                         | [attendance.md](./references/products/attendance.md)           |
| `skill`           | 技能市场：搜索/下载                                         | [simple.md](./references/products/simple.md)           |

## 意图判断决策树

用户提到"表格/多维表/AI表格/记录/数据" → `aitable`
用户提到"日程/日历/会议室/约会" → `calendar`
用户提到"通讯录/同事/部门/组织架构" → `contact`
用户提到"文档/知识库/写文档"以及用户传入文档URL（如 `https://alidocs.dingtalk.com/*`） → `doc`
用户提到"待办/TODO/任务提醒" → `todo`
用户提到"邮件/邮箱" → `mail`
用户提到"听记/会议录音/转写/AI摘要"以及用户传入听记URL（如 `https://shanji.dingtalk.com/*`） → `minutes`
用户提到"帮我做/建/生成/生成系统/AI应用/创建应用/智能应用" → `aiapp`
用户提到"DING/紧急消息/电话提醒" → `ding`
用户提到"考勤/打卡/排班" → `attendance`
用户提到"群聊/群消息/群成员/聊天记录/建群/机器人发消息/Webhook/通知" → `chat`
用户提到"审批/OA" → `oa`
用户提到"开发/API/调用错误 文档" → `devdoc`
用户提到"视频会议/预约会议" → `conference`
用户提到"直播" → `live`
用户提到"日志/日报/周报/日志统计/写日报/提交周报/发日志/填日志" → `report`
用户提到"钉盘/文件/网盘/下载文件/上传文件" → `drive`
用户提到"技能市场/查找技能" → `skill`

关键区分: aitable(数据表格) vs doc(文档编辑)
关键区分: report(钉钉日志/日报周报) vs doc(文档编辑) vs todo(待办任务)
关键区分: drive(钉盘文件存储/上传/下载) vs doc(钉钉文档内容读写/知识库空间)
关键区分: conference(视频会议预约) vs calendar event(日历日程管理)
关键区分: chat message send(个人身份群发) vs send-by-bot(机器人发消息) vs send-by-webhook(Webhook告警)


> 更多易混淆场景及用户表达示例，见 [intent-guide.md](./references/intent-guide.md)

## 危险操作确认

以下操作为不可逆或高影响操作，执行前**必须先向用户展示操作摘要并获得明确同意**，同意后才加 `--yes` 执行。

| 产品 | 命令 | 说明 |
|------|------|------|
| `aitable` | `base delete` | 删除整个 AI 表格，含全部数据表和记录 |
| `aitable` | `table delete` | 删除数据表，含全部记录 |
| `aitable` | `field delete` | 删除字段，该列数据不可恢复 |
| `aitable` | `record delete` | 删除记录（支持批量） |
| `calendar` | `event delete` | 删除日程，所有参与者同步取消 |
| `calendar` | `participant delete` | 移除日程参与者 |
| `calendar` | `room delete` | 取消会议室预定 |
| `todo` | `task delete` | 删除待办 |
| `doc` | `block delete` | 删除文档块元素 |
| `oa` | `approval approve/reject` | 同意或拒绝审批（审批决策不可撤回） |

### 确认流程
```
Step 1 → 展示操作摘要（操作类型 + 目标对象 + 影响范围）
Step 2 → 用户明确回复确认（如 "确认" / "好的"）
Step 3 → 加 --yes 执行命令
```

## 核心流程
作为一个智能助手，你的首要任务是**理解用户的真实、完整的意图**，而不是简单地执行命令。在选择 `dws` 的产品命令前，必须严格遵循以下四步流程：

1. 意图分类：首先，判断用户指令的核心 动词/动作 属于哪一类。这比关注名词更重要。
2. 歧义处理与信息追问：如果用户指令模糊或包含多个产品的关键字，严禁猜测。必须主动向用户追问以澄清意图。这是你作为智能助手而非命令执行器的核心价值。
3. 精准产品映射：在完成前两步，意图已经清晰后，参考产品总览和意图判断决策树 来选择产品。
4. 充分阅读产品参考文件，通过编写代码或直接调用指令实现用户意图。

## 错误处理
1. 遇到错误，加 `--verbose` 重试一次
2. 仍然失败，报告完整错误信息给用户，禁止自行尝试替代方案
3. 认证失败时，参考 [global-reference.md](./references/global-reference.md) 中的认证章节处理
4. 各产品高频错误及排查流程见 [error-codes.md](./references/error-codes.md)

## 详细参考 (按需读取)

- [references/products/](./references/products/) — 各产品命令详细参考
- [references/intent-guide.md](./references/intent-guide.md) — 意图路由指南（易混淆场景对照）
- [references/global-reference.md](./references/global-reference.md) — 全局标志、认证、输出格式
- [references/field-rules.md](./references/field-rules.md) — AI表格字段类型规则
- [references/error-codes.md](./references/error-codes.md) — 错误码 + 调试流程
- [scripts/](./scripts/) — 各产品批量操作脚本（AI表格/日历/群聊/通讯录/文档/钉盘/邮箱/听记/审批/日志/待办等）
