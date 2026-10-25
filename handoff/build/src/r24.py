"""Review r24, folded into 7a (applied to the p6i text before the 7a look). Each patch must match exactly once."""
import re, sys

def rep(s, a, b, n=1):
    c = s.count(a)
    if c != n: sys.exit(f'r24 patch count {c} != {n}: {a[:100]!r}')
    return s.replace(a, b)

def apply(src):
    # BLOCKING (rd2): a target set or changed applies to the period in progress; only finished periods keep their old rule
    src = rep(src, "const nt = { from: w.today, ...(tg.cmp === 'range'",
      "const cadence = t.cad === 'everyN' ? { type: 'everyN', n: t.n } : { type: t.cad }; const pa = Math.min(w.today, Math.max(it.src.created || 0, periodOf({ ...it.src, cadence }, w.today)[0])); /* r24: from the start of the period in progress */\n"
      "  const nt = { from: pa, ...(tg.cmp === 'range'")
    src = rep(src, "const targets = [...(it.src.targets || []).filter(x => x.from < w.today), nt]; const cadence = t.cad === 'everyN' ? { type: 'everyN', n: t.n } : { type: t.cad };",
      "const targets = [...(it.src.targets || []).filter(x => x.from < pa), nt];")
    # the toast says it plainly (r24: "Observation, no target… Past periods keep theirs" read oddly)
    src = rep(src, "M.closeSheet(); M.patch(it, { targets, cadence }, 'Saved', `${E.cadText({ ...it, src: null, cad: t.cad, n: t.n }, tg)}, from now. Past periods keep theirs.`); });",
      "const pw = t.cad === 'everyN' ? 'window' : t.cad; const said = E.cadText({ ...it, src: null, cad: t.cad, n: t.n }, tg);\n"
      "  M.closeSheet(); M.patch(it, { targets, cadence }, 'Saved', it.kind === 'observation' ? (tg.cmp === 'none' ? 'No intention now. It’s noted when it happens.' : `${said}, starting this ${pw}`) : tg.cmp === 'none' ? 'No target now. It’s recorded as it happens.' : `${said}, starting this ${pw}. Earlier ${pw}s keep the rule they had.`); });")
    src = rep(src, "it.tg.cmp === 'none' ? 'Starts today. Until now it had no target, so nothing earlier counts against it.'",
      "it.tg.cmp === 'none' ? `Counts from the start of this ${t.cad === 'everyN' ? 'window' : t.cad}. Before that it had no target, so nothing earlier counts against it.`")
    # the same rule in the app's own target sheet: a routine without a period gets one from the start of this period
    src = rep(src, "const from = noCad && cmp !== 'none' ? db.today : when === 'now' ? ns : nextStart;",
      "const from = noCad && cmp !== 'none' ? Math.min(db.today, Math.max(it.created || 0, periodOf({ ...it, cadence: { type: pd } }, db.today)[0])) : when === 'now' ? ns : nextStart; /* r24 */")
    # context: holiday rests routines too
    src = rep(src, "<div class=\"sub\">On sick and away days, routines rest and those days are set aside, not missed.", "<div class=\"sub\">On sick, away and holiday days, routines rest and those days are set aside, not missed.")
    src = rep(src, "<h2>Cues on sick and away days</h2>", "<h2>Cues on sick, away and holiday days</h2>", 2)
    src = rep(src, "<p className=\"t-s\">On sick and away days, routines rest.</p>", "<p className=\"t-s\">On sick, away and holiday days, routines rest.</p>")
    src = rep(src, "label=\"Cues on sick and away days\"", "label=\"Cues on sick, away and holiday days\"")
    # context: newest first, always; an open span reads as ongoing
    src = rep(src, "past = w.contexts.filter(c => c.to < w.today).reverse(), next = w.contexts.filter(c => c.from > w.today);",
      "past = w.contexts.filter(c => c.to < w.today).sort((a, b) => b.from - a.from || b.to - a.to), next = w.contexts.filter(c => c.from > w.today).sort((a, b) => a.from - b.from); now.sort((a, b) => a.from - b.from); /* r24: in date order */")
    src = rep(src, "<small>${D.range(c.from, c.to)}, ${plural(c.to - c.from + 1, 'day')}${c.keep",
      "<small>${c.open ? `Ongoing, since ${D.day(c.from, { noDow: true })}` : `${D.range(c.from, c.to)}, ${plural(c.to - c.from + 1, 'day')}`}${c.keep")
    # a v3 sheet never outlives the page it was opened over: any route change closes it
    src = rep(src, "    push: (r, t) => { const tt = t || tab; setLeaving(null);", "    push: (r, t) => { const tt = t || tab; setLeaving(null); setSheets(ss => ss.some(x => x.k === 'v3') ? ss.filter(x => x.k !== 'v3') : ss); /* r24 */")
    src = rep(src, "    reset: (t, routes = []) => { setLeaving(null);", "    reset: (t, routes = []) => { setLeaving(null); setSheets(ss => ss.some(x => x.k === 'v3') ? ss.filter(x => x.k !== 'v3') : ss); /* r24 */")
    src = rep(src, "    setTab: t => { setLeaving(null);", "    setTab: t => { setLeaving(null); setSheets(ss => ss.some(x => x.k === 'v3') ? ss.filter(x => x.k !== 'v3') : ss); /* r24 */")
    src = rep(src, "    pop: () => setStacks(s => {", "    pop: () => { setSheets(ss => ss.some(x => x.k === 'v3') ? ss.filter(x => x.k !== 'v3') : ss); setStacks(s => {")
    src = rep(src, "return { ...s, [tab]: st.slice(0, -1) }; }),\n", "return { ...s, [tab]: st.slice(0, -1) }; }); },\n")
    # caffeine: a new drink is confirmed, and a name already there is not added twice
    src = rep(src, "on('dadd', () => { const n = M.q('[data-dn]').value.trim(); if (n.length < 2) return; const m = /(\\d+)\\s*mg/.exec(n); const it = cafIt(); const mg = m ? +m[1] : 80; M.patch(it, { servings: [...it.src.servings, { id: uid('sv'), name: n.replace(/,?\\s*about\\s*\\d+\\s*mg/i, '').trim(), sub: `≈ ${mg} mg`, mg }] }, 'Drink added', `About ${mg} mg`); M.afterDraw(drinksSheet); });",
      "on('dadd', () => { const n = M.q('[data-dn]').value.trim(); if (n.length < 2) { M.toast('Name it first', 'e.g. Matcha, about 70 mg'); return; } const m = /(\\d+)\\s*mg/.exec(n); const it = cafIt(); const mg = m ? +m[1] : 80; const nm = n.replace(/,?\\s*about\\s*\\d+\\s*mg/i, '').trim();\n"
      "  const dup = (it.src.servings || []).find(s => s.name.trim().toLowerCase() === nm.toLowerCase()); if (dup) { M.toast(`${dup.name} is already one of your drinks`, `About ${dup.mg} mg. Change it above`); return; } /* r24 */\n"
      "  M.patch(it, { servings: [...it.src.servings, { id: uid('sv'), name: nm, sub: `≈ ${mg} mg`, mg }] }, `${nm} added`, `About ${mg} mg, in your familiar drinks`); M.afterDraw(drinksSheet); });")
    src = rep(src, "const save = close => { const s = { id: uid('dr'), name: name.trim(), sub: `≈ ${lo}–${Math.max(lo, hi)} mg`, mg: Math.round((lo + Math.max(lo, hi)) / 2), own: true };",
      "const save = close => { const dup = (it.servings || []).find(x => x.name.trim().toLowerCase() === name.trim().toLowerCase()); if (dup) { S.toast({ title: `${dup.name} is already one of your drinks`, sub: 'Pick it from your familiar drinks', neutral: true, glyph: it.glyph, hue: 0 }); return; } /* r24 */ const s = { id: uid('dr'), name: name.trim(), sub: `≈ ${lo}–${Math.max(lo, hi)} mg`, mg: Math.round((lo + Math.max(lo, hi)) / 2), own: true };")
    # unit plurals, everywhere a count meets a unit: "1 rep", never "1 reps"
    src = rep(src, "else if (it.measure === 'reps') amt = `${tg.v} reps`;", "else if (it.measure === 'reps') amt = plural(tg.v, 'rep');")
    src = rep(src, "if (it.measure === 'reps') return ev.v ? `${ev.v} of ${tg.v} reps` : `aim ${tg.v} reps`;", "if (it.measure === 'reps') return ev.v ? `${ev.v} of ${plural(tg.v, 'rep')}` : `aim ${plural(tg.v, 'rep')}`;")
    src = rep(src, ": it.measure === 'reps' ? 'reps' : it.measure === 'passive' || it.measure === 'duration' ? 'min'", ": it.measure === 'reps' ? (n === 1 ? 'rep' : 'reps') : it.measure === 'passive' || it.measure === 'duration' ? 'min'")
    SING = {'reps': 'rep', 'days': 'day', 'weeks': 'week', 'times': 'time', 'sessions': 'session', 'nights': 'night', 'entries': 'entry', 'minutes': 'minute', 'sets': 'set'}
    n0 = [0]
    def fx(m):
        e, u = m.group(1), m.group(2)
        if re.fullmatch(r"\s*\d+\s*", e) or '`' in e or "'" in e and '?' in e and not re.search(r'\w\s*$', e): return m.group(0)
        n0[0] += 1
        return '${' + e + '} ${(' + e + ') === 1 ? \'' + SING[u] + '\' : \'' + u + '\'}'
    parts = re.split(r'(<script type="text/babel" data-presets="react">.*?</script>)', src, flags=re.S)
    for i in range(1, len(parts), 2):
        parts[i] = re.sub(r'\$\{([^{}`]+)\} (reps|days|weeks|times|sessions|nights|entries|minutes|sets)\b', fx, parts[i])
    src = ''.join(parts)
    print('r24: plurals guarded', n0[0])
    return src
