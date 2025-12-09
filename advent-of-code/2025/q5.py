f = open('in5_test.txt')
f = open('in5.txt')

ll = f.read().splitlines()
fr = []
for l in ll[:ll.index('')]:
    fr.append(tuple([int(x) for x in l.split('-')]))

def part_1():
    def is_fresh(id):
        for r in fr:
            if r[0] <= id <= r[1]:
                return True
        return False

    f_cnt = 0
    for l in ll[ll.index('')+1:]:
        if is_fresh(int(l)):
            f_cnt += 1
    print('part 1:', f_cnt)

def part_2(): # Similar to 2021 day22
    def intersect(r1: tuple[int, int], r2: tuple[int, int]):
        st = max(r1[0], r2[0])
        en = min(r1[1], r2[1])
        return (st, en) if st <= en else None

    pool = [] #[(sign, (start, end))]
    for r in fr:
        n = []
        for p in pool:
            inter = intersect(p[1], r)
            if inter: n.append((p[0] * -1, inter))
        pool.extend(n)
        pool.append((1, r))

    s = 0
    for p in pool:
        s += p[0] * (p[1][1]-p[1][0]+1)
    print('part 2:', s)

part_1()
part_2()
