f = open('in3.txt')
#f = open('in3.txt')
ll = f.read().split()

c_part1, c_part2 = 0, 0

for l1 in ll:
    l = [int(x) for x in list(l1)]
    first = max(l[:-1])
    second = max(l[(l[:-1]).index(first)+1:])
    c_part1 += first*10+second

    cl = l.copy()
    for n in range(12,0,-1):
        d = max(cl[:-n+1]) if n > 1 else max(cl)
        next = cl[cl.index(d)+1:]
        cl = next.copy()
        c_part2 += d*10**(n-1)

print('part 1', c_part1)
print('part 2', c_part2)
