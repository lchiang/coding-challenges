#ll = open('./2022/09/test1.txt').read().splitlines()
ll = open('./2022/09/input.txt').read().splitlines()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

h = Point(0,0)
t = []
for i in range(9):
    t.append(Point(0,0))

'''
---> +x
|
v
+y
'''

def tail_move(hx,hy,tx,ty):
    x,y = tx,ty
    if (hx == tx):
        if (abs(hy-ty) == 2): y = (hy+ty) // 2
    elif (hy == ty):
        if (abs(hx-tx) == 2): x = (hx+tx) // 2
    else:
        if ((abs(hy-ty) == 2) or (abs(hx-tx) == 2)):
            y = y + (1 if hy > ty else -1)
            x = x + (1 if hx > tx else -1)
    return (x,y)

t_path = set()
for l in ll:
    dir, step = l.split()[0], int(l.split()[1])
    for s in range(step):
        if (dir == 'U'):
            h.y = h.y - 1
        elif (dir == 'D'):
            h.y = h.y + 1
        elif (dir == 'L'):
            h.x = h.x- 1
        elif (dir == 'R'):
            h.x = h.x + 1

        ''' Part A
        new_t = tail_move(h.x, h.y, t.x, t.y)
        t.x, t.y = new_t
        t_path.add(new_t)
        '''
        ''' Part B '''
        t[0].x, t[0].y = tail_move(h.x, h.y, t[0].x, t[0].y)
        for i in range(8):
            t[i+1].x, t[i+1].y = tail_move(t[i].x, t[i].y, t[i+1].x, t[i+1].y)
        t_path.add((t[8].x, t[8].y))

print(len(t_path))
