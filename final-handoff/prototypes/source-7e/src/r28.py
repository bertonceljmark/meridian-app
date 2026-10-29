# pass 7d, Mark's calls on the 7c preview: no drawn phone status bar (the real one, through the safe area), no moat,
# page changes that sink and extrude, the v7 plate everywhere, and a new Time chart. Applied after r27.
import re

def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, n, a[:160])
    return s.replace(a, b)

# the top of every screen: the real status bar's height in a home-screen PWA (Dynamic Island included), 0 in a browser tab
SB = 'var(--sb)'

def status(src):
    # the meta that lets a home-screen PWA draw under the real status bar
    src = rep(src, '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n<meta name="theme-color" content="#1D2633">')
    # the drawn status bar, island and home bar go; the demo's "Different data" pill moves into Today's header (v3 scenario only)
    a = src.index('    <div className={cx(\'status\', (deepTop || weekClose || onboard) && \'on-deep\')}>')
    b = src.index('    <div className="sr" aria-live="polite" data-announce>', a)
    src = src[:a] + '    <div className="n7sb" aria-hidden="true" /> {/* r28: the real status bar\'s band (env(safe-area-inset-top)); no drawn one */}\n' + src[b:]
    src = rep(src, "    <div className={cx('homebar', (weekClose || onboard || !anySheet) && 'on-deep')} />\n", '')
    src = rep(src, "      {ctxTxt && <button className=\"zctxchip\"",
        "      {S.scen === 'v3' && <button className=\"ddata\" onClick={() => S.setSample(((S.sample || 0) + 1) % T3_SAMPLES.length)} aria-label=\"Show different data\" data-sample-pill>Different data <b>{(S.sample || 0) + 1}/{T3_SAMPLES.length}</b></button>}\n"
        "      {ctxTxt && <button className=\"zctxchip\"")
    src = src.replace('.status .ddata', '.zhead .ddata')
    # the fixed offsets that sat under the drawn bar (54 px) now sit under the real one
    R = [
        ('.navbar { position: absolute; left: 0; right: 0; top: 0; height: 98px; padding-top: 56px;', f'.navbar {{ position: absolute; left: 0; right: 0; top: 0; height: calc({SB} + 48px); padding-top: calc({SB} + 4px);'),
        ('.navbar .ttl { position: absolute; left: 70px; right: 70px; top: 54px;', f'.navbar .ttl {{ position: absolute; left: 70px; right: 70px; top: calc({SB} + 4px);'),
        ('.rootbar { position: absolute; left: 0; right: 0; top: 0; height: 98px; padding-top: 56px;', f'.rootbar {{ position: absolute; left: 0; right: 0; top: 0; height: calc({SB} + 48px); padding-top: calc({SB} + 4px);'),
        ('.rootbar .ttl { position: absolute; left: 0; right: 0; top: 54px;', f'.rootbar .ttl {{ position: absolute; left: 0; right: 0; top: calc({SB} + 4px);'),
        ('.statusscrim { position: absolute; left: 0; right: 0; top: 0; height: 54px;', f'.statusscrim {{ position: absolute; left: 0; right: 0; top: 0; height: {SB};'),
        ('.statusscrim { background: var(--stage); height: 50px;', f'.statusscrim {{ background: var(--stage); height: {SB};'),
        ('.today-head { padding: 64px var(--gut) 0; }', f'.today-head {{ padding: calc({SB} + 16px) var(--gut) 0; }}'),
        ('.today-head { padding-top: 64px; }', f'.today-head {{ padding-top: calc({SB} + 16px); }}'),
        ('.today-head { padding-top: 56px; }', f'.today-head {{ padding-top: calc({SB} + 16px); }}', 2),
        ('.today-head { padding-top: 48px; }', f'.today-head {{ padding-top: calc({SB} + 16px); }}'),
        ('max-height: calc(100% - 58px);', f'max-height: calc(100% - {SB} - 8px);'),
        ('.sheet.full { top: 58px; }', f'.sheet.full {{ top: calc({SB} + 8px); }}'),
        ('.hero { position: relative; background: var(--field); padding: 104px var(--gut) var(--sp-5); }', f'.hero {{ position: relative; background: var(--field); padding: calc({SB} + 56px) var(--gut) var(--sp-5); }}'),
        ('.onboard .ob-body { flex: 1; overflow-y: auto; padding: 72px 20px 20px; }', f'.onboard .ob-body {{ flex: 1; overflow-y: auto; padding: calc({SB} + 32px) 20px 20px; }}'),
        ('justify-content: center; padding-top: 56px; position: absolute; left: 0; right: 0; top: 0; }', f'justify-content: center; padding-top: calc({SB} + 16px); position: absolute; left: 0; right: 0; top: 0; }}'),
        ('.wclose .bars { display: flex; gap: var(--sp-1); padding: 64px var(--gut) 0; }', f'.wclose .bars {{ display: flex; gap: var(--sp-1); padding: calc({SB} + 16px) var(--gut) 0; }}'),
        ('.plainhead { padding: 104px var(--gut) 0; }', f'.plainhead {{ padding: calc({SB} + 56px) var(--gut) 0; }}'),
        ('.mi-ptr { position: absolute; left: 0; right: 0; top: 54px;', f'.mi-ptr {{ position: absolute; left: 0; right: 0; top: {SB};'),
        ('.toast.top { bottom: auto; top: 54px; }', f'.toast.top {{ bottom: auto; top: calc({SB} + 8px); }}'),
        ('.t3 .zhead { position: relative; padding: 56px var(--gut) 0;', f'.t3 .zhead {{ position: relative; padding: calc({SB} + 16px) var(--gut) 0;'),
        (':is(.t3,#n7a) .zhead{padding-top:48px}', f':is(.t3,#n7a) .zhead{{padding-top:calc({SB} + 16px)}}'),
        ('.head{position:relative;z-index:2;padding:56px var(--gut) 0;', f'.head{{position:relative;z-index:2;padding:calc({SB} + 16px) var(--gut) 0;'),
        ('.back{display:flex;align-items:center;gap:2px;height:40px;margin:48px 0 0 var(--sp-2);', f'.back{{display:flex;align-items:center;gap:2px;height:40px;margin:calc({SB} + 4px) 0 0 var(--sp-2);'),
        (':is(.screen,#n7a) .v3bar { display: block !important; padding: 64px 112px 0 !important;', f':is(.screen,#n7a) .v3bar {{ display: block !important; padding: calc({SB} + 14px) 112px 0 !important;'),
        ("<div key=\"0\" data-ob=\"welcome\" style={{ paddingTop: 56 }}>", "<div key=\"0\" data-ob=\"welcome\" style={{ paddingTop: 'calc(var(--sb) + 16px)' }}>"),
        ("<div style={{ padding: '104px var(--gut) 0' }} data-dayview={d}>", "<div style={{ padding: 'calc(var(--sb) + 56px) var(--gut) 0' }} data-dayview={d}>"),
        ("<div style={{ padding: '104px var(--gut) 0' }} data-monthview={m}>", "<div style={{ padding: 'calc(var(--sb) + 56px) var(--gut) 0' }} data-monthview={m}>"),
        ("<div style={{ padding: '104px var(--gut) var(--sp-5)' }} data-analysis-empty>", "<div style={{ padding: 'calc(var(--sb) + 56px) var(--gut) var(--sp-5)' }} data-analysis-empty>"),
        ("<div style={{ padding: '104px var(--gut) 0' }} data-analysis={key}>", "<div style={{ padding: 'calc(var(--sb) + 56px) var(--gut) 0' }} data-analysis={key}>"),
    ]
    for r in R:
        src = rep(src, r[0], r[1], r[2] if len(r) > 2 else 1)
    # the v3 bar (a solid title bar once scrolled) is as tall as the head it replaces
    src = rep(src, '.v3bar { position: absolute; top: 0; left: 0; right: 0; height: 92px;', f'.v3bar {{ position: absolute; top: 0; left: 0; right: 0; height: calc({SB} + 52px);')
    # the v3 pages' own spacer under the navbar (98 px bar - 6)
    src = rep(src, '.v3sp{height:92px}', '.v3sp{height:calc(var(--sb) + 42px)}')
    # the spacers the older pages start with (98 px bar + 22) and their selectors
    src = src.replace('div[style^="padding: 104px"]', 'div[style^="padding: calc(var(--sb) + 56px)"]')
    css = f'''
/* r28: no drawn status bar. --sb is the real one (env(safe-area-inset-top)): about 59 px under a Dynamic Island in a
   home-screen PWA, 0 in a browser tab. A band of the surface's own colour sits under it so scrolled content never
   runs behind the system's clock; the clay rise takes its bottom as the visible top edge */
:root {{ --sb: env(safe-area-inset-top, 0px); }}
.n7sb {{ position: absolute; left: 0; right: 0; top: 0; height: {SB}; z-index: 60; background: var(--nSurf, var(--bg)); pointer-events: none; }}
.status, .island, .homebar {{ display: none !important; }}
.zhead .ddata {{ display: inline-flex; align-items: center; gap: 6px; margin: var(--sp-2) 0 0 !important; pointer-events: auto; }}
.page .scroll > div[style^="height: 120px"]:first-child {{ height: calc({SB} + 66px) !important; }}
'''
    i = src.index('<style id="neu7">')
    src = src[:i] + '<style id="n7sb">' + css + '</style>\n' + src[i:]
    return src


