I'm attaching meridian-final-handoff.zip. Unzip it into this repo as `handoff/` and read `handoff/START-HERE.md`, then every file it lists, in order, before doing anything else.

Context: after you built the native infrastructure, I spent 11 days with another Claude redefining Meridian: goal, logic, look, motion and a full web prototype. The package holds my messages verbatim, what I approved and rejected and why, the spec, the prototypes and the lessons learned. Most of your earlier design context is now invalid; some infrastructure may still be useful.

Your job is to turn this into the final native app (iPhone, Watch, widgets), and it has to be really polished. I'm not 100% happy with the prototype. Validate everything again: UI, flows and the logic itself. Anything can change if evidence backs it. Stay rooted in what I actually want (`01-GOAL.md` and my messages in `evidence/`), not in what any AI proposed.

How I want you to work:
1. First, audit your existing code, docs and old rules against the package (`05-KEEP-OR-DROP.md`). Write down what you keep, adapt and drop, and why. Also fix your own process: replace any old rules that conflict.
2. Set up the process in `06-PROCESS.md`: owner log, decision log, requirement trace, and verification gates. Improve it where you see a better way.
3. Do the validations yourself, proactively: tests, simulator screenshots on several sizes, recordings, performance checks, and a separate reviewer agent that didn't write the code. I shouldn't have to ask for the extra step. When I catch something, add the check that would have caught it.
4. Only show me things that passed the gates. Keep messages short. Ask me only about taste or goals, one question at a time, with something small to look at.
5. Install `handoff/CLAUDE.md` as the repo's CLAUDE.md, merged with anything still valid from your current one.

Start with the audit and a short plan. Then keep going.
