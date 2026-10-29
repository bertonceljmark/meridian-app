# 17 · Feature ledger (20 Oct)

Every product requirement from all 34 of Mark's messages in owner-messages.md plus CONTRACT v1.1.1, deduplicated to one line each and assessed by driving Studio's Step 1 build (evolve/meridian.html, md5 f3406895) in Playwright at 390×844.
Step 1 totals were 354/158/72/21. Re-checked on Step 2A (evolve/meridian.html md5 7c2e178c, 20 Oct ~21:00): all 230 open items re-driven. Step 2A: 378/157/49/21. Re-checked on Step 2B (md5 325b2b1d, 20 Oct ~23:00), incl. 48 never-rules the new suggestions could break. Step 2B: 439/131/14/21. Re-checked on Step 2C (md5 bbb1927a, 21 Oct ~00:40). Step 2C: 468/112/4/21. Re-checked on Step 2D (md5 4b3874b6, 21 Oct ~02:30). Totals below.
Live page (Mark corrects here): https://claude.ai/artifact/7q81yN3Kpg2c2yAX4UqU8A · data: review/ledger/feature-ledger.json
Provenance: own = Mark's informal words; contract = approved contract; brief = long structured brief (may be AI-drafted). 'how unconfirmed' = mechanism never endorsed by Mark; the outcome stands.
Method: 6 extraction agents (1,735 raw lines with verbatim quotes, script-checked) → 5 merge+assess agents. Cross-area duplicates remain (e.g. 'never reward medication' appears under Gamification and Medication).

CURRENT (Step 2D): 487 present · 93 partial · 4 missing · 21 iPhone-only.


## Logging & undo

- **Present** (was Missing) [LG-04] I can change the water preset amounts to my own familiar quantities · contract · how: customisable presets  
  Build: Water logger "Edit" / Settings > Familiar amounts: removed 150, added 400; Save → Today row and logger show 250/330/400/500/750.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g, CONTRACT §0, CONTRACT §R-11
- **Present** (was Missing) [LG-10] I can add my own custom caffeinated drinks · contract  
  Build: Caffeine logger "+ Add a drink": name + mg range → "Matcha latte ≈ 40–80 mg" added to familiar servings, loggable.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-11
- **Present** (was Partial) [LG-11] Familiar supplements (e.g. L-theanine) can be logged quickly with their usual serving · brief  
  Build: Log › Supplements: + Add a supplement (Iron 14 mg added, one-tap), 6 familiar servings; L-theanine chip logs 200 mg. Item page leaks alcohol/caffeine copy.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [LG-16] Anything recorded can be inspected, corrected or reversed, including merges and links · brief  
  Build: Entry sheet: time/amount Save correction, Remove entry; Same one now links (no crash) with 'Unlink, they were different' + Undo; contexts editable.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [LG-17] Timestamps and time zones are handled correctly · brief  
  Build: Unchanged: time chips only; Search 'time zone' finds nothing; no time-zone handling visible.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [LG-22] I can start, pause and finish a timed session, and finishing moves from doing to results · brief  
  Build: Start→live bar Pause/Resume→End→length sheet→'Session saved' (length, settled this window, vs usual 40 min, lifetime count, Undo).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Partial** [LG-25] Statuses mean the same everywhere: recorded, skipped, none, unknown, planned, completed, paused, retired · brief  
  Build: Unchanged mix: 'Didn’t do it', 'Paused · nothing expected', intentions 'resting, not overdue', 'Kept as started', 'unknown, not missed'.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [LG-26] An explicit "none" or "skipped" can be recorded, even after the fact, distinct from not recorded · contract  
  Build: "Didn’t do it today" in loggers (toast "nothing is owed", item moves to Later as "not today"); Day view "Not recorded" Add it/Didn’t do it toggle.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-09, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [LG-01] Recording feels pleasurable and gives clear feedback on what changed; reviewing it is meaningful · brief  
  Build: Water preset: digits roll, toast "+250 ml · 830 ml of 2 L"; completing a period plays a short burst then settles; Day view timeline in Time.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [LG-02] Logging stays fast, unambiguous and forgiving for water, meals, medication, feel and simple routines · contract  
  Build: Water preset and Later chips log in 1 tap; Log sheet groups items with a one-tap quick button per row; item page has Log now / Start.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, CONTRACT §R-11, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [LG-03] Water is logged in one tap from familiar amounts (150 / 250 / 330 / 500 / 750 ml) · contract · how: presets 150/250/330/500/750 ml  
  Build: Today water tile shows 150/250/330/500/750 presets; one tap logs and shows new total with Undo.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §0, CONTRACT §R-11, cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g
- **Present** [LG-05] Ordinary logging never needs typed numbers or a learned gesture (never) · brief  
  Build: All amounts are chips/presets; no number keyboard anywhere in logging; hold is optional (opens full logger).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [LG-06] Meals are recorded with a quick confirmation that supports eating regularly · contract · how: one-tap meal confirmation (unconfirmed)  
  Build: Later chip "Meals" logs in 1 tap: toast "Logged · Meals, 2 of 3 today", Undo.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-11
- **Present** [LG-07] No calorie counting or food weighing, and logging a meal never implies it was nutritionally adequate (never) · contract  
  Build: Meals is a count; About text: "A quick confirmation that you ate. It doesn’t measure what or how much."  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-11
- **Present** [LG-08] Activities are recorded as sessions with a type and a duration (e.g. 30 min walk) · brief  
  Build: Log → Movement → Already done it: type chips (Walk, Run, Strength…) + 10–60 min, "Log 30 min".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [LG-09] Caffeine is logged by familiar drinks (Turkish coffee, espresso, vending, Red Bull, Monster…) with estimated mg · contract  
  Build: Log → Caffeine shows 8 drinks with ranges ("≈ 50–90 mg"); tap Turkish coffee → toast "2 today · ≈ 191 mg estimated". Recent chip re-logs.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-11, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** [LG-12] Exposures such as alcohol are easy to log from familiar drink/serving choices, not unit maths · contract · how: drink/serving presets (unconfirmed)  
  Build: Log → Alcohol: Beer 0.5 L / 0.33 L, Wine 150 ml, Spirit 40 ml, Cocktail, Cider; one tap, time chips.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, CONTRACT §R-10
- **Present** [LG-13] Cannabis (or similar) logging never assumes the potency is known (never) · contract  
  Build: No potency field anywhere; a user-made "Something I notice" item logs only the event. No cannabis preset exists.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, CONTRACT §R-10
- **Present** [LG-14] Every log can be undone immediately, and undo feels natural · contract  
  Build: Every log toast has Undo; tapping it restores ("Undone · Water is back where it was", 830→580 ml).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, CONTRACT §R-11, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [LG-15] Past entries can be corrected sensibly (time, amount, remove) without inviting obsessive re-editing · contract  
  Build: Item page → Recent entries → entry sheet: ±15 min/1 h/Day before, amount chips, Save correction; Remove entry has Undo.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §R-09, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** [LG-18] How something is logged comes from its measure type (never its name), so new routines get it automatically · brief  
  Build: Composer step 2 "What counts" picks the measure: "The same choice decides how it’s logged everywhere"; Log groups by measure.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [LG-19] Each measure has its own feedback: a confirmation, an amount added with new total, an event landing in its history · brief · how: per-measure interaction primitives (unconfirmed)  
  Build: Done → completion burst; water → "+250 ml · 830 ml of 2 L"; headache event → toast + Day view timeline row.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [LG-20] Feedback always reflects a real change; success is never shown when nothing was recorded (never) · brief  
  Build: Toasts only follow a stored entry; weekly Done disabled when met; logging past aim says "not counted as more".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [LG-21] No ceremony or unnecessary confirmation screen for water, a meal or a simple event (never) · brief  
  Build: Water/meal/event log in 1 tap with a toast; only Retire asks for confirmation.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [LG-23] Rapid repeated taps are safe, each tap clearly meaning one more entry with feedback and correction · brief  
  Build: 4 fast taps on 150 ml → 4 entries (580→1.18 L); toast updates each time with Undo.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [LG-24] A routine can be logged several times in one day (e.g. water) · contract  
  Build: Water logged repeatedly same day; tile shows "N glasses, last 08:32".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-03
- **Present** [LG-27] Missing data never counts as abstinence, a skipped dose or a failure (never) · contract  
  Build: Day view "Nothing recorded… unknown, not missed"; Time legend "unknown, not missed"; med "Unknown, not missed".  
  Src: CONTRACT §R-09
- **Present** [LG-28] Motivation features never slow logging, navigation, analytics or accessibility, nor gate tracking (never) · brief  
  Build: Moments are optional (You → Contextual moments switch); logging works directly from Today and Log without them.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u

## Routines: create & edit

- **Partial** (was Missing) [RT-13] Health evidence informs defaults and recommendations · brief  
  Build: Unchanged: Health only in composer water guidance; no Health-driven defaults elsewhere.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [RT-19] A routine can carry an estimated duration so suggestions fit the time available · brief · how: routine property: estimated duration (unconfirmed)  
  Build: "Usually takes" drives Today "A good moment for": I have about 15 min shows only Stretching (10 min); 1 h shows Friends/Stretching/Movement.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [RT-20] A routine can carry optional preferred circumstances (when/where it fits best) · brief · how: routine properties: contextual eligibility, preferred circumstances (unconfirmed)  
  Build: "Fits best" used in suggestion reasons (Short night: "Movement, a short one · fits outdoors · free until 09:00").  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Partial** [RT-10] Choose how a routine is measured: events, amounts, time, sessions, repetitions, confirmations, passive · brief  
  Build: Composer 'What counts' now 8 kinds (adds How it is for me); Watch-measured/passive still not selectable.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** (was Partial) [RT-12] Sensible defaults per measure type speed up creation · contract · how: defaults per measure type (unconfirmed)  
  Build: Defaults per kind: amount "At least 1.5 L a day", sessions "3 a week", time "20 min a day", reps "50 a day", done "Once a day".  
  Src: CONTRACT §R-06
- **Present** [RT-01] Unlimited custom routines with no arbitrary cap · contract  
  Build: 'New routine' always available; 60-configured scenario holds 28 active, 14 paused, 18 retired  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, CONTRACT §R-02, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [RT-02] Add new routines whenever I choose, progressively, without rebuilding anything · brief  
  Build: Created 'Pottery class' mid-year in 5 steps; it appeared in Today at once ('Not yet this week · 6 days left')  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [RT-03] Any personally meaningful recurring behaviour (physical, mental, relational, social), not a fixed catalogue · contract  
  Build: Composer step 1 is a free name ('e.g. Deep clean the flat'); no category picker; 60 scenario has Spanish, Floss, plants  
  Src: CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-01, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** [RT-04] No behaviour needs a medical justification, and the app isn't limited to physical-health habits (never) · contract  
  Build: Composer asks only name, what counts, how often, reminder; no health reason or category required  
  Src: CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY
- **Present** [RT-05] Examples (walks, volleyball, date night) are tests, never hardcoded categories, special features or the app's purpose (never) · contract  
  Build: Routines grouped by cadence only; Date night is an ordinary event routine; no 'Relationships' category anywhere  
  Src: CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** [RT-06] One generic routine model: no new routine needs bespoke interaction, animation, rule, report or integration (never) · contract  
  Build: New 'Haircut'/'Pottery class' got the same Today row, Results, Growth, In Time and Settings as built-in routines  
  Src: CONTRACT §R-01, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [RT-07] A new routine automatically fits Today, progress, growth and history with the same good interactions · brief  
  Build: Haircut detail: Results ('first window still running'), Growth ('first entry becomes first milestone'), Open in Time  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [RT-08] Specialised interactions only where they materially help, never as a prerequisite · brief  
  Build: Run report and water presets are extras; every routine works through the generic row/sheet  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** [RT-09] Creating a routine is simple, not an elaborate configuration workflow · contract  
  Build: New routine: 5 short steps (Name, What counts, How often, Reminder, Ready) with one choice each  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-06, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [RT-11] Choose frequency and target while creating, covering the full cadence range briefly · contract  
  Build: Composer step 3: Day/Week/Month/Every N/None with At least/About/At most and stepper  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §R-06, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [RT-14] Optional reminder settings when creating a routine · brief  
  Build: Composer step 4 'A reminder? Optional. Quiet, once, never repeated' with No reminder / last day of window  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [RT-15] A routine detail view · brief  
  Build: Tapping any routine row opens detail: hero progress, Results, Growth, In Time, Recent entries, Settings  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [RT-16] Relationship routines are tracked plainly; relationship quality is never rated or quantified (never) · brief  
  Build: Date night logs as an event with one tap; no rating or quality field anywhere  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY
- **Present** [RT-17] Routines may involve another person, e.g. walking with my girlfriend · brief  
  Build: Any free name works (e.g. a shared walk) without special support; nothing person-specific is needed  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [RT-18] Practice, social, occasional longer and daily-practice routines all work · contract  
  Build: Guitar practice (sessions), Time with friends (weekly), Reading (no target), Stretching (daily) all present  
  Src: CONTRACT §R-01, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [RT-21] The multi-routine purpose is never dropped because one habit has stronger evidence (never) · brief  
  Build: Today, Routines and Time all treat 15–28 varied routines equally; walking is one of many  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g

## Cadence, goals & changes

- **Present** (was Partial) [CG-20] Non-daily routines create no daily obligation; a month-long target is never treated as an urgent daily task (never) · contract  
  Build: Back after 5 weeks: Now holds only Water; Date night under Later › This month "aim 2"; suggestions "nothing is suggested" first days back.  
  Src: CONTRACT §R-04, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [CG-01] Daily routines with daily targets, including ones done several times a day (e.g. water) · brief  
  Build: Routines: 'Water · At least 2 L a day', 'Regular meals · At least 3 a day'; composer Period=Day with count  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [CG-02] Weekly and several-times-a-week routines (e.g. volleyball once a week, walking 3x a week) · brief  
  Build: Routines 'Every week' group (Movement at least 3 a week, Call parents once a week); composer Period=Week  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [CG-03] Per-calendar-month targets like a date at least twice a month; a one-date month is not a failure · contract  
  Build: Date night 'At least 2 a month · 1 of 2 in October'; results show 'partly', never failed; new monthly routine counts from today  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, CONTRACT §AS-03
- **Present** [CG-04] Custom intervals such as every N days or every six weeks · brief  
  Build: Composer How often → Every N with days/weeks switch; created 'Haircut · Once every 6 weeks'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [CG-05] Calendar periods where they fit (month, week) and rolling windows for every-N cadences · contract · how: cadence: calendar or rolling periods (unconfirmed)  
  Build: Month/Week are calendar ('1 of 2 in October'); Every N uses rolling windows ('This 2-week window · 14 days left')  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, CONTRACT §7
- **Present** [CG-06] Occasional routines with no fixed target or cadence at all · contract · how: cadence: none (unconfirmed)  
  Build: Composer Period=None: 'No target: it’s simply recorded… Nothing can be behind'; Reading listed under 'No target'  
  Src: CONTRACT §AS-04, CONTRACT §7
- **Present** [CG-07] The full range of frequencies (several a day to monthly, irregular, infrequent), not just daily and weekly · contract  
  Build: Routines groups: Every day / Every week / Every month / Every few days / No target; all creatable in composer  
  Src: CONTRACT §R-04, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [CG-08] Targets can be at least, at most, about, or none · contract · how: target comparator at_least|at_most|about|none (unconfirmed)  
  Build: Composer Target segment At least/About/At most + Period None; How often sheet 'Kind of target' has all four  
  Src: CONTRACT §7
- **Present** [CG-09] Change a routine's target at any time · contract  
  Build: Routine → Settings → How often sheet: stepper + Save; Movement changed to at least 4 a week  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-04
- **Present** [CG-10] Changing a goal never rewrites past achievements; each period is judged by the target in force then · contract · how: target history with effective dates (unconfirmed)  
  Build: After edit, 'Target history: From Mon 2 Nov at least 4 / 1 Feb – 1 Nov at least 3'; past bars unchanged  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, CONTRACT §R-05, CONTRACT §R-05 / §7
- **Present** [CG-11] Changing a target mid-period is handled: the current rule is clear and past periods stay unchanged · contract  
  Build: How often sheet: Starting 'Next week | This week', 'Takes effect Monday 2 November. This week stays as it is.'  
  Src: CONTRACT §AS-06
- **Present** [CG-12] Pause, resume and retire routines (active / paused / retired) · contract · how: active/paused/retired states  
  Build: Detail Settings: Pause / Resume ('Starts counting again from today') / Retire; Routines header '15 active · 2 paused · 3 retired'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §R-02, CONTRACT §R-05, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** [CG-13] Paused and retired routines keep their history and growth · brief  
  Build: Retired Walks detail still shows Results, Growth (12 h, milestones) and In Time  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [CG-14] Paused spans are left out of evaluation and shown distinctly · contract  
  Build: Paused Movement: 'Nothing is expected; logging still works'; Results bars marked 'paused' in legend  
  Src: CONTRACT §R-05 / AS-07
- **Present** [CG-15] Periods spanning a pause, travel, sickness or a target change, and other changes in circumstances, are handled · contract  
  Build: Results summary '1 set aside or paused'; Time marks sick/travel/away spans; target history splits periods  
  Src: CONTRACT §R-04, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [CG-16] A retired routine can be brought back with its history kept · contract  
  Build: Routines → Retired Show 3 → Walks → 'Bring it back'; detail returns with 'Growth only grows' intact  
  Src: CONTRACT §R-05 / AS-07
