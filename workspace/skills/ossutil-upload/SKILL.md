---
name: ossutil-upload
description: 使用阿里云 ossutil 上传文件到 OSS 存储桶。支持指定 bucket，单文件上传。需要预先配置好 ossutil 认证信息。
---

# ossutil-upload

使用阿里云 ossutil 命令行工具上传本地文件到阿里云对象存储 OSS。

## 前置要求

- ossutil 已经安装并配置好认证信息（`~/.ossutilconfig`）
- 目标 OSS bucket 已创建

## 使用方法

### 上传单个文件

```bash
node_modules/openclaw/skills/ossutil-upload/scripts/upload.js <local-file> <bucket> [object-name]
```

参数说明：
- `local-file`: 本地文件路径（必需）
- `bucket`: OSS 存储桶名称（必需，不需要包含 oss:// 前缀）
- `object-name`: OSS 对象名称（可选，默认使用本地文件名）

### 示例

1. 上传图片到指定 bucket：
```bash
./scripts/upload.js /Users/liuchenglong/Downloads/photo.jpg my-bucket
```

2. 上传并重命名对象：
```bash
./scripts/upload.js /local/path/file.txt my-bucket remote/path/new-name.txt
```

## 技能触发场景

当用户说：
- "帮我上传这个文件到 OSS"
- "把这个图片上传到 oss 的 xxx bucket"
- "用 ossutil 上传文件"

自动使用此技能。

## 输出

上传成功后会显示：
- 文件大小
- 上传耗时
- OSS 对象完整路径（`oss://bucket/object`）
- ETAG 校验值
