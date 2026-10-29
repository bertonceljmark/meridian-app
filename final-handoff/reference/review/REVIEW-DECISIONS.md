# Meridian decision record

Continued from `phase1/DECISION-RECORD.md` (kept as history). Kept by the Review thread.

Concise and cumulative. Each line: date, decision, source. **Approved** means Mark said so. **Rejected** means Mark rejected that implementation; the design family is not banned unless stated [19:26 §2]. **Experimental** means explored, never approved, usable as evidence. **Pending** means awaiting Mark. Sources: `[C]` CONTRACT.md, `[hh:mm]` Mark on 18 Oct, `[19/hh:mm]` Mark on 19 Oct (all in owner-messages.md).

## Approved
- 18 Oct 13:07 · CONTRACT.md v1.1.1, including §0 clarifications · [C]
- 18 Oct 13:07 · P-1 reduction intentions, conditional on explicit evidence · [C §3]
- 18 Oct 13:07 · P-3 medication records in principle · [C §3]
- 18 Oct 13:07 · P-2 Screen Time not excluded; feasibility pending · [C §3]
- 18 Oct 19:26 · Meaningful engagement may exist inside the app; families of mechanics aren't banned for earlier failures; collection-level engagement worth exploring; five outcomes kept apart · [19:26]
- 19 Oct 05:46 · Keep the full capability for optional observations, medication, contextual records and subjective well-being information · [19/05:46]
- 19 Oct 07:30 · **Approved in part:** keep generic, explainable assistance ("a genuine improvement, preserve that progress"); its heuristics stay experimental · [19/07:30 §5]
- 19 Oct 09:30 · Phased process with review stops (diagnosis, directions, slice, refinement); no silent scope reductions; no disabled optional features without authorisation · [19/09:30]
- 19 Oct 09:30 · Voluntary feel and function recording is a committed capability, and its removal was a regression · [19/09:30 §3]

- 19 Oct 10:54 · Phase 1 accepted provisionally as the working foundation; the inventory is a working reference, not a specification; Phase 2A only authorised. Prototypes are disposable design evidence for a native SwiftUI app, with no production engineering · [19/10:54]

## Rejected (implementations)
| Proposal | Where | Mark's verdict |
|---|---|---|
| Day Line, Atlas, Questions | prototype 01 | Rejected; a user-maintained Questions list is ruled out [11:49] |
| Loadout, Broadcast, Rhythm | reset/ | Too loud; Rhythm tied to times of day [12:40] |
| Tempo, Forecast, Almanac | p02/ | Streak-like, journal-like, plain [14:09] |
| Pursuits, Developing, Invitations as the engagement system | engagement/ | None compelling [18:43] |
| Four-week concierge test; written weekly reflections; Health export requests | engagement-design/ | Not approved [19:26] |
| Composition, Portrait as motivation | engagement-slices/ | Presentation features, not motivation [20:31 §0] |
| Practice Book, Barometer, Perennials, Kalendar, Repertoire (Phase 2A); Phase 2B builds cancelled | phase2a/ | "I don't particularly like any of them"; converged visually and structurally; concept-first process; visual exploration narrow, editorial, conventional [19/13:26] |
| Conversation-first architecture; an LLM required for normal use | experiments/ | Rejected [15:15] |

## Experimental (never approved; evidence only)
| Proposal | Where | Mark's verdict |
|---|---|---|
| Counterpart, Turn, Surface | experiments/ | Counterpart's visual quality liked, chat structure not; Turn's motion liked, ceremony not; Surface's physicality liked, doesn't scale [15:15] |
| Whole-product architecture and style (Today, Log, Time, Routines, You; grammar by measure type; milestones, comebacks, week-close) | whole/ | "Coherent" but "drifted toward generic iOS wellness design"; motivation "mostly feedback" [17:10] |
| Range, Craft, Company, Record baseline | engagement-design/ | Hypotheses [19:26] |
| Hold, Start, Cross; event-anchored intentions; runway | ef-support/ | Research only, not reviewed as product design |
| Analytics data model, rule-based Patterns, evidence ladder, context assumptions | analytics/, integrated/, refined/, studio/ | The capability binds; method and presentation are hypotheses [C §0] |
| Horizons Today, Time with radial plates, You tab | integrated/, refined/ | Not approved; plates questioned [19/07:30 §8] |
| "Quiet instrument, vivid record" art direction; no pills, cards or uppercase; 13 interaction primitives; one moment at a time on Today; History ledger | studio/ | Not approved; "dissatisfied with the overall direction and quality" [19/09:30] |
| Craft studies S1–S3, nine takes; integration architecture v0 and its demos | craft-studies/, integration/ | "Some of the individual interactions look promising"; no direction selected [19/15:12]. Review verdict in review/01 |