# ---- the Time chart: a carved well with a mark a week, in one strong accent (or the routine's hue when filtered), a clear
# zero line, printed month labels and context bands under it, today marked once, and each month a key you press ----
YEAR_JS = r'''
/* r28: the year as a carved well, a mark a week (53), each as tall as the week's share of routines touched; months are keys */
function yearWeeks(w, f) { const days = yearDays(w, f); const ws0 = D.wStart(0); const out = [];
  for (let k = 0; k < 53; k++) { const a = ws0 + 7 * k, b = a + 6; if (a > 364) break; let n = 0, sum = 0, known = 0, aside = 0, fut = 0, pre = 0, sick = 0;
    for (let d = Math.max(0, a); d <= Math.min(364, b); d++) { const x = days[d]; if (x.fut) { fut++; continue; } if (x.pre) { pre++; continue; } n++; sum += x.h || 0; if (x.known) known++; if (x.ctx) { aside++; if (x.ctx === 'sick') sick++; } }
    out.push({ k, a, b, n, h: n ? sum / n : 0, known, aside, sick, fut, pre, m: D.monthOf(Math.min(364, Math.max(0, a + 3))) }); }
  return out; }
function heroRead(w, m, f) { const r = monthRead(w, m, f); const fresh = w.today - w.first < 1; let h = '';
  const big = r.ahead || r.pre ? '' : f ? (r.fdays ? `<span class="fig tnum">${r.fdays}<small>of ${plural(r.n, 'day')}</small></span>` : '') : r.n && r.done ? `<span class="fig tnum">${r.done}<small>of ${plural(r.n, 'day')}</small></span>` : '';
  h += `<div class="read rd8" aria-live="polite"><b class="rt">${D.MONTHS[m]}${r.open ? ', so far' : ''}</b>${big}<div class="tx">${esc(fresh ? 'Your year starts today. Every week you log something rises here.' : r.ahead || r.pre ? r.say : (f ? r.say : r.done ? `with something done. ${r.say}` : r.say))}</div></div>`;
  if (!r.ahead && !r.pre && !fresh) h += `<div class="gos" style="margin-top:var(--sp-2)"><button class="go" data-act="month" data-m="${m}">Open ${D.MONTHS[m]}${AR}</button>${f ? `<button class="chip sm x on" data-act="unfilter">Only ${esc(f.short)} ${M.icon('close', 14, 2.2)}</button>` : ''}</div>`;
  else if (f) h += `<div class="chips" style="margin-top:var(--sp-3)"><button class="chip sm x on" data-act="unfilter">Only ${esc(f.short)} ${M.icon('close', 14, 2.2)}</button></div>`;
  return h; }
const YW = { H: 148, base: 124, top: 16, px: 14 };
function drawHero(sc, w) {
  const host = sc.querySelector('#yhero'); if (!host) return; const well = host.querySelector('.yw'), inn = host.querySelector('.ywin'), prt = host.querySelector('.ypr'); if (!well || !inn || !prt) return;
  const f = S.filter ? w.byId[S.filter] : null; const cm = D.monthOf(w.today); const m = S.sel != null ? S.sel : cm;
  const W = well.clientWidth || 358; const ws0 = D.wStart(0); const span = 53 * 7; const iw = W - 2 * YW.px; const X = d => YW.px + (d - ws0) / span * iw; const step = iw / 53; const bw = Math.max(3, Math.min(8, step * .64));
  const hh = f && f.src && f.src.hue != null && !f.src.neutral ? neuHue(f.src) : f && f.hue != null && !f.neutral ? neuHue(f) : null;
  const acc = hh == null ? 'var(--yac)' : `oklch(.78 .14 ${hh})`;
  const wk = yearWeeks(w, f); const ht = YW.base - YW.top; let s = '';
  // the zero line: solid where there are days to read, faint ahead
  const x0 = X(Math.max(0, f ? Math.max(w.first, f.created) : w.first)), xT = X(w.today + 1);
  s += `<line class="z0" x1="${x0.toFixed(1)}" x2="${xT.toFixed(1)}" y1="${YW.base + .5}" y2="${YW.base + .5}"/><line class="z0 ah" x1="${xT.toFixed(1)}" x2="${(W - YW.px).toFixed(1)}" y1="${YW.base + .5}" y2="${YW.base + .5}"/>`;
  wk.forEach(q => { if (!q.n) return; const cx = X(q.a + 3.5); const sel = q.m === m; const cls = `wk${sel ? ' on' : ''}`;
    if (!q.known) { s += `<circle class="${cls} uk" cx="${cx.toFixed(1)}" cy="${YW.base - 3}" r="2.4"/>`; return; } /* nothing recorded: unknown, not zero */
    const hv = Math.max(0, Math.min(1, q.h)); const hp = hv * ht; const col = q.aside >= Math.ceil(q.n / 2) ? (q.sick >= q.aside / 2 ? 'var(--night)' : 'var(--aside)') : acc;
    if (hp < 2.5) { s += `<rect class="${cls} zr" x="${(cx - bw / 2).toFixed(1)}" y="${YW.base - 2}" width="${bw.toFixed(1)}" height="2" rx="1"/>`; return; } /* a week with records and nothing done: a zero tick */
    s += `<rect class="${cls}${col === acc ? ' ac' : ''}" x="${(cx - bw / 2).toFixed(1)}" y="${(YW.base - hp).toFixed(1)}" width="${bw.toFixed(1)}" height="${hp.toFixed(1)}" rx="${Math.min(bw / 2, 2.5).toFixed(1)}" style="fill:${col === acc && !sel ? 'var(--ydim)' : col}"/>`; });
  // today, once: a small sun on the zero line
  s += `<circle class="sun" cx="${X(w.today + .5).toFixed(1)}" cy="${YW.base + .5}" r="3.5"/>`;
  const fx = f ? Math.max(w.first, f.created) : w.first; let pre = '';
  if (fx > 40) pre = `<span class="ybm" style="left:${YW.px}px;width:${Math.max(0, X(fx) - YW.px - 6).toFixed(0)}px">${f ? 'Before ' + esc(f.short) : 'Before Meridian'}</span>`;
  inn.style.setProperty('--ydim', `oklch(.72 .025 ${hh == null ? 232 : hh})`); /* the other months: the same hue, pale and quiet, never a dark (brown) shade */
  inn.innerHTML = `<svg width="${W}" height="${YW.H}" viewBox="0 0 ${W} ${YW.H}" aria-hidden="true">${s}</svg>${pre}` +
    Array.from({ length: 12 }, (_, k) => { const a = D.mStart(k), b = D.mEnd(k); const l = X(a), r = X(b + 1); const ok = k <= cm; const rr = ok ? monthRead(w, k, f) : null;
      return `<button class="ym${k === m ? ' on' : ''}" data-ym="${k}" style="left:${l.toFixed(1)}px;width:${(r - l).toFixed(1)}px"${ok ? '' : ' disabled'} aria-pressed="${k === m}" aria-label="${esc(D.MONTHS[k])}${rr ? ': ' + esc(rr.say) : ', still ahead'}${k === m && ok ? '. Press again to open it' : ''}"></button>`; }).join('');
  // printed under the well: month letters, the selected one lit; set-aside spans as bands with their names; today's word
  let lb = ''; for (let k = 0; k < 12; k++) { const x = (X(D.mStart(k)) + X(D.mEnd(k) + 1)) / 2; lb += `<span class="lb${k === m ? ' on' : ''}${k > cm ? ' q' : ''}" style="left:${x.toFixed(1)}px">${D.MON3[k][0]}</span>`; }
  const tx = X(w.today + .5); lb += `<span class="lb sun bd" style="left:${tx.toFixed(1)}px">today</span>`; const taken = [tx];
  w.contexts.filter(c => c.from <= w.today && c.to >= Math.max(0, w.first) && c.to - c.from >= 2).forEach(c => { const a = Math.max(0, c.from), b = Math.min(c.to, w.today); const l = X(a), r = X(b + 1); const cls = c.type === 'sick' ? 'nt' : 'as';
    lb += `<i class="yb ${cls}" style="left:${l.toFixed(1)}px;width:${Math.max(3, r - l).toFixed(1)}px"></i>`; const x = (l + r) / 2; if (taken.some(t => Math.abs(x - t) < 58)) return; taken.push(x); lb += `<span class="lb bd ${cls}" style="left:${x.toFixed(1)}px">${esc(c.label || M.CTXN[c.type])}</span>`; });
  prt.innerHTML = lb;
  if (host._wired) return; host._wired = true;
  // a tap reads a month; the same month again opens it; a drag across the well reads month by month
  const mAt = e => { const r = well.getBoundingClientRect(); const k0 = r.width ? (well.offsetWidth / r.width) : 1; const x = (e.clientX - r.left) * k0; const d = ws0 + (x - YW.px) / iw * span; return Math.max(0, Math.min(cm, D.monthOf(Math.max(0, Math.min(364, Math.floor(d)))))); };
  const setSel = k => { const cur = S.sel != null ? S.sel : D.monthOf(M.w.today); if (k === cur) return; S.sel = k; drawHero(sc, M.w); const rd = sc.querySelector('#yread'); if (rd) rd.innerHTML = heroRead(M.w, k, S.filter ? M.w.byId[S.filter] : null); };
  let down = null, moved = false;
  well.addEventListener('pointerdown', e => { down = e.clientX; moved = false; });
  well.addEventListener('pointermove', e => { if (down == null) return; if (!moved && Math.abs(e.clientX - down) > 8) { moved = true; try { well.setPointerCapture(e.pointerId); } catch (x) { } } if (moved) setSel(mAt(e)); });
  const up = () => { down = null; }; well.addEventListener('pointerup', up); well.addEventListener('pointercancel', up);
  well.addEventListener('click', e => { if (moved) { moved = false; return; } const b = e.target.closest('.ym'); if (!b || b.disabled) return; const k = +b.dataset.ym; const ww = M.w; const cur = S.sel != null ? S.sel : D.monthOf(ww.today);
    if (k === cur) { if (D.mStart(k) <= ww.today && D.mEnd(k) >= ww.first) openMonth(k); } else { setSel(k); const nb = well.querySelector(`.ym[data-ym="${k}"]`); if (nb) nb.focus({ preventScroll: true }); } });
}
'''

