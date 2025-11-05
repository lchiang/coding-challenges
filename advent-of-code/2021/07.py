f = open('in07.txt')
l = [int(x) for x in f.readline().split(',')]
#l = [16,1,2,0,4,2,7,1,2,14]
d = {}
for pos in range(min(l), max(l)+1):
    r = 0
    for x in l:       
        #r += abs(x-pos) # Part A        
        r += abs(x-pos) * (abs(x-pos)+1) // 2 # Part B, Triangular number: n(n+1)/2
    d[pos] = r
print(d[min(d, key=d.get)])