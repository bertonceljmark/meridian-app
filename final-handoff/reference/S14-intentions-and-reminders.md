# §14 · What the architecture must leave open for intentions, reminders and contextual support

18 Oct 2026. This answers §14 of Mark's 17:10 message. It is **not** a reminder design, and nothing in it is approved.
- It says only which distinctions and openings the main product's data model and platform plan must keep, so that the separate executive-function research can later land without a rewrite.
- That research is not read or anticipated here.
- No reminder system is added to the prototype.

## 1. The one structural change: reminders stop being a routine setting

Today, in the whole-product prototype and contract R-07, a reminder is a field on a routine (`reminder: {text}`). That cannot express a Thursday deadline for a Friday collection, a flowers opportunity, or "remind me later".

**What must stay open:** **prompts** become their own records that *refer to* items. They are not attributes *of* items.

- A routine can exist with no prompts.
- A prompt can exist with no routine. Examples: a one-off commitment, an opportunity, or an intention about something Meridian doesn't track.

## 2. Six kinds that must not collapse into one

The six kinds differ in who created them, how time works, what persistence means and what a dismissal means.

| Kind | Example | Created by | Time | Persists until | A swipe-away means |
|---|---|---|---|---|---|
| **Commitment with a real deadline** | Trash out before Fri 07:00 collection | Mark, or a recurring rule he set | A window ending at a **latest useful moment** (Thu night), derived from an external event | Done, or explicitly dropped | Not now. It never means "uninterested", and the deadline still stands. |
| **Flexible routine** | Meditation, 3 a week | Mark (the routine) | The routine's period; no single moment | The period ends; the next period starts fresh | Nothing about the routine |
| **Optional opportunity** | Buy flowers | Mark's idea, or a Meridian suggestion | Loose; may be tied to a context such as "near a florist" or "before date night" | It quietly expires; never recurs unless Mark makes it recur | Not now. It is never counted as missed and never becomes a task. |
| **Intention for later** | "Tonight I'll practise" | Mark, explicitly | A time or context he chose | Begun, done, or let go | Unknown, and it stays his intention |
| **Explicit reminder** | "Remind me at 18:00" | Mark, explicitly | Exactly what he asked for | Delivered, then done or snoozed | Snooze. Meridian must not reinterpret it. |
| **Deferred suggestion** | A suggestion parked at 08:00 | Meridian | May resurface in a different context | Accepted, declined explicitly, or aged out | **No information.** It is not rejection. |

Every prompt record therefore needs:
- `kind`;
- `origin` (Mark or Meridian);
- a link to an item, if any;
- a **time window** (earliest, preferred, latest useful, hard deadline, each optional);
- **optional context conditions**;
- **recurrence, independent of any routine cadence**;
- a **persistence rule**.

**User-defined scheduling constraints** sit above all prompts:
- "not before 09:00";
- "not during work hours";
- "never on Sundays, except deadlines".

## 3. Lifecycle: keep three separate tracks, never one status enum

A single status such as `dismissed` or `done` is the trap. The model needs three independent tracks.

1. **Response: what Mark did with the prompt.**
   - Values: unseen, seen, opened, swiped away, not now (until a time or context), remind me later (explicit time), not interested (an explicit choice, scoped to *this one* or *this kind*), done by hand.
   - Only the explicit "not interested" may suppress anything. A swipe-away, a timeout or an unopened notification records **no preference**.
2. **Intention: what Mark committed to.**
   - Values: chosen, begun, completed, let go, expired.
   - "Chosen" and "begun" are his statements. "Completed" requires evidence.
3. **Evidence: what actually happened.** This lives in the existing entry model and comes from his record or a passive source (a Watch workout, a HealthKit sample).
   - An opened reminder is **not** evidence.
   - An accepted intention is **not** a completed activity.
   - A missed suggestion never writes anything into a routine's history. The routine's period is judged only by entries, as now.

Corollaries:
- **Dismissing at 08:00 leaves the suggestion eligible later.** The research decides when it reappears.
- **The architecture must store enough to avoid nagging:** per prompt, the times it was shown and the responses to it. The research decides the back-off.

## 4. Context: inputs, labelled by how much they can be trusted

