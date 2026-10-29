// cadm.js <file> [W]: the cadence matrix. For each unit (count: Meals, volume: Water, duration: Reading, sessions: Guitar) and each change of type
// among day, week and month (both directions, 6 pairs), the routine is first given type X from its start (a fixture through
// S.updateItem, as if it had always had it), then changed to Y today through How often. Asserts, against ground truth computed
// from the db: the toast; Time > month Totals (the figure's unit, and each finished period counted by its own type and rule);
// the hero ("since ..." for a cut-short period, never "in Oct"); the item page's open period (its dates when cut short) and its
// summary; the Growth note's period word. Exit code 1 on any failure.
const { chromium } = require('playwright'); const W = +(process.argv[3] || 390);
const UNITS = [['meals', 'count', { day: 3, week: 20, month: 80 }], ['water', 'quantity', { day: 2000, week: 12000, month: 50000 }], ['reading', 'duration', { day: 30, week: 180, month: 600 }], ['guitar', 'session', { day: 1, week: 3, month: 10 }]];
const T = ['day', 'week', 'month'], LBL = { day: 'Day', week: 'Week', month: 'Month' };
const PL = { day: 'days', week: 'weeks', month: 'months' };
(async () => { const b = await chromium.launch(); let fails = 0, n = 0; const rows = [];
  for (const [id, unit, V] of UNITS) for (const X of T) for (const Y of T) { if (X === Y) continue; n++;
    const ctx = await b.newContext({ viewport: { width: W, height: W === 430 ? 932 : 844 }, deviceScaleFactor: 1, isMobile: true, hasTouch: true }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://127.0.0.1:8765/' + process.argv[2]); await p.waitForFunction(() => window.__meridian, null, { timeout: 60000 }); await p.waitForTimeout(500);
    await p.evaluate(() => window.__meridian.setScen('base')); await p.waitForTimeout(900);
    await p.evaluate(([id, X, v]) => window.__meridian.S().updateItem(id, { cadence: { type: X }, targets: [{ from: 0, cmp: 'at_least', v, cad: { type: X } }] }), [id, X, V[X]]); await p.waitForTimeout(500);
    const tap = re => p.evaluate(src => { const R = new RegExp(src); let hit = null; const w = r => { if (hit) return; for (const e of r.querySelectorAll('button,[role=button]')) if (R.test((e.textContent || '').trim())) { hit = e; return; } r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); };
      const sh = [...document.querySelectorAll('.sheet')]; if (sh.length) w(sh[sh.length - 1]); if (!hit) w(document); if (hit) hit.click(); return !!hit; }, re.source);
    const host = () => p.evaluate(() => { const h = [...document.querySelectorAll('.page:not(.under) .v3host')].pop(); const R = h.shadowRoot; const q = s => [...R.querySelectorAll(s)].map(e => e.textContent.replace(/\s+/g, ' ').trim());
      return { sub: q('.phead .sub').join(' | '), read: q('#perread .pn').join(' | ') + ' :: ' + q('#perread .pv').join(' | '), say: q('.say.lead').join(' | '), notes: q('.note').join(' || ') }; });
    await p.evaluate(id => window.__meridian.S().nav.reset('routines', [{ k: 'item', id }]), id); await p.waitForTimeout(900);
    await tap(/^How often/); await p.waitForTimeout(700); await tap(new RegExp('^' + LBL[Y] + '$')); await p.waitForTimeout(500);
    await p.evaluate(() => { const L = []; const w = r => { r.querySelectorAll('[data-act=savetg]').forEach(e => L.push(e)); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); if (L[0]) L[0].click(); });
    await p.waitForTimeout(900);
    const toast = await p.evaluate(() => [...document.querySelectorAll('.toast:not(.out)')].map(t => t.innerText.replace(/\s+/g, ' ')).join(' / '));
    await p.waitForTimeout(400); const page = await host();
    // ground truth from the db: October's periods by their own type and rule
    const truth = await p.evaluate(id => { const db = window.__meridian.db(); const it = db.byId[id]; const today = db.today; const m = monthOf(today); const out = [];
      let d = monthStart(m) - 6; for (let g = 0; g < 80 && d <= monthEnd(m); g++) { const [a, b] = periodOf(it, d); const c = cadOn(it, a).type; if (monthOf(Math.min(a + 3, b)) === m && b >= it.created && a <= today) { const ev = evalPeriod(db, it, a, b); out.push({ a, b, c, st: ev.state, open: b >= today, v: ev.v }); } d = b + 1; }
      const cur = periodOf(it, today); const nat = periodOfC(it, cadOn(it, today), today); const nEnt = (db.byItem[id] || []).filter(e => e.t != null && dayOf(e.t) >= monthStart(m) && dayOf(e.t) <= today).length;
      return { today, m, P: out, cur, nat, cad: it.cadence.type, tg: it.targets.map(t => [t.from, t.v, (t.cad || {}).type]), nEnt }; }, id).catch(e => ({ err: e.message }));
    await p.evaluate(m => window.__meridian.S().nav.reset('time', [{ k: 'month', m }]), truth.m); await p.waitForTimeout(1200);
    const tot = await p.evaluate(id => { const h = [...document.querySelectorAll('.page:not(.under) .v3host')].pop(); const e = h && h.shadowRoot.querySelector(`.cb[data-id="${id}"]`); return e ? e.textContent.replace(/\s+/g, ' ').trim() : null; }, id);
    // assertions
    const F = []; const ok = (c, msg) => { if (!c) F.push(msg); };
    ok(/starting today/.test(toast) && /Earlier periods keep the rule and the period they had/.test(toast), 'toast: ' + toast);
    ok(truth.tg && truth.tg.length >= 2 && truth.tg[truth.tg.length - 1][2] === Y && truth.tg[truth.tg.length - 1][0] === truth.today && truth.tg[0][2] === X, 'rules: ' + JSON.stringify(truth.tg));
    const fin = (truth.P || []).filter(q => !q.open && !['set-aside', 'paused', 'before', 'retired'].includes(q.st));
    const met = fin.filter(q => q.st === 'met').length; const types = [...new Set(fin.map(q => q.c))];
    ok(fin.every(q => q.c === X), 'finished October periods keep type ' + X + ': ' + JSON.stringify(fin.map(q => q.c + q.a + '-' + q.b)));
    if (tot == null) F.push('no Totals row'); else {
      ok(unit === 'quantity' ? /\d L|\d ml/.test(tot) : unit === 'duration' ? /\d (min|h)\b/.test(tot) : / times?/.test(tot), 'Totals unit: ' + tot);
      ok(!/\d+ of \d+ so far/.test(tot) || unit === 'count', 'Totals aim without unit: ' + tot);
      if (fin.length > 1 || (fin.length === 1 && X !== 'month')) { const word = types.length === 1 ? PL[types[0]] : 'periods'; const want = met ? new RegExp(`${met} of ${fin.length} ${fin.length === 1 ? word.replace(/s$/, '') : word}`) : /Not at its aim yet/;
        ok(want.test(tot), `Totals judgement want ${want} got: ${tot}`); }
      if (fin.length === 1 && X === 'month') ok(/At its aim| of /.test(tot), 'Totals one cut month: ' + tot); }
    const cut = truth.cur && truth.nat && truth.nat[0] < truth.cur[0];
    if (Y !== 'day') { ok(cut, 'the first ' + Y + ' is cut short: ' + JSON.stringify([truth.cur, truth.nat]));
      ok(!/\bin (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b/.test(page.sub) && !/this (week|month)/.test(page.sub), 'hero: ' + page.sub);
      ok(Y === 'month' ? !/October/.test(page.read) && /27/.test(page.read) : /27 Oct/.test(page.read), 'open period name: ' + page.read);
      ok(/A short first/.test(page.notes), 'short-first note missing'); }
    const g = /Logged at least once in (\d+) of its (\d+ )?finished (\w+)/.exec(page.notes);
    if (g) { const word = g[3]; const ty = word.replace(/s$/, ''); ok(word === 'periods' || word === 'period' || (ty === X && Y === X) || (ty === X) || (ty === Y && +(g[2] || 1) <= 1), 'Growth word: ' + g[0]); }
    ok(!/finished (days|weeks|months)/.test(page.say) || new RegExp('finished ' + PL[X]).test(page.say) || /finished periods/.test(page.say), 'summary: ' + page.say);
    ok(!errs.length, 'errors: ' + errs.join(' | '));
    const line = `${F.length ? 'FAIL' : 'ok  '} ${unit.padEnd(8)} ${id.padEnd(7)} ${X}->${Y}`.padEnd(36);
    console.log(line + ` | toast "${toast.replace(/^Saved /, '').replace(/ Undo$/, '').slice(0, 60)}" | totals "${tot}" | hero "${page.sub.slice(0, 70)}" | open "${page.read.slice(0, 50)}"`);
    F.forEach(f => console.log('      - ' + f)); if (F.length) fails++; rows.push({ id, X, Y, F, toast, tot, page, truth });
    await ctx.close(); }
  console.log(`cadence matrix ${n} cases, ${fails} failing`); require('fs').writeFileSync('cadm-' + W + '.json', JSON.stringify(rows, null, 1)); await b.close(); process.exit(fails ? 1 : 0); })();
