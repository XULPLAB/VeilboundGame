import os
import requests
import sys

def send_to_architect(message):
    # Pulling secrets from the GitHub Environment
    bot_token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('ARCHITECT_ID')
    
    if not bot_token or not chat_id:
        print("Envoy Error: Missing TG_TOKEN or ARCHITECT_ID")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Envoy: Message delivered to Architect.")
        else:
            print(f"Envoy: Failed to send. Status: {response.status_code}")
    except Exception as e:
        print(f"Envoy Error: {e}")

if __name__ == "__main__":
    # If the CEO sends a specific message via command line, use it.
    # Otherwise, send a standard "System Live" report.
    report = sys.argv[1] if len(sys.argv) > 1 else "🔱 XULPLAB: System synchronization complete. Ledger is updated. Standing by for Tower Projections."
    
    send_to_architect(report)
