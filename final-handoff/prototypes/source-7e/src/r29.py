"""pass 7e (review r28): two blocking fixes and five polish items on 7d. No new features."""
def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, n, a[:160])
    return s.replace(a, b)

def weeks(src):
    # B1: the week page reads each day and each period by the rule version and type in force then (cadOn / periodOf), as monthTotal does
    src = rep(src, "    const RD = R.filter(it => it.cad === 'day' && it.tg.cmp !== 'none'), RW = R.filter(it => it.cad === 'week' && it.tg.cmp !== 'none'), RO = R.filter(it => it.cad === 'none' || it.tg.cmp === 'none');",
        "    /* r29 (review r28 B1): a routine whose type changed this week appears under each type for the days that type held */\n"
        "    const tyOn = (it, d) => it.src ? cadOn(it.src, d).type : it.cad; const tgOn = (it, d) => it.src ? E.state(w, it, d, d).tg || it.tg : it.tg;\n"
        "    const daysOf = (it, ty) => { const o = []; for (let d = Math.max(ws, it.created); d <= Math.min(we, w.today); d++) if (tyOn(it, d) === ty && tgOn(it, d).cmp !== 'none') o.push(d); return o; };\n"
        "    const wkP = it => { const L = daysOf(it, 'week'); if (!L.length) return null; const [pa, pb] = it.src ? periodOf(it.src, L[0]) : [ws, we]; return [Math.max(pa, ws), Math.min(pb, we)]; };\n"
        "    const RD = R.filter(it => daysOf(it, 'day').length), RW = R.filter(it => wkP(it)), RO = R.filter(it => !RD.includes(it) && !RW.includes(it) && (it.cad === 'none' || it.tg.cmp === 'none'));")
    src = rep(src, "<div class=\"staff\">${RD.map(it => rail(w, it, ws)).join('')}</div>", "<div class=\"staff\">${RD.map(it => rail(w, it, ws, d => tyOn(it, d) === 'day')).join('')}</div>")
    src = rep(src, "<div class=\"staff\">${RW.map(it => staff(w, it, ws, we)).join('')}</div>", "<div class=\"staff\">${RW.map(it => { const [pa, pb] = wkP(it); return staff(w, it, pa, pb, false, pa > ws ? pa : null); }).join('')}</div>")
    # rail: only the days that were day periods are judged; the others are not part of it
    src = rep(src, "function rail(w, it, ws) { const aim = it.tg.v || 1; let met = 0, fin = 0, rec = 0;\n  const cells = Array.from({ length: 7 }, (_, k) => { const d = ws + k; if (d < it.created || (it.retired != null && d >= it.retired) || d > w.today) return '<i class=\"x\"></i>'; const st = E.state(w, it, d, d);\n    if (st.st === 'aside' || st.st === 'paused') return '<i class=\"a\"></i>';",
        "function rail(w, it, ws, isDay) { let met = 0, fin = 0, rec = 0; /* r29: isDay(d) false = that day belonged to another type of period */\n  const cells = Array.from({ length: 7 }, (_, k) => { const d = ws + k; if (d < it.created || (it.retired != null && d >= it.retired) || d > w.today || (isDay && !isDay(d))) return '<i class=\"x\"></i>'; const st = E.state(w, it, d, d); const aim = (st.tg || it.tg).v || 1;\n    if (st.st === 'paused') return '<i class=\"pz\"></i>'; if (st.st === 'aside') return '<i class=\"a\"></i>';")
    # staff: a period cut short by a change of type says since when, never "for the week"
    src = rep(src, "function staff(w, it, a, b, bare) {", "function staff(w, it, a, b, bare, cut) {")
    src = rep(src, "  const say = st.st === 'met' ? (st.open ? `${vtxt(it, st.v)}, settled for the ${it.cad === 'month' ? 'month' : 'week'}` : `${vtxt(it, st.v)}, at its aim`) : st.st === 'aside' ? 'Set aside' : st.st === 'paused' ? 'Paused' : !st.n ? (st.open ? 'Not yet' : 'Nothing recorded') : `${vtxt(it, st.v)} of ${aimTxt(it, tg0)}${st.open ? ' so far' : ''}`;",
        "  const since = cut != null ? ` since ${cut === w.today ? 'today' : D.day(cut, { noDow: true })}` : ''; /* r29 */\n"
        "  const say = st.st === 'met' ? (st.open ? (since ? `${vtxt(it, st.v)}, at its aim${since}` : `${vtxt(it, st.v)}, settled for the ${it.cad === 'month' ? 'month' : 'week'}`) : `${vtxt(it, st.v)}, at its aim`) : st.st === 'aside' ? 'Set aside' : st.st === 'paused' ? 'Paused' : !st.n ? (st.open ? (since ? `None logged${since}` : 'Not yet') : 'Nothing recorded') : `${vtxt(it, st.v)} of ${aimTxt(it, tg0)}${st.open ? (since || ' so far') : ''}`;")
    return src

