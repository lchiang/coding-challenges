
f = open('in14c.txt')
patt = [list(x) for x in f.read().splitlines()]

mapp = [['.' for _ in range(17)] for _ in range(17)]

map_w = len(mapp[0])
map_h = len(mapp)

map_w, map_h = 17, 17

d = {(x,y) for y in range(map_h) for x in range(map_w)}

def print_dict(dd):
    for y in range(map_h):
        l = []
        for x in range(map_w):
            if (x,y) in dd:
                l.append('#')
            else:
                l.append('.')
        print(''.join(l))
    print()

def match_pattern(d):
    match = True
    for y in range(4):
        for x in range(4):
            if patt[y][x] == '#' and (x+13,y+13) not in d:
                match = False
                break
            if patt[y][x] == '.' and (x+13,y+13) in d:
                match = False
                break
    return match

def num_active_neighbour_n_self(x,y):
    count = 0
    if (x, y) in d: count += 1
    if (x-1, y-1) in d: count += 1
    if (x-1, y+1) in d: count += 1
    if (x+1, y-1) in d: count += 1
    if (x+1, y+1) in d: count += 1

    if x == map_w-1 and y == map_h-1:
        if (x, y) in d: count += 1
    elif x == map_w-1:
        if (x, y-1) in d: count += 1
        if (x, y+1) in d: count += 1
    elif y == map_h-1:
        if (x-1, y) in d: count += 1
        if (x+1, y) in d: count += 1
    return count

round = 1
total_active = 0
ta, seen = {}, {}

TOTAL_ROUND = 1_000_000_000

while round < TOTAL_ROUND:
    round += 1
    dn = set()
    for y in range(map_h):
        for x in range(map_w):
            n = num_active_neighbour_n_self(x,y)
            if (n%2 == 0):
                dn.add((x,y))
    if match_pattern(dn):
        total_active += len(dn)
        print(f"Round {round}, active {len(dn)}, total active {total_active}")
        ta[round] = len(dn)


    state = frozenset(dn)
    d = dn.copy()

    if state in seen:
        num_loop = TOTAL_ROUND//(round - seen[state])
        remaining_round = TOTAL_ROUND % (round - seen[state])
        ta_before, ta_loop, ta_after = 0, 0, 0
        for key, value in ta.items():
            if 0 <= key < seen[state]:
                ta_before += value
                print(f"Key: {key}, Value: {value}")
            if seen[state] <= key < round:
                ta_loop += value
                print(f"Key: {key}, Value: {value}")
            if 0 <= key < remaining_round:
                ta_after += value
                print(f"Key: {key}, Value: {value}")
            print('part 3', (ta_before+ta_loop*num_loop+ta_after)*4)
        break
    else:
        seen[state] = round

print('part 1, 2', total_active)

