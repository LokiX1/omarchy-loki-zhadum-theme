#!/usr/bin/env bash
# Foreground wrapper for the zhadum-wallpapers systemd service.
# Starts one mpvpaper per monitor and exits non-zero if any of them dies,
# so systemd (Restart=on-failure) brings the whole set back.
set -u
BG="$HOME/backgrounds/zhadum"

# Wait for the Wayland socket (up to ~30s) so the service can start at login
# even if it races the compositor.
RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"
for _ in $(seq 1 60); do
  for s in "$RUNTIME_DIR"/wayland-*; do
    if [ -S "$s" ]; then
      export WAYLAND_DISPLAY="$(basename "$s")"
      export XDG_RUNTIME_DIR="$RUNTIME_DIR"
      break 2
    fi
  done
  sleep 0.5
done
if [ -z "${WAYLAND_DISPLAY:-}" ]; then
  echo "zhadum-wallpapers: no Wayland socket found" >&2
  exit 1
fi

# Take over any strays (e.g. from the autostart launcher) so the service is
# the single owner of the mpvpaper processes.
pkill -x mpvpaper 2>/dev/null || true
sleep 0.5

mpvpaper -l bottom -o "no-audio --loop" DP-2 "$BG/zhadum-left-2160x3840.jpg" &
mpvpaper -l bottom -o "no-audio --loop" DP-1 "$BG/zhadum-center-5120x2160.jpg" &
mpvpaper -l bottom -o "no-audio --loop" DP-3 "$BG/zhadum-right-2160x3840.jpg" &
wait -n
echo "zhadum-wallpapers: an mpvpaper instance exited, restarting" >&2
exit 1
