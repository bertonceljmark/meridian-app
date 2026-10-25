import sys, re
def rep(s, a, b, n=1):
    c = s.count(a)
    if c != n: sys.exit(f"r25 patch count {c} != {n}: {a[:90]!r}")
    return s.replace(a, b)

def apply(src):
    # 6: You > feel field: the tap handler looked for the reading under M.top().el, which is null on a tab root; look in the field's own root
    src = rep(src, "const rd = M.top().el.querySelector('#fread');", "const rd = host.getRootNode().querySelector('#fread');")
    # polish: sheets trap focus (Tab and Shift+Tab stay inside the top sheet, through v3's shadow roots), and the grabber
    # is a named button: Enter, Space or a plain tap closes, a drag still drags
    src = rep(src, "  useEffect(() => { const k = e => { if (e.key === 'Escape') close(); }; window.addEventListener('keydown', k); return () => window.removeEventListener('keydown', k); }, [close]);\n  // follows the finger",
      "  useEffect(() => { const k = e => { if (e.key === 'Escape') close(); }; window.addEventListener('keydown', k); return () => window.removeEventListener('keydown', k); }, [close]);\n"
      "  useEffect(() => { const el = ref.current; if (!el) return; const SEL = 'button:not([disabled]), [href], input:not([disabled]), textarea, select, [tabindex]:not([tabindex=\"-1\"]), summary';\n"
      "    const list = () => { const o = []; const walk = r => r.querySelectorAll('*').forEach(x => { if (x.matches(SEL) && x.getClientRects().length && getComputedStyle(x).visibility !== 'hidden') o.push(x); if (x.shadowRoot) walk(x.shadowRoot); }); walk(el); return o; };\n"
      "    const deepActive = () => { let a = document.activeElement; while (a && a.shadowRoot && a.shadowRoot.activeElement) a = a.shadowRoot.activeElement; return a; };\n"
      "    const trap = e => { if (e.key !== 'Tab') return; const all = [...document.querySelectorAll('.sheet:not(.out)')]; if (all[all.length - 1] !== el) return; const L = list(); if (!L.length) return; const a = deepActive(); const i = L.indexOf(a);\n"
      "      if (i < 0 || (e.shiftKey && i === 0) || (!e.shiftKey && i === L.length - 1)) { e.preventDefault(); (e.shiftKey ? (i < 0 ? L[L.length - 1] : L[L.length - 1]) : L[0]).focus(); } };\n"
      "    window.addEventListener('keydown', trap, true); return () => window.removeEventListener('keydown', trap, true); }, []); /* r25: focus stays in the sheet */\n"
      "  const moved = useRef(false);\n  // follows the finger")
    src = rep(src, "    if (d.dy > 110 || (v > .5 && d.dy > 12)) { leave();", "    moved.current = Math.abs(d.dy - d.base) > 4; if (d.dy > 110 || (v > .5 && d.dy > 12)) { leave();")
    src = rep(src, "      <div className=\"grabber\" onPointerDown={down} onPointerMove={mv} onPointerUp={up} onPointerCancel={up}><i /></div>",
      "      <div className=\"grabber\" role=\"button\" tabIndex={0} aria-label=\"Close, or drag down\" onClick={() => { if (!moved.current) close(); moved.current = false; }} onKeyDown={e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); close(); } }} onPointerDown={down} onPointerMove={mv} onPointerUp={up} onPointerCancel={up}><i /></div>")
    # polish: one word for the dial, "ring"
    src = rep(src, "Log anything below and it gathers on the arc above.", "Log anything below and it gathers on the ring above.")
    # polish: a number and its unit agree everywhere ("+2 cups", "100 cups"), and reps are reps, not the routine's name
    src = rep(src, "const unitN = (u, n) => n === 1 ? ({ litres: 'litre', hours: 'hour', sessions: 'session', times: 'time' }[u] || u.replace(/s$/, '')) : u;",
      "const unitN = (u, n) => typeof unitSing === 'function' ? (n === 1 ? unitSing(u) : unitPl(u)) : n === 1 ? ({ litres: 'litre', hours: 'hour', sessions: 'session', times: 'time' }[u] || u.replace(/s$/, '')) : u; /* r25: the app's own rule */")
    src = rep(src, "Your intention is at most ${it.tg.v}${it.unit ? ' ' + it.unit : ''}", "Your intention is at most ${it.tg.v}${it.unit ? ' ' + unitN(it.unit, it.tg.v) : ''}")
    src = rep(src, "(it.unit ? `${p.v} ${it.unit}` : plural(p.v, 'time'))", "(it.unit ? `${p.v} ${unitN(it.unit, p.v)}` : plural(p.v, 'time'))")
    src = rep(src, "`Log ${it.presets ? it.presets[1] : 250} ${it.unit}`", "`Log ${it.presets ? it.presets[1] : 250} ${unitN(it.unit, it.presets ? it.presets[1] : 250)}`")
    src = rep(src, "${n ? `${n}${it.unit ? ' ' + it.unit : ''} this week`", "${n ? `${n}${it.unit ? ' ' + unitN(it.unit, n) : ''} this week`")
    src = rep(src, "`+${v} ${it.unit}`", "`+${v} ${unitN(it.unit, v)}`", 2)
    src = rep(src, "`${v} ${it.unit || ''}`.trim()", "`${v} ${it.unit ? unitN(it.unit, v) : ''}`.trim()")
    src = rep(src, "return `+${S.lastAmount(it)}${it.unit === 'ml' ? '' : ' ' + (it.unit || '')}`;", "return `+${S.lastAmount(it)}${it.unit === 'ml' ? '' : ' ' + unitN(it.unit || '', S.lastAmount(it))}`;")
    src = rep(src, "const unit = it.measure === 'quantity' ? (it.unit === 'ml' ? 'litres' : it.unit) : it.measure === 'duration' ? 'hours' : it.measure === 'reps' ? it.name.toLowerCase() : it.measure === 'session' ? 'sessions' : 'times';",
      "const unit = it.measure === 'quantity' ? (it.unit === 'ml' ? 'litres' : unitPl(it.unit || '')) : it.measure === 'duration' ? 'hours' : it.measure === 'reps' ? 'reps' : it.measure === 'session' ? 'sessions' : 'times';")
    # 5: the period in progress is the period of the chosen type. v3's periodOf is E.prev over fakeSrc, which only reads a
    # cadence from .src; handing it a bare item made every save fall back to "none" (a week).
    src = rep(src, "periodOf({ ...it.src, cadence }, w.today)[0]", "periodOf({ src: { ...it.src, cadence } }, w.today)[0]")
    src = rep(src, "`${said}, starting this ${pw}`", "`${said}, starting ${pw === 'day' ? 'today' : 'this ' + pw}`")
    src = rep(src, "`${said}, starting this ${pw}. Earlier ${pw}s keep the rule they had.`", "`${said}, starting ${pw === 'day' ? 'today' : 'this ' + pw}. Earlier ${pw}s keep the rule they had.`")
    src = rep(src, "From this ${t.cad} on; past periods keep the rule they had.", "From ${t.cad === 'day' ? 'today' : 'this ' + (t.cad === 'everyN' ? 'window' : t.cad)} on; past periods keep the rule they had.")
    # the app's own target sheet: never defaults to "next"; the period in progress takes the new rule
    src = rep(src, "const [when, setWhen] = useState('next');", "const [when, setWhen] = useState('now'); /* r25: apply to the period in progress by default */")
    src = rep(src, "S.toast({ title: when === 'now' ? `${preview} from this ${it.cadence.type === 'day' ? 'day' : it.cadence.type}` : `${preview}, from ${fmtDay(from)}`, sub: 'Past periods keep the target they had'",
      "S.toast({ title: when === 'now' || noCad ? `${preview}, starting ${it2.cadence.type === 'day' ? 'today' : 'this ' + (it2.cadence.type === 'everyN' ? 'window' : it2.cadence.type)}` : `${preview}, from ${fmtDay(from)}`, sub: 'Earlier periods keep the target they had'")
    src = rep(src, "`Starts today. Until now it had no target, so nothing earlier counts against it.`", "`Counts from ${pd === 'day' ? 'today' : 'the start of this ' + pd}. Before that it had no target, so nothing earlier counts against it.`")
    return src