- **Present** [CG-17] Pausing or retiring a routine never implies personal failure or loss of identity (never) · brief · how: 'Earlier' section/state (unconfirmed)  
  Build: Retired list reads 'Became Movement on 1 Feb', 'Tried for two months'; 'Their history and growth are kept'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC
- **Present** [CG-18] Routines are not tied to a fixed time of day (never) · contract  
  Build: Composer never asks a time; Later chips show learned 'usually ~21:30' only. Reminders can still carry a clock time  
  Src: CONTRACT §R-04, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY
- **Present** [CG-19] Low-frequency, irregular, relationship and social routines are first-class, not assumed high-frequency · contract  
  Build: Date night, Time with friends, Sketching every 4 days, Haircut every 6 weeks sit beside daily items in Today and Routines  
  Src: CONTRACT §R-04, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [CG-21] Completing a weekly or monthly period is acknowledged · brief · how: interaction primitive: period completion (unconfirmed)  
  Build: Logging 2nd Date night: burst + toast 'Date night settled for October · 2 of 2'; moves to Settled  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [CG-22] Optional reduction intentions, e.g. alcohol at most N a week or less caffeine · brief  
  Build: Alcohol 'At most 4 a week' observation; composer At most works for any item. Caffeine itself is observation-only  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [CG-23] A reduction target counts as met only with enough explicit evidence; unknown stays unknown (never) · brief  
  Build: Alcohol detail: 'Unconfirmed weeks stay unknown: two drinks and then silence isn’t a result'; bars 'unknown'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** [CG-24] Reduction goals never demand daily abstinence confirmations (never) · brief  
  Build: Alcohol asks only one optional weekly 'That’s everything'; no daily prompt anywhere  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** [CG-25] A low-friction way to supply evidence for a reduction goal when I want to · brief  
  Build: Alcohol detail 'Last week: 2 logged · That’s everything' one tap → week counted as confirmed within  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** [CG-26] Weekly effort feels rewarding without punishing lapses; goals guide without dominating · brief  
  Build: Results use 'at target / partly / unknown, not missed'; Growth 'only grows'; period-settled burst  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w

## Today / home

- **Partial** [TD-02] Today is not a checklist, habit grid, planner or record-then-progress-bar loop (never) · brief  
  Build: Default Today still Now rows with check/+/Start, Later chips, By a date lane; day line opt-in.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [TD-07] Today avoids too many competing blocks (moments, now, later, settled, week) fighting for attention · brief  
  Build: Unchanged: moments, Now, By a date, Later, A good moment for, Settled, This week all on Today.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [TD-09] Today differs sensibly between a busy day and a quiet day · brief  
  Build: Unchanged: Short night lightens suggestions + calendar gaps; Now list same as base day.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [TD-10] Today has something good to show when there's nothing to do · brief  
  Build: Unchanged: 'Nothing to suggest right now. That’s fine'; no all-done state.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [TD-12] Today changes through the day · brief  
  Build: Prototype Clock: at 11:40 Meals joins Now; 18:00 'fits evening' reasons; 21:30 Stretching into Now, Water to Later, suggestions reshuffle.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [TD-14] No duplicate suggestions or repeated calls to action in several places (never) · brief  
  Build: s60 day line 100%/135%: each item once (Water row above line, line/Also around then/Later disjoint); list mode no repeats; also checked at 21:30.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [TD-17] A small focus set beside a larger catalogue, never blocking anything outside it · contract · how: focus set (unconfirmed)  
  Build: Unchanged: no user-chosen focus set; Now is automatic.  
  Src: CONTRACT §H-06, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [TD-01] Opening the app on an ordinary day shows what's relevant across several kinds of routines, quick to record · brief  
  Build: Today: Now (6 of 15 in play) mixes daily, weekly, monthly, every-N items with one-tap controls  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [TD-04] Rewarding and useful from day one with little or no data; depth grows over time · contract  
  Build: Time travel 1 Jan: 'Day one · 10 routines, all starting today. Nothing is behind.' no '0 of'  
  Src: CONTRACT §R-18 / AS-11, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [TD-05] Today shows what deserves attention now; the rest stays available without always being displayed · brief  
  Build: Now (in play) vs Later one-tap chips vs Settled; everything else reachable via Routines/Log  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [TD-06] A contextual suggestion may appear but never dominates; the app stays fully useful when it has nothing to say · brief  
  Build: You → Contextual moments off removes the cards; Today, logging and Routines work unchanged  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [TD-08] Advanced depth never overwhelms the everyday experience (never) · contract  
  Build: Patterns, sleep, workouts live under Time → Look closer; Today shows at most one pattern card (switchable)  
  Src: CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** [TD-11] Rewarding feedback right after an action · brief  
  Build: Water preset → toast '+250 ml · Water 830 ml of 2 L' with Undo; period completion gives a burst  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [TD-13] Explanations are revealed only on request · brief  
  Build: 'See the evidence', 'Open the report', 'More…' reveal detail; Today shows one-line summaries  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [TD-15] Never feels like a manager allocating my evening or constantly demanding input (never) · brief  
  Build: No prompts or schedules; Later chips show only 'usually ~21:30'; check-ins 'never prompted'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [TD-16] Depth is available but the everyday experience never demands continuous improvement (never) · contract  
  Build: No improvement goals or nudges on Today; patterns say 'nothing here asks you to change anything'  
  Src: CONTRACT §R-19
- **Present** [TD-18] Open app, meet an activity, decide, record, get feedback, then jump to its history or reports · brief  
  Build: Today row tap → routine detail with Results/Growth/Open in Time; run card → 'Open the report'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u

## Scale & many items

- **Partial** [SC-01] Today stays calm and manageable however many routines are configured, even on a busy day · contract  
  Build: 60 configured: Now 7 rows, Later 13 chips, 3 suggestions; Today ~3.9 screens tall.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §AS-04, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Partial** [SC-04] High-frequency routines like water never visually drown out rarer, more significant ones · brief  
  Build: Unchanged: Water still largest Now row with 5 preset buttons.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC
- **Partial** [SC-05] Works with real, substantial data and many items, not just five routines and perfect synthetic data · brief  
  Build: Own records scenario adds headaches/melatonin/2nd med, but still synthetic seed data; no real import.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Present** [SC-02] Every routine stays discoverable and reachable at 20, 40 or 60 routines · own  
  Build: 60 configured: all alive items reachable from Today chips; Routines grouped by cadence with 'Find a routine' search  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFAhZJN3mnWpZLXv2gNNurL, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [SC-03] A large catalogue (e.g. 60 configured, 12 active) stays manageable with minimal friction, no imposed scheme · contract · how: catalog (unconfirmed)  
  Build: Routines header '28 active · 14 paused · 18 retired'; paused/retired collapsed; search 'pia' → Piano  
  Src: CONTRACT §R-02 / AS-12, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-02

## Return, lapses & no backlog

- **Present** (was Partial) [RL-11] Tell a genuinely missed activity apart from one I simply didn't record · brief  
  Build: Any routine logger has "Didn’t do it today/this week"; Day view "Not recorded" toggle marks past days; Results legend "didn’t do it".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC
- **Present** [RL-01] Missing days or breaks never destroy accumulated progress (no destructive streaks) (never) · contract  
  Build: Detail Growth 'only grows… Gaps, pauses and sick weeks never take any of it away'; no streak counters  
  Src: CONTRACT §0, cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY
- **Present** [RL-02] No punishment or shame for missed days, lapses, resting or stopping something (never) · contract  
  Build: Results say 'unknown, not missed' and 'partly'; no red marks, warnings or failure copy found  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §P-1, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, CONTRACT §R-21
- **Present** [RL-03] No backlog of overdue records or pile of incomplete tasks, even after months of use (never) · brief  
  Build: Back after five weeks: 'Welcome back. Nothing piled up.' Routines show only the current period  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Present** [RL-04] Never required to repair, backfill or complete past records (never) · contract  
  Build: No prompts to fill gaps; unrecorded days stay 'nothing recorded: unknown, not missed'  
  Src: CONTRACT §R-09, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [RL-05] Returning after weeks away is welcoming and previous progress is intact · contract  
  Build: Back after five weeks scenario: welcome card 'Everything you built is where you left it'; Growth totals kept  
  Src: CONTRACT §AS-10, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §0
- **Present** [RL-06] Never pressured to explain an absence (never) · brief  
  Build: Welcome card asks nothing; offers only 'See those weeks in Time'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [RL-07] I can resume immediately after returning · brief  
  Build: Return Today: 'today starts like any other day'; Now list ready to log at once  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [RL-08] Interruptions and gaps feel normal, not catastrophic or uncomfortable · brief  
  Build: Growth lists 'Back after 13 days, after being sick · picked up where you left off' as a positive milestone  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [RL-09] After an absence, Watch data is shown, manual gaps stay unknown, and no missed records are invented · contract  
  Build: Time → Sep: 'Away from the app… Your Watch kept recording sleep and workouts. Everything else is unknown, not missed.'  
  Src: CONTRACT §AS-10, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [RL-10] Missing data is never treated or animated as failure or as proof a routine stopped (never) · brief  
  Build: Time disc and Results legend: 'nothing recorded: unknown, not missed'; quiet weeks shown neutral  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [RL-12] Missing data never automatically pauses, breaks or completes a routine without a defensible rule (never) · brief  
  Build: After 5 weeks away routines are still active with history; nothing auto-paused or auto-completed  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC
- **Present** [RL-13] A missed suggestion is not a missed routine (never) · brief  
  Build: Dismissing a Today moment card (×) changes no routine; routines' results unaffected  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [RL-14] A partly completed period never feels like failure (never) · brief  
  Build: Results label such weeks 'partly' in a neutral tone; e.g. 'Of the last 15 closed weeks: 12 at target, 2 partly'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG

## Kinds: behaviours, observations, outcomes

- **Present** (was Missing) [KD-20] Shared or social routines as a possible future capability · brief · how: Company (unconfirmed)  
  Build: You › Shared routines: 'Preview · not available yet' page (who/what/counting/no pressure/leaving), mock Date night card, 'Tell me if it becomes available'.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** (was Missing) [KD-23] Relationship routines may optionally capture extra information if a design justifies it · contract  
  Build: Date night logger has an "Optional note" field ("a few words") before "Log date night now".  
  Src: CONTRACT §0
- **Partial** [KD-06] Optionally track detrimental exposures: late caffeine, alcohol, cannabis, late screen use, skipped meals · brief  
  Build: Unchanged: caffeine/alcohol built in; Search 'cannabis'/'skipped' finds nothing; others only as own observation.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** (was Partial) [KD-10] Exposures integrate naturally with analytics and custom tracking · brief  
  Build: Own records: Headache, Melatonin, Hay fever tablet in Patterns catalog with honest pace labels ("Too early · about 42 more weeks · 6 days and 73").  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** (was Partial) [KD-14] My own observations (e.g. melatonin) can record amount, timing and other details where known · contract  
  Build: Own records: Melatonin logger "Amount · optional 0.5 mg / Don’t know"; composer "Also note": amount, when it started, how long.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, CONTRACT §R-10
- **Present** (was Partial) [KD-15] Any new measurement can be recorded, categorised, interpreted and explored in analysis · brief  
  Build: New items join catalog + Explore; "I note it every time" switch on analysis page makes Guitar comparable (86 vs 97 days, "No clear difference").  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [KD-19] Worthwhile one-off activities can matter without counting toward a numeric target · brief  
  Build: Intention Done → Day view row 'Done · counts toward nothing'; Routines › Intentions › Done list keeps it with time; toast no NaN.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Partial** [KD-25] The same topic can exist as an observation and a behaviour (skipped meals vs regular meals) · contract  
  Build: Unchanged: Regular meals 'Didn’t do it'; no linked Skipped meals observation.  
  Src: CONTRACT §R-08
- **Present** [KD-01] Routines are not all checkboxes: each routine has its own measure type · contract  
  Build: Composer offers Each time, Done or not, Sessions, An amount, Time spent, Repetitions, Something I notice.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, CONTRACT §R-03, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** [KD-02] Measures include confirmation, quantity, minutes, sessions, repetitions and single events · brief  
  Build: Vitamin D (done), Water (ml), Reading (min), Guitar (sessions), Push-ups (+20 reps), Date night (event) all log as such.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [KD-03] Routines can be fed by automatically imported measurements · brief  
  Build: Daylight "measured by your Watch. Nothing to log"; Movement and Running filled by Watch workouts.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [KD-04] Observations such as caffeine are never rewarded or celebrated for consumption, and never shamed (never) · contract  
  Build: Caffeine/alcohol toasts are neutral grey "Noted · …"; Observations page "Noticed, not rewarded"; no judgement copy.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §R-08, cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po
- **Present** [KD-05] Recording a supplement never implies it works (never) · contract  
  Build: Vitamin D About: "Recording it says nothing about whether it works."  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-11
- **Present** [KD-07] I can create my own observation types, not only the predefined examples · brief  
  Build: Routines → New routine → "Something I notice" → named item appears in Log and Routines → Observations.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [KD-08] Missing exposure entries never mean abstinence; an explicit "no use" is distinct from no information (never) · brief  
  Build: Alcohol week counts only after "That’s everything"; Patterns use only confirmed weeks; unconfirmed = unknown.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po
- **Present** [KD-09] Meridian never becomes a substance-use tracker; exposures stay off-centre (never) · contract  
  Build: Observations are absent from Today; they sit under You → Records and Routines → Observations.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, CONTRACT §R-10
- **Present** [KD-11] An exposure can be a neutral observation or carry an optional reduction intention · contract  
  Build: Alcohol: Intention "At most 4 a week"; Caffeine: no target; Intention sheet offers At most / No target.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, CONTRACT §R-08
- **Present** [KD-12] Three kinds coexist: behaviours (reinforced), observations (tracked or reduced), outcomes (understood) · contract  
  Build: Routines page sections: routines, Observations "noticed, not rewarded", Measures (Sleep, Workouts, Feel, Medication).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, CONTRACT §R-08
- **Present** [KD-13] Outcomes include sleep, workouts, physiology, subjective functioning and long-term change · brief  
  Build: Measures: Sleep report, Workouts, How you feel; Patterns outcomes: sleep, overnight HR, energy; Time year growth.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY
- **Present** [KD-16] No dedicated hard-coded features for single cases like melatonin or headache (never) · brief  
  Build: Headache made through the generic "Something I notice" type; no special-purpose screens.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [KD-17] The data model covers recurring behaviours, one-off events, quantities and durations · brief  
  Build: Recurring routines, event measure, ml/reps quantities, minute durations; Intentions hold one-off items.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [KD-18] One real-world event serves several purposes without duplicate records · brief  
  Build: A Watch run counts for Running and Movement once (Movement about text "never twice").  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [KD-21] A measurement is kept distinct from a behavioural goal · brief  
  Build: Sleep/Workouts are Measures with no target; routines carry targets.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [KD-22] No routine, including relationship routines, ever requires a quality rating (never) · contract  
  Build: Event logger: "It counts. There’s nothing to rate."; Date night/Call parents log in 1 tap.  
  Src: CONTRACT §0, CONTRACT §R-01
- **Present** [KD-24] Kind sets reward treatment only; in analysis any item can be cause or outcome · contract  
  Build: Patterns filter "Sleep after / Sleep before": "The same night can play either role."  
  Src: CONTRACT §R-08

## Feel, function & symptoms

- **Present** (was Missing) [FF-06] Validated questionnaires used only sparingly · brief · how: validated questionnaires (unconfirmed)  
  Build: Module 'Questionnaire and focus check': WHO-5, 5 items worded answers, Skip, Save → '64 of 100 · not a diagnosis'; next from 10 Nov.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Missing) [FF-07] Voluntary focus-session measurements · brief · how: focus sessions (unconfirmed)  
  Build: Start a focus check: 10 dot trials, result '112 ms typical tap', device caveat, 'Save this check' / 'Don’t save'.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Missing) [FF-19] Events can carry optional generic details such as onset and duration · brief  
  Build: Headache logger: "When it started" (Just now…Woke with it) and "How long it lasted · optional" (Still going…Most of the day).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [FF-01] See whether medication, sleep, exercise and nutrition relate to how I function day to day · brief  
  Build: Catalog compares meds, meals, movement, sleep with energy/feel; Vitamin D, meals, movement now checked; energy pairs honestly "Not knowable at current pace".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Partial** [FF-05] Lower-burden, behaviourally specific signals of functioning (e.g. got started easily) instead of self-ratings · contract · how: behaviourally anchored choices (unconfirmed)  
  Build: Check-in words like 'got started easily' now selectable as Explore outcomes; still optional words, no other low-burden signals.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §4
- **Partial** [FF-08] Device activity and passive health data used as context for functioning · brief  
  Build: Focus check now in Patterns when module on (0 results); Screen Time still feasibility page + sample numbers, no device data.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [FF-21] A generic optional self-report item type I can create, its form decided by research · contract · how: self-report item type (unconfirmed)  
  Build: Composer › How it is for me: None→a lot / Yes or no / own words (4 inputs); logs from Log › In your words; Explore input+outcome. Item page shows '0 min'.  
  Src: CONTRACT §R-13
