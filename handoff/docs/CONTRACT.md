# Meridian product contract

**Version 1.1.1 · 18 Oct 2026 · status: APPROVED by Mark (13:07), with the clarifications in §0** (supersedes v1.0, v1.1)

## 0. Approval clarifications (binding, 18 Oct 13:07)

- **Provenance rule.** Many historical messages were AI-drafted prompts Mark pasted. They reflect his intentions, but wording such as "must" or "non-negotiable" in them does not by itself make an item binding. **Req** therefore protects the underlying capability or outcome. Specific mechanisms, interface structures and implementation approaches inside those prompts are **hypotheses** unless Mark explicitly endorsed them. Keep traceability, and don't ask him to audit old prompt wording.
- **Water presets:** a preference for fast logging with familiar quantities. The exact amounts are customisable.
- **No destructive streaks:** binding. Missing days never destroy accumulated progress.
- **Absence:** the 17 days were illustrative. The requirement is graceful recovery after any meaningful absence, with no punishment or backlog.
- **Evidence ladder:** scientific honesty, stated uncertainty and no fabricated correlations are binding. The specific ladder categories and their presentation are design hypotheses.
- **"Is not" list:** protects the overall identity and boundaries. It does not forbid individual features that prove useful.
- **Relationship routines** never require quality ratings. Optional extra information is allowed if a design justifies it.
- **Finite rewards:** long-term progression never depends on a finite collection of rewards. Individual achievements or badges are not forbidden.
- **Feedback fits the routine:** every routine can get appropriate progress feedback, but numerical reports or statistics are never forced onto activities where they aren't meaningful.

This file is the single authority for what Meridian must be. Every research brief, design brief and prototype cites it by version and attaches `owner-messages.md`, which holds Mark's messages word for word.

**Layers.** Only layer A binds, and within it only items typed **Req**.

- **A. Owner layer.** Each item is typed by provenance:
  - **Req** is an explicit requirement. Binding.
  - **Pref** is a stated preference. A strong default, but a design may deviate if it says so and Mark agrees.
  - **Idea** is an approach Mark proposed or floated. It is an open input, not a decision.
- **B. Research recommendations** (`E-`) are evidence-backed advice. They may never narrow layer A.
- **C. Product hypotheses** (`H-`) are creative interpretations to test. Never required.
- **D. Implementation decisions** (`D-`) apply to prototypes only.

Owner items are typed by the provenance rule in §0. Where a table row below names a specific mechanism or interface taken from an AI-drafted prompt, only its underlying outcome is binding.

Sources:

| Code | Message |
|---|---|
| `[B§n]` | Original brief |
| `[X]` | Exposures message |
| `[R§n]` | Creative reset |
| `[C§n]` | Integrity correction |
| `[M]` | Mechanisms clarification |
| `[V§n]` | v1.0 review, 12:55 |

## 1. Product identity

**Definition [C§1, V§1].** Meridian is a gamified personal well-being and routine app for iPhone, Apple Watch and widgets. It covers any personally meaningful recurring behaviour, whether physical, mental, relational, social or otherwise. No behaviour needs a medical justification.

**Priorities, in this order [V§1]:**
1. Helping Mark establish and maintain personally meaningful routines.
2. Making those behaviours genuinely enjoyable, satisfying and motivating.
3. Making progress, accomplishments and results beautiful and interesting to explore.
4. Helping him understand how his lifestyle relates to his well-being and functioning.

**Product hierarchy [V§10].** These are relative priorities, not screens, tabs or navigation sections. The experience stays coherent.

| Level | Contents |
|---|---|
| **Core product** | A satisfying, beautiful, flexible system for maintaining personally meaningful routines, with sustainable gamification and rewarding progress. |
| **Integrated experiences** | Rich results and history, sleep and workout reports, meaningful measurements, convenient observational tracking. |
| **Optional advanced depth** | Context-aware personal insights, functioning analysis, medication associations, deeper exploration of lifestyle relationships. Shapes the architecture from the start, but never overwhelms the everyday experience. |