- **Optional and opt-in.** Each context source is opt-in, stays on the device, and is labelled as **known** or **inferred**.
- **Known:** "a calendar event exists 14–16", "Focus filter Work is on", "inside the home region", "a workout is in progress".
- **Inferred:** anything beyond that. Inferences may be stored for one decision but never written as facts, and never reused by analytics as if they were measurements.

Fixed rules the model must enforce, whatever the research proposes:
- **An empty calendar is not availability.** Calendar data can only say "probably occupied", never "free to act".
- **Device signals never establish readiness, motivation or attention.** That includes sleep, heart rate, motion and screen use.
- **Poor sleep never suppresses or delays a commitment with a real deadline.** Commitments and explicit reminders are outside every suggestion heuristic.
- **"Why am I seeing this?"** Each prompt shown keeps the reason and the inputs it used, so Mark can see why it appeared and so analytics can tell suggestions from facts (§15).

**Shared context, not shared semantics.** A context episode such as a work trip or being sick is one record. Analytics may read it to interpret data, and prompts may read it to adjust what's realistic. Neither system changes the other's records.

## 5. Delivery: one prompt, several possible surfaces, under one budget

- **The surfaces:** the in-app Today, a Home or Lock Screen widget, the Watch Smart Stack or a complication, a notification, and a Live Activity for something already under way.
- **Choosing a surface is a delivery decision,** stored separately from the prompt. Mark's per-kind channel preferences decide it. Example: deadlines may notify; opportunities appear only in-app and in widgets.

**Interruption budget (the opening needed):**
- A per-day, per-channel ceiling that Mark can set, with per-kind caps and a repeat limit for the same prompt.
- Explicit reminders and real deadlines are what he asked for, so they are not charged against the *suggestion* budget. They still respect his quiet hours unless he marks them otherwise.

## 6. Platform constraints the plan must accept

These need verifying against the current SDK before anything relies on the numbers.

- **No continuous context evaluation on iOS.**
  - Background work is opportunistic (`BGAppRefreshTask`).
  - Timing must be **pre-scheduled** (time triggers, at most 64 pending local notifications) or **event-triggered** (location regions, about 20 monitored per app; HealthKit background delivery, e.g. a workout saved).
  - "Context-aware timing" therefore means *choosing among triggers ahead of time*, or reacting to a few system events. It does not mean watching the user.
- **Focus.**
  - The app cannot read which Focus is on.
  - It can offer a **Focus filter** that Mark configures (e.g. "in Work Focus, only deadlines"), and it can mark notifications as time-sensitive. Time-sensitive needs the entitlement, and Mark can turn it off per app.
  - Scheduled Summary may batch ordinary notifications.
  - Newer system alarm APIs (AlarmKit) may suit explicit reminders and hard deadlines. Verify.
- **Widgets and Watch.**
  - Widgets refresh on a budgeted timeline (roughly tens of reloads a day), so they show *what's relevant in a window*, not live decisions.
  - The Smart Stack accepts relevance hints. A Watch complication shows one small fact.
- **Authorization.** Notifications, calendar (full access versus write-only), location (when-in-use versus always) and HealthKit are separate permissions. Each prompt kind must degrade gracefully when a permission is missing.

## 7. With everything switched off

With prompts, notifications and context all off, Meridian loses nothing else:
- routines, logging, Today, Time, reports, patterns and growth all work;
- Today shows what's in play from cadence state alone.

This is a test case for every future proposal.

## 8. Changes this implies for the prototype later (not now)

1. Replace `item.reminder` with a separate prompt store that refers to items.
2. Creating a routine offers "add a prompt" as an optional link, not a reminder step.
3. Add three tracks (response, intention, evidence) to the data model.
4. Add a context record shared with analytics.
5. Add the budget and quiet-hours settings under You.

None of this is built until the executive-function research is reviewed.

## 9. Questions this leaves for the executive-function research (not answered here)

- When does a parked suggestion reappear, and how quickly does it back off?
- Which kinds may interrupt, and by default on which surface?
- How is "chosen → begun" captured with no extra work? Is it a tap, starting a session, or nothing?
- What does a good "not now" look like on the Watch?
- How do opportunities get their context without new manual input?