def late(src):
    src = v3hue(src)
    # 9: the old light-DOM sheets keep the 16 px gutter their headers use
    src = src.replace("padding: '0 20px'", "padding: '0 var(--gut)'")
    src = rep(src, ".sheet [style*=\"padding: 0 20px\"] .list, .sheet [style*=\"padding: 0px 20px\"] .list {", ".sheet [style*=\"padding: 0 20px\"] .list, .sheet [style*=\"padding: 0px 20px\"] .list, .sheet [style*=\"padding: 0 var(--gut)\"] .list {")
    src = rep(src, ".sheet .laterwrap { padding: 0 20px; }", ".sheet .laterwrap { padding: 0 var(--gut); }")
    src = rep(src, "padding: '22px 20px 0'", "padding: '24px var(--gut) 0'")
    src = rep(src, "padding: '4px 20px 18px'", "padding: '4px var(--gut) 16px'")
    src = spacing(src)
    # 10: one deterministic hue per routine (neuAssign, in neu.jsx), set before the items are mapped
    src = rep(src, "  const visible = items.filter(it => it.created <= today", "  if (typeof neuAssign === 'function') neuAssign(items); /* r25: one hue per routine, neighbours distinct */\n  const visible = items.filter(it => it.created <= today")
    src = rep(src, "const items0 = t3SampleItems(s).map(", "const items0 = (() => { const L0 = t3SampleItems(s); if (typeof neuAssign === 'function') neuAssign(L0); return L0; })().map(")
    # 10: Today's own colour: the strip's kicks (sleep in night light, a workout in moss, an observation in its routine's),
    # Later's names, the suggestion's name and the Settled dots all carry their routine's light
    src = rep(src, "  return open ? <button className={cls} onClick={open} aria-label={label} data-tcard={m.kind} data-tcard-id={m.id}>{X}{body}</button> : <div className={cls} data-tcard={m.kind} data-tcard-id={m.id}>{X}{body}</div>;",
      "  const H = m.kind === 'night' || m.kind === 'nightmiss' ? 278 : m.kind === 'fresh' ? 138 : m.kind === 'pattern' && m.p && m.p.to && m.p.to.hue != null && !m.p.to.neutral ? (typeof neuHue === 'function' ? neuHue(m.p.to) : m.p.to.hue) : null; /* r25 #10 */\n"
      "  const cls2 = cx(cls, H != null && 'hue'), st2 = H != null ? { '--h': H } : undefined;\n"
      "  return open ? <button className={cls2} style={st2} onClick={open} aria-label={label} data-tcard={m.kind} data-tcard-id={m.id}>{X}{body}</button> : <div className={cls2} style={st2} data-tcard={m.kind} data-tcard-id={m.id}>{X}{body}</div>;")
    src = rep(src, "  return <span className=\"ztok\" data-later-item={it.id} data-row={it.id}>", "  return <span className={cx('ztok', hueCls(it))} style={hueStyle(it)} data-later-item={it.id} data-row={it.id}>")
    src = rep(src, "      return <div key={c.id} className=\"zsug\" data-suggestion={c.id} data-suggestion-kind={c.kind}>", "      return <div key={c.id} className={cx('zsug', c.kind === 'routine' && it ? hueCls(it) : null)} style={c.kind === 'routine' && it ? hueStyle(it) : undefined} data-suggestion={c.id} data-suggestion-kind={c.kind}>")
    src = rep(src, "{settled.map(x => <button key={x.it.id} className={cx(popped === x.it.id && 'pop')} ", "{settled.map(x => <button key={x.it.id} className={cx(popped === x.it.id && 'pop', hueCls(x.it))} style={hueStyle(x.it)} ")
    # 10: Today's neighbours never share a light (neuRepair, in neu.jsx), before the rows and the dial draw
    src = rep(src, "if (li > 0) nowRows = [nowRows[li], ...nowRows.filter((_, i) => i !== li)]; } /* pass 6b (r17 B1): the live row leads and is never folded */",
      "if (li > 0) nowRows = [nowRows[li], ...nowRows.filter((_, i) => i !== li)]; } /* pass 6b (r17 B1): the live row leads and is never folded */\n  if (typeof neuRepair === 'function') { neuRepair(nowRows.filter(r => r.k === 'r').map(r => r.x.it)); }")
    src = rep(src, "  const laterSorted = useMemo(() => [...later].filter(x => !hold[x.it.id]).sort((a, b) => ((a.ev.b ?? 9999) - (b.ev.b ?? 9999)) || (b.score - a.score)), [later, hold]);",
      "  const laterSorted = useMemo(() => [...later].filter(x => !hold[x.it.id]).sort((a, b) => ((a.ev.b ?? 9999) - (b.ev.b ?? 9999)) || (b.score - a.score)), [later, hold]);\n  if (typeof neuRepair === 'function') neuRepair(settled.map(x => x.it));\n  if (typeof neuRepair === 'function') neuRepair(laterSorted.map(x => ({ x, w: model.calm ? ['any', 9999] : laterWhen(x) })).sort((a, b) => (WHEN_O.indexOf(a.w[0]) - WHEN_O.indexOf(b.w[0])) || (a.w[1] - b.w[1])).map(o => o.x.it));")
    # 5: the target sheet's choice leads with the period in progress and says "today" for a day
    src = rep(src, "<Seg options={[{ v: 'next', l: `Next ${it.cadence.type === 'day' ? 'day' : it.cadence.type === 'everyN' ? 'window' : it.cadence.type}` }, { v: 'now', l: `This ${it.cadence.type === 'day' ? 'day' : it.cadence.type === 'everyN' ? 'window' : it.cadence.type}` }]} value={when} onChange={setWhen} />",
      "<Seg options={it.cadence.type === 'day' ? [{ v: 'now', l: 'Today' }, { v: 'next', l: 'Tomorrow' }] : [{ v: 'now', l: `This ${it.cadence.type === 'everyN' ? 'window' : it.cadence.type}` }, { v: 'next', l: `Next ${it.cadence.type === 'everyN' ? 'window' : it.cadence.type}` }]} value={when} onChange={setWhen} />")
    src = rep(src, "This ${it.cadence.type} stays as it is.` : `Applies to this ${it.cadence.type} too. Earlier periods keep their own target.`}",
      "${it.cadence.type === 'day' ? 'Today' : `This ${it.cadence.type === 'everyN' ? 'window' : it.cadence.type}`} stays as it is.` : `${it.cadence.type === 'day' ? 'Applies to today too' : `Applies to this ${it.cadence.type === 'everyN' ? 'window' : it.cadence.type} too`}. Earlier periods keep their own target.`}")
    # 3: each Watch key names its routine for VoiceOver, as the widget's keys do
    src = rep(src, "data-act=\"${isLive(it) ? 'widstop' : 'widlog'}\" data-id=\"${it.id}\">${isLive(it) ? 'Stop' : it.measure === 'session' ? 'Start' : 'Log'}</button>",
      "data-act=\"${isLive(it) ? 'widstop' : 'widlog'}\" data-id=\"${it.id}\" aria-label=\"${isLive(it) ? 'Stop' : it.measure === 'session' ? 'Start' : 'Log'}, ${esc(nm(it))}\">${isLive(it) ? 'Stop' : it.measure === 'session' ? 'Start' : 'Log'}</button>")
    # r26 #10: the Routines list carries each routine's light (its glyph and a lead light); "Settled" in that light, not in sun
    src = rep(src, "return `<button class=\"tk${s ? ' met' : ''}\" data-act=\"open\" data-id=\"${it.id}\"><span class=\"tn\">",
      "return `<button class=\"tk${s ? ' met' : ''}\" data-act=\"open\" data-id=\"${it.id}\"${typeof neuRH === 'function' ? neuRH(it) : ''}><span class=\"tn\">")
    # r26 polish: the strip fits the card in view (NeuStripBox, in neu.jsx)
    src = rep(src, "return <div className=\"zstrip\" role=\"region\" aria-label=\"Since last time\" data-today-cards={list.length}>{list.map((m, i) => <T3Panel key={m.id} m={m} solo={list.length === 1} last={i === list.length - 1} />)}</div>;",
      "return <NeuStripBox className=\"zstrip\" role=\"region\" label=\"Since last time\" n={list.length}>{list.map((m, i) => <T3Panel key={m.id} m={m} solo={list.length === 1} last={i === list.length - 1} />)}</NeuStripBox>;")
    # r26 polish: a number and its unit keep their space on the widget key ("+250 ml", never "+250ml")
    src = rep(src, "'+' + M.amt(it, (it.presets || [250])[Math.min(1, (it.presets || [250]).length - 1)]).replace(/\\s/g, '')", "'+' + M.amt(it, (it.presets || [250])[Math.min(1, (it.presets || [250]).length - 1)]).replace(/\\s/g, '\\u00a0')")
    # 8: actions leave the sentence and become keys (44 pt); links that only navigate stay inline (the inline exception)
    src = rep(src, "${ok ? '' : `<button class=\"b\" data-act=\"confirmwk\" data-id=\"${it.id}\" data-k=\"${lw}\">That’s everything</button>`}</p></div>`; }",
      "</p>${ok ? '' : `<div class=\"gos\" style=\"margin-top:4px\"><button class=\"go\" data-act=\"confirmwk\" data-id=\"${it.id}\" data-k=\"${lw}\">That’s everything<span class=\"ar\" aria-hidden=\"true\">→</span></button></div>`}</div>`; }")
    src = rep(src, ". <button class=\"b\" data-act=\"hold\">Hold something</button>, or give it a date.${done.length ? ` Done lately: ${done.map(x => `${esc(x.title)}, ${D.rel(x.done, w.today)}`).join('; ')}.` : ''}</p></div>`; }",
      ".${done.length ? ` Done lately: ${done.map(x => `${esc(x.title)}, ${D.rel(x.done, w.today)}`).join('; ')}.` : ''}</p><div class=\"gos\" style=\"margin-top:4px\"><button class=\"go\" data-act=\"hold\">Hold something, or give it a date<span class=\"ar\" aria-hidden=\"true\">→</span></button></div></div>`; }")
    return src

