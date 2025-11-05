
import time

start = time.time()


from itertools import groupby

def iterate(inp):
    s = ""
    for k, g in groupby(inp):
        s += str(len(list(g))) + str(k)
    return s

def length_niter(inp, n):
    for a in range(n):
        inp = iterate(inp)
        print(a)
    return len(inp)

inp = '3113322113'
print(length_niter(inp, 40))



end = time.time()
print(end - start)
