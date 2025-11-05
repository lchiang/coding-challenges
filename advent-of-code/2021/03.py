f = open('in03.txt')
inputfile = f.read().splitlines()
digit = len(inputfile[0])

def common_least(ll,i):
    one_cnt, zero_cnt = 0,0
    for l in ll:
        if l[i] == '1':
            one_cnt += 1
        else:
            zero_cnt += 1
    
    common = '1' if one_cnt >= zero_cnt else '0'
    least =  '0' if one_cnt >= zero_cnt else '1'
    return (common, least)

g, e = '', ''
for i in range(digit):
    (common,least) = common_least(inputfile,i)
    g += common
    e += least
print(int(g,2) * int(e,2)) # part A

ogrlist = inputfile.copy()
index = 0
while len(ogrlist) > 1 :
    ogrkeep = [] 
    common = common_least(ogrlist,index)[0]
    for l in ogrlist:        
        if l[index] == common:
            ogrkeep.append(l)
    #print(ogrkeep, common)
    ogrlist = ogrkeep
    index += 1
    
csrlist = inputfile.copy()
index = 0
while len(csrlist) > 1 :
    csrkeep = []
    least = common_least(csrlist,index)[1]
    for l in csrlist:        
        if l[index] == least:
            csrkeep.append(l)
    #print(csrkeep, least)
    csrlist = csrkeep
    index += 1

print(int(ogrlist[0],2) * int(csrlist[0],2)) # part B
