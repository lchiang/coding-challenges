ll = open('./2022/22/test.txt').read().splitlines()
ll = open('./2022/22/input.txt').read().splitlines()

w = 0
h = len(ll[:-2])
m = []
for l in ll[:-2]:
    w = max(w, len(l))
    m.append(list(l))

'''
di
   ^3
2  |
<--.-->0
   |
   v1
'''
pos = (ll[0].index('.'), 0)
di = 0

import re
rr = ll[-1]
#rr = '10R5L6L2L10R1L2L7R4'
#print(rr)
path = re.split(r'([RL])',rr)
visited = {}

import copy
def print_map():
    mm = copy.deepcopy(m)
    for k,v in visited.items():
        u = '.'
        if v==3: u = '^'
        elif v==0: u = '>'
        elif v==1: u = 'V'
        elif v==2: u = '<'
        mm[k[1]][k[0]] = u
    for y in range(h):
        print(''.join(mm[y]))

def can_walk_a(pos,di):
    x,y = pos
    if di == 0: # looking to right
        if (x+1 < len(m[y])):
            if ('.' == m[y][x+1]):
                x+=1
        else: # out of bound
            if ('#' not in m[y] or
                m[y].index('.') < m[y].index('#')):
                x = m[y].index('.')

    elif di == 2: # looking to left
        if (x-1 >= 0) and (' ' != m[y][x-1]):
            if ('.' == m[y][x-1]):
                x-=1
        else: # out of bound
            last_tile = len(m[y]) - 1 - m[y][::-1].index('.')
            last_rock = len(m[y]) - 1 - m[y][::-1].index('#')
            if ('#' not in m[y] or
                last_tile > last_rock):
                x = last_tile

    elif di == 1: # looking down
        all_space_below = True
        for i in range(y+1,h):
            if (x < len(m[i])) and (' ' != m[i][x]):
                all_space_below = False
        if (y+1 < h) and not all_space_below:
            if ('.' == m[y+1][x]):
                y+=1
        else: # out of bound
            first_tile = h+1
            first_rock = h+1
            for i in range(h):
                if (x < len(m[i])) and ('.' == m[i][x]):
                    first_tile = min(first_tile,i)
                if (x < len(m[i])) and ('#' == m[i][x]):
                    first_rock = min(first_rock,i)
            #print('fff',first_tile, first_rock)
            if first_tile < h and first_tile < first_rock:
                y=first_tile

    elif di == 3: # looking up
        all_space_above = True
        for i in range(y):
            if (x < len(m[i])) and (' ' != m[i][x]):
                all_space_above = False
        if (y-1 >= 0) and not all_space_above:
            if ('.' == m[y-1][x]):
                y-=1
        else: # out of bound
            last_tile = -1
            last_rock = -1
            for i in range(h):
                if (x < len(m[i])) and ('.' == m[i][x]):
                    last_tile = max(last_tile,i)
                if (x < len(m[i])) and ('#' == m[i][x]):
                    last_rock = max(last_rock,i)

            if last_tile > -1 and last_rock < last_tile:
                y=last_tile
    #print(pos, x,y,m[y][x])
    return ((x,y),di)

def can_walk_b(pos,di):
    x,y = pos
    x1,y1=pos
    di1 = di
    if di == 0: # looking to right >

        if 0<=y and y<50 and x==149: #0-49
            print('blue edge')
            #(149,0) > to (99,149) <
            #(149,49) > to (99,100) <

        elif y<=50 and y<100 and x==99: #50-99
            print('green edge')
            #(99,50) > to (100,49) ^
            #(99,99) > to (149,49) ^

        elif y<=100 and y<150 and x==99: #100-149
            print('blue edge')
            #(99,100) > to () <
            #(99,149) > to () <


        elif y<=150 and x==49: #150-199
            print('purple edge')
            #(49,150) > to () ^
            #(49,199) > to () ^

        else:
            x1 = x+1


        '''
        if (x+1 < len(m[y])):
            if ('.' == m[y][x+1]):
                x+=1
        else: # out of bound
            if ('#' not in m[y] or
                m[y].index('.') < m[y].index('#')):
                x = m[y].index('.')
        '''

    elif di == 2: # looking to left <
        if (x-1 >= 0) and (' ' != m[y][x-1]):
            if ('.' == m[y][x-1]):
                x-=1
        else: # out of bound
            last_tile = len(m[y]) - 1 - m[y][::-1].index('.')
            last_rock = len(m[y]) - 1 - m[y][::-1].index('#')
            if ('#' not in m[y] or
                last_tile > last_rock):
                x = last_tile

    elif di == 1: # looking down
        all_space_below = True
        for i in range(y+1,h):
            if (x < len(m[i])) and (' ' != m[i][x]):
                all_space_below = False
        if (y+1 < h) and not all_space_below:
            if ('.' == m[y+1][x]):
                y+=1
        else: # out of bound
            first_tile = h+1
            first_rock = h+1
            for i in range(h):
                if (x < len(m[i])) and ('.' == m[i][x]):
                    first_tile = min(first_tile,i)
                if (x < len(m[i])) and ('#' == m[i][x]):
                    first_rock = min(first_rock,i)
            #print('fff',first_tile, first_rock)
            if first_tile < h and first_tile < first_rock:
                y=first_tile

    elif di == 3: # looking up
        all_space_above = True
        for i in range(y):
            if (x < len(m[i])) and (' ' != m[i][x]):
                all_space_above = False
        if (y-1 >= 0) and not all_space_above:
            if ('.' == m[y-1][x]):
                y-=1
        else: # out of bound
            last_tile = -1
            last_rock = -1
            for i in range(h):
                if (x < len(m[i])) and ('.' == m[i][x]):
                    last_tile = max(last_tile,i)
                if (x < len(m[i])) and ('#' == m[i][x]):
                    last_rock = max(last_rock,i)

            if last_tile > -1 and last_rock < last_tile:
                y=last_tile

    #print(pos, x,y,m[y][x])

    if ('.' == m[y1][x1]): # if can move then move
        x=x1
        y=y1
        di=di1
    return ((x,y),di)



for p in path:
    if p.isnumeric():
        mv = int(p)
        #print('-',mv,'steps')
        for i in range(mv):
            new_pos, new_di = can_walk_a(pos,di)
            pos = new_pos
            di = new_di
            visited[pos] = di
            #print(i, pos, di)

    elif 'L' == p:
        #print('- Left')
        di = (di-1)%4
        #print(pos, di)
    elif 'R' == p:
        #print('- Right')
        di = (di+1)%4
        #print(pos, di)
    else:
        print('ERR',p)

#print_map()

print(1000*(pos[1]+1) + (4*(pos[0]+1)) + di)