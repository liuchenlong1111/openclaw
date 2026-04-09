#!/bin/bash
#
# Whisper 转录脚本
# Usage: ./transcribe.sh <input_file> [output_format] [language] [model]
# Example: ./transcribe.sh audio.mp3 vtt zh medium

INPUT_FILE="$1"
OUTPUT_FORMAT="${2:-all}"
LANGUAGE="${3:-auto}"
MODEL="${4:-medium}"

if [ -z "$INPUT_FILE" ]; then
    echo "Usage: $0 <input_file> [output_format] [language] [model]"
    echo "Example: $0 audio.mp3 vtt zh medium"
    exit 1
fi

if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file '$INPUT_FILE' not found"
    exit 1
fi

echo "Starting Whisper transcription..."
echo "Input: $INPUT_FILE"
echo "Output format: $OUTPUT_FORMAT"
echo "Language: $LANGUAGE"
echo "Model: $MODEL"
echo "======================================"

# 寻找 whisper 命令
WHISPER_CMD=$(which whisper)
if [ -z "$WHISPER_CMD" ]; then
    # 常见安装路径
    if [ -f "/Users/liuchenglong/Library/Python/3.9/bin/whisper" ]; then
        WHISPER_CMD="/Users/liuchenglong/Library/Python/3.9/bin/whisper"
    elif [ -f "/usr/local/bin/whisper" ]; then
        WHISPER_CMD="/usr/local/bin/whisper"
    elif [ -f "/opt/homebrew/bin/whisper" ]; then
        WHISPER_CMD="/opt/homebrew/bin/whisper"
    else
        echo "Error: whisper command not found in PATH"
        echo "Please install openai-whisper first: pip install openai-whisper"
        exit 1
    fi
fi

# 构建命令
CMD="$WHISPER_CMD \"$INPUT_FILE\" --model $MODEL"

if [ "$LANGUAGE" != "auto" ]; then
    CMD="$CMD --language $LANGUAGE"
fi

CMD="$CMD --output_format $OUTPUT_FORMAT"

# 执行
eval "$CMD"

EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ]; then
    echo "======================================"
    echo "Transcription completed successfully!"
    echo "Output files saved to: $(pwd)"
    echo ""
    echo "📥 Download links:"
    # 获取输入文件名（不含扩展名）
    BASENAME=$(basename "$INPUT_FILE" | sed 's/\.[^.]*$//')
    if [ "$OUTPUT_FORMAT" = "all" ]; then
        EXTENSIONS=("txt" "vtt" "srt" "json" "tsv")
    else
        EXTENSIONS=("$OUTPUT_FORMAT")
    fi
    for ext in "${EXTENSIONS[@]}"; do
        OUTPUT_FILE="$(pwd)/${BASENAME}.${ext}"
        if [ -f "$OUTPUT_FILE" ]; then
            SIZE=$(ls -lh "$OUTPUT_FILE" | awk '{print $5}')
            echo "  - $ext: file://$OUTPUT_FILE ($SIZE)"
        fi
    done
else
    echo "======================================"
    echo "Transcription failed with exit code $EXIT_CODE"
    exit $EXIT_CODE
fi
