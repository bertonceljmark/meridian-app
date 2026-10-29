# C. Timing and adaptation model

18 Oct 2026. This is a proposal, not an approved design. It answers one question: how can Meridian help at a useful moment while inferring as little as possible and asking as little as possible?

**Short answer.** Let Mark name the moment with an event the phone can actually detect, deliver it once, and keep the item visible afterwards instead of repeating it. Learn only from what he explicitly does. Intelligent timing, meaning inferring when he is receptive, isn't worth its complexity for anything he has chosen or committed to. At most it might later choose when, inside a window he has allowed, to show an optional idea.

## 1. Three kinds of thing, three timing contracts

| | **Commitment** (trash on Thursday, a birthday present) | **Intention** (send the invoice, book the dentist) | **Opportunity** (flowers just because, try the sauna) |
|---|---|---|---|
| Who creates it | Mark, with a window or a date | Mark, with a moment ("bring it back when…") | Mark saves it, or he opted into a starter library |
| When it surfaces | The whole window, on ambient surfaces | Once, at the moment he picked | Only where there is room; never on a schedule |
| Interrupt budget | Optional cue at window start, plus one last call before it closes | One cue at the moment; one more at the next moment if he chose "later" | None by default. Passive only if he enables it, and at most 2 a week |
| Can context suppress it? | **Never.** Sleep, rest, vacation or a busy calendar can't remove it. Only Mark can (one tap: "I'm away this week") | No. Context may only offer a different default for "later" | Yes. Busy evening, sick, away or a short night all hide it or swap in a lighter one |
| What silence means | The window closes and the result is **unknown**, not failed | It stays held and visible. After two unanswered moments it stops interrupting | Almost nothing; a tiny lowering of priority |
| Reward | None, unless Mark made it a routine | None for holding it. A real action is recorded as itself | None. An optional private log of moments only |

This separation answers Mark's trash example directly. A deadline doesn't disappear because the system thinks he should rest. It also means an idea never borrows a deadline's urgency.

## 2. The cue vocabulary: moments the phone can actually detect

| Moment | How it's detected | Status | Caveat |
|---|---|---|---|
| A time or day | Local notification | **Verified** | Time-based, so it relies on the deficit. Offered last in the list |
| The next time Meridian is opened (optionally "on a weekday" or "this weekend") | In-app | **Verified, no permission** | Only works if he opens the app |
| When a calendar event ends | A notification pre-scheduled from EventKit | **Conditional** | Needs full calendar access. Goes stale if the event moves while the app is closed, so it re-syncs on every launch, widget refresh and background refresh |
| When work ends (or starts) | Meridian's Focus filter, run when the Focus changes | **Conditional** | Mark has to add Meridian's filter to a Work Focus once. I could not confirm in the docs that it runs on turn-off; needs an on-device check |
| Arrive at or leave Home or another place | Location notification trigger (When In Use is enough) or region monitoring | **Conditional** | 20-region limit, roughly 200 m and minutes of latency, nothing after a reboot until first unlock |
| A workout ends | HealthKit background delivery | **Conditional** | Often hourly or later, so it's useful for "after volleyball", not "the second I stop" |
| Shortcuts automations (CarPlay, Wi-Fi, alarm stopped) | An App Intent Mark adds in Shortcuts | **Conditional** | Mark has to set it up himself; offered only as an advanced option |
| Keep it visible, never notify | Widget, Watch Smart Stack, Live Activity | **Verified** | The Smart Stack order is a hint, not a guarantee |
| "When I'm free", "when I'm focused", "when I've stopped working" | — | **Not possible** | No API exposes mental availability, app content or free time. An empty calendar isn't free time |

All of this runs on the device, without a server or an LLM. Meridian compiles the next 1–3 days into system triggers whenever it gets time to run (64 pending notifications; repeating triggers count as one).

## 3. The delivery ladder

From least to most intrusive:

1. In-app, on next open
2. Widget or Watch card
3. Live Activity (during a window or a runway)
4. Passive notification (silent)
5. Active notification
6. Time Sensitive
7. AlarmKit (breaks through Focus and silent mode)

| Kind | Default | Maximum without Mark asking |
|---|---|---|
| Opportunity | 1–2 | 4, only if enabled |
| Intention | 5 at the moment, then 2 | 5 |
| Commitment | 2–3 for the window, 5 for the last call | 6. AlarmKit (7) only if he picks "must not miss" for that commitment |

