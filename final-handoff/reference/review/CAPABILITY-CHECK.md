# Capability check (living)

v1.1 · 20 Oct 2026 · kept by the Review thread. It replaces `phase2a/coverage-map.md` v0.1 as the working check. The old map stays as history: its per-row trace questions still apply, and its 2A direction columns are retired. Source rows: CONTRACT v1.1.1, Mark's messages, the G-gaps from Phase 1. Checked against architecture v1 (`01-integration-review.md` §3).

**Status.**
- **Shown**: a built, touchable screen exists. Cited as a craft take, demo or evidence frame (E-nn).
- **Ruled**: v1 says where it lives and the rule it follows, but it is not yet drawn credibly.
- **Open**: a design question that is still unresolved, numbered as in 01 §4 (Q1–Q6).
- **Conflict**: contradicts the contract. None are open at v1.

**Fid** follows Mark's 10:54 §2: HF is core and frequent, CF is complex but less frequent, SP is technical.

**Counts, v0 → v1.** v0 was traced on 79 rows: 15 covered, 38 thin, 21 missing and 5 in conflict. v1 merges those into 70 rows: **Shown 21 · Ruled 35 · Open 13 · Pending Mark 1 · Conflict 0**. "Ruled" is not "designed". It means the row can no longer get lost. Eight of the 13 open rows wait on one question, Q1: what the home is for.

## How this check is used (from 20 Oct 17:33)
Review no longer gates rounds before Mark. Studio evolves the 18 Oct whole-product prototype (whole/) and shows each step to Mark directly. Review runs this check alongside and sends gaps straight to Studio. It goes to Mark only when a gap forces a real trade-off.

## Gate 0: what is what (retired as a gate; a screen for obvious failures only)
In a cold read, a fresh agent with no project context must say confidently, for every state and action on each key screen (navigation labels may be learned), what it is, whether it is done, to do, running or information, and what tapping it does. This only screens out obvious failures. It twice passed screens Mark couldn't read (20 Oct), so it never stands in for him. Order: cold-read screen, then Mark's look, then the hard set. Added 20 Oct (review/10, review/14).

## The hard set (tested on every round before Mark sees it)
Mark, 20 Oct 06:25: he worries that a design he picks won't fit everything, or that functionality gets forgotten. So every design round is driven against these before it reaches him. The presenting message names the ones tested, in one line. Nothing is dropped without his word.
1. **Scale.** 30 configured with 10–25 alive, every alive item reachable in one step, and 60 configured staying calm (R-02/AS-12, R-19).
2. **Fast log and undo** for an amount, a done and a session, plus a five-log morning burst with its taps counted (R-11/AS-01).
3. **Kinds and honesty.** Observations and medication get no reward, excess dims, every figure has one meaning, and recorded is distinct from unknown (R-08, R-22, R-09).
4. **An import arrives** and opens the report (AS-02, R-16).
5. **Time.** Day one, the return after five weeks with no backlog, and month six showing a real change (AS-11, AS-10/G-9, AS-20).
6. **Intentions.** A held intention's moment arrives, and a passed deadline is offered once (G-14, R-07).
7. **Generic routines.** Twice a month, every 6 weeks, no cadence, pause and retire, and a rule change that keeps history (R-01, R-04, R-05).
8. **Access.** 135% text, 44 pt targets, and VoiceOver actions (R-24).
9. **Privacy.** Modules switched off leave no trace, and private items stay private (AS-17).
Rounds so far: home tests 1–3 covered 1–6 and 8, but not 7 or 9. The next round must add 7 and 9.

## 1. Routines
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| R-01 | Generic routines | One record model; Add → composer | Ruled | HF | |
| R-06 | Simple creation with defaults | Add → composer with live preview of its own mark | Ruled | HF | Must show "every 6 weeks" in a few taps and no false past misses (AS-05) |
| R-03 | All measure types incl. paired values | Composer; detent per measure; paired = two detents | Ruled | HF | Blood pressure rule from BREAK 1 |
| R-04 | Cadence incl. at most / about / none | Composer; no-cadence = tally + last occurrence | Ruled | HF | |
| R-05/AS-06 | Rule change, history intact | Routine page; whole rule effective-dated; seam drawn | Ruled | CF | |
| R-05/AS-07 | Pause, retire, revive | Routine page; paused span distinct from unknown | Shown | CF | S2-A volleyball year E-02 (pause, away, sick distinct) |
| R-02/AS-12 | 60 configured, manageable | Catalog at Life's top edge; Home shows only what is alive | Shown (look open) | CF | Solved functionally by T1 Set as type (E-36); structure loved blind (taste/findings.md); surface open |
| AS-03/04 | Test set without special cases | Kind + cadence rules | Shown | HF | S2-A/S2-B years of water, volleyball, date, kettle |
| — | No bespoke gesture per routine | Gesture rules 01 §3.3 | Ruled | SP | |

