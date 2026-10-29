# B. Opportunity shortlist: ranked mechanisms

18 Oct 2026. Not approved. Evidence grades as in `A-evidence-review.md` (A adults with ADHD, B other populations, C hypothesis, D therapy). Burden is split into **once** (setup), **occasional**, **daily** and **per occurrence**.

## Ranking

Scores run from 1 to 5. Burden is scored so that 5 means lowest burden.

| Rank | Mechanism | Benefit | Generality | Low burden | Feasibility | Evidence | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | **Held intentions with event anchors** | 5 | 5 | 4 | 4 | 4 | Build into a test |
| 2 | **Deadline windows with one last call** | 4 | 3 | 5 | 5 | 3 | Build into a test |
| 3 | **Ambient persistence** (widget, Watch, Live Activity instead of repeat pushes) | 4 | 5 | 5 | 4 | 3 | Build; delivery layer for 1 and 2 |
| 4 | **Start: first step and bounded runway** (also the stop point) | 4 | 4 | 4 | 5 | 2 | Test |
| 5 | **Ideas shelf** (saved opportunities, rarely resurfaced) | 3 | 4 | 4 | 5 | 2 | Test, small and inside 1 |
| 6 | **Cross: work-to-home transition** | 3 | 2 | 3 | 3 | 2 | Test on Mark only; first to cut |
| 7 | **Cues that fade as routines stabilise** | 2 | 5 | 5 | 5 | 3 | Adopt as a rule for R-07 reminders |
| — | Week look-ahead planning ritual | 3 | 3 | 1 | 5 | 2 | Reject: a recurring planning chore |
| — | Inferred receptivity or "smart" timing | 1 | 4 | 5 | 2 | 3 (against) | Reject now; revisit for ideas only |
| — | Morning card as the main surface | 2 | 4 | 2 | 5 | 2 | Reject as default (see C §6) |
| — | LLM-generated suggestions | 2 | 4 | 4 | 3 | 1 | Optional rewording only |
| — | Temptation bundling, body doubling, accountability partners | 1–2 | 2 | 3 | 3 | 1–3 | Reject: niche or needs other people |

**Why this order.** Rank 1 targets the deficits with the best adult ADHD evidence (planning a vague intention; time-based cueing) and works for any activity. Ranks 2 and 3 are low burden and fully buildable, but deadlines are a narrower class of things. Start is cheap and broad, but its evidence is only that its parts sit inside effective CBT programs. Cross is the most specific to Mark's life and the most likely to become a ritual.

## The mechanisms

### 1. Held intentions with event anchors (experiment Hold)
- **Difficulty.** An idea occurs at the wrong moment and is gone by the right one. Examples: invoice, dentist, flowers.
- **Mechanism.** It turns a vague intention into an if-then plan whose "if" is an event the phone can detect: work ends, arrive home, after an event in the calendar, next weekend, the next time Meridian is opened. The cue fires once, at that event.
- **Evidence.**
  - A: planning and time-based cueing are the documented deficits.
  - B: if-then plans, effect sizes 0.27–0.66 [Sheeran 2025]; offloading improves remembering [Gilbert 2015].
  - The if-then evidence in ADHD is from children only.
- **Interaction.** One text line (or a routine or saved idea), then one tap on a "bring it back" moment. When the cue fires, the answers are Start, Later (moves it to the next moment), Already done.
- **Information and permissions.** Notifications. Optional: calendar full access, location "Home" (a When-In-Use permission is enough for an arrival notification), adding Meridian's Focus filter to a Work Focus.
- **Burden.** Once: permissions, optionally home and Work Focus. Per occurrence: about 5 seconds to capture, 1 tap at the cue. Nothing daily.
- **Risks.**
  - Becoming a task manager. Mitigation: no due dates on intentions, no lists to sort, a soft limit around 15 held items, and stale ones fade into ideas.
  - Dependence: Meridian becomes Mark's memory and a failed cue is costly. Mitigation: redundant delivery and items stay visible after the cue.
