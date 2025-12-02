f = open('in1.txt')
ll = f.read().split()

dial, prev = 50, 50
cnt_zero, cnt_rotate = 0, 0

for l in ll:
    neg = (l[0]=='L')
    move = (-1 if neg else 1) * int(l[1:])
    dial += move

    r = abs(dial//100)
    if (dial % 100 == 0 and dial != 0 and not neg) or (prev == 0 and neg):
        r -= 1
    
    dial = dial % 100
    if dial == 0:
        cnt_zero += 1    
    cnt_rotate += r
    #print(f"{prev:5} + {move:5} = {prev+move:5}| dial:{dial:3}, rotate:{r:3} |{cnt_zero:5} {cnt_rotate:5}| {cnt_zero + cnt_rotate:5}")
    prev = dial
print('Part A: ', cnt_zero)
print('Part B: ', cnt_zero + cnt_rotate)


