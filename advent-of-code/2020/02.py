f = open('in02.txt')
l = f.read().splitlines()
#l = [int(i) for i in l]
    
import re
regex = r'([\d]+)-([\d]+) (\w): ([\w]+)'

# PART A
valid = 0
for ll in l:
    m = re.search(regex, ll)
    pw_min = int(m.group(1))
    pw_max = int(m.group(2))
    pw_ch = m.group(3)
    pw = m.group(4)
    pw_cnt = pw.count(pw_ch)
    if pw_min <= pw_cnt and pw_cnt <= pw_max:        
        valid += 1
print(valid)
        

# PART B
valid = 0
for ll in l:
    m = re.search(regex, ll)
    pw_pos1 = int(m.group(1))-1
    pw_pos2 = int(m.group(2))-1
    pw_ch = m.group(3)
    pw = m.group(4)
    p1 = pw[pw_pos1] == pw_ch
    p2 = pw[pw_pos2] == pw_ch    
    if (p1 or p2) and not (p1 and p2):        
        valid += 1
print(valid)
        
