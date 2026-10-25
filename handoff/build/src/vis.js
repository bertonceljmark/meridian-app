// vis.js <file> [W]: a VISIBLE press for every tappable on every route and sheet: CDP-forced :active, a screenshot of the
// element's box (plus 6 px) before and during, and the pixel change. A press shows when >= 2% of the box (at least 120 px at DPR 1)
// moves by more than 16 levels. Prints the classes that do not.
const { chromium } = require('playwright'); const T = require('./tour-lists.js'); const { PNG } = require(require.resolve('playwright-core/lib/utilsBundle', { paths: [require.resolve('playwright')] }));
const W = +(process.argv[3] || 390);
(async () => { const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: W, height: W === 430 ? 932 : 844 }, isMobile: true, hasTouch: true }); const p = await ctx.newPage(); const cdp = await ctx.newCDPSession(p);
  await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
  await p.goto('http://127.0.0.1:8765/' + process.argv[2]); await p.waitForFunction(() => window.__meridian, null, { timeout: 60000 }); await p.waitForTimeout(800);
  await p.evaluate(() => window.__meridian.setScen('base')); await p.waitForTimeout(1200);
  const fail = {}, okc = {}; let n = 0, nf = 0;
  const diff = (a, c) => { const A = PNG.sync.read(a), C = PNG.sync.read(c); let k = 0, mx = 0; for (let i = 0; i < A.data.length; i += 4) { const d = Math.max(Math.abs(A.data[i] - C.data[i]), Math.abs(A.data[i + 1] - C.data[i + 1]), Math.abs(A.data[i + 2] - C.data[i + 2])); if (d > 16) k++; if (d > mx) mx = d; } return { k, mx, tot: A.data.length / 4 }; };
  const check = async nm => {
    const cnt = await p.evaluate(() => { window.__tp = []; const sel = 'button, a[href], [role="button"], [role="tab"], [role="switch"], [role="checkbox"], summary, [tabindex="0"]';
      const walk = r => { r.querySelectorAll(sel).forEach(e => { const bb = e.getBoundingClientRect(); if (bb.width < 8 || bb.height < 8 || bb.top < 64 || bb.bottom > innerHeight - 4 || bb.left < 0 || bb.right > innerWidth) return; const cs = getComputedStyle(e); if (cs.visibility === 'hidden' || cs.pointerEvents === 'none' || e.disabled) return;
          const scr = document.querySelector('.screen.has-sheet'); const inSheet = e.closest('.sheet') || (e.getRootNode().host && e.getRootNode().host.closest('.sheet')); if (scr && !inSheet) return;
          const top = (e.getRootNode().elementFromPoint ? e.getRootNode() : document).elementFromPoint(bb.left + bb.width / 2, bb.top + bb.height / 2); if (top && top !== e && !e.contains(top) && !(top.shadowRoot && top.shadowRoot.contains(e))) return;
          window.__tp.push(e); }); r.querySelectorAll('*').forEach(x => { if (x.shadowRoot) walk(x.shadowRoot); }); }; walk(document); return window.__tp.length; });
    await cdp.send('DOM.getDocument', { depth: -1, pierce: true });
    for (let i = 0; i < Math.min(cnt, 60); i++) {
      const d = await p.evaluate(i => { const e = window.__tp[i]; const bb = e.getBoundingClientRect(); return { k: e.tagName.toLowerCase() + '.' + (typeof e.className === 'string' ? e.className.trim().split(/\s+/).slice(0, 2).join('.') : ''), t: (e.getAttribute('aria-label') || e.textContent || '').trim().slice(0, 20), x: Math.max(0, bb.left - 6), y: Math.max(0, bb.top - 6), w: Math.min(innerWidth - Math.max(0, bb.left - 6), bb.width + 12), h: Math.min(innerHeight - Math.max(0, bb.top - 6), bb.height + 12) }; }, i);
      let nodeId = null; try { const r = await cdp.send('Runtime.evaluate', { expression: `window.__tp[${i}]` }); nodeId = (await cdp.send('DOM.requestNode', { objectId: r.result.objectId })).nodeId; } catch (e) { continue; }
      const clip = { x: d.x, y: d.y, width: Math.max(1, d.w), height: Math.max(1, d.h) };
      const a = await p.screenshot({ clip }); await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active'] }); await p.waitForTimeout(160); const c = await p.screenshot({ clip }); const dbg = process.env.DBG ? await p.evaluate(i => { const e = window.__tp[i]; const cs = getComputedStyle(e); const bb = e.getBoundingClientRect(); return [cs.transform, cs.backgroundColor, cs.getPropertyValue('--e'), Math.round(bb.top), Math.round(bb.bottom), innerHeight].join(' ; '); }, i) : ''; await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }); await p.waitForTimeout(60);
      const r = diff(a, c); n++; const vis = r.k >= Math.max(120, .02 * r.tot) || (r.tot < 4000 && r.k >= .04 * r.tot);
      if (!vis && process.env.DBG) console.log('FAIL', d.k, d.t, 'k', r.k, 'tot', r.tot, dbg); if (!vis) { nf++; (fail[d.k] = fail[d.k] || { n: 0, ex: new Set(), mx: 0 }).n++; fail[d.k].ex.add(nm + ':' + d.t); fail[d.k].mx = Math.max(fail[d.k].mx, r.mx); } else okc[d.k] = (okc[d.k] || 0) + 1; } };
  for (const [t, st] of T.ROUTES) { const nm = 'r-' + t + (st.length ? '-' + st.map(s => s.k + (s.id || s.m || s.d || '')).join('-') : ''); if (process.env.ONLY && !new RegExp(process.env.ONLY).test(nm)) continue;
    await p.evaluate(([t, st]) => { const S = window.__meridian.S(); S.sheet.closeAll(); S.nav.reset(t, st); }, [t, st]); await p.waitForTimeout(900); await check(nm);
    if (!process.env.NOSCROLL) { await p.evaluate(() => { const s = [...document.querySelectorAll('.page:not(.under) .scroll')].pop(); if (s) s.scrollTop = 700; }); await p.waitForTimeout(600); await check(nm + '@700'); } }
  for (const [k, o] of T.SHEETS) { const nm = 's-' + k; if (process.env.ONLY && !new RegExp(process.env.ONLY).test(nm)) continue;
    await p.evaluate(([k, o]) => { const S = window.__meridian.S(); S.sheet.closeAll(); S.nav.reset('today', []); S.sheet.open({ k, ...o }); }, [k, o]); await p.waitForTimeout(1000); await check(nm); }
  console.log('checked', n, 'no visible press', nf);
  Object.entries(fail).sort((a, b) => b[1].n - a[1].n).forEach(([k, v]) => console.log(v.n + '\t' + k + '\tmax ' + v.mx + '\t' + [...v.ex].slice(0, 3).join(' | ')));
  await b.close(); })();
