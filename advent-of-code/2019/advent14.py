import time
start_time = time.time()

f = open('input14.txt')
d = f.read().splitlines()

import re
import math


recipe = {}
for r in d:
    frm, to = r.split(' => ')
    s = re.search('(\d+) (\w+)', to)    
    product = (s.group(2), int(s.group(1)))
    source = []
    for frm_item in frm.split(', '):
        s = re.search('(\d+) (\w+)', frm_item)
        source.append((s.group(2), (int(s.group(1)))))
    recipe[product[0]] = (product, source)


def ore_needed(fuel_needed):
    needed = {}
    excess = {}
    ore_needed = 0
    needed['FUEL'] = fuel_needed

    while sum(needed.values()) > 0:
        
        # pop
        n = next(iter(needed.items()))
        del needed[n[0]]

        # convert
        formula = recipe[n[0]]
        num_needed = n[1]
        if n[1] % formula[0][1] == 0:
            fac = n[1] // formula[0][1]
        else:
            fac = n[1] // formula[0][1] + 1
                
        for i in formula[1]:
            prod = i[0]
            num = i[1]            
            if prod == 'ORE':
                ore_needed += num*fac
            elif prod in needed:
                needed[prod] += num*fac
            else:
                needed[prod] = num*fac

        #leftover
        left_over_num = formula[0][1]*fac-n[1]
        if left_over_num > 0:
            if n[0] in excess:
                excess[n[0]] += left_over_num
            else:
                excess[n[0]] = left_over_num
        
        # minus excess
        for prod, num in needed.items(): 
            if prod in excess:
                if num <= excess[prod]:
                    excess[prod] -= num
                    needed[prod] = 0           
                elif num > excess[prod]:
                    needed[prod] -= excess[prod]
                    excess[prod] = 0

    return ore_needed

# part 1
print(ore_needed(1))

# part 2
target = 1000000000000
low = 0
high = 100000000

while high - low > 1:
    mid = (high + low) // 2
    if ore_needed(mid) == target:
        print('done', mid)
    elif ore_needed(mid) < target:
        low = mid
    else:
        high = mid
    
for i in range(low, high+1):
    print(i, 'fuel from', ore_needed(i) , 'ore. exceeded=', ore_needed(i)>target)

print('--- {0:.2f} ms ---'.format((time.time() - start_time)*1000))

