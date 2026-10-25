# Open items at handoff

## Not yet done
- **Smart suggestions** (Mark loves the idea).
  - Now shows due routines plus a couple of context-fitting suggestions, marked as suggestions and ranked by fit.
  - There is no limit of one at a time.
  - Triggers are named moments (arriving at work, a meeting ending, 2 h of sitting), based on activity and location.
  - Pushes are few, can be logged straight from the push, and back off when ignored.
  - Not built.
- **Gamification** is unsolved. The "Cut" idea was rejected on 21 Oct.
- **Glass for modals and popups.** Thick glass was rejected. The liquidGL test at `/liquid-glass/` was never confirmed on Mark's phone. On iOS, use native Liquid Glass materials instead.

## Known rough edges in 7e (web prototype)
- **Page-change frame rate.** In headless tests it matches 7c, but the push/back render frames are slow (550–650 ms of React rendering). Native SwiftUI avoids this.
- **Unpressable controls.** 2–3 tappables have no visible press: the dial's drag ring, an already-selected segment, and one feel-page row.
- **Stuck plate.** 1 stuck plate after a swipe on the Log sheet at 430 px width.
- **Pending review.** Review's final re-check of 7e was still pending when processes stopped.
