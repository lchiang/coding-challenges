import ic
import os
import time
import multiprocessing

def printscreen(m, score):
    #time.sleep(0.1)
    os.system('cls')
    for y in range(len(m)):
        print(''.join(m[y]))
    print('Score', score)

def test_pt(d,x,y):
    o = ic.intercode_one_output(d, [x, y])
    print(x, y, ':', o)

def printRange(code, start_x, start_y, size_x=80, size_y=10):
    m = [['' for x in range(size_x)] for y in range(size_y)]
    for j in range(size_y):
        first = -1
        last = -1
        for i in range(size_x):
            x = start_x + i
            y = start_y + j
            o = ic.intercode_one_output(code, [x,y])
            m[j][i] = o
#            if o == 1:
#                affected_cnt += 1
            if (first == -1) and (o == 1):
                first = x
            if (first != -1) and (last == -1) and (o == 0):
                last = x-1

#           print(x, y, ))
        print(''.join([str(x) for x in m[j]]), 'Line:',y, first, last, last-first+1)



if __name__ == '__main__':
    f = open('input19.txt')
    d = f.readline().split(',')
    d = list(map(int, d))
    d += [0 for x in range(50000)]
    
    printRange(d, 630,950, 120, 5)
    #printRange(d, 37100,49000, 100, 5)
    # initialize board
    #block_cnt, score = 0, 0
    #ball_at, paddle_at = 99, 99
    rng = 20
    m = [['' for x in range(rng)] for y in range(rng)]

    def canfit(x,y,size):
        print('== can fit? ==', x, y, size)
        top_right = ic.intercode_one_output(d, [x+size-1,y])
        bottom_left = ic.intercode_one_output(d, [x,y+size-1])
        print(top_right, x+size-1,y)
        print(bottom_left, x,y+size-1)
        return (top_right==1 and bottom_left==1)


    #print(ic.intercode_one_output(d, [1,1]))            
    
    affected_cnt = 0
  
    print('---')    
    for y in range(rng):
        first = -1
        last = -1
        for x in range(rng):
            o = ic.intercode_one_output(d, [x,y])
            m[y][x] = o
            if o == 1:
                affected_cnt += 1
            if (first == -1) and (o == 1):
                first = x
            if (first != -1) and (last == -1) and (o == 0):
                last = x-1

#           print(x, y, ))
        print(''.join([str(x) for x in m[y]]), y, first, last, last-first+1)



    
    def find_first1(yy):
        low_x = yy//2
        high_x = yy//3*2
        while high_x - low_x > 1:
            mid_x = (low_x + high_x)//2
            mid_val = ic.intercode_one_output(d, [mid_x, yy])
            if mid_val == 0:
                low_x = mid_x
            else:
                high_x = mid_x
            #print(low_x, mid_x, high_x, ic.intercode_one_output(d, [low_x, yy]),\
            #    ic.intercode_one_output(d, [mid_x, yy]), ic.intercode_one_output(d, [high_x, yy]))
        return mid_x

    def find_last1(yy):
        low_x = yy//4*3
        high_x = yy//5*4
        while high_x - low_x > 1:
            mid_x = (low_x + high_x)//2
            mid_val = ic.intercode_one_output(d, [mid_x, yy])
            if mid_val == 1:
                low_x = mid_x
            else:
                high_x = mid_x
            #print(low_x, mid_x, high_x, ic.intercode_one_output(d, [low_x, yy]),\
            #    ic.intercode_one_output(d, [mid_x, yy]), ic.intercode_one_output(d, [high_x, yy]))
        return mid_x

    #find_first1(6543218)
    #find_last1(6543218)

    def canfit_on_line(y):
        x = find_last1(y)
        return canfit(x-99,y,100)

    low = 0
    high = 10000

    while high - low > 1:
        mid = (low + high)//2
        if canfit_on_line(mid):
            high = mid
        else:
            low = mid

#        print(low, mid, high)

    print(canfit_on_line(949))
    print(canfit_on_line(948))
    print(canfit_on_line(947))
    print(canfit_on_line(946))
    print(canfit_on_line(945))
   
    print(619*10000+948)

    printRange(d, 719-2 , 949-2, 5, 5)
    printRange(d, 620-2 , 1048-2, 5, 5)

