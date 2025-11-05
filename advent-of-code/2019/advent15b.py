import os

def printscreen(m):
    #time.sleep(0.1)
    #os.system('cls')
    for yy in range(len(m)):
        li = m[yy].copy()
        print(''.join(li))

if __name__ == '__main__':
    f = open('input15b.txt')
    d = f.read().splitlines()
    
    h = len(d)
    w = len(d[0])
    m = []
    for y in range(h):
        m.append(list(d[y]))        
        
    printscreen(m)
    update_list = []
    
    i = 0
    finished = False
    while not finished:
        finished = True
        for y in range(h):
            for x in range(w):
                if m[y][x] == '.':
                    finished = False
                if m[y][x] == 'O':
                    print('oxygen at', x, y, m[y][x])
                    if m[y-1][x] == '.':
                        update_list.append((x, y-1))
                    if m[y+1][x] == '.':
                        update_list.append((x, y+1))
                    if m[y][x-1] == '.':
                        update_list.append((x-1, y))
                    if m[y][x+1] == '.':
                        update_list.append((x+1, y))
                    m[y][x] = 'o'
        if finished:
            print('done, i =', i)
            break
        else:
            while update_list:
                ux, uy = update_list.pop(0)
                m[uy][ux] = 'O'
            printscreen(m)
            i += 1
    
