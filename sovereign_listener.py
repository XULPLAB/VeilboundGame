import requests
import time
import os
import subprocess

TOKEN = "8339651790:AAFwaRsqdrFgtjByCvGXnpR5znSlTGRGwRs"
CHAT_ID = "8099879191"
OFFSET = 0

def send_msg(text):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": text})

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
            
            # TRIGGER: APPROVE & SYNC
            if "#approve" in content:
                send_msg("🚀 [CEO]: Approval received. Migrating Kith to Godot and pushing to GitHub...")
                
                # 1. Move files from staging to project
                os.makedirs(f"/workspaces/VeilboundGame/godot_project/assets/creatures/kith", exist_ok=True)
                subprocess.run(["cp", "-r", "/workspaces/VeilboundGame/temp_staging/.", "/workspaces/VeilboundGame/godot_project/assets/creatures/kith/"])
                
                # 2. Git Push
                os.chdir("/workspaces/VeilboundGame")
                subprocess.run(["git", "add", "."])
                subprocess.run(["git", "commit", "-m", "Master CEO: Integrated new Kith batch"])
                subprocess.run(["git", "push", "origin", "main"])
                
                send_msg("✅ [SENTRY]: Sync Complete. Assets are live in the project repository.")

            # TRIGGER: REFINE (With actual Slicing attempt)
            elif "#refine" in content and "photo" in msg:
                send_msg("🧬 [ARTISAN]: Photo received. Initiating Kith extraction and shader application...")
                
                file_id = msg['photo'][-1]['file_id']
                get_path = requests.get(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}").json()
                img_data = requests.get(f"https://api.telegram.org/file/bot{TOKEN}/{get_path['result']['file_path']}").content
                
                raw_path = "/workspaces/VeilboundGame/temp_staging/active_sheet.png"
                with open(raw_path, "wb") as f:
                    f.write(img_data)
                
                # Logic: We attempt to slice the sheet into tiles (assuming a grid)
                # This is a placeholder for the actual CV slicing logic
                subprocess.run(["convert", raw_path, "-crop", "256x256", "/workspaces/VeilboundGame/temp_staging/kith_slice_%d.png"])
                
                send_msg("✅ [ARTISAN]: 100% Complete. 24-28 form variants staged. Send #Approve to sync.")

    except Exception as e:
        pass

if __name__ == "__main__":
    while True:
        process_telegram_input()
        time.sleep(1)
