#!/usr/bin/env python3
"""
Video Generation Script using Doubao Seedance on Volcengine ARK Platform
Correct format for ARK endpoints
"""
import os
import sys
import json
import time
import base64
import httpx
from pathlib import Path

# Environment variables:
# - ARK_API_KEY: Your Volcengine ARK API Key (starts with AK)
# - ARK_ENDPOINT_ID: Model endpoint ID (the one you got from ARK console, like cca86b4a-...)

ARK_API_KEY = os.environ.get("ARK_API_KEY", os.environ.get("VIDEO_GEN_API_KEY", ""))
ARK_ENDPOINT_ID = os.environ.get("ARK_ENDPOINT_ID", "cca86b4a-7106-4336-8a7a-7c3ea7d83400")
ARK_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

def create_video_task_ark(
    prompt: str,
    mode: str = "text_to_video",
    first_frame_path: str = None,
    aspect_ratio: str = "16:9",
    duration: int = 5,
) -> dict:
    """Create video generation task using ARK endpoint"""
    
    if not ARK_API_KEY:
        print("ERROR: ARK_API_KEY (or VIDEO_GEN_API_KEY) environment variable is required", file=sys.stderr)
        sys.exit(1)
    
    url = f"{ARK_BASE_URL}/endpoints/{ARK_ENDPOINT_ID}/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ARK_API_KEY}",
    }
    
    # Build the content according to Seedance format
    content = []
    
    # Add text prompt
    content.append({
        "type": "text",
        "text": prompt
    })
    
    # Add first frame if provided
    if first_frame_path and os.path.exists(first_frame_path):
        with open(first_frame_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{img_b64}"
                }
            })
    
    payload = {
        "model": "doubao-seedance-1.5",
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "parameters": {
            "aspect_ratio": aspect_ratio,
            "duration": duration
        }
    }
    
    print(f"Creating video task with ARK endpoint: {ARK_ENDPOINT_ID}", file=sys.stderr)
    
    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
    except Exception as e:
        print(f"ERROR: API call failed: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}", file=sys.stderr)
        sys.exit(1)
    
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate video with Doubao Seedance (Volcengine ARK format)")
    parser.add_argument("prompt", help="Text prompt for video generation")
    parser.add_argument("--first-frame", help="First frame image file path")
    parser.add_argument("--aspect-ratio", default="16:9", help="Aspect ratio")
    parser.add_argument("--duration", type=int, default=5, help="Duration in seconds")
    parser.add_argument("--output", "-o", help="Output video file path")
    args = parser.parse_args()
    
    if ARK_ENDPOINT_ID == "cca86b4a-7106-4336-8a7a-7c3ea7d83400":
        print(f"Note: Using default endpoint ID from env: {ARK_ENDPOINT_ID}", file=sys.stderr)
    
    result = create_video_task_ark(
        prompt=args.prompt,
        first_frame_path=args.first_frame,
        aspect_ratio=args.aspect_ratio,
        duration=args.duration,
    )
    
    print(json.dumps(result, indent=2, ensure_ascii=False))
