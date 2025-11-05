f = open('in01.txt')
l = f.read().split()
l = [int(i) for i in l]


# Part A
for i in l:
    for k in l:
        if i != k:
            if (i+k) == 2020:
                print(i*k)
                
#Part B
for i in l:
    for k in l:
        for j in l:
            if i != k and i != j and k != j:
                if (i+k+j) == 2020:
                    print(i*k*j)
            
            
