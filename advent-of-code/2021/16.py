l = open('in16.txt').read().splitlines()[0]
#l = '9C0141080250320F1802104A08'

hb = bin(int(l, 16))
hb = hb[2:].zfill(len(l) * 4) # pad zero

total_v = 0

def read_packet(b):
    #print('read:', len(b))#, b)
    i, result = 0, 0

    version = int(b[i:i+3],2)
    i+=3
    type_id = int(b[i:i+3],2)
    i+=3
    #print('version', version, 'type', type_id)

    global total_v
    total_v += version

    if type_id == 4: # literal value
        read_next = True
        lit = ''
        while read_next:
            read_next = (b[i]=='1')
            lit += b[i+1: i+5]
            i += 5
        #print('literal >', int(lit,2))
        result = int(lit,2)

    else: #operator
        length_type_id = b[i]
        i += 1
        vl = []
        if length_type_id == '0':
            sp_length = int(b[i:i+15],2)
            i += 15
            tl = 0
            while tl < sp_length:
                #print('> will read pack with length', sp_length, 'from', i+tl)
                (l, v) = read_packet(b[i+tl:i+sp_length])
                tl += l
                vl.append(v)
            i += sp_length
            #print(i, '> done read pack')
        else: # 1
            sp_num = int(b[i:i+11],2)
            i += 11
            #print('> will read', sp_num, 'pack')
            for j in range(sp_num):
                (l, v) = read_packet(b[i:])
                i += l
                vl.append(v)
            #print('> done read pack')

        if type_id == 0: # sum
            result = sum(vl)
        elif type_id == 1: # product
            re = 1
            for x in vl:
                re = re * x
            result = re
        elif type_id == 2: # min
            result = min(vl)
        elif type_id == 3: # max
            result = max(vl)
        elif type_id == 5: # gt
            result = 1 if vl[0] > vl[1] else 0
        elif type_id == 6: # lt
            result = 1 if vl[0] < vl[1] else 0
        elif type_id == 7: # eq
            result = 1 if vl[0] == vl[1] else 0

    return (i,result) # length read, value

(lll,vvv) = read_packet(hb)
print('total version', total_v)
print('result', vvv)
