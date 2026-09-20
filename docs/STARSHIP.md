# Starship companion preset

The Starship prompt configuration is optional. Installing the Loki Zhadum
Omarchy theme does not automatically replace an existing Bash prompt.

## Included file

```text
starship/loki-zhadum.toml
```

## Requirements

Bash must initialize Starship from `~/.bashrc`:

```bash
eval "$(starship init bash)"
```

## Preview without changing your default config

Start a temporary interactive Bash session that loads the Loki Zhadum preset:

```bash
STARSHIP_CONFIG=~/.config/omarchy/themes/loki-zhadum/starship/loki-zhadum.toml \
  bash --noprofile --rcfile ~/.bashrc -i
```

Exit the temporary shell when finished:

```bash
exit
```

## Install as your default Starship configuration

Back up your existing configuration:

```bash
cp -av \
  ~/.config/starship.toml \
  ~/.config/starship.toml.before-loki-zhadum
```

Then install the preset:

```bash
cp \
  ~/.config/omarchy/themes/loki-zhadum/starship/loki-zhadum.toml \
  ~/.config/starship.toml
```

Open a new terminal or start a new Bash shell afterward.

## Use without replacing your default config

To use the theme preset without replacing `~/.config/starship.toml`, export
`STARSHIP_CONFIG` from `~/.bashrc` before Starship is initialized:

```bash
export STARSHIP_CONFIG=\
"$HOME/.config/omarchy/themes/loki-zhadum/starship/loki-zhadum.toml"
```

To remove the override later, delete or comment out that `export` line and
open a new Bash shell.
