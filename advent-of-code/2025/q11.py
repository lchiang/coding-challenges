with open('in11.txt') as f:
    ll = f.read().splitlines()

from collections import defaultdict

g = defaultdict(set)
for l in ll:
    k, v = l.split(':')
    g[k] = v.split()

from functools import cache

@cache
def find_paths_num(start, end, avoid):
    if start == end:
        return 1
    if start not in g:
        return 0
    n = 0
    for neighbor in g[start]:
        if neighbor not in avoid:
            n += find_paths_num(neighbor, end, avoid)
    return n

dac_fft = find_paths_num('dac', 'fft', ('svr','out'))
fft_dac = find_paths_num('fft', 'dac', ('svr','out'))
print(dac_fft)
print(fft_dac)

if fft_dac:
    re = find_paths_num('svr', 'fft', ('dac','out')) * fft_dac * find_paths_num('dac', 'out', ('svr','fft'))
else:
    re = find_paths_num('svr', 'dac', ('fft','out')) * dac_fft * find_paths_num('fft', 'out', ('dac','fft'))
print('part 2: ', re)
