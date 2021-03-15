#! /bin/bash
lxsession &
#picom --experimental-backends &
picom &
nitrogen --restore &
#urxvtd -q -o -f &
/usr/bin/emacs --daemon &
#volumeicon &
nm-applet &
xrandr --output DisplayPort-2 --mode 1920x1080 --rate 143.98 &
xrandr --output DP-2 --mode 1920x1080 --rate 143.98 &
xrandr --output DP-3 --mode 1920x1080 --rate 143.98 &
#TODO Sensitivity Matrix and no Acceleration
xinput set-prop "pointer:Razer Razer DeathAdder V2 Pro" "libinput Accel Speed" -0.8 &
xset -dpms &
polybar left &
polybar middle &
polybar right &

enpass &
