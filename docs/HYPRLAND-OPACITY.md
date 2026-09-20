# Hyprland opacity companion

Loki Zhadum includes an optional Hyprland rule snippet for a subtle
inactive-window fade. Omarchy defines default window opacity rules outside the
theme-template system, so this companion is intentionally opt-in.

The snippet is:

```text
extras/hypr/loki-zhadum-opacity.lua
```

## Behavior

- Focused normal windows: 1.00 opacity
- Inactive normal windows: 0.99 opacity
- Inactive Chromium- and Firefox-family browsers: 0.99 opacity
- Qutebrowser: 1.00 opacity through its own rule
- Video-playing windows: 1.00 opacity

A global Hyprland `inactive_opacity` setting can still provide a gentle visual
fade to any unfocused window, including Qutebrowser.

## Install

Back up your active Hyprland look-and-feel configuration:

```bash
cp ~/.config/hypr/looknfeel.lua \
  ~/.config/hypr/looknfeel.lua.before-loki-zhadum-opacity
```

Open the file in Neovim:

```bash
nvim ~/.config/hypr/looknfeel.lua
```

Copy the reviewed rules from:

```text
~/.config/omarchy/themes/loki-zhadum/extras/hypr/loki-zhadum-opacity.lua
```

Reload Hyprland:

```bash
hyprctl reload
```

Some opacity behavior is assigned when a client opens, so restart applications
you want to retest.

## Qutebrowser fix

Qutebrowser’s Hyprland class is:

```text
org.qutebrowser.qutebrowser
```

Do not use a terminal-style Qutebrowser rule such as:

```lua
opacity = "0.90 0.85"
```

It makes the browser uncomfortably transparent. Use the reviewed rule included
in the companion instead:

```lua
o.window("^org%.qutebrowser%.qutebrowser$", {
  tag = "-default-opacity",
  opacity = "1.0 override 1.0 override",
})
```

See [`QUTEBROWSER.md`](QUTEBROWSER.md) for the matching opaque Qutebrowser UI
preset.
