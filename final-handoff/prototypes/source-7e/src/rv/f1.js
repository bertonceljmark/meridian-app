// f1.js [W] : real CDP touch swipes on every scrolling route/sheet: frames, taps fired, momentum, overscroll, stuck plates
const L=require('./L.js');const fs=require('fs');const INP=fs.readFileSync(L.OUT+'inpage.js','utf8');const W=+(process.argv[2]||390);const FILE=process.env.FILE||'p7a.html';const ONLY=process.env.ONLY?new RegExp(process.env.ONLY):null;
(async()=>{const b=await L.launch();const p=await L.open(b,{w:W,dpr:+(process.env.DPR||2),file:FILE});const c=p._cdp;const res=[];
 const views=[...L.ROUTES.map(([t,st])=>({nm:L.rn(t,st),go:()=>L.route(p,t,st,1300)})),...L.SHEETS.map(([k,o])=>({nm:L.sn(k,o),go:()=>L.sheet(p,k,o,1300)}))];
 const sig=()=>p.evaluate(()=>{let h=0;const s=JSON.stringify(Object.keys(localStorage).sort().map(k=>[k,localStorage[k]]));for(let i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))|0;const t=[...document.querySelectorAll('.toast')].filter(e=>e.getBoundingClientRect().height>0).map(e=>e.innerText).join('/');return [document.querySelectorAll('.sheet').length,document.querySelectorAll('.page').length,h,t].join('|')});
 const probe=()=>p.evaluate(()=>{window.__fr=[];window.__on=1;const f=t=>{if(!window.__on)return;window.__fr.push(t);requestAnimationFrame(f)};requestAnimationFrame(f);window.__clicks=[];});
 const stop=()=>p.evaluate(()=>{window.__on=0;const a=window.__fr;const d=[];for(let i=1;i<a.length;i++)d.push(a[i]-a[i-1]);d.sort((x,y)=>x-y);const q=k=>d.length?Math.round(d[Math.min(d.length-1,Math.floor(d.length*k))]*10)/10:0;return {n:d.length,p50:q(.5),p95:q(.95),max:q(1),over33:d.filter(x=>x>33.4).length,over50:d.filter(x=>x>50).length}});
 const st=()=>p.evaluate(S=>{const s=eval(S);return s?Math.round(s.scrollTop):-1},L.SCROLLER);
 const clayState=()=>p.evaluate(()=>{const C=window.__clay;if(!C)return [];const o=[];C.areas.forEach(A=>{if(!A.el.isConnected||!A.el.offsetParent)return;A.items.forEach(it=>{const t=it.p||it.el;const g=k=>(k==='--ta'||k==='--rk'?it.el:t).style.getPropertyValue(k);o.push([g('--w3'),g('--w7'),g('--m'),g('--ta'),g('--rk'),g('--mm')].join('#').length+':'+[g('--ta'),g('--rk')].join(','))});});return o});
 for(const v of views){ if(ONLY&&!ONLY.test(v.nm))continue; await v.go(); await p.evaluate(INP);
  await p.evaluate(()=>{if(!window.__ixC){window.__ixC=1;document.addEventListener('click',e=>{(window.__clicks=window.__clicks||[]).push(window.__ix.path(e.composedPath()[0]).split('>').slice(-1)[0])},true);}});
  const H=await p.evaluate(S=>{const s=eval(S);if(!s)return null;const r=s.getBoundingClientRect();return {sh:s.scrollHeight,ch:s.clientHeight,top:r.top,bot:r.bottom}},L.SCROLLER);
  if(!H||H.sh<=H.ch+5){res.push({v:v.nm,skip:'no scroll',H});continue;}
  const row={v:v.nm,H,sw:[]};
  // start points: tappables in middle band
  const starts=await p.evaluate(([t,b])=>{const ids=window.__ix.list();const m=ids.map(id=>window.__ix.meta(id)).filter(m=>m&&!m.inp&&m.cy>t+120&&m.cy<b-60);const pick=[];const seen=new Set();for(const x of m){const k=x.path.split('>').pop();if(seen.has(k))continue;seen.add(k);pick.push({id:x.id,x:x.cx,y:x.cy,k:k+' "'+x.txt.slice(0,16)+'"'});}return pick.slice(0,5)},[H.top,Math.min(H.bot,p.H-90)]);
  if(!starts.length)starts.push({x:W/2,y:Math.min(H.bot,p.H)-200,k:'(plain)'});
  for(const s of starts){ if(s.id){const q=await p.evaluate(id=>{const e=window.__ix.byId[id];if(!e||!e.isConnected)return null;e.scrollIntoView({block:'center'});const b=e.getBoundingClientRect();return {x:b.left+b.width/2,y:b.top+b.height/2}},s.id);await p.waitForTimeout(500);if(q){s.x=q.x;s.y=q.y;}}
   const s0=await sig();const a=await st();await probe();
   const dist=Math.min(360,s.y-H.top-20);let mid=null;
   await L.swipe(p,s.x,s.y,s.y-dist,220,async()=>{mid=await st();});
   const atEnd=await st();await p.waitForTimeout(1600);const after=await st();const fr=await stop();
   const clicks=await p.evaluate(()=>window.__clicks.splice(0));
   const sec=await p.evaluate(S=>{const main=eval(S);const o=[];for(const R of window.__ix.roots())R.querySelectorAll('*').forEach(e=>{if(e===main)return;const cs=getComputedStyle(e);if(!/(auto|scroll)/.test(cs.overflowY))return;const b=e.getBoundingClientRect();if(!b.height)return;if(e.scrollTop>0||(e.scrollHeight>e.clientHeight+1&&!/sheet-body|scroll/.test(e.className)))o.push(window.__ix.path(e).split('>').pop()+' sT'+Math.round(e.scrollTop)+' '+e.scrollHeight+'/'+e.clientHeight)});return o},L.SCROLLER);const s1=await sig();
   row.sw.push({sec,from:s.k,a,atEnd,after,mom:after-atEnd,fr,clicks,changed:s0!==s1?[s0,s1]:null});
   if(s0!==s1){await v.go();await p.evaluate(INP);}
  }
  // stuck check after settle: compare plate state to a forced re-measure
  await p.waitForTimeout(800);const c0=await clayState();await p.evaluate(()=>window.__clay&&window.__clay.refresh());await p.waitForTimeout(300);const c1=await clayState();
  row.stuck=c0&&c1?c0.filter((x,i)=>x!==c1[i]).length+'/'+c0.length:'n/a';
  // mid-scroll shot for the rise band
  await p.screenshot({path:L.OUT+`shots/f1-${W}-${v.nm}-settled.png`});
  // overscroll at top: pull down
  await p.evaluate(S=>{eval(S).scrollTop=0},L.SCROLLER);await p.waitForTimeout(500);const s0=await sig();
  await L.swipe(p,W/2,H.top+80,H.top+330,300);await p.waitForTimeout(80);
  const pull=await p.evaluate(S=>{const s=eval(S);return [s.style.transform||'none',getComputedStyle(s).transform,s.scrollTop].join(' ')},L.SCROLLER);
  await p.waitForTimeout(2600);
  const rel=await p.evaluate(S=>{const s=eval(S);return [s.style.transform||'none',s.scrollTop,document.scrollingElement.scrollTop,Math.round(document.querySelector('[data-screen]').getBoundingClientRect().top)].join(' ')},L.SCROLLER);
  const s1=await sig();
  // overscroll at bottom
  await p.evaluate(S=>{const s=eval(S);s.scrollTop=s.scrollHeight},L.SCROLLER);await p.waitForTimeout(500);const bt=await st();
  await L.swipe(p,W/2,Math.min(H.bot,p.H-100)-60,H.top+100,200);await p.waitForTimeout(1500);
  const bot=await p.evaluate(S=>{const s=eval(S);return [Math.round(s.scrollTop),s.scrollHeight-s.clientHeight,document.scrollingElement.scrollTop,Math.round(document.querySelector('[data-screen]').getBoundingClientRect().top),getComputedStyle(s).overscrollBehaviorY].join(' ')},L.SCROLLER);
  row.over={pull,rel,pullSig:s0!==s1?[s0,s1]:null,bot,bt};
  res.push(row);console.error(v.nm,JSON.stringify(row.sw.map(x=>[x.a,x.atEnd,x.after,x.fr.p95,x.fr.max,x.clicks.length,!!x.changed])),row.stuck);
 }
 fs.writeFileSync(L.OUT+`f1-${FILE.replace('.html','')}-${W}.json`,JSON.stringify(res,null,1));console.log('errs',p._errs.slice(0,8));await b.close();})();
