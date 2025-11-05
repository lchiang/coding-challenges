import multiprocessing
import math
import ic
import time

def param(d, i, param_num):
    mode = d[i]//(10*(10**param_num))%10
    # 0 = position mode, d[raw]
    # 1 = immediate mode, raw
    # 2 = relative mode, d[rel_base+raw]
    re = 0
    if (mode == 0):
        re = d[d[i+param_num]]
    elif (mode == 1):
        re = d[i+param_num]
    else: # mode = 2
        rel_pos = relative_base + d[i+param_num]
        re = d[rel_pos]
    return re
    

def param_write(d, i, param_num):    
    mode = d[i]//(10*(10**param_num))%10
    # 0 = position mode, raw
    # 1 = immediate mode, raw
    # 2 = relative mode, rel_base+raw
    if (mode == 0 or mode == 1):
        return d[i+param_num]
    else: # mode = 2
        return relative_base + d[i+param_num]


    
def intercode(input_val, code, i):    
    while (d[i]!=99):
        #print('instruction',i,':', d[i:i+3])
        #print(d, i, d[i])
        opcode = d[i]%100

        if (opcode == 1):
            #print(d[i:i+4], i, 1, '=', param(d,i,1), '=', param(d,i,2))
            val = param(d,i,1) + param(d,i,2)        
            d[param_write(d,i,3)]=val
            i += 4
            
        elif (opcode == 2):
            val = param(d,i,1) * param(d,i,2)        
            d[param_write(d,i,3)]=val
            i += 4
            
        elif (opcode == 3):
            d[param_write(d,i,1)]=input_val.pop(0)
            i += 2
            
        elif (opcode == 4):
            return param(d,i,1)
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
            
        else:
            break

def try_seq(seq, d):
    out = intercode([seq[0],0], d.copy(), 0)
    out = intercode([seq[1],out], d.copy(), 0)
    out = intercode([seq[2],out], d.copy(), 0)
    out = intercode([seq[3],out], d.copy(), 0)
    out = intercode([seq[4],out], d.copy(), 0)
    return out

def part1():
    max_out = 0
    import itertools
    for x in itertools.permutations([0,1,2,3,4], 5):
        oo = try_seq(x, d.copy())
        if oo > max_out:
            max_out = oo
            print(max_out)
    print(max_out)
    
def try_seq_2(seq, d):
    try:
        e_out = 0
        proc_a, conn_a = ic.start_intercode_process(d.copy())
        conn_a.send(seq[0])
        proc_b, conn_b = ic.start_intercode_process(d.copy())
        conn_b.send(seq[1])
        proc_c, conn_c = ic.start_intercode_process(d.copy())
        conn_c.send(seq[2])
        proc_d, conn_d = ic.start_intercode_process(d.copy())
        conn_d.send(seq[3])
        proc_e, conn_e = ic.start_intercode_process(d.copy())
        conn_e.send(seq[4])
        conn_a.send(0)    
        while True:
            conn_b.send(conn_a.recv())
            conn_c.send(conn_b.recv())    
            conn_d.send(conn_c.recv())    
            conn_e.send(conn_d.recv())    
            result_e = conn_e.recv()
            if result_e != 'HALT':
                e_out = int(result_e)
            if not proc_a.is_alive():
                break
            conn_a.send(result_e)
    except:
        #print('pipe closed')
        i=0
    return int(e_out)

def part2():
    max_out = 0
    import itertools
    for x in itertools.permutations([5,6,7,8,9], 5):
        oo = try_seq_2(x, d.copy())
        if oo > max_out:
            max_out = oo
            print(x, max_out)
    print(max_out)

if __name__ == '__main__':
    f = open('input07.txt')
    d = f.readline().split(',')
    d = list(map(int, d))

    print('Part 1')
    part1()

    print('Part 2')
    part2()


    