**Anti-centrality rules [V§1, V§8, V§10]. These are binding.**
- No single measurement becomes the organising principle, main gamification system or dominant interface. That covers sleep, subjective well-being, medication, Screen Time, alcohol and any other.
- How much a topic has been discussed is not evidence of how important it is in the product.
- Examples are tests of general capabilities, never boundaries or categories.
- Products Mark enjoys are clues about mechanisms, not designs to imitate.

**Meridian is not** [B§6, B§36, X, C§1, V§1]. This is an identity boundary, not a ban on individual useful features (§0):
- a task manager, planner, notes app or productivity suite;
- a walking, sleep, ADHD-symptom or medication tracker;
- a substance-use tracker;
- a research app, health dashboard, clinical dashboard or diagnosis tool;
- a chart collection or a decorated habit checklist;
- a second game with chores.

## 2. Owner requirements (layer A)

### Routines

| ID | Type | Meaning | Implied capability | Unknowns / edge cases |
|---|---|---|---|---|
| R-01 Generic routines [C§1, V§7] | Req | Any meaningful recurring behaviour works naturally without hardcoded categories or features. Examples: a date twice monthly, a weekly social activity, an occasional longer activity, a daily practice. | One routine model with no domain-specific core logic. | Never requires a quality rating; optional extra information is allowed if a design justifies it. It is not a task manager. |
| R-02 Unlimited, manageable [B§7, C§2, V§6] | Req | No limit on routines. Routines can be active, paused or retired. Many routines stay manageable with minimal friction. No particular organising or navigation scheme is mandated. | A catalog and lifecycle. | How the everyday view scales; this is open to design. |
| R-03 Measurement types [B§7, C§2] | Req | Confirmation, event, quantity, duration, session, repetitions, passive or imported. | A measure type per routine; several logs per day. | Mixed sources without double counting. |
| R-04 Flexible cadence [B§7, C§2, V§7] | Req | Several per day, daily, N per week, weekly, monthly, custom intervals, calendar periods where appropriate, adjustable targets. Not tied to a time of day. Low-frequency and irregular routines are first-class, with no artificial daily obligations. | Cadence model of period type, target and comparator. | Periods spanning a pause, travel or a target change. |
| R-05 Lifecycle and versioning [B§7, C§2] | Req | Pause, resume, retire. Change goals without rewriting history. | Targets with effective dates; paused spans excluded. | Changing a target mid-period; reviving a retired routine. |
| R-06 Simple creation [B§7] | Req | Not an elaborate configuration workflow. | Defaults per measure type. | Covering the full cadence range briefly. |
| R-07 Optional reminders [V§6] | Req | Reminders for any routine, including relationship routines, are optional, flexible, unobtrusive and under Mark's control. No artificial urgency. | Per-routine reminder settings, off by default unless he chooses. | Low-frequency reminders that don't feel like tasks. |

### Information