YEAR_CSS = r'''
/* r28 structure: the reading under the chart is one stack: the month, its figure, one sentence */
#yread .read.rd8{display:flex !important;flex-direction:column;align-items:flex-start;gap:var(--sp-1);grid-template-columns:none !important}
#yread .rd8 .rt{font:600 calc(20px * var(--ts,1))/1.2 var(--ui);color:var(--cream);letter-spacing:-.01em}
#yread .rd8 .fig{font-size:calc(48px * var(--ts,1)) !important;line-height:1 !important;margin:var(--sp-1) 0 0 !important}
#yread .rd8 .fig small{font-size:var(--pS,15px) !important;margin-left:6px}
#yread .rd8 .tx{font-size:var(--pS,15px) !important;line-height:1.4 !important;color:var(--t2) !important;max-width:34ch}

/* r28: the year, carved: a well with a mark a week; months are keys; labels and set-aside bands printed under it */
#yhero{margin:var(--sp-3) var(--gut) 0 !important;height:auto !important;--yac:oklch(.80 .11 232)}
#yhero .yw{position:relative;height:148px;border-radius:24px;--e:-1;box-shadow:var(--nElev);background-color:var(--nTone);overflow:hidden;touch-action:pan-y;cursor:pointer}
#yhero .ywin{position:absolute;inset:0}
#yhero svg{position:absolute;left:0;top:0;display:block;pointer-events:none}
#yhero .wk{opacity:.55}
#yhero .wk.on,#yhero rect.wk.ac{opacity:1}
#yhero rect.wk.on:not(.zr){filter:drop-shadow(0 0 4px color-mix(in oklab,var(--yac) 45%,transparent))}
#yhero .zr{fill:var(--t3)}
#yhero .uk{fill:none;stroke:var(--t3);stroke-width:1.2}
#yhero .z0{stroke:rgba(232,239,248,.34);stroke-width:1}
#yhero .z0.ah{stroke:rgba(232,239,248,.10);stroke-dasharray:2 4}
#yhero .sun{fill:var(--sun);filter:drop-shadow(0 0 5px rgba(255,107,61,.7))}
#yhero .ybm{position:absolute;top:56px;text-align:center;font:500 calc(12px*var(--ts,1))/1.2 var(--ui);color:var(--t3);pointer-events:none;text-shadow:var(--deb)}
#yhero .ym{position:absolute;top:0;bottom:0;padding:0;border:0;background:transparent;border-radius:10px;-webkit-tap-highlight-color:transparent;transition:background-color .12s}
#yhero .ym.on{background:rgba(var(--nSl),.035)}
#yhero .ym:active{background:rgba(var(--nSd),.38);box-shadow:inset 2px 3px 6px rgba(var(--nSd),.6),inset -1px -1px 2px rgba(var(--nSl),.06)}
#yhero .ym:focus-visible{outline:2px solid var(--sun2);outline-offset:-2px}
#yhero .ym:disabled{cursor:default}
#yhero .ypr{position:relative;height:46px;margin-top:var(--sp-2)}
#yhero .ypr .lb{position:absolute;top:0;transform:translateX(-50%);white-space:nowrap;font:500 calc(12px*var(--ts,1))/1 var(--ui);color:var(--t3);text-shadow:var(--deb);pointer-events:none}
#yhero .ypr .lb.on{color:var(--cream);font-weight:650}
#yhero .ypr .lb.q{color:var(--t4)}
#yhero .ypr .lb.bd{top:26px}
#yhero .ypr .lb.sun{color:var(--sun2);font-weight:600}
#yhero .ypr .lb.nt{color:var(--night)}
#yhero .ypr .lb.as{color:var(--aside)}
#yhero .ypr .yb{position:absolute;top:18px;height:3px;border-radius:2px;opacity:.85}
#yhero .ypr .yb.nt{background:var(--night)}
#yhero .ypr .yb.as{background:var(--aside)}
'''

