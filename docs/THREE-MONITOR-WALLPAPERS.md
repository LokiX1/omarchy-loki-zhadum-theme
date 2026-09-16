# Three-monitor wallpapers

Loki Osiris includes an optional static Hyprpaper profile with three coordinated
wallpapers.

![Loki Osiris three-monitor clean layout](../screenshots/loki-osiris-three-monitor-clean-layout.jpg)

![Loki Osiris three-monitor desktop](../screenshots/loki-osiris-three-monitor-desktop.png)

![Loki Osiris three-monitor wallpaper set](../screenshots/loki-osiris-three-monitor-wallpapers.jpg)

The first preview shows the complete three-monitor wallpaper layout without
applications covering the backgrounds. The second shows Loki Osiris in active
desktop use. The third shows the three coordinated static backgrounds included
with the theme.

## Included images

```text
backgrounds/three-monitor/caelum-left-portrait-2880x2880.jpg
backgrounds/three-monitor/roche-center-5120x2880.jpg
backgrounds/three-monitor/outland-right-portrait-2880x2880.jpg
```

## Tested layout

The included example was tested with:

```text
DP-2  Left portrait display   → Caelum
DP-1  Center ultrawide        → Roche
DP-3  Right portrait display  → Outland
```

Your monitor names may differ. Check them with:

```bash
hyprctl monitors
```

## Install Hyprpaper

On Arch and Omarchy:

```bash
sudo pacman -S hyprpaper
```

## Apply the example

Back up an existing Hyprpaper config first:

```bash
test -f ~/.config/hypr/hyprpaper.conf && \
  cp -av \
    ~/.config/hypr/hyprpaper.conf \
    ~/.config/hypr/hyprpaper.conf.before-loki-osiris
```

The example uses the author's `DP-1`, `DP-2`, and `DP-3` output names and
`/home/loki` path. It is a tested reference profile, not an automatic
configuration for every installation.

Copy the example:

```bash
mkdir -p ~/.config/hypr

cp \
  ~/.config/omarchy/themes/loki-osiris/extras/hypr/hyprpaper-three-monitor.conf.example \
  ~/.config/hypr/hyprpaper.conf
```

Edit the copied file before starting Hyprpaper:

- Replace `DP-1`, `DP-2`, and `DP-3` with your own output names.
- Replace `/home/loki` with your own home-directory path.
- Change or remove display blocks you do not use.

## Start Hyprpaper

Start it for the current session:

```bash
hyprpaper &
```

Inspect active assignments:

```bash
hyprctl hyprpaper listactive
```

## Persistent user service

Create a user service:

```bash
mkdir -p ~/.config/systemd/user

cat > ~/.config/systemd/user/hyprpaper.service <<'UNIT'
[Unit]
Description=Hyprpaper wallpaper service
After=graphical-session-pre.target
PartOf=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/hyprpaper
Restart=on-failure
RestartSec=2

[Install]
WantedBy=graphical-session.target
UNIT
```

Enable it:

```bash
systemctl --user daemon-reload
systemctl --user enable --now hyprpaper.service
```

## Compatibility

Use one wallpaper renderer at a time. Disable or stop conflicting wallpaper
services such as Wallpaper Engine, Waypaper Video, `mpvpaper`, `swww`, or other
wallpaper managers before using this Hyprpaper profile.
