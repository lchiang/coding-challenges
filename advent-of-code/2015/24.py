ll = open('in24.txt').read().splitlines()
ll = [int(x) for x in ll]

w = sum(ll) // 3
pp = sorted(ll, reverse=True)
fewest_pack = len(ll)
fpl = []

def grp(g, limit):
    if len(g) < limit:
        p = [x for x in pp if x < min(g)] if g else pp.copy()

        for e in p:
            ng = sum(g) + e
            np = sum(p) - e
            if ng == w:
                global fewest_pack, fpl
                if len(g+[e]) == fewest_pack:
                    fpl.append(g+[e])
                elif len(g+[e]) < fewest_pack:
                    fewest_pack = len(g+[e])
                    fpl.clear()
                    fpl.append(g+[e])
                #print('done',g+[e])
            elif ng < w and ng + np >= w:
                grp(g+[e], limit)

grp([], len(pp)//3)
import math
miqe = math.prod(ll)
fpp = []
for fl in fpl:
    p = math.prod(fl)
    if p < miqe:
        miqe = p
        fpp = fl
print(miqe, fpp)
