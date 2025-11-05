ll = open('./2022/23/test.txt').read().splitlines()
ll = open('./2022/23/input.txt').read().splitlines()

elves = set()
for y in range(len(ll)):
    for x in range(len(ll[0])):
        if ll[y][x]=='#' and (x,y) not in elves:
            elves.add((x,y))
#print(elves)

def print_map(elves):
    min_x = len(ll[0])+10
    min_y = len(ll)+10
    max_x = -10
    max_y = -10
    for e in elves:
        x, y = e
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    for y in range(min_y-3, max_y+4):
        line = []
        for x in range(min_x-3, max_x+4):
            if (x,y) in elves:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))

def count_map(elves):
    min_x = len(ll[0])+10
    min_y = len(ll)+10
    max_x = -10
    max_y = -10
    for e in elves:
        x, y = e
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    empty = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) not in elves:
                empty+=1
    return empty

def updatep(propose,ee, x, y):
    if (x,y) not in propose:
        propose[(x,y)] = ee
    else:
        del propose[(x,y)]

round = 0
#print_map(elves)
direction = 0
while round < 10000:
    propose = {}
    for ee in elves:
        x, y = ee
        n = (x,y-1) in elves
        s = (x,y+1) in elves
        e = (x+1,y) in elves
        w = (x-1,y) in elves
        ne = (x+1,y-1) in elves
        se = (x+1,y+1) in elves
        nw = (x-1,y-1) in elves
        sw = (x-1,y+1) in elves
        any_around = n or s or e or w or ne or se or nw or sw
        if any_around:
            if direction == 0:
                if not (n or ne or nw): updatep(propose,ee,x,y-1)
                elif not (s or se or sw): updatep(propose,ee,x,y+1)
                elif not (w or sw or nw): updatep(propose,ee,x-1,y)
                elif not (e or ne or se): updatep(propose,ee,x+1,y)
            elif direction == 1:
                if not (s or se or sw): updatep(propose,ee,x,y+1)
                elif not (w or sw or nw): updatep(propose,ee,x-1,y)
                elif not (e or ne or se): updatep(propose,ee,x+1,y)
                elif not (n or ne or nw): updatep(propose,ee,x,y-1)
            elif direction == 2:
                if not (w or sw or nw): updatep(propose,ee,x-1,y)
                elif not (e or ne or se): updatep(propose,ee,x+1,y)
                elif not (n or ne or nw): updatep(propose,ee,x,y-1)
                elif not (s or se or sw): updatep(propose,ee,x,y+1)
            elif direction == 3:
                if not (e or ne or se): updatep(propose,ee,x+1,y)
                elif not (n or ne or nw): updatep(propose,ee,x,y-1)
                elif not (s or se or sw): updatep(propose,ee,x,y+1)
                elif not (w or sw or nw): updatep(propose,ee,x-1,y)

    round += 1
    direction = (direction+1)%4

    for k,v in propose.items():
        elves.remove(v)
        elves.add(k)
    #print_map(elves)

    if (len(propose)==0):
        print('Part B',round)
        break

    if (round==10):
        print('Part A', count_map(elves))
