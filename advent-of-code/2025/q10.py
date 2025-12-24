with open('in10_test.txt') as f:
    ll = f.read().splitlines()

def press(state, button, presses):
    s = list(state)
    for i in range(len(presses)):
        if presses[i] == 1: # press i-th button
            for b in button[i]:
                s[b] ^= 1   # XOR flip
    return s

def min_press_to_off(lights, buttons):
    from itertools import product
    combos = list(product([0,1], repeat=len(buttons)))
    combos.sort(key=lambda c: (sum(c), c))
    for combo in combos:
        # print(combo, press(lights, buttons, combo))
        ls = press(lights, buttons, combo)
        if all(x == 0 for x in ls):
            return sum(combo)

press_num = 0
for l in ll:
    import re
    light_str = re.search(r'\[(.*?)\]', l).group(1)
    lights = tuple([1 if c == '#' else 0 for c in light_str])
    button_strs = re.findall(r'\((.*?)\)', l)
    buttons = [tuple(map(int, s.split(','))) for s in button_strs]
    int_list_str = re.search(r'\{(.*?)\}', l).group(1)
    int_list = list(map(int, int_list_str.split(',')))

    print(l)
    print("Lights:", lights)
    print("Buttons:", buttons)
    print("Int list:", int_list)
    press_num += min_press_to_off(lights, buttons)

print(press_num)