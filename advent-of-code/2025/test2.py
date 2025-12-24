from itertools import product

target  = [3,5,4,7]
buttons = [(3,), (1,3), (2,), (2,3), (0,2), (0,1)]

def apply_combo(length, buttons, combo):
    result = [0] * length
    for count, btn in zip(combo, buttons):
        for idx in btn:
            result[idx] += count
    return result

def solve(target, buttons, max_val=10):
    n = len(buttons)
    solutions = []
    combos = list(product(range(0, max_val+1), repeat=n))
    combos.sort(key=lambda c: (sum(c), c))
    for combo in combos:  # positive integers only
        if apply_combo(len(target), buttons, combo) == target:
            solutions.append(combo)
            break
    return solutions

# Run solver
solutions = solve(target, buttons, max_val=10)

print(apply_combo(4, buttons,(1,3,0,3,1,2)))


print("Possible solutions:")
for sol in solutions:
    print(sol, "Total presses:", sum(sol))