def v3hue(src):
    # 10: the year and the month in each routine's light: a day's line is a stack of the routines touched that day,
    # each in its own light; a month day carries a small row of its routines' lights under its point
    src = rep(src, "    out.push({ d, h, known, ctx: c ? c.type : null, n: dd.n });", "    out.push({ d, h, known, ctx: c ? c.type : null, n: dd.n, ids: f ? (dd.items.has(f.id) ? [f.id] : []) : [...dd.items] });")
    src = rep(src, "  const L = M.light(host, o); host._L = L;",
      "  const L = M.light(host, o); host._L = L;\n"
      "  { const old = host.querySelector('.yhue'); if (old) old.remove(); const cv = document.createElement('canvas'); const dpr = Math.min(3, window.devicePixelRatio || 1); cv.className = 'yhue'; cv.setAttribute('aria-hidden', 'true'); cv.width = Math.round(W * dpr); cv.height = Math.round(HERO_H * dpr); cv.style.cssText = `position:absolute;left:0;top:0;width:${W}px;height:${HERO_H}px;pointer-events:none`;\n"
      "    const cx = cv.getContext('2d'); cx.scale(dpr, dpr); const ord = it => w.items ? w.items.indexOf(it) : 0; /* r25 #10: each line a stack of its routines' lights */\n"
      "    days.forEach(x => { if (x.fut || x.pre || !(x.h > 0) || !x.ids || !x.ids.length || x.ctx === 'sick') return; const X = PAD + (x.d + .5) * dw; const sel = x.d >= sa && x.d <= sb ? .95 : .5; const its = x.ids.map(id => w.byId[id]).filter(Boolean).sort((a, b) => ord(a) - ord(b)); const hgt = HT * x.h, seg = hgt / Math.max(1, its.length); let y = HZ;\n"
      "      its.forEach(it => { const s0 = it.src || it; const hh = s0.hue != null && !s0.neutral ? neuHue(s0) : null; cx.fillStyle = hh == null ? `rgba(232,239,248,${.6 * sel})` : `oklch(.76 .14 ${hh} / ${sel})`; cx.fillRect(X - Math.max(.5, dw * .34), y - seg, Math.max(1, dw * .68), seg); y -= seg; }); });\n"
      "    host.appendChild(cv); }")
    src = rep(src, "aria-label=\"${D.day(p.d, { long: true })}${p.x.fut ? ', still ahead' : p.x.known ? '' : ', nothing recorded'}\"><span>${D.dom(p.d)}</span></button>`).join(''));\n}",
      "aria-label=\"${D.day(p.d, { long: true })}${p.x.fut ? ', still ahead' : p.x.known ? '' : ', nothing recorded'}\"><span>${D.dom(p.d)}</span></button>`).join(''));\n"
      "  /* r25 #10: under each day's point, the lights of the routines done that day (up to five) */\n"
      "  host.insertAdjacentHTML('beforeend', pts.map(p => { const ids = (p.x.ids || []).map(id => w.byId[id]).filter(it => it && (it.src || it).hue != null && !(it.src || it).neutral); if (!ids.length) return ''; const n = Math.min(5, ids.length), gap = 5;\n"
      "    return `<span class=\"cdh\" aria-hidden=\"true\" style=\"left:${(p.cx - (n * gap - 2) / 2).toFixed(1)}px;top:${(p.cy + 8).toFixed(1)}px\">${ids.slice(0, n).map(it => `<i style=\"background:oklch(.76 .14 ${neuHue(it.src || it)})\"></i>`).join('')}</span>`; }).join(''));\n}")
    # 10: the Routines loom draws each thread in its routine's light: the colour rides in the free 32nd cell of its row
    src = rep(src, "rows.push([n ? Math.min(1, .3 + n * .14) : 0, settledHere ? 1 : 0, 0, Math.exp(-(w.today - d) / 2.5)]); } for (let k = LOOM_DAYS; k < 32; k++) rows.push([0, 0, 0, 0]); });",
      "rows.push([n ? Math.min(1, .3 + n * .14) : 0, settledHere ? 1 : 0, 0, Math.exp(-(w.today - d) / 2.5)]); } for (let k = LOOM_DAYS; k < 31; k++) rows.push([0, 0, 0, 0]); const s0 = it.src || it; const hh = s0.hue != null && !s0.neutral && typeof neuRGB === 'function' ? neuRGB(neuHue(s0)) : null; rows.push(hh ? [hh[0], hh[1], hh[2], 1] : [0, 0, 0, 0]); });")
    src = rep(src, "      vec3 cl=mix(CREAM,mix(CREAM,WARM*1.3,.75),warm);", "      vec4 rcd=dat(31.,row); vec3 RC=rcd.a>.5?rcd.rgb:CREAM; vec3 cl=mix(RC,min(RC*1.25+.06,vec3(1.2)),warm);")
    src = rep(src, "            ctx.fillStyle = `rgba(${255},${Math.round(230 - 90 * warm)},${Math.round(199 - 140 * warm)},.92)`;",
      "            { const s0 = it.src || it; const hh = s0.hue != null && !s0.neutral && typeof neuRGB === 'function' ? neuRGB(neuHue(s0)).map(v => Math.round(v * 255)) : null; ctx.fillStyle = hh ? `rgba(${hh.join(',')},.92)` : `rgba(${255},${Math.round(230 - 90 * warm)},${Math.round(199 - 140 * warm)},.92)`; }")
    # 10: the v3 ledgers carry their routine's hue (neuRH, in neu.jsx)
    src = rep(src, "  return `<div class=\"sf ${cls}\"><div class=\"sl\">${M.glyph(it.glyph, 17)}<b>${esc(it.short)}</b><span>${esc(say)}</span></div>${tr}</div>`; }",
                   "  return `<div class=\"sf ${cls}\"${neuRH(it)}><div class=\"sl\">${M.glyph(it.glyph, 17)}<b>${esc(it.short)}</b><span>${esc(say)}</span></div>${tr}</div>`; }")
    src = rep(src, "  if (bare) return `<span class=\"sfb ${cls}\">${tr}</span>`;", "  if (bare) return `<span class=\"sfb ${cls}\"${neuRH(it)}>${tr}</span>`;")
    src = rep(src, "  return `<div class=\"sf\"><div class=\"sl\">${M.glyph(it.glyph, 17)}<b>${esc(it.short)}</b><span>${!fin ?", "  return `<div class=\"sf\"${neuRH(it)}><div class=\"sl\">${M.glyph(it.glyph, 17)}<b>${esc(it.short)}</b><span>${!fin ?")
    src = rep(src, "  return `<span class=\"comb${aim ? ' aim' : ''}\">${V.map(", "  return `<span class=\"comb${aim ? ' aim' : ''}\"${neuRH(it)}>${V.map(")
    src = rep(src, "  return `<span class=\"wkb\">${out.join('')}</span>`; }", "  return `<span class=\"wkb\"${neuRH(it)}>${out.join('')}</span>`; }")
    src = rep(src, "return `<button class=\"cb\" data-act=\"filterTo\" data-id=\"${it.id}\">", "return `<button class=\"cb\" data-act=\"filterTo\" data-id=\"${it.id}\"${neuRH(it)}>")
    return src

