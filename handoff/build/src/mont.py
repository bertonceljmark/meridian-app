import sys,glob,os
from PIL import Image
# mont.py outfile cols scale files...
out=sys.argv[1]; cols=int(sys.argv[2]); sc=float(sys.argv[3]); fs=sys.argv[4:]
ims=[Image.open(f).convert('RGB') for f in fs]
w=int(ims[0].width*sc); h=int(ims[0].height*sc)
rows=(len(ims)+cols-1)//cols
o=Image.new('RGB',(cols*w,rows*h),(255,255,255))
for i,im in enumerate(ims):
    o.paste(im.resize((w,int(im.height*sc))),((i%cols)*w,(i//cols)*h))
o.save(out)
