# R4: Rewarding interaction, accumulated history, and progression without finite content or punishment

Contract v1.1.1 read first. "Abstract" or "secondary" means I did not read the full text.

## 1. Established evidence

1. **Feedback: an inverted U, and success-dependence matters more than amplification.** (moderate)
   - Kao (2020): medium and high "juiciness" beat both none and extreme on experience, intrinsic motivation and playtime. Secondary summaries: https://arxiv.org/pdf/2011.09201
   - Kao et al. (CHI 2024), pre-registered, n=1,699: feedback that depended on success raised competence, effectance and curiosity; *amplification lowered them*. Curiosity was the only predictor of playtime. https://spiral.imperial.ac.uk/entities/publication/253c32f5-d124-4a23-88b5-9aaaf114608d
   - Visual embellishment raised visual appeal but raised competence only under specific conditions (Hicks et al. 2019, abstract): https://unpaywall.org/10.1145%2F3311350.3347171
   - *Meridian:* feedback should show what this action changed. Louder isn't better.

2. **Haptics.** (moderate)
   - Tactile confirmation brought touchscreen typing close to physical-keyboard performance (Hoggan et al. 2008, abstract): https://eprints.gla.ac.uk/43811
   - Apple's guidance is advice, not evidence: one causal meaning per pattern, intensity and sharpness matched to the animation, no overuse, always optional. "The best haptic experience is one that people may not be conscious of, but miss when it's turned off": https://developer.apple.com/design/human-interface-guidelines/playing-haptics

3. **Latency and continuity are what "physicality" is made of.** (moderate)
   - Devices showed up to 125 ms latency, and performance fell as latency rose (Jota et al. 2013, abstract): https://unpaywall.org/10.1145%2F2470654.2481317
   - Instrument design calls for "minimal and low variance latency" and "initial ease of use coupled with a long term potential for virtuosity" (Wessel & Wright 2002): https://opensoundcontrol.stanford.edu/publications/2002-Problems-and-Prospects-for-Intimate-Musical-Control-of-Computers.html
   - Apple's fluid-interface talk: instant response, 1:1 tracking, gestures redirectable mid-motion, projected momentum, soft rubber-band edges, spatially consistent paths. Default to 100% damping and add overshoot only to reward momentum: https://developer.apple.com/videos/play/wwdc2018/803/

4. **Measuring an activity can reduce enjoyment of it.** (moderate; 6 experiments)
   - People walked and read more but enjoyed it less, even when they had chosen to be measured. The effect was weaker when the activity was framed as work (Etkin 2016): https://scholars.duke.edu/publication/1134328
   - *Meridian:* this directly supports the owner's correction 3.

5. **Need satisfaction drives enjoyment.** (strong as theory) Autonomy and competence predicted enjoyment and continued play, and intuitive controls fed perceived competence (Ryan, Rigby & Przybylski 2006): https://acuresearchbank.acu.edu.au/item/8q128/the-motivational-pull-of-video-games-a-self-determination-theory-approach

6. **The right view depends on how much data exists.** (moderate; n=141 lapsed Fitbit users; full text read) Epstein et al. (UbiComp 2016): https://www.escholarship.org/content/qt51k9h1mg/qt51k9h1mg.pdf
   - Short or intermittent users found aggregations (by hour, by weekday) more informative. Long-term users preferred month and year timelines.
   - Reflecting on barriers was rated more judgmental ("snarky") than recalling past successes.
   - A count of days tracked inspired long-term users but discouraged those with little data ("disappointed in myself").
   - Encouragement to return helped guilty lapsers but felt "presumptive" to people who saw tracking as useless.
   - Showing old data in new formats is proposed as a way to bring people back.

7. **History becomes meaningful through interpretive work.** (moderate; qualitative)
   - Records became "meaningful digital possessions" only through people's own accounting. Design should help people build their own accounts, not assume more data will (Elsden et al. 2016): https://library.selfresearch.org/research/a-quantified-past-toward-design-for-remembering-with-personal-informatics/
   - Collecting, building and reflecting were intertwined when people built their own physical data displays (Thudt et al. 2018): https://ixlab.cs.sfu.ca/publications/self-reflection-and-personal-physicalization-construction

8. **Things people build gain value, but not once they are destroyed.** (moderate) Self-built objects were valued more, and the effect vanished if the object was destroyed or unfinished (Norton et al. 2012): https://dash.harvard.edu/handle/1/12136084
   - *Meridian:* this is a mechanism behind the binding no-destruction rule.

9. **Slow, sparse resurfacing.** (weak to moderate)
   - Photobox, 3 homes over 14 months: frustration at first, then acceptance, reflection on past events and renewed interest in the photo archive (Odom et al. 2014): https://www.dourish.com/classes/infx161f14/readings/Odom-DesigningForSlowness-CHI2014.pdf
   - Positive reminiscence raised self-reported happiness (Bryant et al. 2005; n=65): https://ideas.repec.org/a/spr/jhappi/v6y2005i3p227-260.html

