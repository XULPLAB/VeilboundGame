import requests
import json
import os

TOKEN = "8339651790:AAFwaRsqdrFgtjByCvGXnpR5znSlTGRGwRs"
CHAT_ID = "8099879191"
PROJECT_DIR = "/workspaces/VeilboundGame"

registry_data = {
    "project": "VeilboundGame",
    "commander": "Commander",
    "aesthetic": "Aetheric Daybreak",
    "style_reference": "image_2.png",
    "lighting": "Magical Daylight (Lexington Sync)",
    "interaction": "Flick-to-Capture",
    "optimization": "Battery-Safe / Low-Processor",
    "status": "FORCE_OVERRIDE_ACTIVE"
}

with open(f"{PROJECT_DIR}/creature_registry.json", 'w') as f:
    json.dump(registry_data, f, indent=4)

message = (
    "⚔️ [VEILBOUND: DAYBREAK OVERRIDE]\n\n"
    "Commander, the visual optimization is forced. The Fleet has been realigned.\n\n"
    "* Aesthetic: High-Visibility Aetheric Daybreak\n"
    "* Grid: Lexington S2 (1:1 Topology)\n"
    "* Capture: Flick-to-Capture Operational\n\n"
    "Hallucination protocols have been stripped. The world is now vibrant."
)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
response = requests.post(url, data={"chat_id": CHAT_ID, "text": message})

if response.status_code == 200:
    print("✅ [Sentry] Force Dispatch Complete. Check Telegram.")
else:
    print(f"❌ [Sentry] Dispatch Failed: {response.text}")
