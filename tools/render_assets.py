#!/usr/bin/env python3
"""Render the profile README's SVG assets in both light and dark themes.

Everything the profile shows as a figure is generated here and committed to the
repo, so nothing on the page depends on a third-party card service staying up.

Usage:
    python3 tools/render_assets.py          # writes assets/*.svg
"""

from __future__ import annotations

import os

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")

SANS = "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,SF Mono,Menlo,Consolas,Liberation Mono,monospace"

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "panel": "#161b22",
        "panel2": "#1c2128",
        "border": "#30363d",
        "grid": "#21262d",
        "text": "#e6edf3",
        "muted": "#8b949e",
        "faint": "#6e7681",
        "accent": "#58a6ff",
        "accent2": "#3fb950",
        "accent3": "#d29922",
        "chip": "#1f6feb",
    },
    "light": {
        "bg": "#ffffff",
        "panel": "#f6f8fa",
        "panel2": "#eaeef2",
        "border": "#d0d7de",
        "grid": "#e6eaef",
        "text": "#1f2328",
        "muted": "#59636e",
        "faint": "#818b98",
        "accent": "#0969da",
        "accent2": "#1a7f37",
        "accent3": "#9a6700",
        "chip": "#0969da",
    },
}


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def text(x, y, s, *, fill, size=14, family=SANS, weight="400", anchor="start",
         spacing=None, opacity=None):
    extra = ""
    if spacing is not None:
        extra += f' letter-spacing="{spacing}"'
    if opacity is not None:
        extra += f' opacity="{opacity}"'
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"{extra}>'
            f'{esc(s)}</text>')


def rect(x, y, w, h, *, fill, stroke=None, rx=6, sw=1, opacity=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{o}/>'


# --------------------------------------------------------------------------
# 1. Hero banner
# --------------------------------------------------------------------------
def hero(c: dict) -> str:
    W, H = 1000, 240
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="Jaerak Son, Robotics Engineer">']

    p.append('<defs>')
    p.append(f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0" stop-color="{c["bg"]}"/>'
             f'<stop offset="1" stop-color="{c["panel"]}"/></linearGradient>')
    p.append(f'<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">'
             f'<stop offset="0" stop-color="{c["accent"]}"/>'
             f'<stop offset="0.55" stop-color="{c["accent2"]}"/>'
             f'<stop offset="1" stop-color="{c["accent"]}" stop-opacity="0"/></linearGradient>')
    p.append(f'<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">'
             f'<path d="M24 0H0V24" fill="none" stroke="{c["grid"]}" stroke-width="1"/></pattern>')
    p.append('</defs>')

    p.append(f'<rect width="{W}" height="{H}" rx="10" fill="url(#bg)"/>')
    p.append(f'<rect width="{W}" height="{H}" rx="10" fill="url(#grid)" opacity="0.55"/>')
    p.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="none" '
             f'stroke="{c["border"]}"/>')

    # left content
    p.append(text(48, 62, "ROBOTICS  ·  MOTION PLANNING  ·  CONTROL", fill=c["accent"],
                  size=13, family=MONO, weight="600", spacing="2.5"))
    p.append(text(46, 122, "Jaerak Son", fill=c["text"], size=54, weight="700", spacing="-1"))
    p.append(f'<rect x="48" y="140" width="420" height="2" fill="url(#rule)"/>')
    p.append(text(48, 172, "Building the control stack for double-steering-drive omni AMRs —",
                  fill=c["muted"], size=15))
    p.append(text(48, 194, "from URDF and ros2_control plugins to docking benchmarks.",
                  fill=c["muted"], size=15))

    chips = ["ROS 2 Jazzy", "C++17", "Python", "ros2_control", "Nav2", "Gazebo"]
    x = 48
    for ch in chips:
        w = 11 + len(ch) * 7.1
        p.append(rect(x, 208, w, 22, fill=c["panel2"], stroke=c["border"], rx=11))
        p.append(text(x + w / 2, 223, ch, fill=c["faint"], size=11, family=MONO, anchor="middle"))
        x += w + 8

    # right: DSD robot schematic — two steerable wheel modules on a rectangular base
    cx, cy = 812, 118
    p.append(f'<g transform="translate({cx},{cy})">')
    p.append(f'<circle cx="0" cy="0" r="96" fill="none" stroke="{c["border"]}" '
             f'stroke-dasharray="3 5" opacity="0.7"/>')
    # chassis
    p.append(rect(-66, -44, 132, 88, fill=c["panel2"], stroke=c["accent"], rx=10, sw=1.6))
    # steering modules (front-left, rear-right) drawn rotated to show independent steering
    for (mx, my, ang) in ((-66, -44, -32), (66, 44, 28)):
        p.append(f'<g transform="translate({mx},{my}) rotate({ang})">')
        p.append(rect(-13, -22, 26, 44, fill=c["bg"], stroke=c["accent2"], rx=5, sw=1.6))
        p.append(f'<line x1="0" y1="-30" x2="0" y2="30" stroke="{c["accent2"]}" '
                 f'stroke-width="1" opacity="0.55"/>')
        p.append('</g>')
    for (mx, my) in ((66, -44), (-66, 44)):
        p.append(f'<circle cx="{mx}" cy="{my}" r="9" fill="none" stroke="{c["faint"]}" '
                 f'stroke-width="1.4"/>')
        p.append(f'<circle cx="{mx}" cy="{my}" r="2" fill="{c["faint"]}"/>')
    # body-frame velocity vectors
    p.append(f'<line x1="0" y1="0" x2="52" y2="-30" stroke="{c["accent3"]}" stroke-width="2.4" '
             f'stroke-linecap="round"/>')
    p.append(f'<path d="M52 -30 L41 -30 L48 -22 Z" fill="{c["accent3"]}"/>')
    p.append(f'<path d="M28 0 A28 28 0 0 0 24 -14" fill="none" stroke="{c["accent3"]}" '
             f'stroke-width="1.8" opacity="0.85"/>')
    p.append(text(58, -36, "v", fill=c["accent3"], size=13, family=MONO, weight="700"))
    p.append(text(34, -18, "ω", fill=c["accent3"], size=12, family=MONO, opacity=0.9))
    p.append(f'<circle cx="0" cy="0" r="3" fill="{c["text"]}"/>')
    p.append('</g>')
    p.append(text(812, 232, "double-steering-drive · holonomic", fill=c["faint"], size=11,
                  family=MONO, anchor="middle"))

    p.append('</svg>')
    return "\n".join(p)


