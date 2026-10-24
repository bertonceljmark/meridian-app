# Meridian morph lab: one surface that deforms

Live: https://bertonceljmark.github.io/meridian-app/morph/ (source: evolve/base7/neu-morph/src, `node src/build.js`).
Owner of the arc and of static depth: Meridian studio. This lab owns motion: how things rise, flatten, sink and flow.

## The idea in one paragraph
Nothing is a card laid on the page, and nothing slides over it. Every form carries ONE number, its height `--h`: +1 is a plateau risen out of the page, 0 is flat page, -1 is a well pressed into it. The shadows are computed from that number and from one light direction, so any form can travel continuously from raised, through flat, to pressed. Every interaction below is a change of that number, of a shape's outline, or of the light. A sheet is not a layer that slides up: the thing you touched rises and becomes the sheet, leaving a dent where it was, and sinks back into it when you close it.

## Rules
1. **Depth is state.** Raised: you can press it. Pressed in: chosen or done. Flat: not a control, or gone.
2. **Whatever you touch is what changes.** A row becomes its sheet, a key becomes its options, the search disc becomes the field, a day cell becomes its day. No generic slide-up panel.
3. **Things leave by melting, arrive by rising.** Removal: height to 0, then the gap flows closed. Arrival: the gap opens, then the form rises. Never a fade on its own.
4. **No black overlay.** Behind a sheet the page flattens and dims; it recedes, it is not covered.
5. **One light.** Shadows, highlights and parallax all come from one light (top left). Tilting the phone moves it; that is what makes the layers read as real depth.
6. **Springs, not curves.** Every motion is a spring given as response and damping, the same numbers SwiftUI uses. Presses: 0.08 s down, spring back (0.28, 0.6). Rises: (0.46, 0.62). Melts: (0.34, 1.0). Sheets open (0.5, 0.8), close (0.4, 0.92).
7. **Hold still before moving.** A finished row waits 0.75 s before it melts, so no tap lands on a row that moved (OP-04).
8. **Reduce motion** turns every change instant; state still reads by depth, glyph and position.

## The engine (for whoever ports it)
- CSS: `@property --h {syntax:'<number>'}` per form; `--lx/--ly` (light) on the app root. Two shadow recipes, regions (`.f`) and keys (`.fk`), each a list of outer shadows scaled by max(h,0) and inset shadows scaled by max(-h,0), offsets multiplied by the light vector.
- JS: one rAF loop sets each form's h = rest x fold(position on screen) x (1 - flick dip) x page energy x its own multiplier. Springs are integrated from (response, damping fraction).
- **SwiftUI**: one `NeuDepth(h: Double, light: Light)` ViewModifier that draws the paired outer shadows when h > 0 and `.fill(.surface.shadow(.inner(...)))` when h < 0 (iOS 17 ShapeStyle inner shadows), interpolating through 0. Make h an `Animatable` value so springs drive it. Light is an @Observable from CoreMotion. Morphs use `.matchedTransitionSource` + `.navigationTransition(.zoom)` (iOS 18) and matchedGeometryEffect.

## Every interactive and transitional element (47)

### The surface

**Scrolling folds the page** (built)
- How: Rows rise out of the page as they come up from the tab bar and sink back flat as they reach the top. A fast flick flattens everything slightly, as if the surface were moving under your finger, and it all rises again when you stop.
- Feel: No haptic. The motion is the feedback.
- SwiftUI: ScrollView + .scrollTransition(.interactive) { c, phase in c.neuDepth(rest * (1 - abs(phase.value))) }. Flick dip: onScrollGeometryChange + onScrollPhaseChange (iOS 18, context.velocity) feeding one @State dip.

**Day name folds into the top bar** (built)
- How: As you scroll, the big day name shrinks and fades while a low ridge forms across the top of the page with the short title on it. Nothing slides in; the bar rises out of the same surface.
- SwiftUI: onScrollGeometryChange(for: CGFloat.self) { $0.contentOffset.y } -> progress; bar = surface shape with .neuDepth(0.45 * progress); title .opacity(progress).

