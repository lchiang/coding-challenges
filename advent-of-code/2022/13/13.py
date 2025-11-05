#ll = open('./2022/13/test.txt').read().splitlines()
ll = open('./2022/13/input.txt').read().splitlines()

import ast
import functools

def compare(l,r):
    if (isinstance(l, int) and isinstance(r, int)):
        if (l < r):
            return True
        elif (l > r):
            return False
    if (isinstance(l, list) and isinstance(r, list)):
        for j in range(len(l)):
            if (j > (len(r)-1)):
                return False
            else:
                com = compare(l[j], r[j])
                if com != None:
                    return com
        if (len(l) < len(r)):
            return True
    if (isinstance(l, int) and isinstance(r, list)):
        return compare([l], r)
    if (isinstance(l, list) and isinstance(r, int)):
        return compare(l, [r])

ss = 0
pl = []
for i in range(len(ll)//3+1):
    l = ast.literal_eval(ll[i*3])
    r = ast.literal_eval(ll[(i*3)+1])
    pl.append(l)
    pl.append(r)
    if (compare(l,r)):
        ss += i+1
print('Part A', ss)

pl.append([[2]])
pl.append([[6]])
def compare1(x, y):
    c = compare(x,y)
    if c == None: return 0
    else: return -1 if c else 1
sp = sorted(pl, key = functools.cmp_to_key(compare1))
print('Part B', (sp.index([[2]])+1)*(sp.index([[6]])+1))
