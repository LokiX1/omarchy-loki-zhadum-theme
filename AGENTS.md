# Loki Zhadum Theme Agent Guide

This document provides essential information for agents working with the Loki Zhadum theme repository, which is a dark purple-black Omarchy theme package.

## Project Overview

This repository contains a theme-only package for Omarchy desktop environment that provides:
- A dark purple-black color palette in the Zhadum aesthetic
- Fastfetch configuration with custom styling
- Starship shell prompt configuration
- Optional CLIamp companion theme for audio visualization

## File Structure

```
.
├── AGENTS.md
├── README.md
├── colors.toml
├── shell.menu.toml           # Optional shell menu styling
├── backgrounds/              # Wallpaper assets
│   ├── osiris-live-still.png # Static still (intentional art/source asset)
│   ├── CREDITS.md
│   └── three-monitor/        # Coordinated 3-monitor wallpapers
├── branding/                 # ZHADUM ASCII art (screensaver, about)
├── docs/
│   ├── BOOT-BRANDING.md
│   ├── CLIAMP.md
│   ├── FASTFETCH.md
│   ├── HYPRLAND-OPACITY.md
│   ├── QUTEBROWSER.md
│   ├── STARSHIP.md
│   └── THREE-MONITOR-WALLPAPERS.md
├── extras/
│   ├── cliamp/loki-zhadum-led.toml
│   └── hypr/
│       ├── hyprpaper-three-monitor.conf.example
│       └── loki-zhadum-opacity.lua
├── fastfetch/
│   ├── loki-zhadum.jsonc
│   └── images/
│       ├── loki-zhadum-emblem.png  # Native-alpha horned emblem (fastfetch logo)
│       ├── loki-zhadum.png
│       ├── lokizhadumff.png
│       └── lokizhadumff-transparent.png
├── qutebrowser/
│   └── theme.py              # Opaque preset (opt-in)
├── scripts/
│   ├── zhadum-plymouth-glitch        # Optional boot/unlock branding generator
│   ├── zhadum-deploy                 # Optional companion-config deployer
│   └── generate-loki-zhadum-emblem.py  # Emblem generator (true-alpha PNG)
├── screenshots/
└── starship/
    └── loki-zhadum.toml
```

## Key Configuration Files

### colors.toml
The core palette definitions in TOML format with:
- Dark background colors (`background`, `dark_background`, etc.)
- Accent and foreground colors with multiple variants (bright, muted)
- Color scheme for various UI elements

### fastfetch/loki-zhadum.jsonc
Fastfetch configuration that includes:
- Custom logo with specific dimensions and positioning
- Hardware information modules with purple color theme
- Software information modules using the theme's color palette
- System status information like uptime, OS age, updates

### starship/loki-zhadum.toml
Starship prompt configuration that:
- Uses a multicolor bar layout with theme-specific gradients
- Includes various system information modules (OS, username, directory, git)
- Displays cloud provider context (AWS, GCP, Azure, OpenStack)
- Shows container and kubernetes context

### CLIamp Integration
The optional CLIamp theme (`extras/cliamp/loki-zhadum-led.toml`) maps:
- Lower spectrum → indigo-violet (`#7e6bff`)
- Middle spectrum → magenta (`#c060e0`)
- Peaks → bright pink (`#ff79c6`)

## Installation Commands

### Install theme
```bash
omarchy theme install https://github.com/LokiX1/omarchy-loki-zhadum-theme.git
```

### Set theme
```bash
omarchy theme set loki-zhadum
```

### Update theme
```bash
omarchy theme update
omarchy theme set loki-zhadum
```

### Install CLIamp companion theme
```bash
mkdir -p ~/.config/cliamp/themes
cp extras/cliamp/loki-zhadum-led.toml ~/.config/cliamp/themes/
```

### Deploy companion configs (recommended)
```bash
./scripts/zhadum-deploy status        # report deployed-vs-repo state
./scripts/zhadum-deploy --dry-run all # preview every change
./scripts/zhadum-deploy all           # install, prompting per component
```
Every write is backed up first and validated after install. Subcommands:
`fastfetch`, `starship`, `cliamp`, `hyprpaper`, `qutebrowser`, `opacity`,
`livewallpaper`.

## Project Characteristics

This is a **theme-only** package that:
- Changes color palettes and assets
- Does not modify personal desktop behavior or install executables
- Is safe for normal Omarchy installation across multiple machines
- Deliberately avoids installing or modifying system configuration files
- Includes only static wallpaper and does not activate live wallpaper hooks

Companion scripts (`scripts/zhadum-deploy`, `scripts/generate-loki-zhadum-emblem.py`) are Python 3 stdlib-only with no build step. All other configurations are in native formats (TOML, JSONC) applied directly by their tools (Omarchy, fastfetch, starship, CLIamp).

## Integration Points

### Fastfetch
The fastfetch configuration is defined in `fastfetch/loki-zhadum.jsonc` with custom modules for system information and color theming.

### Starship
The starship configuration includes a complex multicolor bar layout that integrates well with the purple-black theme aesthetic.

### CLIamp
The optional CLIamp companion theme maps the three spectrum tiers to specific colors from the Loki Zhadum palette to provide audio visualization that matches the desktop theme.

## Qutebrowser

The optional opaque Qutebrowser preset is stored at
`qutebrowser/theme.py`. It intentionally uses:

```python
c.window.transparent = False
```

and solid UI background colors rather than alpha-bearing `rgba(...)` values.

The live file at `~/.config/qutebrowser/theme.py` may be regenerated by
Omarchy when themes are applied. The repository copy is therefore an opt-in,
reviewed preset. See [`docs/QUTEBROWSER.md`](docs/QUTEBROWSER.md) for the
backup/install command and validation check.

The matching Hyprland rule uses Qutebrowser’s verified class:

```lua
o.window("^org%.qutebrowser%.qutebrowser$", {
  tag = "-default-opacity",
  opacity = "1.0 override 1.0 override",
})
```

Do not use a terminal-style Qutebrowser rule such as
`opacity = "0.90 0.85"`—it makes the browser excessively transparent. The
Qutebrowser rule keeps the focused browser solid; a global Hyprland
`inactive_opacity` setting may still provide the intended subtle fade when it
loses focus.

## Additional Resources

For installation instructions, usage examples, and detailed information about each component:
- [`docs/CLIAMP.md`](docs/CLIAMP.md) - CLIamp integration documentation
- [`docs/FASTFETCH.md`](docs/FASTFETCH.md) - Fastfetch configuration documentation
- [`docs/STARSHIP.md`](docs/STARSHIP.md) - Starship configuration documentation
