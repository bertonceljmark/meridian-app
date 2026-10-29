# Meridian: what the research changes, and three product concepts

> **Status after Mark's review (18 Oct, 13:28): none of Tempo, Forecast, Almanac, or their combination is approved.** Prototype 02 is disposable research. Corrections to this document:
> - Enjoyment *during an activity* predicting persistence does not show that satisfying *logging* has the same effect. Initiation, the activity itself and the reward afterwards are distinct opportunities.
> - Measurement can reduce enjoyment, but that does not override Mark's explicit interest in rich workout statistics.
> - 85–140 days is one illustrative estimate (r ≈ .30, 80% power), not a universal rule. Data needs depend on the measure and the analysis.
> - Missing data may not pause, preserve, break or complete a routine without a defensible rule.
> - Forecasting must never be a prerequisite for discoveries.
> - History must be able to be beautiful with zero extra input.

Contract v1.1.1 applies. Raw notes with every source are in `r1-mechanisms.md`, `r2-routines-wellbeing.md`, `r3-measurement-analytics.md` and `r4-interaction-progression.md`. Bracketed codes such as [r1·5] point to a finding there. Most figures come from abstracts, and the notes say where.

**Evidence labels:**
- **E** means established (moderate or strong).
- **H** means my inference.
- **S** means speculative.

## Part 1. Ten findings that change the product

1. **The reward has to be in the doing, not in the report afterwards.** [E: r1·1, r2·2]
   - Enjoyment during an activity predicts persistence; the long-term benefits people name as their reasons do not.
   - Keeping a routine going depends on being satisfied with what it has *actually* given, not with what was expected [E: r2·1].
   - *Change:* every log needs its own small, satisfying consequence. Reports come second.

2. **"Results as reward" (your hypothesis) is only partly right.** [E: r1·5, r1·11, r4·4]
   - Measuring an enjoyable activity makes people do more but enjoy it less (6 experiments).
   - Very fast informational payoffs build *checking* habits, not doing habits. People avoid the app after bad news (logins fell 9.5% after market drops).
   - You said you enjoy results even when you struggle to do the activity. That fits inspecting, not doing [H].
   - *Change:* results attach to the act and depend on it. Routines enjoyed for their own sake (dates, social, creative) get quiet acknowledgement and memory, with numbers only on request.

3. **Feedback should show what changed, not get louder.** [E: r4·1]
   - Feedback tied to success raised competence and curiosity; amplification lowered both (pre-registered, n = 1,699).
   - Curiosity was the only predictor of continued play. Moderate feedback beat both none and extreme.
   - *Change:* this confirms your rejection of loud ceremonies on evidence, not just taste.

4. **Continuity motivates. Breakage and self-blame are what hurt.** [E: r2·8, r2·9, r1·13]
   - Unbroken streaks do raise continuation; broken ones lower it, especially with self-blame, and less when they can be repaired.
   - Goals with built-in spare days beat easy and hard goals for persistence after a miss.
   - In a 61,000-person gym megastudy, the best of 54 interventions rewarded *returning after a missed workout*. Flexible timing beat fixed times.
   - *Change:* continuity can be kept if it can't be destroyed. Spare capacity is part of the goal, and a comeback is a positive event.

5. **Routines last for different reasons, so feedback should differ while the data model stays the same.** [E: r2·5, r2·13–15; H: r2·H-A]
   - For weekly behaviour, repetition count didn't predict automaticity; feeling good afterwards did.
   - Scheduling leisure for an exact time makes it feel like a chore; loose timing doesn't.
   - Anticipation carries much of the value of rare events. People underestimate how much they'll enjoy rediscovering ordinary moments later.
   - *Change:* a twice-monthly date should feel like a rhythm kept alive and memories accumulating, not a ratio filling up.

6. **Mastery mostly lives outside the routine itself.** [H: r1·H2; E: r1·9, r1·16, r1·17]
   - Water or a date have no skill to master. Mastery can live in three places:
     - the **craft**, where one exists (training, music, cooking);
     - **knowing yourself**, i.e. how well you predict your own patterns;
     - **designing your own system**.
   - Authoring your own approach reduces "one number replaces the goal", and self-made things are valued more unless destroyed.
   - Authoring can also *feel* like progress without being it. Developers using AI were 19% slower while believing they were 20% faster. You named "optimizing a system instead of using it" as one of your own struggles.
   - *Change:* authorship is included, but with brakes on it.

