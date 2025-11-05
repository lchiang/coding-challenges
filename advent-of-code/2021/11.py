ll = open('in11.txt').read().splitlines()
b = [[int(x) for x in l] for l in ll]
x_max = len(b[0])
y_max = len(b)

def print_board(bb):
    for l in bb:        
        print(''.join(['{:1}'.format(c) for c in l]))
    print('>')
print_board(b)

total_flash_num = 0
for step in range(500):
    #print('step', step+1)
    for y in range(len(b)):
        for x in range(len(b[0])):
            b[y][x] += 1

    nb = []
    for l in b:
        nb.append(l.copy())
    #print('after add one')
    #print_board(b)

    done_flash = False
    flashed = []
    while not done_flash:
        done_flash = True
        for y in range(len(b)):            
            for x in range(len(b[0])):                
                if b[y][x] > 9 and (x,y) not in flashed:
                    flashed.append((x,y))
                    total_flash_num += 1
                    xl = [xa for xa in range(max(0,x-1),min(len(b[0]),x+2))]
                    yl = [ya for ya in range(max(0,y-1),min(len(b[0]),y+2))]
                    #print(x,y,xl,yl)
                    for yy in yl:
                        for xx in xl:
                            if not(x==xx and y==yy):
                                #print(x,y,xx,yy)
                                nb[yy][xx] += 1
                                done_flash = False
        #print('just flash', done_flash, flashed)
        #print_board(nb)
        b = nb

    #print('flashed')
    for y in range(len(b)):            
        for x in range(len(b[0])):
            if b[y][x] > 9:   
                b[y][x] = 0    
    tt = 0
    for l in b:            
        tt += sum(l)

    if tt == 0:
        print('step', step+1)
        break
        # Step at break = Part B answer
    #print_board(b)
print(total_flash_num) # Part A answer