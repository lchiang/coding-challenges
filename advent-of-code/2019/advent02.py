import csv

with open('input02.txt', newline='') as csvfile:
    d = list(csv.reader(csvfile))[0]
    
d = list(map(int,d))


d[1] = 78
d[2] = 70

i = 0

while (d[i]!=99):
    #print(d[i:i+4], d[i])
    #print(d)
    if (d[i] == 1):
        re = d[d[i+1]] + d[d[i+2]]
    elif (d[i] == 2):
        re = d[d[i+1]] * d[d[i+2]]
    pos = d[i+3]
    d[pos]=re
    #print(d)
    
    i += 4   
    
print(d[0])
print(100 * 78 + 70)