with open('in19b.txt') as f:
    ll = [list(map(int, line.strip().split(','))) for line in f]

from collections import namedtuple
from typing import List
Point = namedtuple('Point', ['x', 'y'])

rd = {}
sd = {Point(x, y) for x, y0, le in ll for y in range(y0, y0 + le)}
wall_at = sorted({x for x, _, _ in ll})

def can_reach_from(c: Point, prev: List[Point]):
    min_flap = None
    for p in prev:
        dx, dy = c.x-p.x, c.y-p.y
        if abs(dy) <= (dx):
            yflap = max(dy ,0)
            xflap = (dx-abs(dy))//2
            min_flap = min(min_flap if min_flap else 10**12, yflap+xflap+rd[p])
    return min_flap

rd[Point(0,0)] = 0
prev_reach = [Point(0,0)]

for w in wall_at:
    # print('line', w, len(prev_reach))
    seg = [pt for pt in sd if pt.x == w and (pt.x+pt.y)%2 == 0]
    reach = []
    for pt in seg:
        flap = can_reach_from(pt, prev_reach)
        if flap is not None:
            rd[Point(pt.x, pt.y)] = flap
            reach.append(Point(pt.x, pt.y))
    prev_reach = reach

min_step = min(rd[r] for r in rd if r.x == wall_at[-1])
print('Answer: ',min_step)
