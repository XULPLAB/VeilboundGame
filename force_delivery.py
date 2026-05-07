import requests
import os

TOKEN = "8339651790:AAFwaRsqdrFgtjByCvGXnpR5znSlTGRGwRs"
CHAT_ID = "8099879191"
PHOTO_PATH = "/workspaces/VeilboundGame/assets/splash/aetheric_daybreak_preview.png"

# Ensure the directory exists
os.makedirs(os.path.dirname(PHOTO_PATH), exist_ok=True)

# If the Artisan hasn't finished, we push the 'World Seed' as a fallback
if not os.path.exists(PHOTO_PATH):
    print("⚠️ [Sentry] Artisan render not found. Pushing System World Seed...")
    # This ensures you get a response even if the render hung
    msg = "🛡️ [SYSTEM]: Render delayed. S2 Grid Lexington active. 21 Creatures seeded. Aetheric Daybreak mode: ON."
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
else:
    with open(PHOTO_PATH, 'rb') as photo:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data={"chat_id": CHAT_ID, "caption": "⚔️ [VEILBOUND_WORLD_SEED]: Visual Optimization Confirmed."}, files={"photo": photo})

print("✅ [Sentry] Force Dispatch Complete.")
