#!/usr/bin/env python3
import os
import sys
import json
import httpx

API_KEY = os.environ.get("VIDEO_GEN_API_KEY", "")
BASE_URL = os.environ.get("VIDEO_GEN_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3")
TASK_ID = "cgt-20260409005707-kfzcj"

headers = {
    "Authorization": f"Bearer {API_KEY}",
}

url = f"{BASE_URL}/contents/generations/tasks/{TASK_ID}"

with httpx.Client(timeout=30.0) as client:
    response = client.get(url, headers=headers)
    response.raise_for_status()
    result = response.json()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    if result.get("status") == "succeeded":
        outputs = result.get("output", {}).get("contents", [])
        for output in outputs:
            if output.get("type") == "video":
                video_url = output.get("video", {}).get("url")
                print(f"\nVideo URL: {video_url}")
                
                # Download it
                print("Downloading...")
                with httpx.Client(timeout=120.0) as dl_client:
                    r = dl_client.get(video_url)
                    r.raise_for_status()
                    with open("/Users/liuchenglong/.openclaw/workspace/generated_video.mp4", "wb") as f:
                        f.write(r.content)
                print("Download complete!")
                break
