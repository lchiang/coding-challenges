f = open('input03.txt')
line1 = f.readline().split(',')
line2 = f.readline().split(',')
f.close()


def read_input_line(line):
    ind_x = 0
    ind_y = 0
    segment = []
    for step in line:
        start_x, start_y = ind_x, ind_y
        if (step[0] == 'R'):
            ind_x += int(step[1:])
            orientation = 'hori'
        elif (step[0] == 'L'):
            ind_x -= int(step[1:])
            orientation = 'hori'
        elif (step[0] == 'U'):
            ind_y += int(step[1:])
            orientation = 'vert'
        elif (step[0] == 'D'):
            ind_y -= int(step[1:])
            orientation = 'vert'
        end_x, end_y = ind_x, ind_y
        line_seg = (orientation, start_x, start_y, end_x, end_y, int(step[1:]))
        segment.append(line_seg)
        #print("Step: {0}{1:4} -> {2}".format(step[0], int(step[1:]), line_seg))
    return segment

seg1 = read_input_line(line1)
seg2 = read_input_line(line2)

def ptOnLine(pt, line):
    if line[0] == 'hori':
        return (pt[1] == line[2]) and between(pt[0], line[1], line[3])
    else:
        return (pt[0] == line[1]) and between(pt[1], line[2], line[4])
    
def between(pt, st, en):
    return (pt<st) ^ (pt<en)
    
def crossAt(l1, l2):    
    crx = ()
    if l1[0] == l2[0]: #same direction
        crx = ()
    elif l1[0] == 'hori': # l1- l2|
        c = (l2[1], l1[2])        
        cx_in_l1x = between(c[0], l1[1], l1[3])
        cy_in_l2y = between(c[1], l2[2], l2[4])        
        crx = c if cx_in_l1x and cy_in_l2y else ()
    elif l1[0] == 'vert': # l1| l2-
        c = (l1[1], l2[2])
        cx_in_l2x = between(c[0], l2[1], l2[3])
        cy_in_l1y = between(c[1], l1[2], l1[4])        
        crx = c if cx_in_l2x and cy_in_l1y else ()
    #print(l1, l2, crx)
    return crx
        
    
cross_list = []
for line1 in seg1:
    for line2 in seg2:
        c = crossAt(line1, line2)
        if (len(c) > 0) and (c != (0,0)):
            cross_list.append(c)
        

#print(cross_list)
#print([abs(c[0]) + abs(c[1]) for c in cross_list])
#print(min([abs(c[0]) + abs(c[1]) for c in cross_list]))

minlen = 99999999
for c in cross_list:
    l = 0
    for s1 in seg1:
        if ptOnLine(c, s1):         
            l += abs(s1[1]-c[0])+abs(s1[2]-c[1])
            break
        else:           
            l += s1[5]
    for s2 in seg2:
        if ptOnLine(c, s2):      
            l += abs(s2[1]-c[0])+abs(s2[2]-c[1])
            break
        else:           
            l += s2[5] 
    if l<minlen:
        minlen = l
        print(c, l)

print('END')
