if __name__ == '__main__':
    f = open('input22.txt')
    li = f.read().splitlines()

    nn = 10007 
    d = [x for x in range(nn)]

    for l in li:
        if l.startswith('deal into new stack'):
            #print('new stack')
            d = d[::-1]
            #print(d)
        elif l.startswith('deal with increment'):
            n = int(l.split(' ')[-1])
            #print('increase', n)
            t = d.copy()
            index = 0
            while t:
                d[index] = t.pop(0)
                index = (index + n) % len(d)
        elif l.startswith('cut'):
            n = int(l.split(' ')[-1])
            d = d [n:] + d[:n]
        else:
            break
    print(d.index(2019))
