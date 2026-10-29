# A. Evidence review: executive-function support

18 Oct 2026. Research material for Mark's review. Nothing here is approved. The full notes, with every URL and the items I could not verify, are in `sources/`.

**Grades:** **A** shown in adults with ADHD. **B** shown in other populations; may transfer. **C** plausible, not validated. **D** an established therapy that an app can support but cannot honestly reduce to a feature.

## The five findings that change design decisions

1. **Planning a vague intention is the weak link, not holding a well-formed one** (A).
   - Unmedicated adults with ADHD were severely impaired at planning a complex future task (d = 1.60).
   - They were not impaired at recalling the plan once made (d = 0.03), and only slightly worse at starting and carrying it out. [Fuermaier 2013, PLoS ONE, 45 vs 45]
   - So the cheapest high-value help is converting "I should buy flowers sometime" into "when X happens, do Y". Storing it is the easy part.
2. **Clock-based remembering is impaired; remembering triggered by an event is largely intact** (A, small samples).
   - Large time-based deficit, no event-based difference. [Altgassen 2014, J Atten Disord, 25 vs 25]
   - Cue intentions to events the phone can detect, such as work ending, arriving home or a calendar event ending. Don't rely on clock times the person has to watch.
3. **Prompts work at first, fade within weeks, and smart timing adds little** (B).
   - In HeartSteps, a suggestion raised steps by 66% on day 1. The effect fell about 2% a day and was gone by about day 28. [Klasnja 2019, Ann Behav Med, n = 44]
   - Phone-sensor models of whether someone will respond reach only F1 0.31–0.36. [Künzler 2019, IMWUT]
   - A per-user learning algorithm gained about 7% in simulation. [Liao 2020]
   - A plain fixed-time notification raised app opening 3.5-fold in the next hour. [Bell 2023, Drink Less]
   - Reliability and relevance matter far more than inferred timing.
4. **Reminders raise repetition but can slow habit formation; event cues help it** (B).
   - Time-based reminders increased repetition but hindered automaticity, while event-based cues increased it. [Stawarz, Cox & Blandford 2015, CHI]
   - A field RCT of if-then plans for gym visits found a tightly estimated null for a repeated behaviour. [Carrera 2018, J Health Econ, n = 877]
   - Cues suit one-off intentions and deadlines best. For routines they should fade.
5. **No single app feature has been shown to reduce functional impairment in adult ADHD** (A).
   - CBT programs work modestly. Effects are large against waitlists and small to moderate against active controls; Cochrane rates certainty low to very low. [Safren 2010, JAMA; Solanto 2010, Am J Psychiatry; Lopez 2018, Cochrane]
   - A 2025 network meta-analysis found no psychological or drug treatment improved quality of life. [Ostinelli 2025, Lancet Psychiatry]
   - Guided internet CBT did no better than internet relaxation. [Nasri 2023, n = 104]
   - The Inflow app improved self-rated symptoms but not functional impairment. [Antshel 2025, n = 154; figures secondary]
   - Meridian can borrow components (one place for intentions, chunking, a first step, timers). It must never claim to treat ADHD.

## Problem by problem