**Results deepen as they reach the centre** (built)
- How: In the swipeable results row, the reading in front is a full hollow; the ones at the edge are shallow and deepen as you swipe them in.
- SwiftUI: Horizontal ScrollView + .scrollTargetBehavior(.viewAligned) + .scrollTransition(axis: .horizontal) driving depth.

**Pull to sync** (built)
- How: Pull Today down and a hollow forms above the header, deepening with your pull. Past the point of no return you feel a tick and the label turns to Release. A line of light sweeps inside the hollow while Health syncs, then it heals flat.
- Feel: One tick at the threshold, one when done.
- SwiftUI: Custom, not .refreshable (its spinner cannot be restyled): onScrollGeometryChange reads negative contentOffset; .sensoryFeedback(.impact(weight: .light), trigger: armed); HealthKit HKObserverQuery refresh. In this lab the pull only works on iPhone (Safari reports the bounce); Try it plays the sync.

**Layers pop: light follows the phone** (built)
- How: Every shadow and highlight is drawn from one light. Tilt the phone and the light swings: shadows lengthen on one side, highlights move, and raised things drift a few points against the page (parallax by height). Wells drift the other way. This is what makes it read as real depth rather than a drawing.
- Feel: Subtle: at most 2-3 pt of drift; never on by default for motion-sensitive users.
- SwiftUI: CoreMotion CMMotionManager.deviceMotion (attitude.roll/pitch) at 30 Hz, smoothed, into an @Observable Light {x, y}; NeuDepth reads it for shadow offsets and .offset(x: h * px). Respect accessibilityReduceMotion. On the web lab: turn on in You (asks motion permission on iPhone); a mouse moves the light on desktop.

**Content passes under the tab bar** (built)
- How: The tab bar is the same page divided by one groove. Rows reaching it flatten into it rather than sliding under a floating bar.
- SwiftUI: Same scrollTransition as above; tab bar = .safeAreaInset(edge: .bottom) with the surface colour and a 2 pt groove.

### Keys and logging

**A key sinks and springs back** (built)
- How: Touch down: the key sinks into the page in 80 ms and shrinks to 96 %. Release: it springs back up with a little overshoot. Raised means you can press it; pressed in means chosen or done.
- Feel: Light impact on touch down: the mechanical-key moment.
- SwiftUI: ButtonStyle reading configuration.isPressed -> depth -0.75, .scaleEffect(0.96), .animation(.spring(response: 0.28, dampingFraction: 0.6)); .sensoryFeedback(.impact(weight: .light), trigger: isPressed).

**Done: the key stays in and fills** (built)
- How: On a one-tap routine the key stays pressed in, its routine colour rises from the bottom like liquid, and the check draws over it. Its groove on the left of the row fills to the new level.
- Feel: Success haptic for routines. Records (coffee, doses) get a plain tick, never a reward.
- SwiftUI: Rectangle masked by the key Circle with animated height; Path trim for the check; .sensoryFeedback(.success, trigger: done).

**Count: the next slot fills** (built)
- How: Meals has one slot per meal set into the key. Each tap fills the next slot from the bottom. The figure in the status rolls up to the new number.
- SwiftUI: HStack of slot Capsules; fill via .scaleEffect(y:, anchor: .bottom); figure with .contentTransition(.numericText()).

**Amount: the tile pours** (built)
- How: Tap 250: the tile presses in, light pours up inside it and drains, and the level groove above fills with a springy overshoot.
- SwiftUI: Tile ButtonStyle + PhaseAnimator([0, 1, 0]) for the pour; level width .animation(.spring(response: 0.5, dampingFraction: 0.6)).

**Hold: the key sinks deeper, then options grow out of it** (built)
- How: Keep holding a key and it keeps sinking past normal pressed depth, like a key with a second stage. At the bottom you feel a tick and the options sheet grows out of the key itself.
- Feel: Tick at the second stage.
- SwiftUI: .onLongPressGesture(minimumDuration: 0.55, perform:, onPressingChanged:) driving depth over time; sheet via matchedGeometryEffect / .matchedTransitionSource + .navigationTransition(.zoom) (iOS 18).

