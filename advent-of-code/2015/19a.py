import re
ll = open('in19.txt').read().splitlines()

d = {}
for l in ll:
    if '=>' in l:
        k, v = l.split(' => ')
        if k in d: d[k].append(v)
        else: d[k] = [v]
    elif l: s = re.sub( r"([A-Z])", r" \1", l).split()

ss = []
for i in range(len(s)):
    if s[i] in d:
        for v in d[s[i]]:
            sr = ''.join(s[:i] + [v] + s[i+1:])
            if sr not in ss:
                ss.append(sr)

print(len(ss))
