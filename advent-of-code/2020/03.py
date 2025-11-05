f = open('in03_2.txt')
mapp = f.read().splitlines()


# ->
#|
#v

def tree(x,y):    
    return mapp[y][x % len(mapp[y])] == '#'
    
def chk_slope(right, down):    
    x, y = right, down
    tt = 0
    while (y < len(mapp)):
        if tree(x, y):
            tt += 1
        #print(x, y, tree(x, y))
        x += right
        y += down

    return tt

#PART A
print(chk_slope(3, 1))

#PART B
print(chk_slope(1, 1) * chk_slope(3, 1) * chk_slope(5, 1) * chk_slope(7, 1) * chk_slope(1, 2))
