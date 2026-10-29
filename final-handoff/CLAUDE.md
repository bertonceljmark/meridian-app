# Meridian (native) · CLAUDE.md

Meridian is a gamified personal well-being and routine app for iPhone, Apple Watch and widgets, built in SwiftUI. Owner: Mark (adult with ADHD, perfectionist, technically sophisticated). He wants to "genuinely enjoy taking care of my health because Meridian makes healthy behavior satisfying, progress meaningful, results fascinating, and the entire experience extraordinarily beautiful."

The full handoff lives in `handoff/` (from the package): START-HERE, 01-GOAL … 06-PROCESS, evidence, reference, ledgers, prototypes. Read `handoff/01-GOAL.md` and `docs/OWNER-LOG.md` at the start of every session.

## Priorities (in order)
1. Personally meaningful routines, any routine, any measure, any cadence.
2. Genuinely enjoyable: satisfying interactions, real sustainable gamification (unsolved).
3. Progress, history and results beautiful and fascinating.
4. Honest optional analytics. 5. Lifestyle links (Health, location, calendar).

## Never
- Streaks, punishment, backlog, the word "kept". Unrecorded is never missed or zero.
- 1–10 ratings, mandatory input, chores, settings that don't earn their place.
- Rewarding consumption (caffeine, alcohol, medication, more water/exercise).
- Invented scores, fabricated correlations, causal claims. "We don't know" is fine.
- Logic, copy, icons or visuals keyed to a routine's name or the sample data.
- LLM required for logging, navigation or stats.
- UI that looks AI-generated, copied from one app, plain, or a decorated checklist.
- Showing Mark anything that hasn't passed the gates in `handoff/06-PROCESS.md`.

## Approved look (can change only with evidence and Mark's yes)
Neumorphic clay on Ink `#1D2633`, everything pulled from one surface; elevation well −1 / page 0 / plate 1 / key 1.5 / dock 2.3 / + key 3.3; plate = 26 pt corners, 20/18 insets, one per item, never nested; colour per routine as a lit dot; screen-width dial hero on Today; raised dock; clay-rise scroll (no moat, no fake status bar); staggered extrude page change; touched element morphs into its sheet; springs 0.5/0.8; haptic on every commit; glass sheets via `.glassEffect`. Details: `handoff/reference/COMPONENTS.md`, `clay-rise-NOTE.md`, `MORPH-HANDOFF-native.md`.

## Working rules
- Log every message from Mark verbatim in `docs/OWNER-LOG.md` immediately. Newest owner words win.
- Record decisions in `docs/DECISIONS.md` with evidence; keep `docs/TRACE.md` (requirements → status) current; never drop a requirement silently.
- Before showing anything: build, tests, simulator screenshots (SE, Pro, Pro Max; largest Dynamic Type; Reduce Motion), recordings of motion, Instruments at 120 Hz, the genericity fixture, then an independent reviewer subagent that didn't write the code. Save evidence under `evidence/`.
- If Mark catches a defect, first add the check that would have caught it.
- Messages to Mark: short, one thing to look at, at most one question. Feel questions get a tiny sketch, not a rebuild. Restate described feels and get a yes before building.
- Decide yourself unless it changes the goal; then ask once with a recommendation.
