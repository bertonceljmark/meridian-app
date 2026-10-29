# 02 · What was tried, what Mark approved, what he rejected, and why

11 days (18–29 Oct 2026), about 70 design rounds in a cloud project with several Claude threads (a builder "Studio", a separate checker "Review", plus motion, glass and taste threads). This is the distilled record. Verbatim quotes are Mark's. Dates are 2026.

The single most important lesson, in his words (18 Oct): **"The fundamental problem we've repeatedly encountered is that the latest interesting idea becomes the whole application."** Walking research produced a walking app, analytics research an analytics journal, game research collectible cards, continuity research a streak interface.

The second: **features passing tests ≠ an experience he likes.** Review signed off "the final UI" with 625 ledger items present on 23 Oct; six hours later Mark called it "plain ugly and boring" and "ai generated slop".

---

## 1. Before this project (the native workspace you may already have)

Another Claude system built native SwiftUI infrastructure: iPhone + watchOS + widgets, HealthKit, local storage, migrations, sync, a medication-agnostic data model, routine models, a "gamification engine", an analytics engine, 500+ tests. Mark rejected every product design from it:

| Design | Why rejected |
|---|---|
| Day Miniature (diorama on top of habit cards) | Toy-like + generic, weak hierarchy, unsatisfying interactions |
| Ruled ledger, timeline sheet, printing-press type | Same structure (one row per routine, slots to fill) under different skins |
| Long Road, Night Sky, Darkroom, Roots, Town, Record Book, Loom, Seasons, Score, Rotation | Metaphors for *displaying* progress, not satisfying experiences |
| Chapters and Combos | Fiddly, cluttered, finite content, not enjoyable |
| Walking-only reduction | "Completely misunderstood the product" |
| Process | "Repeatedly froze design decisions, declared its concepts successful, and implemented them before I had seen convincing interactive visual work." |

The infrastructure "can be reused later". Its design, IA and gamification engine cannot (see 05-KEEP-OR-DROP).

## 2. 18 Oct: product definition

- **P01 (Today / Atlas / Questions):** rejected. "Restrained personal analytics journal with logging controls." Especially the **Questions** mechanic: "Why am I being asked to manage a list of questions?"
- **A Loadout, B Broadcast:** "aggressive, in-your-face … excessively game-like or sports-broadcast-like". **C Rhythm:** calmer but assumes fixed times of day.
- **Contract v1.0 → v1.1 → v1.1.1, approved 13:07** (`reference/CONTRACT.md`). Requirements integrity: layer A owner requirements, B research, C hypotheses, D prototype decisions. Never promote C/D to A; never narrow A because of B.
- **P02 Tempo + Forecast + Almanac:** rejected. Tempo "may just be a forgiving streak mechanic"; Forecast "dangerously close to the rejected Questions"; Almanac "risks becoming another journal".
- **E1 Counterpart / E2 Turn / E3 Surface (interaction experiments):** first "genuinely different" work. Counterpart = his visual benchmark for restraint and composition, but **not** conversational ("I don't want Meridian to become a chatbot wrapped around a routine database"). Turn = good choreography, but "a satisfying interaction should not become a ceremony". Surface = good physicality, but "Do we need to invent a gesture for every new category?"
- **Whole-product prototype (`meridian/whole/`):** "gets substantially more things right". On 20 Oct: **"My favourite version is still the first ever full app prototype we built."** Not approved as design; strongest structural reference.
- **Engagement experiments Pursuits / Developing / Invitations:** none compelling. Key insight he wrote: **"We've repeatedly confused feedback with motivation."** He split motivation into A before action, B initiation, C reward after, D sustained over time, E intrinsic delight.
- **Range / Craft / Company / Record:** Range only helps routines with natural variation; Craft "turns maintaining a healthy lifestyle into another optimization project"; Company optional future; **Record (excellent records and results) is the baseline he won't sacrifice**. "Play happens off-screen" was an over-narrow assumption: meaningful in-app engagement around real actions is allowed.
- **Composition / Portrait slices:** presentation features, not motivation systems.
- **Parallel research (not approved, findings usable):** analytics workstream (`reference/analytics/`, generic data model, rule-based candidate discovery, honest evidence states, life-event context); executive-function workstream (`reference/ef-support/`: user-named event moments beat clock reminders, Hold / Start / Cross, inferred "receptivity" rejected); §14 prompt kinds (`reference/S14-intentions-and-reminders.md`).