**Completed row melts into the page** (built)
- How: After you finish something, the row holds still for 0.75 s (so no tap lands on a row that moved), then sinks flat into the page, the gap flows closed, and its light appears in Settled.
- SwiftUI: Custom Transition (iOS 17 Transition protocol): removal = depth -> 0 then .frame(height: 0); withAnimation(.spring(response: 0.35, dampingFraction: 1)) after a 0.75 s Task.sleep.

**Undo: the row rises back where it was** (built)
- How: Undo in the toast reverses it exactly: the gap opens, the row rises out of the page in its old place, and the key comes back up.
- SwiftUI: Same Transition, insertion = height opens then depth 0 -> 1 with .spring(response: 0.46, dampingFraction: 0.62).

**Toast swells out like a blister** (built)
- How: The confirmation starts as a small bump above the tab bar, swells sideways into a slab, shows the running total and Undo, drains a groove for 4 s, then sinks back flat. A new toast replaces the old one by flattening it first.
- SwiftUI: Overlay in .safeAreaInset(edge: .bottom); width + depth driven by one spring; TimelineView(.animation) for the draining groove.

**On it stays pressed in** (built)
- How: A dated task can be marked On it: the word key stays pressed in until done, and its status says so. Tap again to lift it.
- SwiftUI: Toggle with a custom ToggleStyle mapping isOn -> depth -1.

**Later words are small keys** (built)
- How: In the Later hollow, each routine name is a small raised key. Tap and it presses in and its pit lights in its colour.
- SwiftUI: Same ButtonStyle at a smaller scale inside a flow layout (Layout protocol).

**Session: the live bar lifts out of the row** (built)
- How: Start Reading: a bar lifts out of the row and travels down to dock above the tab bar with the live time. End sinks it back into the row, which then melts into Settled.
- SwiftUI: matchedGeometryEffect(id: "live-\(id)") between the row and a .safeAreaInset(edge: .bottom) bar; Live Activity (ActivityKit) for the lock screen.

### Appearing and disappearing

**More: hidden rows rise one by one** (built)
- How: Tap 2 more: the page opens a gap and each row rises out of it, one after another. Fewer melts them back.
- SwiftUI: ForEach with the custom rise/melt Transition and .animation(.spring.delay(i * 0.09)).

**Hidden result: the hollow heals** (built)
- How: Tap the x on a reading: its content fades, the hollow fills back up to flat page, then the row of readings flows closed. Undo reopens the gap and sinks the hollow back in.
- SwiftUI: Same Transition, with depth -1 -> 0 for wells.

**New reading arrives: a hollow forms** (built)
- How: When a walk comes in from the Watch, a gap opens at the front of the readings, a hollow presses into the page, and then the reading appears inside it.
- SwiftUI: HKObserverQuery -> model insert; insertion Transition for wells (width opens, depth 0 -> -1, then content .opacity).

**Not now: the suggestion melts** (built)
- How: The suggestion sinks into the page and the space closes. No scolding, no badge left behind.
- SwiftUI: Removal Transition as above.

**Filters: rows melt and rise** (built)
- How: In Routines, pick Body and the other rows melt away while the gap flows closed; pick All and they rise back.
- SwiftUI: Filtered ForEach + the rise/melt Transition inside withAnimation.

**A setting reveals more** (built)
- How: Turning Remind me on opens the page and the time wheel rises into it. Turning it off melts it back.
- SwiftUI: if reminder { TimeWheel().transition(.neuRise) } in a Form-free VStack.

**Loading: the surface breathes** (built)
- How: No shimmer. While Health syncs, a few faint ridges slowly rise and settle in a wave across the hollow. When data lands, they flatten into the real lines.
- SwiftUI: PhaseAnimator over depth 0.05 <-> 0.55 with staggered delays; .redacted is not used.

**Empty (day one): the page melts, one invitation rises** (built)
- How: Everything flattens into the page, then a single hollow forms with Start with one thing and one key.
- SwiftUI: Root view switches on model.isEmpty with the melt/rise Transition.