10. **Milestones cause a slump after each one.** (moderate to strong; field data) Effort sped up near a reward and dropped after earning it, a pattern called "post-reward resetting" (Kivetz et al. 2006): https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal

11. **Lapses and self-comparison.** (moderate)
    - Responding to failure with self-compassion increased motivation to improve (Breines & Chen 2012): https://pubmed.ncbi.nlm.nih.gov/22645164/
    - People disparage *distant* past selves to feel they have improved; one non-Western sample did not replicate this (Wilson & Ross 2001): https://scinapse.io/papers/2058906994
    - The "what-the-hell effect" is reportedly worse with short-horizon, inhibitory goals. Secondary and unverified: https://more.efpsa.org/rpblog/?p=1172

12. **Variety raises adherence.** (moderate; RCT, n=121) Variety support increased exercise adherence through perceived variety, along with positive affect (Sylvester et al. 2016): https://researchportal.bath.ac.uk/en/publications/variety-support-and-exercise-adherence-behavior-experimental-and-

13. **Mature aesthetics.** (moderate; lab studies)
    - The best-liked designs maximise typicality and novelty together, "most advanced, yet acceptable" (Hekkert et al. 2003, secondary): https://www.jimdavies.org/summaries/HekkertSneldersVanwieringen2003.html
    - Two principles of aesthetic pleasure: "maximum effect for minimum means" and "unity in variety" (Hekkert 2006): https://pure.tudelft.nl/ws/portalfiles/portal/54686438/Hekkert_P._Design_aesthetics_principles_of_pleasure_in_design.pdf

14. **Theory, not evidence.**
    - Calm technology moves between the centre and periphery of attention: https://calmtech.com/papers/designing-calm-technology
    - Slow technology: https://unpaywall.org/10.1007%2FPL00000019
    - Ludic design, for curiosity rather than tasks: https://research.gold.ac.uk/4721/1/p885-gaver.pdf
    - Computational "edit wear and read wear": https://acawiki.org/Edit_wear_and_read_wear
    - I found **no peer-reviewed evidence** on prestige or reset mechanics.

15. **Platform facts (verified).**
    - **Controls** (iOS 18+): run App Intents from Control Center, the Lock Screen or the Action button without opening the app, and can require authentication: https://developer.apple.com/documentation/widgetkit/creating-controls-to-perform-actions-across-the-system
    - **Interactive widgets and Live Activities** use buttons and toggles through App Intents. They are inactive while the phone is locked, and Lock Screen accessory widgets are interactive only on iPhone and iPad: https://developer.apple.com/documentation/widgetkit/adding-interactivity-to-widgets-and-live-activities
    - **Live Activities** last up to 8 h active and 12 h on the Lock Screen, appear on the Watch, carry at most 4 KB of data, and can be started from a control: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities
    - **watchOS 26 controls** appear in Control Center, the Smart Stack and the Ultra's Action button. iPhone controls appear on the Watch but execute on the iPhone. RelevanceKit can use date, sleep schedule, fitness and point-of-interest signals: https://developer.apple.com/videos/play/wwdc2025/334/
      - *Conflict:* the hardware page lists only workout and dive intents for the Watch Action button: https://developer.apple.com/documentation/appintents/hardware-interactions
    - **Double tap** (Series 9 and Ultra 2 or later): one primary action per scene, including in Smart Stack widgets and Live Activities: https://developer.apple.com/documentation/watchos-apps/enabling-double-tap
    - **Digital Crown** detents with haptics: https://developer.apple.com/documentation/swiftui/view/digitalcrownrotation(detent:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:)
    - **Core Haptics** composes transient and continuous patterns, with sharpness, intensity and synchronised audio: https://developer.apple.com/documentation/corehaptics
    - **NFC:** background tag reading needs a notification tap and an unlock (https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading), but a Shortcuts NFC automation **can run without asking**: https://support.apple.com/en-asia/guide/shortcuts/apd602971e63/3.2/ios
    - **iOS 27:** Siri reaches app actions in natural language through App Intents schemas, and on-device Foundation Models are available: https://developer.apple.com/ios/whats-new/

## 2. Reasonable hypotheses (inferences)

