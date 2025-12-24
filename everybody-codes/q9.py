with open('in9.txt') as f:
    ll = f.read().splitlines()

import math
from collections import namedtuple, deque
P = namedtuple('P', ['x', 'y'])

ps = [P(*map(int, line.split(','))) for line in ll]

def draw_polygon_to_svg(width, height, points, filename='polygon.svg'):
    min_x, max_x = min(x for x, y in points), max(x for x, y in points)
    min_y, max_y = min(y for x, y in points), max(y for x, y in points)
    range_x, range_y = max_x - min_x, max_y - min_y
    scale   = min(width  / (range_x + 1), height / (range_y + 1))
    padding = int(min(width, height) * 0.05)
    w  = int(range_x * scale + 2 * padding)
    h = int(range_y * scale + 2 * padding)

    def to_svg_coords(x, y):
        sx = (x - min_x) * scale + padding
        sy = h - ((y - min_y) * scale + padding)
        return sx, sy

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'  <rect x="0" y="0" width="{w}" height="{h}" fill="white"/>'
    ]
    poly_points = " ".join(f"{to_svg_coords(x,y)[0]:.2f},{to_svg_coords(x,y)[1]:.2f}" for x,y in points)
    svg_parts.append(f'  <polygon points="{poly_points}" fill="none" stroke="black" stroke-width="2"/>')
    svg_parts.append('</svg>')
    svg_content = "\n".join(svg_parts)

    with open(filename, "w", encoding="utf-8") as sf:
        sf.write(svg_content)

draw_polygon_to_svg(800,600,ps)

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

    print_map(green)
    queue = deque([start])
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

def get_max_area2():
    global green_tiles
    max_area = 0
    for i in range(len(compressed)):
        for j in range(len(compressed)):
            p1, p2 = compressed[i], compressed[j]
            st_x, en_x = min(p1.x, p2.x), max(p1.x, p2.x)
            st_y, en_y = min(p1.y, p2.y), max(p1.y, p2.y)
            outside = False
            for x in range(st_x, en_x+1):
                for y in range(st_y, en_y+1):
                    if (x,y) not in green_tiles:
                        outside = True
                        break
            if not outside:
                a = (abs(x_rev_map[p1.x] - x_rev_map[p2.x]) + 1) * (abs(y_rev_map[p1.y] - y_rev_map[p2.y]) + 1)
                max_area = max(max_area, a)
    return max_area
print('Part 2: ', get_max_area2())