- **iPhone only** [FF-11] Screen use split into overlapping sleep, awake and possibly distracting, using real sleep times and caution · brief  
  Build: Not in prototype: You → Screen Time says the numbers can’t be read by apps; nothing simulated.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [FF-02] I can optionally note how I feel or function, simply, with no conversation or questionnaire · contract  
  Build: You → How you feel → Check in (also Log → How you feel): one tap on a field, optional words, toast with Undo.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-13, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [FF-03] Feel and function recording is never removed for simplicity (never) · brief  
  Build: Check in present in You, Log and Routines → Measures; module on by default.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [FF-04] No 1–10 ratings or invented numeric scores just for charting (never) · contract  
  Build: Feel is a tap on a pleasant/energy field plus words; history shows words, not numbers; footer "No scores and no ratings".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-13 / AS-14
- **Present** [FF-09] No ADHD severity, focus, stress, productivity or functioning score from indirect data (never) · contract  
  Build: No score anywhere; Patterns only show pairs with uncertainty; Feel page "No scores and no ratings".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §R-13
- **Present** [FF-10] Phone use, movement, HRV or heart rate never presented as measuring ADHD, mood or motivation (never) · brief  
  Build: HR appears only as overnight heart rate outcome (alcohol pair); no claim it measures symptoms.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [FF-12] Screen Time is never judged good or bad; night-time YouTube playback is never read as distraction (never) · brief  
  Build: No Screen Time judgement anywhere; Screen Time page is neutral and suggests an optional phone-free routine only.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [FF-13] ADHD functioning is optional support, never the product identity or a clinical symptom dashboard (never) · contract  
  Build: No symptom dashboard; Feel is one optional module in You → Modules.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, CONTRACT §R-13
- **Present** [FF-14] Optional notes can cover energy, fatigue, mood, clarity, initiation, concentration, motivation, irritability, stress · contract · how: candidate dimensions (unconfirmed)  
  Build: Field axes pleasant/energy + words: tired, focused, clear-headed, hard to start, motivated, irritable, overwhelmed, scattered.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-13
- **Present** [FF-15] Feel entries can be occasional or event-triggered (e.g. "felt overwhelmed today") · contract · how: event-triggered input (unconfirmed)  
  Build: Check in any time from You or Log; "overwhelmed" word chip; nothing scheduled.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §AS-14
- **Present** [FF-16] Subjective tracking needs very few, low-effort optional interactions and never becomes a chore · brief  
  Build: Whole check-in is one tap ("That’s the whole check-in"); words optional; nothing required.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [FF-17] No imposed check-ins, daily questionnaires, mandatory ratings or end-of-day reconstruction (never) · contract  
  Build: Feel never prompted ("never prompted"); picker records now only; no reminder option for feel.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, CONTRACT §R-13, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** [FF-18] I can record an occasional symptom such as a headache without creating a daily habit · brief  
  Build: Routines → New routine → "Something I notice" → Headache: no target, logs via "Log now", "noted, never rewarded".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** [FF-20] Prefer passive and real-event data; what can’t be measured, or wasn’t recorded, stays unknown · brief  
  Build: Patterns footer: "days you didn’t record count as unknown, never as zero"; feel gaps "are normal".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [FF-22] Sparse feel logging causes no nagging, backlog or guilt (never) · contract  
  Build: Feel page: "Gaps are normal; this is never asked for."; no reminders or counts of missed check-ins.  
  Src: CONTRACT §AS-14

## Medication

- **Present** (was Partial) [MD-10] Explore how medication timing relates to functioning, without fabricated conclusions · brief  
  Build: Med analysis: same-day "Energy later that day"/"rest of that day" + next-day outcomes; "A record, not medical advice"; honest Too early labels.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** (was Partial) [MD-02] Medication tracking is generic: any medication and regimen (or none), including dose changes · brief  
  Build: Medication: rename, unit mg/ml/tablets, "new dose applies from" Today…Two weeks ago with history (1 Jan–26 Oct 36 mg, since 27 Oct 46 mg), Add another.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [MD-16] Medication can be tracked locally in Meridian when Apple Health is unavailable or unwanted · brief  
  Build: Per-medication "Read doses from Apple Health" switch; new med defaults Off ("only what you log in Meridian"); Stop tracking keeps history.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **iPhone only** [MD-15] Uses authorised Apple Health medication data where available · contract · how: HealthKit medication read (unconfirmed)  
  Build: Simulated: records tagged "Apple Health"; Connections says it reads medication. Real HealthKit read only judgeable in iOS.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §P-3
- **Present** [MD-01] Medication tracking is optional and never defines the product · contract  
  Build: You → Modules → Medication switch; when off, page says module off; Today never shows medication.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-12
- **Present** [MD-03] Record that a dose was taken, with its time · contract  
  Build: Log → Morning medication: "Taken · 36 mg" + time chips; You → Medication → Record a dose.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §P-3, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** [MD-04] Record an explicitly skipped dose · contract  
  Build: Log → Medication "Skipped today, on purpose"; past unknown day sheet "Skipped, on purpose" → toast "Recorded as skipped".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §P-3
- **Present** [MD-05] Note when a dose was later than usual or a different amount from the regimen · contract · how: configured regimen  
  Build: Amount chips 18/27/36/54 mg; list shows "later than usual" and "different amount" chips; calendar marks both.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, CONTRACT §P-3 / AS-13, CONTRACT §P-3
- **Present** [MD-06] Taken, late, different amount, skipped and unknown are all kept distinct · contract  
  Build: Medication calendar legend: Taken 20 · Later than usual 1 · Different amount 1 · Skipped 1 · Nothing recorded 4.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, CONTRACT §P-3, CONTRACT §AS-13
- **Present** [MD-07] Missing medication records are never read as a forgotten or skipped dose (never) · contract  
  Build: Unrecorded days show "Unknown, not missed"; sheet "It stays unknown unless you add something" with "Leave it unknown".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §P-3
- **Present** [MD-08] Medication records can be corrected · contract  
  Build: Tap a day → Correct the time ±15 min/1 h, Amount chips → Save correction → toast "Record corrected", row tagged corrected.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §P-3
- **Present** [MD-09] Review medication history directly, from an easy-to-find place · brief  
  Build: You → Records → Medication: month calendar + last two weeks list with sources; also Log → Medication → Open records.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [MD-11] Never advise on dose, infer efficacy, or suggest changing or skipping medication (even for experiments) (never) · contract  
  Build: Page: "Record · no rewards, no advice"; "gives no medical advice"; no suggestions anywhere.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, CONTRACT §P-3
- **Present** [MD-12] Extra doses or medication quantity never earn rewards (never) · contract · how: planned-adherence acknowledgment (unconfirmed)  
  Build: Dose logs give neutral grey toast "Recorded · 36 mg"; no burst, no progress, not on Today.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §P-3 / R-22
- **Present** [MD-13] Medication records look precise and neutral and are not rewarded for their own sake · brief  
  Build: Neutral grey hue, plain times and mg; no celebration on record.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [MD-14] Medication never dominates the home screen or visual identity (never) · brief  
  Build: Today shows no medication; it lives under You → Records; private on Lock Screen by default.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [MD-17] Medication sources are shown and Health vs manual duplicates of one dose are merged · contract  
  Build: 27 Oct sheet "Where this came from": Apple Health 08:10 + Logged in Meridian 08:12, shown as one dose; remove duplicate.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §P-3 / AS-13

## Life events & context

- **Present** (was Partial) [LE-05] An optional normal work schedule as a context source · brief  
  Build: Your usual week drives Patterns: unchecking Thu/Fri changed moved→sleep from 184 to 111 nights; copy matches.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Partial** (was Missing) [LE-06] Sleep and wake records used as a context source · brief  
  Build: Sleep feeds Patterns (Sleep the night before, Waking near usual) and Short night; Context page still doesn’t use sleep.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Missing) [LE-16] Note an external life event (e.g. "My car broke down") as a one-line entry with no severity or category · brief · how: free-text lightweight observation (unconfirmed)  
  Build: Context sheet "Something happened?" / Day view chip / Context page: one-line note, no category; saved "Boiler broke" shows in Day timeline.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** (was Missing) [LE-20] Prolonged, delayed or recurring effects of an event can be related back to it without an incident record · brief  
  Build: Event sheet lists entries from 3 weeks after to link ("My car broke down · 2 later things next to it"); copy says not a cause.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [LE-26] A configurable end-of-work event can trigger reminders (better than geofence when working from home) · brief · how: end-of-work event trigger (unconfirmed)  
  Build: You › Context › Your usual week: 'Work usually ends' stepper (17:30→18:00); Reminder › After… 'When your workday ends 18:00' follows it.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Partial** (was Missing) [LE-27] Reminders adapt during travel and sickness · brief  
  Build: Unchanged: reminders sick/away Pause/Keep and local-time copy; delivery not shown.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [LE-02] Day contexts: vacation, sick, travel, off work, unusual hours, part-day work, weekend, stress · contract  
  Build: Context sheet: Workday, Day off, Travel, Sick, Away, Unusual hours, Holiday, Part-day work, Stressful; weekends via Your usual week.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-15, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [LE-03] No rigid rule-based interpretation of days (never) · brief  
  Build: Patterns › Sick and travel days Left out/Included; each detail shows both views + By context (workday vs day off); 'nothing is left out on its own'.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Partial** [LE-04] Context is understood with minimal admin, inferred from sources like calendar and sleep where possible · contract · how: work schedule, calendar, sleep/wake, date ranges, one-tap overrides, weekday (unconfirmed)  
  Build: Unchanged: Your usual week manual; calendar flight only in Short night; contexts manual.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §4
- **Present** (was Partial) [LE-07] Optional vacation or illness date ranges · brief · how: date ranges (unconfirmed)  
  Build: Context sheet "Dates…": From/To steppers; past range 22–26 Oct set Sick (shown in Time); future Lisbon 9–13 Nov listed "planned".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [LE-09] Day of week and other reliable passive data used as context · brief  
  Build: Workday from Your usual week now used across all sleep comparisons (night counts change when days toggled).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [LE-14] Context and timing change what an exposure means (a drink on holiday vs before a workday) · brief  
  Build: Drinks → HR detail › By context: Before a workday (1 and 107) vs Before a day off or holiday (5 and 41), side by side.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po
- **Present** (was Partial) [LE-15] A vacation is not treated like an unsuccessful working week · brief  
  Build: Holiday context rests routines: Today "Routines are resting while you’re on holiday", Now hidden, suggestions quiet.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Partial** [LE-19] A recorded event is not an order to ignore data or rewrite every reminder and finding (never) · brief  
  Build: Patterns now keep sick days in both views, but Context › Sick still 'sets routines aside' wholesale, no per-routine choice.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [LE-23] A recorded trip can shape suggestions and, separately, inform analysis · brief  
  Build: Travel context quiets suggestions ("Travelling: suggestions stay quiet today"); travel days left out of analysis; planned trip editable.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [LE-24] Suggestions hold back when I’m sick, travelling, exhausted or already committed · brief  
  Build: Suggestions hold back: Sick "nothing is suggested", Holiday/Travel quiet, Back "first days back", short night/stressful → lighter versions.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Partial** [LE-28] Travel, including time zones and mixed work-and-travel days, is inferred without location tracking · contract  
  Build: Unchanged: calendar flight proposes travel (Short night only); no time zones.  
  Src: CONTRACT §R-15, CONTRACT §AS-08
- **Present** [LE-01] Unusual life circumstances don’t corrupt statistics: context decides which days are compared · brief  
  Build: Patterns: "Sick and travel days are left out"; Time shows Sick/Montréal/Away spans; raw entries kept.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [LE-08] Context is set or overridden with one tap and lasts for a span · contract · how: one-tap context; time spans (unconfirmed)  
  Build: Today → Context chip → Travel + "A week" → "Travel, 27 Oct – 2 Nov"; tap again clears.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-15 / AS-08
- **Present** [LE-10] Never assume Monday means work or Saturday means leisure; no silently inferred work schedule (never) · contract  
  Build: "Workday" is only set by the user; Context chip reads "none set" by default.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §R-15
- **Present** [LE-11] A single day can hold several contexts · contract  
  Build: Set Travel then Workday: chip reads "Travel · Workday until 2 Nov".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-15
- **Present** [LE-12] Unknown context stays unknown · contract  
  Build: Default chip "Context none set"; nothing guessed for today.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-15
- **Present** [LE-13] Context never needs retroactive cleanup of my history and never becomes a chore (never) · contract  
  Build: No prompts to classify past days; contexts optional.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-15
- **Present** [LE-17] Never ask me to rate, scope, classify or keep re-confirming a life event or adjust analyses myself (never) · brief  
  Build: No such prompts exist anywhere; contexts are single taps.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [LE-18] Never require a diary or turn Meridian into a journal (never) · brief  
  Build: No journal or diary feature.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [LE-21] The app never invents how severe an event was, how long it lasted or what it changed (never) · brief  
  Build: No inferred severity anywhere.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [LE-22] Analytics stay useful even if I never record a life event · brief  
  Build: Patterns work from routines, Watch and observations with no context input.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [LE-25] A sick week or travel period is recognised with little admin, no punishment and progress intact · contract  
  Build: Time travel 15 Mar: "Nothing here is expected of you this week… never counted as misses", "I’m better now".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §AS-19

## Gamification & reward

- **Missing** [GR-02] Gamification is never quietly reduced to log animations, weekly summaries, milestone counters or a number rising (never) · brief  
  Build: Unchanged (skipped): settle ripple/toast, weekly story, milestones, Session saved; new Weeks and Year pages add more summaries, no gameplay  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Missing** [GR-15] Progression changes the experience itself and evolves with my routines, not just bigger numbers · contract  
  Build: Unchanged (skipped): Today/Routines look the same at any stage; Growth totals and milestone lists only grow; Year page is history, not progression  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-20
- **Partial** (was Missing) [GR-28] Makes activities attractive before I do them: anticipation, curiosity, commitment and a reason to start · brief  
  Build: Unchanged: reasons + 'First step:' lines on Now, Start 15 min, one idea a day ('Sounds good'); no anticipation or curiosity mechanic  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Missing** [GR-34] Engagement through mastery, strategy, meaningful choice, short loops and experimentation · contract · how: mastery/strategy/short loops/choice (unconfirmed)  
  Build: Unchanged (skipped): no strategy, mastery or experimentation loop; suggestions still Start/Not now/⋯ cards  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU52nZRGUysVB5Joy6bn9kkc, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, CONTRACT §4
- **Partial** [GR-01] Meridian is genuinely gamified: real healthy actions are the gameplay and the emotional centre, not an analytics journal · contract  
  Build: Unchanged: settle ripple + toast, Growth/milestones, story, Session saved; new Weeks/Year/Patterns pages are analytics, not gameplay  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, CONTRACT §1, CONTRACT §R-20
- **Partial** [GR-05] Long-term progression never runs out and never depends on a finite set of rewards or badges (never) · contract  
  Build: Unchanged: Movement 'Next milestone: 150 sessions, in about 17 weeks'; threshold milestone list, no open-ended progression  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g, CONTRACT §0, CONTRACT §R-20 / AS-20
- **Partial** [GR-13] Healthy actions accumulate meaningfully across a day and week into something interesting · brief  
  Build: Unchanged: day/week accumulate as totals ('Day 2 of 7', '1 of 3'); Weeks page lists per-routine 'settled'/'at the aim on N days'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Partial** [GR-14] After six months something worth seeing has developed and there are reasons to keep coming back · contract  
  Build: Time › Look closer adds Weeks (‹ › every week) and Earlier years; richer record, but month ten still looks like month one on Today/Routines  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, CONTRACT §R-20 / AS-20
- **Present** (was Partial) [GR-23] Never encourage excess water, exercise, medication, supplements or caffeine, or push beyond a target (never) · contract  
  Build: Session saved: 'longer than your usual 35 min' neutral, 'shorter… counts the same'; Growth caps past aim; no push beyond target  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §R-11, CONTRACT §R-22, CONTRACT §AS-01
- **Present** (was Partial) [GR-24] Never nudge me to log extra things just to complete a picture or distort real behaviour to fit the game (never) · brief  
  Build: No nudges to log extras; Questionnaire never prompted; 'Already done' logs usual and offers 'a different amount…'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [GR-29] Supports initiation, the activity itself and the reward afterwards as different moments, only where it helps · brief  
  Build: Initiation (reasons, First step, Start 15 min), activity (live bar, past-usual cue), and after: 'Session saved' sheet with week progress, length vs usual  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Partial** [GR-31] Rewarding moments stay meaningful at the 50th, 100th, 200th time and over months, not just as novelty · brief  
  Build: Unchanged: every session ends in the same Session saved sheet, logs same toast/ripple; nothing keeps it meaningful at the 200th time  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Partial** [GR-32] Moments of excitement, curiosity, discovery and delight beyond logging feedback and milestones · brief  
  Build: Unchanged: one idea a day from 38-idea library ('Look up the history of your street'); otherwise toasts and milestones  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Partial** [GR-33] Builds a sense of ownership, competence and mastery I'm emotionally invested in · brief  
  Build: Unchanged: mastery only for running pace; other routines show settled weeks / days at aim / lifetime counts  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Partial** [GR-35] Creative agency for the user as a source of engagement · brief · how: creative agency (unconfirmed)  
  Build: Unchanged: own ideas, colour/glyph, Water skin, new self-report 'own words'; no creative agency as engagement  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Partial** [GR-36] Doing my whole collection of routines is enjoyable even when single routines (like water) aren't · brief  
  Build: Weeks page lists all routines for a week ('11 with something settled'); still a list, nothing makes the whole set enjoyable  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Partial** [GR-40] Different kinds of routines (relationship, enjoyable, necessary) get different kinds of satisfaction · brief  
  Build: Unchanged: all routine pages share Results/Growth/milestones/Recent entries template; Session saved same for every timed routine  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Partial** [GR-43] Periodic landmarks give fresh starts without feeling like a reset · contract · how: periodic landmarks (unconfirmed)  
  Build: Unchanged: week close note only; Weeks page is browsing past weeks, no fresh-start landmark at week/month turns  
  Src: CONTRACT §H-02
