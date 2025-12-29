from itertools import product

target  =   [51, 38, 12, 25, 9, 52, 42, 42, 58, 49]
buttons = [(0, 1, 5, 6, 7, 8, 9), (4, 5), (1, 2, 3, 5, 6), (0, 3), (8, 9), (0, 3, 5, 6, 7, 8, 9), (0, 1, 4, 6, 7, 9), (1, 2), (5, 8)]
# target = [3, 5, 4, 7]
# buttons = [(3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)]


def apply_combo(length, buttons, combo):
    result = [0] * length
    for count, btn in zip(combo, buttons):
        for idx in btn:
            result[idx] += count
    return result

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



def solve(target, buttons, max_val=10):
    n = len(buttons)
    solutions = []
    toggle_c = toggle_combo(len(target),buttons,[x % 2 for x in target])

    combosd = []
    for c in product(range(0, max_val+1), repeat=n):
        if tuple([x % 2 for x in c]) in toggle_c:
            combosd.append(c)
    print('123', len(combosd))
    combosd.sort(key=lambda c: (sum(c), c))

    for combo in combosd:  # positive integers only
        if apply_combo(len(target), buttons, combo) == target:
            solutions.append(combo)
            return sum(combo)

# print('123123')
# good_combo = [1, 3, 0, 3, 1, 2]
# bad_combo = [1, 3, 0, 3, 1, 1]

# Run solver
solutions = solve(target, buttons, max_val=5)

print("min_press:", solutions)

