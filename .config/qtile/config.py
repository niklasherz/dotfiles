# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import KeyChord, Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key
myTerm = "alacritty"                             # My terminal
myConfig = "/home/nik/.config/qtile/config.py"    # The Qtile config file location


## TODO: Seperate workspaces for screens, Bindings for additional Applications, Widgets and Color Schemes



keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "space",
             lazy.spawn("dmenu_run -p 'Run: '"),
             #lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
             desc='Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "h",
             lazy.window.toggle_minimized(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key(["control", "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
        Key([mod, "shift"], "f",
            lazy.spawn("firefox"),
            desc='Firefox'
            ),
        Key([mod, "shift"], "Return",
            lazy.spawn("pcmanfm"),
            desc='Launch File Manager'
            ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([], "XF86AudioNext",
             lazy.spawn("playerctl next"),
             desc='Next Song'
             ),
         Key([], "XF86AudioPrev",
             lazy.spawn("playerctl previous"),
             desc='Next Song'
             ),
         Key([], "XF86AudioPlay",
             lazy.spawn("playerctl play-pause"),
             desc='Next Song'
             ),
         Key([], "XF86AudioLowerVolume",
             lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"),
             desc='Lower Volume by 10%'
             ),
         Key([], "XF86AudioRaiseVolume",
             lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"),
             desc='Lower Volume by 10%'
             ),
         Key([], "XF86AudioMute",
             lazy.spawn("pactl set-sink-mute 0 toggle"),
             desc='Lower Volume by 10%'
             ),

    
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "control"], "space",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod, "shift"], "m",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             )
]


group_names = [("一", {'layout': 'monadtall'}),
               ("二", {'layout': 'monadtall'}),
               ("三", {'layout': 'monadtall'}),
               ("四", {'layout': 'monadtall'}),
               ("五", {'layout': 'monadtall'}),
               ("六", {'layout': 'monadtall'}),
               ("七", {'layout': 'monadtall'}),
               ("八", {'layout': 'monadtall'}),
               ("九", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "5FA8D3",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.Max(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.TreeTab(
    #      font = "Ubuntu",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND"],
    #      section_fontsize = 11,
    #      bg_color = "141414",
    #      active_bg = "90C435",
    #      active_fg = "000000",
    #      inactive_bg = "384323",
    #      inactive_fg = "a0a0a0",
    #      padding_y = 5,
    #      section_top = 10,
    #      panel_width = 320
    #      ),
    #layout.Floating(**layout_theme)
]

colors = [["#282c34", "#282c34"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#CAE9FF", "#CAE9FF"], # font color for group names
          ["#BEE9E8", "#BEE9E8"], # border line color for current tab
          ["#BEE9E8", "#BEE9E8"], # border line color for other tab
          ["#5FA8D3", "#5FA8D3"], # window name
          ["#59886b", "#59886b"], # widget #1
          ["#c05555", "#c05555"], # widget #2
          ["#ffc85c", "#ffc85c"], # widget #3
          ["#fff8c1", "#fff8c1"], # widget #4
          ["#c5d7bd", "#c5d7bd"], # widget #5
          ["#9fb8ad", "#9fb8ad"], # widget #6
          ["#BEE9E8", "#BEE9E8"], #bright Text
          ["#1B4965", "#1B4965"]] #dark Text

brightText = colors[-2]
darkText = colors[-1]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),

               widget.TextBox(
                        #foreground = darkText,
                        background = colors[0],
                        text = "⏻",
                        mouse_callbacks ={'Button1': lambda qtile: qtile.cmd_spawn("shutdown-dialog")}
                        ),
                widget.Sep(
                         linewidth = 0,
                         padding = 6,
                         foreground = colors[2],
                         background = colors[0]
                         ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[5],
                       background = colors[0],
                       padding = 0
                       ),
            widget.TextBox(
                  text = '◥',
                  background = colors[0],
                  foreground = colors[6],
                  fontsize = 60,
                  width = 27
                  ),
              widget.TextBox(
                       text = " 🌡",
                       padding = 2,
                       foreground = darkText,
                       background = colors[6],
                       fontsize = 11
                       ),
              widget.ThermalSensor(
                       foreground = darkText,
                       background = colors[6],
                       threshold = 90,
                       padding = 5
                       ),
              widget.TextBox(
                    text = '◥',
                    background = colors[6],
                    foreground = colors[7],
                    fontsize = 60,
                    width = 27
                    ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = darkText,
                       background = colors[7],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = darkText,
                       background = colors[7],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                    text = '◥',
                    background = colors[7],
                    foreground = colors[8],
                    fontsize = 60,
                    width = 27
                    ),
              widget.Net(
                       interface = "enp34s0",
                       format = '{down} ↓↑ {up}',
                       foreground = darkText,
                       background = colors[8],
                       padding = 5
                       ),
              widget.TextBox(
                    text = '◥',
                    background = colors[8],
                    foreground = colors[9],
                    fontsize = 60,
                    width = 27
                    ),
              widget.TextBox(
                      text = " Vol:",
                       foreground = darkText,
                       background = colors[9],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = darkText,
                       background = colors[9],
                       padding = 5
                       ),
              widget.TextBox(
                    text = '◥',
                    background = colors[9],
                    foreground = colors[10],
                    fontsize = 60,
                    width = 27
                    ),
              widget.TextBox(
                       text = " ☐",
                       foreground = darkText,
                       background = colors[10],
                       padding = 0
                       ),
              widget.CurrentLayout(
                       foreground = darkText,
                       background = colors[10],
                       padding = 5
                       ),
                widget.TextBox(
                      text = '◥',
                      background = colors[10],
                      foreground = colors[11],
                      fontsize = 60,
                      width = 27
                      ),
              widget.Clock(
                       foreground = darkText,
                       background = colors[11],
                       padding = 5,
                       format = "%A, %B %d  [ %H:%M ]"

                       ),
              widget.Systray(
                       background = colors[11],
                       padding = 5
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

# def init_screens():
#     return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
#             Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
#             Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

def init_screens():
    return [Screen(),
            Screen()]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
