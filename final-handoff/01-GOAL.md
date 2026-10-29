# 01 · The goal, in Mark's words

Everything here is traceable to `evidence/owner-messages-1-log.md` (18–23 Oct) and `evidence/owner-messages-2-after-log.md` (21–29 Oct). Quotes are verbatim, typos included. When this file and his messages disagree, his messages win, and the newer message wins over the older one.

A provenance warning Mark gave himself (18 Oct 13:07): many of his long messages were AI-drafted prompts he pasted. **Keep the outcome he wanted. Treat specific mechanisms inside those prompts as hypotheses unless he endorsed them.** His short, informal messages are the strongest evidence of taste.

---

## 1. Who it is for

> "I'm an adult with diagnosed ADHD. I struggle with sustaining healthy routines, especially when the benefits are delayed. I am technically sophisticated … I am also quite perfectionistic, including about design, accuracy, and the quality of my personal projects."

> "I can be intensely interested in something for a period of time. But when it becomes repetitive or unrewarding, maintaining it becomes difficult."

He is the first user, but Meridian is not an ADHD app and not a Concerta app: "It should work equally well with any medication, supplements, or no medication at all." Later he names the audience as people like him: "its extremely important that it looks really good because of our target a udience" (23 Oct).

## 2. The one-sentence goal

> "I want to genuinely enjoy taking care of my health because Meridian makes healthy behavior satisfying, progress meaningful, results fascinating, and the entire experience extraordinarily beautiful." (18 Oct)

Broadened the same day: it is "a gamified personal well-being and routine application", not only physical health. Relationships, social life and anything personally meaningful count ("take my girlfriend on a date at least twice per month … is a completely legitimate Meridian routine").

## 3. The four priorities, in order (repeated in nearly every brief)

1. **Establishing and maintaining personally meaningful routines.**
2. **Making that genuinely enjoyable**: satisfying interactions and real, sustainable gamification.
3. **Making progress, history and results beautiful and fascinating** ("I genuinely enjoy exploring workout statistics, sleep reports, personal records, trends and historical comparisons. This is a major part of the product's appeal.")
4. **Understanding lifestyle and functioning**: honest, optional personal analytics. "The fourth priority adds depth; it must not overwhelm the first three."

The 25 Oct handoff added a fifth, lowest rung: lifestyle links (Health, calendar, location context).

## 4. What it must feel like

> "I've never used an app quite like this, but everything feels natural."

> "I want something: Radically original. Sophisticated. Mature. Extremely beautiful. Cohesive. Intuitive. Tactile. Fluid. Delightful. Precisely crafted. Visually memorable."

> "Restraint must not mean blandness … originality must not mean visual aggression."

> "Cleanliness, richness and originality should coexist." "Clean AND rich. Those are not opposites."

> "What I would like is tons of polish microinteractions" (21 Oct)

> "Just please great looking clear structure" (25 Oct)

> "Make sure paddings margind etc are right, make sure all dunctionality still intact, check every single component and make sure its right, make sure every element has interactions, make sure again that nothing is hardcoded in a way where dynamic data wouldnt support it" (24 Oct, his own polish checklist)

And the failure he keeps naming: **"It still looks very much like ai slop."** (21 Oct, 23 Oct twice). "I do not want obviously AI-generated UI."

## 5. His non-negotiables (binding outcomes)

**Psychological safety (perfectionism + ADHD)**
- "No destructive streaks." Missing days never destroy progress. Avoid the word "kept" (reads as a streak).
- "Unrecorded ≠ missed." Missing data is never zero, never abstinence, never a forgotten dose.
- Graceful return after any absence: "It should still feel beautiful, welcoming, and worthwhile … I don't have hundreds of incomplete tasks to resolve."
- No 1–10 ratings: "I worry about whether I've chosen the correct number." Zero mandatory subjective input; optional "Feel/Function" recording must still exist (he called its removal a regression, 19 Oct).
- No chores: "Also things like this toggle, why have it? The app becomes a chore" (23 Oct). Remove settings that don't earn their place; pick sensible defaults.
- "Don't make me do more work in Meridian so Meridian can tell me more about my life."

**Scope and generality**
- Unlimited custom routines with any measure (yes/no, quantity, minutes, sessions, reps, imported) and any cadence (daily, n per week, weekly, n per month, every N days/weeks, calendar periods), pause / resume / retire, targets editable "without rewriting historical achievements".
- "Routine names must not determine the interaction mechanism." No bespoke gesture, animation, report or suggestion rule per routine. "A routine I create tomorrow should become eligible … without requiring you to code a custom rule for its name."
- Must work with 5 routines and with 60.
- Examples are tests, not the product: "Our repeated failure has been narrowing the product around whichever example was most recently discussed."

**Safety and honesty**
- Never reward consumption (caffeine, alcohol, medication quantity, extra water or exercise). Observations are neutral.
- No invented scores (no ADHD, focus, stress or 0–100 habit-strength score). A transparent, qualified summary score is allowed where honest (he likes his Sleep Cycle score).
- No fabricated correlations or causal claims. "A system that sometimes says 'we don't know' is preferable."
- No LLM required for logging, navigation or statistics; direct control always.

**Not this list:** task manager, planner, journal, chatbot, medical dashboard, ADHD tracker, sleep app, walking app, decorated checklist, "a game bolted onto a habit tracker".

## 6. What he loves (evidence of taste, never designs to copy)

- Results: Sleep Cycle morning score, Apple Watch workout stats, Strava breakdowns. "The results of an activity can become part of the reward for performing the activity."
- Engagement: chess, Clash Royale, social media, building with Claude. "Clues about possible engagement mechanisms, not designs to imitate."
- Look and feel: **Not Boring apps (Andy Allen)** "equally for their visual design and satisfying animations and interactions". Blind taste test (20 Oct, `reference/taste-findings.md`): loved Oura, Sleep Cycle, Endel, Opal, Halide, Gentler Streak, Bevel, Tiimo, Partiful, NB Habits, NB Weather; rejected Things 3, Streaks, Duolingo; 0 of 10 flat generated styles. Pattern: lit depth and material, one confident hero, heavy physical feedback (loved "mechanical key" and "liquid fill"). Not childish.
- "I dont want to copy a look, I want it to be unique, refresshing" (23 Oct).

## 7. Where he is now (29 Oct)

> "I am not 100% happy with the final result, everything needs to be validated again - from UI and flows to logic itself. I am open to everything changing if backed by evidence."

> "Figure out how to make it do the actual validations, proactive thinking verifications so I dont have to constantly interject and make sure to do the extra step. Final product needs to be really polished."

> "It needs to know what the actual goal is … What I want. And it needs to be proactive to acheieve it."

So: the web prototype is evidence, not a spec to port. The approved look (§ 02-HISTORY) is the strongest signal of taste so far, but even it can change if evidence shows something better, shown to him as a small sketch first.

## 8. Still unsolved, and he knows it

**Gamification.** "Gamification remains a central UNSOLVED problem … Do not silently downgrade gamification into pleasant logging animations, weekly summaries and milestone counters … if you cannot find a credible long-term game mechanism, say it remains unresolved." Every candidate so far was rejected (see 02-HISTORY §5). He wants motivation *before* action, not only nicer feedback after it: "none automatically explains why I would feel excited to perform an activity before I've performed it."

**Smart suggestions.** "I love the suggestions idea. Would like to make it truly smart, based on what you are doing and where you are. This will be enforced by push too." Then: "I think we drop the only one constraint" (Now shows due routines plus a couple of context-fit suggestions, marked and ranked).
