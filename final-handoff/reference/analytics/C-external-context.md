# C. External context strategy

18 Oct 2026. Research proposal, not approved. Data objects are in `A-data-model.md`; the statistics that use them are in `B-discovery.md`.

## The position

Outside life is the biggest unmeasured influence on everything Meridian looks at, and most of it will never be recorded. So:

1. **Robustness comes first, notes second.** Every finding is checked for whether it depends on one stretch of days, whether the "effect" already existed before the input happened, and whether it holds on new data. These checks need no input and catch a car breakdown Mark never wrote down.
2. **A note is a fact with an unknown effect.** "My car broke down" records that something happened at a time. Meridian never infers how bad it was, how long it lasted, or what it changed.
3. **Context changes how results are shown, never which data exists.** No observation is removed. A result is shown under a few explicit assumptions, and Meridian says whether it changes.
4. **"We can't tell" is a valid result.**

## 1. Recording context with no admin

| Gesture | What it does | What it never does |
|---|---|---|
| **Note** in the Log sheet: one line of text, saved | Puts a mark in Time at that moment | Ask for a category, severity, mood, end date or follow-up |
| **"Same thing" chip** when writing a later note: the two most recent notes are offered as chips ("Car broke down · 2 days ago") | One tap links the new note to the earlier one, forming a **thread** | Require linking. Without a tap it's a separate note |
| Existing **one-tap context** (sick, trip, day off) | A labelled span, as in the prototype | Ask when it ended. It ends when Mark switches it off, or stays open with no harm |
| **Calendars** Mark chooses, once | All-day events and flights become imported context, labelled "from calendar" | Read an empty calendar as "free", or create obligations |

The chips are ordered by recency only. Optional on-device text matching may reorder them; it never links anything by itself. There is no incident screen, no "are you still affected?" question, and no backlog. A note can be edited or deleted like any record.

**Derived circumstances need nothing at all:** a time zone change, wrist temperature plus resting HR well above Mark's own baseline, public holidays, and *co-shifts* (several unrelated outcomes moving away from his usual range at the same time). A co-shift is shown as a quiet mark in Time ("several measures were unusual from 12 Mar"). It is never a prompt. Mark may add a note there if he wants; nothing waits for one.

## 2. What can and cannot be modelled

| Credible | Must stay unknown |
|---|---|
| When a note was written, and when its thread's later notes were written | How stressful or significant anything was |
| That a period contains stated, imported or possible context | Which outcomes were affected, and by how much |
| Whether a result depends on that period (sensitivity) | How long an effect lasted. Acute, delayed and recurring effects are all possible, and a single person's data cannot separate them |
| Whether a result depends on *any* single stretch, noted or not (influence) | Everything that was never recorded |
| Whether the "effect" was already there before the input (pre-period check) | Whether stress *caused* a change, or explains a relationship |
| Unusual co-movement across several measures | What caused a co-shift |

## 3. How analysis uses context: assumptions, not corrections

Every candidate relationship in B is computed under a fixed set of **context assumptions**. They are shown, not chosen:

| Assumption | Meaning |
|---|---|
| **As recorded** | All data. Measured context (weekday, travel, existing sick and trip spans) used as covariates only |
| **Short influence** | Leave out the day of each note or context start, plus the next 2 days |
| **Long influence** | Leave out each note day plus 14 days. A thread spans from its first note to its last, plus 3 days |
| **Without possible circumstances** | Also leave out derived periods (body signals unusual, co-shifts) |

The window lengths are placeholders (D-03). They bracket two findings: most repeated daily stressors stop affecting mood by the second day, sometimes with a rebound (Bolger et al. 1989); and major events differ widely in how long adaptation takes, with no single default (Luhmann et al. 2012). Daily stressors are also common, occurring on about 40% of days in a national sample (Almeida et al. 2002), so a stretch of unrecorded stress is the normal case, not the exception. These are sensitivity brackets, not claims about Mark. Sources: `sources.md` §7.

**Reading the result:**
- The estimate and its interval are compared across assumptions.
- If the conclusion is the same under all of them: **"Holds with or without the noted periods."**
- If it moves materially (the interval crosses "no meaningful difference", or the estimate changes by more than half): **"Changes when [Car broke down] is set aside"**, with that period highlighted in the chart.
- The main estimate stays the "as recorded" one. Meridian never presents the adjusted number as the true one.

**Influence check (works with zero notes).** Each comparison is recomputed leaving out one 7-day block at a time. If one block moves the estimate more than the others combined would suggest, the result is flagged **"Mostly from one stretch (12–18 Mar)"**, and any notes or context in that block are shown beside it. This is how unrecorded events surface without asking about them.

**Pre-period check.** The same comparison is run with the outcome shifted to *before* the input. A difference that already exists before the input happened cannot be its effect. That points to selection or outside circumstances, and the result is shown as **"Already different beforehand"**.

## 4. Consequences, cascades and threads

A car breakdown is a thread of notes Mark happened to write: the breakdown, "borrowed Ana's car", "mechanic", "€640". Meridian treats the thread's span as one period for the long-influence assumption, and nothing more. It does not:
- assign the later notes to outcomes;
- extend the span beyond the last note plus the tail;
- treat a thread as more important because it has more notes.

Recurring consequences (the mechanic visit several days later) are handled only by being their own notes in the thread. If Mark writes nothing after the first note, the long-influence window covers the uncertainty.

## 5. What Meridian says when it cannot know

Wording is fixed templates, filled from computed values:

- "Most of the evenings with caffeine after 15:00 fall in one stretch of March. Set aside, the difference is about half as large."
- "The nights you took melatonin were already shorter the night before. This can't show what melatonin did."
- "This is a pattern in what was recorded. Plenty that affects you isn't recorded, so it can't be a cause."
- "Not enough comparable days yet. Context doesn't change that."

## 6. Interaction with routines and contextual support

- **Notes never change progress, periods or routines.** R-21 already means a hard week costs nothing.
- **Notes are layer 1 facts** (A §6). The executive-function layer may read a stated trip to choose realistic suggestions. Whether a note like "car broke down" should influence suggestions at all is the EF thread's question. Meridian must never use a note or poor sleep to suppress a commitment Mark created.
- **No note is ever required.** Every analysis has a complete, honest result with zero notes. Notes only add sensitivity results and labels.
