import re
ll = open('testb.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

def nu(s):
    if s == 'one': return 1
    if s == 'two': return 2
    if s == 'three': return 3
    if s == 'four': return 4
    if s == 'five': return 5
    if s == 'six': return 6
    if s == 'seven': return 7
    if s == 'eight': return 8
    if s == 'nine': return 9

c = 0
for l in ll:

    #print('==', l)
    fi_pos, la_pos = 999, -1
    fi_val, la_val = '0', '0'

    # PART B Start
    l1 = l
    aa = re.search('(one|two|three|four|five|six|seven|eight|nine)', l)
    if aa:
        first_find = aa.group(0)
        i = l.find(first_find)
        l1 = l[:i] + str(nu(first_find)) + l[i:]
        #print(l1)
    l2 = l1
    oo = re.search('('+'one|two|three|four|five|six|seven|eight|nine'[::-1]+')', l1[::-1])
    if oo:
        last_find = oo.group(0)
        i = (l1[::-1]).find(last_find)
        l2 = (l1[::-1][:i] + str(nu(last_find[::-1])) + l1[::-1][i:])[::-1]
        #print(l2)
    l = l2
    # PART B End
    
    nn = [c for c in list(l) if c.isdigit()]
    n = int(''.join([nn[0],nn[-1]]))
    #print(n)
    c += n
    
print(c)
