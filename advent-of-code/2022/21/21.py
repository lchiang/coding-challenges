ll = open('./2022/21/test.txt').read().splitlines()
ll = open('./2022/21/input.txt').read().splitlines()

m = {}
part_b = False

class Monkey:
    def __init__(self, name, job) -> None:
        self.name = name
        self.job = job

    def yell(self):
        #print('yelling', self.name, self.job)
        j = self.job
        if part_b and self.name == 'root':
            a, b = j.split(' + ')
            #print('yelling', self.name, self.job, m[a].yell(), m[b].yell(), m[a].yell()==m[b].yell())
            return m[a].yell()-m[b].yell()
        elif j.isnumeric():
            return int(j)
        elif '+' in j:
            a, b = j.split(' + ')
            return m[a].yell() + m[b].yell()
        elif '-' in j:
            a, b = j.split(' - ')
            return m[a].yell() - m[b].yell()
        elif '*' in j:
            a, b = j.split(' * ')
            return m[a].yell() * m[b].yell()
        elif '/' in j:
            a, b = j.split(' / ')
            return m[a].yell() / m[b].yell()
        return 0

for l in ll:
    n,j = l.split(': ')
    #print(n,j)
    m[n] = Monkey(n,j)

print('Part A', m['root'].yell())
part_b = True
low = 1 #+
high = 999999999999999 #-
while True:
    mid = (high+low)//2
    m['humn'].job = str(mid)
    tt = m['root'].yell()
    if tt==0:
        print('Part B', mid)
        break
    elif tt > 0:
        low = mid
    else:
        high = mid
    #print(mid, low, high, tt)
