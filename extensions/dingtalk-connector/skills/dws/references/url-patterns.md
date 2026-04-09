# 已知 URL 格式

需要自行拼接链接时，只能使用以下模板：

| 产品 | 用途 | URL 格式 | ID 来源 |
|------|------|----------|---------|
| `aitable` | AI表格 Base 链接 | `https://alidocs.dingtalk.com/i/nodes/{baseId}` | `base list/search/create/get` 返回的 `baseId` |
| `aitable` | AI表格模板预览 | `https://docs.dingtalk.com/table/template/{templateId}` | `template search` 返回的 `templateId` |
| `doc` | 文档链接 | `https://alidocs.dingtalk.com/i/nodes/{dentryUuid}` | `doc` 命令返回的 `dentryUuid` |
| `minutes` | 听记链接 | `https://shanji.dingtalk.com/app/transcribes/{taskUuid}` | `list mine/shared` 返回的 `taskUuid` |

不在此表中的产品，禁止自行拼接 URL。命令返回中包含完整链接时直接使用，否则告知用户无法提供。
