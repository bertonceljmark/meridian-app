# D. End-to-end demonstrations

18 Oct 2026. Every number below is computed by the prototype's engine (`prototype/engine.js`, seed 4) on a synthetic 20-week history (1 Jun to 18 Oct 2026). Open the matching step in the prototype to see it: https://claude.ai/artifact/18qy1PiyQwjWe3B8exqgV4. None of the four examples uses item-specific code. They differ only in their descriptors.

## D1. Melatonin, taken occasionally (prototype steps 1, 2, 7)

**Create.** Log › New › "Melatonin". The template is "Something I take", which sets domain *substance*, timing *that night, next day*, kind *observation* (neutral, never rewarded). Then shape: amount (mg); taken: **when needed**; recorded: every time. That's four taps, or zero beyond the name if the defaults fit.

**Record.** One tap logs the last amount (1 mg) at the current time; both can be changed afterwards. Provenance is "manual". A HealthKit medication record for the same dose would join the same dedup group (A §1).

**What becomes eligible, by rule:**
- that night: falling asleep (clock time), time asleep, overnight resting heart rate;
- next day: steps, and a recorded headache (case-crossover);
- next-day feel, only if Mark records any.

**What is shown as not measurable:**
- *How long it took to fall asleep after getting into bed.* Apple's sleep data has no reliable in-bed start without Mark marking it, and Watch "awake" samples only occur *between* sleep periods (Apple HKCategoryValueSleepAnalysis).
- *How well you slept.* Quality is not a Watch measurement.
- Sleep stages exist, but they are proxies (deep sleep underestimated by about 43 min in Robbins et al. 2024), so they are never automatic outcomes.

**What the analysis says:** 17 melatonin evenings vs 88 comparable ones.
- That night: onset +14 min later (−1 to +32).
- **The night before:** +35 min later (+20 to +51).

Melatonin was taken on nights that were already going badly, so the state is **Already different beforehand**: "This can't show what melatonin did." Meridian offers no estimate, no "works or doesn't" statement and no dose suggestion.

**Why that's right here:** the meta-analytic effect of melatonin on sleep latency is about 7 minutes (Ferracioli-Oda 2013). One person's observational nights will almost never resolve that against selection. The honest ceiling for this example is a description of when Mark took it.

## D2. An occasional headache (prototype steps 1, 2, 8)

**Create.** "Headache" → "Something I noticed": domain *symptom*, shape event, recorded **when I notice**. No daily question, ever.

**Record.** One tap logs "started now, still going". Optional afterthoughts are "started an hour ago" or "since this morning", and later "it's gone", which closes the duration. No severity is required. If Mark ever wants one, a generic attribute could map to HealthKit's headache type, which has severity levels.

**How absence is handled.** No coverage, so unrecorded days are unknown, never headache-free. That rules out "days with vs without a headache" comparisons. Instead:
- **As an outcome:** case-crossover. Each recorded headache is compared with the same weekday 1–4 weeks earlier, for covered inputs: sleep, late caffeine (caffeine is recorded every time), volleyball, sauna, melatonin.
- **As an input:** describe only. "Next-day steps after a headache" has no fair comparison, because the other days aren't known to be headache-free.

**Result:** 16 recorded headaches. The night before each was 20 min shorter than the matched nights (−39 to −3). Among 22 comparisons that doesn't clear the 10% false-discovery threshold, so the state is **No clear relationship · could easily be chance**. With the car thread set aside, only 12 headaches remain and the hint disappears.

In the synthetic truth, short nights really do triple headache risk. The calibration (B §6) shows this is detected only 3–4 times in 60 histories of this length. Saying "not yet" is the correct behaviour. It also cannot say anything about **unrecorded** headaches, or about whether recorded ones were the worse ones (Houle & Turner 2013 on the limits of natural trigger studies).

## D3. A new item: sauna (prototype steps 1, 9)

**Create on 31 Jul**, mid-history (AS-05). "An activity": shape session, recorded every time. Mark may also make it a routine (for example "twice a month"). A single sauna record then counts toward that routine, appears in Time, and is an analysis input, without duplication.

**Eligible by rule:** that night's onset, time asleep and overnight HR; next-day headache via case-crossover. Its history before 31 Jul is not drawn as absence.

**Result:** overnight resting HR +2.7 bpm (+1.5 to +4.0) after sauna evenings. But **88% of sauna evenings were also volleyball evenings**, so the state is **Can't be separated** from volleyball. Volleyball itself is one of the few **Tentative** results (+1.9 bpm, +1.0 to +2.9). It holds under every context assumption, and no single week carries it.

**A typed item works the same way:** "Noisy night" as "Something around me" gets a timing of *that night*, eligibility for that night's onset and time asleep and a same-day headache. Because both it and headaches are recorded "when I notice", the headache pair is correctly marked "no fair comparison", while the sleep pairs are "describe only": unrecorded nights aren't known to be quiet. Switching it to "every time" (one tap, effective from that day) would make them comparable from then on. No developer designed that pairing.

## D4. Complicated by a major outside event: late caffeine and the car (prototype steps 3–6)

**History.** Late caffeine (after 15:00) was recorded every time. Its true synthetic effect on sleep onset is +6 min, which is below the 15-min "matters" band. On Mon 14 Sep Mark's car broke down. For about 10 days he drank late coffee most afternoons and fell asleep much later for reasons that had nothing to do with coffee. He wrote three lines in total:
- "My car broke down" (14 Sep);
- "Borrowed Ana's car for work" (16 Sep, linked by one tap on the "same thing" chip);
- "Mechanic. €640" (21 Sep).

**What the analysis shows:**

| Assumption | Late caffeine → sleep onset that night | Late-caffeine evenings used |
|---|---|---|
| As recorded | **+25 min** (+7 to +39) | 22 |
| Short influence (each note + 2 days) | +12 min (0 to +24) | 16 |
| Long influence (thread 14–21 Sep + 3 days, at least 14 days from the first note) | +10 min (−4 to +24) | 12 |

- **Pre-period check:** the night *before* late-caffeine days was also +18 min later (+4 to +34). That disappears (+7, −5 to +21) once the car period is set aside.
- **One-stretch check:** the 14–20 Sep week moves the estimate most (about 14 of the 25 min), and the note is in that week.
- **Chance check:** passes (1 of 22 comparisons).
- **State: Changes with context.** Headline: "Changes when 'My car broke down' is set aside." The main number stays the "as recorded" one. Meridian doesn't present the 10 min as the true effect, doesn't say the car caused anything, and doesn't drop the data.

**With zero notes** (prototype: "Pretend I never wrote notes"):
- The same candidate is **Already different beforehand**. The late nights started before the coffee, and nothing set aside explains it.
- The influence chart still points at 14–20 Sep, with no flag in it.
- The naive "+25 min" finding is never shown as a finding, with or without the note. The note only adds an explanation Mark can recognise.

**What Mark did:** three one-line notes, one tap to link them. No severity, no end date, no affected outcomes, no "still affected?" question, nothing marked invalid.
