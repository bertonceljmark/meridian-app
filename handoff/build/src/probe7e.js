// probe7e.js <file> <outdir> <tag> [W]: shots and the raised forms of the screens in the r28 look slice
const { chromium } = require('playwright'); const [file, out, tag, w] = process.argv.slice(2); const W = +(w || 390); const TS = +(process.env.TS || 1);
const SCR = [
  ['sleep-day', `M.S().nav.reset('time', [{ k: 'sleep', d: M.db().today - 1 }])`],
  ['log-sheet', `M.S().sheet.open({ k: 'log' })`],
  ['sugmore', `M.S().sheet.open({ k: 'sugmore' })`],
  ['drink', `M.S().sheet.open({ k: 'drink', id: 'water' })`],
  ['export', `M.S().sheet.open({ k: 'export' })`],
  ['medication', `M.S().nav.reset('you', [{ k: 'medication' }])`],
  ['time-year', `M.S().nav.reset('time', [])`],
  ['week44', `M.S().nav.reset('time', [{ k: 'weeks', off: 0 }])`],
  ['routines', `M.S().nav.reset('routines', [])`],
  ['day', `M.S().nav.reset('time', [{ k: 'day', d: M.db().today - 1 }])`],
  ['water', `M.S().nav.push({ k: 'item', id: 'water' })`],
  ['guitar', `M.S().nav.push({ k: 'item', id: 'guitar' })`],
];
(async () => { const b = await chromium.launch(); const only = process.env.ONLY ? process.env.ONLY.split(',') : null;
  for (const [nm, js] of SCR) { if (only && !only.includes(nm)) continue;
    const ctx = await b.newContext({ viewport: { width: W, height: W === 430 ? 932 : 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 }); const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://127.0.0.1:8765/' + file); await p.waitForFunction(() => window.__meridian, null, { timeout: 60000 }); await p.evaluate(() => window.__meridian.setScen('base'));
    if (TS !== 1) await p.evaluate(ts => { const S = window.__meridian.S(); if (S.setPref) S.setPref('textSize', ts); document.querySelectorAll('[data-screen]').forEach(e => e.style.setProperty('--ts', ts)); }, TS);
    await p.waitForTimeout(900);
    await p.evaluate(js => { const M = window.__meridian; (new Function('M', js))(M); }, js); await p.waitForTimeout(1800);
    if (process.env.SCROLL) await p.evaluate(y => { const s = [...document.querySelectorAll('.sheet .scroll, .sheet .sbody, .page:not(.under) .scroll')].pop(); if (s) s.scrollTop = +y; }, process.env.SCROLL), await p.waitForTimeout(500);
    await p.screenshot({ path: `${out}/${nm}-${W}-${tag}.png` });
    if (process.env.PROBE) { const r = await p.evaluate(() => { const L = []; const vis = (root) => root.querySelectorAll('*').forEach(e => { if (e.shadowRoot) vis(e.shadowRoot); const cs = getComputedStyle(e); if (cs.boxShadow === 'none' || e.closest('.dock,.tabbar,nav')) return; const r = e.getBoundingClientRect(); if (r.width < 120 || r.height < 30 || r.bottom < 0 || r.top > innerHeight) return; const txt = [...e.querySelectorAll('*')].find(x => x.childNodes.length && [...x.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())); const tf = txt ? getComputedStyle(txt) : null; L.push(`${e.tagName.toLowerCase()}.${[...e.classList].join('.')} ${Math.round(r.left)},${Math.round(r.top)} ${Math.round(r.width)}x${Math.round(r.height)} rad ${cs.borderRadius} pad ${cs.padding} | ${txt ? txt.tagName.toLowerCase() + '.' + [...txt.classList].join('.') + ' ' + tf.fontSize + '/' + tf.fontWeight + ' "' + txt.textContent.trim().slice(0, 30) + '"' : ''}`); }); vis(document); return L; }); console.log('== ' + nm + (errs.length ? ' ERR ' + errs.join(' | ') : '')); console.log(r.join('\n')); }
    else if (errs.length) console.log(nm, 'ERR', errs.join(' | '));
    await ctx.close(); }
  await b.close(); })();
