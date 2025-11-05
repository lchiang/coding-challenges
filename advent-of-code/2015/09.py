from re import search
from itertools import permutations 

ll = open('in09.txt').read().splitlines()
d = {}
dest = []
for l in ll:
    m = search(r'(\w+) to (\w+) = (\d+)', l)
    d1, d2, d3 = m.groups()
    d[(d1,d2)] = int(d3)
    d[(d2,d1)] = int(d3)
    if d1 not in dest: dest.append(d1)
    if d2 not in dest: dest.append(d2)
min_d = 9999999999999
max_d = 0
for p in permutations(dest):
    dd = 0
    for i in range(len(p)-1):
        dd += d[(p[i],p[i+1])]
    min_d = min(min_d, dd)
    max_d = max(max_d, dd) 
print(min_d, max_d)
