---
name: whisper-transcribe
description: 使用 OpenAI Whisper 在本地转录音视频为文本，支持字幕输出
homepage: https://github.com/openai/whisper
metadata: {"clawdbot":{"emoji":"🎙️","requires":{"bins":["whisper","ffmpeg"]},"install":[{"id":"whisper","kind":"pip","pip":"openai-whisper","bins":["whisper"],"label":"Install OpenAI Whisper (pip)"},{"id":"ffmpeg","kind":"brew","formula":"ffmpeg","bins":["ffmpeg"],"label":"Install ffmpeg (brew)"}]}}
---

# Whisper Transcribe Skill

使用 OpenAI Whisper 从音视频文件中提取文本，支持纯文本输出和带时间戳的 VTT/SRT 字幕格式。

## Description

本技能封装了 Whisper 命令行工具，提供便捷的音视频转录功能：

- 支持常见音视频格式（mp3, wav, flac, mp4, m4a 等）
- 可指定输出格式：纯文本(txt)、VTT字幕、SRT字幕、JSON、TSV
- 支持手动指定语言，默认自动检测
- 支持不同模型大小（tiny, base, small, medium, large）
- 输出文件自动保存在当前工作目录

## Usage

```
当用户需要从音视频中提取文字或生成字幕时，使用此技能。

Examples:
- "帮我把这个 MP3 转成文字"
- "提取这个视频的字幕，要带时间戳"
- "用 whisper 转录这个音频，输出 vtt 格式"
```

## Parameters

- `input_file`: 输入音视频文件路径（必填）
- `output_format`: 输出格式，可选 `txt`, `vtt`, `srt`, `json`, `tsv`, `all`，默认 `all`
- `language`: 语言代码，例如 `zh`, `en`, `ja`，默认自动检测
- `model`: 模型大小，可选 `tiny`, `base`, `small`, `medium`, `large`，默认 `medium`（中文推荐 medium 或 large）

## Requirements

- Whisper 命令行工具已安装 (`pip install openai-whisper`)
- FFmpeg 已安装（用于处理音视频）
- 模型会自动下载，需要网络连接

## Examples

### 示例 1：默认转录（输出所有格式，中文 medium 模型）

```
transcribe /path/to/audio.mp3 --language zh
```

### 示例 2：只输出带时间戳的 VTT 格式

```
transcribe /path/to/video.mp4 --output_format vtt --language zh
```

### 示例 3：使用大模型获得更高准确率

```
transcribe /path/to/audio.mp3 --output_format all --language zh --model large
```

## Notes

- 模型越大准确率越高，但速度越慢：
  - `tiny` ~1GB 内存，最快
  - `base` ~1GB 内存
  - `small` ~2GB 内存
  - `medium` ~5GB 内存
  - `large` ~10GB 内存，最慢但最准确
- 中文建议使用 `medium` 以上模型，准确率较好
- 首次使用会自动下载模型文件，需要等待

## Author

Created by user request
