// ctxsmoke.js <file>: a full context save for every kind, the span-replacement path, and Undo for each, with a
// console and page-error listener. Prints one line per check and "ctx errors N" at the end; exits 1 on any failure.
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await (await b.newContext({ viewport: { width: 390, height: 844 } })).newPage();
  const errs = []; p.on('pageerror', e => errs.push('P ' + e.message)); p.on('console', m => { if (m.type() === 'error') errs.push('C ' + m.text().slice(0, 200)); });
  await p.goto('http://127.0.0.1:8765/' + process.argv[2]); await p.waitForFunction(() => window.__meridian, null, { timeout: 60000 }); await p.waitForTimeout(1200);
  const ev = (f, a) => p.evaluate(f, a); const W = ms => p.waitForTimeout(ms); let fail = 0;
  await ev(() => { window.__T = []; setInterval(() => { const t = [...document.querySelectorAll('.toast')].map(e => e.innerText.replace(/\n/g, ' ')).join(' / '); if (t && window.__T[window.__T.length - 1] !== t) window.__T.push(t); }, 80); });
  const ctxs = () => ev(() => window.__meridian.db().contexts.map(c => `${c.id}:${c.type}:${c.from}-${c.to}`));
  const set = async (kind, len) => { await ev(([k, l]) => { const S = window.__meridian.S(); S.sheet.closeAll(); S.nav.reset('you', [{ k: 'contexts' }]); }, [kind, len]); await W(900);
    const e0 = errs.length; await ev(([k, l]) => { window.__v3.SCR = 'you'; window.__v3.acts.ctxset({ dataset: {} }); window.__v3.acts.cxt({ dataset: { v: k } }); window.__v3.acts.cxl({ dataset: { v: l } }); window.__T.splice(0); window.__v3.acts.cxsave({ dataset: {} }); }, [kind, len]); await W(900);
    return { e: errs.length - e0, t: await ev(() => window.__T.splice(0).join(' >> ')) }; };
  const undo = async () => { const ok = await ev(() => { const u = document.querySelector('.toast .undo'); if (u) { u.click(); return true; } return false; }); await W(900); return ok; };
  const check = (name, ok, info) => { console.log((ok ? 'ok   ' : 'FAIL ') + name + (info ? '  ' + info : '')); if (!ok) fail++; };
  for (const kind of ['sick', 'away', 'holiday', 'travel', 'work', 'dayoff', 'unusual', 'stress']) {
    await ev(() => window.__meridian.setScen('base')); await W(1200);
    const before = await ctxs(); const r = await set(kind, '6'); const after = await ctxs();
    const added = after.filter(x => !before.includes(x));
    check(`save ${kind}`, r.e === 0 && added.length >= 1 && /from today/.test(r.t), `added=${added.join(',')} toast="${r.t.slice(0, 90)}"`);
    const u = await undo(); const back = await ctxs();
    check(`undo ${kind}`, u && back.join() === before.join(), `now=${back.length} before=${before.length}`);
  }
  // span replacement: sample 4 is sick today; setting Away ends Sick yesterday, and Undo restores both
  await ev(() => window.__meridian.setSample(4)); await W(1500);
  const s0 = await ctxs(); const r = await set('away', '6'); const s1 = await ctxs();
  check('replace sick with away', r.e === 0 && s1.some(x => /:sick:304-304$/.test(x)) && s1.some(x => /:away:305-311$/.test(x)) && /Sick ends yesterday/.test(r.t), s1.join(' ') + `  toast="${r.t.slice(0, 120)}"`);
  await undo(); const s2 = await ctxs();
  check('undo replacement', s2.some(x => /:sick:304-307$/.test(x)) && !s2.some(x => /:away:/.test(x)), s2.join(' '));
  // a span that started today is replaced, not shortened
  const r2 = await set('sick', 'o'); const s3 = await ctxs(); const r3 = await set('away', '0'); const s4 = await ctxs();
  check('replace a same-day span', r3.e === 0 && !s4.some(x => /:sick:305-/.test(x) && !/s-sick/.test(x)) && s4.some(x => /:away:305-305$/.test(x)), s4.join(' '));
  console.log('ctx errors ' + errs.length + (errs.length ? ' ' + JSON.stringify(errs.slice(0, 5)) : '')); await b.close(); process.exit(fail || errs.length ? 1 : 0); })();
