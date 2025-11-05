#ll = open('./2022/05/test.txt').read().splitlines()
ll = open('./2022/05/input.txt').read().splitlines()

empty_line = ll.index('')
stack_num = int(ll[empty_line-1].split()[-1])
s = [[] for x in range(stack_num+1)]

for i in range(empty_line-2, -1, -1):
    for j in range(1, stack_num+1):
        if ((len(ll[i]) > j*4-3) and (ll[i][j*4-3].isupper())):
                s[j].append(ll[i][j*4-3])
#print(s)

for l in ll[empty_line+1:]:
    cmd = l.split()
    mv, fm, to = int(cmd[1]), int(cmd[3]), int(cmd[5])
    ''' Part A Start
    for i in range(mv):
        c = s[fm].pop()
        s[to].append(c)
    '''
    ''' Part A End '''
    ''' Part B Start '''
    s[to] = s[to] + s[fm][mv*-1:]
    s[fm] = s[fm][:mv*-1]
    ''' Part B End'''

result = ''
for si in s:
    if (si):
        result = result + si[-1]
print(result)
