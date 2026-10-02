#!/usr/bin/env python3
"""Loki Zhadum horned emblem v2 — native-alpha PNG for fastfetch/theme use.

Composition (1024x1024, drawn at 2x supersample, true RGBA transparency):
  * circular rune halo — double ring with abstract glyph ticks (no text)
  * paired upward-sweeping horns — violet -> magenta gradient, cyan rim light
  * descending circuit-sigil spine — traces, node dots, faceted gem
Palette: Zhadum ultraviolet/violet/magenta/cyan on transparent.
"""
import math
import os
import sys
from PIL import Image, ImageDraw, ImageFilter

S = 2
W = H = 1024 * S
CX, CY = 512 * S, 512 * S

VIOLET_DEEP = (110, 30, 170)
VIOLET = (155, 46, 205)
VIOLET_BRIGHT = (196, 120, 255)
MAGENTA = (255, 79, 216)
MAGENTA_SOFT = (255, 140, 230)
CYAN = (110, 231, 255)
CYAN_DIM = (70, 160, 200)
PALE = (235, 220, 255)


def vgrad(w, h, stops):
    col = Image.new("RGB", (1, h))
    dc = ImageDraw.Draw(col)
    for y in range(h):
        t = y / (h - 1)
        for i in range(len(stops) - 1):
            t0, c0 = stops[i]
            t1, c1 = stops[i + 1]
            if t0 <= t <= t1:
                f = (t - t0) / (t1 - t0) if t1 > t0 else 0
                dc.point((0, y),
                         tuple(int(a + (b - a) * f) for a, b in zip(c0, c1)))
                break
    return col.resize((w, h))


def qbez(p0, p1, p2, t):
    u = 1 - t
    return (u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
            u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1])


def qbez_d(p0, p1, p2, t):
    return (2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0]),
            2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1]))


def tapered_poly(p0, p1, p2, w0, w1, n=64):
    """Polygon of a tapering stroke along a quadratic bezier."""
    left, right = [], []
    for i in range(n + 1):
        t = i / n
        x, y = qbez(p0, p1, p2, t)
        dx, dy = qbez_d(p0, p1, p2, t)
        m = math.hypot(dx, dy) or 1
        nx, ny = -dy / m, dx / m
        w = (w0 * (1 - t) + w1 * t) / 2
        left.append((x + nx * w, y + ny * w))
        right.append((x - nx * w, y - ny * w))
    return left + right[::-1]


img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
g = ImageDraw.Draw(glow)

R_OUT, R_IN = 440 * S, 408 * S
RING_W = 7 * S

# --- rune halo: double ring -------------------------------------------
for r, col, w in ((R_OUT, VIOLET, RING_W), (R_IN, VIOLET_DEEP, RING_W - 2 * S)):
    d.ellipse([CX - r, CY - r, CX + r, CY + r], outline=col + (255,), width=w)
    g.ellipse([CX - r, CY - r, CX + r, CY + r],
              outline=MAGENTA + (255,), width=w)

# abstract glyph ticks between the rings (no readable text)
import random
random.seed(1337)
for i in range(24):
    a = math.radians(i * 15 + 7.5)
    rmid = (R_OUT + R_IN) / 2
    x, y = CX + rmid * math.cos(a), CY + rmid * math.sin(a)
    kind = i % 4
    col = (MAGENTA if i % 2 == 0 else CYAN) + (255,)
    s2 = 9 * S
    if kind == 0:      # diamond
        d.polygon([(x, y - s2), (x + s2 * 0.6, y),
                   (x, y + s2), (x - s2 * 0.6, y)], fill=col)
    elif kind == 1:    # dot
        d.ellipse([x - s2 * 0.5, y - s2 * 0.5,
                   x + s2 * 0.5, y + s2 * 0.5], fill=col)
    elif kind == 2:    # cross tick
        d.line([x - s2, y, x + s2, y], fill=col, width=4 * S)
        d.line([x, y - s2, x, y + s2], fill=col, width=4 * S)
    else:              # chevron
        d.line([x - s2, y + s2 * 0.6, x, y - s2 * 0.6,
                x + s2, y + s2 * 0.6], fill=col, width=4 * S,
               joint="curve")

# --- horns: upward-sweeping pair --------------------------------------
horn_mask = Image.new("L", (W, H), 0)
hm = ImageDraw.Draw(horn_mask)
horns = []
for sgn in (-1, 1):
    p0 = (CX + sgn * 150 * S, CY + 190 * S)
    p1 = (CX + sgn * 330 * S, CY - 40 * S)
    p2 = (CX + sgn * 215 * S, CY - 330 * S)
    poly = tapered_poly(p0, p1, p2, 96 * S, 8 * S)
    horns.append((poly, p0, p1, p2))
    hm.polygon(poly, fill=255)
