def printmap(m):
    for y in range(len(m)):
        print(''.join(['#' if v==1 else '.' for v in m[y]]))
    print()

if __name__ == '__main__':
    f = open('input24.txt')
    li = f.read().splitlines()
    h = len(li)
    w = len(li[0])

    m = []
    for y in range(h):               
        m.append([1 if v=='#' else 0 for v in li[y]])

    print('original map')
    printmap(m)
        
    bio_dict = []
    
    for i in range(100):
        cm = [] # map for counting

        for y in range(h):
            cm.append([])
            for x in range(w):
                cm[y].append(0)
                c = 0
                
                if x == 0:
                    c += m[y][x+1]
                elif x == w-1:
                    c += m[y][x-1]
                else:
                    c += (m[y][x-1] + m[y][x+1])

                if y == 0:
                    c += m[y+1][x]
                elif y == h-1:
                    c += m[y-1][x]
                else:
                    c += (m[y-1][x] + m[y+1][x])
                cm[y][x] = c
                
        #print('count map')
        #for y in range(len(cm)):
        #    print(cm[y])

        bio_hash = 0
        bh = 1
        
        nm = []
        for y in range(h):
            nm.append([])
            for x in range(w):
                nm[y].append(0)
                if m[y][x] == 1: #bug
                    nm[y][x] = 1 if (cm[y][x] == 1) else 0
                else: #empty
                    nm[y][x] = 1 if ((cm[y][x] == 1) or (cm[y][x] == 2)) else 0
                bio_hash += nm[y][x] * bh
                bh = bh*2


            
        print('After ', i+1, 'minutes. Biohash:', bio_hash)
        printmap(nm)
        

        if bio_hash in bio_dict:
            print('found')
            break
        else:
            bio_dict.append(bio_hash)


        # copy map
        for y in range(h):
            m[y] = nm[y].copy()

      
