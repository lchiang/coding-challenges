import ic
import os
import time
import multiprocessing
from random import choice

def printscreen(m,x,y):
    #time.sleep(0.1)
    os.system('cls')
    for yy in range(len(m)):
        li = m[yy].copy()
        if yy == y:
            li[x] = 'D'
                    
        print(''.join(li))

if __name__ == '__main__':
    f = open('input15.txt')
    d = f.readline().split(',')
    d = list(map(int, d))
    #d += [0 for x in range(50000)]

    


    # initialize board
    map_size = 50
    #block_cnt, score = 0, 0
    #ball_at, paddle_at = 99, 99
    m = [['.' for x in range(map_size)] for y in range(map_size)]
    x, y = map_size//2, map_size//2

    dist = {}
    # dist[(x,y)] = distance value
    dist[(x,y)] = 0
    
    '''
    Program Input:
        movement commands are understood:
            north (1), south (2), west (3), and east (4).
            
    Progam output
        The repair droid can reply with any of the following status codes:

        0: The repair droid hit a wall. Its position has not changed.
        1: The repair droid has moved one step in the requested direction.
        2: The repair droid has moved one step in the requested direction; 
            its new position is the location of the oxygen system.
    
    '''
    
    # init game process
    parent_conn, child_conn = multiprocessing.Pipe()
    icp = multiprocessing.Process(target=ic.intercode, args=(d, child_conn))
    icp.start()
    mv = 1


    
    
    i = 0
    #for i in range(900):
    while True:

        
        parent_conn.send(mv)
        ball_moved = False
        o = parent_conn.recv()
        #print('try move', mv, ', result', o)
        if o == 'HALT':
            break
        elif o == 0:
            #print('hit wall')
            if mv == 1:
                m[y-1][x] = '#'                
            elif mv == 2:
                m[y+1][x] = '#'                
            elif mv == 3:
                m[y][x-1] = '#'                
            elif mv == 4:
                m[y][x+1] = '#'
                    
        elif o == 1:
            #print('moved', mv)
            ori_dist = dist[(x,y)]
            
            if mv == 1:
                y += -1
            elif mv == 2:
                y += 1
            elif mv == 3:
                x += -1
            elif mv == 4:
                x += 1

            if (x,y) not in dist:
                dist[(x,y)] = ori_dist + 1
            
                
        elif o == 2:
            print('moved', mv, 'and found oxygen')
            ori_dist = dist[(x,y)]
            
            if mv == 1:
                y += -1
            elif mv == 2:
                y += 1
            elif mv == 3:
                x += -1
            elif mv == 4:
                x += 1
            m[y][x] = 'O'
            printscreen(m,0,0)
            print(ori_dist+1)
            break
        else:
            print(o)

        # next move
        n_stuck = ((m[y-1][x] == '#') or (m[y-1][x] == ','))
        s_stuck = ((m[y+1][x] == '#') or (m[y+1][x] == ','))
        w_stuck = ((m[y][x-1] == '#') or (m[y][x-1] == ','))
        e_stuck = ((m[y][x+1] == '#') or (m[y][x+1] == ','))
        if (n_stuck and s_stuck and w_stuck):
            m[y][x] = ','
            mv = 4
        elif (n_stuck and s_stuck and e_stuck):
            m[y][x] = ','
            mv = 3
        elif (n_stuck and w_stuck and e_stuck):
            m[y][x] = ','
            mv = 2
        elif (s_stuck and w_stuck and e_stuck):
            m[y][x] = ','
            mv = 1
        #elif (o == 1): #ball moved, keep direction
        #    mv = mv
        else:            
            mv = choice([1,2,3,4])

        if i % 10000 == 0:
            printscreen(m,x,y)
            print(dist[(x,y)])
        i += 1
    
    
    icp.join()
    
