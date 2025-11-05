ll = open('./2022/20/test.txt').read().splitlines()
ll = open('./2022/20/input.txt').read().splitlines()

k = 811589153

import copy
class Number:
    def __init__(self, val) -> None:
        self.val = val

l = []
for x in ll:
    l.append(Number(int(x)*k)) # k=1 for part A

o = copy.copy(l)

for iii in range(10): # run once for part A
    i = 0
    for x in o:
        b4_i = l.index(x)
        at_i = (b4_i + x.val)%(len(o)-1)
        p = l.pop(b4_i)
        if at_i == 0:
            at_i = len(o)-1
        l.insert(at_i, p)
        #print([k.val for k in l], 'cycle',i,':', x.val, 'pos', b4_i, 'to', at_i)
        i+=1
    #print([k.val for k in l], iii)

ii = [k.val for k in l].index(0)
a = l[(ii+1000)%len(o)].val
b = l[(ii+2000)%len(o)].val
c = l[(ii+3000)%len(o)].val
print(a+b+c)
