#ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

t_pri = 0
for l in ll:
    a = l[:len(l)//2]
    b = l[len(l)//2:]
    c = list(set(a) & set(b))[0]
    pri = ord(c)-(96 if (c.islower()) else 38)
    t_pri += pri
print('A', t_pri)

t_pri = 0
for x in range(len(ll)//3):
    a = ll[x*3]
    b = ll[x*3+1]
    c = ll[x*3+2]
    co = list(set(a) & set(b) & set(c))[0]
    pri = ord(co)-(96 if (co.islower()) else 38)
    t_pri += pri
print('B', t_pri)
