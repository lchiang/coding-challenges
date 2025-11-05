import time
import numpy as np
start_time = time.time()

f = open('input16.txt')
s = f.read().splitlines()[0]
l = [int(c) for c in s]
#print('input list:',l)

base_pattern = [0,1,0,-1]
repeating_pat = []
phase_target = 100
skip_pat = []

def repeating_pattern(pattern, length, repeat_num):
    re = [item for item in pattern for i in range(repeat_num)]
    loop_num = (length+1)//len(re) + 1
    return (re * loop_num)[1:length+1]

for i in range(1,len(l)+1):
    rp = repeating_pattern(base_pattern, len(l), i)    
    #print(rp, all(x == 0 for x in rp))
    repeating_pat.append(rp[i-1:])    

# part 1
input_list = l
for p in range(phase_target):
    out_list = []
    for i in range(len(l)):
        if (i <= len(l)//2):
        #dp = sum([a*b for (a, b) in zip(input_list[i:], repeating_pat[i][i:])]) # dot product
            dp = sum([a*b for (a, b) in zip(input_list[i:], repeating_pat[i])]) # dot product
        else:
            dp = sum(input_list[i:])        
        out_list.append(abs(dp)%10)
    input_list = out_list

print('Part 1 :', ''.join([str(x) for x in out_list]))
print('--- {0:5f} s ---'.format(time.time() - start_time))


# part 2
input_list = l * 10000
message_offset = int(''.join(map(str,l[:7])))
input_list = input_list[message_offset:]

#print('input len :',len(input_list))
#print('offset :',message_offset)
#print('len :', len(input_list))

for p in range(phase_target):
    out_list = [0 for x in range(len(input_list))]
    ss = 0
    for i in range(1, len(input_list)+1):
        ss += input_list[-i]
        out_list[-i] = abs(ss)%10    
    input_list = out_list

print('Part 2 :', ''.join([str(x) for x in out_list[:8]]))    
print('--- {0:5f} s ---'.format(time.time() - start_time))