horn_layer = None  # (kept for clarity; gradient paints directly below)
# paint a full-canvas vertical gradient through the horn mask
# (magenta at the top where the horn tips are, deep violet at the base)
horn_grad = vgrad(W, H, [(0.0, MAGENTA), (0.35, VIOLET), (0.75, VIOLET_DEEP)])
grad_rgba = horn_grad.convert("RGBA")
blank = Image.new("RGBA", (W, H), (0, 0, 0, 0))
blank.paste(grad_rgba, (0, 0), horn_mask)
img.alpha_composite(blank)
g.bitmap((0, 0), horn_mask, fill=MAGENTA + (255,))

# cyan rim light along each horn's outer edge
for poly, p0, p1, p2 in horns:
    edge = []
    for i in range(65):
        t = i / 64
        x, y = qbez(p0, p1, p2, t)
        dx, dy = qbez_d(p0, p1, p2, t)
        m = math.hypot(dx, dy) or 1
        w = (96 * S * (1 - t) + 8 * S * t) / 2
        sgn = 1 if p0[0] < CX else -1
        edge.append((x - sgn * (-dy / m) * w * 0.82,
                     y - sgn * (dx / m) * w * 0.82))
    d.line(edge, fill=CYAN + (255,), width=4 * S, joint="curve")

# --- circuit-sigil spine ----------------------------------------------
spine_x = CX
spine_top, spine_bot = CY - 130 * S, CY + 300 * S
d.line([spine_x, spine_top, spine_x, spine_bot],
       fill=VIOLET_BRIGHT + (255,), width=8 * S)
g.line([spine_x, spine_top, spine_x, spine_bot],
       fill=VIOLET + (255,), width=10 * S)

random.seed(77)
node_ys = [CY - 60 * S, CY + 20 * S, CY + 100 * S, CY + 180 * S, CY + 250 * S]
for k, ny in enumerate(node_ys):
    sgn = 1 if k % 2 == 0 else -1
    x1 = spine_x + sgn * 95 * S
    x2 = spine_x + sgn * 150 * S
    col = (CYAN if k % 2 == 0 else MAGENTA_SOFT) + (255,)
    d.line([spine_x, ny, x1, ny, x1, ny - 34 * S, x2, ny - 34 * S],
           fill=col, width=5 * S, joint="curve")
    d.ellipse([x2 - 11 * S, ny - 34 * S - 11 * S,
               x2 + 11 * S, ny - 34 * S + 11 * S], fill=col)
    d.ellipse([spine_x - 8 * S, ny - 8 * S,
               spine_x + 8 * S, ny + 8 * S], fill=PALE + (255,))
    g.ellipse([x2 - 11 * S, ny - 34 * S - 11 * S,
               x2 + 11 * S, ny - 34 * S + 11 * S], fill=col)

# faceted gem at the spine's heart
gx, gy, gr = spine_x, CY + 60 * S, 46 * S
gem = [(gx, gy - gr * 1.25), (gx + gr * 0.8, gy - gr * 0.35),
       (gx + gr * 0.5, gy + gr * 0.9), (gx, gy + gr * 1.25),
       (gx - gr * 0.5, gy + gr * 0.9), (gx - gr * 0.8, gy - gr * 0.35)]
d.polygon(gem, fill=MAGENTA + (255,), outline=PALE + (255,))
d.polygon([(gx, gy - gr * 1.25), (gx + gr * 0.8, gy - gr * 0.35),
           (gx, gy + gr * 0.1), (gx - gr * 0.8, gy - gr * 0.35)],
          fill=(255, 200, 245, 255))
d.ellipse([gx - 12 * S, gy - 14 * S, gx + 2 * S, gy], fill=(255, 255, 255, 230))
g.polygon(gem, fill=MAGENTA + (255,))

# crown base bridging the horns
d.arc([CX - 190 * S, CY + 60 * S, CX + 190 * S, CY + 320 * S],
      start=20, end=160, fill=VIOLET + (255,), width=10 * S)

# --- neon glow pass ----------------------------------------------------
glow = glow.filter(ImageFilter.GaussianBlur(14 * S))
img = Image.alpha_composite(Image.alpha_composite(
    Image.new("RGBA", (W, H), (0, 0, 0, 0)), glow), img)

img = img.resize((1024, 1024), Image.LANCZOS)

# Output: repo's fastfetch/images/loki-zhadum-emblem.png by default
# (script lives in scripts/, so repo root is one level up); or argv[1].
if len(sys.argv) > 1:
    out = sys.argv[1]
else:
    here = os.path.dirname(os.path.abspath(__file__))
    repo = here if os.path.isfile(os.path.join(here, "colors.toml")) \
        else os.path.dirname(here)
    out = os.path.join(repo, "fastfetch", "images",
                       "loki-zhadum-emblem.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
img.save(out)
print("wrote", out)

# verify true alpha
a = img.getchannel("A")
print("mode:", img.mode, "size:", img.size)
print("corners alpha:", a.getpixel((0, 0)), a.getpixel((1023, 0)),
      a.getpixel((0, 1023)), a.getpixel((1023, 1023)))
print("center alpha:", a.getpixel((512, 512)))
print("fully transparent px:", a.histogram()[0], "of", 1024 * 1024)
