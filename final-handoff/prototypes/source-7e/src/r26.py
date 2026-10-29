# pass 7c: review r26 (on top of r25.late). Honesty: the period type is versioned with each rule.
def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, n, a[:120])
    return s.replace(a, b)

def late(src):
    # the period type travels with each rule version: cadOn (the type in force on a day), cadSpan (the days that type covers)
    src = rep(src, "const targetOn = (it, d) => { let t = it.targets[0]; for (const x of it.targets) if (x.from <= d) t = x; return t || { cmp: 'none', v: 0 }; };",
      "const targetOn = (it, d) => { let t = it.targets[0]; for (const x of it.targets) if (x.from <= d) t = x; return t || { cmp: 'none', v: 0 }; };\n"
      "/* r26 (honesty): each rule carries the period type it was set with (t.cad). A finished period keeps both its rule and its type;\n"
      "   a rule with no type of its own (before 7c) has the routine's, which is what it was judged by until then */\n"
      "const cadKey = c => c ? c.type + (c.type === 'everyN' ? ':' + c.n : '') : '';\n"
      "const cadOn = (it, d) => { const T = it.targets || []; if (!T.some(x => x.cad)) return it.cadence; let c = T.length && T[0].from > d ? T[0].cad : null; for (const x of T) if (x.from <= d) c = x.cad || null; return c || it.cadence; };\n"
      "const cadSpan = (it, d) => { const T = it.targets || []; if (!T.some(x => x.cad)) return [-1e9, 1e9]; let lo = -1e9, hi = 1e9, pk = null;\n"
      "  for (const x of T) { const k = cadKey(x.cad || it.cadence); if (pk != null && k !== pk) { if (x.from <= d) lo = x.from; else { hi = x.from - 1; break; } } pk = k; } return [lo, hi]; };\n"
      "/* when a save changes the type, the rules it keeps are stamped with the type they had and the new rule with the new one */\n"
      "const stampCad = (old, patch) => { if (!old || !(patch.targets || patch.cadence)) return patch; const oc = old.cadence, nc = patch.cadence || oc; const OT = old.targets || [];\n"
      "  const T = (patch.targets || OT).map(t => t.cad ? t : { ...t, cad: OT.includes(t) ? oc : nc }); return { ...patch, targets: T }; };")
    src = rep(src, "function periodOf(it, d) {\n  const c = it.cadence;\n",
      "function periodOf(it, d) { const r = periodOfC(it, cadOn(it, d), d); const [lo, hi] = cadSpan(it, d); return [Math.max(r[0], lo), Math.min(r[1], hi)]; }\nfunction periodOfC(it, c, d) {\n")
    src = rep(src, "const periodWord = (it, a, b, today) => {\n  const c = it.cadence.type;", "const periodWord = (it, a, b, today) => {\n  const c = cadOn(it, a).type;")
    # migration: every rule in the built db carries a type (the routine's, where it had none)
    src = rep(src, "targets: it.targets.filter(t => t.from <= today || t.future), pauses:", "targets: it.targets.filter(t => t.from <= today || t.future).map(t => t.cad ? t : { ...t, cad: it.cadence }), pauses:")
    # saves stamp the types
    src = rep(src, "  const updateItem = (id, patch) => { if ((patch.targets || patch.cadence) && db.byId[id])", "  const updateItem = (id, patch) => { patch = stampCad(db.byId[id], patch); /* r26 */ if ((patch.targets || patch.cadence) && db.byId[id])")
    # where a save asks "the start of the period in progress under the new type", it asks without the old rules' types
    src = rep(src, "periodOf({ ...it, cadence: { type: pd } }, db.today)", "periodOf({ ...it, cadence: { type: pd }, targets: [] }, db.today)")
    src = rep(src, "periodOf({ src: { ...it.src, cadence } }, w.today)", "periodOf({ src: { ...it.src, cadence, targets: [] } }, w.today)")
    # polish: the How-often copy says today / this week, never "this day"
    src = rep(src, "`Counts from the start of this ${t.cad === 'everyN' ? 'window' : t.cad}. Before that it had no target, so nothing earlier counts against it.` : `From this ${t.cad === 'everyN' ? 'window' : t.cad} on. Past periods keep the rule they had.`",
      "`Counts from ${t.cad === 'day' ? 'today' : 'the start of this ' + (t.cad === 'everyN' ? 'window' : t.cad)}. Before that it had no target, so nothing earlier counts against it.` : `From ${t.cad === 'day' ? 'today' : 'this ' + (t.cad === 'everyN' ? 'window' : t.cad)} on. Past periods keep the rule and the period they had.`")
    # the toast tells the truth about a change of period type
    src = rep(src, "`${said}, starting ${pw === 'day' ? 'today' : 'this ' + pw}. Earlier ${pw}s keep the rule they had.`); });",
      "`${said}, starting ${pw === 'day' ? 'today' : 'this ' + pw}. ${it.src.cadence && cadKey(it.src.cadence) !== cadKey(cadence) ? 'Earlier periods keep the rule and the period they had.' : `Earlier ${pw}s keep the rule they had.`}`); });")
    # a change of period type starts today, never at the start of a week that already holds finished days:
    # those days stay day periods under their own rule, and the first week runs from today (cadSpan clips it)
    src = rep(src, "const pa = Math.min(w.today, Math.max(it.src.created || 0, periodOf({ src: { ...it.src, cadence, targets: [] } }, w.today)[0])); /* r24: from the start of the period in progress */",
      "const cadMoved = !!(it.src.cadence && it.src.cadence.type !== 'none' && cadKey(it.src.cadence) !== cadKey(cadence) && cadence.type !== 'none'); const pa = cadMoved ? w.today : Math.min(w.today, Math.max(it.src.created || 0, periodOf({ src: { ...it.src, cadence, targets: [] } }, w.today)[0])); /* r24: from the start of the period in progress; r26: a new period type from today */")
    src = rep(src, "'Earlier periods keep the rule and the period they had.'", "'Earlier periods keep the rule and the period they had.'")
    src = rep(src, "`${said}, starting ${pw === 'day' ? 'today' : 'this ' + pw}. ${it.src.cadence", "`${said}, starting ${pw === 'day' || cadMoved ? 'today' : 'this ' + pw}. ${it.src.cadence")
    src = rep(src, ": `From ${t.cad === 'day' ? 'today' : 'this ' + (t.cad === 'everyN' ? 'window' : t.cad)} on. Past periods keep the rule and the period they had.`}</p>",
      ": (it.src.cadence && it.src.cadence.type !== 'none' && (t.cad !== it.src.cadence.type || (t.cad === 'everyN' && t.n !== it.src.cadence.n))) ? `From today. The first ${t.cad === 'everyN' ? 'window' : t.cad} runs from today; finished periods keep the rule and the period they had.` : `From ${t.cad === 'day' ? 'today' : 'this ' + (t.cad === 'everyN' ? 'window' : t.cad)} on. Past periods keep the rule they had.`}</p>")
    # the item page's columns of light: each period names, labels and counts itself by the type it had
    src = rep(src, "r = state0(w, it, a, b); if (it.src) C.set(ck, r); } return r; };",
      "r = state0(w, it, a, b); if (it.src) { if (r.cad == null) r.cad = cadOn(it.src, a).type; C.set(ck, r); } } return r; }; /* r26: the period type it had */")
    src = rep(src, "function perLabel(it, P) { return `The last ${P.length} ${per(it)} as columns",
      "const perP = (it, P) => { const cs = [...new Set(P.map(p => p.cad || it.cad))]; return cs.length === 1 ? per({ cad: cs[0] }) : 'periods'; }; /* r26: mixed types read as periods */\nfunction perLabel(it, P) { return `The last ${P.length} ${perP(it, P)} as columns")
    src = rep(src, "return `Of the last ${fin.length === 1 ? 'finished ' + per(it).replace(/s$/, '') : `${fin.length} finished ${per(it)}`}:",
      "return `Of the last ${fin.length === 1 ? 'finished ' + perP(it, fin).replace(/s$/, '') : `${fin.length} finished ${perP(it, fin)}`}:")
    src = rep(src, "function perName(it, p) { if (it.cad === 'day') return D.day(p.a); if (it.cad === 'month')",
      "function perName(it, p) { const c = p.cad || it.cad; if (c === 'day') return D.day(p.a); if (c === 'month')")
    src = rep(src, "function pLabel(it, p, n, k) { if (it.cad === 'day') return p.open ? 'today' : D.DOW[D.dow(p.a)][0]; if (it.cad === 'month') return D.MON3[D.monthOf(p.a)]; if (it.cad === 'everyN')",
      "function pLabel(it, p, n, k) { const c = p.cad || it.cad; if (c === 'day') return p.open ? 'today' : D.DOW[D.dow(p.a)][0]; if (c === 'month') return D.MON3[D.monthOf(p.a)]; if (c === 'everyN')")
    return src