**Global cap.** At most 3 interruptions a day outside commitments. When the cap is reached, items wait on rung 2. Mark can see the cap and change it.

## 4. Answering a cue: the five responses, without showing five buttons

| What Mark means | How he says it | What happens |
|---|---|---|
| Not now | Swipes the notification away, or ignores it | It stays visible on rungs 1–2. Nothing is inferred about the item |
| Remind me later | "Later" (the first action, so the Watch Double Tap does it) | It moves to **the next moment of the same kind**: tomorrow when work ends, the next time he's home. Long-press gives other moments. No snooze intervals |
| Not interested (this time) | Ideas only: "Some other time" | The idea rests for longer than before |
| Don't suggest again | Ideas: "Not this one". Intentions: "Drop it", from a long-press or the Held list | Gone. Recoverable from history |
| Already done | "Already done" or "Done" | Recorded with the real time. Nothing extra fires |

A notification shows 2–3 actions. Which ones depends on the kind: an intention shows Start, Later and Already done; a commitment shows Done and I'm on it; an idea shows Tonight, Some other time and Not this one.

## 5. How the two failure modes are prevented together

- **Forgotten intentions** are prevented by reliability and visibility, not repetition:
  - the cue is tied to an event;
  - it is delivered redundantly (Watch haptic plus phone);
  - after the cue, the item stays visible on the widget or Watch, ordered by how soon its next moment is.
  - **Every held item has a next moment.** Nothing sits in a list waiting to be remembered.
- **Notification fatigue** is prevented by:
  - one interrupt per moment;
  - a hard global cap;
  - automatic quieting after two unanswered moments. The item stays visible but stops interrupting.
  - **Nothing ever goes overdue.** An intention with no deadline that sits untouched for about four weeks moves quietly to Ideas. It isn't deleted and there's no guilt.
- **Back-off.** If Mark ignores three passive idea notifications in a row, ideas stop pushing and stay on the shelf. He doesn't need to change a setting.

## 6. Why "a morning card" isn't the model

Mark's own example is the argument: a good suggestion dismissed at 08:00 could be useful at 14:00, and something chosen in the morning can be forgotten by evening. A morning card fixes one moment for everything, catches him at a low point, and makes a daily ritual.

The model above keeps what is useful in the idea: he can pick "next time I open Meridian" or "tomorrow morning" as the moment for a specific thing, but morning is one anchor among many. Choosing something in the morning only helps if it returns at its real moment, which is what Hold does.

## 7. What context may and may not do

| Signal | May | May not |
|---|---|---|
| Short or poor sleep (HealthKit) | Swap a demanding optional idea for a lighter one; never show a "rest" prompt | Suppress commitments or intentions. It is never read as "Mark wants rest" |
| Calendar event this evening (e.g. volleyball) | Mark the evening as full for ideas | Infer that the rest of the day is free |
| Empty calendar | Nothing | Count as free time |
| Meridian context: sick, away, vacation | Hide ideas. Offer "when I'm back" as the default for Later | Silence commitments without asking: one tap pauses a commitment for that span |
| Many ignored cues | Reduce interruptions (§5) | Conclude that Mark dislikes the items |

## 8. What is learned, from how much data

A single user produces roughly 2–10 explicit responses a week. That is enough for counts and simple per-category rates. It is far too little for a receptivity model. Learned, with no questions asked:

- **Which moments Mark actually uses.** This orders the "bring it back" list, so his favourites come first.
- **Per item: his usual "later".** This sets the default when the item returns.
- **Per idea category: how often he acts on it.** A simple Beta count with lengthening cooldowns and rotation between categories keeps ideas from repeating.
- **Per routine: whether the cue still helps.** If he does the routine before the cue several times, the cue fades (B §7).

Not learned: mood, availability, motivation, "best time of day". There is no questionnaire and no rating.

## 9. Is intelligent timing worth it?

**Not now.** In the best studies, phone-sensor receptivity models misjudge 20–30% of moments. The best deployed gains were measured against random timing. A learning algorithm added about 7% in simulation, and every effect decayed within weeks. Fixed, predictable cues produced the larger effects in the trials reviewed. User-named event moments get most of the benefit attributed to "smart" timing at almost no cost: they are event-based (which suits ADHD), explainable and controllable.

**Only one place it might earn a role later** is choosing when, inside a window Mark has approved, to show an optional idea. Even that should ship as fixed rules first and be compared in-app (fixed versus inferred, randomly alternated) before anyone calls it intelligent.
