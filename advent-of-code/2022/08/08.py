#ll = open('./2022/08/test.txt').read().splitlines()
ll = open('./2022/08/input.txt').read().splitlines()

m = [[int(x) for x in list(l)] for l in ll]
v = set()
for y in range(len(m)):
    # look from left
    hl = -1
    for x in range(len(m[0])):
        if (m[y][x] > hl):
            v.add((x,y))
            hl = m[y][x]

    # look from right
    hr = -1
    for x in range(len(m[0])-1,-1,-1):
        if (m[y][x] > hr):
            v.add((x,y))
            hr = m[y][x]

for x in range(len(m)):
    # look from above
    ha = -1
    for y in range(len(m[0])):
        if (m[y][x] > ha):
            v.add((x,y))
            ha = m[y][x]

    # look from below
    hb = -1
    for y in range(len(m[0])-1,-1,-1):
        if (m[y][x] > hb):
            v.add((x,y))
            hb = m[y][x]

print('Part A', len(v))

ms = 0
for y in range(1,len(m)-1):
    for x in range(1,len(m[0])-1):
        # right
        sr = 0
        for xp in range(x+1,len(m[0])):
            sr += 1
            if (m[y][xp] >= m[y][x]): break

        # left
        sl = 0
        for xp in range(x-1,-1,-1):
            sl += 1
            if (m[y][xp] >= m[y][x]): break

        # up
        su = 0
        for yp in range(y-1,-1,-1):
            su += 1
            if (m[yp][x] >= m[y][x]): break

        # down
        sd = 0
        for yp in range(y+1,len(m[0])):
            sd += 1
            if (m[yp][x] >= m[y][x]): break

        s = su * sl * sr * sd
        ms = max(ms, s)

print('Part B', ms)
