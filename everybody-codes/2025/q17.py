f = open('in17c_test1.txt')
# f = open('in17b.txt')


mapp = [list(x) for x in f.read().splitlines()]
map_w = len(mapp[0])
map_h = len(mapp)

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

mapd = set()

line_below_v = set()

for y in range(map_h):
    for x in range(map_w):
        if mapp[y][x] == '@':
            xv, yv = x,y
        elif mapp[y][x] == 'S':
            xs, ys = x,y
        else:
            mapd.add((x,y))

for y in range(yv, map_h+1): #Add 1?
    line_below_v.add((xv, y))

# left side of each round = remain with y <= yv
# below is viped, so we can do simple DFS

import heapq




# right side of each round = remain with y >= yv

def in_range(x, y, r=10):
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

part_2()

def map_after_round(round):

    remain = mapd.copy()
    will_destroy = set()

    for (x,y) in remain:
        if in_range(x,y,round):
            will_destroy.add((x,y))
    remain = remain - will_destroy
    return remain



def dijkstra_left():
    dist = {}
    dist[(xs,ys)] = 0
    pq = []
    heapq.heappush(pq, (0, (xs,ys)))
    NEIGHBORS = [(-1,0), (1,0), (0,-1), (0,1)]


    while pq:
        d, (xu, yu) = heapq.heappop(pq)
        # print(pq)

        if d > dist[(xu, yu)]:
            continue

        for dx,dy in NEIGHBORS:
            nx, ny = xu + dx, yu + dy


            if (nx,ny) not in mapd or (nx,ny) in dist or in_range(nx, ny, 2) or nx > yv:
                continue
            print((nx,ny))
            '''
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))
            '''
            dist[(nx,ny)] = dist[(xu, yu)] + int(mapp[ny][nx])
            print(dist)
            heapq.heappush(pq, (dist[(nx,ny)], (nx,ny)))
            # print('123', (dist[(nx,ny)], (nx,ny)), pq)

    # Return the final shortest distances from the source
    return dist
dl = dijkstra_left()

print_dict(mapd)
print_dict(dl)
'''
def print_dict(dd):
    for y in range(map_h):
        l = []
        for x in range(map_w):
            if (x,y) in dd:
                l.append('@')
            else:
                l.append('.')
        print(''.join(l))
    print()

def get_adjacent(x,y):
    count = 0
    NEIGHBORS = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
    for dx,dy in NEIGHBORS:
        if (x + dx, y + dy) in paper:
            count += 1
    return count

def can_remove(x,y):
    adjacent_count = get_adjacent(x,y)
    return adjacent_count < 4

to_remove = set()
total_removed = 0
for round in range(1000):
    for (x,y) in paper:
        if can_remove(x,y):
            to_remove.add((x,y))
    if round == 0:
        print(f'Part 1: {len(to_remove)}')
    if not to_remove:
        break
    total_removed += len(to_remove)
    paper = paper - to_remove
    to_remove = set()
# print_dict(paper)
print(f'Part 2: {total_removed}')
'''