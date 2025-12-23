with open('in9.txt') as f:
    ll = f.read().splitlines()

import math
from collections import namedtuple, deque
P = namedtuple('P', ['x', 'y'])

ps = [P(*map(int, line.split(','))) for line in ll]


# start1 = time.perf_counter()
# max_area = 0
# area = []
# for i in range(len(ps)):
#     for j in range(len(ps)):
#         p1, p2 = ps[i], ps[j]
#         a = (abs(p1.x - p2.x)+1) * (abs(p1.y - p2.y)+1)
#         area.append(((p1, p2), a))
#         max_area = max(max_area, a)
# area.sort(key=lambda x: x[1])
# end1 = time.perf_counter()
# print(f"Elapsed time: {end1 - start1:.6f} seconds")

# print(max_area)

def print_map(m):
    mx, my = 0,0
    for x,y in m:
        mx = max(mx, x)
        my = max(my, y)
    for y in range(my+1):
        li = []
        for x in range(mx+1):
            if P(x,y) in m: li.append('#')
            else: li.append('.')
        print(''.join(li))
    print()




# --- Coordinate compression ---
xs = sorted(set(p.x for p in ps))
ys = sorted(set(p.y for p in ps))

# Maps from original to compressed
x_map = {x: i for i, x in enumerate(xs)}
y_map = {y: i for i, y in enumerate(ys)}


x_rev_map = {i: x for i, x in enumerate(xs)}
y_rev_map = {i: y for i, y in enumerate(ys)}

# Compressed points
compressed = [P(x_map[p.x], y_map[p.y]) for p in ps]

# --- Compute max area using compressed coordinates ---

def get_max_area1():
    max_area = 0
    for i in range(len(compressed)):
        for j in range(len(compressed)):
            p1, p2 = compressed[i], compressed[j]
            a = (abs(x_rev_map[p1.x] - x_rev_map[p2.x]) + 1) * (abs(y_rev_map[p1.y] - y_rev_map[p2.y]) + 1)
            max_area = max(max_area, a)
    return max_area

print('Part 1: ', get_max_area1())


def get_green_list(m, start):
    green = set()
    for i in range(len(m)):
        p1, p2 = m[i], m[(i+1)%len(m)]
        for x in range(min(p1.x, p2.x), max(p1.x, p2.x)+1):
            for y in range(min(p1.y, p2.y), max(p1.y, p2.y)+1):
                green.add(P(x,y))
        # print(p1, p2, [x for x in range(min(p1.x, p2.x), max(p1.x, p2.x)+1)],[y for y in range(min(p1.y, p2.y), max(p1.y, p2.y)+1)])

    print_map(green)
    queue = deque([start])
    # Define bounding box to avoid infinite expansion
    min_x = min(p.x for p in green) - 1
    max_x = max(p.x for p in green) + 1
    min_y = min(p.y for p in green) - 1
    max_y = max(p.y for p in green) + 1

    while queue:
        p = queue.popleft()
        if p in green:
            continue
        if not (min_x <= p.x <= max_x and min_y <= p.y <= max_y):
            continue
        green.add(p)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            queue.append(P(p.x + dx, p.y + dy))
    return green


green_tiles = get_green_list(compressed, P(120,190))
print_map(green_tiles)


def get_max_area2():
    max_area = 0
    for i in range(len(compressed)):
        for j in range(len(compressed)):
            p1, p2 = compressed[i], compressed[j]
            #TODO check if all tiles are in green_tiles
            a = (abs(x_rev_map[p1.x] - x_rev_map[p2.x]) + 1) * (abs(y_rev_map[p1.y] - y_rev_map[p2.y]) + 1)
            max_area = max(max_area, a)
    return max_area

print('Part 2: ', get_max_area2())
