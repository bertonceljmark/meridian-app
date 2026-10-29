# pass 7d: review r27 (on top of r26.late). Cadence, the rest of the way: every reading of the past takes each period's own
# rule version and type (Time > month Totals, the hero, the item page, the Growth note), and amounts keep their units.
def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, n, a[:140])
    return s.replace(a, b)

MONTH_TOTAL = r'''function monthTotal(w, it, m) {
  /* r27 #5a: the month is read period by period, each by its own rule version and type (cadOn / periodOf), never by the routine's
     current type; the figure keeps its unit whatever the type (43.36 L, 7 h 49 min, 17 times) */
  const a = Math.max(D.mStart(m), it.created), b = Math.min(D.mEnd(m), w.today); const v = E.val(w, it, a, b);
  const fig = () => it.measure === 'quantity' ? { f: M.amt(it, v.v), u: '' } : it.measure === 'duration' ? { f: D.dur(v.v), u: '' } : it.measure === 'reps' ? { f: String(v.v), u: 'done' } : it.measure === 'confirmation' || it.measure === 'count' ? { f: String(v.n), u: 'times' } : { f: String(v.v), u: 'times' };
  const paused = () => E.status(w, it) === 'paused';
  if (!it.src) return { f: '', u: '', s: 'Nothing recorded yet' };
  // the periods that belong to this month: a period belongs to the month its fourth day (or its last, if shorter) falls in
  const P = []; let d = D.mStart(m) - 6; for (let guard = 0; guard < 80 && d <= D.mEnd(m); guard++) { const [pa, pb] = periodOf(it.src, d); if (!(pb >= pa)) break;
    if (D.monthOf(Math.min(pa + 3, pb)) === m && pb >= it.created && pa <= w.today) { const s = E.state(w, it, pa, pb); P.push({ ...s, pa, pb, c: cadOn(it.src, pa).type }); } d = pb + 1; }
  const judged = P.filter(p => p.tg && p.tg.cmp !== 'none' && p.tg.cmp !== 'at_most' && ['day', 'week', 'month'].includes(p.c));
  if (!judged.length) { if (!v.n) return { f: '', u: '', s: 'Nothing recorded yet' }; return { ...fig(), s: P.some(p => p.c === 'everyN') ? E.cadText(it) : 'No target, it grows' }; }
  const fin = judged.filter(p => p.pb < w.today && !['aside', 'paused', 'pre'].includes(p.st)); const met = fin.filter(p => p.st === 'met').length;
  const types = [...new Set(fin.map(p => p.c))]; const word = types.length === 1 ? types[0] : 'period';
  const open = judged.find(p => p.pb >= w.today);
  let s;
  if (!fin.length) s = open ? (open.st === 'met' ? 'At its aim' : open.n ? `${vtxt(it, open.v)} of ${aimTxt(it, open.tg)} so far` : 'Not yet') : paused() ? 'Paused' : `No finished ${open ? open.c : 'period'} yet`;
  else if (fin.length === 1 && word === 'month') s = fin[0].st === 'met' ? 'At its aim' : `${vtxt(it, fin[0].v)} of ${aimTxt(it, fin[0].tg)}`;
  else s = met ? `At its aim ${word === 'day' ? 'on' : 'in'} ${met} of ${plural(fin.length, word)}` : 'Not at its aim yet';
  if (!v.n && !v.v) return { f: '', u: '', s: fin.length ? 'Nothing recorded yet' : s };
  return { ...fig(), s }; }
'''

