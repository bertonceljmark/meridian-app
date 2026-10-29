# Homes worth opening: how 8 products handle many items without a dashboard
Research thread, 19 Oct 2026, for Studio's home test (`review/03-studio-brief-home-test.md`). Execution only, not visual style. Not Boring is covered in `integration/research/not-boring.md`.
[V] = checked against a source this session. [K] = from product knowledge, not re-checked today, so confirm the details before relying on them. [I] = my inference.

## The one finding that matters most
**None of these homes shows the inventory.** Each one stores tens to hundreds of items, but the home holds only what *changed since your last visit* or what *is waiting on you now*. Things doesn't show your 300 to-dos, Chess.com doesn't show your 40 finished games, and the Smart Stack doesn't show all your widgets. Each product has a firm rule for what counts as "alive". Everything else is dormant (out of sight until its moment) or archived (one gesture away). The reason to open is **news**: something the person didn't fully cause, or doesn't yet know, has arrived. That might be an opponent's move, a report from last night, a date that has come, or a world that changed overnight. A dashboard answers "how is everything?" A home worth opening answers "what's new, and what's mine to do?" [I, from the cases below]

## Cases

**1. Things 3: dormancy is a feature.** You open Today and see only what you chose for today, plus a separate "This Evening" band. A to-do with a future start date leaves every list and waits in Upcoming. On its date it "transforms into an actionable item in Today". Projects with future start dates hibernate and vanish from the sidebar. Someday is a deliberate home for "not now", not a failure state. [V culturedcode.com/things/support/articles/2803579; blakecrosley.com/guides/design/things]
*Principle:* each item carries a "when it becomes alive" rule, and the home is just the set of items whose moment has come. Waking up is an event the person sees ("it's back"). The empty end of the day is a legitimate, calm state. [I]
*For 60 items:* twice-a-month routines spend most of their life dormant and never show as "0 of 1".

**2. Chess.com daily games: only "your move" sits at the top.** With 20 correspondence games running, the home lists the games where it is your turn. Games waiting on the opponent drop below or out of view. A move notification brings you back. [K]
*Principle:* the person is called back by **someone or something else acting**, not by their own backlog. Something they care about is in an unresolved state that only they can resolve. [I] In Meridian the "other party" can be the world: a run that arrived from the Watch, a period that opened, a moment Mark himself set earlier (a held intention).

**3. Clash Royale: they removed the waiting.** For years the home was organised around four chest slots on timers, so you came back because something had *ripened*. In March 2025 Supercell removed chest timers, slots and cycles, and replaced them with Lucky Drops opened right after each match. The stated reason was that timers delayed the reward, so players couldn't "enjoy their success in the moment". [V royaleapi.com/blog/rip-chests-2025-q1-update; egw.news 26988]
*Principle:* "come back later to collect" makes people return to the app, not do the thing, and even its inventor dropped it in favour of reward at the moment of the act. That agrees with research finding 1 in `05-synthesis.md` (the reward belongs in the doing). **Ripening is evidence for returning, not for acting.** If it is used at all, it should only show what accumulated history has made visible, never as a reward held back.

**4. Apple Watch Smart Stack: rank by context, show one thing.** The stack orders widgets using time, location, activity and app-provided relevance hints, such as "every time a person starts a workout". The user can pin items to the top. A relevance-driven widget can produce one card per relevant entry. [V developer.apple.com/documentation/widgetkit/widgetrelevancegroup; WWDC23 10309]
*Principle:* with a small screen and many items, the system **commits to a guess** and puts the most relevant thing first. The rest is a scroll away, and the user can override the guess. Being wrong is cheap because nothing is hidden. [I] This is the same design question as Review's A3 (is the Watch home a list or the single most-alive item?).

**5. Oura Today: the same home changes through the day.** A 2024 redesign cut five tabs (Home, Readiness, Sleep, Activity, Resilience) down to Today, Vitals and My Health. Today leads with what matters when you wake up and "surfaces insights through the day". A daily highlight changes with the time of day, and a timeline shows your day. [V ouraring.com/blog/new-oura-app-experience]
*Principle:* one surface, with **content set by time of day**. The morning, evening and Sunday homes differ because different things are alive, not because the user navigates. Oura also folded separate category tabs into one "today", which is the same move as dropping a home organised by routine. [I]
*Caution:* Oura's morning hero is a score. Meridian has no score to lead with, and shouldn't invent one. [I]

