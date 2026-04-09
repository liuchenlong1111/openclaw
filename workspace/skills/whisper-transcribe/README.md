# Whisper Transcribe

OpenAI Whisper 音视频转录技能 - 从音视频中提取文字，生成带时间戳的字幕。

## 功能特点

- 🎧 支持所有常见音视频格式（MP3, WAV, FLAC, MP4, M4A 等）
- 📝 支持多种输出格式：纯文本(txt)、VTT字幕、SRT字幕、JSON、TSV
- ⏱️ 每个文本片段都带有准确的时间戳
- 🌍 支持多语言，中文推荐使用 medium 或 large 模型获得最佳效果
- 🚀 自动下载模型，开箱即用

## 使用方法

在 OpenClaw 中，当用户需要提取音视频文本时，调用此技能：

1. 提供输入音视频文件路径
2. 指定输出格式（默认输出所有格式）
3. 指定语言（中文用 `zh`，英文用 `en`）
4. 选择模型大小（默认 `medium`）

## 安装依赖

```bash
pip install openai-whisper
brew install ffmpeg  # macOS
# 或
apt install ffmpeg  # Ubuntu/Debian
```

## 输出示例

VTT 格式（带时间戳）：

```vtt
WEBVTT

00:00.000 --> 00:11.000
你好,我是冯雪,中国医学科学院阜外医院生活方式医学中心的常务副主任

00:11.000 --> 00:28.000
欢迎来到我的课程,家庭健康管理100讲。
```

## License

MIT