def paused(src):
    # B2: a paused routine reads "Paused" in a month's Totals, and its periods are drawn as paused, never as empty expectations
    src = rep(src, "  if (!fin.length) s = open ? (open.st === 'met' ? 'At its aim' : open.n ? `${vtxt(it, open.v)} of ${aimTxt(it, open.tg)} so far` : 'Not yet') : paused() ? 'Paused' : `No finished ${open ? open.c : 'period'} yet`;",
        "  if (!fin.length) s = paused() || (open && open.st === 'paused') ? 'Paused' : open ? (open.st === 'met' ? 'At its aim' : open.n ? `${vtxt(it, open.v)} of ${aimTxt(it, open.tg)} so far` : 'Not yet') : `No finished ${open ? open.c : 'period'} yet`; /* r29 (review r28 B2): paused first */")
    src = rep(src, "    out.push(st.st === 'aside' || st.st === 'paused' ? '<i class=\"a\"></i>' :", "    out.push(st.st === 'paused' ? '<i class=\"pz\"></i>' : st.st === 'aside' ? '<i class=\"a\"></i>' :")
    src = rep(src, "V.push({ v: v.n ? (it.measure === 'confirmation' || it.measure === 'count' && !aim ? v.n : v.v) : 0, n: v.n, as: st.st === 'aside' || st.st === 'paused', met: st.st === 'met' }); }",
        "V.push({ v: v.n ? (it.measure === 'confirmation' || it.measure === 'count' && !aim ? v.n : v.v) : 0, n: v.n, as: st.st === 'aside' || st.st === 'paused', pz: st.st === 'paused', met: st.st === 'met' }); }")
    src = rep(src, "x.as && !x.n ? '<i class=\"a\"></i>' :", "x.pz && !x.n ? '<i class=\"pz\"></i>' : x.as && !x.n ? '<i class=\"a\"></i>' :")
    return src


def guard(src):
    # P1: a sheet opened for an item that isn't there says so, instead of taking the React tree down
    src = rep(src, "const SheetView = ({ s }) => {\n  switch (s.k) {",
        "const ID_SHEETS = ['target', 'presets', 'measure', 'rename', 'drink', 'itemdet', 'linkw']; /* r29: sheets that read one item */\n"
        "function GoneSheet() { const S = useStore(); return <Sheet title=\"Not here any more\" onClose={S.sheet.close} sheetKey=\"gone\">{() => <p className=\"t-xs\" style={{ padding: '0 var(--gut)' }} data-gone>This routine isn’t in Meridian any more, so there is nothing to change. Nothing was changed.</p>}</Sheet>; }\n"
        "const SheetView = ({ s }) => {\n  const S8 = useStore(); if (ID_SHEETS.includes(s.k) && !(S8.db && S8.db.byId[s.id])) return <GoneSheet />;\n  switch (s.k) {")
    return src

