ll = open('in13.txt').read().splitlines()
d = {}
for l in ll:
    if l.split()[0][0] not in d:
        d[l.split()[0][0]] = {}
    d[l.split()[0][0]][l.split()[-1][0]] = int(('' if l.split()[2] == 'gain' else '-') + l.split()[3])

# Part B: Adding Self BEGIN
zd = {}
for k,v in d.items():
    zd[k] = 0
    d[k]['Z'] = 0
d['Z'] = zd
# Part B: Adding Self END

ppl = list(d.keys())

import itertools
comb = [[ppl[0]] + list(k) for k in itertools.permutations(ppl[1:])]
highest = 0
for c in comb:
    m = 0
    for i in range(len(c)):        
        l = c[i-1]
        r = c[(i+1)%len(c)]
        dd = d[c[i]]
        m += dd[l] + dd[r]
    highest = max(highest, m)
print(highest)
