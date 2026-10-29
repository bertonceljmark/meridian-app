# B. Analytical discovery strategy

18 Oct 2026. Research proposal, not approved. It uses the objects in `A-data-model.md`. Sources are in `sources.md`, and r3 §1 findings 10–14 (`research/r3-measurement-analytics.md`) still apply. The rules below run in the prototype's small engine (`prototype/engine.js`), so every claim about behaviour on this page was checked on synthetic data.

## The answer in one paragraph

Pairs are never written by hand, and they are never "everything against everything". A **fixed, small rule set** turns item descriptors into a short list of time-ordered candidates. A **design chosen by data shape** compares each candidate within Mark's own history. A **fixed sequence of checks** (selection, overlap, context, single stretch, chance) decides one of a few **evidence states**, and "we don't know" is a normal outcome. Optional AI can only suggest descriptors and wording. It never selects, computes or verifies.

## 1. Pipeline

```
items + descriptors ─► derived variables (by shape, A §3)
                    ─► candidates (rules §2)            ~20–40, capped
                    ─► design by data shape (§3)
                    ─► readiness gates (§4)
                    ─► checks (§5) ─► multiplicity (§6) ─► evidence state (§7)
                    ─► recomputed at monthly checkpoints, never stored as fact
```

## 2. Candidate generation: rules, not pairings

A candidate is (input variable, outcome variable, lag). It exists only if every rule holds:

1. **Role eligibility.** The input can be an input and the outcome can be an outcome. A variable that is "not measurable" is never either. Notes are never outcomes, and never inputs in automatic discovery (C §3).
2. **Time order.** The input's window ends before the outcome's window starts: evening → that night; night → next day; day → next day. The lags come only from the input's **timing profile** (A §2), so usually one or two are tried, never a sweep.
3. **Domain plausibility.** A coarse affinity table, per domain rather than per pair. For example, substance → sleep, physiology, next-day activity, symptoms; activity → sleep, physiology, next-day feel; social → next-day feel. About 6×6 cells, maintained by Meridian, not by Mark.
4. **Not definitional.** The input and outcome don't come from the same source item (steps vs. a workout's steps; a routine vs. its own follow-through), using the derivation lineage.
5. **Cap and priority.** If more than about 30 survive, keep the highest priority, which is computed from:
   - **affinity strength**;
   - **feasibility**: expected weeks to the readiness gates at the current recording rate;
   - **attention**: items Mark logs or opens often;
   - **controllability**: a behaviour beats an observation, which beats a passive signal.

   Substances and medication still enter, but they are never given priority *because* the result could guide their use (R-22).

Mark can optionally **mute** or **pin** a candidate. This is never needed, and there are no questions to maintain (R-17).

In the prototype these rules generate 24 candidates from 9 variables. They are chosen identically for melatonin, a headache, a sauna, or a "noisy night" typed by hand (step 1).

## 3. Comparison design is chosen by data shape

| Input | Outcome | Design | Why |
|---|---|---|---|
| Recorded with coverage (both yes and no known) | Continuous, per night or day | **Within-person contrast**: input days vs other comparable days. Remove the weekday-type effect, widen the interval for day-to-day carry-over (lag-1 autocorrelation) | Days are compared only with Mark's own similar days |
| Continuous (sleep duration) | Continuous (next-day steps) | **Split contrast**: his shorter vs longer half | Readable. Avoids pretending a straight line |
| Covered (sleep, workouts, closed caffeine weeks) | **Event recorded when noticed** (headache) | **Case-crossover**: the window before each event vs the same weekday 1–4 weeks earlier (Maclure 1991) | Uses only the days it happened. Never assumes unrecorded days were headache-free |
| Event recorded when noticed | Anything | **Describe only** | No known "without" days |
| Note or context | Anything | **Never automatic** | Context is a modifier (C), not an exposure |
| A behaviour as *outcome* (did the routine happen) | Prior night, prior day | Contrast on the routine's own periods | Roles swap, as R-17 requires |

A real engine should replace the bootstrap contrast with a small within-person regression: weekday type, time trend and lag-1 term, with context as covariates (Bernal et al. 2017). It should also add a self-controlled case-series variant for repeated events (Whitaker 2006). The design table stays the same.

## 4. Readiness gates (minimum data)

- Contrast: at least about 15 input days and about 15 comparable non-input days. Case-crossover: at least about 10 events with two or more control windows each. Placeholders (D-03). Real thresholds should come from simulation of Mark's own variability (Percha et al. 2019), not a fixed number of days.
- **Variation.** Both groups exist.
- **Coverage.** Non-input days count only where absence is known (A §4).
- **Recording-practice breaks.** Comparisons don't cross a detected break.
- When a gate isn't met, the state is **Building** with a time estimate at the current pace, or **Not knowable at this pace** if it would take more than six months. Neither asks Mark to record more.

