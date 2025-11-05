ll = open('test.txt').read().splitlines()
ll = open('input.txt').read().splitlines()

pts = 0
d,n = {},{}

for l in ll:
    game_ind = int(l.split(':')[0].split()[1])
    game_line = l.split(':')[1].split('|')
    win = game_line[0].split()
    num = game_line[1].split()
    lenw = len([x for x in num if x in win])
    d[game_ind] = lenw
    n[game_ind] = 1
    if lenw > 0:
        pts += 2**(lenw-1)
print('a',pts)

for i in range(1,len(ll)+1):    
    for ii in range(i+1, i+1+d[i]):        
        n[ii] = n[ii] + n[i]
print('b',sum(n.values()))
