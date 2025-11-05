#ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()
#c, cl = 0, []
c = 0
for l in ll:
    #print(list(l))
    nn = [int(word) for word in list(l) if word.isdigit()]
    #print(nn[0],nn[-1])
    n = int(''.join([str(nn[0]),str(nn[-1])]))
    #print(n)
    c += n
print(c)
    
