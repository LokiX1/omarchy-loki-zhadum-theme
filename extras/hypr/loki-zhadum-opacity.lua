-- Loki Zhadum companion: subtle inactive-window fade.
--
-- Add these rules to ~/.config/hypr/looknfeel.lua after reviewing them.
-- They are intentionally not applied automatically by the theme.
--
-- This snippet assumes Omarchy's default window tagging. The separate
-- qutebrowser rule prevents an old terminal-style 0.90/0.85 rule from making
-- qutebrowser unusably transparent. The compositor's global inactive_opacity
-- setting may still provide a subtle fade when qutebrowser loses focus.

o.window({ tag = "default-opacity" }, { opacity = "1.0 0.99" })

o.window({ tag = "chromium-based-browser" }, { opacity = "1.0 override 0.99 override" })
o.window({ tag = "firefox-based-browser" }, { opacity = "1.0 override 0.99 override" })

-- Qutebrowser: solid while focused. Keep it out of default-opacity so an old
-- terminal-style rule cannot compound alpha/transparency.
o.window("^org%.qutebrowser%.qutebrowser$", {
  tag = "-default-opacity",
  opacity = "1.0 override 1.0 override",
})

o.window({ tag = "video-playing" }, { opacity = "1.0 override 1.0 override" })