- **Partial** [GR-50] Rewards are things I genuinely value, not decorative visualisation · brief  
  Build: Unchanged: run report/pace valued; most rewards remain milestone flags and toasts; new Weeks/Year are stats  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Partial** [GR-55] An interesting long-term progression with a compelling reason to keep routines, satisfying across seconds to months · contract  
  Build: Growth + Weeks + Earlier years give a long record; reads as history, not a compelling reason to keep going  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §R-20
- **Partial** [GR-58] Treats enjoying the app, returning, acting in real life and sustaining behaviour as distinct goals · brief  
  Build: Unchanged: suggestions, dates lane, reminders serve real-life action; nothing distinct for enjoying the app or returning  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC
- **Partial** [GR-59] Meaningful in-app experiences around real behaviour (not only planning) are allowed and present · brief  
  Build: Adds Pattern detail › The days behind it, Weeks, Year; still read-only views beside run report, story, live cue, Session saved  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **iPhone only** [GR-10] Feedback uses motion, haptics, visual transformation, sound and physicality · brief · how: motion/haptics/sound (unconfirmed)  
  Build: Prototype simulates haptics as island labels ('light tap', 'success haptic', 'soft tick') plus a ripple; no sound; real haptics need iOS  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [GR-03] No game bolted onto the tracker: no unrelated minigame, decorative world, missions or second set of in-app chores (never) · contract  
  Build: No minigame, world or missions; Questionnaire/focus check are opt-in modules off by default, never prompted  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, CONTRACT §1, CONTRACT §R-20
- **Present** [GR-04] Not a literal game: no XP, levels, streak counters, stars or collectible sets as the system (never) · brief · how: XP/levels/streaks/collectibles  
  Build: No XP, levels, streaks, stars or collectibles; Session saved shows plain counts  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [GR-06] Individual achievements or badges are allowed alongside open-ended progress · contract · how: achievements/badges (unconfirmed)  
  Build: Routine pages show milestones, firsts and bests (Water: '400 litres', 'First glass', 'Back after 23 days away')  
  Src: CONTRACT §0
- **Present** [GR-07] No destructive streaks: a gap never wipes out what was built (never) · brief  
  Build: No streaks; Growth 'Gaps, pauses and sick weeks never take any of it away'; back after 5 weeks 'Nothing piled up'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [GR-08] Lifetime accumulations and achievements are never lost and survive interruptions; evaluation never lowers them · contract · how: lifetime accumulations (unconfirmed)  
  Build: Routine Growth section labelled 'only grows' with lifetime litres/dates; comeback entries ('Back after 23 days away'); retire keeps growth  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §7, CONTRACT §H-01, CONTRACT §R-21
- **Present** [GR-09] Every log gets immediate, worthwhile acknowledgment, even for short or small actions · brief  
  Build: Water preset → toast '+750 ml · Water 1.33 L of 2 L' + ripple; Stretching chip → 'settled for today · 80 sessions since 6 Apr'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [GR-11] Feels rewarding without becoming slow, childish or a forced multi-step ceremony · brief  
  Build: Reaching 2 L water: one ~1 s ripple, row turns 'Water settled for today', toast with Undo; nothing blocks the next tap  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [GR-12] Partial days and periods still count and feel worthwhile; no all-or-nothing · contract  
  Build: Results bars show 'partly' separately from 'at target'; story lists '6 of 7 days'; Today shows '1 of 3' without failure language  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-20 / AS-01
- **Present** [GR-16] New or changing routines fit naturally into progress and visuals without breaking the model · brief  
  Build: Composer (Routines→New routine) adds to Today/Log/Time/Routines; new routine shows Growth empty state 'first entry becomes the first milestone'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [GR-17] Every routine type and cadence gets fitting progress feedback, no special cases (daily, weekly, monthly, every-N) · contract  
  Build: Water (daily L) and Date night (2 a month) pages both get Results, Growth, milestones, bests; Sketching every 4 days; Reading no-target  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, CONTRACT §0, CONTRACT §R-20, CONTRACT §R-20 / §7
- **Present** [GR-18] A routine added midway through the year works naturally · brief  
  Build: Date night created Feb: Growth 'since 1 Feb', Results by month from Feb, milestones from 'First date 6 Feb'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY
- **Present** [GR-19] Travel, sickness and weeks away from the app don't break progress or engagement · contract  
  Build: 'Back after five weeks' scenario: 'Welcome back. Nothing piled up'; Time marks Sick/Montréal/Away spans; comeback milestone on routine page  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, CONTRACT §R-20
- **Present** [GR-20] Changed, paused or retired routines keep their progress and history · brief  
  Build: Retire confirm: 'history, milestones and growth stay'; Paused section 'nothing expected'; Target history 'past periods keep the rule'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY
- **Present** [GR-21] Low-frequency or irregular activities never create artificial daily obligations (never) · brief  
  Build: Date night stays '1 of 2 dates · 5 days left'; dates lane lists real deadlines only; no daily prompts for low-frequency items  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** [GR-22] Observations, medication and consumption are recorded but never rewarded or gamified (never) · contract  
  Build: Medication 'a record, no rewards'; observations not in suggestions; WHO-5 results listed 'not a diagnosis', no reward  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, CONTRACT §R-08, CONTRACT §P-1
- **Present** [GR-25] Choosing, planning or holding an intention is never rewarded as if it were done; no planning busywork as progress (never) · brief  
  Build: Holding/starting an intention rewards nothing: 'Kept as started · 1 min so far', no Session saved/Growth for intentions  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [GR-26] No shame, pressure, artificial urgency, manipulation, compulsive variable rewards or grinding (never) · contract  
  Build: No pressure copy: 'nothing is ever overdue', 'Nothing is recorded, nothing is missed'; mild 'Due today', '6 days left' only  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouU52nZRGUysVB5Joy6bn9kkc, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, CONTRACT §R-22
- **Present** [GR-27] Aims at real-world behaviour, not screen time or compulsive checking (never) · brief  
  Build: No feed; at most three suggestions; reminders off by default with daily limit  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Present** [GR-30] Results afterwards feel worthwhile; real accomplishments and workout reports can be the reward themselves · brief  
  Build: Today run card → full report: route, splits, HR zones, 'Compared with recent runs: 2nd fastest of 23'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [GR-37] Mundane repetitive routines get low friction, fitting encouragement and a place in the bigger pattern · brief  
  Build: Water presets log in one tap; Later chips one tap with undo; settle feedback; daily routines feed Time spokes  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** [GR-38] Not every activity needs entertainment; the whole day of tracking need not feel like a game · brief  
  Build: No per-activity game layer; date night, volleyball, water just log and settle  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [GR-39] Relationship routines get meaningful positive progress and history · brief  
  Build: Date night page: Growth '15 dates', milestones, 'Most in a month: 3 dates', 'First date'; Parents '19 times so far' on 30 Jun card  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY
- **Present** [GR-41] Personal records and comparisons appropriate to every domain, including rare routines · contract · how: personal records (unconfirmed)  
  Build: Bests per routine ('Most in a month: 3 dates', 'Longest', 'Biggest day'); run report compares to previous 8 runs  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, CONTRACT §H-04
- **Present** [GR-42] Never present a consistency estimate or 0-100 habit-strength score as measured automaticity (never) · contract · how: habit-strength rating (unconfirmed)  
  Build: No habit-strength score; WHO-5 0–100 is a wellbeing questionnaire, sleep summary score off by default and labelled placeholder  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, CONTRACT §H-03
- **Present** [GR-44] Gives value on day one with no imported history · brief  
  Build: Time travel 1 Jan: 'Day one · 10 routines, all starting today. Nothing is behind'; first entry becomes first milestone  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** [GR-45] No exaggerated identity statements from sparse or incomplete records (never) · brief  
  Build: Copy factual; no identity statements in suggestions, Session saved or ideas  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC
- **Present** [GR-46] Social or shared routines are optional, never mandatory, monitoring or accountability pressure (never) · brief  
  Build: Shared routines preview: opt-in invite, 'no leaderboards, no nudges about the other person, no streaks'; nothing sent  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** [GR-47] Spontaneous gestures are never turned into compulsory routines or transactions (never) · brief  
  Build: Idea 'Sounds good' toast: 'Enjoy it. Nothing is recorded unless you make it a routine.'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [GR-48] Motivation needs no extra admin or maintenance; progress never requires administrative work (never) · brief  
  Build: Progress automatic from logs and Watch; suggestions/ideas need no setup  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [GR-49] No arbitrary or meaningless rewards for just using the app; follow-through rewarded without making life transactional (never) · brief  
  Build: No rewards for opening/tapping; Sounds good/Not now record nothing  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [GR-51] Doesn't imitate referenced products or reuse rejected mechanics (cards, seasons, rankings, feeds, chapters) (never) · contract  
  Build: No decks, seasons, rankings, feeds or chapters; Shared preview has no leaderboards  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU52nZRGUysVB5Joy6bn9kkc, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, CONTRACT §6
- **Present** [GR-52] Motivation feels like one app with stats, reports, history and context, not two joined together · brief  
  Build: Growth lives on each routine page next to Results; story and six-month card draw on the same data  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [GR-53] No single measurement or metaphor defines the whole motivational system (never) · contract  
  Build: Feedback spread across settle, Growth, records, report, Patterns, Session saved; no single score  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFJqyjjvzyuFPZND4VetQ41, CONTRACT §1
- **Present** [GR-54] Numbers and statistics are never forced onto activities where they aren't meaningful (never) · contract  
  Build: Reading 'No target'; Date night as dates; ideas carry only an approximate length  
  Src: CONTRACT §0
- **Present** [GR-56] Familiar mechanics are allowed if they earn their place; no mechanic banned just because earlier versions failed · contract  
  Build: Prototype uses milestones and records where they fit  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, CONTRACT §R-23
- **Present** [GR-57] Motivation works whether I have few or many routines · brief  
  Build: 60 configured scenario: Today groups 28 alive items; each routine still has Growth; 1 Jan with 10 routines works  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [GR-60] Reaching a target I set gets appropriate feedback · brief  
  Build: Water hits 2 L → row becomes 'Water settled for today' with ripple, 'success haptic', moves to Settled  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [GR-61] Any continuity mechanic never becomes another number to obsessively protect (never) · brief  
  Build: No streak or protected number; lifetime count and Growth only grow  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC

## Results: workouts, sleep & imports

- **Present** (was Missing) [RS-08] Sleep report can include a transparent, qualified summary or score · contract · how: sleep score (unconfirmed)  
  Build: Sleep report › Summary score toggle: 77/100, three equal-weight ingredients with formulas, stages/HR left out, 'not a health measure'.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-16
- **Present** (was Partial) [RS-29] Confirmed links are shown differently from possible duplicates · brief  
  Build: Log Running Yesterday, move to 17:40, Same one: no crash; Day view 'linked as one with the Watch workout, counted once'; 18:02 run 'linked with your entry'.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Missing) [RS-30] A new custom workout routine can be linked to an existing measured activity · brief  
  Build: Composer "Also count Watch workouts" (sessions/time): Jogging+Run counted a hand-logged Run (1 of 3); link not shown in Settings after.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** (was Missing) [RS-35] Sleep-adjusted screen-use estimate (e.g. YouTube playing after I fall asleep), combining Screen Time with sleep · brief  
  Build: Unchanged: Screen Time › A worked example with sample numbers beside real sleep; no real data.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Partial** (was Missing) [RS-36] Raw screen usage kept separate from the qualified awake-usage estimate · brief  
  Build: Unchanged: worked example separates Raw 2 h 14 / Awake estimated / Possibly asleep; sample data only.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** (was Partial) [RS-02] Results are meaningful, beautiful and more interesting than Apple Health, not a generic chart collection · contract  
  Build: Hero units now sit on the baseline (sleep "7 h 04 min asleep", run "6.2 km run"); reports keep their own designs.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, CONTRACT §R-16, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Partial** [RS-06] Sleep report shows longer-term trends · brief  
  Build: Sleep report still 30/90 nights; monthly sleep + yearly medians only on Time › Earlier years (2024/2025), not linked from report.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** (was Partial) [RS-15] A weekly activity view · brief  
  Build: Time › Weeks: per-day activity bars, kinds, distance, vs usual week, sleep, routines, 26-week bars; ‹ › to Week 1; Workouts › By week.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Partial** [RS-17] A workout is connected to sleep and other outcomes · brief  
  Build: Run report still links only to routines; no sleep link (Patterns 'Days you moved → sleep' exists separately).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Partial** [RS-19] Rare, short or occasional workouts still give an enjoyable result · contract  
  Build: Unchanged: timed sessions get 'Session saved' summary; 'Already done' logs toast only.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-16 / AS-02, CONTRACT §R-11 / AS-02
- **Present** (was Partial) [RS-26] Manual and imported records of the same workout are reconciled · contract  
  Build: Same one / Different both work: Linked as one counts once ('Counts once, as the Watch run at 18:02'); Unlink → 'Kept as two · both count'.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-11
- **Present** (was Partial) [RS-33] A new custom workout without GPS works properly · brief  
  Build: Log anything › Movement › Run 30 min → toast "Running settled for this week 2 of 2"; Routines shows Running settled.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [RS-34] Imported data arriving feels different from manual recording · brief  
  Build: Unchanged; arrival treatment only in 'Run arrives' scenario.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [RS-37] Freedom to explore my own data in depth · brief  
  Build: Explore: Two things (27 inputs × ~60 outcomes incl. words/own items), All/90/30/Choose dates calendars, Two periods, See the days.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **iPhone only** [RS-23] Workouts and other HealthKit measurements import automatically and take part in the experience · contract  
  Build: Simulated: You > Connections 'Apple Health · On', 124 workouts, 300 nights, 137 medication records  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, CONTRACT §R-11, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [RS-01] Seeing interesting results of an activity is part of the reward for doing it · contract · how: do > feedback > result > history > curiosity loop (unconfirmed)  
  Build: Today 'Last night · arrived from your Watch' > run report > Counts toward Movement/Running > Growth milestones  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §4, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** [RS-03] Feedback is as rewarding as Sleep Cycle / Watch / Strava, complementing rather than copying them · contract  
  Build: Run report adds 'Pace at the same effort' and 'Compared with recent runs', beyond a copy of Watch summaries  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, CONTRACT §R-16
- **Present** [RS-04] Checking last night's sleep in the morning is something to look forward to · brief · how: morning sleep report (unconfirmed)  
  Build: Today 'Slept 7 h 04' tile; Time > Sleep opens a full-bleed night report with hypnogram + HR  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** [RS-05] Sleep stages and awakenings are shown, with stages stated honestly as approximate · contract  
  Build: '2 times awake, 27 min'; stages as ~% with note 'minutes per stage can be off by 20 minutes or more'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §R-16, CONTRACT §E-08
- **Present** [RS-07] Compare a night with previous nights and see the previous day's relevant context · brief  
  Build: 'Compared with your last 30 nights' + 'The day before: Run 6.2 km · 18:02, Last caffeine 13:40'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [RS-09] No invented or medically-validated sleep score; no claimed medical validity (never) · contract  
  Build: No score or medical claims in Sleep report  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-16
- **Present** [RS-10] Shows connections between lifestyle and sleep (what Sleep Cycle lacks) · brief  
  Build: Sleep report 'The day before' + 'Patterns involving sleep' button opening Patterns filtered to sleep  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [RS-11] Rich sleep report: duration, timing, consistency, awakenings, stages and overnight heart rate, explorable · contract  
  Build: Sleep: 7 h 04, 23:41-07:12, wakes, hypnogram + HR, vs usual, night arrows, 30/90 history. Day one (1 Jan) shows 'usual NaN h'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §4
- **Present** [RS-12] Sleep feedback never makes me feel worse · contract  
  Build: Comparisons are neutral ('22 min less'); no judgement words or red states  
  Src: CONTRACT §E-07
- **Present** [RS-13] Workout report: duration, heart-rate zones, distance, pace, splits and intensity where available · contract · how: these report contents (unconfirmed)  
  Build: Run report: Splits, Pace and HR scrub chart, HR zones Z1-Z5, climb, kcal; Volleyball report: Intensity + zones  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC, CONTRACT §4
- **Present** [RS-14] Workout report shows personal comparisons and improvement over time · brief  
  Build: 'Compared with recent runs' (13 s/km faster), '2nd fastest of 23', 'Pace at the same effort since January'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [RS-16] Meaningful personal milestones for workouts · brief  
  Build: Run 'Personal bests' (fastest km, 5 km, longest run); Movement Growth milestones ('100 sessions')  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [RS-18] A rare or short workout never feels insignificant and gets no condescending praise (never) · brief  
  Build: Manual 10-min walk: toast '10 min · Movement, 2 of 3 this week', counted plainly  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [RS-20] Detailed, interactive workout reports with meaningful comparisons, visually expressive yet readable · brief  
  Build: Tap route stretch/split to highlight km, drag-to-scrub pace+HR, tap a recent run for its numbers  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [RS-21] Record a workout manually · brief  
  Build: Movement > Log time… > type (Walk/Run/…) + duration + when > Log; also Log anything > Workouts  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [RS-22] Inspect a workout imported from Apple Watch · brief  
  Build: Time > Workouts list (124, filter by type) > full report per workout  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [RS-24] One imported workout fulfils its routines, appears in history, gets a report, counts to progress and feeds analysis · brief  
  Build: Run report 'Counts toward Movement 1 of 3, Running 1 of 2 · counted once'; in Workouts list, Growth and movement pattern  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [RS-25] One real event never becomes duplicate records or double-counted totals (never) · contract  
  Build: Imported run counts once toward each routine; Connections: 'A workout counts once toward every routine it feeds'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §R-03 / AS-02
