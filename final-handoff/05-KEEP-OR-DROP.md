# 05 · Your old context: what to keep, what to let go

You (the local session) built native Meridian infrastructure before this cloud work. Since then Mark spent 11 days redefining the product. Most of your earlier design context is superseded. Infrastructure may be reusable. Decide with evidence, not memory.

## 1. Order of authority when sources disagree

1. Mark's newest words (`evidence/owner-messages-2-after-log.md`, then `-1-log.md`). Newer beats older. Short informal messages beat long pasted prompts.
2. `reference/CONTRACT.md` layer A, and `ledgers/feature-ledger.json` items with `confirmed` = owner/contract.
3. Recorded decisions (`reference/DECISIONS*.md`, `reference/review/REVIEW-DECISIONS.md`, `reference/review/21-flow-findings.md`).
4. Research (`reference/research`, `analytics`, `ef-support`, `ledgers/research-ledger.json`): advice, never a reason to narrow a requirement.
5. Anything an AI proposed that Mark didn't endorse, including your own old docs and this package's suggestions.

## 2. Almost certainly drop

- Every earlier visual design and IA: Day Miniature, ledger/print styles, all metaphors (Long Road, Night Sky, Town, Seasons…), the timeline-sheet structure.
- The old gamification engine content: streaks, XP, levels, chapters, combos, collectibles, "kept". Mechanisms and code that implement them.
- Per-routine special cases (code keyed on routine names or seed ids), seeded "baseline" categories, the "Plan the week" sample routine.
- Mandatory ratings, 1–10 scales, required reflection.
- Anything walking-only, Concerta/ADHD-specific, or medication-rewarding.
- Old process habits Mark called out: freezing decisions before he saw interactive work, declaring concepts successful, the builder grading itself.

## 3. Probably keep, after you verify it

- Xcode project, targets (iPhone, Watch, widgets), signing setup.
- HealthKit integration, permissions flows, background delivery.
- Persistence layer, migrations, sync, export.
- Generic data model pieces: routines with measure/cadence/target history, entries, observations, coverage. Compare against 03-SPEC §1 and `reference/analytics/A-data-model.md`; adapt rather than rewrite if it fits.
- Tests (500+): keep the ones that test still-valid logic; delete ones that encode dropped behaviour.

## 4. Audit procedure (do this first, write the result down)

1. Inventory the existing repo: targets, modules, models, views, tests. Build it and run the tests; record what passes.
2. For each module, mark **keep / adapt / drop** with one line of evidence against 01–03 and the ledger. Put it in `docs/AUDIT.md` (in the native repo).
3. For your old docs/notes/CLAUDE.md: list each standing rule and mark it **still true / superseded (by which message) / unknown**. Rules marked unknown go to Mark only if they change the goal; otherwise decide.
4. Map the 625 feature-ledger items to native: `ledgers/feature-ledger.json` → `docs/TRACE.md` or a JSON with `native_status` (planned / built / verified / dropped-with-reason). Never drop silently.
5. Only after the audit, write the build plan (06-PROCESS phase 1).

## 5. The prototype is evidence, not the spec

Port the approved feel (look, scroll, motion, depth, colour per routine), the logic rules and the requirement coverage. Do not port the web IA, copy or components blindly: Mark is not happy with the result and expects everything re-validated. Where you change something, record why (decision log) and show him the difference small and early.
