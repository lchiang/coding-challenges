
'''
# Sample
target_x_low = 20
target_x_high = 30
target_y_low = -10
target_y_high = -5
'''

# target area: x=156..202, y=-110..-69
target_x_low = 156
target_x_high = 202
target_y_low = -110
target_y_high = -69


def in_target(x,y):
    return (target_x_low <= x <= target_x_high) and (target_y_low <= y <= target_y_high)

def hit(vx, vy):
    x, y = 0, 0
    h = -100
    while y >= target_y_low:
        x += vx
        y += vy
        if vx < 0:   vx += 1
        elif vx > 0: vx -= 1
        vy -= 1
        h = max(h, y)
        #print(h,x,y,vx,vy,in_target(x,y))
        if in_target(x,y):
            return (True, h)
    return (False,0)


max_h = 0
cnt = 0
for x in range(0,300):
    for y in range(-200,200):
        hh = hit(x,y)
        if hh[0]:
            #print(x,y)
            max_h = max(max_h, hh[1])
            cnt += 1
print(max_h, cnt)
