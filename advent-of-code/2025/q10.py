with open('in10_test.txt') as f:
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

    print(l)
    # print("Part 1 Init State:", init_state)
    # print("Buttons:", buttons)
    # print("Part 2 Target:", target)
    press_num_1 += min_press_to_off(init_state, buttons)


    # print("Target Pattern", [x % 2 for x in target])
    solutions = solve(target, buttons, max_val=5)

    if solutions == None:
        print(l)
    press_num_2 += solutions

# 1, 3, 0, 3, 1, 2

    # tc = toggle_combo(len(init_state_str),buttons,[x % 2 for x in target])
    # for c in tc:
    #     print('>', c)
    #     print(apply_combo(len(init_state),buttons,c))


    print()

print(press_num_1)
print(press_num_2)