# A. Data architecture

18 Oct 2026. A research proposal for Workstream B. Nothing here is approved, and it changes no existing file. It refines contract §7 (Item, Entry, Context, Analysis); it does not replace it.

## The model in one paragraph

Meridian stores **facts** once and derives everything else. There are four stored things: **items** (what can be recorded), **records** (each real-world occurrence or measurement), **notes** (one-line context, optionally linked into a thread) and **coverage** (when silence means "none"). Routine progress, Time, reports and Patterns are all **views computed from the same records**, so one volleyball session counts for the routine, appears in the month, feeds the workout report and can be an analysis input without being copied. Analysis variables, candidate relationships and findings are **derived and recomputed**, never written back as facts.

## 1. Stored objects

| Object | Holds | Notes |
|---|---|---|
| **Item** | name, *kind* (behaviour, observation, outcome; governs reward only, R-08), *shape*, *descriptor* (§2), optional cadence and target, lifecycle | Effective-dated versions: target, unit, recording practice. Changing any of them never rewrites history (R-05). |
| **Record** | item, time, value, state, source, provenance | One per occurrence. Append-only: a correction is a new record that supersedes the old one, and both stay. |
| **Note** | short text, time, optional thread link | Context the person chose to write. Never scored. See C. |
| **Coverage** | item, interval, how it is known | The only thing that turns "nothing recorded" into "none". See §4. |

### Record fields

- **time**: an instant or an interval, stored as UTC plus the UTC offset at the time, plus *time precision* (exact, about, "this evening", "some time today"). Records entered later keep their real time and an `entered_at`.
- **value**, by shape:
  - event: nothing, or an end time;
  - quantity: number and unit;
  - duration or session: start and end;
  - repetitions: count;
  - self-report: whatever form R-13 research settles on;
  - passive: the source's own sample.
- **attributes** (optional, generic): onset, end, "still going", location label, free words, and up to a few *item-defined* fields (for example "temperature" on a sauna item). Attributes are never required to save.
- **state**: value, explicit none, skipped, or (by absence) not recorded (R-09).
- **source**: manual, Watch, HealthKit (with the sample UUID), calendar, derived. **Provenance** keeps the chain: "imported from Health, corrected by hand on 4 Mar".
- **dedup group**: records from different sources that describe one occurrence (a HealthKit dose and a manual tap; a Watch workout and a manual "volleyball") are grouped, with a preferred source per item. Analysis and progress read the group once.

### The person-day

"Day" and "next day" are defined relative to sleep, not midnight. A day runs from one main wake to the next. When there is no sleep data it falls back to 04:00 local. Each record also keeps its local date in the time zone where it happened. A change of UTC offset creates a derived *travel* context automatically (§5), with no input.

## 2. Descriptors: the semantic metadata that makes discovery generic

Each item carries a small descriptor. Defaults come from the shape and from a fixed built-in **template** chosen at creation ("something I take", "a symptom or something I noticed", "an activity", "time with people", "something in my surroundings"). Mark never edits a descriptor unless he opens advanced settings.

| Field | Values | Used for |
|---|---|---|
| **domain** | substance, activity, social, symptom, rest, environment, work, place, other | Which outcome families are plausible (B §2) |
| **timing profile** | moment (minutes to hours), that night, next day, a few days, cumulative (weeks) | Which lags are tested. Usually two, never all |
| **recording practice** | passive (device), every time, when noticed, occasional | How absence is read (§4) and which comparison design is possible (B §4) |
| **use pattern** (substances, symptoms relief) | regular, when needed | *When needed* marks a likely **selection by indication** (B §5) |
| **can be an outcome / an input** | both by default; notes never outcomes | Role eligibility, decided per analysis (R-17) |

Optional AI may *suggest* a template from the item's name. The suggestion is a pre-selected chip Mark can change, and the descriptor is stored only when he saves. No model ever computes a value, chooses an analysis or writes a finding.

## 3. Derived variables (computed, never stored as facts)

Analysis never reads records directly. A fixed set of **transforms by shape** turns records into per-window variables, so a new item gets variables without new code:

