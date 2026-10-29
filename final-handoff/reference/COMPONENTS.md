# Pass 7d: component inventory (Ink, neumorphic)

This file replaces 7c's. What 7d changed: **the plate** (one spec for every card, row and tile, below), no plate inside a plate, the routine's dot instead of its bar, v7 keys and one-line amount rows, no moat, no drawn status bar (the top of every screen is the real safe area), page changes that sink and extrude, and the Time chart as a carved well.

## The plate: the single spec for every card, row and tile (new in 7d)
Every item the app shows on a surface, on Today, Time, Routines, the item pages, You and the sheets, is one raised plate. Nothing else is a card.

| Part | Value | Token |
|---|---|---|
| Form | raised, `--e: 1`: v7's recipe, a broad soft drop (blur up to 14.4 px) and a cool top-left rim and highlight, from `--nElev` and `--nTone` | `css/recipe-*.css` |
| Corners | 26 px | `--pR` |
| Insets | 20 px left and right, 18 px top and bottom (Today's rows 14 px on the key side) | `--pX`, `--pY` |
| Between plates | 12 px | `--pGap` |
| Title | 20 px, weight 600, line 1.2, cream (Today's lead row 24) | `--pT` |
| Sub-line and body | 15 px, weight 400, line 1.35, `--t2` | `--pS` |
| Meta (the smallest text on a plate) | 13 px | `--pM` |
| Figures | display type, 24 to 56 px, light weight | |
| A routine's colour | an 8 px dot before its name, lit with its own glow (v7's accent); no bar down the side, no glyph before the name | `--hf` / `--rc` |
| Press | Today's row press everywhere: `--e: -.4`, the face takes the pressed inset (`inset 9px 9px 20px` dark, `inset -6px -6px 14px` light) and the walls and drop go to .3; 80 ms down, 300 ms back on `--back` | |

- **List size.** Settings rows (`.set .li`) and timeline rows (`.tl .li`) use the same plate with list type: title 17/600, sub 15, at least 64 px tall. It is the spec's one size step.
- **No plate holds a plate.** A group is spacing and an engraved label (13 px, weight 600, `--t3`, `--deb`), the way Today's NOW and Later's "This evening" read. Later is no longer a well of rows; the v3 plateaus (the Routines index, This week, Months, Totals, patterns, records, settings lists, timelines, ledgers) are plain stacks of plates. The item's details (`.kvs`) are one plate with grooved lines inside it: one item, not a plate of plates.
- **Where each plate is:**
  - Today: rows (`.zrow`), the strip's panels (`.zpanel`, now raised), moments (`.zsug`), Later's routines (`.ztok`), the date line.
  - Routines: the index (`.idx .tk`), one column of row plates: the name on the left (wrapping, up to three lines), its state on the right (up to 18 characters a line).
  - Time: This week (`.staff .sf`), the report figures (`.figs .fg`; an odd last plate takes the full row), Months (`.toc .tc`: the month and one reading, no distance), a month's Totals (`.combs .cb`), ledgers (`.ledger .ln`).
  - You: patterns (`.pats .pt`), records (`.recs .rec`), settings rows (`.set .li`).
  - Item and day pages: entries and timelines (`.tl .li`), details (`.kvs`).
  - Sheets: cards (`.card`).
- **Keys** are v7 keys: 48 px (`--kH`), raised 1.5, 16 px corners (`--kR`) or round, labels 16/600. Primary sheet buttons are 56. Chips are at least 44 tall at 15 px.
- **Amounts on one line.** Today's familiar amounts, the item page's log keys (`.logrow`), the Log sheet's amounts and durations (`.optgrid`) and its time offsets (`[data-timechips]`) sit on one line that scrolls sideways when it doesn't fit. Choice sets (how often, contexts, words) still wrap.
- **Density.** With 60 routines configured (`s60`) and a 44-character name, the Routines index stays one column of row plates, long names wrapping (pass7d/after/timechart/routines-*-s60-*).


## How elevation works
- **One number, `--e`, per element.** Above 0 a form is raised, below 0 it is carved, and 0 is flat on the surface.
- The shared recipe (`css/recipe-light.css`, `css/recipe-shadow.css`) turns `--e` into its shadows (`--nElev`) and its face tone (`--nTone`). The light comes from `--lx`/`--ly`, top left.
- **Correction to 7a's and 7b's notes:** 7a said "there is no blur", and 7b said the keys and plates "use hard shadows only". Neither is accurate. The recipe's `--nElev` is built from blurred layers: the raised drop blurs up to 14.4 px and the carved inset up to 12.6 px, per unit of `--e`. Two further soft layers are part of the look:
  - the cast shadow (`.shc`, 4 px).

  The moat (the mantle around a rising plate) is gone in 7d.

  There is no glass and no backdrop blur.
- **Pressing lowers `--e`.**
  - A raised key drops to between -.36 and -.64.
  - A key that is already "on" (in its well) drops one step deeper, to between -.64 and -.95, and also gives (scale .94), because its own `transform: none` had hidden the press.
  - Switches, chips, icon keys and primary keys give to .9–.95. Segment and "on" buttons take a .3 shade.
- **The sink (new in 7c).** Every row, day, link and summary that is not a key presses into the surface: `--e -.5` through the recipe (its carved shadow) plus a .16 shade, 80 ms down. This covers the light DOM and the v3 shadow roots (`li`, `tk`, `cb`, `tc`, `cd`, `rm`, `sf`, `ln`, `pt`, `ob`, `summary`). The Routines index draws its well on a `::before` that reaches 10 px past each word. The grabber's pill widens to 96 and lightens.
- **The clay plates** (Today's rows and suggestions, v3 lists) are drawn by a plate layer (`.n7c`) and also answer a press. While `button.zopen` is held:
  - the face takes today-neu v7's pressed inset (`inset 9px 9px 20px` dark, `inset -6px -6px 14px` light);
  - the 7 walls and the drop sink to .3;
  - `--e` goes to -.4.

  The response takes 80 ms on the way down and 300 ms on the way back, on the `--back` curve.
- **The current tab** presses one step deeper than "on" (-1.15), and its glyph scales to .88.
- **The clay rise** (`neu.jsx`, CLAY):
  - A plate rises out of the surface as it enters the 80 px band at either edge.
  - Its content fades with it, but never below **.92** (`TA0`), so text in the band still clears 4.5:1 at rest. The faintest text on Ink, `--t3` at .62, measures 5.3:1 on the surface at .92. On plate faces, `con.js` finds no enabled run under 4.5:1 at rest.

| Elevation `--e` | Used for |
|---|---|
| 5.7 | toast |
| 3.3 | log button (+), with a carved collar at -.55 (the collar takes no taps) |
| 3 | live bar, the dial's bead chooser (a popover at z 9500) |
| 2.3 | dock / tab bar |
| 1.5 | primary/accent buttons, presets, options, quick keys, switch thumb |
| 1.2 | dial disc |
| 1 | the plate: every card, row and tile (see "The plate") |
| .85 | icon buttons, chips, secondary buttons, the widget and Watch keys |
| .5 | a disabled key or chip: it keeps its form, and its label dims to .4 |
| 0 | ghost buttons, text links |
| -.36 | chip "on", ghost pressed |
| -.4 | a Today row or suggestion while it is held |
| -.5 | any other row, day, link or summary while it is held (the sink) |
| -.55 | tab "on" (-1.15 pressed) |
| -.64 | carved fields: search, text fields, segmented controls, switches, steppers, progress grooves |
| -.9 | dial well |
| -1 | wells: notices, the Lock Screen, widget and Watch mocks, the Time chart |

Sheets are solid raised slabs on #252E3C with a carved grabber, not glass. While a sheet is open, the page under it desaturates (to .2) and shrinks to .955.

## Spacing
- **The scale:** `--sp-1` 4, `--sp-2` 8, `--sp-3` 12, `--sp-4` 16, `--sp-5` 24 and `--sp-6` 32 px, in `css/tokens.css`. They are not in `--s`, which holds colours.
- **In use (7c):** every on-scale value in the CSS and in the JSX style strings is written as its token. That is 1,195 of the 1,336 snapped values. JSX numeric values stay numbers, and 20, 40 and 56 stay literals.
- **The grid:** every padding, margin and gap in the app's CSS and in its JSX style objects sits on the 4 px grid.
  - `r25.spacing()` snapped 911 values. A tie rounds up (6 becomes 8), and anything over 32 goes to a multiple of 8.
  - Hairlines of 2 px or less and negative values are kept.
- **Insets:** every plate takes 18/20 (the plate spec). Notices and devices take 16.
- **Gutters:** 16 (`--gut`), in the light-DOM sheets too: Log, Sugmore, Delete all, Drink and Export.
  - A sheet's top-level `.list` sits at x16.
  - A list inside an already padded block takes no gutter of its own.
  - A token row's text starts at x66 in every list.
- **Today's rhythm:** every section header is 26 below what precedes it and 10 above what it heads (a 20 px header box; its aside is taken out of the height).

## Light DOM (app shell, Today, v2 sheets)
| Component | States covered | Notes |
|---|---|---|
| `nav.tabbar`, `button.tab` / `.tab.on`, `button.logbtn` | rest, on, pressed, under sheet | dock 2.3, tab on -.55 (-1.15 pressed), logbtn 3.3 |
| `div.sheet`, `.sheet.full`, `.sheet.v3sh`, `.sheet-foot`, `.sheet-scrim` | half, full, v3, with footer | solid slab. Tab and Shift+Tab stay inside the top sheet, and Escape closes it |
| `div.grabber` | rest, focus, drag | `role="button"`, "Close, or drag down", Enter or Space closes. It is 26 pt tall; the sheet's 44 pt Close is the equivalent target |
| `button.btn` (acc, primary, sec2, ghost, big, wide) | rest, pressed, disabled | disabled keeps its form at .5, with the label at .4 |
| `button.chip`, `.chip.small`, `.chip.on`, `.lchip.lkey` | rest, on, pressed, on+pressed, disabled | |
| `button.opt`, `.opt.on`, `button.act.quick44`, `.preset` | rest, on (carved, hue text), pressed | 44 pt |
| `button.iconbtn.filled`, `button.zib` | rest, pressed | 44 pt |
| `div.seg`, `.seg.n5`, `button.switch`, `div.thumb` | off, on, pressed | carved -.64 |
| `div.search` | empty, filled, focus | carved once; the input inside is flat and fills the search's height |
| `input.field-in`, `textarea.growfield` | empty, filled, focus | carved |
| Today `zrow` with `zkey` (round, seg, pill, word), `zlevel`, `zx` | open, done, live, last, pressed (plate press), the routine's dot | the plate; keys 1.5 at 48 px. The `zinl` bar is hidden |
| `zsug`, `zprimary`, `zsec2`, `zdots`, `zpanel`, Settled | rest, pressed, dismissed; each with its routine's dot | plates; each panel is as tall as its content |
| Later: `zlater` (no form), `zlg .zh` label, `ztok` plates with `ztk` keys | rest, done, pressed | one plate per routine, 72 px; round 48 px keys |
| `.zstrip` (`NeuStripBox`) | swipe across; a vertical swipe goes to the page; the card in view sets the height | `overflow-y: hidden`, `overscroll-behavior-x: contain`. The height follows the swipe between two cards' heights. A taller neighbour fades over 36 px at the foot (`.zcut`, `--zcut`). 16 px of bottom padding holds the card's drop and the focus ring |
| `zdateline`, dial `dl-disc`, `dl-well`, knob | rest, scrubbing | |
| live bar, toast (`mi-hair` .9) | on, with undo | up to three lines before it clips |

### The dial's beads (new in 7b)
- **Art and targets are separate.** The svg (`aria-hidden`) draws the beads. The targets are real buttons, `button.dbt`, in `.dl-tg` above the art: 44 pt each, never overlapping, and each one labelled.
- **One bead per routine per hour, on the ring.** Two beads closer than 44 px merge into a group, and the merging repeats until no two targets overlap.
- **A group (7c)** draws as a fan of beads along the ring, one per routine and each in its own light, with no count on the art. Rows hold six beads, 15.5 px apart, at radius 7.4. The fan leans away from the now-sun, and its one target follows it.
  - Its label lists the routines, the count and the hours, for example "Water, Vitamin D, Meals, Daylight: 5 logged between 07:00 and 09:00. Choose one".
  - A tap, Enter or Space opens the chooser, `div.dlch.neu-pop` (`role="dialog"`).
    - It is portalled to `.screen`, fixed, at z 9500 and raised to 3, so it sits above the strip, the rows and the dock.
    - It opens below its bead, or above when there is no room. It is at most 60% of the screen, and it scrolls inside (`.dlch-in`).
  - The chooser has one 44 pt row per routine (`.dlco`), with the routine's light, its name and its hours. Focus goes to the first row.
  - Inside it, the arrow keys, Home and End move between rows, and Tab wraps.
  - Choosing a row focuses that routine on the dial and returns focus to the bead.
  - Escape (at any point), a tap outside it or a page scroll closes it and returns focus to the bead.
- **A single routine** toggles focus on that routine directly.
- **Clear of the now-sun:** beads keep away from it.

## Shadow DOM (v3 screens and sheets)
| Component | States covered | Notes |
|---|---|---|
| `.ledger .ln`, `.set .li`, `.tl .li`, `.staff .sf`, `.toc .tc`, `.idx .tk`, `.pats .pt`, `.recs .rec`, `.combs .cb`, `.figs .fg`, `.kvs` | rest, pressed (Today's row press: the face carves in, walls and drop to .3), rising | each a plate; their containers are plain stacks with 12 px gaps |
| `.notif`, `.dev` | rest | wells at -1, 16 px inset |
| `button.btn`, `.btn.primary`, `.btn.ghost`, `button.key` | rest, pressed, disabled | |
| `button.chip.sm`, `.chip.sm.on` | rest, on, pressed, on+pressed, disabled | 44 tall, 15 px |
| `button.key`, `.key.num`, `.logrow` | rest, pressed | v7 keys at 48 px; the row scrolls sideways |
| `button.ib`, `button.close`, `.foot button`, `.mnav button` | rest, pressed | 44 pt. Close sits clear of the grabber. The month arrows are two 44 pt keys side by side |
| `button.go` | rest, pressed | 44 pt. Actions that used to sit inside a sentence ("That's everything", "Hold something, or give it a date") are now keys on their own line |
| `button.b`, `button.lk` inside a sentence | rest, pressed | navigation links in prose. They keep their line box and have no expander, under the inline exception, so no link reaches the next line's link |
| `div.search`, `input.field`, `div.stepper`, `.seg`, `button.sw`, `.sw.on` | off, on, pressed, focus | carved; switch hit area 56x44; on is Ink blue (`oklch(.60 .11 232)`) |
| `button.tc/.pt/.rec`, calendar `.cd` (today, future, disabled) | rest, pressed, out of range | each day carries a dot per routine logged, in its light (`.cdh`) |
| loom threads, staff `.sf/.sfb`, rail, `.comb`, `.wkb`, month `.cb` | each in its routine's light (`[data-rh]`, `--rh`) | |
| Time chart (`#yhero`): `.yw` well, `.ym` month keys, `.ypr` printed row | rest, month selected, month pressed, dragging, filtered to one routine, nothing yet | see "The Time chart" |

### Lock Screen, widget and Watch mocks (You › Watch, widgets and Lock Screen)
| Mock | Parts | Notes |
|---|---|---|
| `.dev.lock` | `.dt` clock (light display type), `.dl` line | a well at -1; no keys. The Live Activity mock uses the same well |
| `.dev.wid` (Home Screen widget) | `.wr` rows (52 pt) with `b` name, the figure and a `button.wk` key; `.wh` foot line | keys are raised (.85, pressed -.5, live `.on` in sun). The aria-label is the key plus the routine |
| `.dev.watch` | `.wr` rows (44 pt) with `b` name and `button.wk` (Log / Start / Stop) | rows are 44 apart, so the keys' expanders never reach a neighbour (7a: 22 apart, 6 to 9 misroutes). The aria-label is the key plus the routine |

## Colour per routine
- **Six lights.** saffron 82, lagoon 232, moss 138, jade 178, iris 300 and rose 8, at oklch(.76 .14 h). Night (278) is sleep's, and ember is "now". Modules keep their own.
- **`neuAssign`, in the Routines order.** The Routines order is by cadence, then as stored; the loom and the list use it.
  - A routine keeps the light nearest its stored hue, unless one of the three routines before it already has that light. Then it takes the nearest free one, so any four in a row differ.
  - The stored hue is never rewritten.
- **`neuRepair`, on every list (7c).** Every list a screen shows reports its order: Today's Now, Later and Settled, the suggestions, and the Routines list. The lists are linked into one neighbour graph (`NEU_ADJ`). A routine that shares a light with any neighbour moves to the nearest light that is free of:
  - its neighbours in any list;
  - the three routines either side of it in the Routines order.

  The repair runs up to three passes, so a move never creates a clash in another list.
- **Where the light shows on a list (7d):** the routine's dot before its name on every plate (Today's rows, Later, moments, the Routines index, This week, Totals), and the word "Settled" in the Routines index when it is settled. The name stays cream. In Settled, the routine's dot.
- **One light per screen.** The assignment holds for the session (it is rebuilt only when the routines change), and every screen reads the same map (`neuHue`, `neuRH`, `neuRGB` for WebGL and canvas). A routine therefore has one light on Today, the dial, the strip, Later, Settled, suggestions, the loom, Time's weekly bars, the month dots, the year stack and the item pages.

## Period type on each rule (7c)
- Each target version stores `cad`, the period type it was set with. `cadOn`, `cadSpan` and `periodOf` judge each day by the type and rule in force on it, and a period never crosses a change of type.
- A change of type starts today, and the first new period is short.
- On the item page, each period carries its own `cad`, which the labels (`pLabel`), the names (`perName`), the summary (`perSay`, "finished periods" when the types mix) and the description (`perLabel`) use.
- State saved before 7c is migrated when it loads: each rule takes the routine's type.

## Checks over the inventory (7b; 7c figures are in pass7c/CHANGES.md)
- **Real hit testing** (`src/hit.js`): `elementFromPoint` through the shadow roots, over every route and sheet, scrolled through, at 390 and 430.
  - Under 44 pt, only these remain:
    - inline navigation links in prose (the inline exception);
    - the grabber (the equivalent Close is 44 pt).
  - **Misroutes:** 0 at rest.
  - What remains is transient:
    - rows scrolled under the fixed header or the dock;
    - one rise-band moment on Sketching's key, whose own box contains the point at rest.
- **Pressed response** (`src/press.js`): 800 tappables.
  - Two have no press of their own: the dial disc (a drag surface; the knob and the bead targets answer) and the grabber.
  - The s-confirm empty name is the ruled tour artefact.
- **Pixels under a press** (`src/pix.js`):
  - Today's first row: 17,467 px change by more than 16, at most 32. 7a changed 4 to 8 levels.
  - The current tab: 658 px, at most 227.
- **Contrast** (reviewer's `con.js`):
  - At 390, 3,878 runs and 15 fails. All 15 are disabled controls or out-of-range days, which are exempt.
  - The 430 figure is in CHANGES.md.

## Structure (7d, Mark: "great looking clear structure")
- **Every screen:** one hero; then sections, each with a label; then one raised plate per item, always in the same order: the routine's dot and name, then its state. Nothing else is raised.
- **Section labels** (`.sec > .sech h2`): 22/600 in full cream, 16 px above the first plate; a group inside an index (`.sec.grp`) 19/600 in `--t2`; the side note (`.aside`) 15 in `--t3`.
- **Fewer parts per plate:** a name, one state line, at most one small figure (a bar, ticks or a sparkline) and one key. A routine's colour is its dot, never its name's colour.
- **Dense screens are simplified, not shrunk:** long lists stay one column at full type; a grid never leaves a hole.

## The top of the screen (7d)
- **No drawn chrome.** The status bar, the island and the home bar are gone from every screen, sheet and state.
- **`--sb`** is `env(safe-area-inset-top, 0px)`: about 59 px under a Dynamic Island in a home-screen PWA, 0 in a browser tab. Every top offset is `calc(var(--sb) + room)`: headers and Today's head +16, the navbar +4 (44 tall), the v3 spacer +42, a full sheet +8, a top toast +8, the deep heads +56.
- **`.n7sb`** is a band of the surface's colour under the real status bar (z 60), so scrolled content never runs behind the clock. Its bottom is the clay rise's top clip edge, where every plate is flat. In a browser tab it is 0 tall.
- The page head carries `apple-mobile-web-app-capable`, `black-translucent` and the theme colour, so a home-screen PWA draws under the real status bar.

## Page changes (7d)
- **One number, `--g`** (registered, inherited, 0 to 1), multiplies every form's height in the recipe (`--nR`, `--nD`) and shows the walls' layers (`.wl`, `.iw`, layer i from g = (i - 1) / 7). At 0 a page is printed only; nothing else changes, and no text moves.
- **Out:** the page's `--g` goes 1 to 0 and its opacity 1 to 0 in 160 ms (ease-in).
- **In:** the printed layer is there at once (push and back: from 130 ms); then each form in view, in reading order, takes `--g` 0 to 1 over 260 ms, 35 ms apart, 300 ms at most. Forms out of view are up already. Keys inside a plate rise with it.
- **Tabs** wait for the sink, then change; a second tap during it changes the landing only (also between the sink's end and the new page's first frame); tapping the tab being left cancels it. The handler goes by the tab in view, recorded when the page commits, so a slow render never stacks two changes. If the sink's end never arrives, the change goes 240 ms after it was due. Each tab gets its scroll back, by page.
- **Push and back** change the route at once; the page under a push sinks, a leaving page sinks on top of the page it reveals. No slide, no zoom, no morph.
- **Reduce Motion:** a 120 ms crossfade; nothing extrudes.
- A film of a change can slow it (`window.__n7slow`, `--n7slow`); nothing else reads them.

## The Time chart (7d)
- **A carved well** (-1, 24 px corners, 148 px), full width inside the gutters, with a mark a week (53): a 4 to 8 px bar, rounded at the top, as tall as the week's share of routines with something done, on an engraved zero line (solid over the days there are, dashed ahead).
- **Colour:** the selected month in one strong accent (Ink blue, `oklch(.80 .11 232)`, or the routine's hue when filtered to one); the other months in the same hue, pale (`oklch(.72 .025 h)`), never a dark shade. A week mostly set aside takes its context's colour (night for sick, aside for away).
- **Missing is not zero:** a week with records and nothing done is a 2 px tick on the zero line; a week with no records is a small ring; before the first record nothing is drawn, and the stretch is named "Before Meridian".
- **Today** is marked once, a small sun on the zero line, with "today" printed under it.
- **Printed under the well:** month letters (the selected one cream, the months ahead dim) and the set-aside bands as coloured 3 px strokes with their names (Sick, Montréal).
- **Months are keys** over the well (`button.ym`, full height, `aria-pressed`, labelled with the month's reading). A press darkens the column; the first press reads that month (the reading under the chart redraws in place); a second opens the month; a drag reads month by month; the months ahead are disabled. The keys are as wide as their month (about 27 px at 390, 81 px tall) and tile the well with no gaps: the one place below 44 px wide, since a wrong tap only selects (opening takes a second press on the selected month). The Time filter recolours it to one routine.
