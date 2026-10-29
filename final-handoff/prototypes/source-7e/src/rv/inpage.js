window.__ix = window.__ix || (() => {
  const SEL = 'button, a[href], [role="button"], [role="tab"], [role="switch"], [role="checkbox"], [role="radio"], [role="option"], [role="link"], [role="slider"], [role="menuitem"], summary, input, textarea, select, [tabindex]:not([tabindex="-1"]), [data-act]';
  const KEYS = ['.t3 .zk-round', '.t3 .zk-seg', '.t3 .zk-pill', '.t3 .zk-word', '.t3 .zamt .zkey', '.t3 .ztk', '.t3 .zchip', '.t3 .zib', '.t3 .zaddbtn', '.t3 .zsb > button', '.t3 .zx', '.t3 .zfoot button', '.t3 .zmore', '.btn', '.chip', '.preset', '.iconbtn', '.n7-key'].join(',');
  const SH_KEYS = ['.btn', '.chip', '.sw', '.seg', '.search', '.n7-key', '.go', '.ib', '.foot button', '.sh .close'].join(',');
  const roots = () => { const out = [document]; const walk = r => r.querySelectorAll('*').forEach(e => { if (e.shadowRoot) { out.push(e.shadowRoot); walk(e.shadowRoot); } }); walk(document); return out; };
  const rp = e => { const k = Object.keys(e).find(k => k.startsWith('__reactProps')); return k ? e[k] : null; };
  const hasH = e => { const p = rp(e); if (!p) return false; return ['onClick', 'onPointerDown', 'onPointerUp', 'onTouchStart', 'onMouseDown', 'onTouchEnd', 'onKeyDown'].some(k => typeof p[k] === 'function'); };
  const hit = (x, y) => { let el = document.elementFromPoint(x, y); while (el && el.shadowRoot) { const n = el.shadowRoot.elementFromPoint(x, y); if (!n || n === el) break; el = n; } return el; };
  const contains = (a, b) => { let n = b; while (n) { if (n === a) return true; n = n.parentNode || n.host; } return false; };
  const isTap = e => e.matches(SEL) || hasH(e) || (e.tagName === 'LABEL');
  const ids = new WeakMap(); let nid = 0; const byId = {};
  const idOf = e => { if (!ids.has(e)) { ids.set(e, ++nid); byId[nid] = e; } return ids.get(e); };
  function path(e) { const parts = []; let n = e; while (n && n.nodeType === 1 && parts.length < 5) { const c = (typeof n.className === 'string' ? n.className : '').trim().split(/\s+/).filter(x => x && !/^(n7cl|n7rel|down|on|full)$/.test(x)).slice(0, 2).join('.'); parts.unshift(n.tagName.toLowerCase() + (c ? '.' + c : '')); n = n.parentElement || (n.parentNode && n.parentNode.host); } return parts.join('>'); }
  function vis(e) { const r = e.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return false; if (!e.checkVisibility({ opacityProperty: true, visibilityProperty: true })) return false; return true; }
  // all candidate tappables that are visible and hittable at their centre right now
  function list() {
    const out = []; const scr = document.querySelector('.screen.has-sheet');
    for (const R of roots()) R.querySelectorAll('*').forEach(e => {
      if (!isTap(e)) return; if (e.closest('.n7c')) return; if (!vis(e)) return; const cs = getComputedStyle(e); if (cs.pointerEvents === 'none' || e.disabled) return;
      // a tappable nested inside another tappable with no own box: skip inner if same box
      const b = e.getBoundingClientRect(); const cx = b.left + b.width / 2, cy = b.top + b.height / 2; if (cx < 0 || cx > innerWidth || cy < 0 || cy > innerHeight) return;
      const t = hit(cx, cy); if (!t || !contains(e, t)) return;
      // is the hit target a deeper tappable? then this one is a wrapper; keep it only if it has its own handler
      let n = t, deeper = null; while (n && n !== e) { if (n.nodeType === 1 && isTap(n)) { deeper = n; break; } n = n.parentNode || n.host; }
      if (deeper) return;
      out.push(idOf(e)); });
    return out;
  }
  function meta(id) {
    const e = byId[id]; if (!e || !e.isConnected) return null; const b = e.getBoundingClientRect(); const cx = b.left + b.width / 2, cy = b.top + b.height / 2;
    // effective hit extent through the centre
    const ext = (dx, dy) => { let n = 0; for (let s = 1; s <= 40; s++) { const t = hit(cx + dx * s, cy + dy * s); if (!t || !contains(e, t)) break; n = s; } return n; };
    const hw = ext(-1, 0) + ext(1, 0) + 1, hh = ext(0, -1) + ext(0, 1) + 1;
    const p = rp(e); const cs = getComputedStyle(e);
    return { id, path: path(e), tag: e.tagName.toLowerCase(), role: e.getAttribute('role'), txt: (e.innerText || e.value || e.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 30), aria: e.getAttribute('aria-label'),
      x: Math.round(b.left), y: Math.round(b.top), w: Math.round(b.width), h: Math.round(b.height), hw, hh, cx, cy,
      native: e.matches('button, a[href], input, textarea, select, summary') || !!e.getAttribute('role'), focusable: e.tabIndex >= 0, react: !!p, handler: hasH(e), act: e.dataset ? e.dataset.act || null : null,
      cursor: cs.cursor, key: e.matches(KEYS) || (e.getRootNode() !== document && e.matches(SH_KEYS)), inp: /INPUT|TEXTAREA|SELECT/.test(e.tagName), shadow: e.getRootNode() !== document };
  }
  // elements that LOOK like keys (match the clay key selectors) but are not tappable themselves or inside a tappable
  function fakeKeys() {
    const out = [];
    for (const R of roots()) { const sel = R === document ? KEYS : SH_KEYS; R.querySelectorAll(sel).forEach(e => { if (!vis(e)) return; let n = e, ok = false; while (n) { if (n.nodeType === 1 && isTap(n)) { ok = true; break; } n = n.parentNode || n.host; } if (!ok) out.push(path(e) + ' "' + (e.innerText || '').trim().slice(0, 24) + '"'); }); }
    return [...new Set(out)];
  }
  // elements with a click handler (react) or pointer cursor that are NOT native/role: a tappable that is not exposed as one
  return { list, meta, byId, fakeKeys, hit, contains, rp, roots, path, idOf };
})();
