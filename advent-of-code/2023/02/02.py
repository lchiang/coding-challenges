#ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

d = {'red':12, 'green':13, 'blue':14}
possible_all, power_all = 0, 0
for l in ll:
    game_ind = int(l.split(':')[0].split(' ')[1])
    m = {}
    possible = True
    for batch in l.split(':')[1].split(';'):
        for b in batch.split(','):
            num = int(b.split(' ')[1])
            col = b.split(' ')[2]
            if col in m:
                m[col] = max(m[col], num)
            else:
                m[col] = num
            if d[col] < num:
                possible = False

    power = m['red']*m['green']*m['blue']
    power_all += power
    if possible:
        possible_all += game_ind

print('a', possible_all)
print('b', power_all)
