# Flow and sense-check findings, 23 Oct (build 2e5157ee)

**Why:** Mark asked 7 questions (23 Oct 09:51) and added "I am sure we can find other non sensical things too". These are researched decisions, not rules applied blindly. Microinteractions and visual polish are out of scope.

**Evidence:** review/flow/{a,b,c,d,e,f}/ holds findings.md and PNGs per track:
- a: logging types, meals
- b: scheduling, plan-the-week
- c: pebbles, copy, categories
- d: whole-app simplification
- e: a new user with their own routines for a week
- f: every screen with the seeded data

**Studio builds everything in sections 2–4.** Section 1 is the answer to Mark.

## 1. Mark's questions: the answers

| # | Question | Decision | Mark's suggestion |
|---|---|---|---|
| Q1 | Stretching, friends: tap, not timer? | Logging follows the measure type, never the name. Stretching is seeded as a timed session, so change it to "Done or not". Friends is already one tap; the "1 h" on the suggestion is an invented estimate (`suggestModel` falls back to 60) and goes. Routines marked "With others" never appear in "If you have a moment". Add "How it's recorded" in routine settings (history kept). | Right on stretching and the suggestion row. Friends was already a tap. |
| Q1b | Morning card to pick a friends goal | Don't build it. A morning choice with nothing to bring it back fails by evening (ADHD time-based memory; ef-support C §6), it rewards choosing, and it becomes a daily chore. The weekly friends rhythm plus Held already does the job. Only change: the suggestion's "Some other time" becomes "Bring it back…" with Held's moments. | His doubt is correct. |
| Q2 | Trash every Thursday | It's a commitment with a deadline, not a "some time this week" routine. The build can do it today, but it takes 8 taps through "Hold something › By a date", and nobody would find it. Add a Log row "Something with a date": name, then Mon–Sun chips, then Weekly (6 taps). Add "Give it a date instead" in the composer's weekly step and in search. A missed Thursday moves to the next one, with no backlog. | — |
| Q3 | Meals: small/big? Is lunch, nuts or ice cream a meal? | No size split. Anything eaten is one tap. The purpose is regular eating despite appetite suppression, plus meal timing vs energy, and both need only timestamps. Snacks are part of regular eating (CBT-E: 3 meals plus 2–3 snacks). About text: "Anything you eat counts: a lunch, a handful of nuts, an ice cream. It records when you ate, not what or how much." Row: "1 of 3 · last 12:05". Milestones count days at target, not meal totals (totals would reward eating or logging more). | No split needed. Lunch, nuts and ice cream all count. |
| Q4 | Plan the week? | It isn't a feature. It's a sample routine an early AI build brief invented. It earns milestones, which rewards planning (against GR-25), and research rejected a weekly planning ritual (EF-79). Remove it from the seed, starters and example text. No ledger item depends on it. | Right to question it. |
| Q5 | Pebbles in Time? | Yes, they're still there: Time's year, the week story, routine pages, You and onboarding. Their shape is random and means nothing. Replace them with the light-behind-ribbed-glass he picked for Today, at Time's scales (see 2.1). One version, no options round; he can veto it on the live build. | Right. |
| Q6 | Sketching "first step" so specific? | It's not generated; it's seeded text in an optional field. It can't honestly be generated without an LLM. Keep it as optional text the user may add: after a session routine's first completed session, ask once "Note a first step for next time? (optional)", never again. With no text, session rows show "Start with 5 min". | Partly right: never required, but don't drop it (IN-54). |
| Q7 | Baseline categories? Water glass for push-ups | No categories. They break contract R-01 and his own 18 Oct rule against permanent categories, add a choice at creation, and there is no evidence-based "baseline" list (the closest, the ACLM pillars, has no water or sunlight). The glass comes from a bug: any amount routine gets the water tumbler. The object should come from measure + unit: a volume unit gets a glass; other amounts get a light column filling toward the aim; sessions get one rib per session; events get slot ribs; observations get quiet grey. The dead "Fill appearance" switch becomes a working "Show as a glass". | Right about the symptom, wrong about the remedy. |

