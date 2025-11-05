#ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()
c, cl = 0, []
for l in ll:
    if l:        
        c = c + int(l)
    else:
        cl.append(c)
        c = 0
cl.append(c)

cl.sort()
print('a',cl[-1])
print('b',sum(cl[-3:]))   
