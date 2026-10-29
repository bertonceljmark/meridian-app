# E. Integration proposal

18 Oct 2026. This shows how the shortlisted mechanisms could fit contract v1.1.1 and the Step A architecture (`whole/A-architecture.md`). Nothing here changes those files. The main design thread decides what earns a place.

## Principle

Proactive support is a **layer on top of items**, not a new product area. It adds three things:
- a *held* state, which says when an item should come back;
- a *window* on routines that have a real deadline;
- a *first step and runway* on start.

It adds no tab, no dashboard and no daily ritual. With every part of it switched off, Meridian is exactly the app in the main prototype (AS-17).

## Fit with the item model (contract §7)

| Need | Fits the existing model as | New? |
|---|---|---|
| A routine that should come back at an event, such as a twice-monthly date or a monthly deep clean | `reminders: optional cues`. The cue is a **moment** (an event anchor), not a clock time | Extends R-07 |
| A real deadline (trash on Thursday) | A routine with a weekly cadence plus a **window** (start, end, one last call). Its kind is up to Mark: a behaviour if he wants it counted, otherwise an unrewarded commitment | Small extension |
| A one-off intention (send the invoice, book the dentist) | **Not in the model today.** It would be an item with `cadence: none` that ends when done | **Needs Mark's decision.** It moves Meridian towards the task-manager boundary in §1 |
| A saved idea (flowers, the sauna) | An item with `cadence: none`, no target, no reminders, plus a cooldown | Needs the same decision |
| Start with a first step | The **session** measure type plus an optional first-step note plus a runway length | Extends the session grammar |
| Started versus finished | Entries already support partial and explicit states (R-09). A session that ended early is a recorded session, not a failure | No |

## Fit with the architecture (A §4)

- **Today.** The optional moment slot (A §4.1, "often empty") becomes where a held item whose moment has arrived appears. It holds at most one, and Hold's rules decide which. There are no new sections.
- **Log.** The Log sheet gains **Hold**. It's the same sheet, so capture from a widget, the Watch, the share sheet or Control Center uses the same code.
- **Held list.** Reached from Today's header and from the widget. It is a short view, not a tab.
- **Routines.** A routine's settings gain "bring it back" (a moment) and an optional window.
- **Time.** Records only what really happened: sessions, done, started. Held items and ideas have no history of non-action.
- **You.** One switch per layer: Moments, Deadlines, Ideas, Cross. There is also a visible daily interruption cap.
- **Watch and widgets.** A Smart Stack card and a Lock Screen widget show the next one or two held items. Interactive Done and Later buttons work without opening the app.
- **Architecture A §6 "Initiation"** says at most one suggestion, from cadence state. Hold sharpens this: Meridian suggests only things Mark held for this moment, or a saved idea when the evening is free. It never invents tasks from cadence alone.

## Contract checks

| Requirement | How it's met |
|---|---|
| R-07 optional reminders, under Mark's control | Every cue is one Mark chose. Everything is off until he turns it on |
| R-15 context, unknown stays unknown | Context can only hide ideas. It never infers availability |
| R-20 gamification, R-22 no artificial urgency | Holding or choosing earns nothing. Ideas have no points, streaks or due states. Urgency exists only for deadlines Mark created |
| R-21 no backlog, graceful absence | Nothing goes overdue. After 17 days away, the windows that passed show as unknown. Intentions that went quiet are still in Held, and ideas are untouched. There's no catch-up screen |
| §1 "is not a task manager or productivity coach" | One-off intentions are the risk; see the decision below. No priorities, projects, due dates on intentions, or productivity statistics |
| AS-17 core without depth | All of it is switchable off with no trace |
| R-26 direct control, no LLM | Everything is direct controls and deterministic rules. Optional on-device rewording at most |

## How it relates to gamification

Mark's priority 1 is establishing routines. The main prototype's evaluation found its motivation layer was still mostly accumulation. Proactive support doesn't fix that, and **it shouldn't be scored**. Making held items or starts into points would reward choosing over doing, and would turn gestures into transactions. Its contribution is indirect: more routines actually get started at a moment that works, and those real actions feed the existing progress and history.

## Decisions only Mark can make

1. **Do one-off intentions belong in Meridian at all?** Hold is most useful with them (the invoice, the dentist). Without them it still works for routines, deadlines and ideas.
   - The alternatives are a strict "items only" Meridian, or one-offs allowed but kept small (soft limit about 15, no due dates, they fade into ideas).
   - My recommendation is to allow them in the small form.
2. **Which experiments go to the main thread.** My recommendation is Hold first, Start second, and Cross only after a self-test (F).
