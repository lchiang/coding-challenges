with open('in6.txt') as f:
    ll = f.read().splitlines()

import math

def part_1():
    pp = []
    sign = []
    for i, v in enumerate(ll):
        parts = v.split()
        if i == len(ll) - 1:
            sign = parts
        else:
            pp.append([int(x) for x in parts])
    total_sum = 0
    for i in range(len(pp[0])):
        match sign[i]:
            case '+':
                total_sum += sum([pp[vi][i] for vi in range(len(pp))])
            case '*':
                total_sum += math.prod([pp[vi][i] for vi in range(len(pp))])
    print('part 1', total_sum)

def part_2():
    def is_problem_break(x):
        if x == len(ll[0]):
            return True
        for i in range(len(ll)):
            if ll[i][x] != ' ':
                return False
        return True

    nn = []
    total_sum = 0
    for x in range(len(ll[0])+1):
        if not is_problem_break(x):
            if ll[-1][x] != ' ':
                sign = ll[-1][x]
            nn.append(int(''.join([ll[i][x] for i in range(len(ll)-1)])))
        else:
            match sign:
                case '+':
                    total_sum += sum(nn)
                case '*':
                    total_sum += math.prod(nn)
            nn = []
    print('part 2', total_sum)

part_1()
part_2()