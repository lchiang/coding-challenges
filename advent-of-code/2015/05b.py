import string
ll = open('in05.txt').read().splitlines()

def twice(s):
    for i in range(0, len(s)-1):
        if (s[i:i+2] in s[0:i]): return True
        if (s[i:i+2] in s[i+2:len(s)]): return True
    return False

def repeat(s):
    for i in range(0, len(s)-2):    
        if (s[i]==s[i+2]): return True    
    return False

nice_cnt = 0
for l in ll:
    if twice(l) and repeat(l):
        nice_cnt += 1
print(nice_cnt)
