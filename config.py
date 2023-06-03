#
# LINKIO'S QTILE CONFIG
#

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "i", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "n", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "e", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "m", lazy.layout.swap_main(), desc="Promote focused window to master"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating state of focused window"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "r", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

def init_group_names():
    return [('I', {'layout': 'monadtall'}),
            ('II', {'layout': 'monadtall'}),
            ('III', {'layout': 'monadtall'}),
            ('IV', {'layout': 'monadtall'}),
            ('V', {'layout': 'monadtall'}),]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))		# Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))		# Send current window to another group	

layouts = [
    layout.MonadTall(
	border_focus='#ebdbb2',
	border_normal='#282828',
	border_width=2,
	margin=5,
	ratio=0.55,
	),
    # layout.Max(),
    # layout.Floating(
    #	border_focus='#ebdbb2',
    #	border_normal='#282828',
    #	),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Columns(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.Spiral(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
		    background='#1d2021', 
		    highlight_method='text',
		    this_current_screen_border='#fe8019',
		    hide_unused=True
		),
                widget.WindowName(background='#1d2021'),
                widget.Systray(backgorund='#1d2021'),
		widget.TextBox("🔉", background='#1d2021'),
		widget.PulseVolume(background='#1d2021'),
		widget.OpenWeather(
		    background='#1d2021',
		    zip='23185', 
		    metric=False,
		    format='{location_city}: {temp} °{units_temperature} {icon} {weather_details}'
		),
		widget.TextBox("⏰", background='#1d2021'),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", background='#1d2021'),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus='#ebdbb2',
    border_normal='#282828',
    border_width=2,
    margin=5, 
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
