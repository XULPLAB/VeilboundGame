import os
import json
import urllib.request
import uuid

def run_sentinel():
    # 1. Access the GitHub Action Payload
    event_path = os.getenv('GITHUB_EVENT_PATH')
    if not event_path:
        return

    try:
        with open(event_path, 'r') as f:
            event_data = json.load(f)
        
        payload = event_data.get('client_payload', {})
        message = payload.get('message', '')
        image_url = payload.get('image_url', '')

        # 2. Routing Logic
        # Default to misc, then check for specific manifests
        target_folder = "assets/textures/misc"
        
        if "#Update Manifest: Waystops" in message:
            target_folder = "assets/textures/waystops"
        elif "#Update Manifest: Prisms" in message:
            target_folder = "assets/textures/prisms"

        # 3. Process Download
        if image_url:
            # Create folder if it doesn't exist
            os.makedirs(target_folder, exist_ok=True)
            
            # Generate unique filename using timestamp + small random hash
            # This prevents overwrites when batch-uploading from Telegram
            time_stamp = int(os.path.getmtime(event_path))
            unique_id = uuid.uuid4().hex[:4]
            filename = f"asset_{time_stamp}_{unique_id}.png"
            filepath = os.path.join(target_folder, filename)
            
            print(f"Downloading asset to: {filepath}")
            
            # Use built-in urllib to avoid 'requests' dependency issues
            urllib.request.urlretrieve(image_url, filepath)
            
            print("Registration complete")
        else:
            print("No image found in payload")
            
    except Exception as e:
        # Avoid emojis in log outputs to prevent GitHub Action parsing errors
        print(f"Sentinel Error: {str(e)}")

if __name__ == "__main__":
    run_sentinel()
