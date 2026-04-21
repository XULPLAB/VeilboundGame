import sys
import os

def process_command(cmd_text):
    # 1. Ignore empty messages or the bot's own status reports
    if not cmd_text or "🔱 XULPLAB" in cmd_text:
        return None  # Tells the workflow to stay silent

    cmd = cmd_text.lower().strip()
    
    # 2. Logic for Waystop Manifest Update
    if "#update manifest: waystops" in cmd:
        return "🔱 XULPLAB: Waystop Manifest locked. Processing Circular and Standard Crystal artifacts for Lexington scatter."

    # 3. Logic for Tower Proposals
    if "propose" in cmd and "tower" in cmd:
        if ":" in cmd:
            location = cmd_text.split(":", 1)[1].strip()
        else:
            location = cmd_text.lower().replace("#propose tower", "").strip()
        
        return f"🔱 XULPLAB: Tower anchor set for {location}. Azure variant initialized."

    return f"🔱 XULPLAB: Directive recognized. Ready for the next build phase."

if __name__ == "__main__":
    telegram_message = sys.argv[1] if len(sys.argv) > 1 else ""
    result = process_command(telegram_message)
    if result:
        print(result)
