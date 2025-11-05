import re
import string
ll = open('in15.txt').read().splitlines()

d = []
for l in ll:
    m = re.search(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', l)
    (ing,cap,dur,fla,tex,cal) = m.groups()
    cap,dur,fla,tex,cal = int(cap),int(dur),int(fla),int(tex),int(cal)
    d.append([ing,cap,dur,fla,tex,cal])

n = 100
max_score = 0
max_combination = []
for i1 in range(0,n+1):
    for i2 in range(0, n+1-i1):
        for i3 in range(0, n+1-i1-i2):
            i4 = n-i1-i2-i3
            capacity = max(0, i1*d[0][1] + i2*d[1][1] + i3*d[2][1] + i4*d[3][1])
            durability = max(0, i1*d[0][2] + i2*d[1][2] + i3*d[2][2] + i4*d[3][2])
            flavor = max(0, i1*d[0][3] + i2*d[1][3] + i3*d[2][3] + i4*d[3][3])
            texture = max(0, i1*d[0][4] + i2*d[1][4] + i3*d[2][4] + i4*d[3][4])
            calories = i1*d[0][5] + i2*d[1][5] + i3*d[2][5] + i4*d[3][5]

            score = capacity*durability*flavor*texture
            if score > max_score and calories == 500:
                max_score = score
                max_combination = [i1,i2,i3,i4]
                print(max_score, max_combination)
