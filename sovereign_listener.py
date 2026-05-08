import requests
import time
import os
import subprocess
from PIL import Image

TOKEN = "8339651790:AAFwaRsqdrFgtjByCvGXnpR5znSlTGRGwRs"
CHAT_ID = "8099879191"
OFFSET = 0
KITH_TYPES = ["normal", "fire", "water", "grass", "steel", "ghost", "flying", "rock", "dragon", "rainbow", "poison", "bubble", "psychic", "fairy", "dark", "mega", "legendary"]

def send_msg(text):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": text})

def atomic_sync(k_type):
    try:
        os.chdir("/workspaces/VeilboundGame")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Artisan: Native Push for {k_type}"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        return True
    except:
        return False

def process_telegram_input():
    global OFFSET
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={OFFSET}&timeout=10"
    try:
        r = requests.get(url).json()
        if not r.get("ok"): return
        
        for update in r.get("result", []):
            OFFSET = update["update_id"] + 1
            msg = update.get("message") or update.get("edited_message")
            if not msg: continue

            content = (msg.get("text", "") or msg.get("caption", "") or "").lower()
            
            if "#approve all" in content:
                send_msg("🚀 [CEO]: 10% - Initiating Native Extraction...")
                sheet_path = "/workspaces/VeilboundGame/temp_staging/active_sheet.png"
                
                if not os.path.exists(sheet_path):
                    send_msg("⚠️ [SENTRY]: No sheet found in staging. Send photo first.")
                    continue

                # Open the sheet with Pillow
                with Image.open(sheet_path) as img:
                    width, height = img.size
                    # Grid settings: Adjust if your sheet layout is different
                    tile_size = 256 
                    
                    for i, k_type in enumerate(KITH_TYPES):
                        type_dir = f"/workspaces/VeilboundGame/assets/creatures/kith/{k_type}"
                        os.makedirs(type_dir, exist_ok=True)
                        
                        # Calculate grid position (assuming vertical or horizontal strip)
                        # This logic takes one 256x256 square per type
                        left = 0
                        top = i * tile_size
                        right = tile_size
                        bottom = (i + 1) * tile_size
                        
                        # Safety check for image bounds
                        if bottom > height: 
                            bottom = height
                        
                        try:
                            variant = img.crop((left, top, right, bottom))
                            variant_path = f"{type_dir}/v_{int(time.time())}_{k_type}.png"
                            variant.save(variant_path)
                            
                            atomic_sync(k_type)
                            send_msg(f"📡 [UPLINK]: {k_type} species extracted and pushed.")
                        except Exception as e:
                            send_msg(f"⚠️ [ARTISAN]: {k_type} extraction failed: {str(e)}")

                send_msg("⚔️ [MASTER CEO]: 100% - SUCCESS. Check GitHub for the Species folders.")

    except Exception as e:
        pass

if __name__ == "__main__":
    while True:
        process_telegram_input()
        time.sleep(1)
