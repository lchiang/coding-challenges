with open('in20c.txt') as f:
    mapp = [list(x) for x in f.read().splitlines()]

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

def print_map(m):
    for row in m:
        print(''.join(map(str, row)))
    print()


def print_dict(d):
    for y in range(len(mapp)):
        l = []
        for x in range(len(mapp[0])):
            l.append(d[(x,y)] if (x,y) in d else ' ')
        print(''.join(l))
    print()

def print_set(d, ch='#'):
    for y in range(len(mapp)):
        l = []
        for x in range(len(mapp[0])):
            l.append(ch if (x,y) in d else ('.' if mapp[y][x] != '.' else ' '))
        print(''.join(l))
    print()

st, ed = None, None

mapd = {}
for y in range(len(mapp)):
    for x in range(len(mapp[0])):
        if mapp[y][x] == '.':
            continue
        else:
            mapd[Point(x,y)] = mapp[y][x]
            if mapp[y][x] == 'S':
                st = Point(x,y)
            elif mapp[y][x] == 'E':
                ed = Point(x,y)

# print_map(mapp)
# print_dict(mapd)

def adj(p: Point):
    a = set()
    if Point(p.x-1, p.y) in mapd: a.add(Point(p.x-1, p.y))
    if Point(p.x+1, p.y) in mapd: a.add(Point(p.x+1, p.y))
    if (p.x + p.y) % 2 == 0:
        if Point(p.x, p.y-1) in mapd: a.add(Point(p.x, p.y-1))
    else:
        if Point(p.x, p.y+1) in mapd: a.add(Point(p.x, p.y+1))
    return a

def r(p: Point):
    x = p.x
    y = p.y
    n = len(mapp[0])//2+1 # SIDE LENGTH
    m = 2*(n-1)
    if (x+y)%2 == 0:
        # down (even)
        x1 = (-x+(3*y)+m)//2
        y1 = (-x-y+m)//2
    else:
        # up (odd)
        x1 = (-x+(3*y)+m+1)//2
        y1 = (-x-y+m-1)//2
    return Point(x1,y1)

def part1():
    pairs = set()
    for k, v in mapd.items():
        # print(k, v)
        if v=='T':
            a = adj(k)
            for aa in a:
                if aa in mapd and mapd[aa] == 'T':
                    # print(k, aa)
                    pairs.add(frozenset({k,aa}))
    # print(pairs)
    print(len(pairs))


visited = {}
checking = set()

visited[st] = 0
checking.add(st)

def rotate_set(s):
    rs = set()
    for ss in s:
        rs.add(r(ss))
    return rs

for i in range(3000):
    next_check = set()
    # print('=1',checking)
    checking = rotate_set(checking)
    # print('=2',checking)
    for c in checking:
        # print(c)

        if c not in visited and c in mapd and mapd[c]=='T':
                # print('aa', aa)
                visited[c] = i+1
                next_check.add(c)
        if c not in visited and c in mapd and mapd[c]=='E':
            print('DONE', c, i+1)

        for aa in adj(c):

            if aa not in visited and aa in mapd and mapd[aa]=='T':
                # print('aa', aa)
                visited[aa] = i+1
                next_check.add(aa)
            if aa not in visited and aa in mapd and mapd[aa]=='E':
                print('DONE', aa, i+1)



    checking = next_check
    # print('next_check', len(next_check))
    # print_set(next_check, 'C')
    # print('visited', len(visited))
    # print_set(visited, 'V')
    # print()





