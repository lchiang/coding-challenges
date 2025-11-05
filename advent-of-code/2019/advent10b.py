import math

m = [list(line.rstrip('\n')) for line in open('input10.txt')]

def printmap(m):
    for y in range(len(m)):
        print(''.join(m[y]))
        
def list_asteroids(m):
    ast_list = {} # (x,y) : num of can see
    for y in range(len(m)):
        for x in range(len(m[y])):
            if (m[y][x] == '#'):
                ast_list[(x,y)] = 0
    return ast_list

def isBlocked(st_x, st_y, x, y, ast_list):
    xdiff = x-st_x
    ydiff = y-st_y
    blocked = False
    if (xdiff==0):
        if ydiff > 0:
            for yy in range(1, ydiff):
                if ((st_x, st_y+yy) in ast_list):
                    blocked = True
        else:
            for yy in range(-1, ydiff, -1):
                if ((st_x, st_y+yy) in ast_list):
                    blocked = True
    elif (ydiff==0):
        if xdiff > 0:
            for xx in range(1, xdiff):
                if ((st_x+xx, st_y) in ast_list):
                    blocked = True
        else:
            for xx in range(-1, xdiff, -1):
                if ((st_x+xx, st_y) in ast_list):
                    blocked = True
    else:
        g = math.gcd(abs(xdiff),abs(ydiff))
        for k in range (1,g):
            if ((st_x+xdiff//g*k, st_y+ydiff//g*k) in ast_list):
                blocked = True
    return blocked

def angle(y,x):
    angle = -math.atan2(-y,x) + math.pi/2
    angle  = (angle + 2*math.pi) % (2*math.pi)    
    #print('{0:>5} {1:>5} {2:>7.2f}'.format(y, x, math.degrees(angle)))
    return math.degrees(angle)

#printmap(m)

## Part A - Find station location
ast_list = list_asteroids(m)

for station in ast_list:
    for aa in ast_list:
        if (aa != station):
            if not isBlocked(station[0], station[1], aa[0], aa[1], ast_list):
                ast_list[station] += 1

#for y in range(len(m)):    
#    li = ['.' if (x,y) not in ast_list else str(ast_list[(x,y)]) for x in range(len(m[y]))]
#    print(''.join(li))

st = max(ast_list, key=ast_list.get)
print('stationed at', st, ', sees', ast_list[st], 'asteroids')

## Part B - Shoot

num_shot = 0
mm = m.copy()
ast_list = list_asteroids(m)


while (len(ast_list) > 1):
    angle_list = {}
    block_list = {}

    for aa in ast_list:
        if (aa != st):
            xdiff = aa[0]-st[0]
            ydiff = aa[1]-st[1]
            if not isBlocked(st[0], st[1], aa[0], aa[1], ast_list):
                angle_list[aa] = angle(ydiff, xdiff)
            else:
                block_list[aa] = 'b'


    ### Print angle list START
    #for y in range(len(m)):
    #    li = []
    #    for x in range(len(m[y])):
    #        if ((x,y) not in angle_list):
    #            li.append(' _____')
    #        else:
    #            li.append('{0:>6.1f}'.format(angle_list[(x,y)]))            
    #    print(''.join(li))
    ### Print angle list END

    while angle_list:
        trgt = min(angle_list, key=angle_list.get)
        num_shot += 1
        if (num_shot == 200):
            print('200th shot', trgt)
        
        mm[trgt[1]][trgt[0]] = '.'
        del angle_list[trgt]
    #printmap(mm)


    ast_list = list_asteroids(m)
    

print('END')


