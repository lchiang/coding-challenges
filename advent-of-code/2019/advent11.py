import multiprocessing
import ic

def move(bot, turn):
    coor = bot[0]
    direction = bot[1]

    # move
    if direction == '^':
        if turn == 0: #left
            final_coor = (coor[0]-1, coor[1])
            final_dir = '<'
        else: #right
            final_coor = (coor[0]+1, coor[1])
            final_dir = '>'
    elif direction == 'v':
        if turn == 0: #left
            final_coor = (coor[0]+1, coor[1])
            final_dir = '>'
        else: #right
            final_coor = (coor[0]-1, coor[1])
            final_dir = '<'
    elif  direction == '>':
        if turn == 0: #left
            final_coor = (coor[0], coor[1]-1)
            final_dir = '^'
        else: #right
            final_coor = (coor[0], coor[1]+1)
            final_dir = 'v'
    elif direction == '<':
        if turn == 0: #left
            final_coor = (coor[0], coor[1]+1)
            final_dir = 'v'
        else: #right
            final_coor = (coor[0], coor[1]-1)
            final_dir = '^'

    return (final_coor, final_dir)

if __name__ == '__main__':
    f = open('input11.txt')
    d = f.readline().split(',')
    d = list(map(int, d))
    d += [0 for x in range(35019)]

    parent_conn, child_conn = multiprocessing.Pipe()
    icp = multiprocessing.Process(target=ic.intercode, args=(d, child_conn))
    icp.start()

    '''
    # === Part 1 ===
    size_x = 90
    size_y = 100
    bot = ((size_x//2,size_y//2+30),'^')
    parent_conn.send(0)
    # ==============
    '''
    # === Part 2 ===
    size_x = 120
    size_y = 20
    bot = ((size_x//2,size_y//2),'^')
    parent_conn.send(1)
    # ==============

    m = []
    painted = []
    for y in range(size_y):
        m.append([0 for x in range(size_x)])
        painted.append([0 for x in range(size_x)])

    def printm(m, bot):
        mm = m.copy()
        for y in range(len(mm)):
            mm[y] = m[y].copy()
        mm[bot[0][1]][bot[0][0]] = bot[1]
        for y in range(len(mm)):
            l = [str(mm[y][x]) for x in range(len(mm[y]))]
            l = ''.join(l)
            l = l.replace('0',' ').replace('1','@')
            print(l)
    
    #   --->x
    #   |
    #   |
    #   V y
   
    print('entering loop') 
    col = parent_conn.recv()
    while col != 'HALT':
        turn = parent_conn.recv()
               
        # paint
        m[bot[0][1]][bot[0][0]] = col
        painted[bot[0][1]][bot[0][0]] += 1

        # move
        bot = move(bot, turn)

        parent_conn.send(m[bot[0][1]][bot[0][0]])
        col = parent_conn.recv()

    icp.join()
    printm(m, bot)
    
    cnt = 0
    for y in range(len(painted)):
        for x in range(len(painted[y])):
            if painted[y][x] > 0:
                cnt += 1
    print(cnt)

