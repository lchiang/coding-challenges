#ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

fully_contained, overlapping = 0, 0
for l in ll:
    al, bl = l.split(',')
    a1c, a2c = al.split('-')
    b1c, b2c = bl.split('-')
    a = list(range(int(a1c), int(a2c)+1))
    b = list(range(int(b1c), int(b2c)+1))
    if (not [x for x in a if x not in b] or not [x for x in b if x not in a]):
        fully_contained += 1
    if ([x for x in a if x in b]):
        overlapping += 1

print('A', fully_contained)
print('B', overlapping)
