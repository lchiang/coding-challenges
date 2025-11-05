f = open('input08.txt')
d = f.readline()
d = [int(x) for x in d] 

w = 25
h = 6
layer_num = len(d) // (w * h)

min_zero_layer = layer_num + 1
min_zero = w*h+1

for j in range(layer_num):    
    layer_start = j * w * h
    layer_end = layer_start + w * h
    zero_cnt = d[layer_start:layer_end].count(0)
    if zero_cnt < min_zero:
        min_zero = zero_cnt
        min_zero_layer = j
        cnt_1 = d[layer_start:layer_end].count(1)
        cnt_2 = d[layer_start:layer_end].count(2)
    #print(j, layer_start, layer_end, zero_cnt, min_zero, min_zero_layer, cnt_1*cnt_2)
    #for i in range(h):
        #print(d[layer_start + i*w: layer_start + i*w+w])
    
fin = []
for i in range(w*h):
    pxl = d[i]
    #print(pxl)
    lay_num = 0
    while (pxl == 2):
        pxl = d[i + lay_num*w*h]
        lay_num += 1
    fin.append(pxl)

for i in range(h):
    print(fin[i*w: i*w+w])