def toasts(src):
    # P2: a change of type starts today, and the toast says so for every type (and for a target set on a period cut short today)
    src = rep(src, "const cadMoved = !!(it.src.cadence && it.src.cadence.type !== 'none' && cadKey(it.src.cadence) !== cadKey(cadence) && cadence.type !== 'none');",
        "const cadMoved = !!(it.src.cadence && it.src.cadence.type !== 'none' && cadKey(it.src.cadence) !== cadKey(cadence) && cadence.type !== 'none'); const madeToday = x => x.set === w.today && x.from <= w.today; /* r29 */")
    # P3: a rule set today and replaced today by a new type is dropped, not left behind as a short period to be judged
    src = rep(src, "  const nt = { from: pa, ...(tg.cmp === 'range'", "  const nt = { from: pa, set: w.today, ...(tg.cmp === 'range'")
    src = rep(src, "  const targets = [...(it.src.targets || []).filter(x => x.from < pa), nt];", "  const targets = [...(it.src.targets || []).filter(x => x.from < pa && !(cadMoved && madeToday(x))), nt];")
    src = rep(src, "`${said}, starting ${pw === 'day' ? 'today' : 'this ' + pw}`) : tg.cmp === 'none'", "`${said}, starting ${pw === 'day' || pa === w.today ? 'today' : 'this ' + pw}`) : tg.cmp === 'none'")
    src = rep(src, "`${said}, starting ${pw === 'day' || cadMoved ? 'today' : 'this ' + pw}.", "`${said}, starting ${pw === 'day' || cadMoved || pa === w.today ? 'today' : 'this ' + pw}.")
    src = rep(src, "`${preview}, starting ${it2.cadence.type === 'day' ? 'today' : 'this ' + (it2.cadence.type === 'everyN' ? 'window' : it2.cadence.type)}`",
        "`${preview}, starting ${it2.cadence.type === 'day' || from === db.today ? 'today' : 'this ' + (it2.cadence.type === 'everyN' ? 'window' : it2.cadence.type)}`")
    return src

def breakdown(src):
    # P3: the breakdown counts every finished period, the ones with no target too; an empty period (cut to nothing) is not one
    src = rep(src, "function perSay(it, P) { const fin = P.filter(p => !p.open);", "function perSay(it, P) { P = P.filter(p => !(p.b < p.a) && !(p.end < p.a0)); if (!P.length) return 'Nothing recorded yet.'; const fin = P.filter(p => !p.open); /* r29: no zero-length period */")
    src = rep(src, "[c('aside'), 'set aside'], [c('paused'), 'paused']].filter(x => x[0])", "[c('aside'), 'set aside'], [c('paused'), 'paused'], [c('rec'), 'with no target'], [c('pre'), 'before it began']].filter(x => x[0])")
    return src

def chartlabel(src):
    # P4: the chart's label follows the filter
    src = rep(src, 'aria-label="2026, a mark a week, as tall as the share of your routines with something done that week. Press a month to read it, again to open it"',
        'aria-label="2026, a mark a week, ${f ? `as tall as the share of that week\'s days with ${esc(f.short)} done` : \'as tall as the share of your routines with something done that week\'}. Press a month to read it, again to open it"')
    return src

def loomnames(src):
    # P5: the Routines hero gives its names the room they need (measured, up to 40 % of the width), not a fixed 86 px
    src = rep(src, "const X0 = PAD + NAMEW, X1 = W - PAD, Y0 = 30;",
        "const NW = (() => { try { const c = document.createElement('canvas').getContext('2d'); c.font = `500 ${12 * (parseFloat(getComputedStyle(host).getPropertyValue('--ts')) || 1)}px Geist, system-ui, sans-serif`; return Math.round(Math.min(W * .4, Math.max(NAMEW, 14 + Math.max(...T.map(it => c.measureText(it.short).width))))); } catch (e) { return NAMEW; } })(); /* r29 */ const X0 = PAD + NW, X1 = W - PAD, Y0 = 30;")
    src = rep(src, "max-width:${NAMEW - 10}px;overflow:hidden;text-overflow:ellipsis\">${esc(it.short)}</span>", "max-width:${NW - 10}px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap\" title=\"${esc(it.short)}\">${esc(it.short)}</span>")
    return src


