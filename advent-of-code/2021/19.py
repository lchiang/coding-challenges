from operator import itemgetter
ll = open('in19t.txt').read().splitlines()


s = []
b = []
for l in ll:
    if l.startswith('--'):
        if b:
            s.append(b.copy())
            b.clear()
    else:
        if l.count(',') > 0:
            x, y, z = [int(x) for x in l.split(',')]
            b.append((x, y, z))
if b:
    s.append(b)





print(len(s))





for ss in s[:3]:

    invert = []
    for e in ss:
        x,y,z = [x*-1 for x in list(e)]
        invert.append((x,y,z))

    print(e)
    print(invert)


    print(len(ss))

    sort_x = sorted(ss,key=itemgetter(0))
    sort_y = sorted(ss,key=itemgetter(1))
    sort_z = sorted(ss,key=itemgetter(2))

    print('sort x')
    for kx in sort_x:
        print(kx, kx[0] - sort_x[0][0])
    print('sort y')
    for ky in sort_y:
        print(ky, ky[1] - sort_y[0][1])
    print('sort z')
    for kz in sort_z:
        print(kz, kz[2] - sort_z[0][2])




'''
x increasing rightward, y increasing upward, Z increasing outward

y
^
|
. -- >x
z


     x,  y,  z
01.  1,  2,  3
02. -2,  1,  3
03. -1, -2,  3
04.  2, -1,  3
05.
06.
07.
08.
09.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.






'''