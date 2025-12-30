buttons = [(1,2,3,6,8,9), (1,3,4,9), (0,8,9), (1,2,3,5,8), (6,8), (0,4,7), (0,1,4,5), (2,5,6,9), (3,4,5,7,8,9), (0,2,4,5,6,7,8,9), (1,2,5,7,8), (0,2,7,8,9), (3,4,5,6,9)]
target = [189,44,198,50,48,52,42,188,209,208]
l = "[#.###.###.] (0,2,6) (1,4,5,9) (2,3,5,8,9) (0,3,4,5,6,8,9) (3,7) (0,1,4,5,8,9) (1) (0,2,3,4,5,6,7,8,9) (0,1,3,6,7,8,9) (0,2,3,4,6,7,8,9) (2,5) (0,2,6,7,8) (0,3,5,7,9) {87,43,219,205,58,207,66,68,236,220}"
# l = "[.#.#..#.#.] (1,2,3,6,8,9) (1,3,4,9) (0,8,9) (1,2,3,5,8) (6,8) (0,4,7) (0,1,4,5) (2,5,6,9) (3,4,5,7,8,9) (0,2,4,5,6,7,8,9) (1,2,5,7,8) (0,2,7,8,9) (3,4,5,6,9) {189,44,198,50,48,52,42,188,209,208}"
# l = "[##..##..] (1,2,3,4,5,7) (2,3,4,5,6) (0,1,2,4,6,7) (0,1,4,5,7) (2,4,5,6) (1,4,5) (0,1,2,3,4,6,7) (1,5) (0,6) (0,2,3,4,6) {222,68,51,38,73,55,214,39}"
# l = "[...##..#.] (1,4,5) (4,5,7) (0,2,4,5,6,8) (0,1,3,4,5,6,7,8) (0,2,3,7,8) (0,2,4,5,6,7,8) (1,3) (0,2,4,6,8) (3,5,7) {45,27,30,30,50,50,34,44,45}"
# l = "[##.#...##.] (1,3,4,6,7,9) (0,1,2,6,7,9) (8,9) (1,3,4,5,6,8) (3,8,9) (0,1,3,4,5,7,8,9) (7,8) (2,3,7,8,9) (0,6) (0,1,2,3,4,5) (0,1,2,3,6,7,8) (2,6) (3,5) {58,248,75,268,220,229,251,62,263,59}"
# l = "[##.#..#.] (0,1,3,4,6) (0,1,2,5,6,7) (3,4,5,6) (0,1,2,3,6) (0,1,2,3,4,5) (3,4,6,7) (2,3,5,7) (0,1,2,4,5) (4,6) (0,1,5,7) {43,43,57,56,49,52,44,33}"
# l = "[.##.#.#...] (1,2,4,6) (0,1,2,4,5,8,9) (0,2,3,4,6,7) (5,6,9) (8,9) (0,1,2,4,7) (0,1,2,3,4,7,8,9) (0,1,2,3,4,5,6,7) (2,3,4,5,6,7,8) (4,5,7,9) (0,1,2,3,4,8,9) (0,2,3,4,5,8,9) (0,1,3,4) {244,248,266,69,299,241,47,67,248,256}"
# l = "[.###.#..##] (4,7) (1,2,5,9) (0,1,2,5,8,9) (2,3,4,6,7) (3,8,9) (0,1,3,4,5,6,8,9) (2,4,5,8) (0,1,3,4,5,6,9) (0,1,3,7,8) (0,3,4,7,8) (0,2,4,6,9) (1,5,6) (0,2,3,6) {152,40,48,148,149,35,33,143,148,24}"

import re
button_strs = re.findall(r'\((.*?)\)', l)
buttons = [tuple(map(int, s.split(','))) for s in button_strs]
target_str = re.search(r'\{(.*?)\}', l).group(1)
target = list(map(int, target_str.split(',')))

print(buttons)
print(target)
from itertools import product
from sympy import Matrix, linsolve, symbols, simplify, lambdify
from numpy import isnan, isinf

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
    sol = linsolve((button_M,Matrix(target, rational=False)), c)

    exprs = list(sol)[0]
    free_vars = list(set().union(*[expr.free_symbols for expr in list(sol)[0]]))

    print(exprs, free_vars)

    min_press = sum(target)
    ranges = [range(0, max(target)) for _ in free_vars]  # 0..10 for each variable
    for values in product(*ranges):
        subs_map = dict(zip(free_vars, values))
        substituted = [expr.subs(subs_map) for expr in exprs]
        if sum(substituted) < min_press and all(n >= 0 for n in substituted) and all(val.is_integer for val in substituted):
            print(f"{subs_map} -> {substituted}, sum {sum(substituted)}")
            min_press = sum(substituted)

    return min_press

print(button_matrix(buttons, len(target)))

mp = solve_solution(button_matrix(buttons, len(target)), target)
print(mp)