PZ_CSS = r'''
.tl .li[data-rh] .d:not(.q) { background: var(--rc); box-shadow: 0 0 6px var(--rcg); } /* r29: an entry's dot in its routine's light */
.scroll { padding-bottom: calc(152px + env(safe-area-inset-bottom, 0px)) !important; } /* r29: clears the dock and the home indicator */
/* r29 (look slice B4): a routine's state goes under its name when both don't fit on one line, so a name is never cut */
:host .idx .tk { display: flex !important; flex-direction: row !important; flex-wrap: wrap !important; justify-content: flex-start !important; align-items: center; column-gap: var(--sp-3); row-gap: var(--sp-1); }
:host .idx .tk .tn { flex: 1 0 auto !important; max-width: 100% !important; min-width: 0; }
:host .idx .tk .tf { flex: 0 1 auto !important; margin-left: auto !important; max-width: 100% !important; text-align: right; }
:host .kvs .kv { font-size: calc(17px * var(--ts, 1)) !important; min-height: 56px; } /* r29: a reading plate in list type */
#yhero .ykey { margin: 0; font: 500 calc(12px * var(--ts, 1))/1.35 var(--ui); color: var(--t3); text-shadow: var(--deb); } /* r29: the year's key */
/* r29 (review r28 B2): a paused period is not an expectation: no empty bar or track, only a faint dotted line, and the plate says Paused */
:host :is(.wkb, .rail) i.pz { background: linear-gradient(90deg, rgba(232,239,248,.22) 50%, transparent 0) 0 50% / 6px 2px repeat-x !important; box-shadow: none !important; border: 0 !important; }
:host :is(.wkb, .rail) i.pz > * { display: none !important; }
:host .comb i.pz { background: none !important; box-shadow: none !important; }
:host :is(.sf.pa, .sfb.pa) :is(.trk, .sg) { background: linear-gradient(90deg, rgba(232,239,248,.22) 50%, transparent 0) 0 50% / 6px 2px repeat-x !important; box-shadow: none !important; border: 0 !important; }
:host :is(.sf.pa, .sfb.pa) :is(.trk, .sg) > * { display: none !important; }
'''

def pzcss(src):
    k = ":host .stepper > button:active { background: rgba(var(--nSd), .38) !important; box-shadow: inset 2px 3px 6px rgba(var(--nSd), .6), inset -1px -1px 2px rgba(var(--nSl), .06) !important; transition: background-color .08s var(--press), box-shadow .08s var(--press); }\n"
    return rep(src, k, k + PZ_CSS.lstrip('\n'))


def perf(src):
    # look slice B1: page changes at 7c's frame rate. The sink is opacity only (one composited layer, no repaint of every shadow);
    # only the first forms in view extrude (PG.max), the rest are up at once; the page no longer starts flat as a whole
    src = rep(src, "const PG = { out: 160, rise: 260, step: 35, cap: 300 };", "const PG = { out: 160, rise: 260, step: 35, cap: 300, max: 8 }; /* r29: at most 8 forms extrude */")
    src = rep(src, "    page.style.setProperty('--g', '0'); let tries = 0;\n    const go = () => { const L = formsIn(page); if (!L.length && tries++ < 6) { requestAnimationFrame(go); return; }\n      L.forEach((e, i) => {",
        "    let tries = 0;\n    const go = () => { const L = formsIn(page).slice(0, PG.max); if (!L.length && tries++ < 6) { requestAnimationFrame(go); return; }\n      L.forEach((e, i) => {")
    src = rep(src, "      page.style.removeProperty('--g'); };\n    requestAnimationFrame(() => requestAnimationFrame(go));", "    };\n    go();")
    src = rep(src, "const a = el.animate(rm ? [{ opacity: 1 }, { opacity: 0 }] : [{ '--g': 1, opacity: 1 }, { '--g': 0, opacity: 0 }],", "const a = el.animate([{ opacity: 1 }, { opacity: 0 }], /* r29: opacity only, composited */")
    src = rep(src, "@keyframes n7sink { from { --g: 1; opacity: 1; } to { --g: 0; opacity: 0; } }", "@keyframes n7sink { from { opacity: 1; } to { opacity: 0; } } /* r29: opacity only */")
    # the forms rise on the compositor (opacity, translate): an extruding --g repaints every shadow each frame. Only the lead form extrudes
    src = rep(src, "L.forEach((e, i) => { const a = e.animate([{ '--g': 0 }, { '--g': 1 }], {",
        "L.forEach((e, i) => { const a = e.animate(i < PG.ext ? [{ '--g': 0, opacity: 0, translate: '0 8px' }, { '--g': 1, opacity: 1, translate: '0 0' }] : [{ opacity: 0, translate: '0 8px' }, { opacity: 1, translate: '0 0' }], {")
    src = rep(src, "cap: 300, max: 8 }", "cap: 300, max: 8, ext: 1 }")
    return src