- **Present** [RS-27] Manual and imported records are not merged on time proximity alone (never) · brief  
  Build: No automatic workout merging exists; medication merge needs same amount within 45 min and can be undone  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [RS-28] Every record keeps and shows its source · contract  
  Build: Entries show 'from your Watch' / 'logged here' / 'Apple Health'; Day view lists source per entry  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §7
- **Present** [RS-31] Specialised views where the data supports them, e.g. a route map for GPS workouts · brief  
  Build: Run report has route shape with km markers; Volleyball report has no route  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [RS-32] Never fabricates a route, pace, split or statistic, or implies unavailable data can be obtained (never) · brief  
  Build: Session report omits route/pace; Screen Time page says Apple doesn't let apps read the numbers  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [RS-38] Results and comparisons for any routine, meaningful even for low-frequency ones · contract  
  Build: Every item page has Results bars + Growth; Date night by month, Sketching by 4-day window, Reading with no target  
  Src: CONTRACT §R-16
- **Present** [RS-39] Respects HealthKit availability, granularity, provenance and limits · brief  
  Build: Zones note 'wrist readings lag'; stages approximate; meds 'merged with Apple Health'; Screen Time honest  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [RS-40] Results, history, sleep and workout reports, measurements and observations form one integrated experience · contract  
  Build: Reports link to routines, Time, Patterns; Day view shows sleep, meds, caffeine and routines together  
  Src: CONTRACT §1

## History & statistics

- **Present** (was Missing) [HS-01] A transparent, interpretable, non-medical summary score where it helps, acknowledging uncertainty · brief · how: summary score (unconfirmed)  
  Build: Sleep Summary score: transparent ingredients/formulas, no score without recording, 'plain summary… not a health measure', placeholders labelled.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [HS-24] Periods are never judged by how much was recorded ('days with something recorded', visual density) (never) · brief  
  Build: Month Totals now per routine aim ("settled in 4 weeks", "at the aim on 20 days"); no entry counts or last-month comparison.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [HS-08] Explore weekly progress · brief  
  Build: Time › Weeks: Previous/Next week back to Week 1 (1–4 Jan); day chips open the Day view; every-week bars tap/drag.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Partial** [HS-14] History visuals are readable at phone size without learning an arbitrary visual language · brief  
  Build: Unchanged: year discs still need the 'a line: a day that has an entry' legend.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [HS-17] The routine overview is more than a list with streak-like visuals (never) · brief  
  Build: Unchanged: Routines tab is a grouped list.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs
- **Partial** [HS-18] Tactile, fluid movement through time and accumulated history · brief  
  Build: Drag-scrub on sleep/charts plus new Weeks bar tap/drag; otherwise taps.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [HS-22] Explore a time period I choose and compare the statistics or measurements I pick · brief  
  Build: Explore › Over: All history / 90 / 30 / Choose dates (From/To month calendars); Two periods › Choose; result updates.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** (was Partial) [HS-27] Progress across weeks, months and years; history spans years · contract  
  Build: Time › Earlier years: 2024 (from 14 Mar) and 2025 pages, workouts/sleep by month, Across the years. Watch-only synthetic data.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §AS-03
- **Partial** [HS-33] Beautiful progress views even for routines with very little data · brief  
  Build: Unchanged: new routine Results/Growth are text ('Nothing yet, and nothing is behind').  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [HS-35] Keeps the scores, goals, comparisons and statistics I enjoy · contract  
  Build: Goals/stats/bests kept, week vs usual week and year comparisons added; only optional sleep summary score.  
  Src: CONTRACT §R-21
- **Present** [HS-02] Scores are never presented as validated medical assessments (never) · brief  
  Build: No scores or medical claims exist  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [HS-03] Personal comparisons, health trends and measurable improvement are shown · brief  
  Build: Month Totals vs previous month, sleep vs last 30 nights, run vs previous 8, pace-at-effort trend  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [HS-04] Comparisons use comparable contexts · brief  
  Build: 'Runs of a similar length since May', weeknights only, sick/travel left out of patterns  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [HS-05] Starts with descriptive results and adds comparisons and associations as history grows, rewarding long before a year · brief  
  Build: 1 Jan: 'Day one… first entry becomes its first milestone'; 15 Mar: Patterns Building; 27 Oct: holds up  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [HS-06] Raw measurements and their uncertainty are always preserved · brief  
  Build: Day view lists every raw entry with time and source; past periods keep their target (Target history)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** [HS-07] Missing and messy data are handled without needing a perfect dataset or treating gaps as failure · brief  
  Build: Results legend 'unknown, not missed'; Away 1-21 Sep hatched; Day view 'Not recorded · unknown, not missed'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** [HS-09] No standard health-dashboard cards, tiny generic charts or text-only summaries (never) · brief  
  Build: Month discs, full-bleed reports, Growth curve; no Apple-Health-style card grid  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [HS-10] Measurements clearly labelled with explicit units, reference periods and consistent conventions · brief  
  Build: 'usual 7 h 27', 'previous 8', 'last 3 weeks', 'since January'; one chart style throughout  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [HS-11] Accumulated history stays meaningful across many weeks and changing routines, and gets more interesting with time · brief  
  Build: Growth 'only grows… gaps, pauses and sick weeks never take any of it away'; target history kept  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [HS-12] Exploring history, progress and results is itself enjoyable and invites curiosity · contract  
  Build: Time year of month discs > month highlights > day; reports tap/scrub; week story  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [HS-13] A monthly progress view · brief  
  Build: Time > month: disc, Highlights, Calendar, Totals vs previous month  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [HS-15] 'Not recorded' is always distinct from 'did not happen', and unknown periods show as unknown · brief  
  Build: Day view 'Not recorded · unknown, not missed'; Away span hatched on Sep disc; bars dashed 'unknown, not missed'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [HS-16] Beautiful, engaging history with zero extra input; no captions, keepsakes or journaling required · brief  
  Build: History builds from logs and Watch data; nothing asks for notes or captions  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC
- **Present** [HS-19] A rich, exploratory statistics experience for routine history, progress and long periods · brief  
  Build: Item pages: Results, Growth, bests, In Time; Time year/month/day; Workouts; Sleep  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [HS-20] Sophisticated interactive visualisations, beautiful and legible, as rich as Strava or Sleep Cycle · brief  
  Build: Scrubbable pace/HR, tappable splits and route, hypnogram, growth markers; hero unit-label glitch noted  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [HS-21] Examine sleep history directly · brief  
  Build: Sleep > History 30/90 nights, tap or drag to open any night  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [HS-23] Rich reports, interactive history and discoveries are never sacrificed for a game (never) · brief  
  Build: No game layer; reports, Time and Patterns all intact  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** [HS-25] A mundane low-activity week or a travel week is presented fairly, not as bad · contract  
  Build: Week story: 'Nothing headline-worthy, which is most weeks.'; travel shaded on discs, travel days left out  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, CONTRACT §AS-08
- **Present** [HS-26] History for each individual routine · brief  
  Build: Routines > item: Results bars, Growth, Recent entries, In Time > 'Only Movement' Time filter  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [HS-28] A year of accumulated history is presented gracefully · brief  
  Build: Time: 12 month discs, 'The year so far' 2,995 entries, 124 workouts, 300 nights  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [HS-29] Partial periods are represented fairly · brief  
  Build: Mar disc '9 of 15 days' at 15 Mar; new item: 'first week is still running'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [HS-30] Monthly, weekly and infrequent routines stay meaningful in history · contract  
  Build: Date night Results 'by month', Sketching 'by 4-day window'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §AS-03
- **Present** [HS-31] Personal records, accumulated accomplishments and milestones are kept · brief  
  Build: Growth milestones and bests ('Longest: 1 h 44', 'Most in a week'); run Personal bests  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [HS-32] Clear split between headline results and deeper analysis · brief  
  Build: Reports and Time show results; Patterns separate under Look closer  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [HS-34] One visual language serves rich reports and quick routine interactions · brief  
  Build: Same hue tokens, fonts and chart style across Today, item pages and reports  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [HS-36] A missed target is shown without reading as failure · contract  
  Build: Results legend 'at target / partly / unknown, not missed'; no red or 'failed'  
  Src: CONTRACT §R-21
- **Present** [HS-37] A routine added mid-year fits history immediately; earlier past isn't drawn as misses · contract  
  Build: Growth 'since 1 Feb'; composer: 'the days before don't count against it'  
  Src: CONTRACT §AS-05
- **Present** [HS-38] History is kept for paused and retired routines · contract  
  Build: Routines: Paused 'nothing expected', Retired 'Show 3… Their history and growth are kept'  
  Src: CONTRACT §AS-07

## Patterns & analysis

- **Present** (was Missing) [PA-05] Explore consistent wake time vs how I function · brief  
  Build: Patterns "Waking near your usual time" vs 5 outcomes incl. energy/feel; "Checked: no clear difference so far".  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [PA-06] Explore medication timing and dose differences vs my day and functioning · brief  
  Build: Inputs "Morning medication later than usual" and "…at a different amount" vs same-day and next-day outcomes; honest Too early labels.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Missing) [PA-07] Explore outdoor time / daylight and sleep regularity vs sleep timing and quality · brief  
  Build: "More daylight" and "Waking near your usual time" vs sleep length / falling asleep; Explore: 82 vs 84 days, no clear difference.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [PA-08] Explore meal patterns vs fatigue and well-being · brief  
  Build: Regular meals checked: 106 vs 77 days "no clear difference" for sleep; energy/feel "Not knowable at current pace" (few check-ins).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [PA-09] Explore supplements vs anything measurable · brief  
  Build: Vitamin D (note-every-time on): 138 vs 45 days, "No clear difference so far" across sleep outcomes; energy not knowable yet.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** (was Partial) [PA-22] Finds relationships across any routines and measures without developers hand-coding each pairing · brief  
  Build: Generic catalog of 26 inputs; Watch/noted inputs checked; others stuck until "I note it every time" is switched on (one tap, works).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** (was Partial) [PA-26] My custom routines and new records (symptoms, substances) become analysable once they have enough data · contract  
  Build: Custom observations (Headache, Melatonin) and routines join catalog; switch makes them analysable; pace labels shown.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-17 / AS-16, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Missing) [PA-27] I can optionally explore a question of my own, alongside automatic discovery · brief · how: ad-hoc question exploration (unconfirmed)  
  Build: Patterns "Explore my own question": pick input and outcome → result ("82 days 57 min or more and 84 less: no clear difference").  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Partial** [PA-01] Helps me understand how my actual lifestyle, including counterproductive habits, affects my well-being and functioning · contract  
  Build: Functioning pairs (WHO-5, focus check) appear when module on but all read 'Nothing to compare yet' (0 results); energy pairs not knowable.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, CONTRACT §1
- **Present** (was Partial) [PA-13] No meaningful personal findings claimed after only a few days or from sparse data (never) · contract  
  Build: Cards no longer state findings while Building (15 Mar: counts only); detail still shows medians with "needs about 32 of each" caveat.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §AS-11, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Partial** [PA-17] Analyses respect time order, confounding and missing or selectively logged data · contract  
  Build: Raw days + 'Not used' accounting, unknown≠zero, both sick views; confounders only named.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-17, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [PA-18] Accounts for selection, e.g. taking something because a bad night was expected · brief  
  Build: Unchanged: no selection handling (e.g. taken because a bad night was expected).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Partial** [PA-19] Handles repeated, time-dependent observations, small samples, routine changes and same-event signals · brief  
  Build: Unchanged: thresholds/resampling range only; no handling of routine changes or dependence.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [PA-23] Any measure (sleep, energy, mood, activity, symptoms, new ones) can be the outcome · brief  
  Build: Explore outcomes: sleep, feel, every routine next day, observations, check-in words, own self-report items (e.g. 'Back pain the next day').  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [PA-24] Analytics are not built around sleep as the main outcome (never) · contract  
  Build: Patterns All / With sleep / Without sleep; 3 of 7 pairs non-sleep, sleep also as input; copy 'Sleep is one outcome among several'.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, CONTRACT §R-17
- **Present** (was Partial) [PA-30] Data is labelled by evidence type: direct behaviour, physiology, self-report, proxy, speculative · contract · how: evidence-class taxonomy (unconfirmed)  
  Build: Pattern detail › Evidence: e.g. 'Direct behaviour, measured by your Watch', 'Physiology, a Watch estimate', 'Observation, from your own log'; also in Explore.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-13, CONTRACT §7, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Partial** [PA-34] Show results under different context assumptions and flag possibly confounded periods · brief · how: sensitivity views / confound flags (unconfirmed)  
  Build: Detail › By context (workday vs day off/holiday) and sick Left out/Included views; no flagging of possibly confounded periods.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Partial** [PA-36] Analyses consider relevant time windows and lags · brief  
  Build: Explore offers same-day vs next-day outcomes; no user-set windows or lags.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [PA-39] I can look at the underlying data and its limits behind any relationship · brief  
  Build: Detail › The days behind it: day rows with group + value, Show all N, 'Not used' breakdown, tapping a row opens that Day view.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Partial** [PA-41] Patterns are visually exceptional and clear about uncertainty · brief  
  Build: Detail adds distribution strip + ladder, but Patterns list is still text cards.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Partial** [PA-46] Context-aware analysis connecting routines, exposures, medication, sleep, exercise and functioning · brief  
  Build: By context, meds and exposures in catalog; WHO-5/focus pairs exist only when opted in and never reach a result (0 data).  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po
- **Present** [PA-02] Analysis adds long-term depth but never dominates or replaces routines, results and motivation · contract  
  Build: Patterns is under Time > Look closer plus one occasional Today card ('A pattern holds up so far'); Today stays routine-first  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-17
- **Present** [PA-03] Explore exercise vs that night's sleep · contract  
  Build: Pattern 'Days you moved > that night's sleep': Holds up so far, +20 min median, likely range 10-27 min, 201 nights  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §4
- **Present** [PA-04] Explore later caffeine vs worse sleep · brief  
  Build: Pattern 'Caffeine after 14:00 > when you fall asleep': Building, needs ~10 more weeks; only days with caffeine logged used  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [PA-10] Relate a night's sleep to how I function the next day · brief  
  Build: Pattern 'Sleep the night before > your energy that day' (Building, 24 check-ins)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [PA-11] Findings are labelled by how strong the evidence is: tentative, holds up, insufficient, unknowable · contract · how: evidence ladder  
  Build: State chips: Not enough yet / Building · needs ~N weeks / Holds up so far / No clear difference / Not knowable at current pace  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g, CONTRACT §0 / R-17, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [PA-12] Honest result states: 'not enough data', 'no clear difference', 'we don't know' are valid answers · contract  
  Build: Patterns at 1 Jan: all 'Not enough yet'; alc-hr 'Not knowable at the current pace'. Blemish: day-one cards show a lone '.' sentence  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §AS-14, CONTRACT §R-21
- **Present** [PA-14] Never claims causes or confuses correlation with causation (never) · contract  
  Build: Patterns footer 'Nothing here is a cause'; each detail has a 'Not a cause.' paragraph naming the likely confounder  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-17, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [PA-15] Never fabricates or manufactures correlations or insights to keep things interesting (never) · contract  
  Build: Pairs computed from the data; weak ones shown as Building / Not knowable rather than hidden or inflated  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §0, CONTRACT §R-17
- **Present** [PA-16] No medication or substance advice or experiments, and no association presented as treatment efficacy (never) · contract  
  Build: alc-hr detail: 'An observation, not advice… nothing here asks you to change anything to find out'. No suggestions anywhere  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU7zpLEoZF5zbxqJbcMkh7Po, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, CONTRACT §R-22, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [PA-20] No brute-force testing of every variable pair; defensible candidate selection guards against spurious findings (never) · contract  
  Build: Patterns lists 5 pairs 'chosen in advance'; no all-pairs search exists (trivially respected)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §R-17 / AS-16
- **Present** [PA-21] How much data is enough depends on the measurement, not one universal threshold · brief  
  Build: Per-pair needs differ (25/32/15/14/12) and cards say 'needs about N more weeks' or 'not knowable at current pace'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [PA-25] The same measure can be an outcome in one analysis and an explanatory factor in another · contract  
  Build: Patterns segment All / Sleep after / Sleep before; detail has 'Sleep as the input instead' link to the swapped pair  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-17, CONTRACT §R-17 / AS-15
- **Present** [PA-28] No research questions or hypotheses I must create or maintain; discoveries come without admin (never) · contract  
  Build: Patterns needs no setup: cards appear and update on their own; no question or hypothesis screens anywhere  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, CONTRACT §R-17, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [PA-29] Never requires me to predict my behaviour or mood to get discoveries (never) · brief  
  Build: No forecasting or prediction prompts anywhere in the app  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouULPZp7C9VYmJKtVYCqY6bVC