## 2. Everyday use
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| R-19 | Everyday surface, quiet and busy | Home | **Open (taste)** | HF | Home tests 1–3: functional answers exist (review/04, 06, 08); Set as type structure loved in the blind taste check (20 Oct); surface open, next experiment |
| R-11/AS-01 | Fast logging, immediate undo | Tap open end on Home/Watch/widget; undo in place | Shown | HF | S1-B; must survive Home redesign |
| G-2 | Second tap meaning per measure | Amount: +1 notch; done: lifts today's record; session: stop | Ruled | HF | From S1-B/S1-C behaviour |
| R-03 | Live session, forgotten session | Session as live trace (phone, Watch, Live Activity); forgotten → end proposed from source, else asked once | Ruled | HF | Live Activity unverified |
| R-09 | Recorded / none or skip / not recorded | Explicit none/skip record, distinct mark; absence = unknown | Ruled | HF | Demo med page shows it for medication only (E-12) |
| R-09/G-3 | Correct anything: exact time, far date, typed value, import | Lift; "Exact" field; far dates via Life | Shown | CF | S1-B, demo lift E-01 |
| — | Feedback layers, hundreds of repeats | Material study in next test | Open (Q2) | HF | Not Boring lessons |
| R-22 | No push past target | No over-rim reward; fill stops at rim, excess shown plain | Ruled | HF | Removes v0 build-brief rule |

## 3. Imports and reports
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| AS-02 | Imported workout counts toward a routine; unlink, reassign | Arrival on Home; record shows "counts toward"; lift → reassign | Ruled | HF | |
| G-5 | Dedup and separate a wrong merge, everywhere | Merge candidates where they arrive; separate from the record | Ruled | CF | Shown for medication only (E-12) |
| R-16 | Workout report | One-cursor report | Shown | HF | S3-B E-04 + S3-A drawing E-05 |
| G-4 | Sparse report (manual run, no HR) | Report variant | Open (Q5) | CF | |
| R-16 | Sleep report, honest stages | Same report family, E-07 framing | Ruled | CF | Never drawn |
| R-16 | Result for a routine with no series | Routine page | **Open (Q3)** | HF | Date, kettle, call |
| R-13 | Evidence class on passive data | Trace carries source + class | Ruled | SP | |

## 4. History and progress
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| R-16 | Personal history across years | Life continuum; routine page year | Shown | HF | S2-C motion, S2-A/S2-B years |
| A2 | Year form per routine | Fold vs radial | Open (A2) | CF | Mark's eye later |
| G-15 | Density not mistaken for success | Zoom aggregates per period, not per record | Ruled | CF | |
| H-04 | Comparisons and records | Inside the figure (hairlines) | Shown | CF | S3-A E-05; non-workout routines Ruled only |
| R-20 | Real gamification | — | **Open (Q1)** | HF | |
| R-21 | No destructive streaks | No streaks exist | Shown | HF | |
| R-20/AS-20 | Never runs out; six months | — | **Open (Q4)** | HF | Month-six frame in next test |
| AS-11 | Day one | Home state | Open (Q1) | HF | Next test |
| R-19 | Depth without pressure | Home never shows analysis | Ruled | HF | |