**Counts and badges** (built)
- How: Bring back the held item: the row in the sheet closes, the sheet sinks back into the flag key, and the badge count rolls then sinks away.
- SwiftUI: .contentTransition(.numericText()) + scale/opacity Transition on the badge.

### Moving around

**Tabs: the well flows, screens melt and rise** (built)
- How: The current tab is a pressed well. Pick another and the well flows across, leading edge first, like a dent travelling under the surface. The old screen melts flat and fades; the new one rises out of the page from the top down.
- Feel: Selection tick.
- SwiftUI: Custom tab bar (not TabView chrome): matchedGeometryEffect for the well with two edge springs; content swap with the rise Transition, delays by row index. .sensoryFeedback(.selection, trigger: tab).

**Open a routine: the row grows into the page** (built)
- How: Tap a routine and its plateau rises a little higher, then spreads to fill the screen and settles flat, becoming the new page. Back shrinks it home. Swipe from the left edge to scrub it back by hand.
- SwiftUI: NavigationStack + .matchedTransitionSource(id:in:) on the row and .navigationTransition(.zoom(sourceID:in:)) (iOS 18), which also gives the interactive edge swipe.

**Log key: the sheet grows out of +** (built)
- How: The + key sinks and stays pressed in while the Log sheet grows out of it. Closing sinks the sheet back into the key, and the key springs up.
- SwiftUI: .matchedTransitionSource on the key + .sheet with .navigationTransition(.zoom). Key depth bound to isPresented.

**Details grow out of the row** (built)
- How: Tap a row and the row itself lifts and becomes the sheet. Where it was, a shallow dent stays in the page. The page behind flattens and dims; there is no black overlay. Drag the top down and the sheet shrinks back toward its row as you pull.
- SwiftUI: .matchedTransitionSource(id: row.id) + .sheet(item:) { Details().navigationTransition(.zoom(sourceID:in:)) }; .presentationBackground(.surface); dent = source row depth -0.35 while presented.

**Report: a hollow fills and rises** (built)
- How: Opening a reading runs the morph in reverse: the hollow fills up, passes through flat, and keeps rising into the report sheet.
- SwiftUI: Same zoom transition; depth interpolated from -1 to +1.25 in the presented view.

**Search: the key spreads into a field** (built)
- How: The search disc sinks and spreads across the header into a pressed field, the page melts, and results rise beneath it. Cancel draws it back into the disc.
- SwiftUI: matchedGeometryEffect between the disc and a TextField container, depth +0.6 -> -1; .searchable is not used (its chrome cannot morph).

**Small sheets from header keys** (built)
- How: Context and Held open from their small keys the same way: the key stays pressed in while its sheet is out.
- SwiftUI: As the Log key.

**A day in the month grows into its sheet** (built)
- How: In Time, each day is a small hollow. Tap one and it fills and rises into that day.
- SwiftUI: LazyVGrid cells with .matchedTransitionSource; .sheet with .navigationTransition(.zoom).

**Drag to dismiss scrubs the morph** (built)
- How: Dragging a sheet down does not just slide it: it runs the morph backwards under your finger, shrinking it toward where it came from. Let go past the line and it finishes; otherwise it springs back up.
- SwiftUI: Built into the zoom transition interactive dismissal (iOS 18).

### Controls

**Switch: a bead flows under the surface** (built)
- How: The knob is a raised bead. Flip it and it stretches as it travels, then settles, while the colour fills in behind it like liquid. Off drains it.
- Feel: Tick on settle.
- SwiftUI: Custom ToggleStyle: Capsule well + bead Capsule whose width animates 24 -> 34 -> 24 via PhaseAnimator while offset springs; fill = Capsule width animation.

**Segmented choice: the well flows** (built)
- How: The chosen option is a pressed well. Pick another and it flows there, leading edge first, the same motion as the tab bar.
- SwiftUI: HStack of buttons + one well with matchedGeometryEffect; two springs for the edges (or a single .spring with a stretch PhaseAnimator).

