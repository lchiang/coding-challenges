f = open('in13a_test.txt')
f = open('everybody_codes_e2025_q13_p1.txt')
ll = [int(x) for x in f.read().splitlines()]
#print(ll)

e = ll[::2]
o = ll[1::2]
o.reverse()

oe = [1]+e+o
print('part 1:', oe[2025 % len(oe)])
