s = '3113322113'
from itertools import groupby
for step in range(50):
    q = ''
    for k, g in groupby(s):
        q += str(len(list(g))) + str(k)
    s = q
    print('{:3}'.format(step+1), len(s))
