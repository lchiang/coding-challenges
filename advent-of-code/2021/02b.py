f = open('in02.txt')
inputfile = f.read().splitlines()
a, h, d = 0, 0, 0 #aim, horizontal position, depth
for l in inputfile:
    c, x = l.split() #command, units
    x = int(x)
    if (c == 'forward'):
        h += x
        d += a*x
    elif (c == 'up'):
        a -= x
    elif (c == 'down'):
        a += x
print(d*h)