def timechart(src):
    # the page: the well, the printed row, and the reading (now redrawn in place while you read months)
    a = src.index("    h += `<div class=\"hero\" id=\"yhero\" style=\"height:${HERO_H}px\"")
    b = src.index("    // this week, said in words", a)
    src = src[:a] + ("    h += `<div class=\"yr\" id=\"yhero\" role=\"group\" aria-label=\"2026, a mark a week, as tall as the share of your routines with something done that week. Press a month to read it, again to open it\"><div class=\"yw n7-well\"><div class=\"ywin\"></div></div><div class=\"ypr\" aria-hidden=\"true\"></div></div>`;\n"
        "    h += `<div id=\"yread\">${heroRead(w, m, f)}</div>`; /* r28 */\n") + src[b:]
    # the drawing: the WebGL light and its hue canvas give way to the well
    a = src.index('function drawHero(sc, w) {'); b = src.index('function reread(sc, w, k)', a)
    src = src[:a] + YEAR_JS.lstrip('\n') + src[b:]
    # the stylesheet: the time screen's own template
    src = rep(src, '<template id="v3-css-time">#yhero{margin-top:var(--sp-2)}', '<template id="v3-css-time">' + YEAR_CSS.replace('\n', '') + '')
    return src

# ---- page changes: sink and extrude (Mark: "smooth and elements extruding staggered"); no slide, the surface stays still ----
PAGE_CSS = r'''
/* r28: page changes. No slide, no zoom, no pane movement: the page under a push sinks into the surface (its forms flatten
   to printed, 160 ms, ease-in) and fades; the new page's printed layer appears as it does; the clay then extrudes its forms
   (CLAY.enter). Back is the same the other way. Reduce Motion: a 120 ms crossfade, nothing extrudes */
@keyframes n7sink { from { --g: 1; opacity: 1; } to { --g: 0; opacity: 0; } }
@keyframes n7pgin { from { opacity: 0; } to { opacity: 1; } }
.page.under { transform: none !important; transition: none !important; animation: n7sink calc(.16s * var(--n7slow, 1)) cubic-bezier(.4,0,1,1) forwards; }
.page.enter-push, .page.enter-zoom { animation: n7pgin calc(.1s * var(--n7slow, 1)) linear calc(.13s * var(--n7slow, 1)) both !important; box-shadow: none !important; transform: none !important; }
.page.leaving { animation: n7sink calc(.16s * var(--n7slow, 1)) cubic-bezier(.4,0,1,1) forwards !important; transform: none !important; }
.has-sheet .page.under { animation: none; }
.page.leaving { background-color: var(--nSurf) !important; }
/* back: the page coming back shows its printed layer once the leaving one has sunk, then extrudes */
.page:not(.under):not(.leaving):has(~ .page.leaving) { animation: n7pgin calc(.1s * var(--n7slow, 1)) linear calc(.13s * var(--n7slow, 1)) both !important; }
.rm .page.under { animation: none; visibility: hidden !important; }
.rm .page.enter-push, .rm .page.enter-zoom { animation: n7pgin .12s linear both !important; }
.rm .page.leaving { animation: n7pgin .12s linear reverse forwards !important; }
.rm .page:not(.under):not(.leaving):has(~ .page.leaving) { animation: n7pgin .12s linear both !important; }
@media (prefers-reduced-motion: reduce) {
  .page.under { animation: none; visibility: hidden !important; }
  .page.enter-push, .page.enter-zoom { animation: n7pgin .12s linear both !important; }
  .page.leaving { animation: n7pgin .12s linear reverse forwards !important; }
}
'''