| # | Difficulty | What is established | Most promising mechanism | Grade | Product implication |
|---|---|---|---|---|---|
| 1 | **Prospective memory** (remembering to act later) | Planning and time-based cueing fail; event-based is intact [Fuermaier 2013; Altgassen 2014]. People offload intentions when it's cheap, and setup effort reduces it [Gilbert 2015; Chiu & Gilbert 2023]. A failed reminder is worse than none, because the person has stopped holding it [Peper 2022]. | One-line capture plus a detectable event cue, delivered reliably and redundantly (Watch, phone, still visible afterwards). | A (deficit), B (offloading) | **Strong.** The core of experiment Hold. |
| 2 | **Planning and prioritisation** | One calendar and task list, A/B/C priorities and problem solving are CBT modules [Safren 2010; Solanto 2010]. They are taught and rehearsed with a therapist. | A short "held" list split into deadlines, intentions and ideas; tonight shown as it really is (calendar plus held deadlines). No priority scoring. | D as a program, C as a feature | **Moderate.** Help plan by subtraction (what already fills the evening), not by making Mark plan. |
| 3 | **Task initiation** | Breaking a task down and naming the first step are inside the effective CBT packages. No isolated test of a "first step" prompt exists. Procrastination interventions: g = 0.34 overall [Rozental 2018]. | A remembered first physical step plus a short bounded runway (5, 10 or 25 min) with an explicit exit. | D (package), C (feature) | **Promising, unproven.** Experiment Start. Cheap to test. |
| 4 | **Transitions** (work to home) | Detachment from work correlates with well-being, small to medium [Wendsche & Lohmann-Haislah 2017, k = 91, mostly correlational]. Unfinished tasks leave attention residue [Leroy 2009]. Writing a plan for an unfinished goal quieted it [Masicampo & Baumeister 2011, unreplicated]. Unfinished tasks are not remembered better, but people reliably want to resume them [Ghibellini & Meier 2025]. | A ~30-second "park it until tomorrow" capture, triggered by a real boundary (Work Focus off). | B/C | **Promising, unproven.** Experiment Cross. Main risk: becomes a daily ritual. |
| 5 | **Time awareness** | Interval reproduction is impaired in most adult studies, but the adult evidence is "not yet conclusive" [Mette 2023, 9 adult studies]. No peer-reviewed study of visual timers in adults. | Visible remaining time for a deadline window or a running session (Live Activity, Watch). | A weak (deficit), C (aid) | **Cheap, low risk, unvalidated.** Folded into Start and deadlines, no separate feature. |
| 6 | **Decision paralysis** | Choice overload averages zero [Scheibehenne 2010]. It appears with hard decisions, uncertain preferences and an effort-minimising goal [Chernev 2015], which describes a tired evening. | Offer one idea at a time, with a quiet "something else", only when there is room. | B | **Modest.** A rule ("at most one"), not a feature. |
| 7 | **Avoidance and procrastination** | ADHD symptoms correlate with procrastination (observational). Steeper delay discounting, d = 0.43 [Jackson & MacKillop 2016]. Temptation bundling settles at about +10–12% [Kirgios 2020, N = 6,792], below the original +51%. | Lower the entry cost (Start). Optionally pair a dreaded task with something liked (Mark already uses podcasts). | A (link), B (bundling) | Start covers it. Bundling isn't worth a feature for Mark (his 15:15 message). |
| 8 | **Follow-through over months** | Median 30-day retention for mental-health apps is 3.3% [Baumel 2019]. Only 8% of 54 gym nudge programs had effects after they ended; rewarding a return after a miss did best [Milkman 2021, Nature, N = 61,293]. Habits plateau at a median of 66 days, range 18–254 [Lally 2010]. | Comeback-friendly design. Cues that fade as routines stabilise. Content that rotates. | B | **Constraint, not feature.** Every mechanism must survive weeks 4–12 and long absences. |
| 9 | **Hyperfocus and stopping** | Associated with ADHD symptoms (self-report) [Hupfeld 2019]. No intervention study. | Same runway mechanism used as a "stop point" with a heads-up 10 minutes before. | A (association), C (aid) | **Narrow.** Reuse Start; no separate feature. |
| 10 | **Emotional friction and overwhelm** | Emotional dysregulation is large in adult ADHD, g = 1.17 [Beheshti 2020]. Its role in avoidance is theory. Reframing thoughts is a therapist-led CBT module. | Wording and structure that never shame; small bounded commitments; no overdue states. | D for thought work | **Don't build therapy.** Express it through tone and the no-backlog rule (R-21). |
| + | **Opportunity discovery** | Doing more rewarding activities (behavioural activation) helps depression, g ≈ 0.74–0.87 in mostly low-quality trials [Cuijpers 2007; Ekers 2014]; scheduling is the burdensome part. Varying kind acts prevented the decline seen when repeating them [Sheldon, Boehm & Lyubomirsky 2013, N = 52]. Help that looks freely chosen earns more gratitude [Weinstein, DeHaan & Ryan 2010]. Expected rewards reduce later voluntary engagement [Deci, Koestner & Ryan 1999]. | Ideas Mark saves himself, resurfaced rarely and varied, with no points or "due" states, and never on a schedule. | B, effects small (r ≈ .10 after correction, White 2019) | **Moderate value, high risk** of feeling transactional. Kept small inside Hold and Cross. |
| + | **Notification burden** | Batching to 3 deliveries a day improved attention and mood; turning notifications off entirely raised anxiety [Fitz 2019, n = 237]. Alerts-on raised self-reported inattention and hyperactivity [Kushlev 2016]. | A hard cap on interruptions. Ambient surfaces (widget, Watch, Live Activity) before pushes. | B | **Binding design constraint** for everything above. |

## Established therapies Meridian should not imitate

- **CBT for adult ADHD** (Safren, Solanto, R&R2ADHD) works as a whole program with a therapist, rehearsal and homework (D). Meridian can provide the container its organising module assumes, a reliable external place for intentions, without the teaching. It must not present itself as CBT.
- **Cognitive reframing and adaptive thinking** (D). Prompts that ask Mark to challenge his thoughts would be therapy-lite and patronising.
- **Goal Management Training** (C for ADHD). Its 81-person RCT found no effect on everyday executive function [Hanssen 2023].
- **Coaching and body doubling** (C). Only tiny pilots or no controlled trials exist, and both need other people.
- **Brain-training games** (A, null for symptoms). Never a route to daily functioning [Gabarron 2025].

## Limitations of this review

- **Thin adult ADHD evidence.** It is mostly small case-control studies plus a few CBT and internet RCTs. No trial in adults tests a reminder, timer, transition cue, if-then plan or JITAI as a standalone feature, so every proposed feature is at most C.
- **Some figures are secondary.** Several numbers come from abstracts or secondary summaries, and these are marked in `sources/`. Examples are the Safren response rates, Inflow's effect sizes, the 2025 if-then meta-analysis bias-adjusted figure, and the Okoshi breakpoint figures.
- **Sources not found.** Five starting points could not be located or verified: Young 2020, Liu 2023, Zheng 2022, Jang, and Ishii. They are not cited.
- **Single-user N.** Mark is one person. Population averages say little about whether a mechanism helps him. That is why each concept in D carries a falsification test he can run on himself in two to four weeks.
