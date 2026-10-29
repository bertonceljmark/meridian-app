// ==== NEU7 BEGIN (pass 7a: the approved neumorphic look, app-wide) ====
/* pass 7a: one Ink surface, the Meridian eight, the dial hero and the clay rise. This block runs after the v3 blocks and
   before the App block, so Today's TodayScreen (block 4) and buildDB (block 1) find these at render time. */

// ---- colour: six routine hues at one lightness and chroma; night and ember are reserved (sleep, and now) ----
const NEU_HUES = [['saffron', 82], ['lagoon', 232], ['moss', 138], ['jade', 178], ['iris', 300], ['rose', 8]];
const NEU_HUE_SET = NEU_HUES.map(h => h[1]);

/* r26 polish: the strip is as tall as the card in view. While it is swiped, its height moves between the two cards' heights by
   how far the swipe has gone, so the page below never waits under a short card for the tallest one */
function NeuStripBox(props) {
  const ref = useRef(null);
  useLayoutEffect(() => { const el = ref.current; if (!el) return; let raf = 0;
    const fit = () => { raf = 0; const cards = [...el.children].filter(c => c.classList.contains('zpanel')); if (!cards.length) { el.style.height = ''; return; }
      const cs = getComputedStyle(el), pad = parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom); const x0 = cards[0].offsetLeft, sl = el.scrollLeft;
      let i = 0; while (i < cards.length - 1 && cards[i + 1].offsetLeft - x0 <= sl) i++;
      const a = cards[i], b = cards[Math.min(i + 1, cards.length - 1)]; const span = b.offsetLeft - a.offsetLeft; const f = span > 0 ? Math.max(0, Math.min(1, (sl - (a.offsetLeft - x0)) / span)) : 0;
      const H = Math.round(a.offsetHeight + (b.offsetHeight - a.offsetHeight) * f); el.style.height = H + pad + 'px';
      /* a taller neighbour peeking in fades out at the strip's foot instead of being cut flat */
      cards.forEach(c => { const cut = c.offsetHeight > H + 1; c.classList.toggle('zcut', cut); if (cut) c.style.setProperty('--zcut', H + 'px'); else c.style.removeProperty('--zcut'); }); };
    const q = () => { if (!raf) raf = requestAnimationFrame(fit); };
    /* r27 polish: keyboard focus never shifts the strip on y (it is overflow-y hidden, but focus could still scroll it 4 px), and a focused card is brought in whole, aligned like a swipe */
    const keepY = () => { if (el.scrollTop) el.scrollTop = 0; };
    const onFocus = e => { const c = e.target.closest && e.target.closest('.zpanel'); keepY(); if (!c || !el.contains(c)) return; const cards = [...el.children].filter(x => x.classList.contains('zpanel')); const x = c.offsetLeft - cards[0].offsetLeft;
      if (Math.abs(el.scrollLeft - x) > 1) el.scrollTo({ left: x, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); requestAnimationFrame(keepY); };
    el.addEventListener('focusin', onFocus);
    const onScroll = () => { keepY(); q(); }; fit(); el.addEventListener('scroll', onScroll, { passive: true }); const ro = typeof ResizeObserver === 'function' ? new ResizeObserver(q) : null; if (ro) [...el.children].forEach(c => ro.observe(c));
    return () => { el.removeEventListener('focusin', onFocus); el.removeEventListener('scroll', onScroll); if (ro) ro.disconnect(); if (raf) cancelAnimationFrame(raf); }; });
  return <div ref={ref} className={props.className} role={props.role} aria-label={props.label} data-today-cards={props.n}>{props.children}</div>;
}
/* a stored hue from before 7a (any number) is shown as the nearest of the six; the record itself is never rewritten */
const neuNear = h0 => { const h = ((+h0 % 360) + 360) % 360; let best = NEU_HUE_SET[0], bd = 999; NEU_HUE_SET.forEach(x => { const d = Math.min(Math.abs(h - x), 360 - Math.abs(h - x)); if (d < bd) { bd = d; best = x; } }); return best; };
/* r25 #10: one hue per routine, the same on every screen, and no two neighbours alike. Routines are taken in their stored
   order: each keeps the light nearest its own hue unless one of the two before it already has it; then it takes the next
   light round the six that neither has. Deterministic, so a routine reads the same colour everywhere, every day. */
const NEU_HMAP = new Map(); let NEU_KEY = ''; let NEU_ORDER = []; const NEU_WANT = new Map();
const neuCd = (a, b) => { const d = Math.abs(a - b) % 360; return Math.min(d, 360 - d); };
/* r25 #10: one light per routine, held for the session. In the Routines order (by cadence, then as stored; the loom and the list use it) any four routines in a row carry four different
   lights; a routine keeps its own light unless one of the three before it has it, then takes the nearest free one. Modules keep theirs. */
const neuAssign = items => { const key = items.map(it => it ? it.id + ':' + it.hue : '').join(','); if (key === NEU_KEY) return; NEU_KEY = key; NEU_HMAP.clear(); NEU_ADJ.clear(); NEU_WANT.clear(); NEU_ORDER = []; const prev = []; const W = 3;
  const CAD = ['day', 'week', 'month', 'everyN', 'none'], gi = it => { const i = CAD.indexOf(it && it.cadence ? it.cadence.type : 'none'); return i < 0 ? 4 : i; };
  const gone = it => it.retired != null; /* retired routines sit after the active ones, so the window counts what the list shows */
  [...items].sort((a, b) => (gone(a) - gone(b)) || (gi(a) - gi(b))).forEach(it => { if (!it || it.hue == null || it.neutral || it.id === 'sleep' || it.kind === 'module') return; const want = neuNear(it.hue); const near = prev.slice(-W);
    const h = near.includes(want) ? NEU_HUE_SET.filter(c => !near.includes(c)).sort((a, b) => neuCd(a, it.hue) - neuCd(b, it.hue) || NEU_HUE_SET.indexOf(a) - NEU_HUE_SET.indexOf(b))[0] : want;
    NEU_HMAP.set(it.id, h); NEU_WANT.set(it.id, it.hue); NEU_ORDER.push(it.id); prev.push(h); }); };
/* r26 #10: every list keeps neighbours apart. Each list a screen shows (Today's Now, Later, Settled, and the rest) reports its
   order here; consecutive routines become neighbours for the session. When two neighbours share a light, the later one moves to
   the nearest light that none of its neighbours (in any list so far, or the three either side in the Routines order) use. */
const NEU_ADJ = new Map();
const neuRepair = seq => { let ch = false; const L = seq.filter(it => it && NEU_HMAP.has(it.id));
  const link = (a, b) => { if (a === b) return; (NEU_ADJ.get(a) || NEU_ADJ.set(a, new Set()).get(a)).add(b); (NEU_ADJ.get(b) || NEU_ADJ.set(b, new Set()).get(b)).add(a); };
  for (let i = 1; i < L.length; i++) link(L[i - 1].id, L[i].id);
  const nbrs = id => { const k = NEU_ORDER.indexOf(id); return [...(NEU_ADJ.get(id) || []), ...NEU_ORDER.slice(Math.max(0, k - 3), k + 4)].filter(x => x !== id); };
  for (let pass = 0; pass < 3; pass++) { let moved = false;
    for (let i = 1; i < L.length; i++) { const b = L[i]; const hb = NEU_HMAP.get(b.id); const N = nbrs(b.id); if (!N.some(x => NEU_HMAP.get(x) === hb)) continue;
      const busy = new Set(N.map(x => NEU_HMAP.get(x))); const want = NEU_WANT.get(b.id);
      let pool = NEU_HUE_SET.filter(c => !busy.has(c));
      if (!pool.length) { const near = new Set([L[i - 1] && NEU_HMAP.get(L[i - 1].id), L[i + 1] && NEU_HMAP.get(L[i + 1].id)]); pool = NEU_HUE_SET.filter(c => !near.has(c)); }
      const h = pool.sort((x, y) => neuCd(x, want) - neuCd(y, want))[0]; if (h == null || h === hb) continue; NEU_HMAP.set(b.id, h); b.hue = h; ch = moved = true; }
    if (!moved) break; }
  /* the objects other lists hold see the same light */
  return ch; };
const neuHue = it => { if (!it || it.hue == null || it.neutral) return it ? it.hue : null; if (it.id === 'sleep') return 278;
  return NEU_HMAP.has(it.id) ? NEU_HMAP.get(it.id) : neuNear(it.hue); };
