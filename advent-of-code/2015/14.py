import re
from collections import namedtuple
Ability = namedtuple('Ability', ['speed', 'stamina', 'rest_time'])
ll = open('in14.txt').read().splitlines()
d = {}
s = {}
score = {}
for l in ll:
    g = re.search(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', l).groups()
    d[g[0]] = Ability(int(g[1]), int(g[2]), int(g[3])) # d['name'] = (speed, stamina, rest_time)
    s[g[0]] = [0, 1,int(g[2])] # dist, flying?, cnt down
    score[g[0]] = 0

t = 0
while t < 2503:
    lead_dist = 0
    for k in s.keys():
        s[k][2] -= 1
        if s[k][1] == 1: # flying
            s[k][0] += d[k].speed
            if s[k][2] == 0:
               s[k][1] = 0
               s[k][2] = d[k].rest_time
        else: # resting
            if s[k][2] == 0:
               s[k][1] = 1
               s[k][2] = d[k].stamina
        lead_dist = max(lead_dist, s[k][0])

    for k, v in s.items():
        if v[0] == lead_dist:
            score[k] += 1
    t += 1
    #print(t, s)

print('Part A:', max(list(s.values()), key=lambda x: x[0])[0])
print('Part B:', max(list(score.values())))
