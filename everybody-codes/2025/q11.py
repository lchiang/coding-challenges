input = [9,1,1,4,9,6] # part i test, ii test
#input = [3,3,19,16,19,12] # part i
input = [805,706,179,48 ,158,150,232,885,598,524,423] # part ii test
print(input)

#f = open('in11b.txt')
#input = [int(s) for s in f.read().splitlines()]
#print(input)

def fchk(l):
    c = 0
    for i in range(len(l)):
        
        c += (i+1) * l[i]
    return c

print(fchk(input))

max_round = 3000000000
l = input.copy()
r = 0

flock_chk = fchk(l)
flock_chk_prev = 0

#print('Round', r, l, flock_chk_prev, flock_chk)

while r < max_round and flock_chk != flock_chk_prev:
    flock_chk_prev = flock_chk
    for i in range(len(l)-1):        
        if l[i] > l[i+1]:
            l[i] -= 1
            l[i+1] += 1    
    flock_chk = fchk(l)
    r += 1

    if r%1000 == 0:
        print('Round', r, l, flock_chk_prev, flock_chk)

r -= 1
flock_chk_prev = 0

print("after A", r)
print('Round', r, l, flock_chk_prev, flock_chk)

mean = sum(l) // len(l)
print(mean)
print(1579-861)
print([x-mean for x in l if x>mean])
print(sum([x-mean for x in l if x>mean]))
print(sum([x-mean for x in l if x<mean]))


while r < max_round and flock_chk != flock_chk_prev:   
    flock_chk_prev = flock_chk
    for i in range(len(l)-1):        
        if l[i] < l[i+1]:
            l[i] += 1
            l[i+1] -= 1    
    flock_chk = fchk(l)
    r += 1

    if r%100 == 0:
        print('Round', r, l, flock_chk_prev, flock_chk)

r -= 1
flock_chk_prev = 0

print(r)