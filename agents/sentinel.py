import sys
import os

def process_command(cmd_text):
    if not cmd_text:
        return "🔱 XULPLAB: No command detected. Sovereign Engine idling."

    # Normalize the text for easier searching
    clean_text = cmd_text.replace('\n', ' ').strip()
    cmd_lower = clean_text.lower()
    
    # Improved logic for Tower Proposals
    if "#propose tower" in cmd_lower:
        try:
            # Splits at the colon and takes everything after it
            if ":" in clean_text:
                location = clean_text.split(":", 1)[1].strip()
            else:
                # Fallback if the colon was missed
                location = clean_text.lower().replace("#propose tower", "").strip()
            
            if not location:
                return "⚠️ XULPLAB: Please specify a location (e.g., #Propose Tower: Castlewood Park)"

            # Create the manifest for the Godot build
            with open("CONSTRUCTION_MANIFEST.txt", "w") as f:
                f.write(f"LOCATION: {location}\nVARIANT: Azure\nSTATUS: BUILDING")
                
            return f"🔱 XULPLAB: Tower proposal received for {location}. Analyzing Azure variant visuals. Ready for 3D Sculpting."
        except Exception as e:
            return f"⚠️ XULPLAB Error: Processing failed. {str(e)}"

    elif "#globalpush" in cmd_lower:
        return "🔱 XULPLAB: World Grid initialization confirmed. Global Shards active."

    return "🔱 XULPLAB: Directive recognized. Standing by for specific instructions."

if __name__ == "__main__":
    telegram_message = sys.argv[1] if len(sys.argv) > 1 else ""
    result = process_command(telegram_message)
    print(result)