| ID | Type | Meaning | Implied capability | Unknowns / edge cases |
|---|---|---|---|---|
| R-08 Behaviours, observations, outcomes [C§3] | Req | Three kinds of information coexist. **Behaviours** are positively reinforced. **Observations or exposures** are tracked or optionally reduced, never rewarded for consumption and never shamed. **Outcomes and measurements** are things to understand. The kind governs reward treatment only; in analysis an item can take any role (R-17). | A kind flag; reward logic only for behaviours and qualified reductions. | "Skipped meals" as an observation alongside "regular meals" as a behaviour. |
| R-09 Three data states [X, R§7, B§10] | Req | Recorded, explicitly none or skipped, and not recorded. Missing never means abstinence, a skipped dose or failure. Corrections are allowed; repairing past records is never required. | Tri-state values; unknown excluded from progress and analysis. | A "none" entered after the fact. |
| R-10 Exposures and reduction [X, R§2, V§5] | Req | Configurable observations with timing, amount and details where known. Familiar servings; cannabis potency unknown by default. Context matters. Not central. **Reduction intentions** are optional (decision P-1, §3). | Custom observation items with an optional at-most target. | How to gather enough evidence with little friction; to be researched. |
| R-11 Low-friction input [B§9, B§18] | Req + Pref | **Req:** fast, unambiguous, forgiving input with immediate undo. No calorie counting. Caffeine from familiar drinks with estimated amounts. Supplements without implied efficacy. Activity as sessions with type and duration, imported where possible. Short sessions acknowledged. Never encourage excess. **Pref:** familiar one-tap quantities (water defaults 150, 250, 330, 500, 750 ml; customisable). **Idea:** a quick meal confirmation. | Presets, imports, undo. | Custom drinks; duplicates between imported and manual entries. |
| R-12 Medication, optional [B§10, V§5] | Req | Decision P-3 (§3). Never defines the product identity. | | |
| R-13 How Mark feels and functions [V§2, V§3, B§14] | Req (capability) | Meridian can capture how Mark actually feels and functions, not only what he does and what devices measure. Candidate dimensions include energy, fatigue, mood, clarity, initiation, concentration, motivation, irritability, stress and overwhelm, plus others found by research. **The measurement methods, dimensions, frequency and interface are unresolved pending research.** Constraints: optional; no clinical symptom dashboard; no endless questionnaires; no imposed regular check-ins unless justified; arbitrary 1–10 ratings avoided [Pref]; no invented scores; no ADHD, focus or stress score; proxies are never treated as direct measures. | A generic optional self-report item type whose form is to be decided by research. A passive-signal layer classed as one of: direct behaviour, reliable physiology, self-report, indirect proxy, speculative biomarker, or inaccessible. | Which dimensions are distinct and valid; how much missing data analyses can tolerate; whether event-triggered input is enough. |
| R-14 Screen Time [B§15–16, V§5] | Req (feasibility pending) | Decision P-2 (§3). Keep raw usage. Distinguish usage overlapping sleep from qualified awake-usage estimates. Night playback is never read as distraction. Don't fake it; don't declare it impossible on outdated assumptions. | Depends on verification (E-11). | Multiple devices; background playback; granularity. |
| R-15 Context [B§17, R§2, C§3] | Req | Work, day off, vacation, sick, travel, unusual hours, part days, weekends, stress. Several contexts per day. Unknown stays unknown. No calendar-day rules (such as "Monday means work"). Minimal admin; no retroactive cleanup. Raw data kept; context decides which comparisons are fair. | Context as time spans, inferred or set with one tap. | Inferring travel without location tracking. |

### Results and discovery

| ID | Type | Meaning | Implied capability | Unknowns / edge cases |
|---|---|---|---|---|
| R-16 Results are rewarding [B§4–5, B§11–12, R§2] | Req | Results are interesting and beautiful. Sleep and workout feedback is satisfying and complements other apps rather than copying them. Rare and short workouts still feel worthwhile. Transparent, qualified scores are allowed. No claimed medical validity; stage accuracy is stated honestly. | Reports and comparisons for any routine, not only sleep and workouts. | What a meaningful result is for a low-frequency or data-less routine. |
| R-17 Relationships between variables [V§4, B§13, R§1] | Req | Roles in an analysis (behaviour or exposure, measurement, outcome) are per analysis, not fixed per item. Example: sleep is the outcome of the previous day and an explanatory variable for the next day. No sleep-centric model. Temporal order, confounding and missing data are respected. Scientific honesty and stated uncertainty are binding. The ladder (observed facts, summaries, tentative, stronger, insufficient, undeterminable) is a design hypothesis (§0). No manufactured correlations and no causal claims. **No user-maintained questions.** Do not test every possible pair: use defensible candidate selection, methods and thresholds (research). Custom routines are eligible when appropriate. Discoveries are an optional, increasingly useful reward, never the core. | An analysis layer over generic items with time-ordered roles. | Candidate selection, methods and thresholds are all to be researched. |
| R-18 Valuable from day one [B§13] | Req | Rewarding with little data; depth grows over time. | | The first-week experience. |
| R-19 Depth without pressure [B§19] | Req + Idea | **Req:** depth is available, and the everyday experience never demands continuous improvement. **Idea:** separate fast-everyday and deep-exploration modes. Not a mandate for tabs. | | |

