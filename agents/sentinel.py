name: Cloud Sentry Pulse

on:
  push:
    paths:
      - 'CEO_DIRECTIVES.md'
  repository_dispatch:
    types: [telegram_cmd]
  schedule:
    - cron: '0 13 * * *'  # 9:00 AM EST
    - cron: '0 17 * * *'  # 1:00 PM EST
    - cron: '0 1 * * *'   # 9:00 PM EST
  workflow_dispatch:

# REQUIRED: This gives the Sentinel permission to save your Waystops/Prisms
permissions:
  contents: write

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

jobs:
  # JOB 1: Status Updates (Messenger)
  apex_genesis:
    if: github.event_name != 'repository_dispatch'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Master CEO Sovereign Command
        env:
          BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
        run: |
          MSG=$(git log -1 --pretty=%B || echo "Manual Trigger")
          curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
          -d chat_id="${CHAT_ID}" \
          -d parse_mode="HTML" \
          -d text="<b>🔱 MASTER CEO: APEX GENESIS ACTIVE</b>"

  # JOB 2: Asset Processing (The Worker)
  sentinel_asset_sync:
    if: github.event_name == 'repository_dispatch'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Execute Sentinel Logic
        env:
          GITHUB_EVENT_PATH: ${{ github.event_path }}
        run: |
          # Use find to locate sentinel.py even if it's nested
          SCRIPT_PATH=$(find . -name "sentinel.py" | head -n 1)
          if [ -z "$SCRIPT_PATH" ]; then
            echo "❌ ERROR: sentinel.py not found in the repository!"
            exit 1
          fi
          echo "✅ Found Sentinel at: $SCRIPT_PATH"
          python3 "$SCRIPT_PATH"

      - name: Commit and Push Assets
        run: |
          git config --global user.name "XULPLAB-Sentinel"
          git config --global user.email "ceo@xulplabs.com"
          git add assets/
          if [ -n "$(git status --porcelain)" ]; then
            git commit -m "🔱 Sentinel: Asset Sync [Build Update]"
            git push origin main
          else
            echo "No new assets to commit."
          fi
