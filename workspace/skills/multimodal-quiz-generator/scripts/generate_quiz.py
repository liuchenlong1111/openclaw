#!/usr/bin/env python3
"""
Generate quiz questions from extracted text content using LLM API.
Supports multiple question types with formatted output.
"""

import sys
import argparse
import os
import json

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai not installed. Run: pip install openai", file=sys.stderr)
    sys.exit(1)

try:
    import anthropic
except ImportError:
    print("Warning: anthropic not installed. Required for Anthropic-compatible APIs like Volces Ark.", file=sys.stderr)

# Type mapping
type_labels = {
    'single': '单选',
    'multiple': '多选',
    'uncertain': '不定项',
    'judgment': '判断',
    'fill': '填空',
    'short': '简答'
}

def get_llm_client(provider='openai', api_key=None, base_url=None):
    """Get LLM client for different providers
    Returns (client, api_type) where api_type is 'openai' or 'anthropic'
    """
    if provider == 'openai':
        key = api_key or os.environ.get('OPENAI_API_KEY')
        if not key:
            raise ValueError("OpenAI API key required. Set OPENAI_API_KEY env var or use --api-key")
        return OpenAI(api_key=key, base_url=base_url), 'openai'
    
    elif provider == 'moonshot':
        key = api_key or os.environ.get('MOONSHOT_API_KEY')
        if not key:
            raise ValueError("Moonshot API key required. Set MOONSHOT_API_KEY env var or use --api-key")
        return OpenAI(api_key=key, base_url=base_url or "https://api.moonshot.cn/v1"), 'openai'
    
    elif provider == 'deepseek':
        key = api_key or os.environ.get('DEEPSEEK_API_KEY')
        if not key:
            raise ValueError("DeepSeek API key required. Set DEEPSEEK_API_KEY env var or use --api-key")
        return OpenAI(api_key=key, base_url=base_url or "https://api.deepseek.com/v1"), 'openai'
    
    elif provider == 'zhipu':
        key = api_key or os.environ.get('ZHIPU_API_KEY')
        if not key:
            raise ValueError("Zhipu API key required. Set ZHIPU_API_KEY env var or use --api-key")
        return OpenAI(api_key=key, base_url=base_url or "https://open.bigmodel.cn/api/paas/v4"), 'openai'
    
    elif provider == 'ark':
        key = api_key or os.environ.get('ARK_API_KEY')
        if not key:
            raise ValueError("Ark API key required. Set ARK_API_KEY env var or use --api-key")
        # Volces Ark supports Anthropic-compatible messages API
        client = anthropic.Anthropic(
            api_key=key,
            base_url=base_url or "https://ark.cn-beijing.volces.com/api/coding"
        )
        return client, 'anthropic'
    
    else:
        raise ValueError(f"Unknown provider: {provider}")

def build_prompt(content, count, types):
    """Build prompt for LLM"""
    type_names = [type_labels.get(t, t) for t in types]
    type_str = "、".join(type_names)
    
    prompt = f"""请根据以下文档内容生成 {count} 道考试题目。

## 文档内容
{content}

## 要求
1. 题目类型包括：{type_str}
2. 每道题必须包含：题目、答案、解析、难度
3. 单选/多选/不定项题必须提供4个选项（A、B、C、D）
4. 填空题用 __ 表示填空位置，并注明填空数和答案形式
5. 解析必须说明答案在原文中的出处
6. 难度分为：易、中、难
7. 题目序号从1开始连续编号

## 输出格式示例

1.[单选]题目内容？
A. 选项A
B. 选项B
C. 选项C
D. 选项D
答案：A
解析：解析内容，说明在原文中的依据
题目难度：中

2.[多选]题目内容？
A. 选项A
B. 选项B
C. 选项C
D. 选项D
答案：BCD
解析：解析内容，说明在原文中的依据
题目难度：中

3.[不定项]题目内容？
A. 选项A
B. 选项B
C. 选项C
D. 选项D
答案：BC
解析：解析内容，说明在原文中的依据
题目难度：中

4.[判断]题目陈述内容。
答案：正确/错误
解析：解析内容，说明在原文中的依据
题目难度：中

5.[填空]题目内容，填空处用__表示。
填空数：1
答案形式：完全一致
参考答案1：答案内容
解析：解析内容，说明在原文中的依据
题目难度：中

6.[简答]题目内容？
参考答案：参考答案内容
解析：解析内容，说明在原文中的依据
题目难度：中

请严格按照上述格式生成 {count} 道题目，确保格式完全正确。"""
    
    return prompt

def generate_questions(content, count=6, types=None, provider='openai', api_key=None, model=None, base_url=None):
    """Generate quiz questions using LLM API"""
    if types is None:
        types = ['single', 'multiple', 'uncertain', 'judgment', 'fill', 'short']
    
    # Get client and API type
    client, api_type = get_llm_client(provider, api_key, base_url)
    
    # Build prompt
    prompt = build_prompt(content, count, types)
    
    # Set default model based on provider
    if model is None:
        if provider == 'openai':
            model = 'gpt-4o'
        elif provider == 'moonshot':
            model = 'moonshot-v1-8k'
        elif provider == 'deepseek':
            model = 'deepseek-chat'
        elif provider == 'zhipu':
            model = 'glm-4'
        elif provider == 'ark':
            model = 'ark-code-latest'
    
    try:
        if api_type == 'openai':
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "你是一个专业的考试题目生成助手。请根据提供的文档内容生成格式规范的考试题目。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4000
            )
            return response.choices[0].message.content
        elif api_type == 'anthropic':
            response = client.messages.create(
                model=model,
                system="你是一个专业的考试题目生成助手。请根据提供的文档内容生成格式规范的考试题目。",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4000
            )
            return response.content[0].text
    
    except Exception as e:
        print(f"Error calling LLM API: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Generate quiz questions from text content using LLM')
    parser.add_argument('--input', '-i', required=True, help='Input text file path')
    parser.add_argument('--count', '-c', type=int, default=6, help='Number of questions to generate')
    parser.add_argument('--types', '-t', default='single,multiple,uncertain,judgment,fill,short',
                        help='Comma-separated list of question types: single,multiple,uncertain,judgment,fill,short')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--provider', '-p', default='openai', 
                        choices=['openai', 'moonshot', 'deepseek', 'zhipu', 'ark'],
                        help='LLM provider (default: openai)')
    parser.add_argument('--api-key', '-k', help='API key for the provider')
    parser.add_argument('--model', '-m', help='Model name (provider-specific)')
    parser.add_argument('--base-url', '-b', help='Base URL for API endpoint (optional)')
    args = parser.parse_args()
    
    # Read input content
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Check content length
    if len(content) > 15000:
        print("Warning: Content is very long. Truncating to 15000 characters.", file=sys.stderr)
        content = content[:15000] + "..."
    
    # Parse question types
    types = [t.strip() for t in args.types.split(',')]
    
    # Validate types
    valid_types = set(type_labels.keys())
    invalid_types = set(types) - valid_types
    if invalid_types:
        print(f"Error: Invalid question types: {invalid_types}", file=sys.stderr)
        print(f"Valid types: {valid_types}", file=sys.stderr)
        sys.exit(1)
    
    # Generate questions
    print(f"Generating {args.count} questions using {args.provider}...", file=sys.stderr)
    questions = generate_questions(
        content, 
        args.count, 
        types, 
        provider=args.provider,
        api_key=args.api_key,
        model=args.model,
        base_url=args.base_url
    )
    
    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(questions)
        print(f"Questions saved to {args.output}", file=sys.stderr)
    else:
        print(questions)

if __name__ == '__main__':
    main()
