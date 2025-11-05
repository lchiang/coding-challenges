ll = open('./2022/24/test.txt').read().splitlines()
ll = open('./2022/24/input.txt').read().splitlines()

def add_to_dict(x,y,symbol,dict):
    if (x,y) not in dict:
        dict[(x,y)] = [symbol]
    else:
        dict[(x,y)].append(symbol)

w = len(ll[0])
h = len(ll)
end_pos = (w-2,h-1)

blizzard = {}
for y in range(len(ll)):
    for x in range(len(ll[0])):
        if ll[y][x] in ['>','v','^','<']:
            add_to_dict(x,y,ll[y][x],blizzard)
#print(blizzard)

def print_map(blizzard,pos):
    for y in range(h):
        line = []
        for x in range(w):
            if (x,y) == pos:
                line.append('E')
            elif (x,y) in blizzard.keys():
                v = blizzard[(x,y)]
                line.append(str(len(v)) if len(v)>1 else v[0])
            elif (x,y)==(1,0) or (x,y)==end_pos:
                line.append('.')
            elif x==0 or x==w-1 or y==0 or y==h-1:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))


def move(blizzard, step):
    b = {}
    for k,vv in blizzard.items():
        x0,y0 = k
        for v in vv:
            if v=='>':
                x = (x0+step-1)%(w-2)+1
                add_to_dict(x,y0,'>',b)
            elif v=='<':
                x = (x0-step-1)%(w-2)+1
                add_to_dict(x,y0,'<',b)
            elif v=='v':
                y = (y0+step-1)%(h-2)+1
                add_to_dict(x0,y,'v',b)
            elif v=='^':
                y = (y0-step-1)%(h-2)+1
                add_to_dict(x0,y,'^',b)
            else:
                print('ERR: Unknown symbol',v)
    return b

def can_walk(map,prev_pos):
    x,y = prev_pos
    re = set()
    if (x,y+1)==end_pos:
        re.add((end_pos))
    else:
        around = [(x,y),(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for aa in around:
            xa, ya = aa
            if ((aa == (1,0)) or (aa == (w-2,h-1)) or
                (xa>0 and xa<w-1 and ya>0 and ya<h-1 and ((xa,ya) not in map))):
                re.add((xa,ya))
    return re


import time
start = time.time()

#print_map(blizzard,pos)

p_set = set()
p_set.add((1,0))

status = 0
turn_around = False
min_found = 9999999999
minute = 0
while minute < 1000 and status != 3:
    minute += 1
    next_map = move(blizzard,minute)
    curr_set = set()
    for p in p_set: # all previous steps
        #print_map(next_map,p)
        cc = can_walk(next_map,p)
        if status == 0: # going to goal
            if end_pos in cc:
                print('reaching goal', minute, 'Part A')
                part_a_time = time.time() - start
                status = 1
                turn_around = True

        elif status == 1: # going to start
            if end_pos in cc:
                print('reaching start', minute)
                status = 2
                turn_around = True

        elif status == 2: # going to goal
            if end_pos in cc:
                print('reaching goal again', minute, 'Part B')
                part_b_time = time.time() - start
                status = 3
                turn_around = True

        curr_set.update(cc)

    if turn_around:
        turn_around = False
        p_set.clear()
        p_set.add(end_pos)
        if status == 1:
            end_pos = (1,0)
        elif status == 2:
            end_pos = (w-2,h-1)
    else:
        p_set = curr_set

print(f'Part A time: {part_a_time:.3f}')
print(f'Part B time: {part_b_time:.3f}')

'''
Time Record O
Part A time: 0.712
Part B time: 2.505

Part A time: 0.767
Part B time: 2.436

Part A time: 0.676
Part B time: 2.285

Part A time: 0.669
Part B time: 2.372
'''
