f = open('in02.txt')
inputfile = f.read().splitlines()
h, d = 0, 0
for l in inputfile:
    c, n = l.split()
    n = int(n)
    if (c == 'forward'):
        h += n
    elif (c == 'up'):
        d -= n
    elif (c == 'down'):
        d += n
print(d*h)