## 5. Checks, in order (all generic)

1. **Already different beforehand (pre-period test).** The same comparison, with the outcome taken from *before* the input. A difference that exists before the input happened can't be its effect. It means the input was chosen in response to the situation: confounding by indication or protopathic bias (Salas 1999). A negative-control idea (Lipsitch 2010) built into every binary input. If the pre-difference persists when noted periods are set aside → **Already different beforehand**, and no estimate is offered. If it disappears, the context explains it → **Changes with context**.
2. **Comes with something else.** If 70% or more of input days are also days of another input in the same window → **Can't be separated**, naming the other one (sauna and volleyball).
3. **Context assumptions.** Recomputed under the C §3 assumption set. If the verdict flips or a tentative estimate moves more than half → **Changes with context**.
4. **One stretch.** Leave out one week at a time. If one or two weeks carry 30–40% or more of the estimate → **Mostly from one stretch**, naming the dates. Works with zero notes.
5. **Meaningful size.** Each outcome variable carries a "too small to matter" band: onset 15 min, time asleep 20 min, resting HR 1.5 bpm, steps 1,000. Placeholders. Inside the band means **No clear relationship**, whatever the p-value.

## 6. Multiplicity and forking paths

- **The family is everything evaluated**, not only what is shown. Benjamini–Hochberg at q = 0.10 across all comparisons that produced an estimate (Benjamini & Hochberg 1995). In the prototype: 22. Anything failing is shown as "No clear relationship · could easily be chance".
- **Designs are locked by rule before results exist.** Lags, windows and thresholds come from descriptors, never from what looks best (Gelman & Loken 2013).
- **Fixed checkpoints.** Re-evaluate monthly, not daily, to limit peeking.
- **Replication before "Holds up so far".** A tentative result must hold again on data collected *after* it first appeared. (Not built in the prototype.)
- **Direct exploration is outside the family.** What Mark looks up in Explore is labelled "You looked for this" and never becomes a finding unless it later appears through the rules and replicates.
- Later improvement: partial pooling of all candidate effects in one hierarchical model (Gelman, Hill & Yajima 2012) instead of a hard FDR cut.

**Calibration on the prototype's synthetic generator** (60 random histories of 20 weeks each):

| Situation | Result |
|---|---|
| No true effects anywhere (about 1,300 comparisons) | 1 false "tentative" in total. About 4% of comparisons were correctly flagged "already different", from melatonin's built-in selection |
| A true +2.6 bpm overnight HR effect after volleyball | Found as tentative in 51 of 60 histories |
| A true 3.2× headache risk after short nights | Found in only 3–4 of 60. 16 events in 20 weeks is too few |
| A true +6 min onset effect of late caffeine | Never "tentative", because it is below the 15-min "too small to matter" band. That is correct |

So the rules are conservative: few false findings, and weak or rare effects stay unknown for months. That matches r3's power arithmetic and is the intended trade.

## 7. Evidence states (fixed rules → fixed wording)

| State | Meaning | Tone |
|---|---|---|
| Building · *n* weeks | Gates not met yet | quiet |
| Not knowable at this pace | Would take more than about six months | quiet |
| No fair comparison | Design impossible (both events recorded only when noticed) | quiet |
| Not enough variation | Always or never | quiet |
| Already different beforehand | Selection; no estimate offered | caution |
| Can't be separated | Overlaps another input | caution |
| Changes with context | Depends on noted or possible periods | caution |
| Mostly from one stretch | Carried by one or two weeks | caution |
| No clear relationship | Inside "too small to matter", interval spans zero, or could be chance | plain |
| Tentative | All checks pass and it survives FDR | signal |
| Holds up so far | Tentative, then replicated on new data | signal |

Never shown: causal verbs ("improves", "causes", "triggers"), advice, composite scores, or any estimate for a substance or medication when the pre-period check fails.

## 8. Optional AI, kept separate

| Allowed (optional, confirmable) | Never |
|---|---|
| Suggest a template or domain from an item's name at creation | Select candidates, lags or windows |
| Phrase a finding from the structured result, followed by a deterministic check that every number and direction in the text matches the result, falling back to the fixed template on any mismatch | Compute, impute, or summarise values it wasn't given |
| Order the "same thing" note chips | Link notes, set context, or infer severity |

Everything in this document works with AI switched off.

## 9. Making it worth looking at (R-17: discovery as an optional reward)

- **Knowability is visible.** "Building · 6 weeks" turns waiting into anticipation without inventing anything.
- **Raw data first.** Every state, including "no clear relationship", opens to the dots behind it.
- **Rich reports stay rich.** The analytics layer adds a "related" strip to the existing run and sleep reports. It never replaces them with generic charts.
- **Patterns is a destination, not a feed.** No cards are pushed. At most, a quiet mark in Today when a state changes to Tentative or Holds up so far.
