with open('in10.txt') as f:
    ll = f.read().splitlines()

from itertools import product
from sympy import Matrix, linsolve, symbols

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
    min_press = sum(target)
    ranges = [range(0, max(target)) for _ in free_vars]
    for values in product(*ranges):
        subs_map = dict(zip(free_vars, values))
        substituted = [expr.subs(subs_map) for expr in exprs]
        if sum(substituted) < min_press and all(n >= 0 for n in substituted) and all(val.is_integer for val in substituted):
            # print(f"{subs_map} -> {substituted}, sum {sum(substituted)}")
            min_press = sum(substituted)
    return min_press

# vibe-coded function
import pulp
def solve_solution3(button_M: Matrix, target: list):
    num_lights, num_buttons = button_M.shape
    A = button_M.tolist()
    prob = pulp.LpProblem("min_sum_non_negative_integers", pulp.LpMinimize)
    c = [pulp.LpVariable(f"c{j}", lowBound=0, cat='Integer') for j in range(num_buttons)]
    prob += pulp.lpSum(c)
    for i in range(num_lights):
        prob += pulp.lpSum(A[i][j] * c[j] for j in range(num_buttons)) == target[i]
    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
    if status == pulp.LpStatusOptimal:
        min_sum = int(pulp.value(prob.objective))
        # solution = [int(pulp.value(var)) for var in c]
        # print(f"Solution: {solution}, sum {min_sum}")
        return min_sum
    else:
        print("No optimal solution found")
        return None

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

    press_num_1 += min_press_to_off(init_state, buttons)
    press_num_2 += solve_solution3(button_matrix(buttons, len(target)), target)

print()
print('Part 1: ',press_num_1)
print('Part 2: ',press_num_2)
