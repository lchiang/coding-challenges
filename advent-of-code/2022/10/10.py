#ll = open('./2022/10/test2.txt').read().splitlines()
ll = open('./2022/10/input.txt').read().splitlines()

x, c, i, sss = 1, 1, 0, 0
turns_left = 0

cl = ''
while c < 280 and not(i >= len(ll) and turns_left == 0):
    if (c % 40 == 20):
        #print('cycle', c, ', x', x, c * x)
        sss += c * x

    pos = (c-1)%40
    cl = cl + ('#' if (pos == x-1 or pos == x or pos == x+1) else '.')
    if (c % 40 == 0):
        print(cl)
        cl = ''

    if (turns_left == 0): #get next cmd
        cmd = ll[i]
        i += 1
        if ('noop' == cmd):
            turns_left = 0
        elif  ('addx' in cmd):
            turns_left = 1

    elif (turns_left == 1):
        if  ('addx' in cmd):
            turns_left = 0
            x = x + int(cmd.split()[1])
    c+=1

print('Part A', sss)
