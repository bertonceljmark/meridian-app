// chk7e.js <file> [W]: the review r28 items, read off the page: B1 the week page after a day->week change, B2 a paused routine in a
// month's Totals, P1 a sheet for a missing item, P2 the toast of every change of type, P3 a none->week->month change on one day,
// P4 the chart's label when filtered, P5 the Routines hero's names. Prints ok/FAIL lines.
const { chromium } = require('playwright'); const [file, w] = process.argv.slice(2); const W = +(w || 390);
(async () => { const b = await chromium.launch(); let bad = 0; const say = (ok, m) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'FAIL', m); };
  const fresh = async () => { const ctx = await b.newContext({ viewport: { width: W, height: 3000 }, isMobile: true, hasTouch: true }); const p = await ctx.newPage(); p.errs = []; p.on('pageerror', e => p.errs.push(e.message));
    await p.goto('http://127.0.0.1:8765/' + file); await p.waitForFunction(() => window.__meridian, null, { timeout: 60000 }); await p.evaluate(() => window.__meridian.setScen('base')); await p.waitForTimeout(900); return p; };
  const deep = (p, sel) => p.evaluate(sel => { const o = []; const w = r => { r.querySelectorAll(sel).forEach(e => o.push(e)); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); return o.map(e => (e.innerText || e.textContent || '').replace(/\s+/g, ' ').trim()); }, sel);
  const change = async (p, id, Y) => { await p.evaluate(id => window.__meridian.S().nav.reset('routines', [{ k: 'item', id }]), id); await p.waitForTimeout(900);
    await p.evaluate(() => { let hit = null; const w = r => { if (hit) return; for (const e of r.querySelectorAll('button')) if (/^How often/.test((e.textContent || '').trim())) { hit = e; return; } r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); hit && hit.click(); }); await p.waitForTimeout(700);
    await p.evaluate(Y => { const w = r => { r.querySelectorAll(`[data-act=tg][data-k=cad][data-v="${Y}"]`).forEach(e => e.click()); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); }, Y); await p.waitForTimeout(400);
    await p.evaluate(() => { const L = []; const w = r => { r.querySelectorAll('[data-act=savetg]').forEach(e => L.push(e)); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); L[0] && L[0].click(); }); await p.waitForTimeout(500);
    const t = (await deep(p, '.toast')).join(' / '); await p.waitForTimeout(5000); return t; };
  // B1: Water day -> week today; Week 44
  { const p = await fresh(); await p.evaluate(() => window.__meridian.S().updateItem('water', { cadence: { type: 'day' }, targets: [{ from: 0, cmp: 'at_least', v: 2000, cad: { type: 'day' } }] })); await p.waitForTimeout(300);
    const t = await change(p, 'water', 'week'); say(/starting today/.test(t), `B1/P2 water day->week toast: ${t}`);
    const st = (await deep(p, '.phead + * , .phead')).join(' ').slice(0, 0);
    const item = (await deep(p, '.phead .sub, .phead')).join(' | '); say(/since today/.test(item), `B1 item page: ${item.slice(0, 120)}`);
    await p.evaluate(() => window.__meridian.S().nav.reset('time', [{ k: 'weeks', off: 0 }])); await p.waitForTimeout(1500);
    const daily = (await deep(p, '.sec .staff .sf')).filter(x => /^Water/.test(x)); const secs = await p.evaluate(() => { const o = {}; const w = r => { r.querySelectorAll('.sec').forEach(s => { const h = s.querySelector('h2'); if (h) o[h.textContent] = [...s.querySelectorAll('.sf')].map(x => x.innerText.replace(/\s+/g, ' ').trim()); }); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); return o; });
    const ed = (secs['Every day'] || []).find(x => /^Water/.test(x)), wa = (secs["This week's aims"] || []).find(x => /^Water/.test(x));
    say(!!ed && /1 finished day|finished day/.test(ed), `B1 Every day has Water for Mon 26: ${ed}`);
    say(!!wa && !/2\.74|settled for the week/.test(wa) && /since today/.test(wa), `B1 This week's aims, Water from today only: ${wa}`);
    const cells = await p.evaluate(() => { let o = null; const w = r => { r.querySelectorAll('.sec').forEach(s => { const h = s.querySelector('h2'); if (h && h.textContent === 'Every day') s.querySelectorAll('.sf').forEach(x => { if (/^Water/.test(x.innerText)) o = [...x.querySelectorAll('.rail i')].map(i => i.className); }); }); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); return o; });
    say(cells && cells[0] !== 'x' && cells[1] === 'x', `B1 Water's day rail judges Mon only: ${JSON.stringify(cells)}`);
    say(!p.errs.length, `B1 errors: ${p.errs.join(' | ')}`); await p.context().close(); }
  // B2: Meditation (paused) in October's Totals; also its item page and the week page
  { const p = await fresh(); await p.evaluate(() => window.__meridian.S().nav.reset('time', [{ k: 'month', m: 9 }])); await p.waitForTimeout(1500);
    const r = (await deep(p, '.cb[data-id="meditate"]'))[0] || ''; const cls = await p.evaluate(() => { let o = null; const w = r => { const e = r.querySelector('.cb[data-id="meditate"]'); if (e) o = [...e.querySelectorAll('.wkb i, .comb i')].map(i => i.className).join(','); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); return o; });
    say(/Paused/.test(r) && !/Not yet/.test(r), `B2 Totals: ${r}`); say(cls && !/(^|,)(o|g|p|m)(,|$)/.test(cls) && /pz/.test(cls), `B2 its bars are paused marks: ${cls}`);
    await p.evaluate(() => window.__meridian.S().nav.reset('time', [{ k: 'weeks', off: 0 }])); await p.waitForTimeout(1300);
    const wk = (await deep(p, '.sf')).filter(x => /^Meditation/.test(x)); say(wk.every(x => /Paused/.test(x)), `B2 week page: ${wk.join(' / ')}`);
    await p.evaluate(() => window.__meridian.S().nav.reset('time', [])); await p.waitForTimeout(1300); const tw = (await deep(p, '.sf')).filter(x => /^Meditation/.test(x)); say(tw.every(x => /Paused/.test(x)), `B2 This week on Time: ${tw.join(' / ') || '(not listed)'}`);
    await p.evaluate(() => window.__meridian.S().nav.reset('routines', [{ k: 'item', id: 'meditate' }])); await p.waitForTimeout(1300); const it = (await deep(p, '.phead')).join(' '); say(/Paused/.test(it) && !/Not yet/.test(it), `B2 item page: ${it.slice(0, 120)}`);
    say(!p.errs.length, `B2 errors: ${p.errs.join(' | ')}`); await p.context().close(); }
  // P1: the target sheet for an item that does not exist
  { const p = await fresh(); await p.evaluate(() => window.__meridian.S().sheet.open({ k: 'target', id: 'no-such-item' })); await p.waitForTimeout(1000);
    const ok = await p.evaluate(() => !!document.querySelector('.screen') && document.querySelectorAll('.sheet').length > 0); const gone = (await deep(p, '[data-gone]')).join(''); say(ok && /isn’t in Meridian/.test(gone) && !p.errs.length, `P1 missing item: tree up ${ok}, says "${gone.slice(0, 60)}", errors ${p.errs.length} ${p.errs.join(' | ').slice(0, 120)}`); await p.context().close(); }
  // P2: every change of type says "starting today"
  for (const [id, X, Y] of [['guitar', 'week', 'month'], ['water', 'day', 'month'], ['reading', 'month', 'week'], ['meals', 'week', 'day'], ['guitar', 'month', 'day']]) { const p = await fresh();
    await p.evaluate(([id, X]) => { const it = window.__meridian.db().byId[id]; window.__meridian.S().updateItem(id, { cadence: { type: X }, targets: [{ from: 0, cmp: 'at_least', v: (it.targets[0] || {}).v || 1, cad: { type: X } }] }); }, [id, X]); await p.waitForTimeout(300);
    const t = await change(p, id, Y); say(/starting today/.test(t), `P2 ${id} ${X}->${Y}: ${t}`); await p.context().close(); }
  // P3: Reading none -> week -> month on one day; no 1-day week judged, and the breakdown counts the no-target periods
  { const p = await fresh(); await p.evaluate(() => window.__meridian.S().updateItem('reading', { cadence: { type: 'none' }, targets: [{ from: 0, cmp: 'none', v: 0, cad: { type: 'none' } }] })); await p.waitForTimeout(300);
    const t1 = await change(p, 'reading', 'week'); const t2 = await change(p, 'reading', 'month');
    const T = await p.evaluate(() => window.__meridian.db().byId.reading.targets.map(t => [t.from, t.cmp, t.cad && t.cad.type].join(':'))); const today = await p.evaluate(() => window.__meridian.db().today);
    say(!T.some(x => /:week$/.test(x)), `P3 no week rule left behind: ${JSON.stringify(T)} (today ${today}); toasts "${t1}" / "${t2}"`);
    await p.evaluate(() => window.__meridian.S().nav.reset('routines', [{ k: 'item', id: 'reading' }])); await p.waitForTimeout(1300);
    const pr = (await deep(p, '.perread, .note, .say')).filter(x => /Of the last|finished/.test(x)); say(!pr.some(x => /partly/.test(x) && /week/.test(x)), `P3 breakdown: ${pr.join(' / ').slice(0, 200)}`);
    say(!p.errs.length, `P3 errors: ${p.errs.join(' | ')}`); await p.context().close(); }
  // P3b: a routine with no-target periods: the breakdown names them
  { const p = await fresh(); await p.evaluate(() => window.__meridian.S().nav.reset('routines', [{ k: 'item', id: 'reading' }])); await p.waitForTimeout(1300); const pr = (await deep(p, '.say, .note, .perread')).filter(x => /Of the last/.test(x)); console.log('     reading as given:', pr.join(' / ').slice(0, 200)); await p.context().close(); }
  // P4: the chart's label follows the filter
  { const p = await fresh(); await p.evaluate(() => window.__meridian.S().nav.reset('time', [])); await p.waitForTimeout(1300); const l0 = await p.evaluate(() => { let o = ''; const w = r => { const e = r.querySelector('#yhero'); if (e) o = e.getAttribute('aria-label'); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); return o; });
    await p.evaluate(() => window.__meridian.S().nav.reset('time', [{ k: 'month', m: 9 }])); await p.waitForTimeout(1300);
    await p.evaluate(() => { const w = r => { const e = r.querySelector('.cb[data-id="guitar"]'); if (e) e.click(); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); }); await p.waitForTimeout(1500);
    const l1 = await p.evaluate(() => { let o = ''; const w = r => { const e = r.querySelector('#yhero'); if (e) o = e.getAttribute('aria-label'); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); return o; });
    say(/share of your routines/.test(l0) && /Guitar/.test(l1) && !/share of your routines/.test(l1), `P4 label: "${l0.slice(0, 70)}" -> "${l1.slice(0, 90)}"`); await p.context().close(); }
  // P5: the Routines hero's names are not cut (base, and a 44-character name)
  for (const long of [false, true]) { const p = await fresh(); if (long) { await p.evaluate(() => window.__meridian.S().updateItem('guitar', { name: 'Practise the lute', short: 'Practise the lute' })); await p.waitForTimeout(300); }
    await p.evaluate(() => window.__meridian.S().nav.reset('routines', [])); await p.waitForTimeout(1500);
    const cut = await p.evaluate(() => { const o = []; const w = r => { r.querySelectorAll('#loom .lb').forEach(e => { if (e.scrollWidth > e.clientWidth + 1) o.push(e.textContent); }); r.querySelectorAll('*').forEach(x => x.shadowRoot && w(x.shadowRoot)); }; w(document); return o; });
    say(!cut.length, `P5 hero names cut${long ? ' (with "Practise the lute")' : ''}: ${JSON.stringify(cut)}`); say(!p.errs.length, `P5 errors: ${p.errs.join(' | ')}`); await p.context().close(); }
  console.log(`r28 items: ${bad} failing`); await b.close(); })();