### Engagement and safety

| ID | Type | Meaning | Implied capability | Unknowns / edge cases |
|---|---|---|---|---|
| R-20 Real gamification [B§20, R§4, C§5, V§7] | Req | Real actions are the gameplay, satisfying across seconds, days, weeks and months. Partial days count. Never runs out. Long-term progression never depends on a finite reward collection (individual achievements are allowed). No XP grind or in-app chores. Every routine can get appropriate progress feedback, without forcing numbers or statistics where they don't fit. Worth returning to after six months and evolves with Mark's routines. It must work, without exceptions or artificial mechanics, for: multiple times daily; several times weekly; twice monthly; a routine added mid-year; irregular travel; an observation with no consumption reward; an absence from the app; a routine that is changed, paused or retired. | Cadence-agnostic, lifecycle-aware progress semantics (§6). | The mechanism is open. |
| R-21 Psychological safety [B§18, R§7, §0] | Req | No destructive streaks: missing days never destroy accumulated progress. No punishment or backlog. Achievements survive interruptions. Graceful recovery after any meaningful absence. Honest uncertainty. Keep the scores, goals, comparisons and statistics Mark enjoys. | | Showing a missed target without it reading as failure. |
| R-22 Safety [B§10, B§20, X, R§7] | Req | Never encourage excess water, exercise, medication, supplements or caffeine. No reward for extra doses. No artificial urgency, shame, manipulation or in-app grinding. No medical or substance experiments. No medication or substance advice drawn from correlations. | | |
| R-23 Mechanisms, not imitation [M, V§6, V§8] | Req | Enjoyed products are evidence about engagement. Research the mechanisms, separate what Mark reported from hypotheses, be willing to find his explanations wrong, and look for new opportunities. Previous designs are not approved and are not reused by default. Familiar mechanics are not permanently prohibited if independently justified. | | |

### Design, platforms and process

| ID | Type | Meaning | Implied capability | Unknowns / edge cases |
|---|---|---|---|---|
| R-24 Visual quality [B§21–24, R§5, C§6] | Req | Sophisticated, mature, original, coherent, tactile and precisely crafted. Not loud sports typography, saturated game cards, endless bright panels or loud ceremonies. Not a quiet generic analytics dashboard either. Originality is structural, not loudness. Radical creativity with conservative usability, readability, accessibility and reduced motion. | | |
| R-25 Platforms [B§1, R§2] | Req | iPhone, a wrist-native Watch app and widgets. HealthKit where it is feasible and verified. | | |
| R-26 Process [B§27, R§3, C§7, V§6, V§9] | Req | Experimental prototypes may be produced autonomously. Mark's approval is required before committing to a major product direction or substantial production implementation. Research uses real sources, never invents citations, and keeps evidence, hypotheses and speculation separate. Research never narrows layer A, and not every finding becomes a feature. Research effort goes to the highest-value open questions, not to whatever was discussed most. | This contract plus `reset/03-contract-review.md` §3. | |

## 3. Decisions recorded (from Mark's v1.0 review)

- **P-1 Reduction intentions: approved with conditions.** Optional. A reduction target is shown as achieved only with sufficient explicit evidence. Two drinks logged followed by silence is **unknown**, not success. No daily abstinence confirmations or new obligations. Low-friction ways to supply enough evidence are to be researched. Consumption is never gamified; excess is never encouraged; lapses are never shamed.
- **P-2 Screen Time exclusion: not approved.** Screen Time analysis is **feasibility pending**. Before anything is claimed or ruled out, verify the following. Mark points to `DeviceActivityData.activityData(filteredBy:using:)`, enhanced family activity data access and EU authorisation provisions.
  - Supported iOS versions.
  - Eligibility in the EU and Slovenia.
  - Entitlements.
  - Signing for a personally installed app.
  - Granularity.
  - Whether Meridian's own analytics can use the data.
  - Whether it combines with HealthKit sleep.
  - Multi-device and background-playback limits.
