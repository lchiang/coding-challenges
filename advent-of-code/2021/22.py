import re
from collections import namedtuple
Pt = namedtuple('Pt', ['switch','x1','x2','y1','y2','z1','z2'])

ll = open('in22t2.txt').read().splitlines()

inp = []
d = {}
for l in ll:
    match = re.search(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', l)
    il = list(match.groups())
    inp.append(Pt(*[1 if il[0] == 'on' else 0]+[int(x) for x in il[1:]]))

### Part A Begin ###
for k in inp:
    #print(k)
    for z in range(max(-50,k.z1),min(51,k.z2+1)):
        for y in range(max(-50,k.y1),min(51,k.y2+1)):
            for x in range(max(-50,k.x1),min(51,k.x2+1)):
                d[(x,y,z)] = k.switch
                if (x,y,z) in d and k.switch == 0:
                    del d[(x,y,z)]
print(len(d))
### Part A End ###

def intersection(sign, c1, c2):
    xl = max(c1.x1, c2.x1) # low x
    xh = min(c1.x2, c2.x2) # high x
    yl = max(c1.y1, c2.y1)
    yh = min(c1.y2, c2.y2)
    zl = max(c1.z1, c2.z1)
    zh = min(c1.z2, c2.z2)
    if xl <= xh and yl <= yh and zl <= zh:
       np = Pt(sign, xl, xh, yl, yh, zl, zh)
    else: np = None
    return np

pool = []
for k in inp:
    new_cube = []
    for p in pool:
        sign = 1 if p.switch==0 else 0
        inter = intersection(sign, p, k)
        if inter: new_cube.append(inter)
    pool.extend(new_cube)
    if k.switch == 1: # 'On' cube
        pool.append(k)

vol = 0
for p in pool:
    size = (p.x2 - p.x1 + 1) * (p.y2 - p.y1 + 1) * (p.z2 - p.z1 + 1)
    vol += size * (1 if p.switch else -1)
print(vol)