| Shape | Variables | Window examples |
|---|---|---|
| event | occurred (yes / unknown, or yes / no under coverage), count, first time, duration | evening, person-day, 3 days |
| quantity | total, last time, time relative to sleep onset | person-day, after 14:00 |
| duration, session | total minutes, ended-before-sleep gap | person-day |
| passive sleep | asleep duration, onset clock time, wake time, mid-sleep regularity, wake-ups | night |
| passive physiology | overnight resting HR, HRV, wrist temperature deviation from own baseline | night |
| passive activity | steps, exercise minutes, daylight minutes | person-day |
| routine | period follow-through (done / not done / unknown) | the routine's own period |

Each derived variable gets a **reliability class** from R-13: direct behaviour, reliable physiology, self-report, indirect proxy, or **not measurable**. Only the first three can be outcomes in automatic discovery. Proxies are shown only with their label (for example, sleep stages). "Not measurable" variables are never computed: time to fall asleep after getting into bed, sleep quality, ADHD severity, effort, focus, stress.

## 4. Absence, coverage and recording practice

Absence of a record means **unknown** unless a coverage interval says otherwise. Coverage comes from four places, cheapest first:

1. **Device wear.** Dense heart-rate samples imply the Watch was worn, so an absent workout or sleep in that window is a real absence.
2. **Recording practice "every time"**, chosen once on the item (effective-dated). Analysis uses it, but still shows it as an assumption.
3. **A closure.** "That's everything this week", already designed for reduction goals (P-1).
4. **An explicit none** record.

*When noticed* items (a headache) have **no coverage by default**. Their unrecorded days are never treated as headache-free, and the analysis designs in B §4 work without that.

**Recording-practice drift is detected, not asked.** When an item's record rate changes abruptly (for example caffeine went from about 2 a day to about 0.3 a day), the series is split there, and comparisons don't cross the break. It shows in the item's history as "recorded less often from 10 May". No question is asked.

## 5. Context: three kinds, kept apart

| Kind | Example | Status | Comes from |
|---|---|---|---|
| **Stated** | "My car broke down", "Sick", "Trip to Vienna" | Fact that it happened. Its effect is unknown | A note or the existing one-tap context |
| **Imported** | All-day calendar event "Vienna", public holidays, a flight | Fact from a source Mark enabled, labelled with the source | Calendars he chose (EventKit full access) |
| **Derived** | Time zone change; wrist temperature and resting HR well above his own baseline; several outcomes shifting together | **Possible** circumstance, never asserted | Deterministic rules on his own data |

A derived circumstance is shown as "Body signals unusual", never as "sick". None of them excludes data on its own. How analysis uses them is in C.

## 6. Boundary with contextual support (Mark's §15)

Five layers of information. A layer may read the ones above it, but never writes into them.

| Layer | What it is | Example | Rules |
|---|---|---|---|
| 1. **Known facts** | Records and stated or imported context | A workout, a dose, "car broke down", a calendar trip | The only things counted as activity |
| 2. **Possible circumstances** | Derived context | "Away from home time zone", "body signals unusual" | Always labelled as possible. Never suppresses an obligation or a deadline |
| 3. **Findings** | Recomputed analysis results with an evidence state | "Later nights after evening caffeine; tentative" | Never stored as facts, never shown as advice |
| 4. **Intentions and suggestions** | Plan objects from the executive-function work: commitment, intention, idea, requested reminder | "Flowers on the way home" | Chosen, begun, dismissed, opened: none of these is a record. Owned by the EF thread |
| 5. **Delivery** | Notifications, widgets, Watch | | Opening a reminder is not evidence of acting |

Five consequences:
- **A missed suggestion is not a missed routine.** Routine follow-through is computed only from records in layer 1.
- **An accepted intention is not activity.** It becomes activity only when Mark logs it in the usual way, or a passive record matches it.
- **Dismissals are not data for analytics.** "Not now" at 08:00 says nothing about wanting the activity. Analytics never reads layers 4 and 5 by default. If follow-through on suggestions is ever studied, it needs Mark to switch it on, and it gets its own clearly named variables.
- **Shared context, separate decisions.** A stated trip is one fact in layer 1. The EF layer may use it to choose what is realistic to suggest. Analytics may use it as a sensitivity assumption. Neither changes what the other does.
- **No reverse flow.** A finding never generates a suggestion about medication or substances (R-22). Whether any finding may ever feed suggestions is the EF thread's question, and needs Mark's decision.

## 7. What was deliberately left out

- A general graph of events with typed causal links. Notes link in one way only, to a thread.
- Severity, impact or duration fields on context.
- A per-item analysis configuration screen.
- Composite scores of any kind.
- Storing derived variables or findings as truth. They are caches.
