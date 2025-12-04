f = open('in4_test.txt')
f = open('in4.txt')

mapp = [list(x) for x in f.read().splitlines()]
map_w = len(mapp[0])
map_h = len(mapp)

paper = set()
for y in range(map_h):
    for x in range(map_w):
        if mapp[y][x] == '@':
            paper.add((x,y))

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
