f = open('in01.txt')
inputfile = f.read().splitlines()
l = [int(i) for i in inputfile]
a, b = 0, 0
for i, item in enumerate(l):
    if (i < len(l)-1):        
        if (l[i] < l[i+1]):
            a += 1

    if (i < len(l)-3):        
        if (sum(l[i:i+3]) < sum(l[i+1:i+4])):
            b += 1
print(a, b)
    
