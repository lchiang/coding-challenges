ll = open('in18.txt').read().splitlines()
b = [list(l) for l in ll]
g = len(b)
b[0][0],b[0][g-1],b[g-1][0],b[g-1][g-1] = '#','#','#','#' # Part B

def print_board(b):
    print('===')
    for l in b:
        print(''.join(str(x) for x in l))

def adj(x,y):
    c = 0
    x_min, x_max = max(x-1,0), min(x+1,g-1)     
    y_min, y_max = max(y-1,0), min(y+1,g-1)    
    for yy in range(y_min, y_max+1):
        for xx in range(x_min, x_max+1):
            if not (xx == x and yy == y):
                if b[yy][xx] == '#':
                    c += 1
    return c

print_board(b)  

total_steps = 100
for step in range(0, total_steps):
    nb = [['.']*g for i in range(g)]
    for y in range(0,g):
        for x in range(0,g):
#A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
#A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
            if b[y][x] == '#':
                nb[y][x] = '#' if (adj(x,y)==2 or adj(x,y)==3) else '.'
            if b[y][x] == '.':
                nb[y][x] = '#' if (adj(x,y)==3) else '.'
    b = nb
    b[0][0],b[0][g-1],b[g-1][0],b[g-1][g-1] = '#','#','#','#' # Part B

print_board(b)

c = 0
for y in range(0,g):
    for x in range(0,g):
        if b[y][x] == '#':
            c += 1
print(c)
 
