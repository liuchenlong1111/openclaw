#!/usr/bin/env python3
"""
Video Generation Script using Doubao Seedance (matches official curl example format)
Based on the official curl example you provided
"""
import os
import sys
import json
import time
import base64
import httpx
from pathlib import Path

# Environment variables from your curl example:
# - API_KEY = cca86b4a-7106-4336-8a7a-7c3ea7d83400 (Bearer token)
# - Model = doubao-seed-1-8-251228

API_KEY = os.environ.get("ARK_API_KEY", os.environ.get("VIDEO_GEN_API_KEY", "cca86b4a-7106-4336-8a7a-7c3ea7d83400"))
MODEL = os.environ.get("VIDEO_GEN_MODEL", "doubao-seed-1-8-251228")
ARK_URL = "https://ark.cn-beijing.volces.com/api/v3/responses"

def create_video_task(
    prompt: str,
    first_frame_path: str = None,
    aspect_ratio: str = "16:9",
    duration: int = 5,
) -> dict:
    """Create video generation task matching official format"""
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    
    # Build content following the official example format
    content = []
    
    # Add first frame if provided (as input_image)
    if first_frame_path and os.path.exists(first_frame_path):
        with open(first_frame_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
            content.append({
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{img_b64}"
            })
    
    # Add text prompt (as input_text)
    content.append({
        "type": "input_text",
        "text": prompt
    })
    
    # Build payload matching the official example structure
    payload = {
        "model": MODEL,
        "input": [
            {
                "role": "user",
                "content": content
            }
        ]
    }
    
    print(f"Creating video with model: {MODEL}, prompt: {prompt[:100]}...", file=sys.stderr)
    
    try:
        with httpx.Client(timeout=httpx.Timeout(180.0)) as client:
            response = client.post(ARK_URL, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
    except Exception as e:
        print(f"ERROR: API call failed: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response text: {e.response.text}", file=sys.stderr)
        sys.exit(1)
    
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate video with Doubao Seedance (official Volcengine format)")
    parser.add_argument("prompt", help="Text prompt for video generation")
    parser.add_argument("--first-frame", help="First frame image file path")
    parser.add_argument("--aspect-ratio", default="16:9", help="Aspect ratio")
    parser.add_argument("--duration", type=int, default=5, help="Duration in seconds")
    parser.add_argument("--output", "-o", default="output.mp4", help="Output video file path")
    args = parser.parse_args()
    
    result = create_video_task(
        prompt=args.prompt,
        first_frame_path=args.first_frame,
        aspect_ratio=args.aspect_ratio,
        duration=args.duration,
    )
    
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # If we got back a video URL, download it
    if "output" in result and args.output:
        # Try to extract video URL from response
        video_url = None
        if isinstance(result.get("output"), list):
            for output_item in result["output"]:
                if output_item.get("type") == "output_video":
                    video_url = output_item.get("video_url")
                    break
        
        if video_url:
            print(f"\nDownloading video to {args.output}...", file=sys.stderr)
            try:
                with httpx.Client(timeout=httpx.Timeout(300.0)) as client:
                    video_response = client.get(video_url)
                    video_response.raise_for_status()
                    with open(args.output, "wb") as f:
                        f.write(video_response.content)
                    print(f"✓ Video saved to: {os.path.abspath(args.output)}", file=sys.stderr)
            except Exception as e:
                print(f"ERROR: Failed to download video: {e}", file=sys.stderr)
                sys.exit(1)
