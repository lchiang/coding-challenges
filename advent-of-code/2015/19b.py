
import random
ll = open('in19.txt').read().splitlines()

d = {}
for l in ll:
    if '=>' in l:
        k, v = l.split(' => ')
        d[v] = k
    elif l: s = l

step = 0
while step < 300 and s != 'e':
    step += 1
    key_list = list(d.keys())
    random.shuffle(key_list)
    for k in key_list:
        if k in s:
            s = s.replace(k, d[k], 1)
            #print('replacing', k , 'with', d[k])
            #print(s)
            break
    if s == 'e':
        print('DONE', step)
        break
