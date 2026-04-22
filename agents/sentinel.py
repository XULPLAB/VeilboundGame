import os
import json
import urllib.request

def run_sentinel():
    event_path = os.getenv('GITHUB_EVENT_PATH')
    if not event_path:
        return

    try:
        with open(event_path, 'r') as f:
            event_data = json.load(f)
        
        payload = event_data.get('client_payload', {})
        command = payload.get('message', '')
        image_url = payload.get('image_url', '')

        # Routing Logic
        target_folder = "assets/textures/misc"
        if "#Update Manifest: Waystops" in command:
            target_folder = "assets/textures/waystops"
        elif "#Update Manifest: Prisms" in command:
            target_folder = "assets/textures/prisms"

        if image_url:
            os.makedirs(target_folder, exist_ok=True)
            # Use timestamp for unique asset naming to prevent overwrites
            filename = f"asset_{int(os.path.getmtime(event_path))}.png"
            filepath = os.path.join(target_folder, filename)
            
            print(f"Downloading asset to: {filepath}")
            urllib.request.urlretrieve(image_url, filepath)
            print("Registration complete")
        else:
            print("No image found in payload")
            
    except Exception as e:
        print(f"Sentinel Error: {e}")

if __name__ == "__main__":
    run_sentinel()
