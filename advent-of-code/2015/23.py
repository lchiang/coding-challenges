ll = open('in23.txt').read().splitlines()
d = {'a': 0, 'b': 0}
i = 0
while i < len(ll):
    l = ll[i]
    r = l[4:]
    print('{:1}'.format(i), '>', l)
    if l[:3] == 'hlf':
        d[r] = d[r] // 2
        i += 1
    elif l[:3] == 'tpl':
        d[r] = d[r] * 3
        i += 1
    elif l[:3] == 'inc':
        d[r] = d[r] + 1
        i += 1
    elif l[:3] == 'jmp':
        i += int(r)
    elif l[:3] == 'jie':
        r, off = r.split(', ')
        i += int(off) if d[r] % 2 == 0 else 1
    else: # l[:3] == 'ji0':
        r, off = r.split(', ')
        i += int(off) if d[r] == 1 else 1
    print('    ', d)