def late(src):
    # a. Time > month Totals
    i = src.index('function monthTotal(w, it, m) {'); j = src.index('function highlights(w, m) {')
    src = src[:i] + MONTH_TOTAL + src[j:]
    # the month's drawing follows the month's periods: a month that holds a change of type draws a tick a day
    src = rep(src, "const t = monthTotal(w, it, m); const draw = it.cad === 'week' ? weekBars(w, it, m) : it.cad === 'month' ? staff(w, it, D.mStart(m), D.mEnd(m), true) : comb(w, it, m);",
      "const t = monthTotal(w, it, m); const mixed = it.src && cadSpan(it.src, D.mStart(m))[1] < D.mEnd(m); /* r27: a change of type inside the month */ const draw = mixed ? comb(w, it, m) : it.cad === 'week' ? weekBars(w, it, m) : it.cad === 'month' ? staff(w, it, D.mStart(m), D.mEnd(m), true) : comb(w, it, m);")
    # comb: each day is coloured by the period it belongs to, and the aim line is a daily one only on daily days
    src = rep(src, "const st = E.state(w, it, d, d); const v = E.val(w, it, d, d); V.push(",
      "const st = E.state(w, it, ...(it.src ? periodOf(it.src, d) : [d, d])); /* r27: the day's own period */ const v = E.val(w, it, d, d); V.push(")
    # the Time target names its unit ("580 ml of 2 L so far"), and a period's aim is that period's rule
    src = rep(src, "const aimTxt = it => it.tg.cmp === 'range' ? `${it.tg.v}–${it.tg.hi}` : it.measure === 'duration' ? D.dur(it.tg.v) : String(it.tg.v);",
      "const aimTxt = (it, tg = it.tg) => tg.cmp === 'range' ? `${vtxt(it, tg.v)}–${vtxt(it, tg.hi)}` : vtxt(it, tg.v); /* r27: with its unit, and the period's own rule */")
    src = rep(src, "const st = E.state(w, it, a, b); const lo = it.tg.v || 1, hi = it.tg.cmp === 'range' ? it.tg.hi : lo;",
      "const st = E.state(w, it, a, b); const tg0 = st.tg || it.tg; const lo = tg0.v || 1, hi = tg0.cmp === 'range' ? tg0.hi : lo; /* r27: the period's own rule */")
    src = rep(src, "`${vtxt(it, st.v)} of ${aimTxt(it)}${st.open ? ' so far' : ''}`;", "`${vtxt(it, st.v)} of ${aimTxt(it, tg0)}${st.open ? ' so far' : ''}`;")
    # b. the hero and every "where it stands" line: a period cut short by a change of type says so ("since 27 Oct"), never "in Oct"
    src = rep(src, "  const p = E.state(w, it, ...E.cur(w, it)); const per = { day: 'today', week: 'this week', month: `in ${MON3_[D.monthOf(w.today)]}`, everyN: 'this window', none: 'this week' }[it.cad];",
      "  const p = E.state(w, it, ...E.cur(w, it)); const cut = it.src && it.cad !== 'day' && it.cad !== 'none' && periodOfC(it.src, cadOn(it.src, w.today), w.today)[0] < p.a; /* r27 #5b: the first period after a change of type */\n"
      "  const per = cut ? `since ${p.a === w.today ? 'today' : D.day(p.a, { noDow: true })}` : { day: 'today', week: 'this week', month: `in ${MON3_[D.monthOf(w.today)]}`, everyN: 'this window', none: 'this week' }[it.cad];")
    src = rep(src, "  if (it.measure === 'quantity') return p.n ? `${M.amt(it, p.v)} of ${M.amt(it, p.tg.v)}` : 'None logged today';",
      "  if (it.measure === 'quantity') return p.n ? `${M.amt(it, p.v)} of ${M.amt(it, p.tg.v)}${it.cad === 'day' ? '' : ' ' + per}` : `None logged ${per}`;")
    src = rep(src, "  if (it.measure === 'reps') return p.n ? `${p.v} of ${p.tg.v}` : 'None logged today';",
      "  if (it.measure === 'reps') return p.n ? `${p.v} of ${p.tg.v}${it.cad === 'day' ? '' : ' ' + per}` : `None logged ${per}`;")
    # the item page names a cut-short period by its dates ("27–31 Oct"), not "October"
    src = rep(src, "function perName(it, p) { const c = p.cad || it.cad; if (c === 'day') return D.day(p.a); if (c === 'month') return D.MONTHS[D.monthOf(p.a)];",
      "function perName(it, p) { const c = p.cad || it.cad; if (c === 'day') return D.day(p.a); if (c === 'month' && p.a === D.mStart(D.monthOf(p.a)) && p.b === D.mEnd(D.monthOf(p.a))) return D.MONTHS[D.monthOf(p.a)]; /* r27: a cut-short month reads by its dates */")
    src = rep(src, "if (c === 'month') return D.MON3[D.monthOf(p.a)]; if (c === 'everyN')",
      "if (c === 'month') return p.a === D.mStart(D.monthOf(p.a)) ? D.MON3[D.monthOf(p.a)] : D.dom(p.a) + '–'; if (c === 'everyN')")
    # the "short first period" note covers a change of type as well as a late start
    src = rep(src, "const [a0] = E.cur(w, it); if (st === 'active' && ['week', 'month', 'everyN'].includes(it.cad) && a0 < it.created && it.created <= w.today) h += `<p class=\"note\">A short first ${it.cad === 'everyN' ? 'window' : it.cad}: it started on ${D.day(it.created)}, so this one counts from then.</p>`;",
      "const [a0, b0] = E.cur(w, it); if (st === 'active' && ['week', 'month', 'everyN'].includes(it.cad) && a0 < it.created && it.created <= w.today) h += `<p class=\"note\">A short first ${it.cad === 'everyN' ? 'window' : it.cad}: it started on ${D.day(it.created)}, so this one counts from then.</p>`;\n"
      "    else if (st === 'active' && it.src && ['week', 'month'].includes(it.cad) && periodOfC(it.src, cadOn(it.src, w.today), w.today)[0] < a0) h += `<p class=\"note\">A short first ${it.cad}, ${D.range(a0, b0)}: the ${it.cad} started counting when you changed how often, so it runs from then. Earlier periods keep the rule and the period they had.</p>`; /* r27 #5b */")
    # c. the Growth note counts each finished period by its own type
    src = rep(src, "${P.length >= 3 && it.cad !== 'day' ? `<p class=\"note\" style=\"margin-top:var(--sp-2)\">Logged at least once in ${withIt} of its ${plural(P.length, 'finished ' + per(it).replace(/s$/, ''), 'finished ' + per(it))}.",
      "${P.length >= 3 && P.some(p => (p.cad || it.cad) !== 'day') ? `<p class=\"note\" style=\"margin-top:var(--sp-2)\">Logged at least once in ${withIt} of its ${plural(P.length, 'finished ' + perP(it, P).replace(/s$/, ''), 'finished ' + perP(it, P))}.")
    # This week: a daily routine counts only the days that are day periods (a week cut short by a change is not a day)
    src = rep(src, "for (let d = Math.max(ws, it.created); d <= w.today; d++) { const p = E.state(w, it, d, d); if (['aside', 'paused'].includes(p.st)) continue; t++; if (p.st === 'met') m++; }",
      "for (let d = Math.max(ws, it.created); d <= w.today; d++) { if (it.src && cadOn(it.src, d).type !== 'day') continue; /* r27 */ const p = E.state(w, it, d, d); if (['aside', 'paused'].includes(p.st)) continue; t++; if (p.st === 'met') m++; }")
    # polish: the last off-scale spacing. 28 (on the 4 px grid but off the scale) goes to 32 (--sp-6) in padding, margin and gap,
    # in the CSS and in the JSX styles; 48, 56 and 64 stay (multiples of 8 past the scale's top, used as deliberate large insets
    # and empty-state padding); min-heights are sizes, not spacing, and 2 px hairlines are kept
    import re as _re
    global SNAP28
    SNAP28 = 0
    def css_decl(m):
        global SNAP28
        v = m.group(2); n = len(_re.findall(r'(?<![\d.-])28px', v)); SNAP28 += n
        return m.group(1) + _re.sub(r'(?<![\d.-])28px', 'var(--sp-6)', v)
    src = _re.sub(r'((?:padding|margin|gap|row-gap|column-gap)(?:-(?:top|bottom|left|right|inline|block)(?:-(?:start|end))?)?\s*:\s*)([^;}"\'`]*)', css_decl, src)
    def jsx_num(m):
        global SNAP28
        SNAP28 += 1
        return m.group(1) + '32'
    src = _re.sub(r'(\b(?:padding|margin|gap|rowGap|columnGap)(?:Top|Bottom|Left|Right|Inline|Block)?: )28(?=[,} ])', jsx_num, src)
    print('r27: 28 px spacing snapped to 32:', SNAP28)
    return src
