ll = open('in15.txt').read().splitlines()
b = [[int(x) for x in l] for l in ll]

'''
# Part A
x_max = len(b[0])-1
y_max = len(b)-1

def get_b(x,y):
    return b[y][x]
'''

# Part B
x_max = len(b[0]) * 5 - 1
y_max = len(b) * 5 - 1

def get_b(x,y):
    w = len(b[0])
    h = len(b)
    inc = x//w + y//h
    n = b[y%h][x%w] + inc
    while n > 9: n -= 9
    return n

def print_board(bb):
    for l in bb:
        print(''.join(['{:1}'.format(c) for c in l]))
    print('-')
#print_board(b)

r = {} #r[(x,y)] = risk
br = {}
r[(0,0)] = 0
br[(0,0)] = 0

step = 0
while (x_max, y_max) not in r and step < 260000:
    step += 1

    connected = {}
    c = []
    br_rm = []
    for x,y in br.keys():
        bool_rm = True
        if y < y_max and (x,y+1) not in r:
            bool_rm = False
            c.append((x,y+1))
        if x < x_max and (x+1,y) not in r:
            bool_rm = False
            c.append((x+1,y))
        if y > 0 and (x,y-1) not in r:
            bool_rm = False
            c.append((x,y-1))
        if x > 0 and (x-1,y) not in r:
            bool_rm = False
            c.append((x-1,y))

        if bool_rm:
            br_rm.append((x,y))

    for rrr in br_rm: # optimisation, remove non-boundary
        del br[rrr]

    c = list(set(c))
    for cx,cy in c:
        mr = 99999
        if (cx,cy-1) in r: mr = min(mr, r[(cx,cy-1)])
        if (cx-1,cy) in r: mr = min(mr, r[(cx-1,cy)])
        if (cx,cy+1) in r: mr = min(mr, r[(cx,cy+1)])
        if (cx+1,cy) in r: mr = min(mr, r[(cx+1,cy)])
        connected[(cx,cy)] = mr + get_b(cx,cy)

    closest = min(connected, key=connected.get)
    r[closest] = connected[closest]
    br[closest] = connected[closest]

    #if step % 1000 == 0:
    #    print('{:4} {:4} {:4} {:4}'.format(step, len(r), len(br), len(c)))

print('risk', r[(x_max, y_max)])
