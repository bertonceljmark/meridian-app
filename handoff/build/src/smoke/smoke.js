const { chromium } = require('playwright');
const ROUTES = [['time', []], ['routines', []], ['you', []], ['routines', [{ k: 'item', id: 'guitar' }]], ['routines', [{ k: 'item', id: 'water' }]], ['routines', [{ k: 'item', id: 'caffeine' }]], ['routines', [{ k: 'item', id: 'alcohol' }]], ['time', [{ k: 'month', m: 9 }]], ['time', [{ k: 'day', d: 298 }]], ['time', [{ k: 'workouts' }]], ['time', [{ k: 'weeks' }]], ['time', [{ k: 'year' }]], ['you', [{ k: 'medication' }]], ['you', [{ k: 'feelpage' }]], ['you', [{ k: 'observations' }]], ['you', [{ k: 'contexts' }]], ['you', [{ k: 'checks' }]], ['you', [{ k: 'reminders' }]], ['you', [{ k: 'connections' }]], ['you', [{ k: 'privacy' }]], ['you', [{ k: 'devices' }]], ['you', [{ k: 'suggestions' }]], ['routines', [{ k: 'held' }]]];
const SKIP = new Set(['delgo', 'delall', 'exportgo']);
(async () => { const b = await chromium.launch(); const p = await (await b.newContext({ viewport: { width: 390, height: 844 } })).newPage();
  const errs = []; let cur = ''; p.on('pageerror', e => errs.push(cur + ' P ' + e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(cur + ' C ' + m.text().slice(0, 200)); });
  await p.goto('http://127.0.0.1:8765/' + process.argv[2]); await p.waitForFunction(() => window.__meridian, null, { timeout: 60000 }); await p.waitForTimeout(500);
  await p.evaluate(() => window.__meridian.setScen('base')); await p.waitForTimeout(1500);
  let n = 0;
  for (const [t, st] of ROUTES) {
    const acts = await p.evaluate(([t, st]) => { const S = window.__meridian.S(); S.sheet.closeAll(); S.nav.reset(t, st); return new Promise(r => setTimeout(() => { const h = [...document.querySelectorAll('[data-v3host]')].pop(); r(h ? [...h.shadowRoot.querySelectorAll('[data-act]')].map((e, i) => i + ':' + e.dataset.act) : []); }, 700)); }, [t, st]);
    for (const a of acts) { const [i, k] = a.split(':'); if (SKIP.has(k)) continue; cur = t + JSON.stringify(st) + ' ' + k;
      await p.evaluate(([t, st, i]) => { const S = window.__meridian.S(); S.sheet.closeAll(); window.__v3.sheet = null; S.nav.reset(t, st); }, [t, st, +i]); await p.waitForTimeout(250);
      await p.evaluate(i => { const h = [...document.querySelectorAll('[data-v3host]')].pop(); const e = h && h.shadowRoot.querySelectorAll('[data-act]')[i]; if (e) e.click(); }, +i); await p.waitForTimeout(350); n++;
      // and every act inside a sheet that opened (first level)
      const sa = await p.evaluate(() => window.__v3.sheet && window.__v3.sheet.root ? [...window.__v3.sheet.root.querySelectorAll('[data-act]')].map(e => e.dataset.act) : []);
      for (let j = 0; j < sa.length; j++) { if (SKIP.has(sa[j])) continue; cur = t + JSON.stringify(st) + ' ' + k + ' > ' + sa[j];
        await p.evaluate(j => { const r = window.__v3.sheet && window.__v3.sheet.root; const e = r && r.querySelectorAll('[data-act]')[j]; if (e) e.click(); }, j); await p.waitForTimeout(200); n++; }
    }
  }
  console.log('clicked', n); console.log(errs.slice(0, 40).join('\n')); console.log('errors', errs.length); await b.close(); })();
