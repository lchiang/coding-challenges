f = open('in17c_test1.txt')
f = open('in17c_test2.txt')
f = open('in17c_test3.txt')
f = open('in17c.txt')

mapp = [list(x) for x in f.read().splitlines()]
map_w = len(mapp[0])
map_h = len(mapp)
mapd = set()

def print_dict(dd):
    for y in range(map_h):
        l = []
        for x in range(map_w):
            if (x,y) in dd:
                l.append(mapp[y][x])
            else:
                l.append('.')
        print(''.join(l))
    print()

for y in range(map_h):
    for x in range(map_w):
        if mapp[y][x] == '@':
            xv, yv = x,y
        elif mapp[y][x] == 'S':
            xs, ys = x,y
        else:
            mapd.add((x,y))

line_below_v = set()
for y in range(yv, map_h+1):
    line_below_v.add((xv, y))

def in_range(x, y, r):
    return ((xv - x) * (xv - x) + (yv - y) * (yv - y)) <= (r * r)

def part_1():
    sum_of_cell = 0
    for y in range(map_h):
        for x in range(map_w):
            if in_range(x,y) and not ((x,y)==(xv,yv)) and not ((x,y)==(xs,ys)):
                sum_of_cell += int(mapp[y][x])
    print('part 1:', sum_of_cell)

def part_2():
    max_destroy = 0
    max_des_round = None
    destroy_this_round = set()
    remain = mapd.copy()
    for round in range(map_h):
        for (x,y) in remain:
            if in_range(x,y,round):
                destroy_this_round.add((x,y))
        sum_of_destroy = sum([int(mapp[y][x]) for (x,y) in destroy_this_round])
        if sum_of_destroy > max_destroy:
            max_destroy = sum_of_destroy
            max_des_round = round
        remain = remain - destroy_this_round
        destroy_this_round = set()
    print('part 2:', max_destroy * max_des_round)

import heapq
def dijkstra(side, round):
    dist = {}
    dist[(xs,ys)] = 0
    pq = []
    heapq.heappush(pq, (0, (xs,ys)))
    NEIGHBORS = [(-1,0), (1,0), (0,-1), (0,1)]
    while pq:
        d, (xu, yu) = heapq.heappop(pq)
        if d > dist[(xu, yu)]:
            continue
        for dx,dy in NEIGHBORS:
            nx, ny = xu + dx, yu + dy
            if (nx,ny) not in mapd or (nx,ny) in dist or in_range(nx, ny, round) or \
               (side == 'left' and nx > xv) or (side == 'right' and (nx < xv and ny > yv)):
                continue
            dist[(nx,ny)] = dist[(xu, yu)] + int(mapp[ny][nx])
            heapq.heappush(pq, (dist[(nx,ny)], (nx,ny)))
            # print('123', (dist[(nx,ny)], (nx,ny)), pq)
    return dist

def dijkstra_left(round):
    return dijkstra('left', round)

def dijkstra_right(round):
    return dijkstra('right', round)

for round in range(1, 110):
    dl = dijkstra_left(round)
    dr = dijkstra_right(round)
    min_cost = 10**12
    for c in line_below_v:
        if c in dl and c in dr:
            total_cost = dl[c] + dr[c]- int(mapp[c[1]][c[0]])
            min_cost = min(total_cost, min_cost)
            print(min_cost, c)
    print(f'Round {round}: {min_cost} {(round+1) * 30}')
    if min_cost < (round+1) * 30:
        print('part 3:', min_cost * round)
        break
