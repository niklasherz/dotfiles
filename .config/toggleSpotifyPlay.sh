#!/usr/bin/env bash
set -euo pipefail

PLAYER="spotifyd"

PLAYERCTL_STATUS=$(playerctl --player=$PLAYER status 2>/dev/null)
EXIT_CODE=$?
echo "Status = $PLAYERCTL_STATUS \n"
echo "Exit_Code = $EXIT_CODE \n"

if [ "$PLAYERCTL_STATUS" == "Playing" ]; then
    playerctl --player=$PLAYER pause
else
    playerctl --player=$PLAYER play
fi
