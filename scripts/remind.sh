#!/bin/bash
# Daily Codeforces reminder (run by launchd: ~/Library/LaunchAgents/com.codeforces.reminder.plist)
REPO="$(cd "$(dirname "$0")/.." && pwd)"
NEXT="$(/usr/bin/python3 "$REPO/scripts/progress.py" --next 2>/dev/null)"
[ -z "$NEXT" ] && NEXT="Open the codeforces repo and run scripts/progress.py --next"
TITLE="${NEXT%% (*}"
/usr/bin/osascript -e "display notification \"$TITLE\" with title \"Codeforces: solve today's problem\" sound name \"Glass\""