/* r25 #10: the v3 renderers mark a routine's row with its hue (attribute text for their template strings) */
const neuRH = it => { const s0 = it && (it.src || it); if (!s0 || s0.hue == null || s0.neutral || s0.kind === 'module') return ''; const h = neuHue(s0); return h == null ? '' : ` data-rh style="--rh:${h}"`; };
/* oklch(.76 .14 h) as sRGB 0..1, for the lights drawn in WebGL and canvas */
const neuRGB = h => { const L = .76, C = .14, a = C * Math.cos(h * Math.PI / 180), b = C * Math.sin(h * Math.PI / 180);
  const l_ = L + .3963377774 * a + .2158037573 * b, m_ = L - .1055613458 * a - .0638541728 * b, s_ = L - .0894841775 * a - 1.291485548 * b;
  const l = l_ ** 3, m = m_ ** 3, s = s_ ** 3; const lin = [4.0767416621 * l - 3.3077115913 * m + .2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - .3413193965 * s, -.0041960863 * l - .7034186147 * m + 1.707614701 * s];
  return lin.map(v => { v = Math.max(0, Math.min(1, v)); return v <= .0031308 ? 12.92 * v : 1.055 * Math.pow(v, 1 / 2.4) - .055; }); };
const neuFill = h => h == null ? 'var(--cream)' : `oklch(.76 .14 ${h})`;
const neuText = h => h == null ? 'var(--cream)' : `oklch(.84 .11 ${h})`;

