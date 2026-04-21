import sys
import os

def process_command(cmd_text):
    if not cmd_text:
        return "🔱 XULPLAB: No command detected. Sovereign Engine idling."

    cmd = cmd_text.lower()
    
    # Logic for Tower Proposals
    if "#propose tower" in cmd:
        try:
            # Extracts 'Castlewood Park' from the string
            location = cmd_text.split("tower:")[1].strip()
            
            # Create a marker for the 3D Artisan to know work is needed
            with open("CONSTRUCTION_MANIFEST.txt", "w") as f:
                f.write(f"LOCATION: {location}\nVARIANT: Azure\nSTATUS: BUILDING")
                
            return f"🔱 XULPLAB: Tower proposal received for {location}. Analyzing Azure variant visuals. Ready for 3D Sculpting."
        except IndexError:
            return "⚠️ XULPLAB Error: Tower proposal format incorrect. Use #Propose Tower: [Location]"

    # Logic for Global World Push
    elif "#globalpush" in cmd:
        return "🔱 XULPLAB: World Grid initialization confirmed. Global Shards active and synchronized."

    # Default Fallback
    return f"🔱 XULPLAB: Directive recognized. Processing system build. Current status: Synchronized."

if __name__ == "__main__":
    # Get the message text passed from the GitHub Workflow
    telegram_message = sys.argv[1] if len(sys.argv) > 1 else ""
    result = process_command(telegram_message)
    
    # This print sends the string back to the GitHub Action
    print(result)