- **P-3 Medication records: approved in principle.** Use authorised HealthKit medication data where available; local tracking otherwise. Preserve:
  - intake;
  - explicit skips;
  - different timing;
  - different amounts;
  - unknown;
  - corrections;
  - provenance and deduplication.

  Never infer a skip from missing records. No dosage advice or rewards for extra consumption. Fully optional.

## 4. Owner ideas (layer A, type Idea; open inputs)

- **Results as reward:** do something, get satisfying feedback, see an interesting result, accumulate history, become curious again [B§4]. Mark's own hypothesis, not a fixed instruction.
- **Mechanisms behind enjoyed products** that Mark proposed: mastery, strategy, short loops, tactical choice, novelty, experimentation, immediate results [B§3, R§4]. Research may show some are wrong.
- **Everyday versus deep exploration** as separate experiences [B§19].
- **Functioning approaches:** occasional concrete check-ins, behaviourally specific questions, sparing validated questionnaires, voluntary focus sessions, device activity, passive context [B§14].
- **Context sources:** work schedule, calendar, sleep and wake times, date ranges, one-tap overrides, day of week [B§17].
- **Sleep report contents:** duration, timing, consistency, awakenings, stages, overnight heart rate, trends, the previous day, a transparent summary [B§11]. **Workout contents:** heart-rate breakdown, pace, comparisons, milestones, links to other outcomes [B§12].
- **Example questions** Mark would like answered over time (exercise and sleep, caffeine timing, wake consistency, medication timing, outdoor time, meals, supplements) [B§13]. These are examples of interest, not a question catalog.

## 5. Research recommendations (layer B; advice only)

Strength:
- ● several studies or reviews;
- ◐ a single or indirect source;
- ○ weak or unverified.

Sources are in `reset/01-diagnosis-research-model.md`. Most figures there come from abstracts.

| ID | Recommendation | Strength |
|---|---|---|
| E-01 | If-then cues improve follow-through. They could be offered as optional cues. | ● |
| E-02 | Breakable streaks discourage people after a lapse. | ◐ |
| E-03 | Expected tangible rewards can undermine intrinsic motivation; informational feedback is safer. | ● |
| E-04 | Gamification effects are modest and fade. | ● |
| E-05 | Temporal landmarks raise goal pursuit. | ◐ |
| E-06 | Habit formation takes weeks to months, with large individual variation; single misses don't matter. | ● |
| E-07 | Negative sleep feedback can worsen how people feel. | ◐ |
| E-08 | Watch sleep stages are approximate; duration and timing are more reliable. | ● |
| E-09 | Self-trackers lapse and resume. | ◐ |
| E-10 | HealthKit medication doses (iOS 26) are read-only for third-party apps. | ◐ |
| E-11 | **Superseded 18 Oct (research/r3 §9).** Apple documents `DeviceActivityData.activityData(filteredBy:using:)` (iOS 26.4+, `approvedWithDataAccess` + app-and-website-usage entitlement; development install supported; EU eligible). Data reaches Meridian at hourly resolution, so sleep overlap can only be bounded. Only one app per device may hold this access, and a single unconfirmed report says Apple's own Screen Time pane stops updating. Needs a hands-on check. | ◐ |
| E-12 | Further research-layer findings (18 Oct) live in `research/r1–r4` and `research/05-synthesis.md`. They are advice only. | — |

## 6. Product hypotheses (layer C; not approved)