def timechart(src):
    # look slice B2: the year reads as a chart. A printed key says what a mark is; the month being read carries its name
    src = rep(src, '<div class="ypr" aria-hidden="true"></div></div>`;',
        '<div class="ypr" aria-hidden="true"></div><p class="ykey" aria-hidden="true">${f ? `Share of days with ${esc(f.short)} done, per week` : \'Share of routines done, per week\'}</p></div>`; /* r29 */')
    src = rep(src, "${D.MON3[k][0]}</span>`; }", "${k === m ? D.MON3[k] : D.MON3[k][0]}</span>`; } /* r29: the month read, by name */")
    # the week: under each day only its name; the count was read as a date. The dots are the count; the button says it
    src = rep(src, """'disabled'}><b class="${c && c.type !== 'travel' ? 'as' : ''}">${D.DOW[D.dow(d)].slice(0, 3)}</b><span class="tnum">${n == null ? '' : n ? n : '·'}</span></button>`""",
        """'disabled'} aria-label="${D.DOW[D.dow(d)]}${n == null ? ', still ahead' : n ? `, ${n} done` : ', nothing done'}"><b class="${c && c.type !== 'travel' ? 'as' : ''}">${D.DOW[D.dow(d)].slice(0, 3)}</b></button>`""")
    return src

PLATE_CSS = r'''
/* r29 (look slice B3): the plate spec off Today too. A card is a plate (26 px corners, 20/18 insets) and its readings are list type;
   a sheet's list is a stack of plates, one per row, never a raised group of rows */
:root:root .card { border-radius: var(--pR) !important; padding: var(--pY) var(--pX) !important; }
:root:root .card > .kv { font-size: calc(17px * var(--ts, 1)) !important; min-height: 48px; align-items: center; }
:root:root .card > .kv .k, .card > .kv .v { font-size: inherit !important; }
:root:root .card > .kv .v { font-weight: 600; color: var(--cream, inherit); }
:is(.screen, #n7a) .sheet .list.list { background: none !important; box-shadow: none !important; border-radius: 0 !important; overflow: visible !important; padding: 0 !important; display: grid !important; gap: var(--pGap) !important; --e: 0 !important; }
:is(.screen, #n7a) .sheet .list.list > .n7c { display: none !important; }
:is(.screen, #n7a) .sheet .list.list > :not(.n7c) { border-radius: var(--pR) !important; position: relative; min-height: 64px; border: 0 !important; }
:is(.screen, #n7a) .sheet .list.list > .row, :is(.screen, #n7a) .sheet .list.list > :not(.row):not(.n7c) > .row { padding: 12px 14px 12px var(--pX) !important; border: 0 !important; }
:is(.screen, #n7a) .sheet .list.list > .row::before, :is(.screen, #n7a) .sheet .list.list > * > .row::before { display: none !important; }
:is(.screen, #n7a) .sheet .list.list .row .ttl { font-size: calc(17px * var(--ts, 1)) !important; font-weight: 600 !important; line-height: 1.25 !important; }
:is(.screen, #n7a) .sheet .list.list .row .sub { font-size: calc(15px * var(--ts, 1)) !important; line-height: 1.35 !important; }
.n7-stack { display: grid; gap: var(--pGap); }
/* r29 (cheap): the dock and everything placed from the bottom clear the home indicator */
:is(.screen, #n7a) .tabbar { bottom: calc(14px + env(safe-area-inset-bottom, 0px)) !important; }
:is(.screen, #n7a) .toast { bottom: calc(96px + env(safe-area-inset-bottom, 0px)); }
:is(.screen, #n7a) .toast.nobar { bottom: calc(40px + env(safe-area-inset-bottom, 0px)); }
:is(.screen, #n7a) .livebar { bottom: calc(96px + env(safe-area-inset-bottom, 0px)) !important; }
:is(.screen, #n7a) .sheet .padhome { padding-bottom: calc(56px + env(safe-area-inset-bottom, 0px)); }
/* a sheet's row plate presses as every plate does: the face carves in, its walls and drop go to .3 */
:is(.screen, #n7a) .sheet .list.list > :not(.n7c):is(button:active, :has(> button:not(.act):active, > .row > button:not(.act):active)) { --e: -.4 !important; transition: --e .08s var(--press); }
:is(.screen, #n7a) .sheet .list.list > :not(.n7c):is(button:active, :has(> button:not(.act):active, > .row > button:not(.act):active)) > .n7c .fc { box-shadow: inset 9px 9px 20px rgba(var(--nSd),calc(.55 * var(--nSda))), inset -6px -6px 14px rgba(var(--nSl),calc(.04 * var(--nSla))) !important; transition: box-shadow .08s var(--press); }
:is(.screen, #n7a) .sheet .list.list > :not(.n7c):is(button:active, :has(> button:not(.act):active, > .row > button:not(.act):active)) > .n7c :is(.wl, .sh) { opacity: .3 !important; transition: opacity .08s var(--press); }
'''

