ll = open('in10.txt').read().splitlines()

total_error_pt = 0
score = []
for l in ll:
    s = []
    error_pt = 0
    for c in l:
        if c in ['(','[','{','<']:
            s.append(c)
        else:
            p = s.pop()
            e = '' #expected
            if p == '(': e = ')'
            elif p == '[': e = ']'
            elif p == '{': e = '}'
            elif p == '<': e = '>'
            if c != e:
                if c == ')': error_pt += 3
                elif c == ']': error_pt += 57
                elif c == '}': error_pt += 1197
                elif c == '>': error_pt += 25137
    total_error_pt += error_pt
    
    if error_pt == 0:
        f = []
        ss = 0
        for i in range(len(s)):
            p = s.pop()
            e = '' #expected
            if p == '(':
                e = ')'
                ss = ss*5 + 1
            elif p == '[':
                e = ']'
                ss = ss*5 + 2
            elif p == '{':
                e = '}'
                ss = ss*5 + 3
            elif p == '<':
                e = '>'
                ss = ss*5 + 4
            f.append(e)
        score.append(ss)
        
print('Part A:', total_error_pt)
print('Part B:', sorted(score)[len(score)//2])
