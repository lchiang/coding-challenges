f = open('in14a_test.txt')
f = open('everybody_codes_e2025_q14_p2.txt')

mapp = [list(x) for x in f.read().splitlines()]

map_w = len(mapp[0])
map_h = len(mapp)

d = {}
for y in range(map_h):
    for x in range(map_w):
        if mapp[y][x] == '#':
            d[(x,y)] = '#'

def print_dict(dd):
    for y in range(map_h):
        l = []
        for x in range(map_w):
            if (x,y) in dd:
                l.append('#')
            else:
                l.append('.')
        print(''.join(l))
    print()

print_dict(d)

def num_active_neighbour_n_self(x,y):
    count = 0
    if (x, y) in d: count += 1
    if (x-1, y-1) in d: count += 1
    if (x-1, y+1) in d: count += 1
    if (x+1, y-1) in d: count += 1
    if (x+1, y+1) in d: count += 1
    return count



import time
start = time.time()

round = 0
dn = d.copy()
total_active = 0

while round < 2025:
    for y in range(map_h):
        for x in range(map_w):
            n = num_active_neighbour_n_self(x,y)
            if (n%2 == 0):
                dn[(x,y)] = '#'
            else:
                if (x,y) in d:
                    del dn[(x,y)]
    round += 1
    if round % 100 == 0:
        print('round', round)

    total_active += len(dn)
    d = dn.copy()
    #print(total_active, map_active())


print('part 1, 2', total_active)
print('===')

end = time.time()
print(end - start)


'''

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

for i in range(len(mapp)):
    mapp[i] = list(mapp[i])

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])


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
'''