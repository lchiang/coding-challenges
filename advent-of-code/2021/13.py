ll = open('in13.txt').read().splitlines()

dots = []
max_x, max_y = 0,0
for l in ll[:ll.index('')]:   
    x,y = [int(x) for x in l.split(',')]
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    dots.append((x,y))

fold = []
for l in ll[ll.index('')+1:]:
    fold.append(l.split()[2])

def print_board(b):
    for l in b:        
        print('>',''.join(['{:1}'.format(c) for c in l]))
    print('>')

b = [['.' for x in range(max_x+1)] for y in range(max_y+1)] 
for (x,y) in dots:
    b[y][x] = '#'
print_board(b)

for f in fold:
    k, n = f.split('=')
    #print('fold', k,n)
    n = int(n)
    if k == 'y': # fold up
        up = b[:n]
        lo = b[n+1:][::-1]
        nb = []
        for y in range(n):
            nb.append(['#' if (up[y][x]=='#' or lo[y][x]=='#') else '.' for x in range(len(b[0]))])
        b = nb        
    else: # fold left
        nb = []
        for bb in b:
            le = bb[:n]
            ri = bb[n+1:][::-1]
            nb.append(['#' if (le[x]=='#' or ri[x]=='#') else '.' for x in range(n)])
        b = nb        
    print_board(b)
    dot_cnt = 0
    for bb in b:
        dot_cnt += bb.count('#')
    print('dot', dot_cnt)