7. **Novelty should come from new ways of reading your history, not from changing your routines.** [E: r1·14, r4·6]
   - In data from 218,606 app users, more variety of activities went with *smaller* well-being gains.
   - Lapsed or light users preferred aggregate views. Tallies of days tracked discouraged people with little data.
   - *Change:* views of history unlock as data accumulates. Day one gets "firsts" and patterns, not empty tallies.

8. **Milestones cause slumps, and calendar seasons fit an irregular life poorly.** [E: r1·8, r4·10; H: r4]
   - Effort falls after each reward is reached.
   - *Change:* use horizons that roll forward, and chapters taken from your actual life (a trip, an illness, a new routine), not six-week seasons.

9. **How you feel splits into about three things.** [E: r3·2–7]
   - The three are pleasantness, energy, and calm versus tension.
   - Clarity, starting tasks and concentration are *functioning*, best asked as concrete questions ("finished what you sat down for?") rather than rated.
   - Burden comes from how long each check-in is, not how often.
   - Missing entries skew towards stressed days, so averages over logged days look rosier than reality.
   - *Change:* a one-gesture "how I feel", event-anchored micro-reports, optional sampling weeks, and honest notes about what's missing.

10. **Honest personal discovery is scarce.** [E: r3·10–15]
    - One person's data supports only about six variables, and a typical relationship needs roughly 85–140 or more days.
    - Consumer apps that mine every pair (Exist, Bearable) and opaque composite scores (Oura) are exactly what the contract rules out.
    - *Change:* use a small set of plausible relationships chosen in advance. Show *how close each is to being knowable* as something to look forward to. Personal discoveries are an occasional reward, never the core.

**Platform facts that change options** (verified on developer.apple.com, r3 §9 and r4·15):
- **Screen Time** data can reach Meridian on iOS 26.4+ at hourly resolution. A development install on your iPhone is supported, and the EU is eligible.
  - **The catch:** only one app per device can hold this access. One unconfirmed report says Apple's own Screen Time pane then stops updating. Needs a hands-on check.
- **One-tap logging outside the app:** Controls, interactive widgets, Watch double tap, and Smart Stack relevance (by sleep schedule or place).
- **NFC tags** can trigger a Shortcuts automation that runs without confirmation. A tag on a water bottle or guitar case could log the routine where it happens.

## Part 2. Foundation shared by every concept

Each of these is backed by evidence above:
- **One generic routine model** (contract §7). The *feedback lens* is inferred from measure and cadence, and you can change it:
  - **quantity** routines fill up;
  - **session** routines get a report;
  - **rhythm** routines (rare) get anticipation and memory;
  - **quiet** routines get acknowledgement with no numbers.
- **The act is the reward:** under a second from action to a visible change, a small vocabulary of haptics, notches that go silent past the target, physical anchors (NFC, controls, double tap), undo everywhere.
- **Nothing is destroyed:** spare capacity per period, pauses and context excluded, comebacks acknowledged warmly, and no tallies of days tracked.
- **Rare and relational routines:** a loose "next time" intention ("sometime this weekend"), an optional keepsake (a word, photo or place, never a rating), and occasional resurfacing ("a year ago, the first of your dinners").
- **How you feel:** one gesture with optional words, behavioural questions for functioning, event-anchored taps after something you did, optional sampling weeks. Physiology appears as gentle context, never a readiness score.
- **Discovery:** a small set of relationships chosen in advance, an honest "needs about 6 more weeks" state, personal *behaviour* experiments (never medical or substance ones), and bad news shown safely, leading with what's intact.

## Part 3. Three product concepts

Each concept centres on a different engine. All three meet the contract foundation above. For each: the core loop, what grows over months, how it handles the hard cases, and the honest main risk.

### Concept 1: "Tempo". Rhythms that hold

**Engine:** continuity that can't break.
- Every routine is a rhythm with its own natural period: hours for water, days for a practice, a week for exercise, a month for the date.
- Doing the routine *keeps time*. The visible state is how long the rhythm has been held, measured in its own periods.
- **Spare capacity** is set when you create a routine (for example, one spare month a year for the date) and absorbs misses.
- Paused spans and context such as sickness or travel simply don't count.
- If the spare runs out, the span *comes to rest*: it closes as a finished, kept achievement. Your next action starts a new span marked as a **comeback**.

