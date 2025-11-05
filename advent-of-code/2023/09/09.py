from functools import cmp_to_key

ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

def dec_fwd(l): #part A
    #print(l)
    end = True
    for c in l:
        if c != 0: end = False
    if end: return 0
    else:
        tl = []
        for i in range(len(l)-1):
            tl.append(l[i+1]-l[i])
        return l[-1] + dec_fwd(tl)

def dec_bck(l): #part B
    #print(l)
    end = True
    for c in l:
        if c != 0: end = False
    if end: return 0
    else:
        tl = []
        for i in range(len(l)-1):
            tl.append(l[i+1]-l[i])
        return l[0] - dec_bck(tl)

ss = 0
for l in ll:
    li = [int(x) for x in l.split()]
    ss += dec_bck(li)
print(ss)

