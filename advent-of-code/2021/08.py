ll = open('in08.txt').read().splitlines()
d = {}
c = 0
total = 0
for l in ll:    
    signal, output = l.split(' | ')
    signal, output = signal.split(' '), output.split(' ')
    len5, len6 = [], []
    
    for s in signal:
        if len(s)==2:
            d[1] = sorted(s)
        elif len(s)==4:
            d[4] = sorted(s)
        elif len(s)==3:
            d[7] = sorted(s)
        elif len(s)==7:
            d[8] = sorted(s)
        elif len(s)==5: #235
            len5.append(sorted(s))
        elif len(s)==6: #069
            len6.append(sorted(s))
        else:
            print('should not print')
    
    for s in len5: #235
        if d[1][0] in s and d[1][1] in s: # '3' contains '1'
            d[3] = s    
        if len([x for x in s if x not in d[4]])==3: # '2' - '4' = 3 segments left
            d[2] = s
    len5.remove(d[2])
    len5.remove(d[3])
    d[5] = len5[0]
   
    for s in len6: #069
        if d[1][0] not in s or d[1][1] not in s: # '6' not contains '1'
            d[6] = s
        if len([x for x in s if x not in d[3]])==1: # '9' - '3' = 1 segments left
            d[9] = s
    len6.remove(d[6])
    len6.remove(d[9])
    d[0] = len6[0]    
    #print(d)

    oo = []
    for o in output:
        for k, v in d.items():
            if v ==sorted(o):
                oo.append(str(k))
    total += int(''.join(oo))
    
    # Part A
    for o in output:        
        if (len(o)==2 or len(o)==4 or len(o)==3 or len(o)==7):
            c += 1

print('Part A:', c)
print('Part B:', total)
