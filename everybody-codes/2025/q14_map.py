f = open('in14a_test.txt')
f = open('everybody_codes_e2025_q14_p2.txt')

mapp = [list(x) for x in f.read().splitlines()]

map_w = len(mapp[0])
map_h = len(mapp)

def print_map(m):
    for y in range(len(m)):
        print(''.join(m[y]))
    print()

print_map(mapp)


def is_active(x, y):
    return 0 <= x < map_w and 0 <= y < map_h and mapp[y][x] == '#'

def num_active_neighbour(x,y):
    count = 0
    if is_active(x-1, y-1): count += 1
    if is_active(x-1, y+1): count += 1
    if is_active(x+1, y-1): count += 1
    if is_active(x+1, y+1): count += 1
    return count

def map_active():
    a = 0
    for y in range(map_h):        
        for x in range(map_w):
            if mapp[y][x] == '#':
                a += 1
    return a

print(num_active_neighbour(2,2))


round = 0

'''
If a tile is active, it will remain active in the next round if the number of active diagonal neighbours is odd. Otherwise, it becomes inactive.
If a tile is inactive, it will become active in the next round if the number of active diagonal neighbours is even. Otherwise, it remains inactive.
Below are a few examples of 3x3 ti

active odd -> active
active even -> inactive
inactive odd -> inactive
inactive even -> active
'''

import time

start = time.time()


import copy
mapn = copy.deepcopy(mapp)

total_active = 0

while round < 2025:
    

    for y in range(map_h):        
        for x in range(map_w):
            n = num_active_neighbour(x,y)
            if (is_active(x,y) and n%2 == 1) or (not is_active(x,y) and n%2 == 0):
                mapn[y][x] = '#'
            else:
                mapn[y][x] = '.'
    round += 1
    if round % 100 == 0:
        print('round', round)
    #print_map(mapn)

    mapp = copy.deepcopy(mapn)
    #total_active += map_active()
    total_active += sum(x.count('#') for x in mapp)
    #print(total_active, map_active())


print('part 1, 2', total_active)
print('===')

print(sum(x.count('#') for x in mapp))

print("hello")
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