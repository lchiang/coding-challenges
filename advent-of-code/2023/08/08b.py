
ll = open('testb.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

nav = ll[0]

d = {}
for l in ll[2:]:
    d[l[0:3]] = (l[7:10], l[12:15])

pos = [x for x in d.keys() if x[-1] == 'A']

def til_z(pos):
    step = 0
    while step < 1000000:
        n = nav[step % len(nav)]
        if n == 'L':
            new_pos = d[pos][0]
        else: # R
            new_pos = d[pos][1]
        #print(step, n, new_pos)
        step += 1
        pos = new_pos
        if new_pos[-1] == 'Z':
            break;
    return step

from math import lcm
step = 1
for p in pos:
    #print(p,til_z(p))
    step = lcm(step,til_z(p))

print(step)