# ---- 9: one spacing scale. Tokens --sp-1..--sp-6 = 4/8/12/16/24/32 (on :root); every padding, margin and gap in the app
# snaps to the 4 px grid (ties up), larger values to 8; negative offsets (centring, overlaps) and hairlines (<= 2) are kept
import math
def snapv(v):
    if v <= 2: return v
    if v <= 32: q = math.floor(v / 4 + .5) * 4
    else: q = math.floor(v / 8 + .5) * 8
    return q
def _num(x):
    v = float(x); return int(v) if v == int(v) else v
SP_TOK = {4: 'var(--sp-1)', 8: 'var(--sp-2)', 12: 'var(--sp-3)', 16: 'var(--sp-4)', 24: 'var(--sp-5)', 32: 'var(--sp-6)'}
TOK_N = [0]
def snap_vals(val, tok=False):
    def f(m):
        sign, num = m.group(1), m.group(2)
        if sign == '-': return m.group(0)
        v = float(num); q = snapv(v)
        if tok and q in SP_TOK: TOK_N[0] += 1; return SP_TOK[q]
        return f"{_num(q)}px"
    return re.sub(r'(?<![\w.#-])(-?)(\d*\.?\d+)px', f, val)
SP_PROPS = r'(?:padding|margin|gap|row-gap|column-gap|scroll-padding)(?:-(?:top|right|bottom|left|inline|block)(?:-start|-end)?)?'
def spacing(src):
    n = [0]
    def css(m):
        new = m.group(1) + snap_vals(m.group(2), True)
        if new != m.group(0): n[0] += 1
        return new
    src = re.sub(r'(?<![\w-])(' + SP_PROPS + r'\s*:\s*)([^;}"`\n]+)', css, src)
    J = r'(?:padding|margin|gap|rowGap|columnGap)(?:Top|Right|Bottom|Left|Inline|Block)?'
    def jsx(m):
        k, v = m.group(1), m.group(2)
        if v.startswith("'"): nv = snap_vals(v, True)
        else:
            x = float(v); nv = v if x < 0 else str(_num(snapv(x)))
        if nv != v: n[0] += 1
        return k + nv
    src = re.sub(r'(?<![\w-])(' + J + r'\s*:\s*)(\'[^\']*\'|-?\d+(?:\.\d+)?)(?![\w.])', jsx, src)
    print('r25: spacing values snapped', n[0], '; written as --sp tokens', TOK_N[0])
    return src
