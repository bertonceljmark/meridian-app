# Motion and interactions: handoff to native (SwiftUI)

These web prototypes are reference only. Rebuild in SwiftUI; don't port the JS line by line.

## Where everything is
- **Morph lab:** https://bertonceljmark.github.io/meridian-app/morph/ (repo `morph/index.html`). It has 47 interactions, each with a "Guide" entry describing how it should feel and the native route.
- **MORPH.md:** `morph/MORPH.md`, the same 47 interactions as text (try / how / feel / native). This is the spec to work from.
- **Clay lab:** https://bertonceljmark.github.io/meridian-app/morph/clay/
  - Board: every element and its states.
  - Fold, Focus, Pages and Clay: scroll experiments.
  - Pane: the pin-screen scroll. The clay stays still and forms rise and sink inside it.
- **Source:** `/mnt/project-files/meridian/evolve/base7/neu-morph/src/` (shell.html, app.js, guide.js, clay.js, clay-extra.css, clay-body.html, build.js). Run `node build.js` to rebuild.
- **Scroll sketches 1, 2 and 4:** owned by Studio (`evolve/base7/scroll-sketches/`). Mark's pick there decides the scroll.

## The rules that carry over
1. **One surface.** Nothing slides over the clay. Things rise out of it (height 0 to +1), press into it (0 to −1), or melt back flat. Each form has a single height value, and shadows come from height × the light direction.
2. **Whatever you touch is what changes.** A row grows into its sheet, a key into its options, a day cell into its day. There is no generic slide-up panel and no black scrim. The source keeps a dent while open, and dragging scrubs the morph backwards.
3. **Springs, not curves.** The lab uses SwiftUI's own (response, dampingFraction) model, so its values copy straight across:
   - Most morphs: `.spring(response: 0.5, dampingFraction: 0.8)`.
   - Closing: `(0.4, 0.92)`.
   - Segment and tab wells: `(0.26–0.44, 0.74–0.8)`, with the leading edge faster.
4. **Haptics** on every commit (`.sensoryFeedback`). **Reduce Motion** turns each morph into a crossfade of about 150 ms.
5. **Tilt light.** The light vector follows the phone (CoreMotion), and the shadows and highlights follow it.
6. **Ink surface.** #1D2633, with shadows rgb(0,3,9) ×1.3 and highlights rgb(196,220,255) ×1.9. These match Studio's values.

## Native routes
| Web prototype | SwiftUI |
|---|---|
| form height `--h`, shadow recipes | a custom `ViewModifier(height:)` using `.shadow` and `ShapeStyle.shadow(.inner)`, driven by an animatable value |
| morph from the source rect | `matchedGeometryEffect`, or `.matchedTransitionSource` + `.navigationTransition(.zoom)` |
| scroll-driven height (Fold, Focus, Pane) | `.scrollTransition` per item, with `onScrollGeometryChange` / `onScrollPhaseChange` for velocity |
| one lit heightfield (Clay, Pane grain) | Metal `[[stitchable]]` shader via `.layerEffect`, with the form rects passed as uniforms |
| glass modals (Studio) | the motion notes in Studio's glass study, on top of a Metal refraction shader |

## Open
- **Scroll model:** not decided yet. Use Studio's sketches 1, 2 and 4 and Mark's pick.
- **Board dial:** the dial iframe crops the top of the disc slightly. This is cosmetic and only on the web board.
