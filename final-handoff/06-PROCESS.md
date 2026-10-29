# 06 · How to work so Mark doesn't have to check your work

Mark: "Figure out how to make it do the actual validations, proactive thinking verifications so I dont have to constantly interject and make sure to do the extra step."

The core rule: **nothing reaches Mark until it has passed the gates below, with evidence saved in the repo.** "I think it works" is not evidence. A screenshot, a test result, a trace or a measured number is.

---

## 1. Standing artefacts (keep updated every session)

| File (native repo) | Purpose |
|---|---|
| `docs/OWNER-LOG.md` | Every message Mark sends, verbatim, dated, appended. Never paraphrase in place. |
| `docs/DECISIONS.md` | Each decision: date, what, why, evidence, which owner message it rests on. Reversals reference the old entry. |
| `docs/TRACE.md` / `trace.json` | Requirement → native status (planned / built / verified / dropped + reason). Seeded from `ledgers/feature-ledger.json`. |
| `docs/AUDIT.md` | Keep/adapt/drop of the old codebase (05). |
| `docs/OPEN.md` | Open questions; which ones need Mark; your recommendation for each. |
| `evidence/<date>-<topic>/` | Screenshots, recordings, test output, perf traces for every gate. |

Re-read OWNER-LOG and DECISIONS at the start of every session and before every gate. Decisions getting lost was a repeated failure.

## 2. Phases

1. **Audit and plan** (05). Output: AUDIT, TRACE, plan. No UI work yet.
2. **Foundations:** data model + period/target engine + storage, fully unit-tested (§4). Design tokens and the plate/elevation/material system as SwiftUI components with a component gallery screen.
3. **Feel spikes**, each tiny and shown to Mark as a TestFlight build or simulator recording: clay-rise scroll (ViewModifier on height / `.scrollTransition` / Metal `.layerEffect`), morph-to-sheet (`matchedGeometryEffect` / `.navigationTransition(.zoom)`), staggered page extrude, `.glassEffect` sheets, dial hero. One question per spike.
4. **Screens and flows** in order of priority: routines + logging → Today → history/results → Time → analytics → Watch/widgets → suggestions.
5. **Gamification track** in parallel from phase 3: research-backed candidates as small playable sketches, Mark picks or rejects, nothing goes in the app until he likes one.
6. **Polish and hardening** (§6 checklist) until every gate is clean twice in a row.

## 3. Gates (every change that touches UI or logic)

A change is ready to show only when all apply:

1. **Builds clean**, no warnings introduced, all tests green.
2. **Simulator screenshots** via XCUITest/`simctl` on iPhone SE (3rd), iPhone 16/17 Pro and Pro Max, at default and the largest accessibility Dynamic Type, with Reduce Motion on and off. Saved to `evidence/`. Look at every one yourself.
3. **Self-critique against the failure list** (§5), written down, per screen.
4. **Independent review:** spawn a separate reviewer subagent that did not write the code. Give it the screenshots, the requirement items touched and §5; ask it to find what's wrong, not to approve. The builder never grades its own work (Mark: "I dont think that the agent that builds the app should analyze it"). Fix or record each finding.
5. **Motion check:** screen recording (`simctl io recordVideo`) of every animation touched; frame pacing at 120 Hz with Instruments (no hitches, scroll stays at refresh rate). For feel changes, compare side by side with the approved web reference.
6. **Data honesty:** run with the fixture sets in §4 (empty, one day, unfamiliar routines, 60 routines, gaps, type changes); no invented history, no water glass on push-ups, no "usual" without history.
7. **TRACE updated** for every requirement touched.

## 4. Logic tests you must have

- Period engine: every cadence × target kind × period boundary (week start, month lengths, DST, time zone change, leap year).
- Target/type changes mid-period: past periods keep their rule; the first partial period reads partial; totals and growth labels use the rule in force (the r27/r28 bugs).
- Paused/retired: nothing expected, never "Not yet" or missed.
- Unknown vs missed with and without coverage.
- Backfill and undo.
- **Genericity test:** a fixture with routines Mark never mentioned ("Ceramics", "Call grandma", "Floss", "Read 20 pages", "At most 2 coffees") with every measure type; snapshot all screens and assert no hardcoded copy, icon or unit from the seed (water, guitar, running) appears. Also grep the code: no routine names in logic.
- Scale: 0, 1, 5, 60 routines; 3 years of history; performance budget.

## 5. The failure list (check every screen against it)

From Mark's rejections, in his words where possible:
- "looks like ai generated slop": generic cards, pills, separators, default SF layouts, evenly weighted everything, gradient blobs, emoji icons.
- "plain and boring checklist tracker"; "decorated checklist".
- "not easy to see what is what because worse visual weights": one clear hero per screen, obvious hierarchy.
- Plate inside a plate, cramped type, thin shadows, clipped names.
- Colour drained to look "safe": colour per routine and depth must stay.
- Toggles and settings that make it a chore; any extra step the user didn't need.
- Streak-like language, punishment, backlog, false zeros, invented numbers.
- Something only working for the sample routines.
- Interactions missing: every element has a visible press and a haptic on commit.
- Motion that is a ceremony, slow, or janky.
- Status bar or system chrome faked; content under the home indicator.

## 6. Polish checklist before calling anything finished

Mark's own (24 Oct): "paddings margins etc are right, all functionality still intact, check every single component, every element has interactions, nothing hardcoded in a way where dynamic data wouldn't support it." Plus: VoiceOver labels, contrast AA, Dynamic Type, landscape not broken, dark-only is fine (Ink) unless decided otherwise, empty states, error states, offline, Health permission denied, notifications denied, first launch, return after 3 weeks away.

## 7. Talking to Mark

- He reads on iPhone. **Short messages.** One result, one link or build, at most one question.
- Before asking: decide yourself if it doesn't change the goal; record it in DECISIONS and tell him in a line.
- Ask him only about taste and goals, always with something to look at: a TestFlight build or a short recording. For a feel question, a tiny sketch first, not a rebuilt app.
- When he describes a physical feel, restate it in one or two sentences and get a "yes" before building.
- His questions are questions, not instructions: research and answer, including disagreeing with evidence.
- Never show him something that failed a gate. Never say "done" without the evidence.
- Log every message he sends in OWNER-LOG the moment it arrives.

## 8. Improve the process itself

At the end of each phase, write 5 lines in DECISIONS: what slowed you, what Mark had to catch that a gate should have caught, and the gate you're adding. If Mark catches a defect, add a check that would have caught it before fixing the defect.
