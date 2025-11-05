f = open('input12.txt')
d = f.read().splitlines()

import re
import numpy as np

# moons
mn = []
original_set = []
reg = re.compile('<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')
for li in d:
    m = reg.findall(li)
    init_pos = np.array([int(x) for x in m[0]])
    init_vec = np.array([0,0,0])
    mn.append([init_pos, init_vec])
    original_set.append((init_pos, init_vec))
f.close()

def x_repeated():
    return repeated(0)
def y_repeated():
    return repeated(1)
def z_repeated():
    return repeated(2)
    
def repeated(c): # 0,1,2 = x,y,z
    for i in range(len(mn)):
        o_pos = original_set[i][0][c]
        m_pos = mn[i][0][c]
        m_vel = mn[i][1][c]
        if m_vel != 0:
            return False
        elif m_pos != m_pos:
            return False
    return True
  
def print_all_moons():
    for i in range(len(mn)):
        print_moon(mn, i)

def print_all_moons_other_universe(universe):
    for i in range(len(universe)):
        print_moon(universe, i)

def print_moon(universe, num):
    m = universe[num]
    pos = '{0:>4}{1:>4}{2:>4}'.format(m[0][0], m[0][1], m[0][2])
    vel = '{0:>4}{1:>4}{2:>4}'.format(m[1][0], m[1][1], m[1][2])
    print('Moon', num, ' |  pos =', pos, ' |  vel =', vel)

print_all_moons()

x_repeat_at = 0
y_repeat_at = 0
z_repeat_at = 0

step = 0
while (x_repeat_at == 0) or (y_repeat_at == 0) or (z_repeat_at == 0):
#for step in range(1,2775):
    step += 1
    # apply gravity to vel
    from itertools import combinations
    comb = combinations(mn, 2)
    for i in list(comb):        
        q, k = i[0], i[1]
        for j in range(3): # x, y, z - axis
            qx = q[0][j]
            kx = k[0][j]            
            if qx != kx:
                if qx > kx:
                    q[1][j] -= 1
                    k[1][j] += 1
                else: # kx > qx
                    k[1][j] -= 1
                    q[1][j] += 1

        
    # add vel to pos
    for m in mn:
        m[0] = np.add(m[0],m[1])

    # calculate total energy
    total_energy = 0
    for m in mn:        
        pot = sum([abs(x) for x in m[0]])
        kin = sum([abs(x) for x in m[1]])
        tot = pot * kin
        total_energy += tot


    if (x_repeat_at == 0) and x_repeated():
        x_repeat_at = step
        print('x repeated at', step)
    if (y_repeat_at == 0) and y_repeated():
        y_repeat_at = step
        print('y repeated at', step)
    if (z_repeat_at == 0) and z_repeated():
        z_repeat_at = step
        print('z repeated at', step)


print(x_repeat_at, y_repeat_at, z_repeat_at)
print(x_repeat_at* y_repeat_at* z_repeat_at)
