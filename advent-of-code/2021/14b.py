ll = open('in14.txt').read().splitlines()
s = ll[0]

d = {}
for l in ll[2:]:
    d[l[:2]] = l[6]

l = {}
for i in range(len(s)-1):
    ss = s[i:i+2]
    if ss not in l: l[ss] = 1
    else:           l[ss] += 1

step = 0
while step < 40:
    step += 1
    n = {}
    for k in l.keys():
        if k in d:
            s1, s2 = k[0]+d[k], d[k]+k[1]
            if s1 in n: n[s1] += l[k]
            else:       n[s1] = l[k]
            if s2 in n: n[s2] += l[k]
            else:       n[s2] = l[k]
    l=n

cnt = {}
for k in l.keys():
    if k[0] not in cnt: cnt[k[0]] = l[k]
    else:               cnt[k[0]] += l[k]
    if k[1] not in cnt: cnt[k[1]] = l[k]
    else:               cnt[k[1]] += l[k]
cnt[s[0]] += 1
cnt[s[-1]] += 1

print((max(cnt.values())-min(cnt.values()))//2)
