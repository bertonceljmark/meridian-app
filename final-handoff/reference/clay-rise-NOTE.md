# Tilt scroll: a sketch of how scrolling feels

`index.html` is v8. `index-v7.html` back to `index-v1.html` are the earlier versions. v1 is kept as it was apart from the default tilt of 7°.

## v8 (Mark: "How could we emphasise the physics of it intruding/extruding gradually")
There are three effects, all on by default. Each has a chip in the new "Effects" row and a URL parameter.
- **Walls (`?walls=0` turns them off).**
  - Raised items show their thickness as a side wall on the lower/right edge, in a colour (#151c27) between shadow and face.
  - It is drawn as 7 one-pixel layers. Each is the item's shape offset i px down and 0.35·i px right, behind the face. Layer i is masked per point so it shows only where h(point above) × N ≥ i. The visible wall height is therefore about h × 5·depth px, and it tapers to 0 toward the edge.
  - Wells get the same rule as an inner wall on their upper/left side (hard inset bands). Small wells cap it at 15% of their height: about 1 px for the tracks and 3 px for the dots.
- **Moat (`?moat=0`).**
  - Displaced clay: a soft dark dip right around each raised item, with a faint lit outer lip about 12–16 px out. It is attached to the item, so it moves with the content.
  - Its strength is the item's "still rising" amount, 4·h̄·(1−h̄) where h̄ is the item's mean height. That is 0 when the item is flat, peaks half-risen, and is 0 once fully up. It is also multiplied per point by the local h, so it is 0 at the clip edge.
  - Wells get the opposite: a slight raised lip, lit upper-left and dark lower-right.
- **Depth (`?depth=1.4`, default; `?depth=1` gives v7).**
  - Full height is scaled 1.4×: shadow offsets and blur, contact shadow, well insets, wall height, and the profile overlay's amplitude.
  - The band becomes 80 px (64 at depth 1). `?band` still overrides it.
- **Kept from v7.** Per-point height, no transforms anywhere, printed-only at 0, the gentle pop, the ramp chips and `?profile=1`.
- **Checks** (Chromium emulating a phone at DPR 3):
  - 0 console errors, including toggling all three chips off and on again.
  - The touch drag scrolls the list natively.
  - 13 of 13 items crossing an edge are exactly 0 at the clip line in every layer: h, shadow, contact, cover, moat, all 7 wall layers, and well depth. The wall masks have forced stops at the shifted edge positions and a 0.02 threshold, so they never interpolate above 0 there.
  - Edge pixels deviate at most 2 levels from #1D2633.
- **Static-artifact check.** I re-ran the 16-frame median check.
  - In the top band (20–64 px), the face region averages −0.85, peaking at +0.84; the middle of the screen peaks at +1.14. There is no bright line.
  - The bottom band averages −1.07: a slightly wider, smooth ramp to flush because the band is now 80 px, with no line.
  - The plots are in `shots/static-artifact-v8.png`, alongside v7.
- **Honest read.**
  - The walls give a visible thickness at the lower/right edge once a row is up, and they grow as it rises.
  - The moat is a soft halo: noticeable around a half-risen row, gone at rest.
  - Depth 1.4 is the most visible change.
  - All of it is subtle at phone scale. If it should read more strongly, the moat could be stronger or the walls thicker.
  - The Effects row adds about 42 px to the header, so the list is 635 px tall.
- **Shots.**
  - `shots/strip-v8-on-vs-off.png` shows the Walk row crossing the bottom edge at 4 positions, with everything on (top) against everything off (bottom).
  - `shots/detail-v8-on-vs-off.png` shows position 2 (fully in +20 px) at full size.

## v7 (Mark: "glow line on top of bottom, static to the screen" and "a gentle pop when element all the way out")
- **Method.** I captured 16 frames at irregular scroll steps (23 + i·61.3 px) so the content averages out, took the per-pixel median, and plotted row-mean luminance against screen y. Anything fixed to the screen survives the median.
- **Cause: v6's slope shading.** The cool "lit" layer and the dark layer were |slope| × h. With the Smooth curve the slope peaks at the middle of the band, and the band is fixed in screen space, so whatever row passed through got a bright strip about 20–64 px below the top edge and a dark strip just above the bottom band.
  - Top band (20–64 px): median face luminance +3.2 above surface, peaking at +6.5 in v6. In v7 it is −0.3, peaking at +1.0, the same as the middle of the screen (+0.5 / +1.2).
  - Bottom band (−64 to −20 px): −3.2 in v6, −0.5 in v7.
- **Fix.** Slope shading is removed entirely. The slope now reads only through the per-point shadow, contact shadow and bevel.
- **Ruled out.** The 1 px forced-0 edge, the shadow masks, the face-edge ramp and the header bottom: none of them leave a line in the v7 median.
- **What remains in screen space.** The intended smooth transition from flush surface at the edge to faces further in. It is a gradient over the band, with no line or spike.
- **Gentle pop, on by default.**
  - It fires once per entry, when the item is fully out of the band.
  - It is a soft spring: response 0.45 s, damping 0.7, peak `--pop` 0.04 at about 80–117 ms, a −0.002 dip and settled by about 0.5 s.
  - It only deepens the shadow: about 8% longer and a faint extra deep shadow (alpha ≤ .16). Nothing moves, and no point exceeds its height.
  - A shallow dip into the band and back does not re-fire (checked).
  - `?pop=0` turns it off; `?pop=0.08` makes it stronger.
- **Kept from v6.** All v6 guarantees: per-point height, no rotateX or transforms, printed-only at 0, wells, `?profile=1`, the band, the curve and the chips.
- **Checks** (Chromium emulating a phone at DPR 3):
  - 0 console errors.
  - The touch drag scrolls the list natively (0 to 265 px).
  - 12 of 12 items crossing an edge are exactly 0 at the clip line (h, shadow, contact, well depth, and the cover at 1).
  - Edge pixels deviate at most 2 levels from #1D2633, with 0 pixels over 3 levels.
- **Shot.** `shots/static-artifact-v6-vs-v7.png` shows the before and after plots next to the median images at 12× contrast.

## v6: height per point (the confirmed model)
Built from v4's per-sample approach. v5 (whole row rises) and v2's rotateX tilt were both wrong.
- **Model.** Every point y of a row or well has its own height: h(y) = curve(clamp((distance from the nearer clip edge − 1 px) / band, 0, 1)) × the item's full height.
  - A row crossing into the screen is low at its edge side and climbs along its length, so the top face slopes down into the edge like bent clay.
  - Each point stops at its own final height. The curves top out at 1, and 1 is the highest value sampled anywhere in the test runs.
  - The 1 px dead zone makes the edge exactly 0 and not merely close to 0.
- **Nothing moves.** There is no rotateX, keystone or translate, and nothing moves as a rigid pane. The shape is drawn only by vertical mask gradients, sampled about every 6 px plus forced stops at the edges and band ends.
- **Slope readouts.** All of these are sampled per point from the local h:
  - shadow length and strength,
  - the contact shadow,
  - the surface-colour cover that hides the face edge, bevel and outline (alpha 1 − 1.3h),
  - slope shading: a faint cool lift where the face rises away from the top edge (it faces the upper-left light), and a darkening where it falls toward the bottom edge.
  The shading is |slope| × h, so it is 0 at the edge and 0 on flat parts. It has no fixed gradient, so the v2 glare strips do not come back.
- **At h = 0.** Printed only, as in v4: text, numbers, glyphs, the progress fill and the printed track and dot bases. No border and no rim.
- **Concave items.** These do the same in reverse: their depth (inset shadows plus a slightly darker floor) is masked per point by h, so it deepens gradually from 0 at the edge. They are:
  - the progress tracks,
  - the set and meal dots,
  - a new recessed "Resting heart rate · this week" chart well with printed bars.
- **Overshoot.** Off by default. `?pop=0.08` turns it on. It only lengthens the shadows of a fully raised item and never transforms anything.
- **Defaults and debug.** Band 64 px (`?band=N`) and the Smooth curve; the chips are kept. `?profile=1` draws each row's and well's h(y) in the right gutter:
  - blue for raised rows, amber for wells,
  - a white line for the surface and a faint line for full height,
  - dashed lines at the band ends.
- **Checks** (Chromium emulating a phone at DPR 3):
  - 0 console errors.
  - The touch drag scrolls the list natively (0 to 265 px).
  - At 6 scroll positions, all 12 items crossing an edge pass: at the exact clip line h = 0, the shadow, contact, slope-light and slope-dark masks are all 0, the cover is 1, and well depth is 0.
  - Edge pixels in the 3 px at each clip line deviate at most 2 levels from #1D2633, with 0 pixels over 3 levels.
  - No `--pop` was written with the default settings.
- **Shots.**
  - `shots/strip-v6.png` shows the Walk row and the chart well each crossing the bottom edge at 5 positions, with the profile overlay.
  - `shots/profile-v6-detail.png` shows position 3 at full size.

## v5 (Mark: "I dont want it to tilt … I just want it to rise gradually")
- **One height per item.** No tilt and no ramp along the row: each row and each key has a single height h for its whole shape. The masks and rotateX are gone. JS writes only `--h`, `--s`, `--pop` and `--ta` per item.
- **Driven by travel.** d is how far the item's edge-side end is inside the nearer clip edge, with the edges re-measured every frame from the scroll container and visualViewport.
  - d ≤ 0, crossing an edge or off screen, gives h = 0: printed only, so a row stays fully flat until it is entirely visible.
  - It then rises over the band: h = curve(d / band).
  - The band defaults to 44 px (`?band=N`). A row is fully up once it has moved 44 px past fully visible, roughly a third of a row.
- **Even rise.** At height h, all of these follow h uniformly across the whole shape:
  - the shadow layer's opacity,
  - the shadow geometry (offset and blur scale),
  - the contact shadow,
  - the surface-colour cover that hides the face edge and bevel (its opacity is 1 − 1.3h),
  - the inset track and dots, which flatten to print,
  - the ink, which goes from 0.74 to 1.
  The shadow geometry is also capped at d/32, so no shadow can reach past the clip edge with any curve.
- **Rise curves.** The chips (Smooth / Late rise / Quick rise, and `?ramp=`) pick the curve of that single height.
  - **Default: Smooth.** The row already waits flat until it is fully visible, so Late rise adds another ~15 px of flat and feels late.
  - Quick rise is mostly up within about 10 px, so the overshoot hardly reads as going past full.
  - Smooth gives an even, gradual rise that lands softly into the overshoot.
- **Overshoot.** Unchanged spring on reaching full height while entering: +8% at about 66 ms, response 0.35 s, damping 0.55, a dip of about −1%, settled by about 0.45 s.
  - It re-arms only after the item drops below 0.3 height.
  - It is cancelled the moment the item drops below full, and never plays on exit.
  - It lengthens and deepens the shadows and lifts the background plate about 4 px; text never transforms.
- **Kept from v4.** Printed-only at 0 with no border, no sheen or glare, and surface #1D2633 continuous from the header into the list. The header toggle is now "Rise / Plain".
- **Checks** (Chromium emulating a phone at DPR 3):
  - 0 console errors.
  - The touch drag scrolls the list natively (0 to 265 px).
  - 13 of 13 items crossing an edge at 6 scroll positions have h = 0, shadow scale 0 and pop 0.
  - No item's shadow reach exceeds its distance from the edge.
  - During the moving touch drag, the 2 rows crossing an edge are flat.
  - Edge pixels in the 3 px at each clip line deviate at most 1 level from #1D2633.
  - Walk entering from the bottom: d −30 and 0 give h 0, d 11 gives .16, d 22 gives .51, d 33 gives .85, and then 1 with the pop 0 → .077 → −.01 → 0.
- **Trade-off.** A tall row stays printed until it is entirely on screen. At the bottom edge that means a scroll of row-height + 44 px between its first appearance and full height. With these rows (74–144 px) it reads fine; a very tall card would look printed for a long stretch.
- **Shot.** `shots/strip-v5.png` shows Walk entering at 5 positions, then the overshoot peak (the real spring, frozen at its 66 ms peak with the `__tilt.pinPopAt` test hook), then settled.

## v4 (Mark: "you can still see the border at the end … like printed text … no border at first" and "this glare row at top and bottom")
- **Flush is printed only.** I removed the v2 engraved rim/seam entirely. Where height is 0, the surface-colour cover hides the whole face: its edge, its corners and the inset bevel lines. The shadows are masked to 0 there too. What is left is the printed content: text, numbers, the + glyph, the progress fill and the dots. Round keys are just their glyph, with no circle.
- **The shape emerges with height.** The cover's alpha is 1 − min(1, 1.3·h), so the face edge and bevel appear in proportion to local height along the row. The shadows already followed h. At h = 0 the outline is invisible.
- **Inset details flatten to print.** The progress track's and dots' inset shadows scale with the row's height through `--hp`, so when flush they are a flat printed track and printed dots, not engravings.
- **Ink contrast.** Printed text sits at 0.74 opacity when flush, rising to 1 when raised (v3 dimmed to 0.62).
- **The glare: we were causing it.** It was v2's "sheen" layer, two pseudo-elements on the face. A rising face in the top band got a light gradient laid over its top, and a falling face in the bottom band got a dark gradient over its bottom.
  - Rows crossing an edge have their top or bottom right at the cut. As the flush cover faded out over the rising part of the band, the sheen showed through as a horizontal bright strip just inside the top edge, and a dark one inside the bottom edge.
  - Measured at x = 195 in the top band, v3 peaked at rgb(36,46,61) against a face of (30,40,54); v4 peaks at (31,41,56), which is just the face's normal light-to-dark gradient.
  - I removed the sheen entirely.
  - Ruled out: the list and header have no background, gradient, inset or border of their own. Both show the body's #1D2633, which is uniform between the header and the list (every sample from y 150 to 190 reads (29,38,51), with no seam). The overscroll background is that same body colour. The 56 px shadow layer and the masks measure 0 at the edges.
- **Edge pixels.** In the 3 css px at each clip edge, across x 0–38 and 352–390 (which covers the old rim and the row sides), the maximum deviation from #1D2633 is 1 level, with 0 pixels over 3 levels. v3 had up to 21 levels and about 90 pixels per edge, which was the rim.
- **Kept.** Late rise, the pop (0 → .078 → −.01 → 0), cancelling the pop on re-entry, and no tilt or shadow at the clip line: 14 of 14 crossings at 6 positions pass, and the 2 rows crossing an edge during a moving touch drag are flat. The touch drag still scrolls the list natively, with 0 console errors.
- **Shots.**
  - `shots/glare-before-after-v4.png` puts v3 and v4 side by side at the top and bottom edges, at scrollTop 213 and 455.
  - `shots/edges-v4.png` shows the top and bottom edges at all 6 positions, at 3x.

## v3 (Mark: "Now its not flat offscreen")
At the visible clip edge, top under the header and bottom, a row is now completely flush: height 0, no shadow, no contact shadow, the face fully covered by surface colour, no tilt and no pop. All that is left there is the engraved seam and the content.

Causes I checked and what I changed:
- **Tilt hinge (the main cause).** The rotateX hinge was on the row's own end, which is offscreen once the row crosses the edge. The plate was therefore still tilted, and slightly widened, right at the cut.
  - Now a row that crosses a clip edge gets no rotateX.
  - A fully visible row hinges on its edge-side end. Its tilt fades in from 0 as that end moves away from the edge, over the flush 35% of the band, so there is no jump when it crosses.
- **Edges re-measured every frame.** Each frame reads the scroll container's getBoundingClientRect, clientHeight and visualViewport. The clip edges are the list top and min(list bottom, visible viewport bottom), so lower browser chrome or the toolbar counts as the edge.
  - In this layout the edges came out as E0 = 0 and E1 = 677 in list coordinates. The old constants were not wrong after the header grew, because v2 also measured relative to the list.
  - The dock and safe area: the list runs to the bottom of the layout and nothing overlays it, so the list bottom is the edge. visualViewport catches the case where chrome covers it.
- **Sampling.** Mask stops are now about every 8 px, with forced stops exactly at both clip edges and at the ramp's kinks (edge + 0.35·band, edge + band). The value at the edge is always sampled as exactly 0 and never interpolated. `heightAt` also returns a hard 0 at or past an edge.
- **Shadow spill.**
  - The shadow layer's padding was 28 px, too small for the pop's extra shadow, which got cut off with a hard edge. It is now 56 px.
  - Fully raised rows within band + 56 px of an edge keep their shadow mask (in v2 they had `--m: none`), so the blur tails and the pop's shadow are masked to 0 at the edge as well.
- **Pop.** It could only fire when every part of the item was at 1, so never for rows partly in a band. Now a pop that is still running is also cancelled, to `--pop: 0`, the moment any part of the item re-enters a band or leaves the screen (checked).

Measured in Chromium emulating a phone at DPR 3, late-rise curve:
- **Six scroll positions** (37, 120, 213, 300, 455, 610). At each one, every item crossing an edge passed: Water and its + key, Sleep, Meals, Walk, Push-ups, Guitar, the three round keys and Journal. That is 14 of 14 crossings, and 0 failures. For each crossing, at the exact clip line:
  - the computed height is 0,
  - the shadow and contact masks are 0,
  - the flush cover is 1,
  - `--rx` is 0deg and `--pop` is 0.
- **Pixels.** In the 3 css px at each clip edge, pixels just outside and just inside each row's side edges (excluding the 1.5 px seam) are exactly the surface colour #1D2633, with 0 deviation. The only non-surface pixels there are the engraved seam where the row's rounded corner meets the cut.
- **Touch and pop.** During a moving touch drag, the 2 rows crossing an edge had tilt 0 and pop 0. The touch drag still scrolls the list natively (0 to 265 px). The pop still plays on full entry: 0, .037, .08, .058, .022, −.002, −.01, then settles to 0. There were 0 console errors.
- **Shot.** `shots/edges-v3.png` shows the top and bottom clip edges at all 6 positions, each crop 70 css px at 3x.

Honest trade-off: rows crossing an edge no longer tilt at all. The incline on them comes only from the shadow and flush ramp, and the keystone tilt appears only on rows whose edge-side end is visible inside the band. The edge is now clean and flat, but the tilt cue is weaker than in v2.

## v2 (Mark: "timing not quite right, maybe a little pop when all the way out")
- **Ramp chips and `?ramp=`.** The chips under the header (Smooth / Late rise / Quick rise) switch the ramp live.
  - `smooth` is v1: smoothstep across the band.
  - `late` stays flush for the first 35% of the band, then uses smoothstep over the remaining 65%.
  - `quick` is an ease-out (1−(1−t)³): it rises early and settles.
- **Default: `late`.** It matches Mark's wording: "for a very short section ... it's flat, then it goes in". With the 56 px band, a row lies truly flat for about 20 px, then rises over about 36 px.
  - Smooth starts rising immediately, so it never reads as flat.
  - Quick looks raised almost at once and mainly shows the tilt.
  - With late, the incline and the pop arrive close together, so the entry reads as one gesture: lying in the surface, tipping up, pop.
- **Pop.** When a row or a round key first comes fully raised on entry, a damped spring runs on `--pop`, driven by time through rAF and not by scroll position. The spring has a response of 0.35 s and a damping ratio of 0.55, and peaks at +0.08 about 66 ms in. It undershoots about −0.01 at around 300 ms and is done by about 0.45 s.
  - `--pop` lengthens the shadow offsets and blur by (1 + 2.5·pop), adds a faint extra deep shadow, and lifts the plate with translateZ (about 4 px, so the plate is about 1% bigger). The plate is the background layer only; text never transforms.
  - It is armed only once some part of the item is below 0.3 height, i.e. well inside a band, and it fires once per entry. A shallow dip into the band and back does not re-pop (checked). Exits never pop.
  - `?pop=0.12` changes the peak.
  - I did not add a settle on going flush. Rows are clipped at the edge before they reach fully flat, so it would not be seen.
- **Engraved seam.** The flush overlay now has an inset rim: a dark line on the upper-left edge and a faint cool line on the lower-right. Because it shares the overlay's mask, it shows only where the row is flush. The flat end now reads as a shape cut into the surface rather than just losing its shadow. It is subtle at full size and visible on the left and right edges of flush rows.
- **Header.** The header is about 42 px taller because of the chip row. The scroll area is 677 px tall instead of 719.
- **Tests.** Run in Chromium emulating a phone at DPR 3, with each of the three ramps. Each run had 0 console errors, and a touch drag scrolled the list natively (0 to 265 px). A real-time sample of `--pop` gave 0.056, 0.079, 0.049, 0.015, −0.005, −0.010, −0.003, 0. Playwright WebKit is still not installed here.
- **v2 shots.**
  - `shots/strip-v2.png` shows the Walk row entering through the bottom band at 5 positions (1–5), then the pop peak (6), then settled (7). Panel 8 is the top band with Sleep leaving.
  - For panel 6, the running spring was frozen at its 66 ms peak with the test hook `__tilt.pinPopAt(ms)`. The scroll that triggered it was real.
  - `shots/pop-peak-vs-settled.png` shows the peak and settled frames side by side at full size.

## v1

Mark's idea: rows are flat right where they scroll in or out at an edge. Each row then inclines gradually along its length, not all at once, until it is clear of the edge band and fully raised.

Open `index.html`. The phone layout is 390 px wide with a fixed "Thursday / 29 October" header and a native `overflow:auto` list.

- `?band=N` sets the band height in px (default 56 in v2; it was 72 in v1).
- `?tilt=D` sets the rotateX angle at full slope (default 7; `?tilt=0` gives the ramp from shadows and masks only).
- `?mode=plain` starts with the effect off. The Tilt / Plain toggle in the header switches it live.
- `?guide=1` draws dashed outlines on the two bands.

## Technique
- **Height ramp.** Height h(y) = smoothstep(min(y/B, (H−y)/B)) over the scroll viewport. It is 0 at the edge and 1 once a point is B px inside.
- **Per-row sampling.** On every scroll rAF, each row samples h along its own length, about every 9 px. The samples become three gradient strings, written as custom properties:
  - `--m` masks the main neumorphic shadow, both the dark lower-right and the cool upper-left light.
  - `--mc` masks a tight contact shadow that peaks at mid-height. A half-risen part therefore has a short, hard shadow instead of a faded long one.
  - `--mf` masks a flush overlay in the surface colour that covers the face where h ≈ 0. Text and grooves sit above it.
- **Tilt.** The decorative plate (shadow, face and overlay) gets `perspective(460px) rotateX()`. The angle is proportional to h(bottom) − h(top), and the hinge is on the edge side: top in the top band, bottom in the bottom band. The raised end comes toward you and widens slightly, which gives the keystone you can see in the close-up.
- **Sheen.** A rising face in the top band brightens slightly and a falling face in the bottom band darkens slightly, because of the upper-left light.
- **Text.** Text never rotates or scales. It stays sharp DOM text and dims from 1 to 0.62 opacity toward flush.
- **Constraints met.** There is no JS scrolling, no touch-action or preventDefault, and no filters, canvas or WebGL. JS writes only custom properties, and skips any that have not changed. Fully raised rows get `--m: none`.

## Honest read
- **Strongest cue.** The incline reads best as a keystone: the half-risen row looks hinged at the edge. Shadows grow along the row as it travels in, so it does not look like a fade or a clip.
- **Weak flush end.** The flush end is subtle. A neumorphic face is nearly the surface colour, so "flat" mostly reads as "no shadow". The list top is also a hard clip at the header, so the row's very top edge is cut off rather than visibly sitting at 0.
- **Tilt angle.** At 12° the row widened a few px past the column and looked like it leaned toward you. The default is now 7°.
- **Gap at rest.** The list has top padding of band + 4 px so that nothing is ramped at rest. That leaves a 72 px empty strip under the header.
- **Testing.** Tested only in Chromium mobile emulation at DPR 3 (Playwright WebKit is not installed here), with 0 console errors. A CDP touch drag scrolled the list natively from 0 to 438 px, including the fling. Real Safari behaviour of masks plus rotateX during momentum scrolling is unverified.

## Shots
- `shots/strip.png` has four frames: (1) at rest at the top, (2) mid-swipe during the touch drag, with Meals in the top band and Walk in the bottom band, (3) a close-up of Sleep with its top inside the top band, tilt above and plain below, and (4) at rest further down.
- `shots/closeup-tilt.png` and `shots/closeup-plain.png` are the close-up crops at full size.