| ID | Hypothesis | Validation needed |
|---|---|---|
| H-01 | Lifetime accumulations that are never lost give lasting progress. | Meaningful for monthly routines. |
| H-02 | Periodic landmarks create fresh starts. | Not felt as a reset; works with an irregular life. |
| H-03 | A computed consistency estimate is useful feedback. | **Never presented as measured automaticity.** |
| H-04 | Personal records and comparisons motivate. | Appropriate for every domain, including rare routines. |
| H-05 | Optional time cues reduce load. | Only as an option; fails for anytime and monthly routines. |
| H-06 | A small focus set beside a larger catalog. | Never blocks anything outside the set. |

From the 18 Oct directions, cards, hands, seasons, broadcast feeds, timing-tower scorelines, long-exposure views and fixed daily moments are **not approved and not reused by default**. Any of them may return only through independent mechanism research (R-23).

## 7. Capability model (mechanism-agnostic)

```
Item        kind (reward treatment): behaviour | observation | outcome
            measure: confirmation | event | quantity(unit, presets) | duration | session | repetitions
                     | self-report(form TBD by research) | passive(source, evidence class)
            cadence: several per day | day | week | month | every N days | none; calendar or rolling
                     target: at_least | at_most (reduction, P-1) | about | none
            reminders: optional, user-controlled; optional cues
            lifecycle: active | paused(span) | retired; target history with effective dates
Entry       value | explicit none/skip | (absence = not recorded); time; source + provenance; dedup; correctable
Context     typed spans (multiple per day allowed); unknown by default; inferred or one-tap
Evaluation  per period against the target in force then; excludes paused and unknown; partial credit;
            reductions only from sufficient explicit evidence; never lowers lifetime accumulation
Analysis    role per analysis (explanatory | outcome); time-ordered; context-matched;
            candidate selection and thresholds by research; evidence ladder; no user-maintained questions
```

Engagement, results and analysis must be built from these primitives only, with no special cases for any example.

## 8. Acceptance scenarios

A concept passes only if every scenario works **without special-case mechanics** and **without making any single measurement the main journey**.

| # | Scenario | Pass criteria |
|---|---|---|
| AS-01 | A routine logged several times a day (e.g., water, 6 logs, at least 2 L). | Fast, undoable input. Partial days are worthwhile. No push beyond the target. |
| AS-02 | Exercise 3× a week, mixing imported and manual sessions. | No double counting. Short sessions acknowledged. A rare workout still produces an enjoyable result. |
| AS-03 | A date twice a month. | Natural to create. Monthly calendar cadence. An event with no quality rating. Progress across months. A one-date month is not a failure. Optional, unobtrusive reminders that Mark controls. History spans years. |
| AS-04 | A weekly social activity, an occasional longer activity with no fixed target, a daily practice, and something every 10 days. | All work in one model. The everyday view stays calm. |
| AS-05 | A routine added mid-year. | Fits progress and history immediately. Its earlier past isn't drawn as misses. |
| AS-06 | A target changed mid-week. | Past periods unchanged; the current rule is clear. |
| AS-07 | One routine paused for 6 weeks, another retired, a third revived. | Paused spans excluded and distinct. History kept. |
| AS-08 | Irregular travel across time zones, including a mixed work-and-travel day. | Context with one tap at most. Fair comparisons only. Not a bad week. |
| AS-09 | Reduction intention "at most 2 drinks a week": 2 logged, then silence. | The week shows **unknown**, not achieved. No daily confirmations demanded. A low-friction way to supply evidence exists. No reward for drinking, no shame. |
| AS-10 | 17 days without opening the app. | Welcoming. Nothing lost or overdue. Passive data shown; manual gaps unknown. |
| AS-11 | Day one. | Already rewarding. No fake insights. |
| AS-12 | 60 routines configured, 12 active. | Manageable with minimal friction. |
| AS-13 | Medication from HealthKit plus a manual entry for the same dose; a late dose, a different amount, a correction, unknown days. | Deduplicated with provenance. All states distinct. Never infers a skip. No rewards or advice. |
| AS-14 | **Feel and function, used occasionally.** Mark records how he feels on a few days a month, sometimes triggered by an event ("felt overwhelmed today"), then nothing for 3 weeks. | No nagging. No backlog. No guilt. Sparse data is analysed honestly ("insufficient" when it is). No arbitrary 1–10 ratings unless research justifies them. |
| AS-15 | **Roles swap.** Previous-day behaviours vs sleep; sleep vs next-day energy; a weekly social activity vs mood. | The same items take different roles over time-ordered windows. Confounding and missing data handled. No causal claims. |
| AS-16 | **Candidate selection.** A new custom routine reaches enough data. | Becomes eligible for analysis by defensible rules, without all-pairs searching or questions for Mark to maintain. |
| AS-17 | **Core without depth.** Mark never enables medication, feel-and-function input, Screen Time or exposures. | The core routine experience is complete and fully rewarding. Nothing appears missing. |
| AS-18 | **Screen Time unavailable vs available.** | Unavailable: everything else works and the product says so plainly. Available: raw usage is kept, sleep-overlapping and awake estimates are qualified, and night playback is never read as distraction. |
| AS-19 | **Sick week** with most routines missed. | No punishment; context recognised with little admin; progress intact. |
| AS-20 | **Six months of mixed use.** | Something has developed that's worth seeing. Nothing runs out. No grind. Sleep is not the dominant journey. |

