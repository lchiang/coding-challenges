ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

time = ll[0].split(':')[1].split()
dist = ll[1].split(':')[1].split()

# Part B Start
time = [''.join(time)]
dist = [''.join(dist)]
# Part B End

w = []
for r in range(len(time)):
    t = int(time[r])
    d = int(dist[r])
    ww = 0
    for h in range(1,t):        
        if h*(t-h) > d:
            ww += 1            
    w.append(ww)

import math 
print(math.prod(w))