def pages(src):
    # tabs: the old page sinks in place (no clone sliding off), then the tab changes and the new page extrudes; a fast
    # second tap during the sink only changes where it lands; each tab keeps its scroll
    src = rep(src, "    setTab: t => { setLeaving(null); setSheets(ss => ss.some(x => x.k === 'v3') ? ss.filter(x => x.k !== 'v3') : ss); /* r24 */ if (t === tab) setStacks(s => ({ ...s, [t]: [] })); else MI.tabFrom(screenRef.current, tab, t); setTabS(t); },",
        "    setTab: t => { setLeaving(null); setSheets(ss => ss.some(x => x.k === 'v3') ? ss.filter(x => x.k !== 'v3') : ss); /* r24 */\n"
        "      /* r28: the tab in view is PG8.shown (set on commit), never this closure's tab, which a slow render leaves stale.\n"
        "         One change at a time: a tap while one is under way only moves where it lands; tapping the tab being left cancels it */\n"
        "      const sc = screenRef.current, shown = PG8.shown || tab; if (PG8.cur && PG8.cur.fired && Date.now() - PG8.cur.at > 1500) PG8.cur = null; const P8 = PG8.cur;\n"
        "      if (P8) { if (t === P8.from && !P8.fired) { clearTimeout(P8.tm); PG8.cur = null; const el = PG8.top(sc); if (el && window.__clay) window.__clay.enter(el); } else P8.to = t; return; }\n"
        "      if (t === shown) { setStacks(s => ({ ...s, [t]: [] })); return; }\n"
        "      const c = PG8.cur = { from: shown, to: t, fired: false }; const fire = () => { if (PG8.cur !== c || c.fired) return; c.fired = true; c.at = Date.now(); clearTimeout(c.tm); PG8.save(sc, c.from); MI.tabFrom(sc, c.from, c.to); setTabS(c.to); };\n"
        "      if (rm || !window.__clay) { fire(); return; }\n"
        "      const el = PG8.top(sc); window.__clay.cancel(); const a = window.__clay.leave(el); c.tm = setTimeout(fire, window.__clay.PG.out * (window.__n7slow || 1) + 240);\n"
        "      if (a) { a.onfinish = fire; a.oncancel = fire; } else fire(); },")
    # push: no morph from the row (the page doesn't grow out of the card any more; it extrudes like every other)
    src = rep(src, "    push: (r, t) => { const tt = t || tab; setLeaving(null);", "    push: (r, t) => { if (r && r.morph) { r = Object.assign({}, r); delete r.morph; } /* r28 */ const tt = t || tab; setLeaving(null);")
    # back: the leaving page is gone when its sink ends (and at most 2.5 s later, should the event not come)
    src = rep(src, "setTimeout(() => setLeaving(l => l && l.r.key === top.key ? null : l), 360);", "setTimeout(() => setLeaving(l => l && l.r.key === top.key ? null : l), 2500);")
    src = rep(src, "<div className={cx('page', leaving.r.morph && !rm ? 'mi-morph-out' : 'leaving')} ref={leaving.r.morph && !rm ? el => MI.morphOut(el, leaving.r) : undefined} style={{ zIndex: 30 }} key={'l' + leaving.r.key}>",
        "<div className={cx('page', leaving.r.morph && !rm ? 'mi-morph-out' : 'leaving')} ref={leaving.r.morph && !rm ? el => MI.morphOut(el, leaving.r) : undefined} style={{ zIndex: 30 }} key={'l' + leaving.r.key} onAnimationEnd={e => { if (e.target === e.currentTarget) { const k = leaving.r.key; setLeaving(l => l && l.r.key === k ? null : l); } }}>")
    # every change of the visible page extrudes the new one; a tab restores its scroll first
    src = rep(src, "  useLayoutEffect(() => { if (prevTab.current && prevTab.current !== tab) MI.tabTo(screenRef.current); prevTab.current = tab; }, [tab]);",
        "  useLayoutEffect(() => { PG8.shown = tab; const c = PG8.cur; if (c && c.fired) { PG8.cur = null; if (c.to !== tab) { PG8.cur = Object.assign(c, { from: tab, fired: true, at: Date.now() }); setTabS(c.to); prevTab.current = tab; return; } }\n"
        "    if (prevTab.current && prevTab.current !== tab) { MI.tabTo(screenRef.current); PG8.restore(screenRef.current, tab); const el = PG8.top(screenRef.current); if (el && window.__clay) window.__clay.enter(el, rm ? 0 : 20); } prevTab.current = tab; }, [tab]);\n"
        "  const prevDepth = useRef(null); /* r28: push and back */\n"
        "  useLayoutEffect(() => { const n = stacks[tab].length, p = prevDepth.current; prevDepth.current = n; if (p == null || p.tab !== tab || p.n === n) { prevDepth.current = { tab, n }; return; } prevDepth.current = { tab, n };\n"
        "    const el = PG8.top(screenRef.current); if (el && window.__clay) window.__clay.enter(el, rm ? 0 : n > p.n ? 170 : 130); }, [stacks, tab]);")
    # the old tab motion: no clone sliding away, no slide in; Reduce Motion keeps its short crossfade
    src = rep(src, "const a = anim(g, rm() ? [{ opacity: 1 }, { opacity: 0 }] : [{ opacity: 1, transform: 'none' }, { opacity: 0, transform: `translateX(${-dir * 14}px)` }], { duration: rm() ? 180 : 220, easing: 'ease-out', fill: 'forwards' });",
        "if (!rm()) { g.remove(); } /* r28: the page sank in place before the change; only Reduce Motion crossfades a copy */ const a = !g.isConnected ? null : anim(g, [{ opacity: 1 }, { opacity: 0 }], { duration: 120, easing: 'linear', fill: 'forwards' });")
    src = rep(src, "if (a) a.onfinish = () => g.remove(); else g.remove(); setTimeout(() => g.isConnected && g.remove(), 420);", "if (a) a.onfinish = () => g.remove(); else if (g.isConnected) g.remove(); setTimeout(() => g.isConnected && g.remove(), 420);")
    src = rep(src, "anim(st, rm() ? [{ opacity: 0 }, { opacity: 1 }] : [{ opacity: 0, transform: `translateX(${W.tabDir * 14}px)` }, { opacity: 1, transform: 'none' }], { duration: rm() ? 200 : 340, easing: WEIGHT }); }",
        "if (rm()) anim(st, [{ opacity: 0 }, { opacity: 1 }], { duration: 120, easing: 'linear' }); /* r28: otherwise the clay extrudes the new page */ }")
    # the helpers: the visible page, and each tab's scroll
    helper = r'''
/* r28: page changes. The page in view; each tab's scroll, kept by page and restored when the tab comes back */
const PG8 = { cur: null, shown: null, scr: {},
  pages: sc => { const st = sc && sc.querySelector(':scope > .zw > .stage'); return st ? [...st.querySelectorAll(':scope > .page:not(.leaving)')].filter(p => p.style.visibility !== 'hidden') : []; },
  top: sc => { const L = PG8.pages(sc).filter(p => !p.classList.contains('under')); return L[L.length - 1] || null; },
  save: (sc, tab) => { PG8.scr[tab] = PG8.pages(sc).map(p => { const s = p.querySelector('.scroll'); return { k: p.dataset.root || p.dataset.route || '', y: s ? s.scrollTop : 0 }; }); },
  restore: (sc, tab) => { const L = PG8.scr[tab]; if (!L) return; let n = 0; const put = () => { const P = PG8.pages(sc); let left = 0; P.forEach((p, i) => { const want = L[i]; if (!want || want.k !== (p.dataset.root || p.dataset.route || '')) return; const s = p.querySelector('.scroll'); if (!s || !want.y) return; if (Math.abs(s.scrollTop - want.y) > 1) { s.scrollTop = want.y; if (Math.abs(s.scrollTop - want.y) > 1) left++; } }); if (left && n++ < 8) requestAnimationFrame(put); else if (window.__clay) window.__clay.refresh(); }; put(); }, /* the rise is measured again for the scroll put back (a page under a sheet gets no scroll event of its own) */
};
'''
    i = src.index('const RouteCtx = createContext(')
    src = src[:i] + helper.lstrip('\n') + src[i:]
    i = src.index('<style id="n7sb">')
    src = src[:i] + '<style id="n7pg">' + PAGE_CSS + '</style>\n' + src[i:]
    return src

def late(src):
    src = status(src)
    src = timechart(src)
    src = pages(src)
    src = structure(src)
    return src

def structure(src):
    # Mark: "great looking clear structure": section names say what the section is, in a few words
    src = rep(src, "<h2>What your records hint at</h2>${L.length ? '<span class=\"aside\" style=\"pointer-events:none\">a hint, not proof</span>'",
        "<h2>Patterns</h2>${L.length ? '<span class=\"aside\" style=\"pointer-events:none\">hints, not proof</span>'")
    return src
