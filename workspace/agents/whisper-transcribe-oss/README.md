# Whisper Transcribe + OSS Upload Agent

一站式音视频转录 + OSS 上传 Agent。

## 功能

1. **自动转录** - 使用 OpenAI Whisper 将音视频转换为文本/字幕
2. **自动上传** - 将所有输出文件上传到阿里云 OSS
3. **返回地址** - 输出所有文件的 OSS 路径

## 依赖

- `whisper` - OpenAI Whisper 命令行工具
- `ffmpeg` - 音视频处理
- `ossutil` - 阿里云 OSS 命令行工具，需要预先配置认证
- `ossutil-upload` skill - 已封装好的上传技能

## 使用方法

```bash
cd /Users/liuchenglong/.openclaw/workspace/agents/whisper-transcribe-oss
./transcribe-and-upload.js <input-file> <bucket> [options]
```

### 参数说明

| 参数 | 必填 | 说明 | 默认值 |
|------|------|------|--------|
| `input-file` | 是 | 输入音视频文件路径 | - |
| `bucket` | 是 | OSS 存储桶名称 | - |
| `--language` | 否 | 语言代码 | `zh` |
| `--model` | 否 | Whisper 模型大小 | `medium` |
| `--format` | 否 | 输出格式 | `all` |
| `--output-dir` | 否 | 本地输出目录 | `./whisper-output` |

### 模型选择

| 模型 | 显存需求 | 说明 |
|------|----------|------|
| tiny | ~1GB | 最快，准确率较低 |
| base | ~1GB | 快 |
| small | ~2GB | 平衡 |
| medium | ~5GB | 较好准确率，中文推荐 |
| large | ~10GB | 最准确，最慢 |

### 输出格式

- `txt` - 纯文本
- `vtt` - VTT 字幕
- `srt` - SRT 字幕
- `json` - JSON 格式（包含时间戳）
- `tsv` - TSV 表格
- `all` - 输出所有格式

## 使用示例

### 示例 1：默认配置（中文 + medium 模型）

```bash
./transcribe-and-upload.js /Users/liuchenglong/Downloads/interview.mp3 whisper-transcribe
```

### 示例 2：大模型提高准确率

```bash
./transcribe-and-upload.js ./meeting.mp4 whisper-transcribe --language zh --model large
```

### 示例 3：只输出纯文本

```bash
./transcribe-and-upload.js ./audio.wav my-bucket --format txt --language en
```

## 输出示例

```
============================================================
🎉 全部完成！
============================================================

📊 统计信息:
   输入文件: /Users/liuchenglong/Downloads/audio.mp3
   输出文件数: 5/5
   输出目录: /path/to/output

📥 OSS 地址列表:
   oss://whisper-transcribe/transcripts/audio/audio.txt
   oss://whisper-transcribe/transcripts/audio/audio.vtt
   oss://whisper-transcribe/transcripts/audio/audio.srt
   oss://whisper-transcribe/transcripts/audio/audio.json
   oss://whisper-transcribe/transcripts/audio/audio.tsv

🔗 如果你开启了公共读，可以通过 HTTPS 访问:
   https://whisper-transcribe.oss-cn-hangzhou.aliyuncs.com/transcripts/audio/{filename}

📄 结果已保存到: /path/to/output/audio.result.json
```

## OSS 路径格式

所有文件会上传到:
```
oss://<bucket>/transcripts/<input-base-name>/<output-file>
```

这样便于整理多个转录任务的文件。

## 前置配置

确保你已经配置好了 `~/.ossutilconfig`，包含：
- endpoint
- accessKeyID
- accessKeySecret

## 作者

Created by user request for OpenClaw
