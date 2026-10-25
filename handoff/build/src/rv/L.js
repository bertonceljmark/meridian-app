const { chromium } = require('playwright');
const R='/tmp/claude-0/-home-user/c8b72fc4-c1cb-5dbd-9f42-01758835eb49/scratchpad/rv/';
const ROUTES = [['today', []], ['time', []], ['routines', []], ['you', []], ['routines', [{ k: 'item', id: 'guitar' }]], ['routines', [{ k: 'item', id: 'water' }]], ['routines', [{ k: 'item', id: 'caffeine' }]], ['routines', [{ k: 'item', id: 'alcohol' }]], ['time', [{ k: 'month', m: 9 }]], ['time', [{ k: 'day', d: 298 }]], ['time', [{ k: 'workouts' }]], ['time', [{ k: 'weeks' }]], ['time', [{ k: 'year' }]], ['you', [{ k: 'medication' }]], ['you', [{ k: 'feelpage' }]], ['you', [{ k: 'observations' }]], ['you', [{ k: 'contexts' }]], ['you', [{ k: 'checks' }]], ['you', [{ k: 'reminders' }]], ['you', [{ k: 'connections' }]], ['you', [{ k: 'privacy' }]], ['you', [{ k: 'devices' }]], ['you', [{ k: 'suggestions' }]], ['routines', [{ k: 'held' }]], ['time', [{ k: 'sleep', d: 298 }]]];
const SHEETS = [['log', {}], ['log', { id: 'water' }], ['log', { id: 'guitar' }], ['feel', {}], ['create', {}], ['target', { id: 'water' }], ['context', {}], ['event', {}], ['presets', { id: 'water' }], ['drink', { id: 'caffeine' }], ['itemdet', { id: 'guitar' }], ['sugmore', {}], ['med', { id: 'med' }], ['intent', {}], ['intentact', {}], ['day3', {}], ['export', {}], ['deleteall', {}], ['confirm', { title: 'Sure?', yes: 'Yes' }]];
const rn=(t,st)=>'r-' + t + (st.length ? '-' + st.map(s => s.k + (s.id || s.m || s.d || '')).join('-') : '');
const sn=(k,o)=>'s-' + k + (o.id ? '-' + o.id : '');
async function launch(){return chromium.launch({executablePath:'/opt/pw-browsers/chromium'});}
async function open(b,o={}){const W=o.w||390,H=W===430?932:844;
 const ctx=await b.newContext({viewport:{width:W,height:H},deviceScaleFactor:o.dpr||2,hasTouch:true,isMobile:true,colorScheme:'dark',reducedMotion:o.rm?'reduce':'no-preference'});
 const p=await ctx.newPage();p._errs=[];p.on('console',m=>{if(m.type()==='error')p._errs.push(m.text().slice(0,200))});p.on('pageerror',e=>p._errs.push('PE '+e.message.slice(0,200)));
 await p.goto('file://'+R+(o.file||'p7a.html')+(o.q||''));await p.waitForFunction(()=>window.__meridian,null,{timeout:60000});await p.waitForTimeout(800);
 await p.evaluate(()=>window.__meridian.setScen('base'));await p.waitForTimeout(1200);
 await p.evaluate(()=>{window.__dq=(sel,root=document)=>{const out=[];const walk=r=>{r.querySelectorAll(sel).forEach(e=>out.push(e));r.querySelectorAll('*').forEach(e=>{if(e.shadowRoot)walk(e.shadowRoot)})};walk(root);return out};});
 p._cdp=await ctx.newCDPSession(p); p.W=W;p.H=H; return p;}
async function route(p,t,st,w=1000){await p.evaluate(([t,st])=>{const S=window.__meridian.S();S.sheet.closeAll();S.nav.reset(t,st);},[t,st]);await p.waitForTimeout(w);}
async function sheet(p,k,o,w=1000){await p.evaluate(([k,o])=>{const S=window.__meridian.S();S.sheet.closeAll();S.nav.reset('today',[]);S.sheet.open({k,...o});},[k,o]);await p.waitForTimeout(w);}
// top scroller of current view
const SCROLLER=`(()=>{const sh=[...document.querySelectorAll('.sheet .sheet-body')].filter(e=>e.getBoundingClientRect().height>0).pop(); if(sh) return sh; return [...document.querySelectorAll('.page:not(.under) .scroll')].pop();})()`;
async function swipe(p,x,y0,y1,ms=260,onMid){const c=p._cdp;const n=Math.max(6,Math.round(ms/16));await c.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x,y:y0}]});
 for(let i=1;i<=n;i++){const t=i/n;await c.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x,y:y0+(y1-y0)*t}]});await p.waitForTimeout(16);if(onMid&&i===Math.round(n*.6))await onMid();}
 await c.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});}
module.exports={launch,open,route,sheet,swipe,ROUTES,SHEETS,rn,sn,R,SCROLLER,OUT:R+'ix/'};
