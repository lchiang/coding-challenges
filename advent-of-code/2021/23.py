
from collections import namedtuple
P = namedtuple('P', ['name','x','y'])

ll = open('in23.txt').read().splitlines()
b = [list(l) for l in ll]
def print_board(b):
    for l in b:
        print('>',''.join(['{:2}'.format(c) for c in l]))
    print('>')
print_board(b)

lowest_cost = 999999


def possible_route(x,y,r,rd:dict,d,b):
    #print('possible_route', x, y, r)
    rr = r.copy()
    rdd = rd.copy()
    for xx, yy in [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
        if b[yy][xx] == '.' and (xx,yy) not in rr: #visited
            rr.append((xx, yy))
            rdd[(xx, yy)] = d+1
            rr,rdd = possible_route(xx,yy,rr,rdd,d+1,b)
    return (rr,rdd)

def is_done(p:P,b):
    rm_lower, rm_upper = room[p.name]
    if (p.x, p.y) == rm_lower: # lower self-room:
        return True
    elif (p.x, p.y) == rm_upper and getB(b,rm_lower) == p.name: # upper self-room:
        return True
    else:
        return False




room = {}
room['A'] = [(3,3), (3,2)]
room['B'] = [(5,3), (5,2)]
room['C'] = [(7,3), (7,2)]
room['D'] = [(9,3), (9,2)]

def getB(b,t:tuple):
    return b[t[1]][t[0]]


def cost_factor(name):
    if name == 'A': return 1
    elif name == 'B': return 10
    elif name == 'C': return 100
    else: return 1000

def possible_stop(p:P,r,rd,b):

    rm_lower, rm_upper = room[p.name]
    stops_list  = []

    if rm_lower in r and getB(b,rm_lower) == '.' and getB(b,rm_upper) == '.':
        stops_list = [rm_lower]
    elif rm_upper in r and getB(b,rm_lower) == p.name and getB(b,rm_upper) == '.':
        stops_list = [rm_upper]
    else: # cannot enter room
        if p.y == 1: # in hallway
            stops_list = []

            # Amphipods will never move from the hallway into a room unless that room
            # is their destination room and that room contains no amphipods which do
            # not also have that room as their own destination.

            # Once an amphipod stops moving in the hallway, it will stay in that spot
            # until it can move into a room.

        else: # in other room
            # Amphipods will never stop on the space immediately outside any room.
            outside_room = [(3,1), (5,1), (7,1), (9,1)]
            stops_list = [rr for rr in r if (rr not in outside_room and rr[1]==1)]

    return [(x,y,rd[(x,y)]*cost_factor(p.name)) for x, y in stops_list]


'''
pods = []
for y in range(len(b)):
    for x in range(len(b[y])):
        if b[y][x] in ['A','B','C','D']:
            (r,rd) = possible_route(x,y,[],{},0)
            #print('r', r) # route
            #print(rd) # route with distance
            s = possible_stop(P(b[y][x], x, y), r)
            print((b[y][x], x, y),'possible stops:',s)
            print()
'''


def move(board,dist):
    print('move, dist=',dist)
    print_board(board)

    finished = True
    move_list = [] #(P, [(x,y),(x,y)])
    for y in range(len(board)):
        for x in range(len(board[y])):
            name = board[y][x]
            if name in ['A','B','C','D']:
                if not is_done(P(name,x,y),board):
                    finished = False
                    #print(P(name,x,y),'checking')
                    (r,rd) = possible_route(x,y,[],{},0,board)
                    #print('r', r) # route
                    #print(rd) # route with distance
                    stops = possible_stop(P(name,x,y),r,rd,board)
                    #print((name, x, y),'possible stops:',stops)
                    for s in stops:
                        move_list.append((P(name,x,y),s))

    if finished:
        print('finished', dist)
        global lowest_cost
        lowest_cost = min(lowest_cost, dist)

    if not move_list:
        print('DONE')
        return None


    ml = [x for x in move_list if x[1][1]>1 ]
    if ml: move_list = ml # if can go to room, eliminate go to hallway
    #print('move list')
    #for p, s in move_list:
    #    print(p,s)

    if dist < 15000:
        for p, s in move_list:
            print('===', p.name, p.x, p.y, s)
            nb = [x[:] for x in board]
            nb[s[1]][s[0]] = p.name
            nb[p.y][p.x] = '.'
            d = s[2] + dist
            move(nb,d)



move(b,0)
print(lowest_cost)


# 18246 too high