- **Generality.** Any one-off or occasional action, including routines with a long cadence (date twice a month, deep clean monthly).
- **Fit.** It is the "held" state of the existing item model. Routines can be held too.
- **Falsified if** over two to three weeks Mark mostly picks clock times, rates more than half of cue moments as wrong, or held items pile up without being acted on or dropped.

### 2. Deadline windows with one last call (Hold, step 3)
- **Difficulty.** Real deadlines (trash on Thursday night, a birthday present) don't care how tired Mark is.
- **Mechanism.** It separates commitments from intentions and ideas. A commitment has a window (for example Thursday 18:00–22:00). It stays visible on the Lock Screen and Watch for the whole window, gets one optional cue at the start and one last call before it closes. No context signal, including sleep or "rest" logic, can suppress it.
- **Evidence.** B: reminders roughly double adherence odds for time-bound actions [Thakkar 2016]. The window and single last call is a C design.
- **Interaction.** Done on the Watch or Lock Screen, or "I'm on it", which silences the last call while the window stays visible. AlarmKit is opt-in for things that must break through Focus.
- **Information and permissions.** Notifications; Time Sensitive used sparingly; AlarmKit authorisation only if chosen.
- **Burden.** Once per commitment: set the window. Per occurrence: one tap, only if he wants to silence it.
- **Risks.** Nagging if he did the task but didn't mark it. Mitigation: exactly one push after the window starts, and the deadline counts as done when the window closes if he never answered (unknown, not failed).
- **Generality.** Narrow class: real external deadlines. Recurring or one-off.
- **Fit.** A commitment is a routine with a window target. It is never rewarded like a behaviour unless Mark makes it a routine.
- **Falsified if** he still misses deadlines he set up, or turns the last call off within two weeks.

### 3. Ambient persistence
- **Difficulty.** The two failure modes compete: forgetting, versus fatigue from repeated reminders.
- **Mechanism.** Persistence without repetition: after at most one interrupt, an intention stays visible where Mark already looks (a Lock Screen widget, a Watch Smart Stack card, a Live Activity during a window). Visibility replaces re-notification.
- **Evidence.** B: batching and fewer alerts improved attention and mood [Fitz 2019; Kushlev 2016]. C: that ambient visibility keeps intentions alive is untested.
- **Interaction.** None required. Interactive widget buttons (Done, Later) work without opening the app.
- **Burden.** Once: add the widget or Watch complication.
- **Risks.** Banner blindness: ambient items stop being seen within weeks. Mitigation: keep it to 1–2 items and order them by anchor proximity.
- **Generality.** Universal delivery layer.
- **Falsified if** Mark can't say what is on the widget when asked at random.

### 4. Start: first step and a bounded runway (experiment Start)
- **Difficulty.** Initiation resistance on aversive admin (an invoice), and hyperfocus that won't stop.
- **Mechanism.** It lowers activation energy with a concrete first physical step and a short commitment that has a sanctioned exit. It is visible elapsed time (Live Activity, Watch). The same timer can run in reverse as a stop point with a heads-up.
- **Evidence.** D/A: chunking and first steps are inside Safren's and Solanto's CBT. C: no isolated test. A weak: time-perception deficits.
- **Interaction.** Start (from a cue, an item, a widget or the Watch), optionally edit the first step, pick 5, 10 or 25 minutes. At the end the Watch taps once: keep going, stop here (it stays held for its next moment), finished.
- **Information and permissions.** None beyond notifications. Live Activities are on by default.
- **Burden.** Per occurrence: 1–2 taps. Writing a first step is optional and remembered.
- **Risks.**
  - Rewarding "started" as if it were done. Mitigation: started and finished are recorded separately, and neither selecting nor holding earns anything.
  - Becoming a productivity timer (Pomodoro). Mitigation: no sessions scoreboard, no focus score.
- **Generality.** Any activity that has a start: chores, admin, practice, meditation, exercise. It is already the "session" measure type.
- **Fit.** It is the existing session logging grammar plus a first step and a runway. No new place in the app.
- **Falsified if** after three weeks Mark uses Start only for things he would have done anyway, and the dreaded items still don't move.

