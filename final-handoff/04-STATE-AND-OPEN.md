# 04 · Where things stand on 29 Oct, and what is open

## 1. The last prototype: 7e (`prototypes/next-7e/`, live at https://bertonceljmark.github.io/meridian-app/next/)

- One React-in-HTML file (React 18.3.1 from cdnjs, needs network). Source and build scripts in `prototypes/source-7e/`. Storage keys `meridian.next.*`.
- Screens: `screenshots/next-01…07` at 390 px. Approved references: `screenshots/approved-today-neu-v7.png`, `screenshots/approved-clay-rise-tilt.png`.
- **7e was never checked by the independent reviewer.** Its six r28 blockers were addressed but not re-verified: Weeks view Water totals, paused shown as "Not yet", page-switch smoothness, Time chart key, cards not on the plate, 22 px name clipping.
- Known rough edges: page change takes 550–650 ms of rendering on the web; 2–3 controls with no visible press; a plate stuck in the Log sheet at 430 px; polish list in `reference/review/27-gate-r27.md`.

## 2. Mark's verdict

> "I am not 100% happy with the final result, everything needs to be validated again - from UI and flows to logic itself. I am open to everything changing if backed by evidence."

His last concrete complaints on /next/ (25 Oct): Time chart looked bad, cards looked bad, page switching bad, moat not working, status bar drawn. Earlier and recurring: "ai slop", "plain", "boring checklist tracker", "hard to see what is what", toggles that make it a chore. Treat these as the failure modes to test against, every round.

What he has positively approved (strongest evidence of taste):
1. neu v7 Today on Ink with screen-width dial and colour per routine;
2. clay-rise scroll ("Yes perfect");
3. the whole-product prototype of 18 Oct as structure ("My favourite version is still the first ever full app prototype");
4. depth, light, material, heavy physical feedback (taste test).

## 3. Open problems (nobody has solved these)

| Problem | What exists | What's needed |
|---|---|---|
| Gamification | Long rejected list, research | Evidence-backed candidates, tiny sketches on device, Mark picks |
| Smart suggestions | Requirement + rules, no build | Native design using real context APIs, privacy, push |
| Glass on device | Web liquidGL fallback, unconfirmed | Real `.glassEffect` sheet on his iPhone, his verdict |
| Whether the IA is right | 7e IA (Today/Time/Routines/You) | Re-validate flows with real use (05-KEEP-OR-DROP §3) |
| Logic correctness | r27/r28 cadence bugs | Unit-tested period engine |
| Performance feel | Web was slow | 120 Hz on device, Instruments |

## 4. What "done" means

A native app on Mark's iPhone (and Watch, widgets) that:
- meets every layer-A requirement in the contract and every ledger item that still holds (or records why it was dropped);
- passes the process gates in 06-PROCESS with evidence;
- that Mark, using it for real for days, calls beautiful and enjoys opening. The last is the real bar; everything else is how you avoid wasting his time getting there.