## 5. Observations, feel, medication
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| R-08 | Three kinds, reward by kind | Kind grammar | Shown | HF | Demo E-09/E-16; S1-B coffee fill breaks it (E-06) |
| — | New neutral observation | Add → composer → marks on its line; first-day page | Shown | CF | Demo E-16 (headache) |
| — | Recording mode per observation | Composer, asked once | Ruled | CF | Default pending Mark (02) |
| P-1/AS-09 | Reduction with honest evidence | Marks + ceiling + known/unknown + optional "that's all" | Shown | CF | Demo E-09 (captioned; redraw needed) |
| — | Symptoms when noticed | Same as observation; occurrence-anchored analysis | Ruled | CF | |
| R-13/AS-14 | Feel and function, voluntary, findable | Add (module) + optional Home entry; words + "compared with usual" | Shown | CF | Demo E-14; "find in seconds" unproven |
| R-13 | Passive feel signals, classed | Trace + evidence class | Ruled | SP | |
| P-3/AS-13 | Medication: provenance, skip, timing, amount, unknown | Medication page; marks on line | Shown | CF | Demo E-12 |

## 6. Insights and context
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| R-17/AS-15 | Roles per analysis | Patterns findings | Ruled | CF | analytics/ prototype is evidence |
| AS-16 | Candidate selection by rule | Patterns primary path | Ruled | CF | Pick-two demoted to "explore" |
| R-17 | Honest uncertainty incl. undeterminable | Ladder gains "can't be determined" | Ruled | CF | |
| R-15/AS-08 | Context spans, one tap | Add → context; band in Life; return zoom | Ruled | CF | One tap from Home: Open (Q1) |
| — | Life-event notes | Record kind "note" on a band | Ruled | CF | |
| P-2/AS-18 | Screen Time | Passive trace, hourly, sleep overlap bounded | Ruled | SP | Feasibility check |

## 7. Intentions and reminders
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| R-07 | Per-routine reminders, off by default | Routine page; fading cues rule (ef-support 7) | Ruled | CF | |
| — | Reminder lifecycle, five states | Intentions experience | Shown | CF | Demo E-13 |
| — | Deadline / recurring / opportunity kept apart | Expiry by kind; distinct marks | Shown | CF | Demo E-13 (glyphs); visual distinction weak |
| — | One-off intentions | Add → intention | **Pending Mark** | CF | Default: yes, small (02) |
| — | Hold: event-anchored moment | Intention + "bring it back" | Ruled | CF | Next test shows one on Home |
| — | Start: first step, runway | Session grammar | Ruled | CF | |
| G-13 | Home not a planner | Home rule | Open (Q1) | HF | Demo's Ahead zone fails |
| G-14 | Motivation before action | Home | **Open (Q1)** | HF | |
| G-16 | Real triggers for states | Feasibility check | Ruled | SP | |

## 8. Devices
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| R-25 | Watch | Alive-now list, crown detent, live session | Shown | HF | Demo E-15, generic; A3 open |
| — | Widgets, Lock Screen, privacy | One-item log widget, next-moment card, private flags | Shown | CF | Demo E-15 |
| — | Live Activity | Session | Ruled | SP | Unverified |
| — | Notification actions | Intentions | Shown | CF | Demo |
| — | Haptics | Specified per take | Ruled | HF | |
| — | Offline, Watch-only, sync | Records carry source+ID; merge on phone | Ruled | SP | |

## 9. Onboarding, settings, access, return
| ID | Capability | Lives in (v1) | Status | Fid | Note |
|---|---|---|---|---|---|
| — | First use | Onboarding experience | Open (Q1) | CF | Depends on Home |
| — | Permissions incl. denied/revoked | Settings; revoked → unknown | Ruled | CF | |
| AS-17 | Modules off leave no trace | Hidden everywhere, kept, deletable | Shown | CF | Demo fix variant |
| — | Sensitive records private | Per-item flag | Shown | CF | E-15 |
| R-24 | Accessibility | Value strings, adjustable controls, AX rows | Ruled | HF | Demo has a VO caption mode; craft takes fail 135% in places |
| AS-10/G-9 | Return after absence | Life zoom onto the away span; passed deadlines once | Open (Q1) | HF | Next test |
| AS-19 | Sick week | Context band; no punishment | Ruled | CF | |
| — | Direct control only | Everywhere | Shown | HF | |

## Change log
- v1.3 (20 Oct): Review checks alongside Studio and no longer gates; the baseline is whole/.
- v1.2 (20 Oct): added gate 0 (cold read) before the hard set.
- v1.1 (20 Oct): added the hard set, and logged the home tests against R-19 and R-02.
- v1.0 (19 Oct): replaced the 2A direction columns with v1 statuses. Took the TRACE/BREAK findings in `integration/review/`. Pick-two Patterns was demoted. The vessel was restricted.