// ---- the dial: the whole 24 hours as one raised disc. Its details live in it: one bead per routine per hour,
// tap a bead to light only that routine, drag the ring to read an hour, tap the centre (or hold inside the ring) for the day ----
const nClock = t => ((t % 1440) + 1440) % 1440;
const nAmt = (v, unit) => !unit || unit === 'ml' ? (v >= 1000 ? `${(v / 1000).toFixed(2).replace(/0+$/, '').replace(/\.$/, '')} L` : `${Math.round(v)} ml`) : `${+v.toFixed(1)} ${unit}`;
function neuDayData(db) {
  const sl = t3Sleep(db); const noNight = !!(sl.missing || sl.none); const now = db.nowMin; const wake = sl.wake; const bed = Math.max(wake + 600, sl.bed);
  const L = dayLights(db).filter(l => l.at <= now + 1);
  const logs = L.filter(l => !l.quiet).map(l => { const it = l.item ? db.byId[l.item] : null; const h = it ? neuHue(it) : null; return { l, id: l.item || l.id, it, h: it && !it.neutral && h != null ? h : null, t: l.at, dur: l.dur || 0 }; });
  const recs = L.filter(l => l.quiet).map(l => ({ l, t: l.at }));
  const by = []; logs.forEach(g => { let r = by.find(q => q.id === g.id); if (!r) by.push(r = { id: g.id, it: g.it, h: g.h, logs: [] }); r.logs.push(g); });
  return { sl, noNight, now, wake, bed, logs, recs, by, health: healthOn(db) };
}
/* a routine's total today in its own measure */
function neuFig(it, logs) {
  const n = logs.length; if (!it) return n > 1 ? `${n} times` : 'once';
  const m = it.measure;
  if (m === 'quantity') return nAmt(logs.reduce((s, g) => s + (g.l.v || 0), 0), it.unit);
  if (m === 'reps') return plural(logs.reduce((s, g) => s + (g.l.v || 0), 0), 'rep');
  if ((m === 'session' || m === 'duration' || m === 'passive') && logs.some(g => g.l.dur || g.l.v)) return fmtDur(logs.reduce((s, g) => s + (g.l.dur || g.l.v || 0), 0));
  if (m === 'count') return plural(n, it.unit || 'time');
  return n > 1 ? `${n} times` : 'once';
}
const nNight = D => D.noNight ? (!D.health ? 'Sleep not connected' : D.sl.none ? 'No sleep record' : 'Last night not in yet') : `${fmtDur(D.sl.asleep)} asleep`;
const nEsc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
function neuGeo(W) { const D = Math.max(220, Math.min(W - 64, 372)), R = D / 2; return { D, R, c: R, rg: R - 46, wr: Math.round(D * .22) }; }
function neuClusters(D, G) {
  /* r25 #4: one bead per routine per hour, all on the ring. Beads whose 44 px targets would touch are one group: it draws
     as a split bead with its count, and its single target opens a small chooser. Targets never overlap. */
  const out = [];
  D.logs.forEach(g => { const hr = Math.floor(nClock(g.t) / 60); let k = out.find(q => q.id === g.id && q.hr === hr); if (!k) out.push(k = { id: g.id, hr, h: g.h, it: g.it, logs: [] }); k.logs.push(g); });
  out.forEach(k => { k.t = k.logs.reduce((s, g) => s + nClock(g.t), 0) / k.logs.length; k.n = k.logs.length; });
  out.sort((a, b) => a.t - b.t);
  const r = G.rg, ang = t => t / 1440 * Math.PI * 2, P = t => [G.c + r * Math.sin(ang(t)), G.c - r * Math.cos(ang(t))];
  const chord = (t0, t1) => 2 * r * Math.abs(Math.sin((ang(t1) - ang(t0)) / 2));
  /* the now-sun sits on the ring; a bead keeps clear of it, moving earlier along the ring */
  const nowT = nClock(D.now), clearT = 22 / (2 * Math.PI * r) * 1440;
  out.forEach(k => { k.pt = k.t; if (Math.abs(k.t - nowT) < clearT) k.pt = nowT - clearT; });
  let grs = out.map(k => ({ m: [k], t: k.pt }));
  const mean = q => q.m.reduce((s, k) => s + k.pt, 0) / q.m.length;
  for (let guard = 0; guard < 200; guard++) { grs.sort((a, b) => a.t - b.t); let bi = -1, bd = 1e9;
    for (let i = 0; i < grs.length; i++) { const j = (i + 1) % grs.length; if (j === i) break; const d = chord(grs[i].t, grs[j].t); if (d < 44 && d < bd) { bd = d; bi = i; } }
    if (bi < 0) break; const j = (bi + 1) % grs.length; const g = { m: [...grs[bi].m, ...grs[j].m] }; g.t = mean(g); grs = grs.filter((_, k) => k !== bi && k !== j); grs.push(g); }
  grs.forEach(g => { g.m.sort((a, b) => a.t - b.t); g.p = P(g.t); g.n = g.m.reduce((s, k) => s + k.n, 0); });
  return { beads: out, groups: grs.sort((a, b) => a.t - b.t) };
}
function neuDialSvg(D, G, fresh) {
  const { R, c, rg } = G;
  const P = (t, r) => { const a = nClock(t) / 1440 * Math.PI * 2; return [c + r * Math.sin(a), c - r * Math.cos(a)]; };
  const arcP = (t0, t1, r) => { if (t1 <= t0) return ''; if (t1 - t0 >= 1439) t1 = t0 + 1439; const [x0, y0] = P(t0, r), [x1, y1] = P(t1, r); return `M${x0.toFixed(2)} ${y0.toFixed(2)}A${r} ${r} 0 ${t1 - t0 > 720 ? 1 : 0} 1 ${x1.toFixed(2)} ${y1.toFixed(2)}`; };
  const HG = {}; const hg = col => HG[col] || (HG[col] = 'nhg' + Object.keys(HG).length);
  const ro = rg + 13, ri = rg - 13;
  /* the groove: carved by plain vector shapes, never a filter (sharp at any device scale, nothing rasterised on iOS).
     Its floor, then the shadow the upper-left rim casts into it and the light on the far wall, clipped to the channel */
  let g = `<defs><radialGradient id="nbsh"><stop offset=".55" style="stop-color:rgb(var(--nSd))" stop-opacity=".6"/><stop offset="1" style="stop-color:rgb(var(--nSd))" stop-opacity="0"/></radialGradient>
    <linearGradient id="nlived" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#E8EEF8"/><stop offset="1" stop-color="#FF8F5E"/></linearGradient>
    <clipPath id="nch"><path clip-rule="evenodd" d="M${c - ro} ${c}a${ro} ${ro} 0 1 0 ${2 * ro} 0a${ro} ${ro} 0 1 0 ${-2 * ro} 0ZM${c - ri} ${c}a${ri} ${ri} 0 1 0 ${2 * ri} 0a${ri} ${ri} 0 1 0 ${-2 * ri} 0Z"/></clipPath></defs>`;
  g += `<circle cx="${c}" cy="${c}" r="${rg}" fill="none" class="dgf" stroke-width="26"/>`;
  g += `<g clip-path="url(#nch)" class="dgw">`;
  [[3.4, 9, .16], [2.6, 5, .26], [1.8, 2.4, .42]].forEach(([o, w, a]) => { g += `<circle cx="${c + o}" cy="${c + o}" r="${ro}" fill="none" stroke-width="${w}" style="stroke:rgba(var(--nSd),${a})"/><circle cx="${c + o}" cy="${c + o}" r="${ri}" fill="none" stroke-width="${w}" style="stroke:rgba(var(--nSd),${a})"/>`; });
  [[-1.6, 3, .07]].forEach(([o, w, a]) => { g += `<circle cx="${c + o}" cy="${c + o}" r="${ro}" fill="none" stroke-width="${w}" style="stroke:rgba(var(--nSl),${a})"/><circle cx="${c + o}" cy="${c + o}" r="${ri}" fill="none" stroke-width="${w}" style="stroke:rgba(var(--nSl),${a})"/>`; });
  g += `</g>`;
  for (let hh = 0; hh < 24; hh++) { const [x, y] = P(hh * 60, R - 27); g += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${hh % 3 ? 1 : 1.7}" class="dpit"/>`; }
  /* last night: cool light in the groove. A missing night is a dotted trace, never zero */
  if (!D.noNight) g += `<path class="dlvh" d="${arcP(D.sl.onset, D.wake, rg)}" stroke="var(--night)" stroke-width="15" stroke-linecap="round" fill="none" opacity=".07"/><path class="dlvh" d="${arcP(D.sl.onset, D.wake, rg)}" stroke="var(--night)" stroke-width="10" stroke-linecap="round" fill="none" opacity=".13"/><path class="dn" d="${arcP(D.sl.onset, D.wake, rg)}" stroke="var(--night)" stroke-width="7" stroke-linecap="round" fill="none"/>`;
  else g += `<path d="${arcP(D.sl.onset, D.wake, rg)}" class="dmiss" stroke-width="2" stroke-dasharray="1.5 5" stroke-linecap="round" fill="none"/>`;
  /* waking to now: warm light */
  if (D.now > D.wake) { const a = arcP(D.wake, Math.min(D.now, D.bed), rg); g += `<path class="dlvh" d="${a}" stroke="url(#nlived)" stroke-width="13" stroke-linecap="round" fill="none" opacity=".07"/><path class="dlvh" d="${a}" stroke="url(#nlived)" stroke-width="8.5" stroke-linecap="round" fill="none" opacity=".14"/><path class="dlv" d="${a}" stroke="url(#nlived)" stroke-width="5" stroke-linecap="round" fill="none"/>`; }
  /* the rest of the day: shallow pits; bedtime a small ring. Nothing expected is lit */
  for (let t = Math.max(D.now, D.wake) + 15; t < D.bed; t += 15) { const [x, y] = P(t, rg); g += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="1.3" class="dpit2"/>`; }
  { const [x, y] = P(D.bed, rg); g += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="3" fill="none" class="dbed" stroke-width="1.2"/>`; }
  D.recs.forEach(e => { const [x, y] = P(e.t, rg + 18); g += `<circle class="drec" data-hr="${Math.floor(nClock(e.t) / 60)}" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="2.6"/>`; });
  g += `<g id="dlmark" style="display:none"><path id="dlhour" d="" class="dlhour" stroke-width="22" stroke-linecap="round" fill="none"/><g id="dlknob"><circle r="15" cx="2.6" cy="3.2" fill="url(#nbsh)"/><circle r="11" class="dlk"/><circle r="11" fill="none" class="dlkr" stroke-width="1.6"/><circle r="6" class="dlkp" opacity=".25"/><circle r="3" class="dlkp"/></g></g>`;
  const { beads, groups } = neuClusters(D, G);
  const nmOf = k => k.it ? (k.it.short || k.it.name) : (k.logs[0].l.names || []).join(' and ');
  groups.forEach((q, gi) => {
    const [px, py] = q.p, x = px.toFixed(2), y = py.toFixed(2); const nw = q.m.some(k => k.logs.some(z => fresh(z.l.id)));
    const ids = q.m.map(k => k.id).join(' '), hrs = [...new Set(q.m.map(k => k.hr))].join(' ');
    const solo = q.m.length === 1, rb = solo ? (q.n > 1 ? 8.5 : 6.5) : 10.5; const col = neuFill(q.m[0].h);
    g += `<g class="db${nw ? ' new' : ''}${solo ? '' : ' grp'}" data-g="${gi}" data-ids="${nEsc(ids)}" data-hrs="${hrs}">` + (solo ? `<circle cx="${(px + 1.2).toFixed(2)}" cy="${(py + 1.7).toFixed(2)}" r="${rb + 2.6}" fill="url(#nbsh)"/><circle cx="${x}" cy="${y}" r="${(rb * 2.1).toFixed(2)}" fill="url(#${hg(col)})"/>` : '');
    if (solo) g += `<circle class="dbc" cx="${x}" cy="${y}" r="${rb}" style="fill:${col}"/>`;
    else { /* r26 #10: a group is drawn as a short fan of its routines' own beads along the ring, each in its light; the 44 pt target over it opens the chooser */
      const U = []; q.m.forEach(k => { const e = U.find(z => z.id === k.id); if (e) e.n += k.n; else U.push({ id: k.id, h: k.h, n: k.n }); });
      let th = Math.atan2(py - c, px - c); const PER = 6, rr = 6.2;
      { /* the fan keeps clear of the now-sun: if it would reach it, it slides back along the ring, and its target with it */
        const [sx, sy] = P(D.now, rg), ts = Math.atan2(sy - c, sx - c); const n0 = Math.min(PER, U.length); const span = ((n0 - 1) / 2 * 15.5 + rr + 14) / rg;
        let df = Math.atan2(Math.sin(th - ts), Math.cos(th - ts)); if (Math.abs(df) < span) { th = ts + (df < 0 ? -1 : 1) * span; q.p = [c + rg * Math.cos(th), c + rg * Math.sin(th)]; } }
      g += `<g class="dbc dfan">`;
      U.forEach((k, j) => { const row = Math.floor(j / PER), inRow = Math.min(PER, U.length - row * PER), i = j % PER; const rad = rg - row * 15; const d = 15.5 / rad;
        const a = th + (i - (inRow - 1) / 2) * d; const bx = c + rad * Math.cos(a), by = c + rad * Math.sin(a); const col = neuFill(k.h);
        g += `<circle cx="${(bx + 1).toFixed(2)}" cy="${(by + 1.4).toFixed(2)}" r="${rr + 2}" fill="url(#nbsh)"/><circle cx="${bx.toFixed(2)}" cy="${by.toFixed(2)}" r="${(rr * 2).toFixed(2)}" fill="url(#${hg(col)})"/><circle cx="${bx.toFixed(2)}" cy="${by.toFixed(2)}" r="${k.n > 1 ? rr + 1.2 : rr}" style="fill:${col}"/>`; });
      g += `</g>`; }
    if (solo && q.n > 1) g += `<text x="${x}" y="${(py + 3.4).toFixed(2)}" text-anchor="middle" class="dbn${solo ? '' : ' on-grp'}">${q.n}</text>`;
    g += `</g>`;
  });
  { const [x, y] = P(D.now, rg); g += `<circle cx="${(x + 2.4).toFixed(2)}" cy="${(y + 2.8).toFixed(2)}" r="13" fill="url(#nbsh)"/><circle class="dsunh" cx="${x.toFixed(2)}" cy="${y.toFixed(2)}" r="20" fill="url(#${hg('var(--sun)')})"/><circle cx="${x.toFixed(2)}" cy="${y.toFixed(2)}" r="9.5" fill="var(--sun)"/>`; }
  g += `<defs>${Object.entries(HG).map(([col, id]) => `<radialGradient id="${id}"><stop offset=".42" style="stop-color:${col}" stop-opacity=".5"/><stop offset=".62" style="stop-color:${col}" stop-opacity=".2"/><stop offset="1" style="stop-color:${col}" stop-opacity="0"/></radialGradient>`).join('')}</defs>`;
  const nums = [0, 3, 6, 9, 12, 15, 18, 21].map(hh => { const [x, y] = P(hh * 60, R - 13); return `<span class="dl-h${hh % 6 ? '' : ' m'}" style="left:${x.toFixed(1)}px;top:${y.toFixed(1)}px">${hh}</span>`; }).join('');
  /* the targets: real buttons over the art (the svg stays aria-hidden), one per group, 44 px, never overlapping */
  /* a group lists each routine once, with the hours it was logged in the group */
  const hh = h => String(h).padStart(2, '0') + ':00';
  /* r27: the chooser and the labels give the times it was logged (07:12, 08:40), not the hour it falls in */
  const hm = t => { const m = Math.round(t) % 1440; return String(Math.floor(m / 60)).padStart(2, '0') + ':' + String(m % 60).padStart(2, '0'); };
  const tsOf = k => (k.logs || []).map(g => nClock(g.t));
  const mrg = m => { const o = []; m.forEach(k => { const e = o.find(x => x.id === k.id); if (e) { e.n += k.n; e.hrs.push(k.hr); e.ts.push(...tsOf(k)); } else o.push({ id: k.id, h: k.h, n: k.n, hrs: [k.hr], ts: tsOf(k), nm: nmOf(k) }); }); o.forEach(e => { e.hrs.sort((a, b) => a - b); e.ts.sort((a, b) => a - b); }); return o; };
  const when = e => { const T = [...new Set(e.ts.map(hm))]; return T.length ? (T.length > 3 ? T.slice(0, 2).join(', ') + ` and ${T.length - 2} more` : T.join(', ')) : hh(e.hrs[0]); };
  const tg = groups.map((q, gi) => { const L = mrg(q.m), solo = L.length === 1, k = q.m[0]; const hs = [...new Set(q.m.map(x => x.hr))].sort((a, b) => a - b);
    const lab = solo ? `${nmOf(k)}, ${L[0].n} logged, ${when({ ...L[0], n: L[0].hrs.length > 1 ? L[0].n : L[0].n })}. Show only ${nmOf(k)}` : `${L.map(e => e.nm).join(', ')}: ${q.n} logged ${(() => { const T = q.m.flatMap(tsOf).sort((a, b) => a - b); return T.length > 1 && hm(T[0]) !== hm(T[T.length - 1]) ? `between ${hm(T[0])} and ${hm(T[T.length - 1])}` : `at ${hm(T[0] != null ? T[0] : hs[0] * 60)}`; })()}. Choose one`;
    return `<button type="button" class="dbt" data-g="${gi}" style="left:${q.p[0].toFixed(1)}px;top:${q.p[1].toFixed(1)}px" aria-label="${nEsc(lab)}"${solo ? '' : ' aria-haspopup="true"'}></button>`; }).join('');
  return { svg: `<svg viewBox="0 0 ${G.D} ${G.D}" width="${G.D}" height="${G.D}" aria-hidden="true">${g}</svg>${nums}`, tg, groups: groups.map(q => mrg(q.m).map(e => ({ ...e, when: when(e) }))), n: beads.length };
}
function neuCentre(D, U) {
  if (U.focus) {
    const r = D.by.find(q => q.id === U.focus); if (!r) { U.focus = null; return neuCentre(D, U); }
    const last = r.logs[r.logs.length - 1]; const nm = r.it ? r.it.name : (last.l.names || []).join(' and ');
    return `<span class="k" style="color:${neuText(r.h)}"><i style="background:${neuFill(r.h)}"></i>${nEsc(nm)}</span><b class="tnum">${nEsc(neuFig(r.it, r.logs))}</b><span class="s">today, last ${fmtHM(last.t)}</span><span class="hint">Tap to see the whole day</span>`;
  }
  if (U.scrub != null) {
    const hr = Math.floor(nClock(U.scrub) / 60), a = hr * 60, b = a + 60, nowM = nClock(D.now);
    const L = D.logs.filter(g => Math.floor(nClock(g.t) / 60) === hr), Rc = D.recs.filter(e => Math.floor(nClock(e.t) / 60) === hr);
    const on = nClock(D.sl.onset), wk = D.wake; const asleep = !D.noNight && (on > wk ? (a < wk || b > on) : (a < wk && b > on));
    const head = `<span class="k tnum">${String(hr).padStart(2, '0')}:00 to ${String((hr + 1) % 24).padStart(2, '0')}:00</span>`;
    let body;
    if (L.length) { const by = []; L.forEach(g => { let q = by.find(z => z.id === g.id); if (!q) by.push(q = { id: g.id, it: g.it, h: g.h, logs: [] }); q.logs.push(g); });
      body = `<span class="ls">${by.slice(0, 3).map(q => `<span class="li"><i style="background:${neuFill(q.h)}"></i>${nEsc(q.it ? (q.it.short || q.it.name) : (q.logs[0].l.names || []).join(' and '))}<em class="tnum">${nEsc(neuFig(q.it, q.logs))}</em></span>`).join('')}${by.length > 3 ? `<span class="more">and ${by.length - 3} more</span>` : ''}</span>`; }
    else if (a > nowM) body = `<span class="s">Later today</span>`;
    else if (asleep && a < wk) body = `<span class="s nt">Asleep</span>`;
    else if (hr === Math.floor(nowM / 60)) body = `<span class="s">Now, nothing yet this hour</span>`;
    else body = `<span class="s">Nothing logged</span>`;
    return head + body + (Rc.length ? `<span class="hint">${plural(Rc.length, 'record')}: ${nEsc(Rc.map(e => (e.l.names || ['Record'])[0].split(' ')[0]).join(', '))}</span>` : '');
  }
  return `<b class="tnum now">${fmtHM(D.now)}</b><span class="s">${D.logs.length ? `${D.logs.length} logged today` : 'Nothing logged yet'}</span><span class="s nt${D.noNight ? ' miss' : ''}">${nNight(D)}</span><span class="hint">${D.logs.length ? 'Tap a bead, or drag the ring' : 'What you log gathers on the ring'}</span>`;
}
function NeuDial({ db, onOpen, dayOne }) {
  const S = useStore(); const ref = useRef(null); const [W, setW] = useState(390); const U = useRef({ focus: null, scrub: null }); const seen = useRef(null);
  useLayoutEffect(() => { const el = ref.current; if (!el) return; const f = () => setW((el.closest('.scroll') || el).clientWidth || 390); f(); const ro = window.ResizeObserver ? new ResizeObserver(f) : null; ro && ro.observe(el); return () => ro && ro.disconnect(); }, []);
  const D = useMemo(() => neuDayData(db), [db]);
  const G = neuGeo(W);
  const ids = D.logs.map(g => g.l.id); const prev = seen.current;
  const fresh = id => !!prev && prev.day === db.today && !prev.ids.has(id) && !S.rm;
  const drawn = useMemo(() => neuDialSvg(D, G, fresh), [D, G.D]);
  useEffect(() => { seen.current = { day: db.today, ids: new Set(ids) }; });
  const chRef = useRef(null), applyRef = useRef(null);
  const closeCh = refocus => { const u = U.current; if (u.choose == null) return; const g0 = u.choose; u.choose = null; applyRef.current && applyRef.current(); if (refocus) { const t0 = ref.current && ref.current.querySelector(`.dbt[data-g="${g0}"]`); if (t0) t0.focus({ preventScroll: true }); } };
  const chEl = () => { if (chRef.current && chRef.current.isConnected) return chRef.current; const host = ref.current; const scr = (host && host.closest('.screen')) || document.body;
    const el = document.createElement('div'); el.className = 'dlch neu-pop'; el.setAttribute('role', 'dialog'); el.setAttribute('aria-modal', 'false'); el.hidden = true; scr.appendChild(el);
    el.addEventListener('click', e => { const co = e.target.closest('.dlco'); if (!co) return; const u = U.current; u.scrub = null; const g0 = u.choose; u.choose = null; u.focus = co.dataset.id; try { S.haptic('select', e); } catch (er) { } applyRef.current(); const t0 = ref.current && ref.current.querySelector(`.dbt[data-g="${g0}"]`); if (t0) t0.focus({ preventScroll: true }); });
    el.addEventListener('keydown', e => { const L = [...el.querySelectorAll('.dlco')], i = L.indexOf(document.activeElement);
      if (e.key === 'Escape') { e.preventDefault(); e.stopPropagation(); closeCh(true); }
      else if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); if (L.length) L[(i + (e.key === 'ArrowDown' ? 1 : -1) + L.length) % L.length].focus(); }
      else if (e.key === 'Home' || e.key === 'End') { e.preventDefault(); if (L.length) L[e.key === 'Home' ? 0 : L.length - 1].focus(); }
      else if (e.key === 'Tab' && L.length) { if (e.shiftKey && i <= 0) { e.preventDefault(); L[L.length - 1].focus(); } else if (!e.shiftKey && i === L.length - 1) { e.preventDefault(); L[0].focus(); } } });
    chRef.current = el; return el; };
  useEffect(() => () => { if (chRef.current) chRef.current.remove(); }, []);
  /* while it is open: Escape from anywhere closes it, a tap outside it closes it, and so does a scroll (the bead moves away) */
  useEffect(() => { const esc = e => { if (e.key === 'Escape' && U.current.choose != null) { e.preventDefault(); e.stopPropagation(); closeCh(true); } };
    const out = e => { if (U.current.choose == null) return; const ch = chRef.current; if (ch && ch.contains(e.target)) return; if (e.target.closest && e.target.closest('.dbt')) return; closeCh(false); };
    const scr = e => { if (U.current.choose == null) return; const ch = chRef.current; if (ch && (e.target === ch || ch.contains(e.target))) return; closeCh(false); };
    document.addEventListener('keydown', esc, true); document.addEventListener('pointerdown', out, true); document.addEventListener('scroll', scr, true);
    return () => { document.removeEventListener('keydown', esc, true); document.removeEventListener('pointerdown', out, true); document.removeEventListener('scroll', scr, true); }; }, []);
  const apply = () => { const host = ref.current; if (!host) return; const u = U.current; const hr = u.scrub != null ? Math.floor(nClock(u.scrub) / 60) : null;
    host.querySelectorAll('.db').forEach(b => b.classList.toggle('dim', (u.focus && !b.dataset.ids.split(' ').includes(u.focus)) || (hr != null && !b.dataset.hrs.split(' ').includes(String(hr)))));
    /* the group chooser (r26 #4): a popover on the screen itself, above the strip, the rows and the tab bar, never taller than
       the room it has; its rows scroll inside it. Its rows are rebuilt only when the group changes, so focus is never lost */
    { const ch = chEl(); const q = u.choose != null ? drawn.groups[u.choose] : null; ch.hidden = !q;
      if (!q) ch.dataset.g = '';
      else { const k0 = u.choose + ':' + drawn.n; if (ch.dataset.g !== k0) { ch.dataset.g = k0; ch.innerHTML = `<div class="dlch-in">${q.map(k => `<button type="button" class="dlco" data-id="${nEsc(k.id)}"><i style="background:${neuFill(k.h)}"></i><span>${nEsc(k.nm)}</span><em class="tnum">${k.when}</em></button>`).join('')}</div>`; ch.setAttribute('aria-label', `${q.length} routines logged around this hour`); }
        const b0 = host.querySelector(`.dbt[data-g="${u.choose}"]`); const par = ch.parentElement; const sr = par === document.body ? { left: 0, top: 0, width: innerWidth, height: innerHeight } : par.getBoundingClientRect();
        const br = b0 ? b0.getBoundingClientRect() : host.getBoundingClientRect(); const W0 = Math.min(240, sr.width - 32); const lft = Math.max(16, Math.min(sr.width - W0 - 16, br.left - sr.left + br.width / 2 - W0 / 2));
        const top0 = 56, bot0 = sr.height - 24, need = q.length * 44 + 8; const below = bot0 - (br.bottom - sr.top + 8), above = (br.top - sr.top - 8) - top0;
        const h = Math.max(96, Math.min(need, Math.max(below, above), Math.round(sr.height * .6))); const top = below >= h || below >= above ? br.bottom - sr.top + 8 : br.top - sr.top - 8 - h;
        ch.style.left = lft + 'px'; ch.style.top = Math.max(top0, Math.min(bot0 - h, top)) + 'px'; ch.style.width = W0 + 'px'; ch.style.height = h + 'px'; } }
    host.querySelectorAll('.drec').forEach(b => b.classList.toggle('dim', !!u.focus || (hr != null && +b.dataset.hr !== hr)));
    host.classList.toggle('focused', !!u.focus); host.classList.toggle('scrubbing', hr != null);
    const mk = host.querySelector('#dlmark'); if (!mk) return;
    if (hr != null) { const P = (t, r) => { const a = t / 1440 * Math.PI * 2; return [G.c + r * Math.sin(a), G.c - r * Math.cos(a)]; };
      const [x, y] = P(nClock(u.scrub), G.rg); mk.style.display = ''; mk.querySelector('#dlknob').setAttribute('transform', `translate(${x.toFixed(1)} ${y.toFixed(1)})`);
      const [x0, y0] = P(hr * 60, G.rg), [x1, y1] = P(hr * 60 + 60, G.rg); mk.querySelector('#dlhour').setAttribute('d', `M${x0.toFixed(1)} ${y0.toFixed(1)}A${G.rg} ${G.rg} 0 0 1 ${x1.toFixed(1)} ${y1.toFixed(1)}`);
    } else mk.style.display = 'none';
    const c = host.querySelector('[data-dial-centre]'); if (c) c.innerHTML = neuCentre(D, u); };
  applyRef.current = apply; useLayoutEffect(apply);
  // the gestures: v7's scroll-safe ring. The page scroll is never blocked up front; the disc stays pan-y
  useEffect(() => { const host = ref.current; const disc = host && host.querySelector('.dl-disc'); if (!disc) return;
    let st = null; const u = U.current;
    const minAt = e => { const b = disc.getBoundingClientRect(), R = b.width / 2, dx = e.clientX - b.left - R, dy = e.clientY - b.top - R; let a = Math.atan2(dx, -dy); if (a < 0) a += Math.PI * 2; return { m: a / (Math.PI * 2) * 1440, r: Math.hypot(dx, dy), R }; };
    const tick = () => { try { MI.tick(); } catch (er) { } };
    const scrubTo = e => { const q = minAt(e); const hr = Math.floor(q.m / 60); if (u.scrub == null || Math.floor(u.scrub / 60) !== hr) tick(); u.focus = null; u.scrub = q.m; apply(); };
    const down = e => { if (e.button > 0) return; const q = minAt(e), rg = G.rg; const touch = e.pointerType === 'touch';
      st = { id: e.pointerId, x: e.clientX, y: e.clientY, t0: performance.now(), r: q.r, rg, ring: q.r > rg - 30 && q.r < q.R - 2, bead: !!e.target.closest('.dbt'), moved: false, touch, claimed: !touch };
      /* hold opens the day only from inside the ring; on the ring a resting finger is the start of a scrub */
      if (!st.ring) st.lp = setTimeout(() => { if (st && !st.moved) { st.held = true; S.haptic('soft', e); onOpen(); } }, 520); };
    const move = e => { if (!st) return; if (!st.moved && Math.hypot(e.clientX - st.x, e.clientY - st.y) > 6) { st.moved = true; clearTimeout(st.lp); if (st.ring && st.claimed) try { disc.setPointerCapture(st.id); } catch (er) { } } if (st.ring && st.moved && st.claimed) scrubTo(e); };
    /* touch decides once, on the finger's first real move, and only for a finger that landed on the groove:
       along the tangent where it runs across the screen (top and bottom) scrubs; on the sides only after a 160 ms press;
       anything else scrolls the page and leaves the dial exactly as it was */
    const tmove = e => { if (!st || !st.touch || e.touches.length !== 1) return; if (st.claimed) { if (e.cancelable) e.preventDefault(); return; } if (st.decided) return;
      const t = e.touches[0], dx = t.clientX - st.x, dy = t.clientY - st.y, d = Math.hypot(dx, dy); if (d < 3) return; st.decided = true;
      if (!st.ring || Math.abs(st.r - st.rg) > 24) return;
      const b = disc.getBoundingClientRect(), ux = (st.x - b.left - b.width / 2) / st.r, uy = (st.y - b.top - b.height / 2) / st.r, tx = -uy, ty = ux;
      const along = Math.abs(dx * tx + dy * ty), across = Math.abs(dx * ux + dy * uy);
      const tangential = along > across * 1.3, crossTangent = Math.abs(tx) > .5, rested = performance.now() - st.t0 >= 160;
      if (tangential && (crossTangent || rested) && e.cancelable) { e.preventDefault(); st.claimed = true; st.moved = true; clearTimeout(st.lp); try { disc.setPointerCapture(st.id); } catch (er) { } scrubTo(t); } };
    const up = e => { if (!st) return; clearTimeout(st.lp); if (st.ring && !st.bead && !st.moved && !st.held) { const q = minAt(e); u.focus = null; u.scrub = q.m; tick(); apply(); } disc._swallow = st.held || st.moved; st = null; };
    const cancel = () => { if (st) clearTimeout(st.lp); st = null; };
    const click = e => { if (disc._swallow) { e.stopPropagation(); e.preventDefault(); disc._swallow = false; return; }

      const b = e.target.closest('.dbt'); if (b) { const q = drawn.groups[+b.dataset.g]; u.scrub = null; S.haptic('select', e);
        if (q.length === 1) { u.choose = null; u.focus = u.focus === q[0].id ? null : q[0].id; } else { u.choose = u.choose === +b.dataset.g ? null : +b.dataset.g; u.focus = null; }
        apply(); if (u.choose != null) { const f = chRef.current && chRef.current.querySelector('.dlco'); if (f) f.focus({ preventScroll: true }); } return; }
      if (u.choose != null) { u.choose = null; apply(); return; }
      if (e.target.closest('[data-dial-well]')) { if (u.focus || u.scrub != null) { u.focus = null; u.scrub = null; apply(); } else onOpen(); } };
    const key = e => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); u.focus = null; u.scrub = nClock((u.scrub == null ? Math.floor(db.nowMin / 60) * 60 : Math.floor(u.scrub / 60) * 60) + (e.key === 'ArrowRight' ? 60 : -60)) + 30; apply(); }
      else if (e.key === 'Escape' && u.choose != null) { e.stopPropagation(); closeCh(true); }
      else if (e.key === 'Escape' && (u.focus || u.scrub != null)) { u.focus = null; u.scrub = null; apply(); } };
    disc.addEventListener('pointerdown', down); disc.addEventListener('pointermove', move); disc.addEventListener('pointerup', up); disc.addEventListener('pointercancel', cancel);
    disc.addEventListener('touchmove', tmove, { passive: false }); disc.addEventListener('click', click, true); disc.addEventListener('keydown', key);
    return () => { disc.removeEventListener('pointerdown', down); disc.removeEventListener('pointermove', move); disc.removeEventListener('pointerup', up); disc.removeEventListener('pointercancel', cancel); disc.removeEventListener('touchmove', tmove); disc.removeEventListener('click', click, true); disc.removeEventListener('keydown', key); };
  }, [G.D, D, onOpen]);
  const n = D.logs.length;
  const label = `Your day as a dial: ${plural(n, 'thing')} logged today. ${nNight(D)}. Tap a bead to show one routine, drag the ring to read an hour, tap the centre for the whole day`;
  return <div className="hero-dial" ref={ref} data-today-arc data-today-dial data-arc-marks={drawn.n} data-arc-recs={D.recs.length} role="group" aria-label={label} style={{ height: G.D + 14 }}>
    <div className="dl-disc" tabIndex={0} style={{ width: G.D, height: G.D }} aria-label="Drag around the ring, or use the arrow keys, to read an hour">
      <div className="dl-art" dangerouslySetInnerHTML={{ __html: drawn.svg }} />
      <div className="dl-tg" dangerouslySetInnerHTML={{ __html: drawn.tg }} />
      <button className="dl-well" data-dial-well style={{ left: G.c - G.wr, top: G.c - G.wr, width: G.wr * 2, height: G.wr * 2 }} aria-label={`${plural(n, 'thing')} logged today. Open the day`}><span data-dial-centre aria-live="polite" /></button>
    </div>
  </div>;
}
// ==== NEU7 DIAL END ====

