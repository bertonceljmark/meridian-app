# Meridian handoff (25 Oct 2026)

This is the state of the web prototype when development moved to Claude Code on Mark's Mac.
The web build is a disposable prototype. The real app is native SwiftUI (iPhone, Watch, widgets).
Use this folder as the spec and reference, not as code to port line by line.

## What is live
- `/next/` (https://bertonceljmark.github.io/meridian-app/next/) is the latest build, pass 7e.
  Its storage keys are renamed `meridian.next.*`, so it never touches the home-screen app's data.
- Root `/` is the older home-screen PWA from 23 Oct, which was never updated.
- `/tilt/` is the approved clay-rise scroll (v8), and `/today/neu/v7/` is the approved Today look.

## Folder
- `build/meridian-src-p7e.html` is the 7e source (React in one file, before bundling; md5 837fe979).
  `next/index.html` is the bundle (2194c7db) with the key rename.
- `build/src/` holds the scripts:
  - `r24.py`…`r29.py` are each pass's changes, written as text replacements.
  - `inj7d.py`, `inj7e.py` and `rebuild7e.sh` rebuild the builds.
  - The test scripts are `cadm.js` (cadence matrix), `vis.js` (press on every tappable), `pgfast.js` and `pgfps.js` (page change), `rv/f1.js` (touch swipes) and `smoke/`.
  - `neu.jsx`, `today-neu.css` and `css/` are the design system pieces.
- `docs/` holds:
  - `CONTRACT.md` (product contract v1.1.1);
  - `COMPONENTS.md` (the plate spec and component list);
  - `DECISIONS.md` (every design decision, with reasons);
  - pass 7d and 7e change logs.
- `references/` holds:
  - the approved Today look (`today-neu-v7.html`);
  - the approved scroll (`clay-rise-tilt-v8.html`, plus `clay-rise-NOTE.md` with the model and tuning);
  - `OPEN.md` with the open items.

## The look in one paragraph
- **Neumorphic Ink.** The surface is #1D2633. Elevation is a single `--h` value: well −1, page 0, plate 1, key 1.5, dock 2.3, + key 3.3.
- **Light.** It is set by `--lx`/`--ly`.
- **Colour.** Each routine has its own hue (saffron, lagoon, moss, jade, iris, rose, night, ember), shown as a lit dot.
- **Today.** The hero is a dial the full width of the screen.
- **Plates.** Every card is one plate: 26 px corners, 20/18 insets, title 20/600, sub 15, 12 px gaps, never a plate inside a plate.
- **Scroll.** It is the clay rise. Rows are printed flat at the clip edge. Each point rises gradually to its height, with no tilt and no overshoot. There is a gentle shadow-only pop when a row is fully out. There is no moat and no drawn status bar.
- **Page change.** The old page sinks and the new page's forms extrude, staggered.

## Rules from Mark (do not break)
- Mark has ADHD.
- No streaks, no punishing lapses, no chores or toggles that create work, no 1–10 ratings.
- "Missing" is not "zero".
- Nothing that looks AI-made.
- No brown.
- Never copy a single app.
- Priority: routines, then enjoyable gamification (still unsolved), then beautiful progress, then lifestyle links.

## Open items
See `references/OPEN.md`.
