# Pass 7e (last pass): review r28 items, then the r28 look slice

Base: 7d bundle 71190659c4e6b82f214d7c5b03586446 (src cf6f4510f51ff71be33c38dd6c4af444, regenerated exactly from inj7d.py).
Output, all in this folder (the project folder is at its file limit):

- meridian-src-p7e.html  md5 837fe979d285f8a381ab054b79fb64e0  (2,119,597 bytes)
- meridian-p7e.html      md5 2194c7db654b4161f1c31f3291d58b59  (2,295,881 bytes; blocks KB 457 / 451 / 130 / 56 / 295)
- src/ (r29.py holds every 7e change as text replacements over the 7d src; inj7e.py and rebuild7e.sh build it; the test scripts)
- DECISIONS-7e.md (also appended to base7/DECISIONS.md)
- shots/ (r28 items, before and after), shots2/ (look slice, before and after), chk/ (side-by-side sheets, test output)

## r28 items (first message)
B1 Weeks view after Water day->week; B2 paused Meditation reads Paused, not "Not yet"; P1 an id sheet for a missing routine
says so and changes nothing; P2 the toast says "starting today" only for a target made today; P3 the breakdown counts
no-target periods and drops zero-length ones; P4 the year's label follows the filter; P5 Routines hero names measured, not cut at 86 px.

## Look slice
1. Page switch. Only the first 8 forms in view rise, and only the lead one animates --g; the rest rise by opacity and 8 px
   translate (compositor). The page under sinks by opacity only. No --g on the page.
2. Time chart. Key under the year ("Share of routines done, per week"; filtered: "Share of days with X done, per week"); the
   month read is named in full (Oct). Week 44: day names only; the count is in each day's spoken label.
3. Plates. Every .card is a plate (26 px, 20/18 insets, 17 px readings). A sheet's list is a stack of plates, one per row, list
   type 17/600 + 15, with the standard press (Log Records, Something happened/Hold/Something with a date, sugmore, all sheet lists).
   Drink From and To are a plate each. "Patterns involving sleep" sits under its card. Medication .kvs readings at 17.
4. Routines index at large text: the state wraps under the name when both don't fit; names are never cut.
Cheap: paused routines count after active ones when lights are given (Reading/Meditation no longer share 232); dock, toasts,
live bar, sheet bodies and v3 page ends add env(safe-area-inset-bottom); day entry dots and the period chart beads take the
routine's light; loom date and "today" labels stay inside the 16 px gutter.

## Results
- err: no console or page errors, both files, app mounts.
- ctx smoke 0 errors, sheet smoke 39 sheets / 20 pressed / 0 errors, route smoke 0 errors (src and bundle).
- cadence matrix 24 cases, 0 failing at 390 and 430.
- chk7e (r28 items): 0 failing at 390 and 430.
- pgfast (stress, Reduce Motion): 0 failing at 390 and 430, also at CPU x6.
- topedge: 28 checked, 0 bad at 390 and 430.
- vis: 390 675 checked, 3 without a visible press; 430 711 checked, 2. The residue is the same as 7c's: the dial's drag ring,
  the already-on segment, one feel-page timeline row at max 25 (7c listed 6 at 390).
- f1 (real touch swipes): errs [] at 390 and 430; 1 stuck plate out of 61 on the Log sheet at 430 only, 0 at 390.

## Frame rate (pgfps: rAF over the 700 ms after each change, DPR 3, headless; 7c and 7e measured in the same run)
| | 7c tab | 7e tab | 7c push | 7e push | 7c back | 7e back |
|---|---|---|---|---|---|---|
| 390 | 46 (p90 17) | 40 (p90 17-100) | 12 | 16 | 12 | 15 |
| 430 | 39 | 38 | 1 | 1 | 7 | 1 |
| 390 CPU x6 | 1 | 18 (p90 17-33) | 1 | 2 | 1 | 1 |
| 430 CPU x6 | 1 | 15 | 1 | 1 | 2 | 1 |
Before the fix 7e tab was 18 at 390 (p90 50-367 ms), push 3, back 2. Run-to-run noise here is about +/-8 fps
(7c tab 43-46 across runs, 7e 35-42). With animations stubbed out, 7c and 7e both reach 42-47, so what is left is the React render.
Push/back are bound by one 550-650 ms render frame in both builds. Both run slower here than on the reviewer's device.

## Notes
- The p7d files and pass7d-* files had vanished from the mount; the 7d src was regenerated from inj7d.py (md5 identical).
- /x: a stray empty root-owned file dated 24 Oct 11:37. Not removed.
- Nothing deployed.