def plates(src):
    k = "@keyframes n7sink { from { opacity: 1; } to { opacity: 0; } } /* r29: opacity only */"
    src = rep(src, k, k + PLATE_CSS)
    # the clay: a list in a sheet is no plate; each of its rows is
    src = rep(src, "'.t3 .ztok', '.list', '.card',", "'.t3 .ztok', '.list:not(.sheet .list)', '.sheet .list > :not(.n7c)', '.card',")
    # the sleep page: the patterns key leaves the card and sits under it
    src = rep(src, """: <p className="t-s">Nothing recorded that day.</p>}
          <button className="btn sec2 wide" style={{ marginTop: 12 }} onClick={() => S.nav.push({ k: 'patterns', role: 'sleep' })} data-sleep-patterns>Patterns involving sleep</button>
        </div>""", """: <p className="t-s">Nothing recorded that day.</p>}
        </div>
        <button className="btn sec2 wide" style={{ marginTop: 'var(--pGap)' }} onClick={() => S.nav.push({ k: 'patterns', role: 'sleep' })} data-sleep-patterns>Patterns involving sleep</button>""")
    # the drink: From and To are a plate each
    src = rep(src, """<div className="card" style={{ padding: 'var(--sp-3) var(--sp-4)', margin: 0 }} data-drink-range>
        {[['From', lo, setLo], ['To', hi, setHi]].map(([l, x, set]) => <div className="kv" key={l} style={{ alignItems: 'center' }}>""",
        """<div className="n7-stack" data-drink-range>
        {[['From', lo, setLo], ['To', hi, setHi]].map(([l, x, set]) => <div className="card" key={l} style={{ margin: 0, paddingTop: 10, paddingBottom: 10 }}><div className="kv" style={{ alignItems: 'center', border: 0 }}>""")
    src = rep(src, """<Icon n="plus" s={18} /></button></span></div>)}
      </div>""", """<Icon n="plus" s={18} /></button></span></div></div>)}
      </div>""")
    return src

def cheap(src):
    # cheap: no two neighbours share a light. The Paused section sits after the active ones too, so the window counts it in that order
    src = rep(src, "[...items].sort((a, b) => (gone(a) - gone(b)) || (gi(a) - gi(b))).forEach(it => {",
        "const pzd = it => (it.pauses || []).some(p => p.to == null); /* r29: paused routines are listed after the active ones */\n  [...items].sort((a, b) => (gone(a) - gone(b)) || (pzd(a) - pzd(b)) || (gi(a) - gi(b))).forEach(it => {")
    return src