- **Present** [PA-31] Proxies never treated as direct measures; no claims about mental state, effort or sleep quality from indirect signals (never) · contract  
  Build: Sleep stages shown as rough shares with accuracy note; Screen Time page says it can't be read; no ADHD/effort/quality claims  
  Src: CONTRACT §R-13, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [PA-32] Unrecorded days count as unknown, never as zero, and are left out of analysis · contract  
  Build: Patterns footer 'days you didn't record count as unknown, never as zero'; caffeine pair uses only logged days, alcohol only confirmed weeks  
  Src: CONTRACT §R-09, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [PA-33] Raw data is kept and context decides which comparisons are fair · contract  
  Build: Pattern 'Left out' section: sick and travel days excluded, away days kept because the Watch recorded  
  Src: CONTRACT §R-15, CONTRACT §7
- **Present** [PA-35] Never auto-removes observations, invents corrections, blames an event, or claims all confounders are controlled (never) · brief  
  Build: Context is only used to set days aside; detail always names remaining confounders ('Busier, better days might bring both')  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [PA-37] Compares me with myself (within-person) · brief  
  Build: All pairs compare my own days/nights, e.g. 92 nights after moving vs 109 without  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [PA-38] Patterns shows a few understandable discoveries first, never an intimidating dashboard or stream of correlation cards (never) · brief  
  Build: Patterns is one short list of 5 plain-language cards; tap opens detail with dots, medians, range and How sure  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** [PA-40] No AI mixed into measurement or statistics: no hallucinated data, no unsupported composite health scores (never) · brief  
  Build: All pattern text is computed from data (bootstrap, medians); no AI text and no composite health score anywhere  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [PA-42] Patterns stay interesting without a definitive finding and need no conversational prompts · brief  
  Build: 'Not knowable' cards explain why and how long; all navigation by tapping cards  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [PA-43] Works with sparse data and grows more informative over months and years · brief  
  Build: Time travel 1 Jan > 15 Mar > 27 Oct: cards move from Not enough yet to Building to Holds up so far  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** [PA-44] Clear boundaries between known facts, inferences, suggestions and outcomes; candid about what it can't know · brief  
  Build: Pattern detail separates 'Your nights and days' (data), 'How sure', 'Not a cause', 'Left out'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [PA-45] Trustworthy, qualified personal insights about routines, sleep, exercise, physiology and well-being · brief  
  Build: Today card 'A pattern holds up so far… An association, not a cause' > See the evidence > pattern detail  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [PA-47] An exercise session is both a rewarded behaviour and a source of measurements · brief  
  Build: Run counts toward Movement/Running and has a full report; workouts also feed the movement>sleep pattern  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** [PA-48] Detailed analytics have a credible, discoverable entry point · brief  
  Build: Time > Look closer > Patterns ('5 pairs · 1 holds up so far'), Today pattern card, Sleep report 'Patterns involving sleep'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [PA-49] Doesn't force numbers or statistics onto activities where they aren't meaningful (never) · brief  
  Build: Done-or-not routines (Call parents) show 'done' / 'at target', no invented stats  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUNq5T9cb1FpgwqWm9cu1C4g
- **Present** [PA-50] A poor night is an observation, not proof I want rest; an empty calendar isn't free time (never) · brief  
  Build: No suggestions are derived from sleep or free time anywhere  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [PA-51] No false precision (never) · brief  
  Build: Ranges ('10 to 27 min'), '~20%' stage shares, '≈' caffeine; but day-one Sleep report shows 'usual NaN h'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv

## Intentions, reminders & proactive help

- **Present** (was Missing) [IN-11] From a reminder I can snooze, dismiss, skip, suppress or correct it directly · brief  
  Build: You → Reminders 'When one arrives' preview: Done logs for real, In 1 hour (comes back 09:40 once), Not today, Not this week, Correct it… opens log sheet  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Missing) [IN-14] Reminders can taper off, and I can review whether they're actually helping · brief · how: reminder reduction over time; effectiveness review (unconfirmed)  
  Build: Reminder sheet 'Fade out when it's going well' toggle; You → Reminders 'Are they helping?' Yes/Not really ('quieter now: it fades out'); taper not simulated  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** (was Missing) [IN-15] Reminders can optionally adapt to my explicit preferences and reliable patterns · brief · how: adaptive reminders (unconfirmed)  
  Build: Skipped: adapts to explicit choices (Not now 3 h then rest of day, Not really fades); no adaptation from reliable patterns  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Missing) [IN-16] Event-based or if-then cues, e.g. when a scheduled activity finishes · contract · how: optional if-then / event cues (unconfirmed)  
  Build: Reminder sheet 'After…': When your workday ends, After your last calendar event (needs Calendar)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, CONTRACT §7 / E-01
- **Present** (was Missing) [IN-17] Optional location-based cues · brief · how: Core Location (unconfirmed)  
  Build: Reminder sheet 'After…' → 'When you get home': off until allowed, toast 'iOS would ask once; only arriving home is used'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Missing) [IN-18] Optional help moving from work mode into home life / household tasks, only with a trustworthy trigger · brief · how: after-work transition cue (unconfirmed)  
  Build: Reminder 'After…' → 'When your workday ends' (about 17:30 from Your usual week, works from home too)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Partial** (was Missing) [IN-28] Help me form a realistic intention · brief  
  Build: Unchanged: intention sheet date grid/repeats, 'Make a start · 15 minutes'; nothing helps size it or make it realistic  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Missing) [IN-29] Optionally, Meridian suggests two or three worthwhile things for today or a relevant moment, each explained · brief · how: morning selection of 2–3 possibilities (not a daily ritual) (unconfirmed)  
  Build: Today 'A good moment for': max 3 suggestions, each with a reason line, Done it/Start, Not now, ⋯; master switch in You → Suggestions  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** (was Partial) [IN-30] Meridian can suggest worthwhile things I haven't set up as routines (meditation, flowers for my girlfriend) · brief  
  Build: Suggestions › Include ideas: 38 generic ideas + 'Your own'; Today keeps one idea place ('A walk in daylight · from the ideas you opted into')  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** (was Missing) [IN-33] Optional opportunities that fit the time I actually have (e.g. a walk when circumstances suit) · brief  
  Build: 'I have about 15 min/30 min/1 h' chips filter; with Calendar, 'This evening, 17:30–19:15 is free' windows (Short night)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Missing) [IN-34] I can say I have about 30 free minutes and get a fitting proposal · brief · how: 'I have 30 minutes' input (unconfirmed)  
  Build: Tap '30 min' on Today: list narrows to Stretching (10 min) and Push-ups (20 min); '1 h' keeps Time with friends  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [IN-35] A suggestion I wave off at a bad moment can return later when it's more useful · brief  
  Build: Not now: 'rests about three hours'; Clock +3 h brings Stretching back 'back from earlier: you said not now at 08:40'. Bug: 2nd Not now returns again  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Missing) [IN-44] Suggestions draw on my routines, targets, windows, deadlines, history and preferences, even with little history · brief  
  Build: Uses open routines/targets ('1 of 3, 6 days left'), Usually takes, Fits best, calendar windows, deadlines ('by Thu 29 Oct'); works on day one  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Missing) [IN-45] Per-routine control over suggestions · brief · how: suggestion preference settings (unconfirmed)  
  Build: You → Suggestions 'Per routine' switches (Suggest Water…); ⋯ 'Don't suggest this again' sets it per routine  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Missing) [IN-46] Suggestion ideas come from an opt-in library, my interests or a constrained AI · brief · how: opt-in library, interests, constrained AI (unconfirmed)  
  Build: You → Suggestions 'Include ideas' opt-in, interest tags People/Calm/Outdoors/Home/Creative; no AI source  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Missing) [IN-49] After bad sleep, offer a less demanding option without assuming I can't do things · brief  
  Build: Short night: 'A shorter night than usual, so lighter versions first'; 'Movement, a short one · Start 15 min'; rest still one tap away  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Partial** (was Missing) [IN-50] Help with executive-function friction: avoidance, procrastination, overwhelm · brief  
  Build: Unchanged: First step field and 'Start 15 min' help initiation; nothing for overwhelm/avoidance beyond that  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Partial) [IN-51] Help with high-resistance admin tasks such as writing an invoice · brief  
  Build: 'Pay the flat service charge · Started · 15 more min' starts a timed session ('a first 15 min, N min left'); End → Done / Started, more / Discard  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Missing) [IN-52] Help stopping hyperfocus and switching activities · brief  
  Build: Live session bar has Pause; after usual length bar reads 'past your usual 30 min. A good place to stop?' (verified with clock fast-forward)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Missing) [IN-53] Help with time awareness and estimating how long things take · brief  
  Build: Suggestions state 'usually about 40 min'; live session past-usual cue; time chips match tasks to available time  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Partial) [IN-54] Make the next action concrete or appealing to reduce friction · brief  
  Build: Item › Time and circumstances 'First step' field on any routine; shows on Now ('First step: Open the book on the nightstand') and suggestions  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Present** (was Partial) [IN-55] Help is richer than 'go for a walk because you haven't walked enough' · brief  
  Build: Help now: reason-first lines, calendar gaps, lighter version after short night, first steps, timed 15-min starts, usual-length cue  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [IN-01] Reminders are a core part of Meridian and richer than one fixed-time alert per item · brief  
  Build: Reminder sheet: Off / Quick / A time (±15 min, days) / A window / After… cues, device, fade-out; You → Reminders limits, quiet hours  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Partial** [IN-07] Both repeating and one-off reminders · brief  
  Build: Skipped: repeating reminders rich; one-off only intention 'Bring it back' (no clock time) or 'In 1 hour'; no one-off clock reminder  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [IN-08] I can choose the exact time a reminder comes (optional time cues) · contract · how: time cues (unconfirmed)  
  Build: Reminder sheet 'A time': At 19:00 with 15-min −/+ steppers and Mon–Sun day chips for weekly items  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, CONTRACT §H-05
- **Present** (was Partial) [IN-09] Flexible reminder windows rather than a single clock time · brief  
  Build: Reminder sheet 'A window': Morning 07–10 / Afternoon 12–17 / Evening 18–21; with Calendar picks a free moment  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [IN-10] A reminder doesn't fire once the activity is already done · brief  
  Build: Preview: after Done, 'Date night is already settled · So this one wouldn't be sent'; sheet copy 'If it's already done, nothing arrives'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [IN-12] Reminders have a full, discoverable lifecycle: set up, become eligible, arrive, get answered, follow up correctly · brief  
  Build: Setup in sheet, preview arrival, answer actions with real effect, 'In 1 hour · comes back at 09:40, once' follow-up (preview only)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** (was Partial) [IN-13] I can set reminder preferences, including which device/channel they arrive on · brief  
  Build: Per-reminder 'Arrives on iPhone/Watch/Both' plus You → Reminders default 'Arrive on' and 'At most N a day'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [IN-19] Reminders and contextual suggestions are clearly different in interaction and not overlapping admin systems · brief  
  Build: Reminders are notifications (You → Reminders preview); suggestions are Today cards with Not now/⋯; separate settings pages  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [IN-20] Meridian tells apart hard commitments, my chosen intentions and optional opportunities, each timed its own way · brief  
  Build: Calendar commitments read-only (day line grey), intentions Bring back/By a date/Repeats, optional suggestions and ideas, each timed differently  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** (was Partial) [IN-22] Real deadlines (rubbish out Thursday for Friday collection) are remembered, incl. recurring ones I configure · brief  
  Build: Intention › By a date › Pick a date grid + Weekly ('Due Tue 27 Oct, then every Tuesday'); 'Put the bins out · By Thu 29 Oct · every Thursday' on Today  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** (was Partial) [IN-25] Meridian distinguishes choosing, starting and completing an intention · brief  
  Build: Intention sheet has Started / Done / Let go; list shows 'Started · By Sat 31 Oct · every month'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Partial) [IN-27] Help me actually start and follow through after deciding, without it becoming a chore · brief  
  Build: Start 15 min / 15 more min run a timed session; End → 'Time on it': Done with it / Started, more another time ('1 min so far') / Discard  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Present** (was Partial) [IN-36] From any suggestion I can act, defer, dismiss or jump elsewhere; suggestions are always optional · brief  
  Build: Each suggestion: Start/Done it/Make a start, Not now, ⋯ (remind later, not this week, don't suggest, already done, Open item)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** (was Partial) [IN-37] Dismissing distinguishes not now, remind later, not interested, don't suggest again, already done · brief · how: dismissal options (not now / later / not interested / never / done) (unconfirmed)  
  Build: ⋯ sheet: Remind me later / Not interested this week / Don't suggest this again / Already done; plus Not now  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** (was Partial) [IN-39] Every suggestion explains why it's being shown · brief  
  Build: Every card leads with a reason: 'not yet today, last done yesterday', '1 of 3 this week, 6 days left', 'from the ideas you opted into'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** (was Partial) [IN-41] Meridian visibly chooses not to intervene in some situations · brief  
  Build: Sick: 'You're sick today: nothing is suggested until you're better'; Back after 5 weeks: 'Your first days back: nothing is suggested'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [IN-42] Help works for any routine, incl. one I create tomorrow, with no custom rule · brief  
  Build: Engine generic over Usually takes/Fits/cadence; new First run routines (Movement) appear in suggestions the same day  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Partial) [IN-47] Support arrives at a genuinely useful moment (day-of-week, calendar and context aware) · brief · how: EventKit (unconfirmed)  
  Build: Calendar free windows, workday span, context holds, Fits best (evening/weekends), short-night lighter versions  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Partial** [IN-56] Different kinds of support per activity: initiation, consistency, anticipation, reflection, progress, none · brief  
  Build: Unchanged: initiation, consistency, session cue, after-summary exist; no per-activity choice of support kind (or none)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs
- **Present** (was Partial) [IN-57] Proactive help needs little setup and stays useful with no context data · brief  
  Build: Suggestions work with no calendar/context (As built, First run day one); master switch off leaves Today fully working  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Partial) [IN-60] Morning cards and fixed-time reminders aren't assumed to be the answer (never) · brief · how: morning card (unconfirmed)  
  Build: Reminders offer windows and After… (work end stepper) besides clock times; suggestions in-app; reminders off by default  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **iPhone only** [IN-67] Opening a reminder is never taken as proof I did it (never) · brief  
  Build: Preview logs only on explicit 'Done'; whether opening a real notification counts needs the iOS app  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [IN-02] Reminders are optional, off by default, available for any routine (incl. relationship ones) and under my control · contract · how: per-routine reminder settings, off by default  
  Build: You → Reminders: 'Off unless you turn one on'; every routine listed; Date night/Parents set; composer step 4 'No reminder' default  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-07, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [IN-03] Reminders for routine upkeep never feel like tasks or obligations · contract  
  Build: Reminder sheet copy: 'Optional, quiet… One notification, never repeated, never urgent.' No overdue/streak language  
  Src: CONTRACT §R-07, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [IN-04] No artificial urgency in reminders or prompts (never) · contract  
  Build: By a date 'nothing is ever overdue'; passed dates 'resting, not overdue', offered once; no red badges  
  Src: CONTRACT §R-07, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [IN-05] No nagging, guilt, dependence or habituation from repeated prompts (never) · brief  
  Build: Reminders single, Not today quiets till tomorrow; but a suggestion waved 'Not now' twice comes back twice in one day (minor)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [IN-06] Reminders work for weekly, monthly, every-N and flexible routines, with lead time for monthly ones · brief  
  Build: Date night (monthly) reminder sheet: '7 days left and fewer than the target', 'First Saturday', 'Mid-month'; every-N: 'Halfway through each window'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** (was Partial) [IN-21] These kinds are never collapsed into one priority score or task list (never) · brief  
  Build: Deadlines removed from 'A good moment for' (routines only); dates in own 'By a date' lane, ideas in a reserved place; Suggestions page 'Dates: never here'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Missing) [IN-23] A real deadline never disappears because I slept badly or rest is recommended (never) · brief  
  Build: 'By a date' lane stays under Sick/Away/Holiday/Travel ('still here while you rest'), Short night, Suggestions off, own new deadlines too  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [IN-24] Something I explicitly chose to do comes back so I don't forget it, without repeated reminders · brief  
  Build: Routines → Hold something → 'Bring it back'; Intentions scenario: Today card 'Back, as you asked' with Done / Later / Let go, once  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [IN-26] Accepting or holding an intention is never counted as having done it (never) · brief  
  Build: Start 15 min / Mark as started add nothing to counts ('Kept as started'); only Done moves a repeating intention on  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [IN-31] Thoughtful gestures (like buying flowers) never become compulsory recurring tasks (never) · brief  
  Build: Ideas: 'Sounds good' records nothing; partner idea 'Only if it fits your life; switch it off'; routine only if chosen  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [IN-32] Flexible recurring personal intentions, e.g. two dates a month, with a nudge while there's still time · brief  
  Build: Date night: 'at least 2 a month', Today '1 of 2 dates · 5 days left', reminder 'When a month has 7 days left and fewer than 2'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [IN-38] A dismissal or repeated decline is never read as 'unwanted' or 'no longer valued' (never) · brief  
  Build: Not now rests ~3 h and may return; nothing learns from declines; only explicit 'Not really' / 'Don't suggest' change behaviour  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [IN-40] When nothing useful applies, no recommendation is manufactured; few, meaningful prompts only (never) · brief  
  Build: 'Nothing to suggest right now. That's fine.' on day one; quiet when sick/away/back; max three. After Sounds good a 2nd idea fills in  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [IN-43] No feature built per example or symptom just for coverage (never) · brief  
  Build: 'Flowers for Ana' gone; library of 38 generic ideas ('Something small for your partner · Only if it fits your life'); grep finds no Mark-specific idea  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [IN-48] No time-consuming suggestions while I'm busy with a known commitment (volleyball Wednesday evening) (never) · brief  
  Build: Short night + Clock 19:30: suggestions point to next gap 20:15–22:30, nothing during the event; Calendar events never taken as free  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [IN-58] Help never becomes admin: no mandatory check-ins, planning, motivation ratings, skip confirmations or questionnaires (never) · brief  
  Build: No mandatory check-ins or ratings; Questionnaire opt-in, never prompted, skippable; no skip confirmations  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [IN-59] Proactive support complements and never replaces direct controls or dominates the app · brief  
  Build: You → Contextual moments switch; turning it off leaves Today's routines and logging intact  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** (was Missing) [IN-61] Meridian never presumes readiness, free time, private facts, partner's wishes or meaning from a routine's name (never) · brief  
  Build: Gaps worded as gaps: 'Now, nothing in your calendar until 09:00', 'a gap in your calendar 17:30–19:15'; no 'free' left in UI copy  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [IN-62] No log is never read as the activity not happening (never) · brief  
  Build: Unrecorded days stay 'unknown, not missed'; Not today 'Nothing is recorded, nothing is missed'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [IN-63] Never claim a technique treats ADHD (never) · brief  
  Build: No ADHD or treatment claims; WHO-5/focus check 'nothing is a diagnosis'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [IN-64] Never claim intelligence or learning from my responses that isn't really there (never) · brief  
  Build: No learning claims; 'Only you can say; Meridian doesn't guess'; ideas rotate by day, not claimed as learned  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [IN-65] Never keep recommending the same few generic activities (never) · brief  
  Build: Ideas rotate daily (27 Oct walk, 30 Jun swim, 1 Jan street history); 38-idea library + own ideas; each switchable  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [IN-66] Hydration reminders never push excessive water (never) · brief · how: hydration reminders (unconfirmed)  
  Build: No water pushes; Water Growth 'amounts beyond it aren't added'; reminders skip when already done  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [IN-68] Optional reduction intentions with an 'at most' target (e.g. alcohol) · contract · how: at-most target  
  Build: Alcohol: 'At most 4 a week', set in item Settings → Intention; no target needed for Caffeine  
  Src: CONTRACT §R-10 / P-1
