#!/bin/bash
# pass 7e: 7d regenerated from 6i (inj7d.py, md5 checked), then r29; bundle built in the same run; both checked. Everything in p7e/.
set -e
S=/tmp/claude-0/-home-user/c8b72fc4-c1cb-5dbd-9f42-01758835eb49/scratchpad
E=/tmp/claude-0/-home-user-meridian-app/c8b72fc4-c1cb-5dbd-9f42-01758835eb49/scratchpad/p7e
B=/mnt/project-files/meridian/evolve/base7
OUT=$E/ python3 $S/p7d/inj7d.py | tail -1
[ "$(md5sum < $E/meridian-src-p7d.html | cut -d' ' -f1)" = cf6f4510f51ff71be33c38dd6c4af444 ] && echo "7d src regenerated exactly" || { echo "7d SRC DIFFERS"; exit 1; }
python3 $S/p7d/inj7e.py
M0=$(md5sum < $E/meridian-src-p7e.html); NODE_PATH=$(npm root -g) node $B/tools/build.js $E/meridian-src-p7e.html $E/meridian-p7e.html | tail -1
[ "$M0" = "$(md5sum < $E/meridian-src-p7e.html)" ] && grep -q "window.__clay" $E/meridian-p7e.html && grep -q 'r29 (review r28 B2)' $E/meridian-p7e.html && echo "bundle built from the current src" || { echo "BUNDLE STALE"; exit 1; }
python3 - <<'PY'
import re
s=open('/tmp/claude-0/-home-user-meridian-app/c8b72fc4-c1cb-5dbd-9f42-01758835eb49/scratchpad/p7e/meridian-src-p7e.html').read()
bl=[m.group(1) for m in re.finditer(r'<script type="text/babel" data-presets="react">(.*?)</script>', s, re.S)]
print('blocks KB', [round(len(b.encode())/1024) for b in bl]); assert all(len(b.encode()) < 500*1024 for b in bl)
for i,b in enumerate(bl[1:],2):
    if re.search(r'\{\s*[^{}]*\.\.\.\w+\s*\}\s*=', b): print('rest destructuring in block', i)
PY
cd $E
for f in meridian-src-p7e.html meridian-p7e.html; do NODE_PATH=$(npm root -g) timeout 120 node $B/pass3/tools/err.js $f | tail -3; done
if [ "${SMOKE:-1}" = 1 ]; then
  for f in meridian-src-p7e.html meridian-p7e.html; do echo "== ctxsmoke $f"; NODE_PATH=$(npm root -g) timeout 300 node $S/v3/ctxsmoke.js $f > $E/ctx.out 2>&1; grep -c "^ok" $E/ctx.out; grep "FAIL\|ctx errors" $E/ctx.out
    echo "== sheetsmoke $f"; NODE_PATH=$(npm root -g) timeout 400 node $S/v3/sheetsmoke.js $f | tail -3
    echo "== route smoke $f"; NODE_PATH=$(npm root -g) timeout 900 node $S/v3/smoke.js $f | tail -1; done
  for w in 390 430; do echo "== cadence matrix $w"; (cd $S/p7d && NODE_PATH=$(npm root -g) timeout 1500 node cadm.js meridian-p7e.html $w > $E/cadm$w.txt 2>&1; grep -c '^ok' $E/cadm$w.txt; grep -A3 '^FAIL' $E/cadm$w.txt | cut -c1-300; tail -n 1 $E/cadm$w.txt); done; fi
