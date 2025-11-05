import multiprocessing

def param(d, i, param_num, rel):
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
        rel_pos = rel + d[i+param_num]
        return d[rel_pos]

def param_write(d, i, param_num, rel):    
    mode = d[i]//(10*(10**param_num))%10
    # 0 = position mode, raw
    # 1 = immediate mode, raw
    # 2 = relative mode, rel_base+raw
    if (mode == 0 or mode == 1):
        return d[i+param_num]
    else: # mode = 2
        return rel + d[i+param_num]


def intercode(code, conn):
    i = 0
    #print('intercode', code[i], i, input_val)
    r = 0 #relative base
    d = code      
        
    while (d[i]!=99):
        #print('instruction',i,':', d[i:i+3])
        opcode = d[i]%100
            
        if (opcode == 1):
            val = param(d,i,1,r) + param(d,i,2,r)        
            d[param_write(d,i,3,r)]=val
            i += 4
            
        elif (opcode == 2):
            val = param(d,i,1,r) * param(d,i,2,r)        
            d[param_write(d,i,3,r)]=val
            i += 4
            
        elif (opcode == 3):
            #print('INTERCODE: waiting for input')
            d[param_write(d,i,1,r)]=conn.recv()
            #print('INTERCODE: receiving', d[param_write(d,i,1,r)])
            i += 2        
            
        elif (opcode == 4):        
            #print(param(d,i,1,r))
            conn.send(param(d,i,1,r))
            #print('INTERCODE: sending', param(d,i,1,r))
            i += 2
            
        elif (opcode == 5):
            i = param(d,i,2,r) if (param(d,i,1,r) != 0) else i+3
            
        elif (opcode == 6):
            i = param(d,i,2,r) if (param(d,i,1,r) == 0) else i+3
            
        elif (opcode == 7):
            d[param_write(d,i,3,r)] = 1 if param(d,i,1,r) < param(d,i,2,r) else 0        
            i += 4
            
        elif (opcode == 8):
            d[param_write(d,i,3,r)] = 1 if param(d,i,1,r) == param(d,i,2,r) else 0
            i += 4
            
        elif (opcode == 9):
            r += param(d,i,1,r)
            i += 2

        else:
            break
        
    conn.send('HALT')

def intercode_one_output(code, input_list):
    i = 0
    r = 0 #relative base
    d = code.copy()
    while (d[i]!=99):
        opcode = d[i]%100            
        if (opcode == 1):
            val = param(d,i,1,r) + param(d,i,2,r)        
            d[param_write(d,i,3,r)]=val
            i += 4            
        elif (opcode == 2):
            val = param(d,i,1,r) * param(d,i,2,r)        
            d[param_write(d,i,3,r)]=val
            i += 4            
        elif (opcode == 3):
            d[param_write(d,i,1,r)]=input_list.pop(0)
            i += 2            
        elif (opcode == 4):                    
            return param(d,i,1,r)
            i += 2            
        elif (opcode == 5):
            i = param(d,i,2,r) if (param(d,i,1,r) != 0) else i+3            
        elif (opcode == 6):
            i = param(d,i,2,r) if (param(d,i,1,r) == 0) else i+3            
        elif (opcode == 7):
            d[param_write(d,i,3,r)] = 1 if param(d,i,1,r) < param(d,i,2,r) else 0        
            i += 4            
        elif (opcode == 8):
            d[param_write(d,i,3,r)] = 1 if param(d,i,1,r) == param(d,i,2,r) else 0
            i += 4            
        elif (opcode == 9):
            r += param(d,i,1,r)
            i += 2
        else:
            break
        
    
def start_intercode_process(code):
    parent_conn, child_conn = multiprocessing.Pipe()
    icp = multiprocessing.Process(target=intercode, args=(code, child_conn))
    icp.start()
    return (icp, parent_conn)
    

