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

if __name__ == '__main__':
    f = open('./2019/input13.txt')
    d = f.readline().split(',')
    d = list(map(int, d))
    d += [0 for x in range(50000)]
    d[0] = 2 # for part2

    # initialize board
    block_cnt, score = 0, 0
    ball_at, paddle_at = 99, 99
    m = [['' for x in range(41)] for y in range(24)]

    # init game process
    parent_conn, child_conn = multiprocessing.Pipe()
    icp = multiprocessing.Process(target=ic.intercode, args=(d, child_conn))
    icp.start()

    while True:
        ball_moved = False
        o = parent_conn.recv()
        if (o == 'HALT'):
            break
        else:
            x = o
            y = parent_conn.recv()
            t = parent_conn.recv()
            if (x == -1) and (y == 0):
                score = t
            elif t == 0:
                s = ' '
            elif t == 1:
                s = 'W'
            elif t == 2:
                block_cnt += 1
                s = 'B'
            elif t == 3:
                s = '_'
                paddle_at = x
            elif t == 4:
                s = 'o'
                ball_at = x
                ball_moved = True
            else:
                s = ' '
            m[y][x] = s

            if ball_moved:
                printscreen(m, score) # suppress update for speed
                if paddle_at > ball_at:
                    parent_conn.send(-1)
                elif paddle_at < ball_at:
                    parent_conn.send(1)
                else:
                    parent_conn.send(0)

    icp.join()
    print('Part 1: block count', block_cnt)
    print('Part 2: score', score)

