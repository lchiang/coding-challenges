import math

m = [list(line.rstrip('\n')) for line in open('input10.txt')]

#print(m)
#lines[y][x]

def printmap(m):
    for y in range(len(m)):
        print(''.join(m[y]))

printmap(m)

ast_list = {} # (x,y) : num of can see

for y in range(len(m)):
    for x in range(len(m[y])):
        if (m[y][x] == '#'):
            ast_list[(x,y)] = 0
        
#print(ast_list)


for station in ast_list:
    #print('checking', station)
    for aa in ast_list:
        if (aa != station):
            xdiff = aa[0]-station[0]
            ydiff = aa[1]-station[1]
            blocked = False
            if (xdiff==0):
                if ydiff > 0:
                    for yy in range(1, ydiff):
                        if ((station[0], station[1]+yy) in ast_list):
                            #print((station[0], station[1]+yy), 'blocking', aa)
                            blocked = True
                else:
                    for yy in range(-1, ydiff, -1):
                        if ((station[0], station[1]+yy) in ast_list):
                            #print((station[0], station[1]+yy), 'blocking', aa)
                            blocked = True
            elif (ydiff==0):
                if xdiff > 0:
                    for xx in range(1, xdiff):
                        if ((station[0]+xx, station[1]) in ast_list):
                            
                            blocked = True
                else:
                    for xx in range(-1, xdiff, -1):
                        if ((station[0]+xx, station[1]) in ast_list):
                            blocked = True
            else:
                g = math.gcd(abs(xdiff),abs(ydiff))
                for k in range (1,g):
                    if ((station[0]+xdiff//g*k, station[1]+ydiff//g*k) in ast_list):
                        blocked = True
            if not blocked:
                ast_list[station] += 1
                
                #print(station ,'can see', aa)

#for y in range(len(m)):    
#    li = ['.' if (x,y) not in ast_list else str(ast_list[(x,y)]) for x in range(len(m[y]))]
#    print(''.join(li))

print(max(ast_list, key=ast_list.get), ast_list[max(ast_list, key=ast_list.get)])

print('END')


