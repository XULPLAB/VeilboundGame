import requests
import time
import os
import subprocess

TOKEN = "8339651790:AAFwaRsqdrFgtjByCvGXnpR5znSlTGRGwRs"
CHAT_ID = "8099879191"
OFFSET = 0

def forge_push_to_git():
    print("📦 [CEO]: Finalizing asset migration and pushing to GitHub...")
    try:
        # Move assets from temp_staging to Godot folders
        subprocess.run(["cp", "-r", "/workspaces/VeilboundGame/temp_staging/.", "/workspaces/VeilboundGame/godot_project/assets/"], check=True)
        
        # Git Push Protocol
        subprocess.run(["git", "add", "."], cwd="/workspaces/VeilboundGame")
        subprocess.run(["git", "commit", "-m", "Artisan Forge: Approved Faction Assets Deployment"], cwd="/workspaces/VeilboundGame")
        subprocess.run(["git", "push", "origin", "main"], cwd="/workspaces/VeilboundGame")
        return True
    except Exception as e:
        print(f"❌ [Sentry] Push Failed: {e}")
        return False

def process_telegram_input():
    global OFFSET
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={OFFSET}&timeout=30"
    try:
        response = requests.get(url).json()
        if response["ok"]:
            for update in response["result"]:
                OFFSET = update["update_id"] + 1
                msg = update.get("message", {})
                text = msg.get("text", "") if "text" in msg else ""
                
                # APPROVAL TRIGGER
                if "#approve" in text.lower():
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                  data={"chat_id": CHAT_ID, "text": "🚀 [CEO]: Approval Received. Deploying 4-Faction Sets to Godot and syncing GitHub..."})
                    
                    if forge_push_to_git():
                        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                      data={"chat_id": CHAT_ID, "text": "✅ [MASTER CEO]: Global Sync Complete. GitHub Repository Updated."})
                    else:
                        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                      data={"chat_id": CHAT_ID, "text": "⚠️ [Sentry]: Sync failed. Check terminal for Git errors."})

                # STATUS QUERY
                elif "#status" in text.lower():
                    status_text = "📊 [STATUS]: Online. Standing by for #Approve of Faction Assets."
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                  data={"chat_id": CHAT_ID, "text": status_text})

    except Exception as e:
        pass

if __name__ == "__main__":
    while True:
        process_telegram_input()
        time.sleep(2)