### 5. Ideas shelf (opportunity discovery, inside Hold)
- **Difficulty.** Worthwhile but unconfigured things never occur to him at a useful time: flowers, the sauna, calling a friend.
- **Mechanism.** Ideas mostly come from Mark: one tap to save from anywhere, plus an optional opt-in starter library by category. An idea resurfaces rarely (at most one, only where there is room), with cooldowns that lengthen after each pass and rotation across categories. Ideas never notify by default and are never "due".
- **Evidence.**
  - B: varying acts prevented the decline seen when repeating them [Sheldon 2013].
  - B: help that looks freely chosen earns more gratitude [Weinstein 2010].
  - B: expected rewards reduce voluntary engagement [Deci 1999].
  - Small effects overall.
- **Interaction.** Save: share sheet, widget, Watch or in-app, with no required fields. When shown, the answers are Tonight, Some other time, Not this one.
- **Learning.** Doing it is a strong positive. "Some other time" says something about timing only. "Not this one" lengthens the cooldown. Ignoring it counts for almost nothing. No ratings.
- **Burden.** Per occurrence: a capture when the idea occurs. Otherwise none.
- **Risks.** It turns gestures into obligations, and could feel creepy about his girlfriend. Mitigation: no streaks, points or "you haven't…" wording; the app never assumes what anyone wants; it can show where each idea came from.
- **Generality.** Any category.
- **Falsified if** within a month he stops saving ideas, or the ideas shown feel generic or nagging.

### 6. Cross: the work-to-home transition (experiment Cross)
- **Difficulty.** Work keeps running in his head after work ends, and household tasks don't start.
- **Mechanism.** A boundary event (Work Focus off; fallback: leaving a place or a set time) offers a 30-second crossing: park open work thoughts until work starts tomorrow, see tonight's real commitments, and at most one optional idea if the evening is empty.
- **Evidence.**
  - B: detachment correlates with well-being.
  - B, unreplicated: plan-making quiets unfinished goals.
  - C: no test of an app ritual.
- **Burden.** Once: enable it and choose the trigger. Per occurrence: optional, 0–30 seconds.
- **Risks.**
  - It is a daily prompt, which is exactly the kind of thing Mark says he would abandon.
  - Mitigation: a silent notification, skipping is free, and no counts. If he uses it on fewer than one evening in five, it turns itself into a widget-only entry.
- **Generality.** Narrow: people with a work boundary. It generalises to other transitions (end of a study block) only in theory.
- **Falsified if** after two weeks he opens it on less than one evening in five, or work thoughts still intrude, by his own account, as much as before.

### 7. Cues that fade as routines stabilise
- **Mechanism.** A routine's optional cue moves from a clock time to an event, then backs off when the routine is being done without it (for example, done before the cue fires on several occasions). Mark can always restore it.
- **Evidence.** B: reminders raise repetition but slow automaticity [Stawarz 2015]; habits plateau at 18–254 days [Lally 2010].
- **Fit.** It refines R-07 (optional reminders) without new UI.
- **Falsified if** a routine reliably drops off after its cue fades.

## Rejected, and why

- **Week look-ahead or planning ritual.** Planning is the deficit, but a weekly session is a recurring chore and the core "task manager" risk. Its useful part (tonight as it really is) is folded into Cross.
- **Inferred receptivity or "smart" timing.** It is wrong 20–30% of the time at best, gives small effects that decay, and needs weeks of data per person. See C §5.
- **Morning card.** It catches Mark at his least receptive moment and is a daily ritual. Morning is one possible anchor among many, not the system.
- **LLM-generated suggestions.** They would pretend to know his partner and values. At most, optional on-device rewording or step breakdown with deterministic fallbacks. Never required.
- **Temptation bundling.** Mark already pairs chores with podcasts; there is no incremental value.
- **Body doubling and accountability.** No controlled evidence, and they need other people.
- **Reframing or self-compassion prompts.** Therapy-lite (D) and likely patronising.
