# Wallpaper keep-alive service

`mpvpaper` is unsupervised by default: it can die on some loops, and nothing
restarts it, so the desktop falls through to Omarchy's built-in single-image
background. This repo ships a systemd user service that keeps one mpvpaper
per monitor alive.

## Files

```text
extras/systemd/zhadum-wallpapers.service      # unit
extras/systemd/zhadum-wallpapers-service.sh  # foreground wrapper
```

The wrapper starts one `mpvpaper -l bottom` per monitor from
`~/backgrounds/zhadum/` (Niflheim / Zhadum / Galdr, seeded from
`backgrounds/zhadum-triptych/` on first deploy) and exits non-zero if any
of them dies, so systemd restarts the whole set (`Restart=on-failure`).
It waits up to ~30s for the Wayland socket, so the service can start at
login even if it races the compositor.

## Install

```bash
cd ~/.config/omarchy/themes/loki-zhadum
./scripts/zhadum-deploy wallpaper-service
```

This seeds `~/backgrounds/zhadum/` from the repo triptych if needed,
installs the wrapper + unit (backing up anything already there), makes the
autostart launcher defer to the service while it's active, then enables
and starts it.

Manual install:

```bash
THEME=~/.config/omarchy/themes/loki-zhadum
install -Dm755 "$THEME/extras/systemd/zhadum-wallpapers-service.sh" \
  ~/.config/hypr/zhadum-wallpapers-service.sh
install -Dm644 "$THEME/extras/systemd/zhadum-wallpapers.service" \
  ~/.config/systemd/user/zhadum-wallpapers.service
systemctl --user daemon-reload
systemctl --user enable --now zhadum-wallpapers.service
```

## Verify / remove

```bash
systemctl --user status zhadum-wallpapers.service
./scripts/zhadum-deploy status   # shows service state + mpvpaper count

# remove (falls back to the autostart launcher behavior):
systemctl --user disable --now zhadum-wallpapers.service
```

The autostart launcher (`~/.config/hypr/zhadum-wallpapers.sh`) defers to
the service while it's active and works standalone when the service is
disabled, so removing the service cleanly falls back to the previous
setup.
