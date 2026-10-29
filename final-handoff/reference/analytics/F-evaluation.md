# F. Critical evaluation

18 Oct 2026. An assessment of A–E, not approved. It is written to support decisions, not to defend the proposal.

## Verdict

The general model is credible and small. Generic candidate generation works. The honest results are mostly "not yet", "can't separate" or "changes with context", and that is the correct output for one person's observational data. The biggest risk isn't technical: a Patterns area that is truthful will be **sparse for months**, so it can't carry engagement (Workstream A) and must not be sold as an insight engine.

## Can be implemented credibly now

| Part | Why it's credible |
|---|---|
| Items, records, notes, coverage; append-only corrections; dedup groups; the person-day; effective-dated descriptors (A) | Standard event-store patterns. Small. No exotic dependencies |
| Derived variables by shape, with reliability classes (A §3) | Deterministic transforms. "Not measurable" is simply never computed |
| Rule-based candidates by domain affinity and timing (B §2) | Ran in the prototype. Generic across melatonin, headache, sauna and typed items |
| Design chosen by data shape, including case-crossover for "when noticed" events (B §3) | Established methods (Maclure 1991; Whitaker 2006) |
| Pre-period, overlap, context-assumption and leave-one-week-out checks (B §5, C §3) | Simple recomputations. In synthetic tests they caught the car period with and without a note |
| Benjamini–Hochberg plus a "too small to matter" band (B §6) | 1 false tentative in about 1,300 null comparisons |
| One-line notes with a "same thing" chip; derived time zone and body-signal circumstances (C §1) | Low effort. EventKit full access is needed for calendars, and only with Mark's consent |

## Needs more research before committing

1. **Real thresholds.** Minimum counts, "too small to matter" bands and assumption windows are placeholders. They should come from simulation on Mark's own variability (Percha et al. 2019), once real data exists.
2. **A proper within-person model.** Regression with trend, weekday and lag terms, plus partial pooling across candidates (Gelman, Hill & Yajima 2012), instead of the prototype's bootstrap contrast and hard FDR cut.
3. **Replication rule for "Holds up so far".** How much new data, and how to avoid optional stopping across monthly checkpoints.
4. **Correlated tests.** FDR assumes roughly independent comparisons. Overlapping lags and shared outcomes violate that, and the cost is unmeasured.
5. **Co-shift detection** (several outcomes leaving their usual range together). It's useful as an unexplained-period marker, but its false-alarm rate is unknown.
6. **Descriptor templates.** Are five templates enough for the things Mark actually records? Test with his real item list.
7. **Comprehension.** Whether "Already different beforehand", the four context assumptions and the dot strips are understandable without explanation. Test with Mark.
8. **Interaction with R-13** (feel and function). Sparse self-reports as outcomes inherit every problem here, plus non-random missingness (r3 §1.7).

## Where uncertainty stays, whatever we build

- **Most outside influences are never recorded.** The robustness checks catch big, concentrated ones. Diffuse ones (a hard month at work, a slow relationship strain) look like trend or noise and can't be separated.
- **Duration and magnitude of life events.** C brackets them; it cannot estimate them.
- **Selectively recorded events.** Headaches recorded only when bad: nothing can be said about the others.
- **Small true effects.** Many real but small effects (melatonin's about 7 min, caffeine's 6 min here) will never be resolvable from one person's observational data.
- **Reverse and two-way relationships** (poor sleep → more coffee → poor sleep) are only partly caught by the pre-period check.

## Should not be attempted

- Treatment-efficacy statements, dose suggestions or medication changes from personal associations (R-22).
- Composite scores of any kind (readiness, stress, focus, ADHD severity, sleep quality).
- Automatic exclusion of data, or numerical "corrections" for life events.
- Inferring severity, duration or affected outcomes from a note's text.
- Asking follow-up questions about notes, or daily check-ins to make analysis work.
- All-pairs correlation mining, or pushing a stream of correlation cards.
- Using reminder states (dismissed, opened, accepted) as behaviour or outcome data by default (A §6).
- Letting an LLM select, compute or verify anything.

## Fit with the contract and the other workstreams

- **Contract.** It satisfies R-09 (three data states, via coverage), R-15 (context with minimal admin), R-17 (roles per analysis, no all-pairs, no user-maintained questions, honest states), R-22 (no substance advice) and AS-14 to AS-17. AS-17 holds: with nothing optional enabled, Patterns still runs on routines and passive data, or shows nothing.
- **Workstream A.** Analytics should feed A only as rare, earned moments ("this became knowable", "this held up"). It can't be the engagement system. The sparse, honest output is a reason *not* to base motivation on insights.
- **Executive-function thread.** It shares only layer 1 facts (stated, imported and derived context) under A §6. No reminder state enters analytics by default. Whether notes like "car broke down" should influence suggestions is that thread's question.

## Decisions for Mark

1. **Is "honest but often 'not yet'" acceptable for Patterns?** The alternative is lowering thresholds, which produces more findings and more false ones. Recommendation: keep it conservative.
2. **Recording practice as a one-time choice per item** ("every time" vs "when I notice"). It's the one extra decision this design asks of him, at creation only. Is that acceptable?
3. **Calendar access** for imported context. It needs full read access (EventKit has no read-only mode). Opt in, or skip?