## 2. BLOCKING: things that only work for the seed person
Mark would see these as nonsense the moment he adds his own routine. The fix is always generic: select by fields, never by routine id or day of year.

1. **Pebbles to LightGlass (Q5).** One shared component, also flat SVG.
   - Time root: 52 week ribs, set-aside weeks frosted, future weeks clear, tap opens the month.
   - Week story: 7 day bands.
   - Routines › item: one rib per session (heights against a fixed reference, BD-11) or slot ribs.
   - Onboarding: the sample year uses the same ribs, and each picked routine becomes a lit rib; "one stone each" copy goes.
   - Later, and not gating: Month dial, sleep blocks, You module stones. The run route stays (Mark: "original is fine").
2. **Amount routines are water everywhere (Q7, E1, F-B1).** "20 ml of 20 pages", "0 L since", "First glass", the "20 ml" chip, the 250 ml target step, "5 min" chips for pages, and the glass in Settled.
   - Format every amount with `fmtAmount(it, v)` and the item's unit.
   - Milestones are multiples of the target; the first one is "First entry".
   - Step size comes from the unit or presets.
   - Glass only per the Q7 rule.
   - Lines: 5260–5265, 5609–5612, 5675, 5743, 8109, 8243, 9446, 11911, 14320, 14525, 15536–15538, 16494, 27250.
3. **Units (E2).**
   - The unit sits inline in the "An amount" card, not below the fold.
   - Free-text unit with suggestions.
   - No 1500 default.
   - Plural unit words.
   - The ml/pages/km-only picker goes.
