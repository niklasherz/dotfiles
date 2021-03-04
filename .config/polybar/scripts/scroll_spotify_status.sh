#!/bin/bash

# # The name of polybar bar which houses the main spotify module and the control modules.
# PARENT_BAR="main"
#
# # Set the source audio player here.
# # Players supporting the MPRIS spec are supported.
# # Examples: spotify, vlc, chrome, mpv and others.
# # Use `playerctld` to detect the latest player.
# # See more here: https://github.com/altdesktop/playerctl/#selecting-players-to-control
# PLAYER="playerctld"
#
# # Format of the information displayed
# # Eg. {{ artist }} - {{ album }} - {{ title }}
# # See more attributes here: https://github.com/altdesktop/playerctl/#printing-properties-and-metadata
# FORMAT="{{ title }} - {{ artist }}"



# see man zscroll for documentation of the following parameters
zscroll -l 15 \
        --delay 0.1 \
        --scroll-padding "  " \
        --match-command "$HOME/.config/polybar/scripts/get_spotify_status.sh --status" \
        --match-text "Playing" "--scroll 1" \
        --match-text "Paused" "--scroll 0" \
        --update-check true "$HOME/.config/polybar/scripts/get_spotify_status.sh" &

wait
