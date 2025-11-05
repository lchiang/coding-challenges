ll = open('in14t.txt').read().splitlines()
s = ll[0]

d = {}
for l in ll[2:]:
    d[l[:2]] = l[6]

step = 0
while step < 15: # Took very long when steps greater than 15
    step += 1
    i = 0
    kkk = 0
    while i < len(s)-1:
        if s[i:i+2] in d:
            s = s[:i+1] + d[s[i:i+2]] + s[i+1:]
            i += 1
        i+=1
    print('{:3}'.format(step), len(s))
cc = list(set(s))
ma = 0
mi = len(s)
for c in cc:
    ma = max(ma, s.count(c))
    mi = min(mi, s.count(c))
print(ma-mi)