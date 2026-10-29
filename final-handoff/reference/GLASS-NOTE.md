# Liquid glass (Mark 24 Oct 18:10: thick glass "bad"; wants Apple Liquid Glass from an existing repo)
Library: liquidGL v3.0.0 by NaughtyDuk (MIT), https://github.com/naughtyduk/liquidGL, npm liquid-gl, loaded as an ES module from jsDelivr.
Why this one: it runs in Safari (WebGPU -> WebGL2 -> WebGL1 -> CSS fallback), uses one shared canvas, and offers bevel, refraction, aberration, frost, specular and tint.
Ruled out:
- liquid-glass-react and other SVG feDisplacementMap ports: Chrome-only.
- @ybouane/liquidglass: one WebGL context per element, plus DOM capture.
- liquid-glass-studio: an editor/demo, not a library.
Setup:
- snapshot = #bg, two still images of the Ink Today: the top, plus the tab bar pinned to the bottom.
- content:false, so the content stays live DOM.
- Lenses move by transform only and wait off-screen when closed, so liquidGL stops drawing them.
Tested: WebKit (iPhone 14 Pro, 393x660 in-app height and full) plus Chromium. No errors and no long tasks.
Pages: index.html -> /liquid-glass/ (Studio pushes).

## v2 tune (Mark 18:57: "much better but looks a bit weird")
Diagnosis:
- liquidGL's frost is a 16-tap random blur. It reads as grain or blotches.
- Its "specular" is two drifting light blobs, not a rim, so it looks like smudges sliding around.
- Aberration 0.5 made rainbow ghosts of the status bar and the dial.
Fix:
- The glass now refracts a pre-blurred copy of the Today (#snap, a gaussian under #bg), with frost 0, so it is calm and cheap.
- specular is off. A CSS hairline rim was added, bright top-left and faint bottom-right.
- A light 4.5% film lifts the face the way Apple's dark glass does.
- aberration is 0.12, and the bevels are thinner.

## v3 hardening (Mark 20:40 "broken" on his phone, not reproducible in WebKit/Chromium incl. WebGPU)
engine forced to webgl2 (iOS 26 Safari would otherwise take the WebGPU path, which I cannot test on real Metal); CSS backdrop-filter fallback if liquidGL fails to load, throws, loses context or has no canvas after 6 s.

# HANDOFF to native (25 Oct)
What's live on Pages:
- /liquid-glass/ is the current pick. It is the hardened build df573f9c; whether it works on Mark's phone is unconfirmed, and he is "not really impressed".
- /glass-thick/ was rejected (source glass-v2/).
- /glass/ is Studio's study.

Native, on the Mac:
- Use the real iOS 26 `.glassEffect(.regular.tint(...), in: .rect(cornerRadius:))` for sheets, popups and toasts, plus GlassEffectContainer for morphs.
- Lessons for a dark Ink surface: a smooth frosted face, one thin rim highlight, little rainbow, a slight light film, high text contrast.
- Custom optics, if ever needed, are a Metal .layerEffect on the page layer (math in glass-v2/glass2.src.html).

Open:
- Confirm the glass on device.
- Fit the sheets into the real Today (Studio motion spec: grow from source, drag to dismiss, page energy 0.25, no scrim).

Nothing is running.
