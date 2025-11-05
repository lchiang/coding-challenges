#ll = open('./2022/15/test.txt').read().splitlines()
ll = open('./2022/15/input.txt').read().splitlines()

import re
from collections import namedtuple

Point = namedtuple("Point", "x y")

def scanned_distance(line_num,s,dist):
    dd = dist-abs(line_num-s.y)
    if (dd<0):
        return None
    return (s.x-dd, s.x+dd)

def union_two_range(a,b):
    a0, a1 = a[0], a[1]
    b0, b1 = b[0], b[1]
    if ((a0 > b1) or (b0 > a1)): # not overlap
        return [a, b]
    else:
        return [(min(a0, b0), max(a1, b1))]

def merge_range(list_of_range):
    rl = list_of_range
    if len(rl)==1:
        return rl
    else:
        new_list = rl.copy()
        for i in range(len(rl)-1):
            tt = union_two_range(rl[i], rl[i+1])
            if (len(tt)==1):
                new_list.remove(rl[i])
                new_list.remove(rl[i+1])
                new_list.extend(tt)
                new_list.sort()
                return merge_range(new_list)
        return rl

def union_list_range(list,a):
    if len(list)==1:
        return union_two_range(list[0], a)
    else:
        list.sort()
        temp_u_list = []
        for r in list:
            temp_u_list.extend(union_two_range(r, a))
        return merge_range(temp_u_list)

def all_possible_position(target_line):
    co = [] # all coverage
    for s in sensors:
        dist = abs(s[0].x-s[1].x) + abs(s[0].y-s[1].y)
        coverage = scanned_distance(target_line,s[0],dist)
        if coverage is not None:
            co.append(coverage)
    co.sort()
    uu = [(co[0][0], co[0][1])]
    for c in co[1:]:
        uu = union_list_range(uu, (c[0], c[1]))
    return uu

sensors = []
for l in ll:
    result = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", l)
    xs, ys, bs, bs = result.groups()
    s = Point(int(result.group(1)), int(result.group(2)))
    b = Point(int(result.group(3)), int(result.group(4)))
    sensors.append((s,b))

### Part A ###
tl = 2000000
#tl = 10 # test input
uu = all_possible_position(tl)
sb=set()
for s in sensors:
    if (s[0].y==tl and uu[0][0]<=s[0].x and s[0].x<=uu[0][1]):
        sb.add(s[0])
    if (s[1].y==tl and uu[0][0]<=s[1].x and s[1].x<=uu[0][1]):
        sb.add(s[1])
print('Part A', uu[0][1]-uu[0][0]+1-len(sb))

### Part B ###
#for y in range(0, 4000000+1):
for y in range(2647445, 2647450):
    yy = all_possible_position(y)
    if (len(yy)>1):
        print(y, yy)

x = 3131431
y = 2647448
print('Part B', x*4000000 + y)
