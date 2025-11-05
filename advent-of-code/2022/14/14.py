#ll = open('./2022/14/test.txt').read().splitlines()
ll = open('./2022/14/input.txt').read().splitlines()

min_x, max_x, min_y, max_y = 501, 499, 500, -1
r = set() # rocks
s = set() # settled sands
f = set() # falling sands

def print_map():
    for y in range(0, max_y+3):
        line = ''
        for x in range(min_x-max_y, max_x+max_y):
            if (x==500 and y==0):
                line = line + '+'
            elif ((x,y) in r):
                line = line + '#'
            elif ((x,y) in s):
                line = line + 'o'
            else: line = line + '.'
        print(line)
        line = ''

for l in ll:
    pp = l.split(' -> ')
    for p in pp:
        x,y = p.split(',')

        min_x = min(min_x, int(x))
        max_x = max(max_x, int(x))
        min_y = min(min_y, int(y))
        max_y = max(max_y, int(y))

    head_x, head_y = 0,0
    for i in range(len(pp)):
        x,y = pp[i].split(',')
        x = int(x)
        y = int(y)
        if i == 0:
            head_x = x
            head_y = y
        else:
            if (x == head_x):
                for yy in range(min(y, head_y),max(y, head_y)+1):
                    r.add((x,yy))
                head_y = y
            elif (y == head_y):
                for xx in range(min(x, head_x),max(x, head_x)+1):
                    r.add((xx,y))
                head_x = x
#print_map()

### Part B Begin ###
for x in range(min_x-max_y, max_x+max_y):
    r.add((x,max_y+2))
### Part B End ###

def can_go(x,y):
    return (x, y) not in r and (x, y) not in s

def falling_sand():
    x = 500
    y = 0
    settled = False
    fallen_away = False
    while not settled and not fallen_away:
        if (can_go(x, y+1)):
            y += 1
        elif (can_go(x-1, y+1)):
            x -= 1
            y += 1
        elif (can_go(x+1, y+1)):
            x += 1
            y += 1
        else:
            settled = True
        if (y>max_y+3):
            fallen_away = True
    return (None if fallen_away else (x,y))

round = 0
while round < 100000:
    #print('round', round)
    #print_map()
    new_sand = falling_sand()
    if (new_sand is None):
        #print_map()
        print('Ending round:', round)
        break
    elif (new_sand == (500,0)):
        #print_map()
        print('Ending round:', round+1)
        break
    else:
        s.add(new_sand)
    round += 1
