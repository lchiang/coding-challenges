f = open('in12c_test2.txt')
#f = open('everybody_codes_e2025_q12_p1.txt')
#f = open('everybody_codes_e2025_q12_p2.txt')
f = open('everybody_codes_e2025_q12_p3.txt')
mapp = f.read().splitlines()
m = [list(map(int, line)) for line in mapp]

map_w = len(m[0])
map_h = len(m)
burnt_list = []

from collections import namedtuple
P = namedtuple('P', ['x', 'y'])

def print_map(m):
    for row in m:
        print(''.join(map(str, row)))
    print()

import copy
def print_list(l):
    ma = copy.deepcopy(m)
    for y in range(map_h):        
        for x in range(map_w):
            ma[y][x] = '*' if (x,y) in l else '.'
    print_map(ma)


print_map(m)

def inmap(x,y):
    return 0 <= x < map_w and 0 <= y < map_h
    
def ignite(x,y,bl,rl):
    igl = []
    if inmap(x-1, y) and m[y][x] >= m[y][x-1] and P(x-1,y) not in bl and P(x-1,y) in rl:
        igl.append(P(x-1, y))
    if inmap(x+1, y) and m[y][x] >= m[y][x+1] and P(x+1,y) not in bl and P(x+1,y) in rl:
        igl.append(P(x+1, y))
    if inmap(x, y-1) and m[y][x] >= m[y-1][x] and P(x,y-1) not in bl and P(x,y-1) in rl:
        igl.append(P(x, y-1))
    if inmap(x, y+1) and m[y][x] >= m[y+1][x] and P(x,y+1) not in bl and P(x,y+1) in rl:
        igl.append(P(x, y+1))
    return igl


def burn_tiles(pl,rl):
    burnt_l = []
    r = 0
    burning_l = pl.copy()
    burnt_l.extend(burning_l)

    while len(burning_l) > 0:
        #print('round', r)
        ignite_l = []
        for p in burning_l:
            ignite_l.extend(ignite(p.x, p.y, burnt_l, rl))
        ignite_l = list(set(ignite_l))
        burning_l = ignite_l
        burnt_l = list(set(burnt_l) | set(ignite_l))
        
        # print(ignite_l)
        r+=1
    return burnt_l

rrr = {}
for y in range(map_h):        
    for x in range(map_w):
        rrr[P(x,y)] = m[y][x]
remain = [k for k, v in sorted(rrr.items(), key=lambda x: x[1], reverse=True)]
print('=========')

max_p1, max_p2, max_p3 = None, None, None

from datetime import datetime

max_bl = []
max_n = 0
rr = 0
checked = []
for p in remain:    
    rr+=1    
    if p not in checked:
        start = datetime.now()
        b = burn_tiles([p], remain)
        removed = len(list(set(b) - set(checked)))
        checked = list(set(checked) | set(b))
        
        if len(b) > max_n:  
            max_n = len(b)
            max_p1 = p
            max_bl = b.copy()
        end = datetime.now()
        print('checking', p, m[p.y][p.x], '|', len(b), removed, len(checked),'|',round((end-start).total_seconds()*1000))
    #else:
    #    print('removed', p)
    #print(rr, max_n, p, m[p.y][p.x], len(checked), len(b))
remain = list(set(remain) - set(max_bl))

max_bl = []
max_n = 0
for p in remain:    
    b = burn_tiles([p], remain)
    if len(b) > max_n:  
        max_n = len(b)
        max_p2 = p
        max_bl = b.copy()
remain = list(set(remain) - set(max_bl))

max_bl = []
max_n = 0
for p in remain:    
    b = burn_tiles([p], remain)
    if len(b) > max_n:  
        max_n = len(b)
        max_p3 = p
        max_bl = b.copy()
remain = list(set(remain) - set(max_bl))


print()
print(max_p1, max_p2, max_p3)

remain = []
for y in range(map_h):        
    for x in range(map_w):
        remain.append(P(x,y))

b = burn_tiles([max_p1, max_p2, max_p3], remain)
print(len(b))
'''
max_round = 200
r = 0
burning_list = [P(0,0)]
burnt_list.extend(burning_list)

while r < max_round:
    print('round', r)
    ignite_list = []
    for p in burning_list:
        ignite_list.extend(ignite(p.x, p.y, burnt_list))

    ignite_list = list(set(ignite_list))

    burning_list = ignite_list

    burnt_list = list(set(burnt_list) | set(ignite_list))        
    #print('ignite_list', len(ignite_list))
    #print('burning_list', len(burning_list))
    #print('burnt_list', len(burnt_list))
    print('ignite_list', ignite_list)
    #print_list(ignite_list)
    if len(ignite_list) == 0:
        print(len(burnt_list))
        break

    #print('burning_list', burning_list)
    #print('burnt_list', burnt_list)
    
    r += 1
'''