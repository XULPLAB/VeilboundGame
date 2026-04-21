import sys
import os
import requests

def send_feedback(message):
    token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("ARCHITECT_ID")
    
    if not message or message.strip() == "" or message == "None":
        print("Envoy: Skipping empty message.")
        return

    # Using HTML parse_mode is much safer than Markdown for status updates
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML" 
    }

    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        print(f"Envoy: Failed to send. Status: {response.status_code}")
        print(f"Response: {response.text}") # This will tell us EXACTLY why it failed
    else:
        print("Envoy: Message delivered successfully.")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else ""
    send_feedback(msg)