- **Present** [IN-69] A reduction target shows as met only with enough explicit evidence · contract  
  Build: Alcohol weeks: 'confirmed within / above / unknown'; a week counts only after 'That's everything'  
  Src: CONTRACT §P-1
- **Present** [IN-70] There's a low-friction way to confirm a reduction week · contract  
  Build: Alcohol page: one 'That's everything' button on last week  
  Src: CONTRACT §P-1 / AS-09
- **Present** [IN-71] A few logs followed by silence show as unknown, not success · contract  
  Build: Alcohol: '19–25 Oct · unknown until you say that's everything'; 'two drinks and then silence isn't a result'  
  Src: CONTRACT §P-1 / AS-09
- **Present** [IN-72] No daily abstinence confirmations or new obligations (never) · contract  
  Build: No daily confirmations; suggestions, reminders, questionnaire all optional  
  Src: CONTRACT §P-1

## Widgets, Watch & notifications

- **Present** (was Missing) [WN-06] Live Activities and App Intents (Siri/Shortcuts) · brief  
  Build: You → Watch, widgets: Live Activity card appears while a session runs (End); Siri and Shortcuts list with working 'Try' (preview)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** (was Missing) [WN-09] Home Screen and Watch keep an intention in view without interrupting · brief  
  Build: Intentions scenario: Home Screen 'Held for later' widget, Watch 'held for today' row, Lock Screen notification with Done/Later/Let go  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** (was Missing) [WN-11] Quiet hours, and defined behaviour for a reminder that falls in them · brief  
  Build: You → Reminders → Quiet hours: Off / 22:00–07:30 / 21:00–08:00 / 23:00–09:00; copy defines wait-until-end, dropped if settled (presets only)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [WN-01] A real wrist-native Apple Watch app: glanceable, quick actions, haptics, in sync · contract  
  Build: Watch preview is interactive: tap row to log, crown amount, Start/End session, on-watch Undo, private item hidden (real app native)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-25, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** (was Partial) [WN-02] Useful, beautiful glanceable Home and Lock Screen widgets · contract  
  Build: Home Screen widget '+330' logs (580→910 ml) with Undo; Next up widget logs; Lock Screen preview  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-25, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** (was Partial) [WN-03] Quick recording from Watch and widgets · brief  
  Build: Widget '+330' and Watch rows log real entries; Watch Guitar 'Start' runs a session  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** (was Partial) [WN-04] iPhone, Watch and widgets share one coherent language without identical screens · brief  
  Build: Watch/widgets reuse item colours and states but device-specific forms (crown amount, Live Activity, compact widget)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** (was Partial) [WN-07] Sessions can run on the Watch · brief  
  Build: Watch preview Guitar → Start runs a timer '0:02 · also on your iPhone' with End; Live Activity mirrors it  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** (was Partial) [WN-08] Reminders and feedback arrive on the right device: Watch, widgets, notifications or in-app · brief  
  Build: Per-reminder 'Arrives on iPhone/Watch/Both' and default 'Arrive on' in You → Reminders  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Partial) [WN-13] Notification limits / interruption budget to avoid fatigue · brief  
  Build: You → Reminders 'At most 1/2/3 a day / No limit' with rule for what waits; quiet hours  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **iPhone only** [WN-10] Meaningful native haptics · brief  
  Build: Simulated: Dynamic Island strip labels 'success haptic' / 'soft tick' / 'light tap'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **iPhone only** [WN-12] Commitments never silently bypass quiet hours; any exception is my explicit choice (never) · brief  
  Build: Quiet hours and 'Focus modes on your iPhone still apply' described; intentions have no notifications; bypass only judgeable on iOS  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **iPhone only** [WN-16] Delivered notifications are updated or withdrawn when records change · brief  
  Build: Not simulated  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **iPhone only** [WN-17] Reminders handle time-zone changes · brief  
  Build: Not simulated (travel context exists, no time-zone behaviour)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **iPhone only** [WN-18] Reminders fire correctly when the app isn't running, within iOS background limits · brief  
  Build: Not simulated  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **iPhone only** [WN-19] Respect Focus modes, authorisation and delivery limits · brief  
  Build: Not simulated  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [WN-05] An iPhone app · contract  
  Build: The prototype is the iPhone app (Today, Time, Routines, You)  
  Src: CONTRACT §R-25
- **Present** [WN-14] No repeated or duplicate notifications (never) · brief  
  Build: 'Each is a single quiet notification'; In 1 hour returns once; Not today quiets until tomorrow; daily limit  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [WN-15] The experience never depends on constant notifications; Meridian isn't a notification engine (never) · brief  
  Build: All reminders off by default; app fully usable with none; suggestions and dates live in-app  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw

## Integrations & permissions

- **Present** (was Missing) [IP-03] Calendar commitments and free windows can inform Meridian, only with my permission · brief · how: calendar integration (EventKit) (unconfirmed)  
  Build: You → Connections → Calendar 'Read my calendar' off by default, read only, choose Personal/Work; feeds free windows (but gaps are treated as free)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** (was Missing) [IP-05] System Reminders can be used where authorised · brief  
  Build: Connections › Reminders 'Read dated reminders' (preview, sample data): items appear in By a date '· from Reminders', also while Sick; off removes  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Partial** (was Missing) [IP-06] Screen Time / device activity as an optional signal where feasible, with proxies treated cautiously · brief · how: Screen Time / DeviceActivity (unconfirmed)  
  Build: Skipped: You › Screen Time 'Feasibility pending · not connected'; sample worked example only, nothing connects  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** (was Missing) [IP-07] Screen Time analysis stays 'feasibility pending', not excluded · contract · how: DeviceActivityData.activityData(filteredBy:using:) (unconfirmed)  
  Build: You → Screen Time: 'Feasibility pending', 5 of 8 checks documented, 3 open; You row 'Feasibility pending · not connected'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §R-14 / P-2
- **Present** (was Missing) [IP-08] Screen Time is never declared impossible on outdated assumptions (never) · contract  
  Build: Screen Time: 'nothing here is claimed or ruled out yet'; no 'impossible' claim  
  Src: CONTRACT §R-14
- **Partial** (was Missing) [IP-12] Screen Time keeps raw usage and handles multiple devices, background playback and granularity · contract  
  Build: Skipped: worked example 'Raw, as reported' hourly sample; multiple devices/background playback still an open check  
  Src: CONTRACT §R-14
- **Partial** (was Missing) [IP-13] Screen Time separates use overlapping sleep from awake use, possibly combined with HealthKit sleep · contract  
  Build: Skipped: worked example splits sample hours vs sleep (Awake / Possibly asleep); static sample only  
  Src: CONTRACT §R-14, CONTRACT §P-2
- **Present** (was Partial) [IP-17] No invented API capabilities, unverified integrations or fictional automatic measurements (never) · brief  
  Build: Screen Time documented vs Open checks; Reminders/Shared marked preview with sample data; sleep score 'placeholder formulas'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Partial** [IP-22] Passive, objective indicators of everyday functioning beyond Screen Time · brief  
  Build: Skipped: reads workouts, sleep, daylight, overnight HR, calendar; focus check is an active test, no new passive indicator  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD
- **Present** (was Partial) [IP-23] Designed permission flows and a settings/permissions screen · brief  
  Build: Onboarding Health step (off → 'Apple Health stays off'); Connections: Health 'Not connected' → tap connects; per-type read switches; Calendar/Reminders opt-in  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **iPhone only** [IP-01] Activities and data come in automatically from Apple Health where possible, manual entry where needed · contract · how: HealthKit  
  Build: Simulated: You → Connections 'Apple Health · On · reads workouts, sleep, daylight'; Today run 'arrived from your Watch'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, CONTRACT §R-25, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **iPhone only** [IP-02] Apple Watch data is used where I allow it · brief  
  Build: Simulated: Connections 'Apple Watch · On'; sleep and workouts labelled 'Watch'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **iPhone only** [IP-15] Screen Time used only as far as a personally installed app in Slovenia/EU can really access it · brief  
  Build: Eligibility can only be checked on device; prototype assumes no access  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **iPhone only** [IP-16] Medication access via HealthKit is only claimed once verified (never) · brief  
  Build: Medication still 'merged with Apple Health'; needs on-device verification  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **iPhone only** [IP-19] The whole experience is realistically buildable on native Apple platforms · brief  
  Build: Judged in the iOS build; prototype stays within plausible HealthKit/WidgetKit surfaces  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **iPhone only** [IP-24] Minimal permission requests and battery impact · brief  
  Build: Only judgeable on device  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [IP-04] A calendar event with someone's name is never silently treated as a confirmed date (never) · brief  
  Build: 'Dinner with Ana', 'Call with Maja' only block time ('a gap is not assumed to be free time'); never turned into entries  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [IP-09] Screen Time features are never faked if the data isn't available (never) · brief  
  Build: Screen Time worked example labelled 'sample numbers, not yours'; no Screen Time numbers in Time or Patterns  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [IP-10] If Screen Time can't work, everything else works and Meridian says so plainly · contract  
  Build: You → Screen Time explains plainly; rest of app unaffected  
  Src: CONTRACT §AS-18, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [IP-11] Don't assume everything in Settings → Screen Time is available to apps (never) · brief  
  Build: Screen Time lists documented vs open checks; no assumption all Settings data is available  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [IP-14] Night-time playback is never read as distraction (never) · contract  
  Build: 'Something playing at night, like a podcast, is never read as distraction'; 'Possibly while asleep' kept separate  
  Src: CONTRACT §R-14
- **Present** [IP-18] Never assume continuous monitoring, mental-availability detection or access to other apps (never) · brief  
  Build: Location only 'arriving home'; no monitoring or other-app access claimed; Reminders read only when allowed  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [IP-20] Records from several sources are deduplicated and connected reliably · brief  
  Build: Medication: 'Apple Health and logged here, merged' + 'Duplicate removed'; Connections: a workout counts once  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [IP-21] Each record shows where it came from and how reliable it is · brief  
  Build: Entries show 'Apple Health' / 'Logged in Meridian' / 'Watch'; Watch entries: 'original stays in Apple Health'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [IP-25] Prefer passive and already-available data over asking me · brief  
  Build: Workouts and sleep arrive on their own ('Workouts from your Watch arrive on their own')  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb

## Privacy & optional modules

- **Present** (was Missing) [PM-05] Location triggers are optional and privacy-respecting · brief  
  Build: Location only via reminder 'When you get home': 'Off until you allow it'; 'only arriving home is used, never a history'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Partial** [PM-11] Privacy boundaries for sensitive records and context data · brief  
  Build: Skipped: 'Private outside the app' per item, Connections lists each read type; search 'privacy' gives scattered rows, no overview  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** (was Partial) [PM-12] Works offline with my data stored locally and owned by me · brief  
  Build: Your data: Export as JSON + 'Delete everything in Meridian…' sheet (disabled until 'I understand' ticked) empties app; offline note in Connections  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **iPhone only** [PM-08] Local-first, on-device intelligence; smart timing without a server or LLM where possible · brief  
  Build: Architecture question for the native app; prototype runs entirely locally  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [PM-01] Meridian stays worthwhile with all reminders and proactive support turned off · brief  
  Build: You → Contextual moments off: Today keeps Now/Later/logging; reminders off by default  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb
- **Present** [PM-02] The core app is complete with every optional module off; none defines its identity · contract  
  Build: Turned off How you feel, Medication, Observations: Today, Time, Routines show no trace and nothing looks missing  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, CONTRACT §AS-17, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Present** [PM-03] Medication, exposures and Screen Time are each fully optional · contract  
  Build: You → Modules: each has its own switch ('each one optional'); Screen Time not used  
  Src: CONTRACT §AS-17, CONTRACT §P-3
- **Present** [PM-04] Context handling is optional · brief  
  Build: Today 'Context · none set' by default; nothing requires it  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [PM-06] Neutral, optional records for alcohol, caffeine and similar exposures · brief  
  Build: Observations: 'Alcohol and caffeine, noticed without judgement'; 'never a reward or a judgement'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [PM-07] Never ask for a full Apple Health export; request only what a question needs (never) · brief  
  Build: Onboarding asks only 'Read sleep and workouts'; Connections reads named types with switches; no export request  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1
- **Present** [PM-09] Optional depth (analysis, wellbeing, medication) designed in from the start · brief  
  Build: Medication, How you feel, Observations and Patterns are fully designed and integrated  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [PM-10] Optional modules are reachable without cluttering or dominating; lightweight, not conversational · brief  
  Build: Under You → Records; modules disappear fully when off; no chat UI  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA

## Accessibility

- **Present** (was Partial) [AX-01] Accessibility designed in throughout, alongside motivational features · contract  
  Build: --ink-3 now ≈4.8:1, follows system text (140% probe scales layout), aria labels; minor: at 140% run card title runs under its X  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §R-24, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** (was Partial) [AX-04] Dynamic Type support · brief  
  Build: You › Follow the system text size (on by default); default font 22px → data-sys-ts 1.4, headline 40→46px; plus Larger text 135%  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [AX-05] Good contrast · brief  
  Build: --ink-3 light rgba(19,20,23,.61) (~4.8:1), dark .55; Time and You scan show no text under 4.5:1  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [AX-07] Every interaction is discoverable and accessible, no hidden gesture-only actions · brief  
  Build: Hold-to-adjust now has screen-reader buttons 'Adjust: log X…', 'Undo last X entry', 'Open X' per item; same actions via + logger and item page  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [AX-02] Psychological safety throughout · brief  
  Build: Neutral copy: 'Missing a date is just information', 'nothing owed', 'Nothing piled up'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [AX-03] Honour Reduced Motion with calm alternatives · contract  
  Build: With system reduced motion, transitions drop to ~0 s; story autoplay and stagger animations are skipped  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §R-24
- **Present** [AX-06] Adequate touch targets · brief  
  Build: Audit of visible controls on Today and You found none under 44 pt (SVG route segments excluded per Step 1 notes)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [AX-08] Readable text and clear navigation are never sacrificed for novelty (never) · brief  
  Build: Text reflows at 135%; navbar back label and title can crowd (Step 1 notes)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w

## Look & feel

- **Missing** [LF-03] No generic rounded cards, progress grids, checklists, orbs, mascots, glass gradients or AI-dashboard look (never) · brief  
  Build: Skipped: Today still white rounded cards; new Weeks page is a white card with bar chart, label/value rows and day pills  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** (was Missing) [LF-04] Not a plain, boring checklist tracker or one-row-per-routine layout (never) · own  
  Build: Unchanged: default Now one row per routine; By a date/Later rows; opt-in day line the only non-list view  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUCiM4wdRpCTShMCHDKdfwG1, CONTRACT §1
- **Partial** [LF-01] An original, distinctive, memorable visual identity that never looks generic or AI-generated · brief  
  Build: Time spokes, run report, day line distinctive; Weeks, Year, Your data, Connections are standard cards and rows  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Partial** [LF-02] Originality is structural (recording, progress, history, motion), not loudness, and restraint never means blandness · contract  
  Build: Unchanged: day line structural (opt-in); recording/progress still list rows; Weeks is a plain bar chart  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, CONTRACT §R-24
- **Partial** [LF-05] The design is impressive and extraordinary without being complicated or gimmicky · own  
  Build: Unchanged: striking run card/report, Time, Watch; everyday screens and new Weeks/Year pages ordinary  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouU9oMMd3Mpe3QGJKw72RSdoB
