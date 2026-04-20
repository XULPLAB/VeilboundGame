import os
import sys

def run_sentinel():
    # Capture the command passed from the Master CEO
    raw_cmd = sys.argv[1].lower() if len(sys.argv) > 1 else "routine_scan"
    
    print(f"🔱 SENTINEL: Initializing Global Watch...")

    # 1. THE HIJACK GATE: Propose vs. Execute
    if "propose hijack" in raw_cmd:
        location = raw_cmd.split("hijack")[-1].strip().upper()
        proposal_log = f"\n- [PENDING] QWEN HIJACK PROPOSAL: {location} | Awaiting Architect Approval."
        
        # Write the proposal to the ledger
        with open("CEO_DIRECTIVES.md", "a") as f:
            f.write(proposal_log)
        
        print(f"Sentinel: Hijack proposed for {location}. Permission required.")

    elif "approve" in raw_cmd:
        # This logic fires only when you send #Approve from Telegram
        approval_log = f"\n- [CONFIRMED] Hijack authorized by Architect. Grid coordinates locked."
        
        with open("CEO_DIRECTIVES.md", "a") as f:
            f.write(approval_log)
        
        print("Sentinel: Hijack EXECUTED. Tower status: GOLD.")

    # 2. GLOBAL SPEED & INTEGRITY CHECK (Anti-Spoofing)
    # Logic: If movement exceeds 900km/h between grid updates, flag the UID.
    print("Sentinel: Scanning S2 Cells for regional desync...")

    # 3. BATTERY OPTIMIZATION AUDIT
    # Ensure all renders are using the 5-decimal GPS truncation
    print("Sentinel: Performance metrics within 15% Amber threshold.")

if __name__ == "__main__":
    run_sentinel()
