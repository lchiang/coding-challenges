import string
lc = string.ascii_lowercase
l_forbid_letter = [lc.index(c) for c in ['i','o','l']]
l_inc_letter = [lc[i:i+3] for i in range(len(lc)-2)]
l_pairs = [c+c for c in lc]

input = 'hepxcrrq' # Part A input
input = 'hepxxyzz' # Part A answer, Part B input
p = [lc.index(c) for c in input]

step = 0
while True:  #and step < 10000:
    step += 1

    # add one + carry
    p[-1] += 1
    for i in range(7,0,-1):
        if p[i] >= len(lc):
            p[i-1] = p[i-1] + p[i] // len(lc)
            p[i] = p[i] % len(lc)

    # skip i,o,l
    for i in range(8):
        if p[i] in l_forbid_letter:
            # print('i', i, p, [lc[k] for k in p])
            while p[i] in l_forbid_letter:
                p[i] += 1
            for j in range(i+1, 8):
                p[j] = 0
            break

    ts = ''.join([lc[k] for k in p])
    # increasing letters
    if any(grp in ts for grp in l_inc_letter):

        # two pairs
        tts = ts
        for pair in l_pairs:
            tts = tts.replace(pair, ' ')
        for pair in l_pairs:
            tts = tts.replace(pair, ' ')
        if len(tts) == 6:
            print(step, tts, ts)
            break