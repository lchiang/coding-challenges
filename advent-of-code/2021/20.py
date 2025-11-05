
ll = open('in20.txt').read().splitlines()

en = 50
algo = ll[0]
width = len(ll[2])
height = len(ll)-2

def print_board(b):
   for l in b:
       print('>',''.join(['{:1}'.format(c) for c in l]))
   print()

b = [list(x) for x in ll[2:]]
#print_board(b)

# add padding
pb = []
for i in range(3):
    pb.append(['.'] * (len(b[0]) + 6))
for k in b:
    x = ['.'] * 3
    pb.append(x+k+x)
for i in range(3):
    pb.append(['.'] * (len(b[0])  + 6))
b = pb
#print('after padding')
#print_board(b)

for i in range(en):
    print('round', i+1)

    #enhance
    nb = [x[:] for x in b]
    for y in range(1,len(b)-1):
        for x in range(1,len(b[0])-1):
            e = b[y-1][x-1:x+1+1] + b[y][x-1:x+1+1] + b[y+1][x-1:x+1+1]
            bin_str = ''.join(['1' if x=='#' else '0' for x in e])
            nb[y][x] = algo[int(bin_str, 2)]
    b = nb
    #print('after enhance')
    #print_board(nb)

    ch = algo[0] if i%2 == 0 else algo[-1]
    #fix padding
    pb = []
    for i in range(2):
        pb.append([ch] * (len(b[0])-2 + 4))
    for k in b[1:-1]:
        x = [ch] * 2
        pb.append(x+k[1:-1]+x)
    for i in range(2):
        pb.append([ch] * (len(b[0])-2 + 4))
    b = pb
    #print('after fix padding')
    #print_board(b)

cnt = 0
for y in range(3,len(b)-3):
    for x in range(3,len(b[0])-3):
        if b[y][x] == '#':
            cnt += 1
print(cnt)

