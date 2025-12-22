with open('in7.txt') as f:
    ll = f.read().splitlines()

from collections import namedtuple
P = namedtuple('P', ['x', 'y'])

splitter = set()
for y in range(len(ll)):
    for x in range(len(ll[0])):
        if ll[y][x] == 'S':

            start = P(x,y)
        elif ll[y][x] == '^':
            splitter.add(P(x,y))

beam = set()
beam.add(P(start.x, start.y+1))

def print_map():
    for y in range(len(ll)):
        li = []
        for x in range(len(ll[0])):
            if P(x,y) == start:
                li.append('S')
            elif P(x,y) in beam:
                li.append('|')
            elif P(x,y) in splitter:
                li.append('^')
            else:
                li.append('.')
        print(''.join(li))
    print()

cnt_split = 0
pn = {}
pn[P(start.x, start.y+1)] = 1

def add_paths(prev_pt: P, new_pt:P):
    global pn
    if new_pt not in pn:
        pn[new_pt] = 0
    pn[new_pt] = pn[new_pt] + pn[prev_pt]

for y in range(2,len(ll),2):
    # print(y, ll[y])
    for x in range(len(ll[0])):
        if P(x,y-1) in beam:
            if P(x,y) in splitter:
                cnt_split += 1
                if x>0:
                    beam.add(P(x-1,y))
                    beam.add(P(x-1,y+1))
                    add_paths(P(x,y-1), P(x-1,y+1))

                if x<len(ll[0]):
                    beam.add(P(x+1,y))
                    beam.add(P(x+1,y+1))
                    add_paths(P(x,y-1), P(x+1,y+1))
            else:
                beam.add(P(x,y))
                beam.add(P(x,y+1))
                add_paths(P(x,y-1), P(x,y+1))

print('part 1', cnt_split)

cnt_p = 0
for k,v in pn.items():
    if k.y == len(ll)-1:
        cnt_p += v
print('part 2', cnt_p)
