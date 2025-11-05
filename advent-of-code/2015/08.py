
ll = open('in08.txt').read().splitlines()
len_l, len_m, len_n = 0, 0, 0
for l in ll:
    k = l[1:-1]
    i, m, n = 0, 0, 6
    while i < len(k):
        m += 1
        if ((k[i] == '\\' and k[i+1]=='\\') or
            (k[i] == '\\' and k[i+1]=='\"')):
            i += 2
            n += 4
        elif k[i] == '\\' and k[i+1]=='x':
            i += 4
            n += 5
        else:
            i += 1
            n += 1
    len_l += len(l)
    len_m += m
    len_n += n
print(len_l - len_m) # Part A
print(len_n - len_l) # Part B