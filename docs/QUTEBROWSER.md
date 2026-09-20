# Qutebrowser companion

The Loki Zhadum Qutebrowser companion keeps browser-owned surfaces opaque while
preserving the desktop's subtle inactive-window fade through Hyprland.

## Why this exists

A previous local Qutebrowser Hyprland rule used terminal-style opacity:

```lua
opacity = "0.90 0.85"
```

That made the browser severely transparent even with
`c.window.transparent = False`. The working Qutebrowser class is:

```text
org.qutebrowser.qutebrowser
```

The companion uses a focused/unfocused compositor override of `1.0 / 1.0`.
If your Hyprland configuration has a global `inactive_opacity` setting, it can
still supply the gentle fade when Qutebrowser is not focused.

## Install the opaque UI preset

The file in `qutebrowser/theme.py` is an opaque copy of the generated Omarchy
theme output. It removes alpha-bearing `rgba(...)` background colors and keeps:

```python
c.window.transparent = False
```

Back up the generated Qutebrowser theme, then install the preset:

```bash
cp ~/.config/qutebrowser/theme.py \
  ~/.config/qutebrowser/theme.py.before-loki-zhadum

cp ~/.config/omarchy/themes/loki-zhadum/qutebrowser/theme.py \
  ~/.config/qutebrowser/theme.py
```

Restart Qutebrowser:

```bash
pkill qutebrowser
qutebrowser &
```

Verify that no translucent UI backgrounds remain:

```bash
grep -niE 'window\.transparent|rgba\(' \
  ~/.config/qutebrowser/theme.py
```

The expected result contains `c.window.transparent = False` and no `rgba(`
matches.

## Hyprland rule

Add the Qutebrowser block from
`extras/hypr/loki-zhadum-opacity.lua` to your active
`~/.config/hypr/hyprland.lua` or equivalent window-rule source:

```lua
o.window("^org%.qutebrowser%.qutebrowser$", {
  tag = "-default-opacity",
  opacity = "1.0 override 1.0 override",
})
```

Reload Hyprland and restart Qutebrowser:

```bash
hyprctl reload
pkill qutebrowser
qutebrowser &
```

## Regeneration note

Omarchy can regenerate `~/.config/qutebrowser/theme.py` when themes are
applied. If translucency returns, rerun the copy command above. This repository
keeps the opaque preset as a reviewed source copy rather than silently
overwriting an existing Qutebrowser configuration during normal theme install.
