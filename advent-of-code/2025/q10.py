with open('in10_trimmed.txt') as f:
    ll = f.read().splitlines()

from itertools import product
def press(init_state, button, presses):
    s = list(init_state)
    for i in range(len(presses)):
        if presses[i]%2 == 1: # press i-th button
            for b in button[i]:
                s[b] ^= 1   # XOR flip
    return s

def toggle_combo(lights_num, buttons, target):
    combos = list(product([0,1], repeat=len(buttons)))
    combos.sort(key=lambda c: (sum(c), c))
    c = []
    for combo in combos:
        ls = press([0]*lights_num, buttons, combo)
        if ls==target:
            c.append(combo)
    return c

def min_press_to_off(init_state, buttons):
    combos = list(product([0,1], repeat=len(buttons)))
    combos.sort(key=lambda c: (sum(c), c))
    for combo in combos:
        ls = press(init_state, buttons, combo)
        if all(x == 0 for x in ls):
            return sum(combo)


def apply_combo(length, buttons, combo):
    result = [0] * length
    for count, btn in zip(combo, buttons):
        for idx in btn:
            result[idx] += count
    return result

def solve(target, buttons, max_val=10):
    n = len(buttons)
    solutions = []
    toggle_c = toggle_combo(len(target),buttons,[x % 2 for x in target])

    combosd = []
    for c in product(range(0, max_val+1), repeat=n):
        if tuple([x % 2 for x in c]) in toggle_c:
            combosd.append(c)
    combosd.sort(key=lambda c: (sum(c), c))
    for combo in combosd:  # positive integers only
        if apply_combo(len(target), buttons, combo) == target:
            solutions.append(combo)
            return sum(combo)



from itertools import product
from sympy import Matrix, linsolve, symbols, simplify

def button_matrix(buttons, light_num):
    m = []
    for b in buttons:
        b_line = [0]*light_num
        for i in b:
            b_line[i] = 1
        m.append(b_line)
    mm = Matrix(m, rational=False).T
    return mm

def solve_solution(button_M: Matrix, target: list):

    c = symbols(f'c0:{button_M.shape[1]}')
    sol = linsolve((button_M,Matrix(target)), c)

    exprs = list(sol)[0]
    free_vars = list(set().union(*[expr.free_symbols for expr in list(sol)[0]]))

    # print(exprs, free_vars)

    min_press = sum(target)
    ranges = [range(0, max(target)) for _ in free_vars]  # 0..10 for each variable
    for values in product(*ranges):
        subs_map = dict(zip(free_vars, values))
        substituted = [expr.subs(subs_map) for expr in exprs]
        if sum(substituted) < min_press and all(n >= 0 for n in substituted) and all(val.is_integer for val in substituted):
            # print(f"{subs_map} -> {substituted}, sum {sum(substituted)}")
            min_press = sum(substituted)

    return min_press





press_num_1 = 0
press_num_2 = 0
for l in ll:
    import re
    init_state_str = re.search(r'\[(.*?)\]', l).group(1)
    init_state = tuple([1 if c == '#' else 0 for c in init_state_str])
    button_strs = re.findall(r'\((.*?)\)', l)
    buttons = [tuple(map(int, s.split(','))) for s in button_strs]
    target_str = re.search(r'\{(.*?)\}', l).group(1)
    target = list(map(int, target_str.split(',')))

    # print(l)
    # print("Part 1 Init State:", init_state)
    # print("Buttons:", buttons)
    # print("Part 2 Target:", target)
    press_num_1 += min_press_to_off(init_state, buttons)





    mp = solve_solution(button_matrix(buttons, len(target)), target)
    print(mp, l)





    press_num_2 += mp

# 1, 3, 0, 3, 1, 2

    # tc = toggle_combo(len(init_state_str),buttons,[x % 2 for x in target])
    # for c in tc:
    #     print('>', c)
    #     print(apply_combo(len(init_state),buttons,c))


    print()

print(press_num_1)
print(press_num_2)