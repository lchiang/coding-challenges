#f = open('in13b_test.txt')
#f = open('everybody_codes_e2025_q13_p2.txt')
f = open('everybody_codes_e2025_q13_p3.txt')
#ll = [int(x) for x in f.read().splitlines()]
ll = f.read().splitlines()
#print(ll)


fwd = []
bkw = []
forward = True
print(len(ll))
i = 0
for l in ll:
    i+=1
    print(i)
    a = [int(x) for x in l.split('-')]
    #print('===', a, forward)
    l = [x for x in range(a[0], a[1]+1)]
    #print([x for x in range(a[0], a[1]+1)])


    if forward:
        fwd = fwd + l
    else:
        bkw = bkw + l
    forward = not forward

bkw.reverse()

o = [1] + fwd + bkw
print()
#print(o)

    

 
print('part 2:', o[202520252025 % len(o)])
