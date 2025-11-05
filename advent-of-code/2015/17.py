from itertools import combinations
l = [5, 20, 15, 10, 5] # Sample
l = [33,14,18,20,45,35,16,35,1,13,18,13,50,44,48,6,24,41,30,42]
target = 150
cnt = 0
min_con = len(l)
for r in range(1,len(l)+1):
    c = [x for x in combinations(l,r)]
    for a in c:
        if sum(a) == target and min_con >= len(a):
            cnt += 1
            min_con = min(min_con, len(a))
print(cnt, min_con)