## 3. 19–20 Oct: process resets

- Integrated → refined → Studio "quiet instrument" builds: functionally better, visually "noticeably AI-generated: conventional layouts … too many pills and separators".
- Phase 1 diagnosis accepted provisionally. Phase 2A: five whole-product directions, **all rejected**; they "converged visually and structurally" because each started from an assigned metaphor.
- Mark hands over ownership (19 Oct 15:26): "take much greater ownership … Use the smallest experiments that answer important questions … Keep communication concise." And: **"I dont think that the agent that builds the app should analyze it."**
- **Taste check (20 Oct):** depth, light and material won; flat lost (0/10). Home tests: "I dont like b at all. A looks 'fine' but I feel it will be unable with many items"; depth test: "Current version is just confusing, I have no clue what is what"; "This is just plain and boring checklist tracker." Decision: evolve the 18 Oct whole-product prototype.
- Mark's worry, recurring: "I am worried I pick the design then we dont manage to fit all functionality in it. Or you forgeting about funcionality." → Review built the **feature ledger** (every requirement from his messages, ~620 items) and **research ledger** (494 items). Both are in `ledgers/` as JSON.

## 4. 21–23 Oct: "Bold 7" (3D objects on a deep stage)

- Style variations: "None of these, they all look like ai generated." Asked to try neumorphism, glassmorphism and others; "I dont like neo brutalism."
- **Picked style 7** (Opal + NB Weather inspired: one rendered three.js object per screen on a deep stage): "Okay, I am happy with 7. Love the 3d elements. Some items still look ai sloppish, also me layout issues." Asked for an autonomous process that misses nothing.
- Rule from him: 3D must come from real data ("There is 3d map of walk on top. Can we do this dynamically based on route? If not we have to do it differently").
- **"Cut" gamification: rejected** ("Indont like this lets skip").
- 22 Oct: "Why pebbles? … does the color shape and sizes mean anything" (they didn't); low-poly cave "looks really cheap"; "We shouldnt try to make it more realistic … it will get dated fast … more of an abstract look"; "the cards you added just look ai slop"; liked the earlier horizontal cards for observations / weekly recap; "This is just different representations of the same idea, not different ideas based on findings."
- 23 Oct 09:05 final UI signed off by Review. Mark: "I think we have a baseline, but a lot of thought and polish is still required. I am sure we can simplify certain flows a lot." His seven flow questions (stretching timed?, trash every Thursday, meals, plan-the-week, pebbles, over-specific sketching step, baseline categories) were researched in `reference/review/21-flow-findings.md`. Note his framing: **"Dont take any of these as new rules. It must be researched and figured out."**
- 23 Oct 15:45: **"the app looks plain ugly and boring … I think it never looked right, just didnt hit me until now."** He refused copying a loved app's look, a mood-image route ("we already did this") and a human designer ("not this"). Richer pass: "This looks bad still", "Still looks like ai generated slop".

## 5. 23–24 Oct: the look he approved (current baseline)

| Step | His words | Result |
|---|---|---|
| New flat Today | "No, it uses styling for times first iphone came out. Also think layout wont allow all the funcitonality?" | rejected |
| Flat Today v2 + 3D arc | "Better yes. I wonder if we can spice it up with 3d elements? Like the arc" / "I know we can make it better. So it actually looks impressive." | iterate |
| Lit 3D arc, angled | "This looks cheap, and the angle is really bad" | rejected |
| Straight-on arc drawn with light (`prototypes/today-arc/`) | **"Yes, perfect"** (24 Oct 09:29) | approved, then superseded by his own next ask |
| Neumorphic Today | "Could we try neuromorphism variation of today page? But every single element down to the button really polished" | started |
| Neu round 1–2 | "I love this, but I am sure we can emphasise it more so everything looks like it was pulled out from one surface" / "make it more colourful … downgrade again to ai sloppy color scheme, and downgraded structure again so its not easy too see what is what because worse visual weights" | colour per routine back |
| Three tops for the dial | **"I think 1 is my favourite, but I would probably make the dial screenwidth and do something clever with details. I feel the depth is much better now."** | screen-width dial |
| Surface colour | "I am also not a fan of this poop bg colour" → "Second one, blue" | **Ink #1D2633** |
| One surface | "it looks like that the phone is a clay surface onto which elements shape into … when scrolling it must look like that the surface is shifting to adjust and not that there is more space than visible" | clay-rise scroll work |
| Layers | "figure out how we make actual layers pop, like it was truly 3d" | depth via light / height |

**Result: neu v7** (`prototypes/today-neu-v7/`, screenshot `screenshots/approved-today-neu-v7.png`): neumorphic Today on Ink, one colour per routine shown as a lit dot, layered depth, raised dock nav, screen-width dial hero.

### The scroll (clay rise), approved 24 Oct 21:16
Sequence: sketches "not really what I am looking for which makes me feel like you dont understand"; "Lets think this from material perspective"; picked pin-screen "but it does not follow physics correctly"; ChatGPT's membrane model "Yeah this wont work". Then **his own idea** (18:27): "for a very short section where item scrolls in or out its flat, than it goes in or out? But not whole item at once it slwly inclines declines". Refinements: "Now its not flat offscreen"; "It should be like printed text and symbols … then they get pulled up or down when scrolling, so no border at first"; "I dont want it to tilt"; per-point slope confirmed ("Yes"); "get rid of" the screen-fixed glow line; "a gentle pop when element all the way out". **"Yes perfect."** Model and tuning in `reference/clay-rise-NOTE.md`, sketch in `prototypes/tilt-clay-rise/`. Next morning: **"Moat is not working for this app"** → moat removed app-wide. Walls and depth stayed.

### Motion
Morph lab (`prototypes/morph/`, spec `reference/MORPH-47-interactions.md`): one surface, nothing slides over it, what you touch becomes the sheet, springs. Mark never gave a verdict on the 47 interactions; treat them as a well-reasoned proposal. He did ask (25 Oct): **"The page switching is bad. It should be smooth and elements extruding staggered."**

### Glass (not settled)
His idea (24 Oct): "for modals and popups we could use really good glass texture instead of clay … But not basic blur and semi transparent." Thick glass: "bad and really slow", "Nah lol this is terrible", "completely bugged". Liquid Glass via liquidGL: "much better now but still not looking great. Looks a bit weird", "not really impressed though", then reported broken on his phone. Native plan: real iOS 26 `.glassEffect`. See `reference/GLASS-NOTE.md`. Unconfirmed on device.

## 6. 24–25 Oct: the whole app in the new look (/next/)

- Mark's checklist for it (24 Oct 20:44): paddings and margins right, all functionality intact, every component checked, every element has interactions, nothing hardcoded that real data would break.
- Overnight passes 7a–7c with Review rounds r25–r27. 25 Oct morning on /next/: "Time chart looks bad", "Moat is not working", "remove the phone status bar", "page switching is bad", "Cards are looking pretty bad too" (cause found: cramped type, plates inside plates, thin shadows vs v7) → 7d plate spec (`reference/COMPONENTS.md`).
- Suggestions: "I love the suggestions idea … truly smart, based on what you are doing and where you are … enforced by push too"; proposed single slot → **"I think we drop the only one constraint."** Not built.
- 25 Oct 14:38 wind-down. **7e** went live on /next/ but **was never re-reviewed**. Review's six r28 blockers were addressed in 7e, untested: Weeks view Water totals, paused shown as "Not yet", page-switch smoothness, Time chart key, cards not on the plate, 22 px name clipping.

## 7. Lessons about working with Mark (from this history)

1. **Show, don't argue.** "Spend less effort arguing that an idea should work and more effort demonstrating whether its actual interaction is enjoyable."
2. **For feel questions, small self-playing sketches first** ("Do animations I can see, so iteration is faster and tou dont have to rebuild everything"). Full rebuilds to test a feel wasted days.
3. **Restate before building when he describes a physical feel.** The scroll took ~10 rounds until a restatement he confirmed with "Yes".
4. **Test at phone size, with touch, at 3× before showing.** Several "it's broken" / "scroll stopped working" / "not fullscreen" reports were shipping defects a device-size check would have caught.
5. **His questions are questions, not rules.** Research them and answer with reasons, including where he is wrong.
6. **Independent review catches function, not taste.** It passed screens he couldn't read. Only his eyes (or a faithful proxy built from his stated taste) judge beauty; design so he sees good options early.
7. **Don't drift visually while adding function.** "We must stop improving functionality while regressing visually." Review rounds that removed colour and depth "to avoid looking AI-made" made it plainer; richness must be an explicit bar.
8. **Decisions get lost across long sessions.** Keep one decision log and one requirement ledger, and re-check them every round.
9. **Short replies.** He reads on iPhone. One link, one question, no walls of text.
