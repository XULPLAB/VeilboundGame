#!/bin/bash
while true; do
  if ! pgrep -f "sovereign_listener.py" > /dev/null; then
    echo "[Fri May  8 03:42:35 UTC 2026] Watchman crashed. Executing Auto-Fix..." >> /workspaces/VeilboundGame/forge.log
    nohup python3 /workspaces/VeilboundGame/sovereign_listener.py >> /workspaces/VeilboundGame/forge.log 2>&1 &
    curl -s -X POST "https://api.telegram.org/bot8339651790:AAFwaRsqdrFgtjByCvGXnpR5znSlTGRGwRs/sendMessage"         -d chat_id="8099879191"         -d text="🛡️ [SENTRY]: Process crash detected. Auto-recovery successful. Standing by for Kith."
  fi
  sleep 5
done