**Stepper: the number rolls** (built)
- How: The +/- keys press like any key; the number rolls up or down out of a small window.
- SwiftUI: .contentTransition(.numericText(countsDown:)) + .sensoryFeedback(.increase/.decrease).

**Time wheel: the hour sits in a well** (built)
- How: A short wheel with one pressed band across the middle. The chosen hour sits in the well; neighbours fade and lift away from it. A tick for every hour you pass.
- Feel: Selection tick per detent: the most mechanical-key moment in the app.
- SwiftUI: ScrollView + .scrollTargetBehavior(.viewAligned) + .scrollPosition(id:) and .scrollTransition per row; .sensoryFeedback(.selection, trigger: hour). (Picker(.wheel) cannot be restyled to match.)

**Colour: the chosen swatch sinks, the page changes light** (built)
- How: The old swatch rises back up as the new one sinks in, and the routine page carries its new colour.
- SwiftUI: Buttons with depth bound to selection; routine hue in the environment so dependants animate.

**Chips: raised until chosen** (built)
- How: Options like times or contexts are small raised keys; the chosen one stays pressed in with a dot, so the state reads without colour.
- SwiftUI: Same ButtonStyle with a selected flag.

**Text field: a well that deepens on focus** (spec only)
- How: Fields are hollows. On focus the hollow deepens slightly and the caret takes the routine colour; on blur it relaxes.
- SwiftUI: @FocusState -> depth -0.8 / -1.1 with .spring.

**Reordering: the row lifts higher** (spec only)
- How: Long-press a routine in edit mode and it rises well above the others; the rows around it flow out of the way as you drag, and it settles back flat into its new place.
- SwiftUI: .draggable/.dropDestination, or List .onMove with a custom row that raises depth to 1.8 while dragged.

**Confirmations without alerts** (spec only)
- How: Retire and Let go do not open a system alert. The key itself asks: it presses in, its label changes to Tap again to let go, and it springs back if you leave it. Everything else is undoable, so it needs no confirmation.
- SwiftUI: Two-stage Button state with a 3 s timeout; no .alert or .confirmationDialog.

### System

**Haptics map** (built)
- How: Press: light impact. Routine done: success. Record (coffee, dose, observation): selection only, never a reward. Hold second stage, pull threshold, wheel detent, tab change: selection. Errors: none (nothing in Meridian fails loudly).
- SwiftUI: .sensoryFeedback for each; Core Haptics only if we add the pour texture later. The web lab uses the iOS 18 Safari switch trick, so it ticks on iPhone (System Haptics must be on).

**Reduce motion** (built)
- How: All depth changes become instant and the light stops following the phone. State still reads by depth, glyph and position, never by motion alone.
- SwiftUI: @Environment(\.accessibilityReduceMotion) swaps springs for .linear(duration: 0) and disables CoreMotion.

**Widgets and Live Activities** (spec only)
- How: Widgets cannot run these animations. They use the same static depth recipe (rendered shadows) and the system content transitions on refresh. The live session uses a Live Activity whose progress groove updates.
- SwiftUI: WidgetKit + .contentTransition(.numericText()); ActivityKit for the session.


## Taste calls (logged, not asked)
- **The tab bar does not hide on scroll.** Hiding it saves 84 pt but moves the one stable anchor; for an ADHD user a fixed home base beats the extra space.
- **No black scrim.** A dimmed, flattened page reads as one surface; a dark overlay reads as a layer on top.
- **Parallax is capped at 2-3 pt.** More starts to look like a 2013 iOS 7 wallpaper effect, which is the gimmick Mark rejects.
- **Loading never shimmers.** Shimmer is the most recognisable template tell; the breathing ridge belongs to this surface.
- **No system alert or confirmation dialog anywhere.** Their chrome cannot morph; everything is undoable or uses a two-stage key.

## Limits of the web lab
- The arc is a flat placeholder; the studio owns it.
- Haptics: real ticks only on iPhone with iOS 18 or later, through the Safari switch trick; one strength only. Native has the full map.
- Tilt light asks for motion permission on iPhone (You > Light follows the phone).
- Animated box-shadows are heavier on the web than native; if it stutters on an older phone, that is the web, not the design.