# --------------------------------------------------------------------------
# 2. Stack diagram
# --------------------------------------------------------------------------
def stack(c: dict) -> str:
    W, H = 1000, 330
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="DSD omni-AMR software stack">']
    p.append(f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             f'markerHeight="7" orient="auto-start-reverse">'
             f'<path d="M0 0 L10 5 L0 10 z" fill="{c["faint"]}"/></marker></defs>')
    p.append(f'<rect width="{W}" height="{H}" rx="10" fill="{c["bg"]}" stroke="{c["border"]}"/>')
    p.append(text(28, 38, "THE DSD OMNI-AMR STACK", fill=c["muted"], size=12, family=MONO,
                  weight="600", spacing="2"))
    p.append(f'<line x1="28" y1="50" x2="{W-28}" y2="50" stroke="{c["border"]}"/>')

    boxes = [
        (28, 78, "dsd_bot_description", "URDF / xacro", "CMake", c["accent"]),
        (268, 78, "double_steering_drive_controller", "ros2_control plugin", "C++", c["accent2"]),
        (596, 78, "pgv_tracing_mode", "PGV line align / trace", "Python", c["accent"]),
        (800, 78, "omni-docking-bench", "ICROS 2026 benchmark", "Python", c["accent3"]),
    ]
    widths = [216, 304, 192, 172]
    for (x, y, name, sub, lang, col), w in zip(boxes, widths):
        p.append(rect(x, y, w, 86, fill=c["panel"], stroke=col, rx=8, sw=1.4))
        p.append(f'<rect x="{x}" y="{y}" width="4" height="86" rx="2" fill="{col}"/>')
        size = 13 if len(name) < 26 else 11.5
        p.append(text(x + 16, y + 30, name, fill=c["text"], size=size, family=MONO, weight="700"))
        p.append(text(x + 16, y + 52, sub, fill=c["muted"], size=12))
        chip_w = 14 + len(lang) * 6.6
        p.append(rect(x + 16, y + 62, chip_w, 18, fill=c["panel2"], stroke=c["border"], rx=9))
        p.append(text(x + 16 + chip_w / 2, y + 75, lang, fill=c["faint"], size=10,
                      family=MONO, anchor="middle"))

    for x1, x2 in ((244, 268), (572, 596), (788, 800)):
        p.append(f'<line x1="{x1}" y1="121" x2="{x2-3}" y2="121" stroke="{c["faint"]}" '
                 f'stroke-width="1.6" marker-end="url(#ar)"/>')

    # second row — supporting + independent modules
    p.append(rect(28, 208, 304, 86, fill=c["panel"], stroke=c["border"], rx=8))
    p.append(text(44, 236, "dsd_control_demo", fill=c["text"], size=13, family=MONO, weight="700"))
    p.append(text(44, 258, "ros2_control hardware interface + bringup", fill=c["muted"], size=12))
    p.append(text(44, 280, "C++  ·  Gazebo & real hardware", fill=c["faint"], size=11, family=MONO))

    p.append(rect(360, 208, 304, 86, fill=c["panel"], stroke=c["border"], rx=8))
    p.append(text(376, 236, "payload_mass_estimator", fill=c["text"], size=13, family=MONO,
                  weight="700"))
    p.append(text(376, 258, "online payload mass — bounded RLS", fill=c["muted"], size=12))
    p.append(text(376, 280, "C++  ·  gated on straight-line excitation", fill=c["faint"], size=11,
                  family=MONO))

    p.append(rect(692, 208, 280, 86, fill=c["panel"], stroke=c["border"], rx=8))
    p.append(text(708, 236, "Sampling-Based-Planning", fill=c["text"], size=13, family=MONO,
                  weight="700"))
    p.append(text(708, 258, "PRM · RRT · RRT* · Informed RRT*", fill=c["muted"], size=12))
    p.append(text(708, 280, "Python  ·  lecture series", fill=c["faint"], size=11, family=MONO))

    p.append(f'<line x1="180" y1="164" x2="180" y2="208" stroke="{c["faint"]}" '
             f'stroke-width="1.6" stroke-dasharray="4 4" marker-end="url(#ar)"/>')
    p.append('</svg>')
    return "\n".join(p)