4. **Target sheet for routines without a target (E3).** It shows "Per undefined days / Next none". When there is no cadence, show a Day/Week/Month period, so "20 pages a day" and "at most N coffees" can be set (CG-22).
5. **Starters carry the seed person (E4).**
   - "Call someone close" becomes "Parents", with the seed's first step, 20 min and evening.
   - `starterItem` keeps only measure, cadence, target and glyph; chips use the starter's name.
   - Add a Name row to routine Settings (there's no rename anywhere today).
6. **Invented history (E5, E6, E11, F-B2).** Gate everything on the user's first use, never on day of year or scenario. No "usual" without history.
   - "usually 20 min" on day one.
   - Patterns "3 pairs" from seeded caffeine and alcohol pairs on day one: show pattern rows only for inputs that exist and are on.
   - "Held most: … 2 months" after one entry: a month counts only once it's closed, or after 2 closed periods.
   - A pre-install week reads "a quieter week": no story before first use.
   - "5 sessions in about 32 weeks" after one entry: divide by min(8, weeks used) and hide until there are 3 entries.
   - "Day one" card on day 7.
   - "Six months in" fires on calendar days 180–186 with water, guitar and call stats, "In January", and running pace for everyone. Trigger it 182 days after first use, using the top 3 routines, and show pace only with runs in both windows.
7. **Hard-wired routine ids (C6-F4, F-B3, F-P4, E8).** Select by field everywhere:
   - Watch, widget, Lock Screen and Siri previews use `byId.water`/`byId.guitar`: use the most-logged amount routine and the most-logged session routine.
   - Six-months stats.
   - The Friends→next-day pattern uses `fits:'With others'`.
   - Curated pairs, and Recent workouts use `source:'watch'`/`linkW`.
   - "Tonight: No…" uses the user's every-time or at-most observations.
   - The caffeine-only rich path: observation results show the count or amount neutrally (not recorded or not-recorded bars).
   - The Observations module label "Alcohol and caffeine" and the "Seen" name are built from item names, and the module is called "Observations".
8. **Health off still says "your Watch" (E7).** Use one `healthOn` predicate for Sleep, Workouts, the Time rows and "Also count Watch workouts". The Watch link only appears on movement sessions.
9. **Copy that contradicts settings (E9, C6-F2, F3).**
   - "How this counts" is built from `everyTime`.
   - `aboutFor(it)` derives the about text from fields: Watch / feeds / observation / count.
   - Reminder text comes from the stored rule.
   - Date night is given a rule the editor can make.
10. **"Didn't do it today" on an every-2-weeks chore (E10).** Check `everyN`; the wording is "not this window".
11. **Names cut to "Clean the" (E12).** No automatic short name; truncate in the layout with an ellipsis.
12. **Icons guessed from substrings (E13).** Brunch gets a runner and Swimming a drop. Match on word boundaries and add an icon picker next to Colour.
13. **Prototype has no +1 day (E20).** Mark can't test his own routines across days. Add ±1 day chips under You › Prototype that keep the user's data.

## 3. Simplifications (accepted)
1. **Today cards (D2).**
   - Cards hold results and arrivals only, newest first (last night before yesterday's run).
   - Held and dated items appear only as Now rows, not also as a card and a teaser.
   - Add the missing "Done" on the passed-date sheet.
2. **Log sheet (D3).** Four doors lead to one line of text. Keep "Hold something" (gains "No particular time") and "Something happened" (the same sheet as Context). Drop "An idea", which also dead-ends when ideas are off.
3. **Composer (D4).** Drop "Usually takes" and "Fits best" from creation; they stay in Settings. Add a "Once a week" quick chip. Reminder days default to none, not Wednesday (E16).
4. **You (D5).** One Records list, the module switch inside each module page, no duplicate Feel block, "Seen" renamed "Observations".
5. **Header Held icon (D6).** Show it only when something is held, with a count.
6. **Time (D7).** Drop the "Last week, as a story" row; Weeks already ends in "Play it as a story". "Look closer" becomes "Reports and patterns".
7. **"Now as a day line" (D8).** Remove the switch and the layout. Mark never asked for it, rejected "Day Line" on 18 Oct, and it conflicts with CG-18. Mark is told.
8. **Context sheet (D9).** Lead with Sick, Away and Holiday plus a span; the other six go under "Other kinds of day".
9. **Privacy (D10).** Merge the three rows into "Privacy and your data". Screen Time and Shared routines go into one "Coming later" row.
10. **Dated items are never folded on Today (D1, part).** The Thursday rubbish stays visible.

**Rejected:**
- D1's fold of Later to one line. Mark asked for Later as a "rest of today" rail on 22 Oct 12:50, and his ask wins.
- Removing Routines › Observations/Measures (KD-12).
- Removing the header Search (access rule 19).

## 4. POLISH (doesn't gate)
- **Labels and wording**
  - "Held" means both a routine that met its aim and a parked intention. Reserve "Held" for intentions and use a plain word for routines, such as "met its aim". Do not use "kept": Mark's rules say it reads as a streak (F-P1).
  - Lowercased names, and the story omits user-created routines (E14).
  - Grammar: "1 times", "Last 1 weeks" (E15).
  - Every-2-weeks is grouped as "Every few days" (E17).
  - "Making room for it" ×5 (E21).
  - "Worth remembering" heading shown with nothing under it.
  - Year range unit repeated.
  - `unitWord` id cases.
- **Wrong or misleading numbers**
  - Time headlines run km every week; distance should come second and use the main workout type (F-P2).
  - The Weeks page treats paused daily routines as quieter and says "yesterday" in a past week (F-P5).
  - "against 1 h" on session pages (F-P7).
  - The focus check seeds 20, not 10 (F-P9).
  - "Yesterday" logs get today's clock time (E22).
- **Behaviour**
  - Intentions show three different clocks; show minutes only if the user set an estimate (F-P6).
  - Watch-recorded Running offers a phone stopwatch; suggestions only fit when the estimate fits the gap (F-P8).
  - Borrowed defaults: every 4 days, a 17:30 workday cue the user never set, 10–60 min hold presets for a 2 h routine (E16).
  - Gratitude has nowhere to write an optional line (E18).

## 5. Direction changes
None. D8 removes a built feature Mark never asked for, so he is told rather than asked. An Opal-style rendered object for Time would need his pick; it is not proposed.

## Must not lose
The ledger ids are listed per item in each track's findings.md. The round-11 review re-runs the full 620-item ledger.
