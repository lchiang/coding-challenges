ll = open('in07.txt').read().splitlines()
kk = sorted(ll)

d = {} # signal sorted out
c = {} # circuit

for l in ll:
    op, symbol = l.split(' -> ')
    #print('==', op, symbol)
    c[symbol] = op

def solve(s):
    #print('in solve', s)
    if s.isnumeric():
        return int(s)
    elif s in d:        
        return d[s]
    else:
        op = c[s]
        #print('cmd:',c[s])
        re = ''
        if 'AND' in op:
            l = op.split(' ')            
            re = solve(l[0]) & solve(l[2])
        elif 'OR' in op:
            l = op.split(' ')
            re = solve(l[0])| solve(l[2])
        elif 'LSHIFT' in op:
            l = op.split(' ')
            re = solve(l[0]) << int(l[2])
        elif 'RSHIFT' in op:
            l = op.split(' ')
            re = solve(l[0]) >> int(l[2])
        elif 'NOT' in op:        
            l = op.split(' ')            
            re = solve(l[1]) ^ 65535
        elif op.isnumeric():
            re = int(op)
        else:
            re = solve(op)
        if isinstance(re,int):
            d[s] = re
        return re

for k,v in c.items():
    #print(k, solve(k))
    solve(k)
    
#print('circuit dict :', c)
d = {key: value for key, value in sorted(d.items())}
#print('result dict  :', d)
print('result:', d['a'])
