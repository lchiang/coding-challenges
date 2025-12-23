f = open('in10c_t1.txt')
mapp = f.read().splitlines()

def print_map1(m):
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
    print_map1(m)


import copy
def print_map3(sl3, d):
    global hideout_list
    for y in range(map_h):
        l = []
        for x in range(map_w):
            if (x,y) == d: l.append('D')
            elif sl3[x]==y: l.append('S')
            elif (x,y) in hideout_list: l.append('#')
            else: l.append('.')
        print(''.join(l))
    print()


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
sl3 = [None] * map_w

for y in range(map_h):
    for x in range(map_w):
        if mapp[y][x] == 'D':
            dragon_start = Point(x, y)
        if mapp[y][x] == 'S':
            sheep_list.append(Point(x, y))
            sl3[x] = y
        if mapp[y][x] == '#':
            hideout_list.append(Point(x, y))

escape_spots = set()
for h in hideout_list:
    touches_bottom = True
    for j in range(h.y,map_h):
        if (h.x,j) not in hideout_list:
            touches_bottom = False
    if touches_bottom:
        escape_spots.add(h)



    # if (x,y) in hideout_list for y from i to map_h
    # then (x,y) for the smallest y add to save_spots

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


def part_2():
    def sheep_move(sl):
        l = []
        for s in sl:
            if s.y+1 <= map_h:
                l.append(Point(s.x, s.y+1))
        return l

    r = 0
    dl = [dragon_start]
    sl = sheep_list.copy()
    total_eat_cnt = 0
    while r < 2:
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

# part_2()

win_cnt = 0
def next_step(sl: list[Point], d, step_str):
    global win_cnt
    print('in next_step', step_str)

    for x in range(len(sl)):
        if sl[x] is not None:
            l = sl.copy()
            next_pos = Point(x, sl[x]+1)
            if next_pos == d and next_pos not in hideout_list:
                continue

            if next_pos in escape_spots or next_pos.y == map_h: # sheep escaped
                l[x] = None
                print('LOSS')
            else:
                l[x] = sl[x]+1

                # print('sheep move', (next_pos.x, next_pos.y))
                step_str += 'S' + f'{next_pos.x}{next_pos.y} '
                print_map3(l, d)

                next_d = next_by_pt_list([d])
                for nd in next_d:

                    nl = l.copy()
                    if nl[nd.x] == nd.y:
                        nl[nd.x] = None
                        # print('ate ', nd)
                    if all(x is None for x in nl):
                        win_cnt += 1
                        print('===win_cnt', win_cnt)
                    else:
                        # print('dragon move', (nd.x, nd.y))
                        step_str += 'D' + f'{nd.x}{nd.y} '
                        # print_map3(nl, nd)
                        next_step(nl, nd, step_str)











next_step(sl3, dragon_start,'')