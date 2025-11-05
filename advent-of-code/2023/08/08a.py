
ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

nav = ll[0]

d = {}
for l in ll[2:]:
    d[l[0:3]] = (l[7:10], l[12:15])

pos = 'AAA'
step = 0
while step < 100000:

    n = nav[step % len(nav)]
    if n == 'L':
        new_pos = d[pos][0]
    else: # R
        new_pos = d[pos][1]

    step += 1
    pos = new_pos
    if new_pos == 'ZZZ':
        break;
print(step)
