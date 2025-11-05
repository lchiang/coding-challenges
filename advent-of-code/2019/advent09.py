f = open('input09.txt')
d = f.readline().split(',')
d = list(map(int, d))
i = 0
input_val = 2
relative_base = 0

d += [0 for x in range(35015192)]

    
def param(d, i, param_num):
    #print(d[i:i+4], d[i+param_num])
    mode = d[i]//(10*(10**param_num))%10
    # 0 = position mode, d[raw]
    # 1 = immediate mode, raw
    # 2 = relative mode, d[rel_base+raw]    
    if (mode == 0):
        return d[d[i+param_num]]
    elif (mode == 1):
        return d[i+param_num]
    else: # mode = 2
        rel_pos = relative_base + d[i+param_num]
        return d[rel_pos]

def param_write(d, i, param_num):    
    mode = d[i]//(10*(10**param_num))%10
    # 0 = position mode, raw
    # 1 = immediate mode, raw
    # 2 = relative mode, rel_base+raw
    if (mode == 0 or mode == 1):
        return d[i+param_num]
    else: # mode = 2
        return relative_base + d[i+param_num]
    
while (d[i]!=99):
    #print('instruction:', d[i])
    #print(d[:20], d[99:102])
    opcode = d[i]%100
        
    if (opcode == 1):
        val = param(d,i,1) + param(d,i,2)        
        d[param_write(d,i,3)]=val
        i += 4
        
    elif (opcode == 2):
        val = param(d,i,1) * param(d,i,2)        
        d[param_write(d,i,3)]=val
        i += 4
        
    elif (opcode == 3):        
        d[param_write(d,i,1)]=input_val
        i += 2
        
    elif (opcode == 4):        
        print(param(d,i,1))
        i += 2
        
    elif (opcode == 5):
        i = param(d,i,2) if (param(d,i,1) != 0) else i+3
        
    elif (opcode == 6):
        i = param(d,i,2) if (param(d,i,1) == 0) else i+3
        
    elif (opcode == 7):
        d[param_write(d,i,3)] = 1 if param(d,i,1) < param(d,i,2) else 0        
        i += 4
        
    elif (opcode == 8):
        d[param_write(d,i,3)] = 1 if param(d,i,1) == param(d,i,2) else 0
        i += 4
        
    elif (opcode == 9):
        relative_base += param(d,i,1)
        i += 2

    else:
        break
    #print(d)
    
#print(d[0])
