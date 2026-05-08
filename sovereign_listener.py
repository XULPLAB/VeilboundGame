import requests
import time
import os
import subprocess
from PIL import Image, ImageOps

TOKEN = "8339651790:AAFwaRsqdrFgtjByCvGXnpR5znSlTGRGwRs"
CHAT_ID = "8099879191"
OFFSET = 0
KITH_TYPES = ["normal", "fire", "water", "grass", "steel", "ghost", "flying", "rock", "dragon", "rainbow", "poison", "bubble", "psychic", "fairy", "dark", "mega", "legendary"]

def send_msg(text):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": text})

def remove_background(img):
    # Converts the image to RGBA and makes the background transparent
    img = img.convert("RGBA")
    datas = img.getdata()
    
    # We assume the background is the top-left pixel color
    bg_color = datas[0]
    
    newData = []
    for item in datas:
        # If the pixel is very close to the background color, make it transparent
        if abs(item[0] - bg_color[0]) < 30 and abs(item[1] - bg_color[1]) < 30 and abs(item[2] - bg_color[2]) < 30:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    
    img.putdata(newData)
    return img

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
                send_msg("🚀 [CEO]: 10% - Initiating Aetheric Alpha Extraction...")
                sheet_path = "/workspaces/VeilboundGame/temp_staging/active_sheet.png"
                
                with Image.open(sheet_path) as img:
                    img_w, img_h = img.size
                    tile_size = 256
                    cols = img_w // tile_size
                    
                    for i, k_type in enumerate(KITH_TYPES):
                        # Grid Math Fix: Calculate Row and Column
                        row = i // cols
                        col = i % cols
                        
                        left = col * tile_size
                        top = row * tile_size
                        right = left + tile_size
                        bottom = top + tile_size
                        
                        # Stop if we exceed sheet height
                        if bottom > img_h: break

                        try:
                            # 1. Crop
                            variant = img.crop((left, top, right, bottom))
                            # 2. Strip Background
                            variant = remove_background(variant)
                            
                            # 3. Save to Correct Folder
                            type_dir = f"/workspaces/VeilboundGame/assets/creatures/kith/{k_type}"
                            os.makedirs(type_dir, exist_ok=True)
                            
                            variant_path = f"{type_dir}/v_{k_type}_transparent.png"
                            variant.save(variant_path, "PNG")
                            
                            # Git Push Logic for this type
                            os.chdir("/workspaces/VeilboundGame")
                            subprocess.run(["git", "add", "."], check=True)
                            subprocess.run(["git", "commit", "-m", f"Artisan: Alpha-Transparent {k_type} pushed"], check=True)
                            subprocess.run(["git", "push", "origin", "main"], check=True)
                            
                            send_msg(f"📡 [UPLINK]: {k_type} Kith extracted, background removed, and pushed.")
                        except Exception as e:
                            send_msg(f"⚠️ [ARTISAN]: {k_type} failed: {str(e)}")

                send_msg("⚔️ [MASTER CEO]: 100% - SUCCESS. Check GitHub for the transparent assets.")

    except Exception:
        pass

if __name__ == "__main__":
    while True:
        process_telegram_input()
        time.sleep(1)
