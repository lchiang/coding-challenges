f = open('in6c.txt')
ll = f.read().splitlines()

r = {}
nn = [[] for i in range(12)]


print(nn)
for l in ll[2:]:
    lc = l.split()    
    r[lc[0]] = lc[2].split(',')
    
for key, value in r.items():
    print(f"{key}: {value}")


def fit(name):
    for i in range(len(name)-1):        
        if (name[i+1] not in r[name[i]]):
            return False
    return True

start_lv = 12
for n in ll[0].split(','):
    print(n, fit(n))
    if fit(n):
        nn[len(n)].append(n)
        start_lv = min(start_lv, len(n))
print(nn, start_lv)


for i in range(start_lv, 7):#11):
    #print(i, nn[i])
    #print(i)
    for n in nn[i]:
        if n[-1] in r:
            #print(n)
            for c in r[n[-1]]:                
                if n+c not in nn[i+1]:
                    nn[i+1].append(n+c)
    #print(i, len(nn[i]))

for i in range(start_lv, 11):
    print(i, len(nn[i]), nn[i][:20])


'''
for i in [3,4,5,6,7,8]:
    end = []
    ed = {}
    for n in nn[i]:
        if n[-1] not in ed:
            ed[n[-1]] = 1
        else:
            ed[n[-1]] += 1
        if n[-1] not in end:
            end.append(n[-1])
    print('>',i, sorted(end))
    sorted_items = sorted(ed.items())
    sorted_dict = dict(sorted_items)
    print(sorted_dict)  
'''  


#print(sum([len(n) for n in nn[7:12]]))
'''
2 1
3 7
4 59
5 247
6 1402
7 6916
8
9
10
11
'''    

def num_comb(num, c):
    en = [[] for x in range(5)]
    en[0] = c
    for i in range(0, num-1):
        #print(i)
        for n in en[i]:
            if n[-1] in r:
                for c in r[n[-1]]:                    
                    if n+c not in en[i+1]:
                        en[i+1].append(n+c)
    return len(en[num-1])

#Tharnri8901
een = ['a', 'b', 'd', 'e', 'h', 'i', 'k', 'l', 'n', 'o', 'r', 's', 't', 'v', 'x', 'y', 'z']

result = len(nn[7])

for digit in range(8,12):
    print(digit)

    suf = {}
    for n in een:
        suf[n] = num_comb(digit-6, n)

    print(suf)

    #print(7, len(nn[7]), nn[7][:20])

    count = 0
    for n in nn[7]:
        count+=suf[n[-1]]
    print(count)
    result += count
print(result)
