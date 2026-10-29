S=/tmp/claude-0/-home-user/c8b72fc4-c1cb-5dbd-9f42-01758835eb49/scratchpad
E=/tmp/claude-0/-home-user-meridian-app/c8b72fc4-c1cb-5dbd-9f42-01758835eb49/scratchpad/p7e
B=/mnt/project-files/meridian/evolve/base7
export NODE_PATH=$(npm root -g)
cd $E
for f in meridian-src-p7e.html meridian-p7e.html; do echo "== err $f"; timeout 200 node $B/pass3/tools/err.js $f 2>&1 | tail -3; done
cd $S/p7d
for W in 390 430; do
  echo "== chk7e $W"; timeout 600 node chk7e.js meridian-p7e.html $W 2>&1 | tail -4
  echo "== vis $W"; timeout 1500 node vis.js meridian-p7e.html $W 2>&1 | tail -6
  echo "== pgfast $W"; timeout 600 node pgfast.js meridian-p7e.html $W 2>&1 | tail -6
  echo "== pgfast cpu6 $W"; CPU=6 timeout 900 node pgfast.js meridian-p7e.html $W 2>&1 | tail -6
  echo "== topedge $W"; timeout 900 node topedge.js meridian-p7e.html $W 2>&1 | tail -4
  for f in meridian-p7c.html meridian-p7e.html; do echo "== pgfps $f $W"; timeout 400 node pgfps.js $f $W 2>&1 | tail -1; echo "== pgfps cpu6 $f $W"; CPU=6 timeout 600 node pgfps.js $f $W 2>&1 | tail -1; done
done
cd $S/rv
for W in 390 430; do echo "== f1 $W"; timeout 1800 node f1.js $W > $E/chk/f1-$W.out 2>&1; tail -5 $E/chk/f1-$W.out; done
echo SUITE DONE