## 19 Oct, afternoon
- 19 Oct 13:26 · All five 2A directions rejected; Phase 2B cancelled; change the process before more directions · [19/13:26]
- 19 Oct 13:36 · Craft studies approved as the step replacing 2B · [card choice "Run studies" on the decision card in the Meridian studio thread, 13:36:42; no text message]
- 19 Oct 15:12 · No craft direction selected. Whole-product integration feasibility review before extending any craft language; four questions kept separate (interaction, visual language, architecture, motivation) · [19/15:12]
- 19 Oct 15:26 · Collaboration mode: Claude owns research, invention, process and experiments; committed capabilities protected; major product decisions go to Mark; small experiments; concise communication · [19/15:26]
- 19 Oct 15:32 · Builders don't evaluate their own work. Studio builds, Review critiques and keeps this record and the capability check · [19/15:32]

## Review decisions (internal, reversible; Mark may override)
- 19 Oct · Kept as components: lift-on-time, detent input, vessel and fold (target routines' own page only), radial year (sparse rhythms), Life continuum, one-cursor report · review/01 §1
- 19 Oct · Abandoned: S1-A, S1-C, S2-B as home; S2-C endpoints; S3-C; vessel as product grammar; zone-stacked Now; pick-two as Patterns' main path; Figtree/cobalt test register; finishing the integration demos · review/02
- 19 Oct · Architecture v1: Home, Life (with catalog), Patterns (rule-selected findings first, explorer second), global Add, Settings; grammar and gesture rules in review/01 §3.3 · review/01 §3
- 19 Oct · No captions or legends as a substitute for honest design; coverage lives in review/CAPABILITY-CHECK.md · review/01 §2.3
- 19 Oct · Next test: one home, built from a stated motivational stance and a chosen material, at most two takes, reviewed before Mark · review/02, review/03
- 19 Oct · Defaults pending objection: Hold and Start carry forward, Cross parked; Patterns conservative; recording mode asked once per observation; calendar access deferred · review/02

- 19 Oct · Home test (two takes) reviewed and passed to Mark without another pass; must-fix list in review/04 · review/04
- 19 Oct 21:53 · Mark: Take B rejected entirely (stone, pieces, the week as home). Review also drops B's week as a candidate for Life's week view. Take A "fine", not loved; his doubt is that it won't hold many items · [19/21:53]
- 19 Oct · Next test: the home under load (20–40 routines, many alive at once). A's stance is tested first; one non-A take is allowed if A can't scale · review/05
- 19 Oct · Home under load (A1 Front and keys, A2 One cursor home) reviewed and NOT shown to Mark: A1 reachable but a tile dashboard, A2 calm but blind. Sent back with review/07 (no grids, cards or pages; find by sight, one tap) · review/06
- 19 Oct · Second pass (T1 Set as type, T2 Sets) reviewed: T1 answers the scale doubt and goes to Mark with T2 as the alternative; fixes listed in review/08 · review/08
- 20 Oct 06:14 · Mark: doesn't really like any of the results, T1 and T2 included; "Baseline may be wrong too" (A's light-on-dark front and the shared material are in question, not just the item layout). No new Studio brief; a Taste calibration thread gathers positive taste signal (real apps rated love/meh/no) before more Meridian screens are built · [20/06:14]
- 20 Oct 06:25 · Mark worries a chosen design won't fit all functionality, or that functionality gets forgotten. Review answers with the hard set in CAPABILITY-CHECK v1.1, tested on every round and named in each presentation · [20/06:25]
- 20 Oct 11:00–11:12 · Blind taste check (50 ratings): loved "Set as type" and the 18 Oct whole-product prototype; 0/10 flat styles loved. **This reverses 06:14 for Set as type as a structure: the surface was the issue, not the structure.** Taste direction: lit, dimensional, rendered material, one big hero, weighty feedback (mechanical key, liquid fill); not flat, not cute · taste/findings.md
- 20 Oct · Next: Studio builds Set as type home + one report + log tap in Meridian's own dimensional material (coordinator brief). Review gates it on the hard set and on taste/findings.md before Mark · taste/findings.md
- 20 Oct · Depth test passed both gates (hard set 1–9 tested; taste matched by Review's judgement) and shown to Mark; three non-blocking fixes in review/09 · review/09
- 20 Oct 15:46 · Mark: depth test rejected; "depth is the wrong thing we took from the apps"; "confusing, I have no clue what is what". Review: the confusion is structural (cold read fails T1 too). New gate 0 "what is what" (cold read) before the hard set. Depth fixes and new builds held · [20/15:46], review/10
- 20 Oct 15:50 · Asked what he loved in the apps, Mark: "All of these I suppose idk". Review takes clarity as the floor, with mood, polish and tap feel layered on top. Depth-test fixes dropped. Studio briefed: clarity-test, gate 0 first · [20/15:50], review/11
- 20 Oct · Clarity test (C1 Now line, C2 Control surface): core now clear in both, but neither passes gate 0 (finished run as hero, ambiguous notes, 25-alive pill wall, switches read as settings). Sent back for a fix pass on both, not shown to Mark · review/12
- 20 Oct · Gate 0 recalibrated: every state and action must read clearly (navigation labels may be learned). After the fix pass C2 Control surface passes; C1 weaker. Shown to Mark with the taste question (clear but conventional). Fixes in parallel: timer format, "Run arrived", dashed note boxes, "0 ml of 2 L" debt on day one and return · review/13
- 20 Oct 16:57 · Mark: C1 and C2 both rejected, "just ugly", "still cant tell". The AI cold read is now a screen for obvious failures only, never a stand-in for Mark. Process change (coordinator): rebuild the real layout of an app he loved (Tiimo default; card in the project chat) with Meridian content, then change one thing at a time. Hard set comes after he finds it readable and good-looking. Presentation: one full-width phone at a time (side-by-side phones were about 145 pt wide on his iPhone) · [20/16:57], review/14
- 20 Oct · Tiimo rebuild (faithful layout with Meridian content) shown to Mark without a fix pass; cold-read flags kept as one-at-a-time changes · review/15
- 20 Oct 17:33 · Mark: Tiimo rebuild rejected ("plain and boring checklist tracker"); his favourite is still the 18 Oct whole-product prototype (whole/); "something about this process is not working" · [20/17:33]
- 20 Oct · Process change (coordinator): Studio evolves the 18 Oct whole-product prototype step by step and shows each step to Mark directly in the Studio thread. Review no longer gates rounds before Mark; it runs the capability check alongside, sends gaps to Studio, and comes to Mark only for a gap that forces a real trade-off · [20/17:33]

## Pending Mark
- One-off intentions in Meridian (small form recommended) · review/02
- Mark judges each step of the whole-prototype evolution directly in the Studio thread

## 20 Oct ~21:00 · Feature ledger
Mark (19:40, Studio thread): "how can we make sure we dont miss any". Review built review/17-feature-ledger.md: 605 deduplicated features from all 34 owner messages plus CONTRACT v1.1.1, each driven in Studio's Step 1 build (354 present, 158 partial, 72 missing, 21 iPhone-only). Mark corrects it on https://claude.ai/artifact/7q81yN3Kpg2c2yAX4UqU8A (db collections "corrections" and "additions"). Gaps sent to Studio as review/17b-ledger-gaps-for-studio.md. The ledger replaces scattered gap lists as the record of what Mark asked for; new owner messages get added to it.

## 21 Oct 17:34 · Final UI loop (autonomous)
Mark picked bold style 7 (Opal + NB Weather; "Love the 3d elements") and asked for the final UI with everything he requested, best ADHD UX and maximum polish, run autonomously. Studio builds evolve/base7/; Review checks every iteration on four tracks (features via the 605-item ledger, layout, AI look against real Opal/NB Weather/Oura, ADHD UX) and signs off at zero open flags. Method: review/19-final-ui-loop.md. Review settles trade-offs by Mark's rules and logs them here; Mark is asked only if a call would contradict an explicit ask of his.

## 21 Oct ~18:00 · Four items previously held for Mark (GR-02, GR-15, GR-34, LF-03), settled by Review
Mark asked for the round to be autonomous (17:33) and for EVERYTHING he requested to be implemented (17:29). He also said gamification is unsolved: don't fake it, no bolted-on game or minigame, don't confuse feedback with motivation, don't reward planning, don't ban whole families. Settled under those rules:
- **LF-03 (no generic rounded cards, glass gradients, AI-dashboard look):** in scope now. Checked by the AI-look track; present only when that track has zero open flags on cards, gradients, glass and dashboard tiles.
- **GR-15 (progression changes the experience):** Studio makes a bounded attempt using what Mark already loves, the style 7 3D objects. Each object visibly develops with sustained real practice (new form, material or detail, not a bigger number). It may only respond to behaviours done, never to observations, medication or planning. It never decays, wilts or resets on a lapse, and after a gap it simply resumes. If the attempt reads as decoration rather than progression, it stays partial with this reason; it is not faked.
- **GR-02 (never quietly reduced to animations, summaries, counters):** judged together with GR-15. Present only if the progression above exists; otherwise partial with the same reason. Adding more counters or summaries does not count.
- **GR-34 (mastery, strategy, meaningful choice, experimentation):** stays open, logged, not built this round. A real strategy or mastery loop is the unsolved gamification problem; building one inside a UI polish round would mean inventing a game mechanism unvalidated, which Mark ruled out ("don't fake it"), and he said it must not block the rest. It is shown as open with this reason on the coverage page.
Not raised with Mark: none of these contradicts an explicit ask; the only alternative to logging GR-34 open would be faking it.
- **Update ~17:52:** Studio is not deferring GR-34. It cites Mark's "EVERYTHING I have requested" and his original mastery and strategy brief, and is building one system, "Cut" (evolve/base7/ENGAGEMENT.md), covering GR-02, GR-15, GR-28 and GR-34. Review accepts and will judge all four against it, because it stays inside Mark's rules:
  - every lever is a real routine setting, not a minigame;
  - only positive events count, and planning and "booked" cut nothing;
  - observations, medication and reduction intentions are excluded;
  - nothing decays, and trials rest during gaps;
  - readings are computed and honest about small samples.
  The ADHD and AI-look tracks will additionally check:
  - Cut adds no mandatory step;
  - the two-trial brake holds;
  - Today gains no clutter before any facet exists;
  - "Next stone" never outranks deadlines.

## 21 Oct ~18:05 · Research ledger built (494 items) and open research conflicts settled
review/20-research-ledger.md (json: review/ledger/research-ledger.json): 457 apply, 29 superseded and 8 conflicts. Every superseded or conflicting item gives the reason. Settled by Review under Mark's rules:
- **One-off intentions (EF-18):** in, but only in the small form (no due dates, priorities or overdue; a soft limit; they fade to Ideas). Mark asked for one-off reminders and for one-off activities that matter, and the small form keeps the contract's "not a task manager".
- **Partner sharing (RS-79):** not built. Mark never asked for it, and building it unasked would contradict "nothing reshaped unasked".
- **Deadline last call (RV-22 vs EF-20):** EF-20 (F-evaluation, the latest) wins. A deadline gets one optional start cue and exactly one last call. Nothing else repeats or escalates.
- **Comeback greeting (RS-25):** the return is neutral.
- **The remaining conflicts stay out:** on-device LLM wording, AI templates, NL/Siri logging beyond a plain shortcut, Meridian-originated deferred suggestions, composite sleep index, regular check-ins, contextual "ideas" headers, and Tempo reserves. Each breaks a binding rule (no LLM, direct control, no scores, no check-ins, no streaks).

## 21 Oct ~18:40 · LF-09 and LF-33 after Mark picked style 7
- **LF-09** ("I think the depth is the wrong thing we took from the apps", 20 Oct) was about the glass depth home, which confused him. "Love the 3d elements" (21 Oct 17:29) supersedes it for 3D objects. The item now reads: depth must never make it unclear what is what. It is present while each object reads as its screen's data and the controls stay plain.
- **LF-33** (never copy an app's appearance): Mark picked a style informed by Opal and NB Weather. The bar is "informed by, not cloned". Objects, geometry and data mapping must be Meridian's own (Cut stones, real routes); a literal copy of Opal's gem, colours or layout is a flag.
- **Guardrail on round 1 fixes:** shrinking the stage (ADHD X-01) or moving cards off it (AI-look B-01) must keep each screen's 3D object as its hero, at least about 180 pt tall on Today and routine pages.

## 21 Oct 21:52 · Mark rejected Cut
Mark: "Indont like this lets skip" (about the Cut gamification). Studio is removing it from the final build. GR-02, GR-15, GR-28 and GR-34, and any other engagement-mechanism items, are DEFERRED BY MARK. They are not open gaps and don't block sign-off, and the coverage page shows them as deferred with his quote. Any Cut leftovers (stones with facets, Way, trials, levers, Next stone, Hold to cut) are flags. Cut stays as evidence: rejected.

## 22 Oct ~02:45 · Research ledger round 2 triage
On build 8779159e the 457 "apply" items came out as 274 met, 115 partly, 55 not met and 13 that can only be judged natively. Every partly or not-met item is now either required for Studio or logged as not applied, so none is silently lost (research-ledger.json, field `not_applied`).
- **Required (98):** applied in the next pass, listed in review/19-final-ui-r2.md.
- **Not applied, unasked new optional features (58), kept for a later round.** Examples: AlarmKit opt-in, a stop-point mode, Shortcuts/NFC moments, opportunities tied to place, multi-point deadlines, a craft layer, an energy tap, sampling weeks, behaviour experiments, patina, chapter captions, pinch-zoom history, drag-to-time logging, a shared cadence axis, mute/pin of patterns, co-shift markers, a monthly checkpoint cadence, learned defaults. The reasons: OT-28 (nothing reshaped unasked), the ADHD rule of minimal decisions, and the fact that most are ef-support D-experiment candidates rather than settled findings.
- **Not applied, conflicts with Mark or the contract (3):**
  - EF-62: Mark made contextual opportunities a requirement, so cadence-based suggestions stay. They must never read as tasks or as due.
  - AN-17 and EG-53: contract RS-08 and HS-01 keep an optional, transparent, non-medical sleep summary score. WHO-5 is a validated instrument that Mark opted into.
- **Native-only (11):** haptic vocabulary, Control Center, complication rendering modes, Focus/summary warnings, permission fallbacks, renderer disposal. These go into the SwiftUI handoff spec.
- **Nuances on required items:**
  - Relationship and enjoyable routines (EG-50, RS-13, RS-15, EG-52) keep Mark's own target, such as twice a month, because the target model is his. They lead with rhythm and memories, show the count second, and get no milestone counts like "15 dates".
  - Milestones stay because Mark asked for them (HS-31, RS-16). They are drawn as plain timeline lines, not a badge shelf (EG-02).
  - Layers off by default (EF-48) applies to a fresh install. The demo scenarios may show them switched on.

## 22 Oct ~03:00 · Round 2 calls
- **Stones stay; Cut mechanics go.** The stones were in style 7 when Mark picked it ("Love the 3d elements"), so they aren't Cut leftovers. Only the facets-earned mechanics and copy are. The holographic pastel material becomes single-hue (no-pastel rule), and the faceted gem used as an icon goes.
- **Onboarding Welcome gem is replaced.** It is near-identical to Opal's signature image, which breaks LF-33. It becomes the routines picked in onboarding, one stone each.
- **Route height = altitude.** Mark asked for a 3D map of the walk, and heart-rate height hides the terrain. Pace stays as the shade.
- **The access map is corrected on LG-11.** Its own rule 11 (observations never on Today) wins.
- **Settings pages may stay plain** (no stage), because a stage there would be decoration. Time Months and Weeks get a data object.

## 22 Oct ~06:30 · Relationship routines keep their progress (correcting my r2 nuance)
In round 2 I wrote "no '15 dates' milestones" for relationship routines (from research EG-50 and RS-15). Studio applied it, and the r3 check shows GR-39 dropping to partial. GR-39 is Mark's own ask: meaningful positive progress for relationship routines. His ask wins over research. The fix:
- Restore Growth and milestones on Date night, Call parents and Friends, framed around the relationship ("First 2-date month", "10 dates since January").
- Never a rating or a quota scolding.
- Keep the rhythm and memories lead and the optional keepsake.
- Counts stay visible, not hidden behind a collapsed row.

## 22 Oct ~07:00 · Mark's targets and milestones win over research EG-50, EG-52, EG-59, TS-92
Research says to drop quotas and milestones around relationship and enjoyable routines (EG-50, EG-52), to drop empty target slots (EG-59), and to drop quantity milestones (TS-92). Mark asked for:
- any frequency target, including twice a month (the date test case);
- meaningful positive progress for relationship routines (GR-39);
- kept personal records and milestones (HS-31);
- kept scores, goals and statistics he enjoys (HS-35).

His asks win. So:
- Targets, counts ("1 of 2") and milestones stay on every routine, including Date night, Guitar and Water.
- For relationship and enjoyable routines they are worded warmly and follow the rhythm and memory lead. They are never a scolding quota, never "days left" pressure on the hero, and never a rating.
- Empty target slots may stay as quiet outlines, but they must not read as missed.

These four research items are marked "conflicts with Mark" and are not applied in full.

## 22 Oct · round 3 calls (build 6e7b6bf7)
- CG-03/IN-32: rhythm rows keep no ratio (RS-13/15); late in period (last 7 days, aim unmet) the row adds neutral "N days left in <month>". Count stays on item page and Log. Access map detail updated.
- "Didn't do it this month" kept on rhythm routines: Mark separates didn't-do from not-recorded. Research A's drop suggestion declined.
- IP-12/13 Screen Time worked example: restore as collapsed "How it would work" sample; counts as present for the prototype.
- RS-05/RS-11 vs RV-06: both hold. Report leads with timing vs usual, stages (named, estimated, with shares) and HR curve follow, also in the flat fallback.
- AL3-01 palette: same hue families, deeper matte/jewel tones. No new hues (evolve, don't reinvent).
- Faceted stage stones stay (style 7, pre-Cut), single-hue.

## 22 Oct · round 4 calls (build 5f52d7ee)
- Count targets keep their ratio ("1 of 4", Mark's targets); "N days left" only late in period, same rule as rhythm rows (CG-03). RS-13/15 partly on Date night item page accepted (count stays there per r3).
- Session stones: one per session (OP-12) rendered as style-7 pebbles, this week lit, earlier matte; heights from zero vs fixed reference (BD-11 honesty) not per-routine min-max (AL4-01 vs OP-12 reconciled).
- Settled tokens stay jewels but lose ring + check badge (AL4-04).
- Records show "None logged" not "0" until confirmed (missing ≠ none).

## 22 Oct · round 5 calls (build d32ad1f3)
- Sign-off gate split: BLOCKING (defects, honesty, lost work, unmet research, visible AI tells) must be fixed; POLISH does not gate sign-off.
- OP5-05 "none without": fix by not claiming a comparison, never by counting unlogged days as "without" (missing ≠ none).
- RS-12: rhythm vs count feedback becomes a per-routine choice (create + settings); routines are generic, seeds can't be special.
- RS-15/CG-03 applies to every overview row (Today, Routines list): rhythm routines show last time (+ days left late); count only on item page and logger.
- AN-09: "I note it every time" records its start date; only later days count as none.
- AL5-04: Welcome uses the app's own year ring object (evolve style 7), not generic pebbles.
- X3-10 far dated items: on glance surfaces only within 7 days; access-map exception recorded.
- OP-22 merge (Studio) accepted.

## 22 Oct · round 6 calls (build 2ef0c482)
- r5 item 8 remainder accepted: Next up widget and Lock Screen show one nearest date by design (BD-29/30); Today carries the full window. "+1 by Sat" hint is polish.
- Open periods (current week/month/year) get no comparative verdict ("quieter than usual"); "so far" values only.
- Retired routines count only to retirement; post-retirement weeks are neither gaps nor unknown; no "Next milestone".
- Windowed items (time window on a given day) join Now on their day only; before that they sit on the "By a date" line.
- Short names (e.g. "Stretch") only on Routines columns; full names in sentences, toasts and history.

## 22 Oct · round 7 calls (build 120797f2)
- Today hero superseded by Mark 11:48 ("why is run now the thing exposed on home page?"): 24 h day ring, routines equal, workouts/sleep as news lines (Studio pass 3f).
- Set-aside periods are a distinct state from "nothing recorded" on every chart + legend; entries inside them stay visible.
- Open-period captions describe content, never recording volume, never a verdict (HS-24 never rule + r6 decision).
- Starting something while a session runs switches sessions in one tap; never silently ends one; Undo restores.
- Round 8 is targeted (5 blockers + Today on 3f + regression diff), not a full fresh pass.

## 22 Oct ~12:55 · Today criteria after Mark's 12:50 asks (relayed by Studio)
- Mark: "I liked that horizontal cards, where observations weekly recap etc went into" → Moments carousel returns under the hero; Today first screen standard relaxed from ≥3 to ≥2 whole Now rows (his ask overrides the review criterion).
- Mark: "Current observation display is just bad" → observation cards with small comparison chart, day count, "a hint, not proof" (honesty rules still apply: missing ≠ none, no causal claims, no verdicts on open periods).
- Later becomes a practical "rest of today" rail.
- Today hero: back in lab after Mark "Yeah this just looks weird"; acceptance criteria sent to Studio (one data source, nothing singled out, count all entries, flat = 3D rules, readable, workout/sleep as chip/news not stage row).

## 22 Oct · round 8 calls (build e8c613ec)
- Today hero findings on 3f (T8-01/02, TH8-01, B8-01) are not gated: the hero is being redesigned on Mark's word; they become acceptance criteria for the port.
- Round 9 is targeted: HON8-01, HS-24b, ported hero, 3h Today changes, regression diff; sign-off if zero BLOCKING.

## 23 Oct · round 9 calls (build 0a0b1f3c, timeline hero)
- Hero criterion 1 (≥2 whole Now rows) is judged at standard text size at any time of day; at 135 %/22 px one whole row plus scroll is acceptable (T9-01 → polish).
- Glass, light and glow in the Today hero are Mark's pick ("I think timeline", 23 Oct); judged on execution only. Boxed cards on Today are an unmet ask (Mark 22 Oct 19:11 "Also the cards you added just look ai slop").
- Observations and medication appear in the hero's count and label but are drawn quiet (grey, no rise/shimmer/flash): counted, never rewarded.
- Round 10 is targeted: 6 BLOCKING + hero criteria + Today regression diff.

## 23 Oct · round 10 sign-off (build 2e5157ee)
- Signed off: 0 BLOCKING. The 15 POLISH items in coverage-data.json known_polish do not gate. Studio's own not-done list (L9-02, HON9-05, X6-05, HON9-03/04, the September disc, RL-05/09, A6-01, L7-01) is all POLISH.
- RS-66 (one next step stands out) stays partly: Studio left it to Mark, and it does not contradict any ask.

## 23 Oct · flow and sense-check round (build 2e5157ee; findings 21-flow-findings.md)
- Mark's 09:51 questions were treated as questions, each with a researched decision: Q1 stretching becomes Done or not; logging follows the measure type; "With others" stays out of the moment row. Q1b no morning card. Q2 dated weekly item via "Something with a date". Q3 meals: one tap, no size; milestones count days at target. Q4 Plan the week removed (sample only, rewarded planning). Q5 pebbles become LightGlass, evolving his pick. Q6 first step stays optional user text, asked once. Q7 no categories; the object follows measure + unit.
- Generic rule: no feature may select by routine id, scenario or day of year; select by fields and first use. Seed-only paths that real data can't produce are BLOCKING.
- D1 Later fold rejected (Mark's 12:50 ask for the Later rail). D8 "Now as a day line" removed and Mark told.

## 23 Oct · round 11 calls (build aac8cadc)
- D10 corrected: no "Coming later" page (OT-18 forbids coming-soon placeholders). Screen Time's sample returns to Connections; Shared routines is hidden until it exists.
- LightGlass uses the Today shader where WebGL exists (Mark's love of the 3D elements, LF-39). SVG is the fallback only.
- A dated chore and a routine are alternatives, not a pair; "Give it a date instead" converts (polish).

## Round 12 (23 Oct, build 8a9c17ba)
- **KD-20** (shared routines as a possible future capability) is now native-only, with no UI. OT-18 bans coming-soon placeholders, and Mark's quote treats it as a future capability. The data model keeps routines per-person, so it can be added later.
- **The arriving card regression** is BLOCKING. An arrival outranks "newest first" in the card rail, because L9-01 requires the arriving card to be visible.
- **LightGlass in WebGL must read the same as the flat SVG** (heights, set-aside frost). The shader can't hide data.
- **Pictures across all item types** frost set-aside and paused periods (the r7 rule applies to the new pictures too).

## Round 13 (23 Oct, build 37f13531)
- "I note it every time" confirms a period only when every day in it is a recording day (the user recorded something in Meridian that day). This follows COV_TEXT and `knownWithout`. A day with no record of anything stays unknown, even with every-time on (missing ≠ none).
- Duration chips: only a duration target is in minutes. A session count target never sets minutes.

## Chore gate (23 Oct 17:50, Mark: "why have it? The app becomes a chore")
- Every toggle, setting, choice or explanatory line is a finding unless removing it would break one of Mark's explicit asks or a contract item. Each one is asked as a question, not removed by a blanket rule.
- Sleep "Show a summary score": remove the toggle, but keep RS-08 and HS-01 (a transparent, qualified summary or score). The summary is always shown in plain words, or the score is dropped and the summary sentence stays. Either way, nothing is lost silently.
- Chore audit 5c: the per-routine feedback lens (rhythm vs count) is no longer a user choice. It is inferred at save time (weekly-or-longer event/confirmation routines with an aim of 2 or fewer use rhythm). This overrides the round 5 "per-routine choice" decision: Mark's chore ask beats the research item RS-12's "changeable". RS-12 is now partly met, with that reason logged. GR-39 is still met.
- Round 16 chores: remove the Reminders preview chips, the Reminders explainer and helper lines, the long Suggestions explainer (cut to one line) and the Screen Time "Tell me when it works" toggle. Keep the quiet-hours extras (IN-01) and "Show as a glass" (round 11). The automatic lens must re-run on every target or cadence save, and applies only to week and month cadences.

## screens-v3 deliberate drops (24 Oct, checked against the ledger)
- **Routine colour per routine: drop accepted.** It fits the v3 look Mark approved, and no ask of his names it.
- **Routine glyph and the icon picker: must stay**, as a flat line glyph.
  - It was a logged flow-round decision (E13: icon picker next to Colour).
  - It is the main scanning aid for 15+ routines (ADHD glanceability). GR-35 creative agency is otherwise partial.
  - The picker moves next to Name.
- **"Show as a glass": drop accepted.** v3 has no objects, so the Q7 water-glass-on-push-ups problem no longer exists.
- **Sleep score: restore** as a transparent, qualified, non-medical summary out of 100 (RS-08, HS-01, HS-35; 5c chore audit).
  - Time's "nothing is graded" note is overruled.
  - Keep "how it's worked out" and "not a health measure".
- **Caffeine estimate by familiar drink (LG-09): must have a home.** The drink list on the Observations page shows the estimated mg per drink, and the caffeine results show the day's estimate as an estimate.
- **Medication duplicate merge (MD-17, RS-27/28/29, LG-16): must be demonstrable.**
  - Add a sample with Health + manual within 45 min.
  - Show both sources, and offer "These are the same dose" and "Remove the duplicate I logged", with undo.
  - Never merge automatically on proximity alone (RS-27).
- **Watch and widget as plain previews: accepted**, as long as each shows the real content the native surface would (WN items).
- **IN-56 "Help with this" → Reminder + "Suggest this": accepted.**
- **"I note it every time" only on observations and no-target items: accepted.**
- **Round 17:** IN-45 restores a per-routine "Suggest this" switch in the item's Settings. That corrects my round 16 CH4 cut, which removed the only way back. "Start with 5 min" applies only until the first real session (Q6).

## Look gate update (24 Oct 12:36)
- Mark: "make it more colourful … downgraded structure again so its not easy too see what is what because worse visual weights".
- Per-routine and per-area colour comes back.
- New look-gate rule: hierarchy and visual weights must be at least as scannable as 5c (94022217). Compare side by side; anything harder to scan is BLOCKING.
- The neumorphic surface restyle is pending Mark's confirmation of neu v2. The 6b gate covers function, honesty, inventory and access only.
- **Round 18 port rule:** a restyled page may change the look, but it must carry every section the old page had unless DECISIONS logs the drop. A ledger item that gets worse in a port is BLOCKING.

## Round 20 (24 Oct)
- The word "kept" anywhere in the UI is BLOCKING under Mark's rule, even when it was missed in earlier rounds. "keep" in a question ("What would you like to keep doing?") is allowed.

## Round 21 (24 Oct)
- "keep" and "keeps" are allowed: "What would you like to keep doing?" and "Past periods keep the rule they had". Only "kept" is banned.

## Round 22 (24 Oct)
- A session stopped while under a minute does not open an end sheet, because that adds work (chore gate). It saves what happened, shown as "under a minute", and the toast offers Undo for an accidental start. No duration pick.

## Round 23 (24 Oct)
- Approved: a new resting span (Sick or Away) ends the current span yesterday, or replaces it if that span started today. The toast offers Undo, which restores both. No overlap, and no question asked.

## Round 24 (24 Oct)
- When a target is set or changed, the period in progress takes the new rule. Only finished periods keep the rule they had. A header must never read "X of 0".

## Round 25 (24 Oct)
- Rise band: text may fall below AA only while it passes through the band during a scroll. Text at rest must pass AA.
- Any button without an accessible name is BLOCKING.

## Round 25 rulings (25 Oct)
- The Appearance (System/Light/Dark) control is dropped: Ink-only look, under the chore gate.
- A new target applies from the start of the current period of the chosen type. It never defaults to "next day".
- Every tappable element must show a visible press. Tap targets must be at least 44 pt without overlapping a neighbour.
- Spacing must sit on one scale, defined in tokens.

## Round 26 (25 Oct)
- Inline sentence links are exempt from 44 pt (WCAG inline exception) if they are at least 24 px tall and do not overlap a neighbour. The 26 pt grabber is fine because the 44 pt Close covers it.

## Round 26b (25 Oct)
- Finished periods keep both the rule and the period type they had. A change of cadence never re-judges the past.

## Round 27 (25 Oct)
- When a routine changes its period type, the new type starts today, not at the start of the period. The first period of the new type reads as partial, counted from today. Finished periods keep their own type and rule.
- Two elements are exempt from the press-state rule: rows hidden under the fixed header, and the dial disc drag surface.

## Round 28 (25 Oct)
- The Time chart month keys (about 27 px wide, tiling the chart) are accepted if each one is at least 44 px tall. A mis-tap only selects a neighbouring month, which is harmless and reversible.
