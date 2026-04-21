import os
import requests
import json
import sys

def process_sentinel():
    # 1. Grab the payload from the GitHub Action environment
    try:
        event_path = os.getenv('GITHUB_EVENT_PATH')
        with open(event_path, 'r') as f:
            event_data = json.load(f)
        
        payload = event_data.get('client_payload', {})
        message = payload.get('message', '')
        image_url = payload.get('image_url', '')
        
        print(f"🔱 Sentinel heard: {message}")
    except Exception as e:
        print(f"❌ Failed to parse payload: {e}")
        return

    # 2. Define the Path Logic
    base_path = "assets/textures"
    folder = "misc"
    
    if "Prisms" in message:
        folder = "prisms"
    elif "Waystops" in message:
        folder = "waystops"

    target_dir = os.path.join(base_path, folder)
    
    # 3. Create the folder if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"📁 Created directory: {target_dir}")

    # 4. Download the image if provided
    if image_url:
        file_extension = ".png" # You can detect this from the URL if needed
        filename = f"asset_{int(os.path.getmtime(event_path))}{file_extension}"
        filepath = os.path.join(target_dir, filename)
        
        print(f"📥 Downloading asset to {filepath}...")
        img_data = requests.get(image_url).content
        with open(filepath, 'wb') as handler:
            handler.write(img_data)
        print("✅ Asset registered successfully.")
    else:
        print("ℹ️ No image attached. Processing command only.")

if __name__ == "__main__":
    process_sentinel()
