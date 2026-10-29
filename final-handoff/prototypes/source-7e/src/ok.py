import math
def s2l(c): c/=255; return c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4
def l2s(c): c=max(0,min(1,c)); return round(255*(12.92*c if c<=.0031308 else 1.055*c**(1/2.4)-.055))
def hex2(h): h=h.lstrip('#'); return [int(h[i:i+2],16) for i in (0,2,4)]
def tolab(rgb):
    r,g,b=[s2l(x) for x in rgb]
    l=.4122214708*r+.5363325363*g+.0514459929*b; m=.2119034982*r+.6806995451*g+.1073969566*b; s=.0883024619*r+.2817188376*g+.6299787005*b
    l,m,s=[x**(1/3) for x in (l,m,s)]
    return [.2104542553*l+.7936177850*m-.0040720468*s, 1.9779984951*l-2.4285922050*m+.4505937099*s, .0259040371*l+.7827717662*m-.8086757660*s]
def fromlab(L):
    L,a,b=L; l=L+.3963377774*a+.2158037573*b; m=L-.1055613458*a-.0638541728*b; s=L-.0894841775*a-1.2914855480*b
    l,m,s=l**3,m**3,s**3
    return [l2s(4.0767416621*l-3.3077115913*m+.2309699292*s), l2s(-1.2684380046*l+2.6097574011*m-.3413193965*s), l2s(-.0041960863*l-.7034186147*m+1.7076147010*s)]
def mix(a,b,p):
    A,B=tolab(hex2(a)),tolab(hex2(b)); return '#'+''.join('%02X'%v for v in fromlab([A[i]*(1-p)+B[i]*p for i in range(3)]))
def lum(rgb): r,g,b=[s2l(x) for x in rgb]; return .2126*r+.7152*g+.0722*b
def cr(a,b): la,lb=lum(a),lum(b); return (max(la,lb)+.05)/(min(la,lb)+.05)
if __name__=='__main__':
    for p in [1.2,1.6,2.4,3.2,3.6,4,5,6,8,10]: print('lift',p,mix('#1D2633','#E6F0FF',p/100))
    for p in [4,5,8,12,20]: print('deep',p,mix('#1D2633','#000000',p/100))
    tx=[232,239,248]; bg=hex2('#1D2633')
    for a in [1,.7,.58,.5,.3]:
        c=[round(tx[i]*a+bg[i]*(1-a)) for i in range(3)]; print('t',a,c,round(cr(c,bg),2))