// ---- the clay rise (tilt-scroll v8, as approved): every point of a row, card or well has its own height, from its distance
// to the visible clip edge of its scroll area. Flat (printed only) at the edge, risen past the band, never above full height.
// Walls show the thickness, the moat the displaced clay while it rises; wells do the reverse. Native scroll, no transforms,
// JS writes only custom properties on each item's plate. Keys rise as one (their own shadow scales by --rk). ----
const CLAY = (() => {
  const P = { band: 80, depth: 1.4, NW: 7, pop: .04, walls: true, moat: false, pad: 56 }; /* r28: no moat (Mark's call on the 7c preview) */ /* tilt v8 defaults, kept as params */
  const RAISED = ['.t3 .zrow', '.t3 .zsug', '.t3 .zdateline', '.t3 .dl-disc', '.t3 .zpanel', '.t3 .ztok', '.list', '.card', '.n7-plate', '.ys-card']; /* r28: the strip's panels and Later's routines are plates */
  const WELLS = ['.n7-well'];
  const KEYS = ['.t3 .zk-round', '.t3 .zk-seg', '.t3 .zk-pill', '.t3 .zk-word', '.t3 .zamt .zkey', '.t3 .ztk', '.t3 .zchip', '.t3 .zib', '.t3 .zaddbtn', '.t3 .zsb > button', '.t3 .zx', '.t3 .zfoot button', '.t3 .zmore', '.btn', '.chip', '.preset', '.iconbtn', '.n7-key'];
  /* the v3 screens draw into shadow roots; their forms are named in their own stylesheet */
  const SH_RAISED = ['.n7-plate', '.ledger .ln', '.set .li', '.tl .li', '.kvs', '.staff .sf', '.toc .tc', '.idx .tk', '.pats .pt', '.recs .rec', '.combs .cb', '.figs .fg', '.n7p']; /* r28: one plate per item, not plateaus of rows */
  const SH_WELLS = ['.n7-well', '.notif', '.dev', '.n7w'];
  const SH_KEYS = ['.btn', '.key', '.chip', '.sw', '.seg', '.search', '.n7-key', '.go', '.ib', '.foot button', '.sh .close'];
  const sR = RAISED.join(','), sW = WELLS.join(','), sK = KEYS.join(','), shR = SH_RAISED.join(','), shW = SH_WELLS.join(','), shK = SH_KEYS.join(',');
  const NONE = 'linear-gradient(transparent,transparent)';
  const clamp01 = v => v < 0 ? 0 : v > 1 ? 1 : v; const smooth = t => t * t * (3 - 2 * t);
  const a3 = v => Math.round(v * 1000) / 1000;
  /* r25: the text in the rise band never drops below AA. t3 (.62 cream) needs .56 effective on the lightest plate face, so content keeps at least .92 */
  const TA0 = .92;
  const reduced = () => prefersReduced() || !!document.querySelector('[data-screen].rm');
  const areas = new Map(); let mo = null, ticking = false; const popping = [];
  // a scroll area's visible clip edges, in its own coordinates. The top is under the status bar, or under a solid bar;
  // the bottom is the top of the dock, the live bar or a sheet's foot, whichever covers it first
  function edges(A) {
    const el = A.el, r = el.getBoundingClientRect(); const scr = el.closest('[data-screen]'); const sr = scr ? scr.getBoundingClientRect() : { top: 0, bottom: innerHeight };
    let top = r.top, bot = Math.min(r.bottom, sr.bottom);
    const vv = window.visualViewport; if (vv) { top = Math.max(top, vv.offsetTop); bot = Math.min(bot, vv.offsetTop + vv.height); }
    if (A.sheet) { const foot = A.sheet.querySelector('.sheet-foot'); if (foot) bot = Math.min(bot, foot.getBoundingClientRect().top); }
    else if (scr) {
      /* r28: no drawn status bar; the real one's band (.n7sb, env(safe-area-inset-top), 0 in a browser tab) is the top edge */
      const st = scr.querySelector(':scope > .n7sb'); if (st) top = Math.max(top, st.getBoundingClientRect().bottom);
      const page = el.closest('.page'); const bar = page && page.querySelector(':scope > .navbar.solid, :scope > .rootbar.solid, :scope > .v3bar.on'); if (bar) top = Math.max(top, bar.getBoundingClientRect().bottom);
      const dock = scr.querySelector('.tabbar'); if (dock) bot = Math.min(bot, dock.getBoundingClientRect().top - 2);
      const lb = scr.querySelector('.livebar'); if (lb) bot = Math.min(bot, lb.getBoundingClientRect().top - 2);
    }
    /* r27: in the area's own (unscaled) pixels: a page under a sheet is scaled to .955, and its plates must not read as moved */
    const k = el.offsetHeight ? r.height / el.offsetHeight : 1;
    return { E0: (top - r.top) / k, E1: (bot - r.top) / k };
  }
  function plateFor(el, well) {
    let p = el.firstElementChild; if (p && p.classList.contains('n7c')) return p;
    p = document.createElement('div'); p.className = 'n7c' + (well ? ' w' : ''); p.setAttribute('aria-hidden', 'true');
    let h = P.moat ? '<i class="mt"></i>' : '';
    if (well) { h += '<i class="ins"></i>'; for (let i = 1; i <= P.NW; i++) h += `<i class="iw" style="--i:${i};box-shadow:inset ${(i * .35).toFixed(2)}px ${i}px 0 var(--nWallIn);-webkit-mask-image:var(--w${i});mask-image:var(--w${i})"></i>`; }
    else { h += '<i class="sh"></i><i class="shc"></i>'; for (let i = P.NW; i >= 1; i--) h += `<i class="wl" style="--i:${i};top:${i}px;bottom:-${i}px;left:${(i * .35).toFixed(2)}px;right:-${(i * .35).toFixed(2)}px;-webkit-mask-image:var(--w${i});mask-image:var(--w${i})"></i>`; h += '<i class="fc"></i><i class="fl"></i>'; }
    p.innerHTML = h; el.insertBefore(p, el.firstChild); return p;
  }
  function collect(A) {
    const el = A.el; const out = []; const seen = new Set();
    const push = (e, kind) => { if (seen.has(e)) return; seen.add(e); out.push({ el: e, kind }); };
    el.querySelectorAll(sR).forEach(e => push(e, 'r')); el.querySelectorAll(sW).forEach(e => push(e, 'w')); el.querySelectorAll(sK).forEach(e => push(e, 'k'));
    el.querySelectorAll('.v3host').forEach(h => { const R = h.shadowRoot; if (!R) return; if (!A.roots.has(R)) { A.roots.add(R); A.mo.observe(R, { childList: true, subtree: true }); }
      R.querySelectorAll(shR).forEach(e => push(e, 'r')); R.querySelectorAll(shW).forEach(e => push(e, 'w')); R.querySelectorAll(shK).forEach(e => push(e, 'k')); });
    return out;
  }
  function measure(A) {
    A.dirty = false; const el = A.el; const r = el.getBoundingClientRect(), st = el.scrollTop; const k = el.offsetHeight ? r.height / el.offsetHeight || 1 : 1; /* r27: unscaled */
    const list = collect(A); const old = new Map(A.items.map(it => [it.el, it]));
    A.items = list.map(({ el: e, kind }) => { if (e.closest('.n7-noclay')) return null; const b = e.getBoundingClientRect(); if (!b.height) return null;
      const it = old.get(e) || { el: e, kind, last: {}, armed: true };
      it.kind = kind; it.top = (b.top - r.top) / k + st; it.h = b.height / k; it.small = kind === 'k';
      if (kind !== 'k') { const p = plateFor(e, kind === 'w'); if (it.p !== p) { it.p = p; it.last = {}; } e.classList.add('n7cl'); if (getComputedStyle(e).position === 'static') e.classList.add('n7rel'); }
      return it; }).filter(Boolean);
    old.forEach((it, e) => { if (!A.items.includes(it)) { /* gone or no longer a form */ } });
  }
  function setP(it, k, v) { if (it.last[k] !== v) { it.last[k] = v; ((k === '--ta' || k === '--rk') ? it.el : (it.p || it.el)).style.setProperty(k, v); } }
  function frame(A) {
    if (A.dirty) measure(A);
    const el = A.el; if (!el.isConnected) { detach(el); return; }
    const st = el.scrollTop, max = Math.max(0, el.scrollHeight - el.clientHeight); const { E0, E1 } = edges(A);
    const B = P.band, rmo = reduced();
    /* the band reaches its full width only once content has passed under an edge: at rest at the top nothing has, so the
       first screen stands at full height; at the very end of a list the bottom stands up too */
    const bT = Math.max(1, Math.min(B, st)), bB = Math.max(1, Math.min(B, max - st));
    const hAt = y => { const d0 = y - E0, d1 = E1 - y; if (d0 <= 1 || d1 <= 1) return 0; const t = Math.min((d0 - 1) / bT, (d1 - 1) / bB); return t >= 1 ? 1 : smooth(clamp01(t)); };
    A.hAt = hAt; A.E = { E0, E1, bT, bB };
    const grad = (y0, from, to, f, shift) => {
      const span = to - from, n = Math.max(4, Math.min(32, Math.ceil(span / 6))), ys = [];
      for (let i = 0; i <= n; i++) ys.push(from + span * i / n);
      const sh = shift || 0;
      [E0 - 1, E0, E0 + 1, E0 + 1 + bT, E1 - 1 - bB, E1 - 1, E1, E1 + 1].forEach(e => { [e, e + sh].forEach(v => { const ly = v - y0; if (ly > from && ly < to) ys.push(ly); }); });
      ys.sort((p, q) => p - q); let s = 'linear-gradient(180deg';
      for (let j = 0; j < ys.length; j++) s += ',rgba(0,0,0,' + a3(f(y0 + ys[j])) + ') ' + (Math.round((ys[j] - from) * 100) / 100) + 'px';
      return s + ')'; };
    const nW = it => { const n = Math.round(5 * P.depth); return it.kind === 'w' ? Math.min(n, Math.floor(it.h * .15)) : n; };
    for (const it of A.items) {
      const y0 = it.top - st, y1 = y0 + it.h; it.y0 = y0; it.y1 = y1;
      if (y1 < E0 - P.pad - 10 || y0 > E1 + P.pad + 10) { it.armed = true; it.wasFull = false; continue; }
      const h0 = hAt(y0), h1 = hAt(y1), hm = hAt((y0 + y1) / 2);
      const full = h0 > .999 && h1 > .999 && hm > .999;
      if (it.kind === 'k') { /* a key rises as one, from the height under its middle */ setP(it, '--rk', full ? '1' : String(a3(hm))); continue; }
      if (!full && Math.min(h0, h1, hm) < .3) it.armed = true;
      if (P.pop > 0 && full && it.wasFull === false && it.armed && !rmo) { it.armed = false; startPop(it); }
      it.wasFull = full;
      const near = (y0 - E0) < bT + P.pad || (E1 - y1) < bB + P.pad; const hav = (h0 + h1 + 2 * hm) / 4;
      setP(it, '--n7full', full ? '1' : '0'); it.p.classList.toggle('full', full && !near);
      // walls: layer i shows where h * N >= i, so the visible wall is about h x 5 x depth px and tapers to 0 at the edge
      const n = P.walls ? nW(it) : 0;
      for (let i = 1; i <= P.NW; i++) {
        if (i > n) { setP(it, '--w' + i, NONE); continue; }
        if (full && !near) { setP(it, '--w' + i, 'none'); continue; }
        const off = it.kind === 'w' ? 0 : i;
        setP(it, '--w' + i, grad(y0 + off, 0, it.h, y => clamp01(hAt(y - off) * n - (i - 1) - .02), off));
      }
      // the moat: displaced clay around a rising item, 0 at the edge and 0 once fully up
      const m = P.moat ? clamp01(4 * (full ? 1 : hav) * (1 - (full ? 1 : hav))) : 0;
      if (P.moat) setP(it, '--mm', m < .002 ? NONE : grad(y0 - 40, 0, it.h + 80, y => m * hAt(y)));
      if (it.kind === 'w') { setP(it, '--m', full ? 'none' : grad(y0, 0, it.h, hAt)); continue; }
      if (full) { setP(it, '--m', near ? grad(y0 - P.pad, 0, it.h + 2 * P.pad, hAt) : 'none'); setP(it, '--mc', NONE); setP(it, '--mf', NONE); setP(it, '--ta', '1'); continue; }
      setP(it, '--m', grad(y0 - P.pad, 0, it.h + 2 * P.pad, hAt));
      setP(it, '--mc', grad(y0 - P.pad, 0, it.h + 2 * P.pad, y => { const h = hAt(y); return Math.min(1, h * 2.2) * (1 - h * .6); }));
      setP(it, '--mf', grad(y0 - 1, 0, it.h + 2, y => 1 - Math.min(1, hAt(y) * 1.3)));
      setP(it, '--ta', String(a3(TA0 + (1 - TA0) * Math.max(hm, (h0 + h1) / 2))));
    }
  }
  // the gentle pop: a soft spring (response .45 s, damping .7) once per entry; it only deepens the shadow
  const W0 = 2 * Math.PI / .45, Z = .7, WD = W0 * Math.sqrt(1 - Z * Z); const TPEAK = Math.atan(Math.sqrt(1 - Z * Z) / Z) / WD;
  const NORM = Math.exp(-Z * W0 * TPEAK) * Math.sin(WD * TPEAK); const TEND = Math.log(200) / (Z * W0);
  const springAt = t => t >= TEND ? 0 : P.pop * Math.exp(-Z * W0 * t) * Math.sin(WD * t) / NORM;
  let popT = false;
  function startPop(it) { it.popT0 = performance.now(); if (!popping.includes(it)) popping.push(it); if (!popT) { popT = true; requestAnimationFrame(popTick); } }
  function popTick(now) { for (let i = popping.length - 1; i >= 0; i--) { const it = popping[i]; const ok = it.wasFull && !reduced(); const v = ok ? springAt((now - it.popT0) / 1000) : 0; setP(it, '--pop', String(a3(v))); if (!ok || v === 0) popping.splice(i, 1); } if (popping.length) requestAnimationFrame(popTick); else popT = false; }
  function schedule() { if (ticking) return; ticking = true; requestAnimationFrame(() => { ticking = false; areas.forEach(A => { if (A.queued) { A.queued = false; try { frame(A); } catch (e) { console.warn('clay', e); } } }); }); }
  function attach(el) {
    if (areas.has(el)) return; const A = { el, items: [], dirty: true, queued: true, roots: new Set(), sheet: el.closest('.sheet') };
    A.onScroll = () => { A.queued = true; schedule(); }; A.mark = () => { A.dirty = true; A.queued = true; schedule(); };
    A.mo = new MutationObserver(muts => { if (muts.some(m => [...m.addedNodes, ...m.removedNodes].some(n => n.nodeType === 1 && !(n.classList && n.classList.contains('n7c'))))) A.mark(); });
    A.mo.observe(el, { childList: true, subtree: true });
    A.ro = window.ResizeObserver ? new ResizeObserver(A.mark) : null; if (A.ro) { A.ro.observe(el); [...el.children].slice(0, 16).forEach(c => { if (!c.classList.contains('n7c')) A.ro.observe(c); }); } /* r28: every block of the area, not only the first: Today's head is first, and the rows under it moved unseen */
    el.addEventListener('scroll', A.onScroll, { passive: true }); areas.set(el, A); schedule();
  }
  function detach(el) { const A = areas.get(el); if (!A) return; A.mo.disconnect(); A.ro && A.ro.disconnect(); el.removeEventListener('scroll', A.onScroll); areas.delete(el); }
  function scan(root) { (root || document).querySelectorAll('[data-screen] .scroll, [data-screen] .sheet-body').forEach(attach); areas.forEach((A, el) => { if (!el.isConnected) detach(el); }); }
  function start() {
    if (mo) return; scan();
    mo = new MutationObserver(muts => { let any = false; for (const m of muts) { for (const n of m.addedNodes) if (n.nodeType === 1 && !(n.classList && n.classList.contains('n7c'))) { any = true; break; } for (const n of m.removedNodes) if (n.nodeType === 1 && (n.matches('.sheet, .scrim') || n.querySelector('.sheet'))) any = true; } /* r28: a sheet closing measures the page it uncovers again */ if (any) { scan(); areas.forEach(A => { A.dirty = true; A.queued = true; }); schedule(); } });
    const root = document.getElementById('root'); if (root) mo.observe(root, { childList: true, subtree: true });
    const all = () => { areas.forEach(A => { A.dirty = true; A.queued = true; }); schedule(); };
    window.addEventListener('resize', all); if (window.visualViewport) { visualViewport.addEventListener('resize', all); visualViewport.addEventListener('scroll', all); }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(all);
    /* bars that turn solid move the top edge; the dock, live bar and toasts come and go */
    setInterval(() => { areas.forEach(A => { if (A.el.isConnected && A.el.offsetParent) { A.queued = true; } }); schedule(); }, 700);
    /* r28: a bar that grows in (the v3 bar, a solid navbar) moves the top edge after the scroll that showed it, and the page under a sheet scales after it opens: measure again when either settles */
    const barEnd = e => { const t = e.target; if (t && t.classList && (t.classList.contains('v3bar') || t.classList.contains('navbar') || t.classList.contains('rootbar') || (/^(transform|scale|translate)$/.test(e.propertyName || e.animationName ? (e.propertyName || 'transform') : '') && [...areas.keys()].some(el => el !== t && t.contains(el))))) all(); };
    document.addEventListener('transitionend', barEnd, true); document.addEventListener('animationend', barEnd, true);
  }
  // r28: page changes. The outgoing page sinks into the surface (every height to 0, printed only, 160 ms, ease-in) as its
  // content fades; the incoming page's printed layer is there at once, then the forms in view extrude in reading order,
  // 35 ms apart (300 ms at most), each over 260 ms with the same height system as the rise (walls and shadows grow, no
  // transform on text). Forms out of view are simply up. Only custom properties animate; a new change cancels the last.
  const PG = { out: 160, rise: 260, step: 35, cap: 300 }; let runs = []; const SLOW = () => window.__n7slow || 1; /* a film of the change (frame strips) slows it, nothing else */
  const drop = a => { const j = runs.indexOf(a); if (j >= 0) runs.splice(j, 1); };
  function cancel() { runs.slice().forEach(a => { try { a.cancel(); } catch (e) { } }); runs = []; }
  function formsIn(page) { const out = []; const H = innerHeight; const top = []; const sel = [sR, sW, sK].join(','), shSel = [shR, shW, shK].join(',');
    const add = e => { if (e.closest('.n7-noclay')) return; const r = e.getBoundingClientRect(); if (!r.height || r.bottom < 0 || r.top > H) return; out.push({ e, y: Math.round(r.top / 12), x: r.left }); };
    page.querySelectorAll(sel).forEach(add); page.querySelectorAll('.v3host').forEach(h => h.shadowRoot && h.shadowRoot.querySelectorAll(shSel).forEach(add));
    out.sort((a, b) => a.y - b.y || a.x - b.x); out.forEach(o => { if (!out.some(p => p !== o && p.e.contains(o.e))) top.push(o.e); }); return top; }
  function enter(page, delay = 0) {
    if (!page || !page.animate) return; if (page._n7out) { try { page._n7out.cancel(); } catch (e) { } page._n7out = null; }
    if (reduced()) { const a = page.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 120 * SLOW(), delay: delay * SLOW(), easing: 'linear', fill: 'backwards' }); runs.push(a); a.onfinish = () => drop(a); return; }
    page.style.setProperty('--g', '0'); let tries = 0;
    const go = () => { const L = formsIn(page); if (!L.length && tries++ < 6) { requestAnimationFrame(go); return; }
      L.forEach((e, i) => { const a = e.animate([{ '--g': 0 }, { '--g': 1 }], { duration: PG.rise * SLOW(), delay: (delay + Math.min(PG.cap, i * PG.step)) * SLOW(), easing: 'cubic-bezier(.22,.7,.3,1)', fill: 'backwards' }); runs.push(a); a.onfinish = a.oncancel = () => drop(a); });
      page.style.removeProperty('--g'); };
    requestAnimationFrame(() => requestAnimationFrame(go));
  }
  function leave(el) {
    if (!el || !el.animate) return null; const rm = reduced();
    const a = el.animate(rm ? [{ opacity: 1 }, { opacity: 0 }] : [{ '--g': 1, opacity: 1 }, { '--g': 0, opacity: 0 }], { duration: (rm ? 120 : PG.out) * SLOW(), easing: rm ? 'linear' : 'cubic-bezier(.4,0,1,1)', fill: 'forwards' });
    el._n7out = a; return a;
  }
  return { P, PG, start, attach, enter, leave, cancel, refresh: () => { areas.forEach(A => { A.dirty = true; A.queued = true; }); schedule(); }, areas, frame };
})();
window.__clay = CLAY;
if (document.readyState !== 'loading') setTimeout(() => CLAY.start(), 0); else document.addEventListener('DOMContentLoaded', () => CLAY.start());
// ==== NEU7 END ====
