#ll = open('./2022/18/test.txt').read().splitlines()
ll = open('./2022/18/input.txt').read().splitlines()

from collections import namedtuple

Cube = namedtuple('Cube', ['x','y','z'])
cube = [Cube._make([int(x) for x in l.split(',')]) for l in ll]

min_x = min(cube, key=lambda k: k.x).x-2
max_x = max(cube, key=lambda k: k.x).x+2
min_y = min(cube, key=lambda k: k.y).y-2
max_y = max(cube, key=lambda k: k.y).y+2
min_z = min(cube, key=lambda k: k.z).z-2
max_z = max(cube, key=lambda k: k.z).z+2
print('size',(max_x-min_x)*(max_y-min_y)*(max_z-min_z))
def can_expand(x,y,z):
    return ((min_x < x and x < max_x) and
        (min_y < y and y < max_y) and
        (min_z < z and z < max_z) and
        (x,y,z) not in cube)

def expand(steamlist):
    #print('before expand', steamlist)
    new_list = []
    for c in steamlist:
        if can_expand(c.x-1,c.y,c.z):
            new_list.append(Cube(c.x-1,c.y,c.z))
        if can_expand(c.x+1,c.y,c.z):
            new_list.append(Cube(c.x+1,c.y,c.z))
        if can_expand(c.x,c.y-1,c.z):
            new_list.append(Cube(c.x,c.y-1,c.z))
        if can_expand(c.x,c.y+1,c.z):
            new_list.append(Cube(c.x,c.y+1,c.z))
        if can_expand(c.x,c.y,c.z-1):
            new_list.append(Cube(c.x,c.y,c.z-1))
        if can_expand(c.x,c.y,c.z+1):
            new_list.append(Cube(c.x,c.y,c.z+1))
    for n in new_list:
        if n not in steamlist:
            steamlist.extend([n])
    #print('after expand', steamlist)


c0 = Cube(min_x+1,min_y+1,min_z+1)
steam = [c0]

prev_steam_size = len(steam)
expand(steam)
while prev_steam_size != len(steam):
    print(len(steam))
    prev_steam_size = len(steam)
    expand(steam)

print('steam expand done')

surface = 0
for c in cube:
    if ((c.x-1,c.y,c.z) not in cube):
        surface +=1
    if ((c.x+1,c.y,c.z) not in cube):
        surface +=1
    if ((c.x,c.y-1,c.z) not in cube):
        surface +=1
    if ((c.x,c.y+1,c.z) not in cube):
        surface +=1
    if ((c.x,c.y,c.z-1) not in cube):
        surface +=1
    if ((c.x,c.y,c.z+1) not in cube):
        surface +=1
print('Part A', surface)


surface = 0
for c in cube:
    if ((c.x-1,c.y,c.z) in steam):
        surface +=1
    if ((c.x+1,c.y,c.z) in steam):
        surface +=1
    if ((c.x,c.y-1,c.z) in steam):
        surface +=1
    if ((c.x,c.y+1,c.z) in steam):
        surface +=1
    if ((c.x,c.y,c.z-1) in steam):
        surface +=1
    if ((c.x,c.y,c.z+1) in steam):
        surface +=1
print('Part B', surface)





