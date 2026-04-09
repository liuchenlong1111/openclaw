#!/usr/bin/env python3
"""
Transcribe audio/video files to text.
Requires OpenAI Whisper or similar transcription service.
"""

import sys
import argparse
import os

def transcribe_with_whisper(file_path, api_key=None):
    """Transcribe media file using OpenAI Whisper API"""
    try:
        import openai
    except ImportError:
        print("Error: openai not installed. Run: pip install openai", file=sys.stderr)
        sys.exit(1)
    
    if api_key:
        openai.api_key = api_key
    elif 'OPENAI_API_KEY' in os.environ:
        openai.api_key = os.environ['OPENAI_API_KEY']
    else:
        print("Error: OpenAI API key required. Set OPENAI_API_KEY env var or use --api-key", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(file_path, 'rb') as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript['text']
    except Exception as e:
        print(f"Error transcribing media: {e}", file=sys.stderr)
        sys.exit(1)

def transcribe_local(file_path):
    """Placeholder for local transcription (requires whisper local install)"""
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(file_path)
        return result["text"]
    except ImportError:
        print("Error: Local whisper not installed. Run: pip install openai-whisper", file=sys.stderr)
        print("Or use --api-key for OpenAI API transcription", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error with local transcription: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Transcribe audio/video files')
    parser.add_argument('file_path', help='Path to media file')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--api-key', help='OpenAI API key')
    parser.add_argument('--local', action='store_true', help='Use local whisper model instead of API')
    args = parser.parse_args()
    
    if args.local:
        text = transcribe_local(args.file_path)
    else:
        text = transcribe_with_whisper(args.file_path, args.api_key)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Transcription saved to {args.output}", file=sys.stderr)
    else:
        print(text)

if __name__ == '__main__':
    main()
