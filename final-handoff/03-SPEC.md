# 03 · Product logic: what the app must do

This is a map, not a replacement. The authoritative sources are:
- `reference/CONTRACT.md` (v1.1.1, approved by Mark 18 Oct): layer A requirements, acceptance scenarios §8;
- `ledgers/feature-ledger.json`: 625 items, each with Mark's quote, source and status in the 7e prototype;
- `ledgers/research-ledger.json`: 494 research findings;
- `reference/review/21-flow-findings.md`: answers to Mark's flow questions and every "only works for the seed person" bug.

**Status of everything below:** requirements (A) are binding outcomes. Mechanisms described are how the prototype did it, which is evidence, not a rule. You may replace any mechanism if you can show a better one meets the same outcome.

---

## 1. Routines (the core, priority 1)

- **Any routine the user names**, unlimited, no categories, no seeded "baseline" list. Names never pick the mechanism (no `if name == "Water"` anywhere; test it, see 06-PROCESS).
- **Measure** chosen per routine: done / not done, count, amount + free-text unit (ml, pages, km, anything), minutes, sessions, reps, imported from Health. Log controls follow the measure, never the name. The visual object follows measure + unit (volume unit → glass; other amounts → light column toward aim; sessions → one rib each; events → slot ribs; observations → neutral grey).
- **Cadence:** every day, n per week, weekly, n per month, every N days/weeks, specific weekdays, calendar periods, or no target. Targets can be "at least" or "at most" (e.g. at most N coffees).
- **Lifecycle:** active, paused, retired. Paused is not "not yet" and not missed: nothing expected, shown as "Paused" and a faint dotted line.
- **Target history:** a change of target or period type applies from today ("starting today"); finished periods keep the rule that was in force then. This was the hardest logic in the prototype (r27/r28 blockers: month totals re-judged under the new type, partial first month, growth labels, Weeks view Water). Write unit tests first (06-PROCESS §4).
- **Unrecorded ≠ missed.** Three states per period: met, not met (only if the user recorded data that day or coverage says silence means none), unknown. Missing never shows as zero or failure.
- **No streaks** and no word "kept". No backlog after absence. Missed dated commitment moves to the next occurrence.
- Must work with 5 and 60 routines, long names (ellipsis in layout, full title kept), Dynamic Type sizes.

## 2. Logging

- Fastest path: one tap on Today for done/count; familiar presets for amounts, editable by the user.
- Undo everywhere; edit/backfill past entries ("yesterday" gets the right date and a chosen time, not today's clock).
- Meals: any food is one tap, records when, not what or how much (21-flow-findings Q3).
- Optional "first step" text for session routines, asked once after the first session, never required.
- Optional Feel/Function note: never mandatory, never a 1–10 rating.
- Medication, supplements, caffeine, alcohol are **observations**: recorded neutrally, never rewarded, never targets unless the user sets an "at most".

## 3. Prompts, reminders, commitments (§14 + ef-support)

`reference/S14-intentions-and-reminders.md` is the model. Six kinds that must stay distinct: commitment with a deadline (trash every Thursday), flexible routine, optional opportunity, intention ("hold this for later"), explicit reminder, deferred suggestion. Lifecycle is three separate tracks, not one status enum.
- Event-based moments named by the user ("after coffee", "when I get home") beat clock reminders (`reference/ef-support/`).
- Inferred "smart timing / receptivity" was researched and rejected as a default; an item stays visible rather than re-notifying.
- Budget: few notifications (prototype: cap 3 per day, quiet hours). Everything works with notifications off.

## 4. Smart suggestions (wanted, not built)

Mark: "truly smart, based on what you are doing and where you are … enforced by push too", then "drop the only one constraint". Now shows due routines plus a couple of context-fit suggestions, clearly marked as suggestions, ranked by fit. Rules from the research: suggestions come from the user's routines and their fields (duration estimate fits the gap, "with others" not suggested when alone, location the user tagged), never from routine names; every input labelled by how trustworthy it is (S14 §4); no LLM required. Native inputs: Core Location (visits/regions), Core Motion activity, HealthKit, EventKit, Focus state via App Intents. **This needs a design and on-device prototype with Mark.** Treat as open (04-STATE §3).

## 5. Results and history (priority 3)

He loves Sleep Cycle scores, Apple Watch workout stats, Strava breakdowns, personal records, trends, historical comparisons. Requirements: beautiful per-routine history, records, period comparisons, run route maps from real GPS (HealthKit workout routes), a year view, weekly recap. Every number honest and explained ("How this counts"). No invented scores; a transparent summary score is acceptable where it is honest.

## 6. Analytics (priority 4, optional depth)

`reference/analytics/`. Facts stored once; coverage records when silence means "none"; candidate pairs come from rules over fields (not names); within-person comparisons; multiple-comparison correction (BH FDR); results can say "not yet" or "we don't know". Life context (sick, away, holiday spans) explains gaps and is excluded from comparisons. No causal claims.

## 7. Gamification (priority 2, unsolved)

There is no approved mechanism. See 02-HISTORY for the long rejected list and 01-GOAL §8. Requirements that any candidate must meet: motivation *before* action, not only reward after; works for any routine; no streaks, no punishment, no consumption rewards; not childish, not a game bolted on; not a ceremony; sustainable over months. The research is in `reference/research/r1,r4,r5` and the feature ledger area "Engagement". Your job includes proposing candidates backed by evidence and testing them with Mark as small on-device sketches.

## 8. Platforms

iPhone first (Mark's device). Apple Watch (quick logging, workouts → routines), widgets and Lock Screen, Siri/App Intents, Live Activity for timed sessions. HealthKit read (sleep, workouts, steps, routes) with Health off fully supported. Local-first storage with migrations; sync optional. Privacy: "Privacy and your data" in one place.

## 9. Information architecture in the prototype (evidence, can change)

Dock: **Today** (dial hero of today's progress, Now rows = what's due/held, Later rail = rest of today, cards = results and arrivals), **Time** (year of week ribs, months, weeks, story), **Routines** (index, item pages, settings, composer), **You** (records, modules, observations, settings). Log sheet from a raised + key. Search in the header. Held icon only when something is held. See screenshots in `screenshots/`.

## 10. Design system (approved look, see 02-HISTORY §5)

- Surface Ink `#1D2633`. Everything is pulled from one clay surface; nothing floats on top except glass sheets.
- Elevation by height `--h`: well −1, page 0, plate 1, key 1.5, dock 2.3, + key 3.3. Shadows `rgb(0,3,9)` ×1.3, highlights `rgb(196,220,255)` ×1.9, light follows phone tilt.
- The plate: 26 px corners, 20/18 insets, title 20/600, sub 15, list type 17/600 + 15, 12 px gaps, **one plate per item, never a plate inside a plate**. Keys 48 px, 16 px corners.
- Colour per routine (saffron, lagoon, moss, jade, iris, rose, night, ember), shown as a lit 8 px dot and in that routine's marks.
- Screen-width dial hero on Today.
- Clay-rise scroll: `reference/clay-rise-NOTE.md`. No moat, no drawn status bar.
- Page change: old page sinks, new page's forms extrude staggered.
- Motion: springs (response 0.5 / damping 0.8; close 0.4 / 0.92), what you touch morphs into the sheet, haptic on every commit, Reduce Motion → ~150 ms crossfade. `reference/MORPH-HANDOFF-native.md`.
- Glass for modals/popups, native iOS 26 `.glassEffect` (not a web imitation). `reference/GLASS-NOTE.md`.
- Full token and component detail: `reference/COMPONENTS.md`, CSS in `prototypes/source-7e/src/css/`.