**6. Sleep Cycle (and Oura mornings): the report that is already waiting.** In the morning you open the app to a finished night: graph, time asleep, sometimes a snore clip. You did nothing except sleep, and the result is new, about you, and slightly uncertain until you look. [K]
*Principle:* curiosity about **your own unknown outcome** is a strong reason to open. It works because the person didn't log anything to earn it. In Meridian this maps onto imports (the 19:12 run, sleep, steps), which arrive by themselves. That makes the run arriving at 19:12 the closest thing Meridian has to a "your move" moment. [I] Remember finding 2 in 05: fast informational payoffs build checking habits, so the arrival should invite acting or noticing, not an endless review.

**7. Duolingo: the path shows one next step, not a catalog.** In 2022 Duolingo replaced a tree of skills, where people could wander and rarely levelled up, with one ordered path. The current node is obvious, past nodes sit behind you and the rest lie ahead. [V blog.duolingo.com/new-duolingo-home-screen-design; heavy user backlash, NBC rcna44655]
*Principle:* making the **next step obvious** removes the choice of where to start, which is the hardest part for an ADHD user facing 60 options. [I] *Limit:* this only works for one sequential activity. Meridian's routines run in parallel at mixed cadences, so it shouldn't borrow the path, only the idea that one thing is clearly next and you can still pick another. The backlash shows the cost of taking away the user's own order.

**8. Animal Crossing: the world changed overnight, and there's a finite amount to find.** Each day there are new fossils to dig, four rocks to strike, a visitor and a changed shop. Seasons and real-time events change what's there. Reviewers describe a short, bounded daily loop that "gives you something new every day" without taking over your life. [V salon.com 2020/03/30; collegian.com AC review] [K for the item counts]
*Principle:* the reason to open is **a small, finite amount of discovery that renews each day**, and when it's gone you're done. There is no infinite list and no backlog after a week away, because missed days simply aren't kept. Returning after months shows a changed, weedy island, which is gentle and sometimes funny. It is not a ledger of what you missed. [K/I]

**Also checked: Strava.** Home is the feed of people you follow plus your own uploads, and your stats live in the You tab. [V triathlete.com Strava layout] Social news is its reason to open. Meridian has no social graph, so the only part that carries over is that **your own new activity arrives as an event** (an upload with segment and PR results attached), not as a row filling up. [I]

## Patterns across the cases (use these, not the products)
1. **Liveness rule over list.** Each item knows when it is alive (period open and reachable, just arrived, its chosen moment has come, a dormant item waking). The home is the set of live items. If nothing is live, the home is calm and complete, not empty. *(Things, Smart Stack, Chess)*
2. **News first.** The top of the home is what changed since the last visit: arrivals, things waking, an observation's moment. Without anything new, there is no reason to open. *(Sleep Cycle, Chess, Animal Crossing)*
3. **Someone else moved.** The strongest pull is a state that another party (the Watch, the calendar, the season, Mark's past self) left waiting for you. *(Chess, Sleep Cycle, Things start dates)*
4. **Time of day sets the content, not navigation.** *(Oura, Smart Stack, Things' Evening)*
5. **Commit to a guess, keep the rest one gesture away, let the user pin.** *(Smart Stack, Duolingo)*
6. **Bounded daily novelty, no carry-over.** Missed days are not kept, so the return is a changed world, not a backlog. *(Animal Crossing, Things)*
7. **Don't hold rewards back to make people come back.** Clash Royale's own reversal is the clearest evidence. Reward the act at the moment of the act. Accumulated history can "ripen", but only as something newly visible, never as a gift withheld. *(Clash Royale)*

## Questions these cases leave open (for Studio, not answered here)
- On a quiet Thursday with nothing new, what fills the home without falling back to inventory? Animal Crossing's answer is that the world itself is slightly different. Things' answer is "nothing, and that's fine". Both are legitimate.
- Is Mark's past self (an intention he set, a routine he configured for "evenings") enough of an "other party" to create a "your move" pull? It is plausible, but none of these products proves it.
- Which accumulated pattern can be newly visible at month six without becoming a score?