- **Feedback should show consequence.** Satisfaction comes from seeing the specific change one entry made to something that persists: a period filling, a span extending. Generic celebration amplifies without informing (evidence 1, 8).
- **Curiosity is the return engine, not reward.** Honest uncertainty about real outcomes ("what will this month look like?") keeps the curiosity mechanism without random rewards (evidence 1).
- **An instrument rather than a game.** The floor is a single tap. The ceiling is optional expressive input. The pleasure is responsiveness plus mastery of one's own system (evidence 3, 5).
- **Progression that never runs out** combines three things, none finite and none destructible (evidence 7, 8, 10):
  - an artefact whose form is generated by Mark's own data;
  - growing self-knowledge;
  - chapters segmented from his actual life.
- **Rules by data regime** (evidence 6):
  - day one or sparse data: aggregations and "firsts";
  - intermittent: success framing and no tallies of days;
  - dense: month and year timelines.
- **Return as an update, not a guilt greeting** (evidence 6, 11).
- **Quiet feedback.** Relationship and creative routines may be best served by acknowledgement and memory, with no numbers (evidence 4).

## 3. Speculative opportunities

1. **Physical anchors (Mark hasn't mentioned these).** An NFC sticker on the water bottle, guitar case, shoes or journal triggers a Shortcuts automation that runs without confirmation and calls a Meridian App Intent, with a distinct haptic signature per routine. The log happens *where the act happens*. It needs one-time Shortcuts setup.
2. **Presets as felt notches.** The Digital Crown "pours" a quantity, with detents at Mark's customised servings and a distinct pattern at the target. Past the target, the notches go silent, so excess is never rewarded (R-22).
3. **Hands-full logging.** RelevanceKit surfaces the relevant routine in the Smart Stack (by sleep schedule or place), and double tap logs it. No notification is needed.
4. **Session Live Activities.** A control starts a practice or reading session. After it ends, the *result* stays on the Lock Screen and Watch for up to 4 h.
5. **A haptic vocabulary of about five patterns:** logged, period complete, first or record, a soft acknowledgement for observations (not a reward), and undo. Each always means the same thing, and sound is optional.
6. **Chapters from life, not calendar seasons.** Change points such as travel, illness, or a new or revived routine segment history. Mark can optionally caption a chapter, which adds the value of building it himself (evidence 7, 8). Retrospectives are assembled from these chapters.
7. **Rare resurfacing** on a widget, never a notification by default ("a year ago: the first of your twice-monthly dinners"). Frequency is tuned against habituation.
8. **Interface wear.** Heavily used routines and dense periods accrue a subtle patina along the history scrubber, so history becomes ambient.
9. **Records that can't be "failed":** "best since…", "first after a gap", and lifetime spans for rare routines. Comparisons only within the same context.
10. **Natural-language logging for rare routines** through iOS 27 Siri ("I just called Mum"). Verify on a device.
11. **Playful, reversible reconfiguration.** Merging, splitting, retargeting or reviving a routine shows an instant preview of how history would read. This draws on Mark's enjoyment of iterating on systems. It stays optional, so it never becomes "another demanding project".

## 4. Challenges to current assumptions

- **"Results as reward" isn't universal.** Evidence 4 predicts a cost from measuring activities Mark already enjoys, such as dates and social or creative routines. The loop is plausible for workouts and sleep. Identical reports also lose curiosity value, so results need real variety.
- **More juice is worse past a moderate level** (evidence 1). This supports Mark's rejection of loud ceremonies.
- **Milestones and levels** predict a slump after each one (evidence 10). Achievements can exist, but they shouldn't be the spine of progression.
- **Personal records:** comparisons with a past self are biased (evidence 11). Reports of Strava PR pressure come from low-quality sources and are unverified. A perfectionist needs records that can't be failed.
- **Calendar seasons and fresh starts** fit an irregular life poorly. Chapters derived from the life itself give landmarks without a reset.
- **Avoiding streaks isn't enough.** The wording of a period outcome can still read as "I failed" (evidence 11).
- **Welcome-back copy** suits some lapsers and offends others (evidence 6). Default to neutral.
- **Day one:** tallies discourage people with little data (evidence 6).
- **Prestige loops** conflict with the binding no-destruction rule and have no evidence base.
- **Mark's own explanation** stresses "tactical choice" (Clash Royale, chess). Evidence 1 suggests the transferable part may be *legible, graded success plus curiosity*. Tactical choice applied to routines risks becoming a chore.

## 5. Open questions

1. Which of Mark's routines does quantification help, and which does it harm? Can a per-routine "quiet" mode be set without adding configuration burden?
2. What accumulated form is honest to the data, never repeats, reads well on day one and at year scale, and is satisfying to change with a single entry?
3. In a within-person trial, do NFC anchors and Crown notches raise logging and enjoyment compared with tap-only logging?
4. Which sources of honest uncertainty sustain curiosity without becoming a variable-reward schedule?
5. Can the Watch Action button run a non-workout control on watchOS 26 or 27? The docs conflict, so test on a device.
6. How often can resurfacing happen before it habituates?
