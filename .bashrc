#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

#list
alias ls='lsd'
alias la='lsd -a'
alias ll='lsd -la'
alias l='lsd'
alias l.="lsd -A | egrep '^\.'"

#network
alias internet='nm-connection-editor'

#Brightness Controls
alias brighter='xbacklight -inc 20'
alias darker='xbacklight -dec 20'

#Battery
alias bat='cat /sys/class/power_supply/BAT0/capacity'

eval "$(starship init bash)"
export PATH="$HOME/.emacs.d/bin:$PATH"
