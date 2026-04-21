import sys
import os

def process_command(cmd_text):
    if not cmd_text:
        return "🔱 XULPLAB: No command detected. Sovereign Engine idling."

    # Normalize the text for maximum flexibility
    cmd = cmd_text.lower().strip()
    
    # BROAD DETECTION: Look for the keywords anywhere in the message
    if "propose" in cmd and "tower" in cmd:
        # Try to find the location name after a colon or just the word tower
        if ":" in cmd:
            location = cmd_text.split(":", 1)[1].strip()
        else:
            location = cmd_text.lower().replace("#propose tower", "").replace("propose tower", "").strip()
        
        if not location:
            location = "Unknown Grid Point"

        # Create the manifest for the Godot world build
        with open("CONSTRUCTION_MANIFEST.txt", "w") as f:
            f.write(f"LOCATION: {location}\nVARIANT: Azure\nSTATUS: BUILDING")
            
        return f"🔱 XULPLAB: Tower proposal received for {location}. Analyzing Azure variant visuals. Ready for 3D Sculpting."

    elif "globalpush" in cmd:
        return "🔱 XULPLAB: World Grid initialization confirmed. Global Shards active."

    return f"🔱 XULPLAB: Directive recognized ('{cmd_text[:20]}...'). Please use #Propose Tower: Location to trigger the build."

if __name__ == "__main__":
    telegram_message = sys.argv[1] if len(sys.argv) > 1 else ""
    result = process_command(telegram_message)
    print(result)