- **Partial** [LF-07] Keeps the first full-app prototype as the favourite reference · own  
  Build: Cannot confirm comparison with the first full-app prototype; same base look  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUCiM4wdRpCTShMCHDKdfwG1
- **Partial** [LF-08] Not Boring-level craft in visuals and interactions while still fitting all functionality · own · how: Not Boring as reference  
  Build: Unchanged: crown drag, Live Activity, day line add craft; most interactions standard taps, sheets, toasts  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUFJqyjjvzyuFPZND4VetQ41, cmsg_01Ju1d1RXQsRdZdTG83zTouU4Py9ZCD16jgyu3fPAP2M5C, cmsg_01Ju1d1RXQsRdZdTG83zTouUEgHfejF9w11vXJHJrCgx4t
- **Partial** [LF-13] Not a quiet generic analytics dashboard, minimalist tracker or generic iOS wellness aesthetic (never) · contract  
  Build: You, Connections, Your data, Reminders, Suggestions still grouped inset lists with switches; Weeks is an analytics card  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx, CONTRACT §R-24
- **Partial** [LF-14] Exceptional typography, spacing, composition and pacing · brief  
  Build: Consistent type/spacing; contrast improved; Today and Time › Look closer keep stacking sections in card+row composition  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Partial** [LF-15] Strong hierarchy: sections don't all look alike and colour reflects importance · brief  
  Build: Unchanged: run card and Now stand out; By a date, Later, A good moment for, Settled share one look  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [LF-16] Avoid overused pill buttons and repeated rows divided by thin lines · brief  
  Build: Unchanged pills ('Start 15 min', Done it/Not now, time chips) plus Weeks day pills; thin-line rows everywhere  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [LF-17] Minimal explanatory copy and few uppercase micro-labels or secondary text · brief  
  Build: Search subtitles now real ('Asks you to confirm first'); still much explanatory copy: Weeks footnote, delete sheet, Reminders paras  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [LF-19] No oversized numeric headlines repeated across unrelated views · brief  
  Build: Big numerals still repeat: '27 October', '6.2 km', '19–25 Oct' Weeks header, Water hero, Growth totals  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [LF-20] Motion, transitions and micro-interactions are crafted, fluid and meaningful, without forced multi-step sequences · brief  
  Build: Unchanged: push transitions, spring sheets, ripple, crown drag; session end still two sheets  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Partial** [LF-25] Consistent but not identical: no forcing everything into one template, metaphor or gesture · brief  
  Build: Most screens still white card + row template, incl. new Weeks, Year, Your data, Connections states  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Partial** [LF-27] Reduce total interface complexity while raising quality · brief  
  Build: Not reduced: Today unchanged in size; Look closer grows to Patterns, Workouts, Sleep, Weeks, Earlier years, story  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [LF-29] Works at real iPhone size with no layout or safe-area problems · brief  
  Build: Time → Patterns cards now fit at 390 with gutters; no horizontal overflow found on Today/Time/Patterns/Routines/You pages, also at 135%  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs
- **Partial** [LF-34] Earlier designs aren't approved or reused by default; the visual direction stays open (never) · contract  
  Build: Still built on the 18 Oct prototype look (warm off-white, Funnel type)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §R-23
- **Partial** [OT-03] Routines feel satisfying, progress meaningful, results fascinating; elegant, a joy to open for years · brief  
  Build: Growth, story, run report, Patterns, Weeks, Year exist; much of the app still lists and rows  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouU4Py9ZCD16jgyu3fPAP2M5C
- **Present** (was Partial) [OT-24] The most-used parts are exceptionally polished, intuitive, efficient and behave as expected · brief  
  Build: Run card now 'Second half 11 s/km faster' (back scenario: '5 s/km slower'); logging + toasts behave as expected  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Partial** [TD-03] Today is genuinely beautiful, distinctive and engaging; opening it may reveal something interesting · brief  
  Build: Unchanged: moment carousel + rows/chips; conventional look.  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **iPhone only** [LF-21] Tactile, satisfying feedback including haptics and direct manipulation · brief  
  Build: Haptics only simulated by Dynamic Island labels; direct manipulation limited to taps (hold opens logger)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [LF-06] Not ugly and legible at a glance · own  
  Build: Text high-contrast and readable at 390 pt; clear status lines ('580 ml of 2 L · 1.42 L to go') in light and dark  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHdmCkSo4MudQacb6FJ2GWk
- **Present** [LF-09] Doesn't take visual 'depth' from reference apps (never) · own · how: depth effect  
  Build: Surfaces are flat with light shadows only; no 3D/depth stacking  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUJXN3g6ZgmBPYdFNKR9K8pM
- **Present** [LF-10] Mature, sophisticated and expressive without being loud or childish · contract  
  Build: Muted off-white/deep green palette, one type family, no mascots or loud colour; report uses deep ground for expression  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, CONTRACT §R-24
- **Present** [LF-11] No loud sports typography, saturated game cards, bright panels or mandatory animated ceremonies (never) · contract  
  Build: Settle is a brief ripple; weekly story is opt-in and 'skippable'; no saturated game panels  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, CONTRACT §R-24
- **Present** [LF-12] Clean without being empty; rich and still beautiful when showing dense data · brief  
  Build: Run report packs route, splits, zones, comparisons legibly; Today is full but ordered  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [LF-18] No generic praise, flattery or narrative padding (never) · brief  
  Build: Toasts and cards state facts ('Water settled for today', '80 sessions since 6 Apr'); no praise copy seen  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC
- **Present** [LF-22] No arbitrary decoration, excess animation or metaphors that hide function; complexity must be justified (never) · brief  
  Build: No decorative illustrations or dioramas; Time spokes encode real data with a legend  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUFJqyjjvzyuFPZND4VetQ41
- **Present** [LF-23] One coherent identity across everyday use, reports, history, meds, suggestions, a full year and a fresh start · brief  
  Build: Same type, tokens and per-item hue across Today, run report, Time, Medication, 1 Jan and 27 Oct states  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [LF-24] Visual range: calm everyday screens, more expressive reports, history and big moments, still coherent · brief  
  Build: Calm off-white Today vs deep-green run report, dark weekly story and six-month card  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** [LF-26] A product-wide design system: type, spacing, colour semantics (incl. neutral), shared components and animation tokens · brief · how: animation tokens (unconfirmed)  
  Build: Tokens in :root (one family, spacing scale, --spring/--out); neutral ink-4 for excess/unknown; Log and New routine share sheet behaviour  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [LF-28] Light and dark appearance both look right at real iPhone sizes · brief  
  Build: Dark colour scheme renders Today/Time/Water correctly; You → Appearance System/Light/Dark  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [LF-30] Feels like a premium native iOS app: distinctive yet familiar, usable and accessible · contract  
  Build: Standard nav bar with back label, sheets with grabber, tab bar with central +; large-text and 44 pt targets added  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, CONTRACT §R-24
- **Present** [LF-31] Effortless and pleasant in repeated everyday use · brief  
  Build: One-tap presets and chips with undo; Log sheet with recents; no confirm dialogs for logging  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [LF-32] Never regress visually while improving functionality (never) · brief  
  Build: Step 1 additions reuse existing tokens/components; only crowding at 135% text noted in STEP1-NOTES  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA
- **Present** [LF-33] Products I like inform mechanisms only; Meridian never copies an app's appearance (incl. Not Boring) (never) · contract  
  Build: No recognisable copied app appearance; weekly story uses a generic stories pattern  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouU4Py9ZCD16jgyu3fPAP2M5C, CONTRACT §1
- **Present** [LF-35] Keep good lessons: localized feedback, composed interactions and visual restraint · brief · how: localized feedback; Counterpart restraint (unconfirmed)  
  Build: Feedback is local: ripple at the tapped preset, the row itself turns 'Water settled'; restrained palette  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [LF-36] Not limited to sparse text and pill response buttons; no chatbot-style structure (never) · brief  
  Build: No chat or response-button structure; screens carry charts, maps and lists  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [LF-37] Beautiful in both everyday screens and detailed reports; rich enough for sophisticated stats · brief  
  Build: Run report shows route map, pace/HR chart, zones, comparisons in the same visual language as Today  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u

## Navigation & findability

- **Partial** [NV-03] Clear what is what and understandable without a guided tour, with consistent intuitive labels · own  
  Build: Look closer rows now have subtitles; 'By a date', 'Later', 'Settled', 'A good moment for' still explained only by small footnotes  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUJXN3g6ZgmBPYdFNKR9K8pM, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [NV-04] The hierarchy is priorities, not a conventional dashboard of tabs; rethink conventional bottom navigation (never) · contract  
  Build: Still 4-tab bottom bar (Today/Time/Routines/You) + centre Log  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** (was Partial) [NV-07] Every feature is findable without asking for it, and progressive disclosure hides nothing important · brief  
  Build: Search everything: 'suggest', 'ideas', 'deadline', 'reminders', 'screen', 'shared', 'sleep score', 'work hours' all return places/settings  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [NV-01] A fast everyday experience separate from deeper optional exploration · contract · how: two modes: everyday vs exploration (unconfirmed)  
  Build: Today for doing; Time → Look closer (Patterns, Workouts, Sleep, story) for exploring  
  Src: CONTRACT §R-19 / §4, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [NV-02] Useful controls are never buried under artistic metaphors (never) · brief  
  Build: Logging is plain buttons/presets; Time's day-disc has a plain calendar and totals beside it  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [NV-05] Not a chatbot: no conversation, scripted replies, NL parsing or LLM needed to log, manage, see stats or navigate (never) · brief  
  Build: No assistant or chat anywhere; all actions and stats are direct taps  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUUWsXyJku7h72ieFbUTZgzA, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [NV-06] I can always start any action directly, even when no suggestion is shown · brief  
  Build: Centre 'Log anything' button and Today search are always present; Routines → New routine  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [NV-08] Navigate directly from an action or feedback to its history, statistics or reports · brief  
  Build: Today row → detail Results/Growth; 'Open in Time ›'; run card → full report  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [NV-09] Progressive reveal of additional detail · brief  
  Build: 'More…' presets, 'Show 3' retired, 'See the evidence', 'Earlier…' entries  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Present** [NV-10] Direct, efficient control is kept, including with all proactive support switched off · brief  
  Build: Contextual moments switch off: Today keeps Now/Later/Settled and all logging  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx
- **Present** [NV-11] Proactive features never silently add navigation or features to the main product (never) · brief  
  Build: Contextual moments are cards on Today only, behind one switch in You; no extra tabs  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw

## Everything else

- **Present** (was Missing) [OT-20] A designed onboarding · brief  
  Build: First run: Welcome → starter picks → Apple Health → optional modules → Ready; each skippable ('Skip all, go to Today'); Today 'Nothing is behind'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Partial** [OT-06] Helps start activities, remember routines and stay consistent once novelty fades · brief  
  Build: Unchanged: suggestions, reminders with fade-out, dates lane, first steps; nothing specific for the novelty-fading phase  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Partial** [OT-08] Not a task manager, planner, notes app, productivity suite or coach, or calendar replacement (never) · contract  
  Build: Unchanged: Today dated-task lane with timers, Done/Started, repeats, Reminders import; done intentions now logged too  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUUUDrvPu7QXbVF93dz5jPrYY, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, CONTRACT §1
- **Partial** [OT-16] One coherent, exceptional product, not disconnected dashboards, modules, utilities or bespoke features · brief  
  Build: New pages (Weeks, Year, Your data delete, Connections states) reuse list style; bespoke pieces keep adding  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUFJqyjjvzyuFPZND4VetQ41
- **Present** (was Partial) [OT-19] Designed empty, loading, error and offline states · brief  
  Build: Empty ('Nothing to suggest…', Day one), loading ('Reading…'), error ('Couldn’t connect… Try again') and offline ('No connection right now…') in Connections  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **Partial** [OT-22] Each capability defines what happens when a module is off, a routine changes, or I return after absence · brief  
  Build: Sick/away reminders paused then resume, dates hold, suggestions hold; reminders after an unmarked absence still undefined  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Partial** [OT-25] Craftsmanship and full functional depth together, never a beautiful shell with missing features · own  
  Build: More works (delete-all, system text, weeks/years, connection states); GR progression/mastery skipped, Shared/Screen Time previews  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU9oMMd3Mpe3QGJKw72RSdoB, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUYLhM87xXmrsLvcDW5hcLRx, cmsg_01Ju1d1RXQsRdZdTG83zTouU4Py9ZCD16jgyu3fPAP2M5C
- **Partial** [OT-26] Nothing Mark asked for silently disappears; the chosen design fits all functionality (never) · own  
  Build: Studio openly holds GR-02/15/28/34, LF-03 (not silent), but they remain missing  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUVMtNkXPNEfRGDvv76GVzYz, cmsg_01Ju1d1RXQsRdZdTG83zTouU8vmDGBUBEtGS1oUXQECrSC, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Partial** [OT-27] Remove screens, information and features whose burden outweighs their benefit · brief  
  Build: Nothing pruned; Time adds Weeks and Earlier years pages, Your data adds delete flow, Prototype toggles grow  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG
- **iPhone only** [OT-01] Meridian is a gamified well-being and routine app for iPhone, Apple Watch and widgets · contract  
  Build: Web prototype; You → Watch, widgets and Lock Screen simulates Lock Screen, Home widgets and Watch  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, CONTRACT §1
- **iPhone only** [OT-02] The design can plausibly be built natively in SwiftUI · brief  
  Build: Only judgeable in the real app; prototype uses standard sheets, lists and segments  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [OT-04] Everyday use has extremely low friction and stays effortless · brief  
  Build: Presets and Later chips log in one tap with Undo toast; 5-log burst in 6 taps (Step 1 notes)  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
- **Present** [OT-05] Not a Concerta or ADHD app; works with any medication, supplements or none (never) · brief  
  Build: Medication is one optional module in You; nothing ADHD-specific on Today  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w
- **Present** [OT-07] Using Meridian never becomes a demanding project, an obligation, self-rating or system-optimising (never) · brief  
  Build: No required check-ins ('never prompted'); setup is the short composer; no scores to maintain  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUMvfWqbrKBH9acB2xpfmRkb, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [OT-09] Not a walking, sleep, exercise, meditation app or walking game; not reduced to one routine (never) · brief  
  Build: Today and Routines carry 15–28 mixed routines; sleep is a single 'Slept' chip  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouUPhxuRHmLAxxHF5hTd3LDj1, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [OT-10] Not a medication, ADHD-symptom or substance-use tracker or ADHD dashboard (never) · contract  
  Build: Medication and observations are optional modules, 'a record, no rewards'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouUKZtqasSazWP4MR7asQ4kSG, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv, cmsg_01Ju1d1RXQsRdZdTG83zTouUHYGmh739hifE8VcKArnP6u
- **Present** [OT-11] Not a diagnosis tool, clinical or health dashboard, research or mental-health treatment app (never) · contract  
  Build: Patterns say 'An association, not a cause'; no clinical scores or diagnoses  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw, cmsg_01Ju1d1RXQsRdZdTG83zTouUPMvQ3wJLPS5W4Sh7GpV3nv
- **Present** [OT-12] Not a giant collection of charts or statistics, though detailed stats are welcome (never) · brief  
  Build: Charts live in routine detail and Time → Look closer; Today carries none beyond a week strip  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUGhMtrq6ezVuBGh85v2zx4w, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g
- **Present** [OT-13] No single measurement (sleep, mood, meds, Screen Time, alcohol) becomes the organising principle or main UI (never) · contract  
  Build: Sleep is one chip; 30 Jun six-months card is about running; Patterns is one entry in Time  
  Src: CONTRACT §1, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, CONTRACT §AS-20
- **Present** [OT-14] The product isn't redefined around the latest mechanism (a game, timeline, conversation or planning) (never) · brief  
  Build: Structure stays routines-first; Time, Patterns and Intentions are secondary areas  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1, cmsg_01Ju1d1RXQsRdZdTG83zTouUKGH8uH9EeLyR4egqMZc2PC, cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2, cmsg_01Ju1d1RXQsRdZdTG83zTouUFmXyEbqwBBWKYArCM6EcVw
- **Present** [OT-15] Priority order: routines, then enjoyable gamification, then results/history, then discovering relationships · contract  
  Build: Today leads with routines; growth/results in detail; Patterns deeper in Time  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb, cmsg_01Ju1d1RXQsRdZdTG83zTouU45sAqaxXQxsr587o58Gn1g, cmsg_01Ju1d1RXQsRdZdTG83zTouURFva6M2p8cypxwZWPLo6rD, CONTRACT §1
- **Present** [OT-17] Keep the generic routine model, flexible frequencies, preserved history, neutral observations, honest analytics · brief  
  Build: All five visible: composer, target history, 'noticed, not rewarded', 'association, not a cause'  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouU3TvrpjZpdRhwgagwQ9dvKs
- **Present** [OT-18] No empty 'Coming soon' placeholder screens (never) · brief  
  Build: No 'Coming soon' anywhere in UI or source  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUT8mmMTKjmY9x4Nz2SnM7Rb
- **Present** [OT-21] Designed settings · brief  
  Build: You: modules, Contextual moments, Reminders, Connections, Watch/widgets, per-item Private  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUHfQFKZZhPykSwMger5rED2
- **Present** [OT-23] Designs handle missing, uncertain data and both high- and low-activity periods · brief  
  Build: 'unknown, not missed' throughout; Time shows quiet Sep away span and busy months alike  
  Src: cmsg_01Ju1d1RXQsRdZdTG83zTouUDTPqXLddmP8Gmpihf8sSx1
