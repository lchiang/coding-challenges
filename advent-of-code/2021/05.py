f = open('in05.txt')
inputfile = f.read().splitlines()

def print_board(b):
    for l in b:        
        print('>',''.join(['{:2}'.format(c) for c in l]))
    print('>')

max_x, max_y = 1100, 1100
b = []
for yy in range(max_y):
    b.append([0]*max_x)

for line in inputfile:
    ll = line.split(' -> ')
    x1, y1 = [int(a) for a in ll[0].split(',')]
    x2, y2 = [int(a) for a in ll[1].split(',')]
    #print(x1, y1, '-', x2, y2)
    if x1 == x2: # |
        yl = list(range(min(y1,y2),max(y1,y2)+1,1))
        for y in yl:
            b[y][x1] += 1
    elif y1 == y2: # -
        xl = list(range(min(x1,x2),max(x1,x2)+1,1))
        for x in xl:
            b[y1][x] += 1
    elif x1-x2 == y1-y2: # \
        xl = list(range(min(x1,x2),max(x1,x2)+1,1))
        yl = list(range(min(y1,y2),max(y1,y2)+1,1))
        for i in range(len(xl)):
            b[yl[i]][xl[i]] += 1
    else: # /
        xl = list(range(max(x1,x2),min(x1,x2)-1,-1))
        yl = list(range(min(y1,y2),max(y1,y2)+1,1))
        for i in range(len(xl)):            
            b[yl[i]][xl[i]] += 1

# print_board(b)
danger = {}
max_d = 0
for l in b:
    for a in l:
        max_d = max(max_d, a)
        if a in danger:
            danger[a] += 1
        else:
            danger[a] = 1
dd = 0
if max_d >= 2:
    for x in range(2, max_d+1, 1):
        dd += danger[x]
print(dd)