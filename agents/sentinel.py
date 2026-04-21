import os
import json
import requests
import sys

def run_sentinel():
    # 1. Access the GitHub Action Payload
    event_path = os.getenv('GITHUB_EVENT_PATH')
    if not event_path:
        print("🔱 Sentinel: No event path found. Standing by.")
        return

    with open(event_path, 'r') as f:
        event_data = json.load(f)

    # 2. Extract Data from Cloudflare
    payload = event_data.get('client_payload', {})
    command = payload.get('message', '')
    image_url = payload.get('image_url', '')

    print(f"🔱 Sentinel heard: '{command}'")

    # 3. Routing Logic
    target_folder = "assets/textures/misc" # Fallback
    
    if "#Update Manifest: Waystops" in command:
        target_folder = "assets/textures/waystops"
        print("🔱 Waystop Manifest locked. Crystal assets registered.")
    elif "#Update Manifest: Prisms" in command:
        target_folder = "assets/textures/prisms"
        print("🔱 Prism Manifest locked. 6 Tiers initialized.")
    elif "#Deploy Shader" in command:
        print("🔱 Shader Deployment sequence initiated.")
        # Add your shader-specific logic here
        return 

    # 4. Create Directory & Download Asset
    if image_url:
        if not os.path.exists(target_folder):
            os.makedirs(target_folder, exist_ok=True)
            print(f"📁 Created directory: {target_folder}")

        # Generate a unique filename using the timestamp
        filename = f"asset_{int(os.path.getmtime(event_path))}.png"
        filepath = os.path.join(target_folder, filename)

        print(f"📥 Downloading asset to {filepath}...")
        try:
            response = requests.get(image_url, timeout=30)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"✅ Registered: {filename}")
            else:
                print(f"❌ Download failed (Status: {response.status_code})")
        except Exception as e:
            print(f"❌ Error during download: {e}")
    else:
        print("⚠️ No image detected in payload. Command processed as text-only.")

if __name__ == "__main__":
    run_sentinel()
