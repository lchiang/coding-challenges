f = open('in10b.txt')
mapp = f.read().splitlines()

def print_map(m):
    for y in range(len(m)):
        print(''.join(m[y]))
    print()

import copy
def print_points(pl, clean_map, c):
    m = copy.deepcopy(mapp)
    for y in range(map_h):        
        for x in range(map_w):
            if clean_map:
                m[y][x] = '.'
            if (x,y) in pl:
                m[y][x] = c
    print_map(m)

def print_pts(pl, c):
    return print_points(pl,True,c)


def next_by_pt_list(pl):
    l = []
    for pt in pl:
        l.append(Point(pt.x-1, pt.y-2))
        l.append(Point(pt.x+1, pt.y-2))
        l.append(Point(pt.x-2, pt.y-1))
        l.append(Point(pt.x+2, pt.y-1))
        l.append(Point(pt.x-2, pt.y+1))
        l.append(Point(pt.x+2, pt.y+1))
        l.append(Point(pt.x-1, pt.y+2))
        l.append(Point(pt.x+1, pt.y+2))    
    pl = []
    for p in l:
        if 0 <= p.x < map_w and 0 <= p.y < map_h and p not in pl:
            pl.append(p)
    return pl

for i in range(len(mapp)):
    mapp[i] = list(mapp[i])
    
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

map_w = len(mapp[0])
map_h = len(mapp)

sheep_list = []
hideout_list = []

for y in range(map_h):
    for x in range(map_w):
        if mapp[y][x] == 'D':            
            dragon_start = Point(x, y)
        if mapp[y][x] == 'S':
            sheep_list.append(Point(x, y))
        if mapp[y][x] == '#':
            hideout_list.append(Point(x, y))

''' Part i Start '''
def reach_in_step(step, pl):
    l = pl.copy()
    for p in pl:
        ns = next_by_pt_list([p])
        for n in ns:
            if n not in l:
                l.append(n)
    return l if step == 1 else reach_in_step(step-1, l)   
    
def count_sheep(pl):
    cnt = 0
    for p in pl:        
        if mapp[p.y][p.x] == 'S':
            cnt += 1    
    return cnt
print('part i', count_sheep(reach_in_step(4,[dragon_start])))
''' Part i End '''

''' Part ii Start '''
def sheep_move(sl):
    l = []
    for s in sl:
        if s.y+1 <= map_h:
            l.append(Point(s.x, s.y+1))
    return l

round = 2
r = 0
dl = [dragon_start]
sl = sheep_list.copy()
total_eat_cnt = 0
while r < round:
    #print('==== ROUND:', r , '====')
    round_eat_cnt = 0    
    r += 1
    dl = next_by_pt_list(dl)
    eaten = []    
    for s in sl:
        if s in dl and s not in hideout_list:
            round_eat_cnt += 1
            eaten.append(s)
    for e in eaten:
        sl.remove(e)
    sl = sheep_move(sl)
    eaten = []
    for s in sl:
        if s in dl and s not in hideout_list:
            round_eat_cnt += 1
            eaten.append(s)
    for e in eaten:
        sl.remove(e)    
    total_eat_cnt += round_eat_cnt
print('part ii', total_eat_cnt)
''' Part ii Start '''