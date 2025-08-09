#!/usr/bin/env python3
import os
import yt_dlp

# Simple test to check if YouTube allows downloads
channel_url = os.getenv('CHANNEL_URL', 'https://www.youtube.com/@YouTube')

ydl_opts = {
    'quiet': False,
    'extract_flat': True,
    'playlist_items': '1'
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Testing YouTube access from Koyeb...")
        info = ydl.extract_info(channel_url, download=False)
        print(f"✅ SUCCESS! Can access YouTube")
        print(f"Channel: {info.get('title', 'Unknown')}")
        print("Koyeb IPs are NOT blocked by YouTube!")
except Exception as e:
    print(f"❌ FAILED: {e}")
    print("Koyeb IPs might be blocked")