## 9. Next research agenda (after approval) [V§9]

Mechanism-first and consequential. Findings are synthesised into product decisions, not a report per topic. The agenda:
- maintaining meaningful routines over time;
- sustainable motivation and intrinsically rewarding interaction;
- engagement mechanisms (novelty, mastery, agency, competence, discovery) and their harms;
- physical, mental and social well-being;
- relationships and infrequent positive routines;
- feel-and-function measurement (R-13);
- credible passive signals, classed as in R-13;
- personal analytics methods and candidate selection (R-17);
- low-friction reduction evidence (P-1);
- Screen Time verification (P-2);
- perfectionism and missing data;
- original interaction design.

Sleep and ADHD get no more effort than their share.

## 10. Implementation decisions (layer D; prototypes only)

- **D-01** Artifacts are single-file React with synthetic data.
- **D-02** The 18 Oct dataset and its 8-step journey are retired as design inputs.
- **D-03** All weights, constants and thresholds used so far are placeholders.
- **D-04** Prototype scenario sets come from §8 and must include monthly, paused, retired, non-health, sparse self-report and day-one cases. Examples may not make up most of a set.

## 11. Unresolved owner decisions

None. U-1 was resolved by §0.

## Change log

**1.1.1 (18 Oct 2026):** approved. §0 added: the provenance rule and U-1 outcomes, plus three corrections covering relationship ratings, finite rewards and appropriate feedback. R-11, R-17, R-20 and R-21 adjusted to match; §11 closed.


**1.1 (18 Oct 2026):**
- **Identity:** priorities restated in Mark's order; product hierarchy and anti-centrality rules added (§1).
- **New R-13** replaces the narrow functioning item. It covers how Mark feels and functions, with methods unresolved.
- **R-17:** analysis roles are per analysis; no all-pairs searching; custom routines eligible.
- **Decisions recorded:** P-1 approved with conditions; P-2 rejected, Screen Time feasibility pending, E-11 marked possibly outdated; P-3 approved in principle with provenance and deduplication.
- **Prescriptive items removed:** the reminder ban (now R-07, optional reminders); the relevance-ranking mandate; the "only if Mark asks" rule on past mechanics; approval before every experiment; automatic analysis of all routines.
- **Attribution:** items now typed Req, Pref or Idea, with owner ideas collected in §4.
- **Acceptance scenarios:** expanded to 20, adding feel-and-function, roles, candidate selection, core-without-depth and Screen Time cases.
- **Research agenda:** §9 added.

**1.0 (18 Oct 2026):** first contract.
