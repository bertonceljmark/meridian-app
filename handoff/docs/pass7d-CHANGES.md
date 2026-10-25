# Pass 7d: the r27 gate on 7c (cadence, BLOCKING) and Mark's calls on the 7c preview

**Where the files are:** the mount refuses new directories (mkdir gives an Input/output error), so pass7d's files are flat in base7: `pass7d-CHANGES.md`, `pass7d-COMPONENTS.md`, `pass7d-src.tar` (the src folder), and every shot as `pass3/p7d-<folder>-<name>.png`. For example, `after/cards/pair-390-today-row.png` is `pass3/p7d-after-cards-pair-390-today-row.png`. The whole folder is also in `pass7d.tar`, laid out as described here.

**Base and output:**
- Base: `meridian-src-p6i.html`, through the 7c chain plus `r27.py` (cadence, applied after `r26.late`) and `r28.py` (Mark's calls, applied last).
- Output: `meridian-src-p7d.html` (md5 cf6f4510f51ff71be33c38dd6c4af444), built as `meridian-p7d.html` (md5 71190659c4e6b82f214d7c5b03586446).
- Blocks: 457, 448, 130, 55 and 295 KB, all under 500. There is no object rest destructuring after block 1.
- Nothing was deployed. `meridian-src.html`, `meridian.html`, `pwa/` and `lab-render/` were not touched.

**Build:** run `pass7d/src/rebuild7d.sh` (its paths point at the scratch copy; change `S` to run it elsewhere).
- `inj7d.py` reads 6i and applies, in order: `r24.apply`, `r25.apply`; the 7a palette, JSX hooks, CSS (now with `css/plate.css` and `css/plate-shadow.css`) and `neu.jsx`; `r25.late`; `r26.late`; `r27.late`; then `r28.late` (status bar, Time chart, page changes, structure).
- The script builds the bundle in the same run, checks by content that the bundle came from this src, checks block sizes and rest destructuring, and runs err.js, the context, sheet and route smokes on both files, and the cadence matrix on the bundle at 390 and 430.

**Results:** on the final build (both files): err.js clean; context smoke 19 ok with 0 errors; sheet smoke 39 sheets and 20 presses with 0 errors; route smoke 0 errors; the cadence matrix 24 of 24 at 390 and at 430. The other checks are under "Checks" below.

## BLOCKING #5: cadence

### a. Time > month Totals judge each period by its own rule and keep the unit
- **Fix (`r27.py`, `monthTotal`):** the month is read period by period. `periodOf` walks from six days before the month; a period belongs to the month its fourth day (or its last, if shorter) falls in. Each period is judged with `E.state` by the rule version and type in force on it (`cadOn`).
- **The unit is the routine's, whatever the type:** quantity as an amount (43.36 L), duration as time (7 h 49 min), reps as "done", count and confirmation as "times".
- **The judgement counts by type:** "At its aim on 10 of 26 days", "in 4 of 5 weeks", or "periods" when the month's finished periods mix types. A single finished month says "At its aim" or "v of aim". The open period says "580 ml of 2 L so far" (the aim with its unit).
- A month that holds a change of type draws a tick a day, each coloured by the period it belongs to.
- **Shots:** `after/cad-390-water-day-to-week-month-totals.png` ("43.36 L, at its aim on 10 of 26 days"), `after/cad-390-guitar-week-to-month-month-totals.png`, `after/cad-390-reading-week-to-month-month-totals.png`.

### b. The first period after a change reads as cut short; the hero tells the truth
- The hero and every "where it stands" line say "since today" or "since 27 Oct" for a period cut short by a change of type, never "in Oct" or "this week". A quantity or reps routine names its period too ("580 ml of 2 L since 27 Oct", "None logged since 27 Oct").
- The item page names a cut-short month by its dates ("27–31 Oct"), labels it "27–", and adds: "A short first month, 27–31 Oct: the month started counting when you changed how often, so it runs from then. Earlier periods keep the rule and the period they had."
- A daily routine's This week counts only days that are day periods.
- **Shots:** `after/cad-390-guitar-week-to-month-item.png`, `after/cad-390-reading-week-to-month-item.png`.

### c. The Growth note counts each period by its own type
- "Logged at least once in N of its M finished weeks / months / days", by the periods' own types, or "periods" when they mix; it shows only when some finished periods are not days.
- **Shots:** `after/cad-390-*-growth.png`.

### The cadence matrix
- `src/cadm.js`: four units (Meals count, Water volume, Reading duration, Guitar sessions) times the six changes among day, week and month. Each routine is given type X from its start, then changed to Y today through How often.
- It asserts, against ground truth from the db: the toast; the rules (the new one from today, the old one kept); that every finished October period keeps type X; the Totals unit and judgement (count and word); the cut-short first period and its name; the hero ("since", never "in Oct" or "this week|month"); the short-first note; the Growth note's word; the summary; no page errors.
- **Result:** 24 cases, 0 failing, at 390 and at 430 (`src/cadm.js`, run by `rebuild7d.sh` on the bundle).

## Polish (r27)
- **Time target unit:** "580 ml of 2 L so far" (`aimTxt` with the unit and the period's own rule).
- **The dial's chooser** gives the logged times (07:55, 08:32), not the hour bucket; two times, then "N more". Shot: `after/polish-chooser-times-390.png`.
- **Press well inset:** a v3 row's press well was drawn flush with its text (0 px). In 7d the rows are plates and the plate itself sinks, so the well is gone (see the plate below). Shots: `after/polish-press-well-*.png` (the r27 version, before the plates).
- **Tab focus in the strip:** focus aligns the focused card like a swipe and never scrolls the strip on y (it moved 4 px).
- **The Log sheet at 430, plates stuck after a sweep:** the clay rise measured in screen pixels while the page under a sheet is scaled to .955, so its plates read as moved. It now measures in each scroll area's own pixels: 1 of 38 stuck (a 2-character rounding difference in one gradient string), against 7 in 7c and 2 in 7b.
- **Stray spacing:** the 21 remaining 28 px paddings, margins and gaps go to 32 (`--sp-6`); 48, 56 and 64 stay as deliberate large insets; min-heights and 2 px hairlines are untouched.
- **Settled gap:** a section that ends on a raised plate is followed by 32 above the next header (the plate's drop reaches 11 px below its box), so Settled's text sits 23 px from the shadow, near the others.

## Mark on the 7c preview

### 1. No moat
- CLAY's `moat` is off and no `.mt` layer is made; walls, depth 1.4, the per-point rise and the gentle pop stay. The strip's bottom padding for it goes from 24 to 16 px (the card's own drop and the focus ring).

### 2. No drawn status bar
- The drawn status bar (time, island, signal, battery) and the drawn home bar are gone from every screen, sheet and state.
- Every top offset is `calc(var(--sb) + room)`, with `--sb: env(safe-area-inset-top, 0px)`: the navbar and its title, the root bars, Today's head, the v3 heads and spacer, the deep heads (`.hero`, `.plainhead`, day, month and pattern pages), a full sheet's top and every sheet's maximum height, the top toast, the pull indicator, onboarding and the week close.
- A band of the surface's colour (`.n7sb`, `--sb` tall) sits under the real status bar; its bottom is the clay rise's top clip edge.
- The page head carries the home-screen PWA meta (`apple-mobile-web-app-capable`, `black-translucent`, theme colour); viewport-fit=cover was already set.
- The v3 scenario's "Different data" pill moves into Today's header.
- **Check (`src/topedge.js`):** with `--sb` at 0 (a browser tab) and 59 (a home-screen PWA under a Dynamic Island), seven pages each scrolled to 300 and 900: the rise's top edge equals the visible top (the band's bottom, or a solid bar's) and the height there is 0. Result: 28 checked at 390 and 28 at 430, 0 bad. (The first full run found 2 at 300 px scrolls, where the v3 bar was still growing in. The rise now measures again when a bar finishes its transition.)
- **Shots:** `after/statusbar/sb59-390-*.png` (Today, scrolled, Time, Routines scrolled, item and item scrolled, a month, Privacy, the Log and Create sheets, a workout), `after/statusbar/sb0-390-*.png`.

### 3. Page changes: sink, then extrude, staggered
- One inherited number, `--g` (0 to 1), multiplies every form's height in the shared recipe and shows the walls' layers, so a page flattens to printed and rises again with the same system as the clay rise: shadows, walls and wells grow, nothing moves, and no text is transformed.
- **Tabs:** the page sinks in place (160 ms, ease-in, its content fading), the tab changes, and the new page's forms extrude in reading order, 35 ms apart (300 ms at most), each over 260 ms. A second tap during the sink only changes where it lands; tapping the current tab cancels it. Each tab gets its scroll back, by page.
- **Push and back:** the route changes at once. The page under a push sinks; the new page's printed layer shows at 130 ms and its forms extrude from 170 ms. Back is the mirror: the leaving page sinks on top, the page under it shows at 130 ms and extrudes. No slide, zoom or morph (the row-to-page morph is no longer used).
- Only items in view animate; only custom properties animate (`--g`, opacity); a new change cancels the last one's runs.
- **Reduce Motion:** a 120 ms crossfade, nothing extrudes.
- **Shots:** `after/motion/strip-tab-390.png`, `strip-push-390.png`, `strip-back-390.png` (frames at 0, 60, 120, 200, 300 and 450 ms of animation time, filmed at a tenth of the speed), and each frame on its own; the same at 430 (`strip-*-430.png`). Each frame is labelled with its target time and the time it was actually filmed at (filming jitters by up to ~80 ms of animation time at 430).

### 4. The plate, one spec for every card
- **The spec** (COMPONENTS.md, "The plate"): v7's raised recipe at `--e: 1` (broad soft drop, cool top-left rim), 26 px corners, 20 px insets (18 top and bottom), title 20/600, sub 15 at 1.35, 12 px between plates; settings and timeline rows use the same plate with 17/600 titles.
- **No plate holds a plate.** Later is an engraved group label and spacing over one plate per routine. The v3 plateaus become plain stacks of plates: the Routines index (one column of row plates, see 6), This week, report figures, Months, a month's Totals, patterns, records, settings lists, entries and timelines.
- **The strip's panels** are raised plates, like every other item.
- **A routine's colour** is a lit dot before its name, v7's accent; the coloured bars and the glyph before names go.
- **Keys** are v7 keys: 48 px, raised 1.5, 16 px corners or round; primary sheet buttons 56. Amount presets (Today, the item page, the Log sheet's amounts and durations) and the time offsets sit on one line that scrolls sideways.
- **Density:** with 60 routines configured and a 44-character name, the Routines index stays readable (`after/timechart/routines-*-s60-*.png`).
- **Shots:** `after/cards/pair-390-*.png`, before (7c) and after side by side, one per card type: Today's row, amounts, first step, strip, Later, moment; the Routines rows; Time's chart, This week, reports, Months; a month's Totals; You's patterns and records; settings rows; the item's keys and entries; the day's timeline; the Log sheet's amounts and time keys; the Export card. Each side is also on its own (`card-390-*-before.png`, `-after.png`).

### 5. The Time chart
- A carved well with a mark a week (53), each as tall as that week's share of routines with something done, on an engraved zero line. The selected month is in one strong accent (Ink blue, or the routine's hue when filtered); the other months in the same hue, pale; a week mostly set aside in its context's colour. No noise texture, no haze, no WebGL.
- Missing is not zero: a week with records and nothing done is a 2 px tick; a week with no records, a small ring; before the first record nothing, named "Before Meridian".
- Month letters, the set-aside bands with their names (Sick, Montréal) and "today" are printed under the well; today is marked once, a small sun on the zero line.
- Every month is a key over the well: a press darkens its column, a first press reads that month (the reading under the chart redraws in place), a second opens it, a drag reads month by month (the old drag stopped after one month, because each change redrew the page under the finger). The filter still recolours it to one routine.
- **Shots:** `after/timechart/time-chart-{390,430}-{base,one-routine,s60,none}-{before,after}.png`: 20 routines with a year of records (base), one routine (filtered to Guitar), 60 configured (s60), and none (first run). The data is the year 2026; 2025 and 2024 are the Watch's earlier years, which the chart does not draw, so "2 years of history" reads as a full year here with no "Before Meridian" stretch.

### 6. Structure (Mark: "Just please great looking clear structure")
- **The bar for every screen:** one hero, sections with clear labels, one raised plate per item in one order (dot and name, then its state), fewer parts per plate, big type, room. Dense screens are simplified rather than shrunk.
- **Section labels** are 22/600 in full cream (groups inside an index 19/600), 16 px above their first plate; they were 15 px at 70 %.
- **Routines** is one column of row plates instead of the two-column grid (no holes, one reading order).
- **Months** show the month and one reading; the unlabelled distance on every plate is gone.
- **The Time reading** is one stack: month, figure, one sentence.
- **Reports:** an odd last plate takes the full row.
- **You:** the first section is "Patterns" (hints, not proof); a switch that is on is Ink blue, not the dimmed orange that read as brown.
- **A month's Totals** name the routine in cream, its colour in the dot.
- **An item's keys** lead with their unit; the item and month heads sit 12 px clear of the bar.
- **Shots:** `after/structure/full-{390,430}-<screen>-{before,after}.png`, each screen whole at a tall viewport, 7c before and 7d after.

**Structure, screen by screen** (hero / sections / item plate):
- **Today:** the dial / the strip, Now, Later (This evening, Any time), If you have a moment, Settled / one plate per routine: dot, name, state, its keys.
- **Time:** the year chart and its month reading / This week, Reports and patterns, Months, The year so far / a routine's plate (dot, name, state, its bar); a report (figure, name, one line); a month (name, one reading).
- **Routines:** the four-week dot field and its sentence / Find, then one group per cadence (Every day, Every week, Every month, On their own interval, No target), Paused, Observations, Measures, Intentions, Retired / one row plate: dot, name, state on the right.
- **You:** the feelings map and How do you feel / Patterns, Records, Meridian (settings) / a pattern (kind, name, one sentence, its strip on the first); a record (name, state, its two weeks of dots); a setting (name, value, switch or chevron).
- **An item page:** name, state and amount keys over its days / Growth, In Time, Recent entries, Settings / an entry (time, amount, chevron); a setting (name, value, chevron).
- **A month:** the month, its sentence and its calendar / Highlights, Totals / one total per routine: dot, name, amount with its unit, its ticks or bars, one judgement.
- **A day:** the date and its sentence / Entries, Doses, Something happened / an entry (time, what, Remove).
- **A week:** the week's day columns / Every day, This week's aims, No target, Sleep, Activity / a routine (dot, name, state, its bar).
- **Settings pages** (Privacy and the rest): the title and one sentence / one group each / a setting plate.
- **Sheets:** the question as the title / its keys on one line, then its fields / one primary key at the foot.

## Checks
All checks ran on the 7d bundle at 390 and 430. The final build adds one CSS rule (the stepper's press) after this run; it was re-checked on its own (vis on You > Contexts: 35 checked, 0 without a press) along with the full smokes and the matrix.
- **Presses (`src/vis.js`):** 677 tappables checked at 390 and 713 at 430. 2 have no visible press at each width, both known from 7c (the dial's disc, which is dragged rather than pressed, and a selected chip). The first full run found 76 v3 plates with no visible press (the drop went down but the drawn walls stayed), so a plate now presses exactly like Today's row.
- **Hit testing (`src/hit.js`):** 20 targets have a reach under 44. Ten are the Time chart's month keys, about 27 px wide; they tile the well with no gaps, a wrong tap only selects, and this is logged in DECISIONS. Seven are inline text links (`.b`) and the sheet grabber, all known from 7c. Two are Feel chips partly covered by the sheet's foot at its first scroll position; they come clear when the sheet scrolls. Misroutes: 3 at 390 and 5 at 430, all fixed chrome (the tab bar or the Log button) over scrolled content, plus Today's key inside its row, as in 7c (7c had 5). Later's names are now at least 44 px tall (they were 40).
- **Edge cases (`src/ecase.js`):** no horizontal overflow and no page errors in any case or route at either width (long German, 22 px type, Reduce Motion and the rest).
- **Contrast (`rv/con.js`):** 2494 runs at 390 and 2675 at 430, 15 fails at each, all disabled buttons (exempt).
- **Layout (`rv/lay.js`):** no new findings. The 15/16 gutter entries are Today's visually hidden overlay labels, as in 7c.
- **The strip (`rv/t7.js`, `rv/t8.js`):** a swipe never scrolls the strip on y (sT 0); the page keeps its place through the strip at both widths.
- **Touch and stuck plates (`rv/f1.js`):** real CDP swipes on every scrolling route and sheet, with 0 page errors. Stuck plates: 0 of 947 at 390 and 1 of 875 at 430, the known 2-character rounding in the Log sheet. The first full run had 7 of 42 on that sheet because the page under it, which scales as the sheet opens, was measured mid-transform. The rise now measures again when an ancestor of an area finishes a transform transition, and when a sheet closes.
- **Page changes under stress (`src/pgfast.js`):** fast taps land on the last tab with nothing left flat; tapping back to the current tab mid-sink cancels the change; each tab keeps its scroll; push then back at once leaves no leaving page; Reduce Motion extrudes nothing. 0 failing at 390 and 430, both at normal speed and with the CPU slowed 6x. The first full run found that a slowed CPU could leave a page flat and invisible after three fast taps. The tab handler now goes by the tab actually in view (recorded on commit) and keeps one change at a time, including the gap between the sink's end and the new page's first frame.
- **Tour (`src/tour.js`):** every route and sheet at 390 and 430, 0 errors (`after/390`, `after/430`; 7c in `before/`).
- **Status bar (`src/sbshot.js`):** no drawn status bar or island on any screen; the band is 59 px in the PWA case and 0 in a browser tab.

**Fixed after the first full run, besides the above:**
- Every block of a scroll area is watched for size changes, not only the first (Today's rows moved below the head without being measured).
- The structure pass (section 6) came after that run; all the checks above were run again on it.

