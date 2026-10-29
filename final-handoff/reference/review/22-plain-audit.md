# Plain audit · 23 Oct · Review's independent read

**Trigger:** Mark, 15:45 on 23ebaabc: "the app looks plain ugly and boring".

**Method:**
- The bold/b7 build (the one he loved on 21 Oct, "Love the 3d elements") and 23ebaabc were both run in WebGL at 390×844, same seed and same moment.
- Screens compared: Today top, Today scrolled, Time, Routines and You.
- Side-by-side images: review/plain-audit/cmp-*.png (b7 left, now right).

**Verdict:** it did get plainer, and most of it came from our own rules. Mark's asks only caused a small part.
- Only Routines still looks like what he loved.
- Everywhere else, b7's lit objects and coloured material became:
  - grey text lists on one white plate;
  - blurry white light streaks.

## What was stripped or flattened

| Screen | b7 (loved) | Now | Caused by |
|---|---|---|---|
| Today top | A 3D run tube on a plate, a huge "6.2", and a pace bar in the routine hue | A mostly black field of faint vertical streaks with one bright spike at 08:40. The 3D run is gone from Today. Moments are small grey bars. | Mark picked the timeline (06:53), so the hero is his. But at 08:40 it is about 90 % empty dark. It has nothing to say early in the day, which is when he opens it most. |
| Today lower | Coloured suggestion plates, keys in the routine's own colour (pink/olive/green), and jewel icon tiles | Ruled rows with grey line icons, white keys and the hairline-list look. | **Our generalisation** of his 19:11 "the cards you added just look ai slop". He said that about the new cards added around the hero proofs; we applied it to every plate on Today. Also the 21 Oct AI-look diagnosis ("one repeated pastel-icon row template"), which pulled out the jewel tiles. |
| Time | 12 faceted month stones with a big stone for this month, then a grid of month dials | 52 hairline ribs that read as a blurred barcode (hues washed together), then a plain grey settings-style list | **My flow decision C5** (pebbles become LightGlass everywhere), plus D7 renaming the section to "Reports and patterns", which turned the dial grid into a list |
| You | Four cut gems (three lit, one off) and an orange "Check in" key | Four white glow blobs that look like a rendering fault, and a plain list | C5 (LightGlass for modules) and D5 (Feel block removed) |
| Routines | Tumblers, coloured jewel icon tiles and progress bars | The tumblers survive, but the list is grey text with no icons or bars | The same row flattening |

**Common thread:**
- We read each AI-tell rule ("no decoration", "colour only on data", "no boxed cards", "no pastel tiles") as **remove**, not **make it crafted**.
- Every round removed something. Nothing ever added material back.
- The ledgers check features and honesty, not richness. So "0 BLOCKING" said nothing about whether it was beautiful. That is a gap in my gate.

## Calls of mine to relax
1. **C5 "LightGlass everywhere" is withdrawn outside Today.**
   - Mark asked what the pebbles *meant* and wanted something more thematic. He never asked for the glass on every screen.
   - At 52 ribs, or on 4 modules, the glass reads as noise or as a bug.
   - The glass stays only on the Today hero, which he picked.
2. **"No boxed cards" goes back to b7's plates.** Use one material: hairline edge, top light, short contact shadow. His 19:11 complaint was about specific added cards, not about b7's plates.
3. **"Colour only on data" becomes: each routine's own hue is its identity everywhere.** That covers its jewel tile, its primary key and its progress bar. b7 did this and he loved it. Pastel tiles stay banned; deep jewel tiles in the routine hue are fine.
4. **The gate gains a richness check.** Before any sign-off, compare each main screen side by side with b7. A screen that is plainer than b7 without a reason Mark gave is BLOCKING.

## The 3 highest-impact fixes
1. **Bring back b7's objects on Time and You, keeping the honesty fixes.**
   - Time: month stones and the month-dial grid, with a meaning Mark can read. Size = how much was met, hue = the routines that met their aims. Set-aside months are frosted stone, the current month is large.
   - You: the four gems, lit when on, dark when off.
   - Item pages: stones per period, as in b7.
   - Keep the r7 and r12 rules (set-aside frosted, missing ≠ none, no random shape: facets come from the data or are fixed per routine).
2. **Restore b7's material and colour below the stages on Today, Routines and Time lists:**
   - plates;
   - jewel icon tiles in the routine hue;
   - keys tinted in the routine hue for the main action;
   - progress bars on rows.

   Keep the flow simplifications, such as fewer rows and no "Plan the week". Only the look comes back.
3. **Give the Today hero something to show at 08:40.**
   - Bring the 3D run tube back as the arrival or Moments card when a workout arrives, as in b7.
   - Let the hero show the rest of today faintly, as expected slots where routines usually land, so the morning isn't a black field. This must stay honest: expected is dim and outlined, never lit.
   - Make the Moments cards full-height plates again, not small grey bars.

## Notes
- **Studio's A/B of the same two builds is separate.** This read was done without seeing it.
- **None of this changes direction.** It is a return to the style he picked. Only a new object type would need his eye, and none is proposed.
- **Swiftshader caveat:** the glass may render a bit crisper on an iPhone GPU. But the year's density problem and the emptiness at 08:40 are structural.

## Update (15:48)
- **Studio's flag on fix 1 is accepted.** Mark questioned the pebbles twice (22 Oct "Maybe not pebbles, any better more thematic?"; 23 Oct "we still have pebbles in time?"). So stones and gems do not come back without his explicit OK.
- **What fix 1 still holds:** Time and You need a real object, not the 52-rib glass, and which object it is is Mark's call.
- **Paused by the coordinator.** Mark said "I think it never looked right, just didnt hit me until now", and a different approach is being discussed with him.

## Pass 5 quick verdict (bdf8d8dc, 17:10)
**Not ready to show Mark.** Side-by-sides are in plain-audit/tri-*.png (b7, 23ebaabc, pass 5).

**By screen:**
- **Today:** looks almost the same as 23ebaabc.
  - The hero is the same sparse streaks.
  - The run tube isn't on the first screen.
  - The coloured keys are the only visible change.
  - The new icon tiles are glossy gradient squares that look like generic app icons.
- **Today scrolled:** rainbow keys on a pale settings list. It reads busier, not richer.
- **Time:** it changed, but in the wrong direction.
  - The 12 month tiles are small rainbow bar charts. That is chart confetti and reads as a generic dashboard.
  - The report cards below have soft glow blobs, which is an AI tell.
- **You:** four sparkline tiles. Cleaner than the blur, but still dashboard-like.
- **Routines:** tumblers fine; the glossy tiles have the same problem as on Today.
- **Type:** no visible change.

**The 3 boldest changes:**
1. **Make the whole app dark,** from the stage to the bottom of the page.
   - Lists become plates of deep ink with hairline edges.
   - The pale iOS-Settings page is what makes it look plain. Opal, Oura and NB Weather are dark all the way down.
2. **One object per stage, not a grid of small charts.**
   - Time: a single glass year object, where each month is a slab of glass lit by one dominant hue (the routine that met its aim most) and brightness shows how much. Tap a slab to open the month.
   - You: one object too.
   - No multicolour bars inside small tiles.
3. **Give the type a voice and use flat colour.**
   - A distinctive display face at very large sizes for the one number on each screen and on each row's figure, so the change is unmistakable.
   - Solid jewel tiles in the routine hue, not gradients.
   - Today: put the run tube on the arrival or Moments card, and let the hero show expected slots dimly so 08:40 isn't empty.
