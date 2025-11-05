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

def elevation(p):
    return ord(ll[p[1]][p[0]])

def invalid(x,y,w,h):
    return (x < 0 or y < 0 or x > w-1 or y > h-1)

def can_climb(xf,yf,xt,yt):
    if ('a' == ll[yt][xt]):
        return False
    elif ('c' == ll[yf][xf] and 'b' == ll[yt][xt]):
        return False
    elif ('c' == ll[yf][xf] and xf<80 and xt < xf):
        return False
    fm = ord(ll[yf][xf])
    to = ord(ll[yt][xt])
    if ('r' == ll[yf][xf]):
        return ((fm+1) >= to)
    else:
        return ((fm) == to or (fm+1) == to)

    #return ((fm+1) >= to)


k=0

def print_path(ll,v):

    line = []

    for y in range(len(ll)):
        for x in range(len(ll[0])):
            if ((x,y) in v):
                line.append('#')
            else:
                line.append(ll[y][x])

        print(''.join(line))
        line = []



def path(v, x, y):
    x0, y0 = v[-1]

    if len(v) >= 510:
        return False

    if (x==xe and y==ye) and (ord(ll[y0][x0])+1 >= ord('z')):
        if (len(v) < 510):
            print('arrived',len(v))
            print(''.join([ll[vvv[1]][vvv[0]] for vvv in v]))
            print_path(ll,v)
        #print('arrived',len(v),v)
        #print([ll[vvv[1]][vvv[0]] for vvv in v])
        #return len(v)
            return True
        return False


    elif ((x,y) in v):
        return False
    elif (x < 0 or y < 0 or x > w-1 or y > h-1):
        return False
    elif not can_climb(x0,y0,x,y) and not (x0==xs and y0==ys):
        return False
    else:

        vv = v.copy()
        vv.append((x,y))

        #print(len(vv))
        #print(''.join([ll[vvv[1]][vvv[0]] for vvv in vv]), v[-1])

        coor = [(x+1, y),(x-1, y),(x,y-1),(x,y+1)]


        s_coor = sorted(coor, key = lambda x: abs(x[0]-xe)+abs(x[1]-ye))


        for sc in s_coor:
            if path(vv, sc[0], sc[1]):
                return True

        return False



        if path(vv, x+1, y):
            return True
        elif path(vv, x-1, y):
            return True
        elif path(vv, x, y-1):
            return True
        elif path(vv, x, y+1):
            return True
        else:
            return False



path([(xs,ys)],xs+1,ys)



