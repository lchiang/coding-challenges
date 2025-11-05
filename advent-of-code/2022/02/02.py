#ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

def roundScoreA(o,s):
    if (o=='A'):
        if (s=='X'):   return 1+3
        elif (s=='Y'): return 2+6
        elif (s=='Z'): return 3+0
    elif (o=='B'):
        if (s=='X'):   return 1+0
        elif (s=='Y'): return 2+3
        elif (s=='Z'): return 3+6
    elif (o=='C'):
        if (s=='X'):   return 1+6
        elif (s=='Y'): return 2+0
        elif (s=='Z'): return 3+3

def roundScoreB(o,s):
    if (o=='A'):
        if (s=='X'):   return 3+0
        elif (s=='Y'): return 1+3
        elif (s=='Z'): return 2+6
    elif (o=='B'):
        if (s=='X'):   return 1+0
        elif (s=='Y'): return 2+3
        elif (s=='Z'): return 3+6
    elif (o=='C'):
        if (s=='X'):   return 2+0
        elif (s=='Y'): return 3+3
        elif (s=='Z'): return 1+6
        
sa, sb = 0, 0
for l in ll:
    o, s = l.split(' ')
    sa += roundScoreA(o,s)
    sb += roundScoreB(o,s)
print(sa)
print(sb)
