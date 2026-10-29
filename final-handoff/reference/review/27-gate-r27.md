# Round 27: 7c (ddd94c9b)

## Status
Fixed:
- #1 bead chooser (popover, 60% cap, inner scroll, keyboard, hue fan)
- #2 press: every element passes except the accepted exceptions
- #3 spacing: Log and Sugmore on 16, `var(--sp)` used 1,201 times
- #4 colour per routine

No regressions against 7b on any check:
- 94 breakdowns checked, 0 "kept"
- 0 misroutes
- 0 errors
- AA contrast at rest
- DPR3

## BLOCKING: #5 cadence, partly fixed (3 defects)
Finished periods, rule stamping, migration, Undo and the toasts are all right. The defects:
- a. **Time › month Totals re-judge the past under the new type** (`monthTotal` uses `it.cad`). Water shows "43360 times · At its aim 4 of 4 weeks", and Reading shows "469 of 30 so far". The wrong units date back to 6i.
- b. **The first month after a type change does not read as partial.** It says "October … still open" where it should give 27–31 Oct. The hero says "None logged in Oct" although there are 17 entries, which is false.
- c. **The Growth note labels mixed periods with the new type** (`per(it)`). It reads "39 of its 40 finished months" when only 9 months have finished. This is new in 7c.

## POLISH
- The Time target has no unit: "580 ml of 2000 so far" (`aimTxt`).
- Chooser rows show the hour bucket instead of the time.
- The press well has a 0 px left inset.
- Tab focus shifts the strip 4 px.
- Stuck plates in the Log sheet at 430 after a sweep: 7 of 38.
- Off-scale 2 px values (451) and a few 28/48/64+ values remain.
- Settled has 21 px above it, other headers about 28.

Evidence: r27/g/.
