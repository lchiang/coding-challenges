#ll = open('./2022/12/test.txt').read().splitlines()
ll = open('./2022/12/input.txt').read().splitlines()

xs,ys,xe,ye=0,0,0,0
w = len(ll[0])
h = len(ll)

for l in ll:
    #print(l)
    if ('S' in l):
        ys = ll.index(l)
        xs = l.index('S')
    if ('E' in l):
        ye = ll.index(l)
        xe = l.index('E')

def print_path(ll,v,o):
    line = []
    for y in range(len(ll)):
        for x in range(len(ll[0])):
            if ((x,y) in v):
                line.append('#')
            elif ((x,y) in o):
                line.append('o')
            else:
                line.append(ll[y][x])
        print(''.join(line))
        line = []

def within_range(x,y,w,h):
    return (x >= 0 and y >= 0 and x <= w-1 and y <= h-1)

def can_climb(xf,yf,xt,yt):
    if (xt==xe) and (yt==ye):
        return (ord(ll[yf][xf])+1 >= ord('z'))
    fm = ord(ll[yf][xf])
    to = ord(ll[yt][xt])
    return ((fm+1) >= to)


def climb(xs,ys,xe,ye):
    o = [] #oblivion
    v = [(xs,ys)] #visited
    y = [] #not yet

    reach = False
    for i in range(w*h):
        to_add = []
        for pt in v:
            x0, y0 = pt[0], pt[1]
            nl = [(pt[0]+1,pt[1]),(pt[0]-1,pt[1]),(pt[0],pt[1]+1),(pt[0],pt[1]-1)]
            for (x,y) in nl:
                if ((within_range(x,y,w,h) and (x0==xs) and (y0==ys)) or
                    (within_range(x,y,w,h) and can_climb(x0,y0,x,y) and ((x,y) not in v) and ((x,y) not in o) and ((x,y) not in to_add))):
                    if (x==xe) and (y==ye):
                        reach = True
                    to_add.append((x,y))
        if reach:
            return (i+1)

        v = v+to_add
        sink_into_oblivion = []
        for pt in v:
            keep = False
            nl = [(pt[0]+1,pt[1]),(pt[0]-1,pt[1]),(pt[0],pt[1]+1),(pt[0],pt[1]-1)]
            for (x,y) in nl:
                if (within_range(x,y,w,h) and ((x,y) not in v) and ((x,y) not in o)):
                    keep = True
            if not keep:
                sink_into_oblivion.append(pt)
                o.append(pt)
        #print_path(ll,v,o)
        for oi in sink_into_oblivion:
            v.remove(oi)
    return -1


print('Part A:', climb(xs,ys,xe,ye))


alist = [(0,y) for y in range(h)]
mmin = w*h
for xxx,yyy in alist:
    mmin = min(mmin, climb(xxx,yyy,xe,ye))
print('Part B:', mmin)