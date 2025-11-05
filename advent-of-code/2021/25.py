#ll = open('in25test.txt').read().splitlines()
ll = open('in25.txt').read().splitlines()

def print_board(b):
   for l in b:
       print('',''.join(['{:1}'.format(c) for c in l]))
   print()

def isEq(b1,b2):
    if (len(b1) and len(b2) and len(b1[0]) and len(b2[0])):
        for y in range(len(b1)):
            for x in range(len(b1[0])):
                if (b1[y][x]!=b2[y][x]):
                    return False
        return True
    else:
        return False

h = len(ll)
w = len(ll[0])
p = []
for l in ll:
    p.append([x for x in l])
#print_board(p)

step = 0
stop_bool = False
while (step < 6000 and not stop_bool):
    step += 1
    n = [ ['.']*w for i in range(h)]
    for y in range(h):
        for x in range(w):
            if (p[y][x] == '>'):
                if (p[y][(x+1)%w] == '.'):
                    n[y][(x+1)%w] = '>'
                else:
                    n[y][x] = '>'
    #print_board(n)

    for x in range(w):
        for y in range(h):
            if (p[y][x] == 'v'):
                if ((p[(y+1)%h][x] != 'v') and
                    (n[(y+1)%h][x] != '>')):
                    n[(y+1)%h][x] = 'v'
                else:
                    n[y][x] = 'v'
    #print_board(n)
    #print(step, isEq(p,n))
    stop_bool = True if isEq(p,n) else False
    p = [x[:] for x in n]

print(step)