**What grows:**
- A lifetime record of held spans, comebacks and total time kept.
- A slow portrait of how all your rhythms run together.
- Chapters from your life segment it.

**Hard cases:**
- Several times daily: the period is a day, and logs fill it.
- Twice monthly: the period is a month with a target of 2, plus anticipation and a keepsake.
- Mid-year start: the rhythm simply begins.
- Travel: context pauses the counting.
- Observation: no rhythm and no reward; reduction intentions close each week with "is that everything?".
- Absence: spans rest and nothing is lost.
- Change, pause or retire: periods are versioned.

**Evidence:** findings 4, 5 and 8.

**Main risk:** it is still about continuity. A perfectionist may watch the spare capacity anxiously. It needs testing with you specifically.

### Concept 2: "Almanac". A life that writes itself

**Engine:** meaning and memory.
- Meridian composes an ongoing record of your life from routines, passive data and keepsakes.
- Logging adds a specific mark to today's entry immediately.
- Sessions produce rich accounts; rare routines produce keepsake pages.
- Chapters come from your life, and you can caption them, which adds the value of having made them yourself.
- New ways of reading the almanac unlock as data accumulates: comparisons, "firsts since", a year ago.

**What grows:** the almanac itself, which is endless, authored and never destroyed.

**Hard cases:** all handled, because entries are generic. Absence shows as a quiet blank, never as failure.

**Evidence:** findings 5, 7 and 8, plus r4·7 and r2·15.

**Main risk:** this is closest to the "restrained personal analytics journal" you rejected in prototype 01. It is strong on priorities 3 and 4 and weak on the pull to *do* things (priorities 1 and 2). I would not make it the core alone.

### Concept 3: "Forecast". Get to know yourself

**Engine:** curiosity and self-calibration.
- At natural moments, you can optionally make a one-tap call. Examples: Monday ("a moving week or a quiet one?"), bedtime, before a workout, before a date ("looking forward a lot or a little?").
- Reality answers, and Meridian shows the gap using honest data.
- Over months you build an endless, honest skill: **how well you know yourself**, by area.
- Missed calls are the most interesting part. They lead naturally into the small set of chosen relationships ("you expected short nights to flatten you; they mostly didn't").

**What grows:** a lifetime record of self-knowledge, the relationships that have become knowable, and the forecasts that came true.

**Hard cases:**
- Rare routines: forecast the month.
- Observations: forecast without judgement.
- Absence: no forecasts are owed.
- Day one: forecasts work immediately, because reality answers within hours.

**Evidence:**
- Information is a reward in its own right [r1·10].
- Curiosity drives return [r4·1].
- Mastery through self-knowledge [r1·H2].
- It also handles the "chosen in advance" analysis requirement without a question catalog: the forecasts *are* the candidates, and they are optional and tied to a moment.

**Main risk:** perfectionism about being right, and drifting into self-surveillance. It must be sparse, never scored as failure, and calibration must mean "know your range", not "be accurate". It is also novel enough that it could feel gimmicky. Only a prototype will tell.

### Not taken as an engine: "Workshop" (authoring your own system)

You'd write your routine system as versions and compare how v3 played out against v2, with personal behaviour experiments. The evidence says this is engaging, and it is also the trap you named yourself. It belongs as a **light layer** in every concept: a "why" line per routine, choosing spare capacity and lens, and occasional "try this for two weeks" experiments. It is not the engine.

## Part 4. Recommendation

**Prototype Tempo as the engine, with Forecast as its optional curiosity layer and Almanac as the shape of history.**
- **Tempo** carries priorities 1 and 2: doing, holding, and coming back.
- **Forecast** gives priorities 3 and 4 an honest, endless engine of curiosity, instead of a stream of reports.
- **Almanac** gives history its meaning.

**What would change my mind:** if testing shows that spare capacity makes you anxious, Forecast becomes the engine and Tempo's continuity is softened to plain "kept" marks.

**Owner decisions surfaced by research** (not needed now):
- **Screen Time:** is Meridian's analysis worth possibly losing Apple's own Screen Time pane? Check hands-on on your phone first.
- **Partner sharing:** should a partner be able to share a routine such as dates, as shared ownership rather than monitoring? Evidence is mixed, and consent would need to be designed.

**Not covered yet:** visual direction. It comes with the prototype and follows the contract's middle-ground boundary (mature, expressive, not loud and not a quiet dashboard). The visual references will be chosen for qualities, not copied.