def hues(src):
    # cheap: a day's entries and an item's chart carry the routine's light, as every other mark of it does
    src = rep(src, """return `<div class="li"><span class="tm">${D.hm(e.t)}</span><i class="d${it.kind === 'observation' ? ' q' : ''}"></i>""",
        """return `<div class="li"${it.kind === 'routine' ? neuRH(it) : ''}><span class="tm">${D.hm(e.t)}</span><i class="d${it.kind === 'observation' ? ' q' : ''}"></i>""")
    src = rep(src, """R.map(e => `<button class="li" data-act="entry" data-e="${e.id}">""", """R.map(e => `<button class="li"${obs ? '' : neuRH(it)} data-act="entry" data-e="${e.id}">""")
    # the periods chart: its beads in the routine's light (cream for a routine without one); today's stay warm
    src = rep(src, "const FS = `uniform float uNP, uNC, uPad, uCW, uBase, uHH, uNoT, uSel;", "const s0 = it.src || it; const hh = s0.hue != null && !s0.neutral ? neuHue(s0) : null; const HC = hh == null ? [1, .9, .78] : neuRGB(hh); /* r29 */\n  const FS = `uniform float uNP, uNC, uPad, uCW, uBase, uHH, uNoT, uSel; uniform vec3 uHC;")
    src = rep(src, "vec3 cl=mix(CREAM,mix(CREAM,WARM*1.3,.8),step(.95,d.a)); float b=(d.a>.5?1.:.75)*(abs(k-uSel)<.5?1.25:1.);",
        "vec3 cl=mix(uHC,mix(uHC,WARM*1.3,.8),step(.95,d.a)); float b=(d.a>.5?1.:.75)*(abs(k-uSel)<.5?1.25:1.);")
    src = rep(src, "gl.uniform1f(Lc('uSel'), S.sel[it.id] != null ? S.sel[it.id] : P.length - 1); },", "gl.uniform1f(Lc('uSel'), S.sel[it.id] != null ? S.sel[it.id] : P.length - 1); gl.uniform3f(Lc('uHC'), HC[0], HC[1], HC[2]); },")
    src = rep(src, "ctx.fillStyle = p[3] > .95 ? 'rgba(255,150,90,.95)' : `rgba(232,239,248,${p[3] > .5 ? .95 : .72})`;", "ctx.fillStyle = p[3] > .95 ? 'rgba(255,150,90,.95)' : `rgba(${HC.map(v => Math.round(v * 255)).join(',')},${p[3] > .5 ? .95 : .72})`;")
    # the loom's labels stay inside the 16 px gutter
    src = rep(src, """const a = w.today - LOOM_DAYS + 1; for (let k = 0; k < LOOM_DAYS; k++) { const d = a + k; if (D.dow(d) === 1) lb += `<span class="lb" style="left:${X0 + (k + .5) * dw}px;top:4px;transform:translateX(${X0 + (k + .5) * dw + 24 > X1 + PAD ? '-100%' : '-50%'})">${D.dom(d)} ${D.MON3[D.monthOf(d)]}</span>`; }
    lb += `<span class="lb sun" style="left:${X1 - dw / 2}px;top:${H - 14}px;transform:translateX(-50%)">today</span>`;""",
        """const hr = host.getBoundingClientRect(), hk = hr.width ? host.offsetWidth / hr.width : 1; const mc = document.createElement('canvas').getContext('2d'); mc.font = `500 ${12 * (parseFloat(getComputedStyle(host).getPropertyValue('--ts')) || 1)}px Geist, system-ui, sans-serif`;
    const inG = (x, t) => { const tw = mc.measureText(t).width + 2; const lo = (16 - hr.left) * hk, hi = (innerWidth - 16 - hr.left) * hk; return Math.round(Math.max(lo, Math.min(x - tw / 2, hi - tw))); }; /* r29: centred on its day, never past the gutter */
    const a = w.today - LOOM_DAYS + 1; for (let k = 0; k < LOOM_DAYS; k++) { const d = a + k; if (D.dow(d) === 1) { const t = `${D.dom(d)} ${D.MON3[D.monthOf(d)]}`; lb += `<span class="lb" style="left:${inG(X0 + (k + .5) * dw, t)}px;top:4px">${t}</span>`; } }
    lb += `<span class="lb sun" style="left:${inG(X1 - dw / 2, 'today')}px;top:${H - 14}px">today</span>`;""")
    return src

def late(src):
    for f in (weeks, paused, guard, toasts, breakdown, chartlabel, loomnames, pzcss, perf, timechart, plates, cheap, hues):
        src = f(src)
    return src