# --------------------------------------------------------------------------
# 3. Docking benchmark figure
# --------------------------------------------------------------------------
def docking(c: dict) -> str:
    import math
    W, H = 1000, 320
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="Short-range docking benchmark protocol">']
    p.append(f'<defs><marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
             f'markerHeight="6" orient="auto-start-reverse">'
             f'<path d="M0 0 L10 5 L0 10 z" fill="{c["accent"]}"/></marker></defs>')
    p.append(f'<rect width="{W}" height="{H}" rx="10" fill="{c["bg"]}" stroke="{c["border"]}"/>')
    p.append(text(28, 38, "SHORT-RANGE DOCKING BENCHMARK  ·  ICROS 2026", fill=c["muted"],
                  size=12, family=MONO, weight="600", spacing="2"))
    p.append(f'<line x1="28" y1="50" x2="{W-28}" y2="50" stroke="{c["border"]}"/>')

    cx, cy = 250, 190
    p.append(f'<g transform="translate({cx},{cy})">')
    for r, lab in ((110, "3 cm start"), (26, "3 mm settle")):
        dash = '3 5' if r > 40 else '2 3'
        col = c["border"] if r > 40 else c["accent2"]
        p.append(f'<circle cx="0" cy="0" r="{r}" fill="none" stroke="{col}" '
                 f'stroke-dasharray="{dash}"/>')
    for i in range(8):
        a = math.radians(i * 45)
        x1, y1 = 104 * math.cos(a), 104 * math.sin(a)
        x2, y2 = 34 * math.cos(a), 34 * math.sin(a)
        p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{c["accent"]}" stroke-width="1.6" opacity="0.85" '
                 f'marker-end="url(#ar2)"/>')
        p.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="3" fill="{c["accent"]}"/>')
    p.append(f'<circle cx="0" cy="0" r="26" fill="{c["accent2"]}" opacity="0.12"/>')
    p.append(rect(-16, -16, 32, 32, fill=c["panel2"], stroke=c["accent2"], rx=4, sw=1.6))
    p.append(f'<line x1="-7" y1="0" x2="7" y2="0" stroke="{c["accent2"]}" stroke-width="1.6"/>')
    p.append(f'<line x1="0" y1="-7" x2="0" y2="7" stroke="{c["accent2"]}" stroke-width="1.6"/>')
    p.append('</g>')
    p.append(text(250, 82, "8 approach directions × heading offsets × repeats",
                  fill=c["faint"], size=11.5, family=MONO, anchor="middle"))
    p.append(text(250, 306, "target pose  ·  PGV fiducial feedback", fill=c["faint"],
                  size=11, family=MONO, anchor="middle"))

    # right: controllers under test
    x0 = 470
    p.append(text(x0, 86, "Controllers under test", fill=c["text"], size=14, weight="700"))
    rows = [
        ("Kinematic", "proposed  ·  PGV-direct feedback", c["accent2"], True),
        ("MPPI", "baseline  ·  sampling-based MPC (Nav2)", c["accent"], False),
        ("DWB", "baseline  ·  dynamic window (Nav2)", c["accent"], False),
    ]
    y = 106
    for name, sub, col, mine in rows:
        p.append(rect(x0, y, 500, 52, fill=c["panel"], stroke=c["border"], rx=8))
        p.append(f'<rect x="{x0}" y="{y}" width="4" height="52" rx="2" fill="{col}"/>')
        p.append(text(x0 + 18, y + 24, name, fill=c["text"], size=14, family=MONO, weight="700"))
        if mine:
            p.append(rect(x0 + 18 + len(name) * 9 + 10, y + 11, 44, 17, fill=col, rx=8,
                          opacity=0.18))
            p.append(text(x0 + 18 + len(name) * 9 + 32, y + 24, "ours", fill=col, size=10,
                          family=MONO, weight="700", anchor="middle"))
        p.append(text(x0 + 18, y + 42, sub, fill=c["muted"], size=12))
        y += 62

    p.append(text(x0, 300, "ROS 2 Jazzy · Ubuntu 24.04 · Apache-2.0 · reproducible via Docker",
                  fill=c["faint"], size=11, family=MONO))
    p.append('</svg>')
    return "\n".join(p)


FIGURES = {"hero": hero, "stack": stack, "docking": docking}


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, fn in FIGURES.items():
        for theme, colors in THEMES.items():
            path = os.path.join(OUT_DIR, f"{name}-{theme}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(fn(colors) + "\n")
            print("wrote", os.path.relpath(path, os.path.dirname(OUT_DIR)))


if __name__ == "__main__":
    main()
