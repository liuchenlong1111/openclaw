---
name: multimodal-quiz-generator
description: 从多模态文件（PDF、PPT、Word、Excel、音视频）中按模板生成考试题目。支持单选、多选、不定项、判断、填空、简答六种题型，输出格式包含题目、选项、答案、解析和难度。Use when the user needs to generate quiz questions from documents or media files with specific formatting requirements.
---

# Multimodal Quiz Generator

## Overview

从各种文件格式中提取内容并按模板生成结构化考试题目。支持音频、视频、PDF、PPT、Word、Excel 等格式。使用 LLM API（OpenAI/Moonshot/DeepSeek）智能生成题目。

## Requirements

### Python Dependencies
```bash
pip install openai PyPDF2 pdfplumber python-docx python-pptx openpyxl
```

### API Keys
设置以下环境变量之一：
- `OPENAI_API_KEY` - OpenAI API
- `MOONSHOT_API_KEY` - Moonshot (Kimi)
- `DEEPSEEK_API_KEY` - DeepSeek

## Supported File Types

- **文档**: PDF, Word (.doc/.docx), PowerPoint (.ppt/.pptx), Excel (.xls/.xlsx)
- **音视频**: MP3, MP4, WAV, AVI, MOV 等常见格式
- **文本**: TXT, Markdown, CSV

## Question Types

支持以下六种题型，按模板格式输出：

### 1. 单选题 [单选]
```
1.[单选]题目内容？
A. 选项A
B. 选项B
C. 选项C
D. 选项D
答案：A
解析：解析内容
题目难度：中
```

### 2. 多选题 [多选]
```
2.[多选]题目内容？
A. 选项A
B. 选项B
C. 选项C
D. 选项D
答案：BCD
解析：解析内容
题目难度：中
```

### 3. 不定项 [不定项]
```
3.[不定项]题目内容？
A. 选项A
B. 选项B
C. 选项C
D. 选项D
答案：BC
解析：解析内容
题目难度：中
```

### 4. 判断题 [判断]
```
4.[判断]题目陈述内容。
答案：正确/错误
解析：解析内容
题目难度：中
```

### 5. 填空题 [填空]
```
5.[填空]题目内容，需要填空的位置用__表示。
填空数：1
答案形式：完全一致
参考答案1：答案内容
解析：解析内容
题目难度：中
```

### 6. 简答题 [简答]
```
6.[简答]题目内容？
参考答案：参考答案内容
解析：解析内容
题目难度：中
```

## Workflow

### Step 1: 提取文件内容

根据文件类型选择提取方式：

**PDF**: 使用 `scripts/extract_pdf.py`
```bash
python scripts/extract_pdf.py <file_path>
```

**Word**: 使用 `scripts/extract_docx.py`
```bash
python scripts/extract_docx.py <file_path>
```

**PPT**: 使用 `scripts/extract_pptx.py`
```bash
python scripts/extract_pptx.py <file_path>
```

**Excel**: 使用 `scripts/extract_excel.py`
```bash
python scripts/extract_excel.py <file_path>
```

**音视频**: 使用 `scripts/transcribe_media.py`
```bash
# 使用 OpenAI API
python scripts/transcribe_media.py <file_path>

# 使用本地 Whisper 模型
python scripts/transcribe_media.py <file_path> --local
```

### Step 2: 生成题目

使用 `scripts/generate_quiz.py` 基于提取的内容生成题目：

```bash
# 使用 OpenAI (默认)
python scripts/generate_quiz.py --input content.txt --count 6

# 使用 Moonshot (Kimi)
python scripts/generate_quiz.py --input content.txt --count 6 --provider moonshot

# 使用 DeepSeek
python scripts/generate_quiz.py --input content.txt --count 6 --provider deepseek

# 指定题型
python scripts/generate_quiz.py --input content.txt --count 6 --types single,multiple,judgment

# 保存到文件
python scripts/generate_quiz.py --input content.txt --count 6 --output quiz.txt
```

参数说明：
- `--input, -i`: 提取的文本文件路径（必需）
- `--count, -c`: 生成题目数量（默认：6）
- `--types, -t`: 题型列表，逗号分隔（默认：全部六种）
- `--provider, -p`: LLM 提供商（openai/moonshot/deepseek，默认：openai）
- `--api-key, -k`: API 密钥（可选，默认读取环境变量）
- `--model, -m`: 模型名称（可选，使用提供商默认模型）
- `--output, -o`: 输出文件路径（默认：stdout）

### Step 3: 输出题目

直接打印格式化后的题目到控制台或保存到文件。

## Example Usage

### 完整流程示例

```bash
# 1. 从 PDF 提取内容
python scripts/extract_pdf.py document.pdf > content.txt

# 2. 使用 Moonshot 生成 6 道题目
export MOONSHOT_API_KEY="your-api-key"
python scripts/generate_quiz.py --input content.txt --count 6 --provider moonshot

# 3. 保存结果
python scripts/generate_quiz.py --input content.txt --count 6 --provider moonshot --output quiz.txt
```

### 从视频生成题目

```bash
# 转录视频
export OPENAI_API_KEY="your-api-key"
python scripts/transcribe_media.py lecture.mp4 > content.txt

# 生成题目
python scripts/generate_quiz.py --input content.txt --count 10 --types single,multiple
```

### 指定题型生成

```bash
# 只生成单选和判断题
python scripts/generate_quiz.py --input content.txt --count 6 --types single,judgment

# 生成全部题型
python scripts/generate_quiz.py --input content.txt --count 12 --types single,multiple,uncertain,judgment,fill,short
```

## Resources

### scripts/
- `extract_pdf.py` - PDF 文本提取
- `extract_docx.py` - Word 文档提取
- `extract_pptx.py` - PPT 内容提取
- `extract_excel.py` - Excel 内容提取
- `transcribe_media.py` - 音视频转录（支持 OpenAI Whisper API 和本地模型）
- `generate_quiz.py` - 题目生成主脚本（支持 OpenAI/Moonshot/DeepSeek）

### references/
- `question_templates.md` - 题目模板详细说明
- `prompts.md` - AI 生成题目的 prompt 模板

## Notes

- 文档内容过长时会自动截断到 15000 字符（LLM 上下文限制）
- 音视频转录需要额外的 API 费用或本地计算资源
- 建议使用 Moonshot (Kimi) 或 DeepSeek 处理中文内容效果较好
