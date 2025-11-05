f = open('input05.txt')
d = f.readline().split(',')
d = list(map(int, d))

i = 0
input_val = 5

while (d[i]!=99):
    #print('instruction:', d[i])
    #print(d[:10])
    opcode = d[i]%100
    param1_is_pos = (d[i]//100%10 == 0)
    param2_is_pos = (d[i]//1000%10 == 0)
    param3_is_pos = (d[i]//10000%10 == 0)

    if (opcode == 1):
        param1 = d[d[i+1]] if param1_is_pos else d[i+1]
        param2 = d[d[i+2]] if param2_is_pos else d[i+2]
        val = param1 + param2
        d[d[i+3]]=val
        i += 4
        
    elif (opcode == 2):
        param1 = d[d[i+1]] if param1_is_pos else d[i+1]
        param2 = d[d[i+2]] if param2_is_pos else d[i+2]
        val = param1 * param2        
        d[d[i+3]]=val
        i += 4
        
    elif (opcode == 3):        
        d[d[i+1]]=input_val
        i += 2
        
    elif (opcode == 4):
        param1 = d[d[i+1]] if param1_is_pos else d[i+1]
        print(param1)
        i += 2
        
    elif (opcode == 5):
        param1 = d[d[i+1]] if param1_is_pos else d[i+1]
        param2 = d[d[i+2]] if param2_is_pos else d[i+2]
        i = param2 if (param1 != 0) else i+3
        
    elif (opcode == 6):
        param1 = d[d[i+1]] if param1_is_pos else d[i+1]
        param2 = d[d[i+2]] if param2_is_pos else d[i+2]
        i = param2 if (param1 == 0) else i+3
        
    elif (opcode == 7):
        param1 = d[d[i+1]] if param1_is_pos else d[i+1]
        param2 = d[d[i+2]] if param2_is_pos else d[i+2]        
        d[d[i+3]] = 1 if param1 < param2 else 0
        
        i += 4
    elif (opcode == 8):        
        param1 = d[d[i+1]] if param1_is_pos else d[i+1]
        param2 = d[d[i+2]] if param2_is_pos else d[i+2]        
        d[d[i+3]] = 1 if param1 == param2 else 0
        i += 4
        
    else:
        break
    #print(d)
    
#print(d[0])
