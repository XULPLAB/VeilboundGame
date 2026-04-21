import os
import json
import requests
import sys

def run_sentinel():
    # 1. Access the GitHub Action Payload
    event_path = os.getenv('GITHUB_EVENT_PATH')
    if not event_path or not os.path.exists(event_path):
        print("Sentinel: No event data found.")
        return

    try:
        with open(event_path, 'r') as f:
            event_data = json.load(f)
    except Exception as e:
        print(f"Error loading event JSON: {e}")
        return

    # 2. Extract Data from Cloudflare Payload
    payload = event_data.get('client_payload', {})
    command = payload.get('message', '')
    image_url = payload.get('image_url', '')

    print(f"Processing command: {command}")

    # 3. Routing Logic
    target_folder = "assets/textures/misc"
    
    if "#Update Manifest: Waystops" in command:
        target_folder = "assets/textures/waystops"
    elif "#Update Manifest: Prisms" in command:
        target_folder = "assets/textures/prisms"

    # 4. Create Directory & Download Asset
    if image_url:
        os.makedirs(target_folder, exist_ok=True)
        
        # Unique filename based on timestamp to avoid collisions
        filename = f"asset_{int(os.path.getmtime(event_path))}.png"
        filepath = os.path.join(target_folder, filename)

        print(f"Downloading to {filepath}...")
        try:
            response = requests.get(image_url, timeout=30)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print("Asset saved successfully.")
            else:
                print(f"Download failed: {response.status_code}")
        except Exception as e:
            print(f"Download error: {e}")
    else:
        print("No image URL provided in payload.")

if __name__ == "__main__":
    run_sentinel()
