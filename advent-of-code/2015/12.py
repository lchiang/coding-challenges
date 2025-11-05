ll = open('in12.txt').read().splitlines()[0]

import re
a = 0
m = re.findall(r'(-?\d+)', ll)
for g in m:
    a += int(g)
print('Part A:',a)

import json
d = json.loads(ll)
def count(l):
    if isinstance(l, int):    return l
    elif isinstance(l, str):  return 0
    elif isinstance(l, dict): return sum([count(v) if 'red' not in l.values() else 0 for v in l.values()])
    elif isinstance(l, list): return sum([count(e) for e in l])
    else: raise ValueError('type', type(l), l)
print('Part B:', count(d))
