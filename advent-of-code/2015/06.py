import re
import string
ll = open('in06.txt').read().splitlines()
#ll = ['turn on 0,0 through 999,999','toggle 0,0 through 999,0','turn off 499,499 through 500,500']

b = [[0]*1000 for i in range(1000)]
def print_board(b):
    for l in b:
        print(''.join(str(x) for x in l))

for l in ll:
    m = re.search(r'(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)', l)
    (cmd, x1, y1, x2, y2) = m.groups()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):

            ''' Part A
            if cmd == 'turn on':
                b[y][x] = 1
            elif cmd == 'turn off':
                b[y][x] = 0
            elif cmd == 'toggle':
                b[y][x] = (b[y][x]+1)%2
            '''

            if cmd == 'turn on':
                b[y][x] += 1
            elif cmd == 'turn off':
                b[y][x] = max(0, b[y][x] - 1)
            elif cmd == 'toggle':
                b[y][x] += 2

#print_board(b)
c = 0
for l in b:
    c += sum(l)
print(c)
