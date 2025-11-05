ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

h = len(ll)
w = len(ll[0])

symbol_dict = {}
for y in range(h):
    for x in range(w):        
        c = ll[y][x]
        if not c.isnumeric() and c != '.':
            #print(c, x, y)
            symbol_dict[(x,y)] = c
#print(symbol_dict)

adj_num = []
scanned_pos = []
g_adj_sum = 0

for p,v in symbol_dict.items():
    x, y = p    
    g_adj = []

    if v == '*': # add for part b
        #print(p,v, x,y)
        for yy in range(max(y-1,0),min(y+1,h-1)+1):
            for xx in range(max(x-1,0),min(x+1,w-1)+1):
                #print('>',xx,yy)
                if (xx,yy) != p and (xx,yy) not in scanned_pos:

                    c = ll[yy][xx]
                    if c.isnumeric():                    
                        s = c
                        #scan backard
                        kx = xx
                        while kx-1 >= 0 and ll[yy][kx-1].isnumeric():
                            s = ll[yy][kx-1] + s
                            scanned_pos.append((kx-1,yy))
                            kx = kx-1
                            
                        #scan foreward
                        kx = xx
                        while kx+1 < h and ll[yy][kx+1].isnumeric():
                            s = s + ll[yy][kx+1]
                            scanned_pos.append((kx+1,yy))
                            kx = kx+1
                        #print(s)
                        adj_num.append(int(s))
                        g_adj.append(int(s))
                    scanned_pos.append((xx,yy))
        
        if len(g_adj) == 2:
            g_adj_sum += g_adj[0]*g_adj[1]
            #print(scanned_pos)

print('a',sum(adj_num))
print('b',g_adj_sum)
