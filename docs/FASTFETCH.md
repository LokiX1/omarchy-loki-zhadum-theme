# Fastfetch companion preset

The Fastfetch preset is optional. Installing the Loki Zhadum Omarchy theme does
not automatically replace an existing Fastfetch configuration.

## Requirements

This layout uses the Kitty graphics protocol:

- Terminal: Kitty
- Fastfetch logo type: `kitty`

## Included files

```text
fastfetch/loki-zhadum.jsonc
fastfetch/images/loki-zhadum-emblem.png
```

The emblem is a native-alpha PNG (true transparency, no baked checkerboard),
regenerated reproducibly with:

```text
scripts/generate-loki-zhadum-emblem.py
```

## Preview without changing your config

```bash
fastfetch --config \
  ~/.config/omarchy/themes/loki-zhadum/fastfetch/loki-zhadum.jsonc
```

## Install as your default Fastfetch config

```bash
mkdir -p ~/.config/fastfetch/images

cp \
  ~/.config/omarchy/themes/loki-zhadum/fastfetch/images/loki-zhadum-emblem.png \
  ~/.config/fastfetch/images/loki-zhadum-emblem.png

cp \
  ~/.config/omarchy/themes/loki-zhadum/fastfetch/loki-zhadum.jsonc \
  ~/.config/fastfetch/config.jsonc
```

## Image layout

The supplied image-logo layout uses:

```jsonc
"logo": {
  "type": "kitty",
  "source": "~/.config/fastfetch/images/loki-zhadum-emblem.png",
  "width": 41,
  "height": 29,
  "padding": {
    "top": 1,
    "left": 2,
    "right": 2
  }
}
```

Adjust `width`, `height`, and `padding` locally if your font, terminal size,
or monitor layout needs a different arrangement.
