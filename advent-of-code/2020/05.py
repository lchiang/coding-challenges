f = open('in05.txt')
inputfile = f.read().splitlines()

sid_list = []
for l in inputfile:
    row = int(l[:7].replace('F','0').replace('B','1'), 2)
    col = int(l[7:].replace('L','0').replace('R','1'), 2)
    #print(row, col, row * 8 + col)
    sid = row * 8 + col
    sid_list.append(sid)

# PART A
print(max(sid_list))

# PART B
l = [i for i in range(min(sid_list), max(sid_list))]
print(set(l)-set(sid_list))
