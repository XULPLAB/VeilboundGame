#!/bin/bash
while true; do
  if ! pgrep -f "sovereign_listener.py" > /dev/null; then
    pkill -9 -f "convert" # Kill any hanging image processes
    nohup python3 /workspaces/VeilboundGame/sovereign_listener.py >> /workspaces/VeilboundGame/forge.log 2>&1 &
  fi
  sleep 5
done
