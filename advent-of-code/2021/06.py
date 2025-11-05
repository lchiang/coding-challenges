f = open('in06.txt')
l = [int(x) for x in f.readline().split(',')]

def after_days(init_list, days_later):    
    d = init_list
    for day in range(days_later):
        nd = {}
        nd[8] = d[0]
        nd[6] = d[0] + d[7]
        for i in [1,2,3,4,5,6,8]:
            nd[i-1] = d[i]        
        #print(d, '>', nd)        
        d = nd        
    return d

d = {x:0 for x in list(range(0,9))}
for x in l:
    d[x] += 1

print(sum(after_days(d.copy(), 80).values())) # Part A
print(sum(after_days(d.copy(), 256).values())) # Part B

'''
Previous Attempt
Can do part A, not enough memory for part B

def after_days_list(init_list, days_later):
    l = init_list
    for day in range(days_later):
        for i, v in enumerate(l):
            if v > 0:
                l[i] = v-1
            else:
                l[i] = 6
                l.append(9)
    return len(l)
'''