// sheetsmoke.js <file>: open every app sheet and the v3 sheets, press each one's primary action, and collect page and
// console errors. Prints "sheets N pressed M errors E" and exits 1 on any error.
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 390, height: 844 } }); const p = await ctx.newPage();
  const errs = []; let cur = ''; p.on('pageerror', e => errs.push(cur + ' P ' + e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(cur + ' C ' + m.text().slice(0, 200)); });
  const U = 'http://127.0.0.1:8765/' + process.argv[2];
  const load = async () => { await p.goto(U); await p.waitForFunction(() => window.__meridian, null, { timeout: 60000 }); await p.waitForTimeout(1000); };
  await load(); await p.evaluate(() => localStorage.clear()); await load();
  const ev = (f, a) => p.evaluate(f, a); const W = ms => p.waitForTimeout(ms); let n = 0, pressed = 0;
  const press = async () => ev(() => { const sh = [...document.querySelectorAll('.sheet')].pop(); if (!sh) return 'nosheet';
    const btn = sh.querySelector('[data-livesave], .btn.acc:not([disabled]), .btn.primary:not([disabled]), .btn.big:not([disabled]):not(.ghost)'); if (!btn) return 'nobtn'; btn.click(); return btn.innerText.slice(0, 30); });
  const v3press = async () => ev(() => { const r = window.__v3.sheet && window.__v3.sheet.root; if (!r) return 'nosheet'; const btn = r.querySelector('.btn.primary:not([disabled])'); if (!btn) return 'nobtn'; btn.click(); return btn.innerText.slice(0, 30); });
  const ids = await ev(() => { const d = window.__meridian.db(); return { e: d.entries.filter(e => e.src !== 'watch').slice(-1)[0].id, c: (d.contexts[0] || {}).id, m: (d.meds[0] || {}).id }; });
  const SHEETS = [['log', { id: 'water' }], ['log', { id: 'guitar' }], ['log', { id: 'headache' }], ['feel', {}], ['ideaedit', { id: 'i1' }], ['who5', {}], ['focus', {}], ['create', {}], ['target', { id: 'water' }], ['target', { id: 'reading' }], ['context', {}],
    ['event', {}], ['presets', { id: 'water' }], ['measure', { id: 'water' }], ['rename', { id: 'water' }], ['explore', {}], ['drink', { id: 'caffeine' }], ['itemdet', { id: 'guitar' }], ['linkw', { id: 'running' }], ['ctxedit', { id: ids.c }],
    ['sugmore', {}], ['entry', { id: ids.e }], ['med', { id: 'med' }], ['medset', { id: 'med' }], ['info', { title: 'Info', body: 'x' }], ['reminder', { id: 'water' }], ['intent', {}], ['suppadd', { id: 'supps' }], ['news', {}], ['intentact', {}], ['day3', {}], ['export', {}]];
  for (const [k, o] of SHEETS) { cur = 'sheet:' + k; n++;
    await ev(([k, o]) => { const S = window.__meridian.S(); S.sheet.closeAll(); S.sheet.open({ k, ...o }); }, [k, o]); await W(700);
    const r = await press(); if (r !== 'nosheet' && r !== 'nobtn') pressed++; await W(700); console.log(cur, '->', r); }
  cur = 'sheet:confirm'; n++; await ev(() => { const S = window.__meridian.S(); S.sheet.closeAll(); S.sheet.open({ k: 'confirm', title: 'Sure?', yes: 'Yes', run: () => {} }); }); await W(700); { const r = await press(); if (r !== 'nosheet' && r !== 'nobtn') pressed++; console.log(cur, '->', r); } await W(600);
  // a live session ended through its sheet path (an intention) and the item path
  cur = 'live'; await ev(() => { const S = window.__meridian.S(); S.sheet.closeAll(); S.startLive(window.__meridian.db().byId.guitar); }); await W(3000); await ev(() => window.__meridian.S().endLive()); await W(800);
  // v3 sheets: each act that opens one, then its primary button
  const V3 = [['routines', 'compose', {}], ['routines', 'target', { id: 'water' }], ['you', 'ctxset', {}], ['you', 'medlog', { id: 'med' }], ['you', 'gonotice', {}]];
  for (const [scr, act, ds] of V3) { cur = 'v3:' + act; n++;
    await ev(([scr, act, ds]) => { const S = window.__meridian.S(); S.sheet.closeAll(); S.nav.reset(scr, []); }, [scr, act, ds]); await W(1200); await ev(([scr, act, ds]) => { window.__v3.SCR = scr; window.__v3.acts[act]({ dataset: ds }); }, [scr, act, ds]); await W(1500);
    if (act === 'compose' || act === 'gonotice') await ev(() => { const i = window.__v3.sheet && window.__v3.sheet.root && window.__v3.sheet.root.querySelector('[data-cn]'); if (i) { i.value = 'Smoke test'; i.dispatchEvent(new Event('input', { bubbles: true })); } }); await W(300);
    const r = await v3press(); if (r !== 'nosheet' && r !== 'nobtn') pressed++; await W(800); console.log(cur, '->', r); }
  // the last: delete everything, then a reload
  cur = 'sheet:deleteall'; n++; await ev(() => { const S = window.__meridian.S(); S.sheet.closeAll(); S.sheet.open({ k: 'deleteall' }); }); await W(700); console.log(cur, '->', await press()); await W(800);
  cur = 'reload'; await load();
  console.log(`sheets ${n} pressed ${pressed} errors ${errs.length}` + (errs.length ? '\n' + errs.slice(0, 12).join('\n') : '')); await b.close(); process.exit(errs.length ? 1 : 0); })();
