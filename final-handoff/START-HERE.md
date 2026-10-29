# Meridian: final handoff package (29 Oct 2026)

From 11 days of design work with Mark in a cloud project to the native SwiftUI build on his Mac.

## Read in this order

1. `01-GOAL.md`: what Mark wants, in his words. Read twice.
2. `02-HISTORY.md`: what was tried, approved and rejected, and why, plus lessons about working with him.
3. `03-SPEC.md`: product logic, mapped to the authoritative sources.
4. `04-STATE-AND-OPEN.md`: the last prototype, his verdict, open problems.
5. `05-KEEP-OR-DROP.md`: how to audit your old work and context.
6. `06-PROCESS.md`: phases, gates, self-verification, how to talk to Mark.
7. `CLAUDE.md`: copy into the native repo root (merge with any existing one per 05).

## Folders

| Folder | What |
|---|---|
| `evidence/` | Mark's messages verbatim. `-1-log` = 18–23 Oct, `-2-after-log` = 21–29 Oct (text after "\|" in headers is context, not his words). The ground truth. |
| `reference/` | Contract v1.1.1, component spec, decisions, motion, clay-rise and glass notes, research, review findings. |
| `ledgers/` | 625 feature requirements and 494 research findings (JSON + summaries), access map, buildability. |
| `prototypes/` | Web prototypes. Open `index.html` in a browser at iPhone width (390×844). `next-7e` = last whole app (needs network for React). `today-neu-v7` = approved Today look. `tilt-clay-rise` = approved scroll. `morph`, `liquid-glass`, `glass-studies`, `today-arc` = studies. `source-7e` = build sources and CSS tokens. |
| `screenshots/` | 7e screens and the two approved references. |

Running prototypes locally: `cd prototypes && python3 -m http.server 8000`, then open `http://localhost:8000/next-7e/` in Safari with Responsive Design Mode on an iPhone size, or on the phone over the LAN. Live copies: https://bertonceljmark.github.io/meridian-app/ (`/next/`, `/today/neu/v7/`, `/tilt/`, `/morph/`, `/liquid-glass/`).
