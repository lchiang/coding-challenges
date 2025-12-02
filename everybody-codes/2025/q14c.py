
f = open('in14c_test.txt')
patt = [list(x) for x in f.read().splitlines()]



mapp = [['.' for _ in range(34)] for _ in range(34)]

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

def match_pattern(d):
    match = True
    for y in range(4):
        for x in range(4):
            if patt[y][x] == '#' and (x+13,y+13) not in d:
                match = False
                break
            if patt[y][x] == '.' and (x+13,y+13) in d:
                match = False
                break
    return match


#13,14,15,16

#print_dict(d)

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

import os





while round < 2000:
    for y in range(map_h):
        for x in range(map_w):
            n = num_active_neighbour_n_self(x,y)
            if (n%2 == 0):
                dn[(x,y)] = '#'
            else:
                if (x,y) in d:
                    del dn[(x,y)]

    #print(round)
    
    print('round', round)    
    round += 1
    if round % 1000 == 0:
        print('round', round)    
    total_active += len(dn)
    
    print_dict(d)
    d = dn.copy()
    #print(total_active, map_active())




print('part 1, 2', total_active)
print('===')

end = time.time()
print(end - start)

