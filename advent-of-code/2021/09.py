ll = open('in09.txt').read().splitlines()
b = [[int(x) for x in l] for l in ll]
x_max = len(b[0])
y_max = len(b)

def is_lowpt(x,y):
    pt = b[y][x]
    if x > 0 and b[y][x-1] <= pt: return False
    if x < x_max-1 and b[y][x+1] <= pt: return False        
    if y > 0 and b[y-1][x] <= pt: return False
    if y < y_max-1 and b[y+1][x] <= pt: return False
    return True

r = 0
for y in range(len(b)):
    for x in range(len(b[0])):        
        if is_lowpt(x,y):
            #print(x,y,b[y][x], is_lowpt(x,y))    
            r += b[y][x] + 1
print('Part A:', r)

def grow_basin(x,y,basin):
    #print(x,y,basin)   
    if x > 0 and b[y][x-1] < 9 and (x-1,y) not in basin:
        basin.append((x-1,y))
        grow_basin(x-1,y,basin)
    if x < x_max-1 and b[y][x+1] < 9 and (x+1,y) not in basin:
        basin.append((x+1,y))
        grow_basin(x+1,y,basin)
    if y > 0 and b[y-1][x] < 9 and (x,y-1) not in basin:
        basin.append((x,y-1))
        grow_basin(x,y-1,basin)
    if y < y_max-1 and b[y+1][x] < 9 and (x,y+1) not in basin:
        basin.append((x,y+1))
        grow_basin(x,y+1,basin)
    return basin

b_dict = {}
b_index = 0
for y in range(len(b)):
    for x in range(len(b[0])):
        if b[y][x] < 9 and (x,y) not in b_dict:
            basin = []
            grow_basin(x,y,basin)
            for bb in basin:
                b_dict[bb] = b_index
            b_index += 1

from collections import Counter
b_cnt = Counter(b_dict.values())
b_sizes = [y for x,y in b_cnt.most_common(3)]
print('Part B:', b_sizes[0]*b_sizes[1]*b_sizes[2])

