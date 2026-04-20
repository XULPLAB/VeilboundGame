import requests
import os

def send_report(report_text):
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": f"🔱 XULPLAB APEX REPORT:\n{report_text}"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_report("Global Grid Status: Stable. Treasury Minting: Active.")
