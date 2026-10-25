"""brown.py dir...: counts brown pixels (dark warm: hue 10-50 deg, saturation > .3, value .12-.6) per shot; Mark's rule is no brown.
An orange accent at full strength is not brown; a dim warm wash is."""
import sys, glob, colorsys
from PIL import Image
for d in sys.argv[1:]:
    tot = 0
    for f in sorted(glob.glob(d + '/*.png')):
        im = Image.open(f).convert('RGB'); w, h = im.size; im2 = im.resize((w // 2, h // 2)); px = im2.load(); n = 0; xs = []
        for y in range(im2.size[1]):
            for x in range(im2.size[0]):
                r, g, b = px[x, y]; hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
                if 10 / 360 <= hh <= 50 / 360 and s > .3 and .12 <= v <= .6: n += 1; xs.append((x * 2, y * 2))
        tot += n
        if n > 40:
            ys = sorted(p[1] for p in xs); print(f'{f.split("/")[-1]:40s} {n:6d}  y {ys[0]}-{ys[-1]} median {ys[len(ys)//2]}')
    print(d, 'total', tot)
