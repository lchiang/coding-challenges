import time

st = time.perf_counter()

ed = time.perf_counter()


print(f"Elapsed time: {ed-st:.4f} seconds")


# import numpy as np

# # Matrix a
# a1 = np.array([
#     [0, 0, 0, 1],
#     [0, 1, 0, 1],
#     [0, 0, 1, 0],
#     [0, 0, 1, 1],
#     [1, 0, 1, 0],
#     [1, 1, 0, 0]
# ], dtype=int)


# a2 = np.array([
#     [0, 0, 0, 0, 1, 1],
#     [0, 1, 0, 0, 0, 1],
#     [0, 0, 1, 1, 1, 0],
#     [1, 1, 0, 1, 0, 0]
# ],dtype=int)

# # Coefficients x
# # (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# # One way to do this is by pressing (3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice.

# x, residuals, rank, singular_values = np.linalg.lstsq(a2, [3,5,4,7], rcond=None)

# print("Solution x:", x, residuals, rank, singular_values)

# # print(np.linalg.solve(a2, [3,5,4,7]))

# x = np.array([1, 3, 0, 3, 1, 2])
# x = np.array([1, 3, 0, 3, 1, 2])

# print("Result:", np.dot(x, a1))
# print("Result:", np.dot(a2, x))




from sympy import Matrix, symbols, linsolve

# Initial and target
init    = [0,0,0,0]
target  = [3,5,4,7]

# Button effect vectors
vectors = [
    [0,0,0,1],  # v0
    [0,1,0,1],  # v1
    [0,0,1,0],  # v2
    [0,0,1,1],  # v3
    [1,0,1,0],  # v4
    [1,1,0,0]   # v5
]

# Number of variables
n = len(vectors)
c = symbols(f'c0:{n}')   # (c0, c1, ..., c5)

# Build matrix A and rhs b
A = Matrix([[v[i] for v in vectors] for i in range(len(init))])
b = Matrix([t - i for t,i in zip(target, init)])

# Solve system A * c = b
solutions = linsolve((A, b), c)
print("General solution set:", solutions)

valid = []
for sol in solutions:
    free_syms = list(sol.free_symbols)
    if not free_syms:
        # direct solution
        if all(val.is_integer and val > 0 for val in sol):
            valid.append(sol)
    else:
        # try small ranges for free parameters
        for t0 in range(0, 10):   # adjust range as needed
            candidate = [val.subs(free_syms[0], t0) for val in sol]
            print(candidate)
            for v in candidate:
                print(v)
            if all(v.is_integer and v > 0 for v in candidate):
                valid.append(candidate)

print("Positive integer solutions:", valid)


from sympy import Matrix, linsolve

A = Matrix([
    [0,0,0,0,1,1],   # coefficients for eq1: c4+c5
    [0,1,0,0,0,1],   # eq2: c1+c5
    [0,0,1,1,1,0],   # eq3: c2+c3+c4
    [1,1,0,1,0,0]    # eq4: c0+c1+c3
])
b = Matrix([3,5,4,7])


sol = linsolve((A,b), c)
print(sol, type(sol))

# Check if candidate is in solution set
candidate_vec = Matrix([1, 3, 0, 3, 1, 2])
print(A * candidate_vec == b)  # True if valid


# # Coefficients x
# # (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# # One way to do this is by pressing (3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice.

from sympy import symbols, FiniteSet


# Extract the tuple inside the FiniteSet
exprs = list(sol)[0]


# Find all free symbols (variables) automatically
free_vars = list(set().union(*[expr.free_symbols for expr in exprs]))
print("Free variables:", free_vars, exprs,sol)

# Enumerate values for all free variables in 0..10
results = []
from itertools import product

ranges = [range(0, 11) for _ in free_vars]  # 0..10 for each variable
for values in product(*ranges):
    subs_map = dict(zip(free_vars, values))
    substituted = [expr.subs(subs_map) for expr in exprs]
    if all(n >= 0 for n in substituted):
        results.append((subs_map, substituted))

# Print results
for subs_map, candidate in results:  # show first 10
    print(f"{subs_map} -> {candidate}, sum {sum(candidate)}")
print(A.row)

print((190/19).is_integer())
print((191/19).is_integer())




from sympy import symbols
from itertools import product

def minimize_positive_solution(exprs, search_range=20):
    free_vars = list(set().union(*[e.free_symbols for e in exprs]))
    print("Free variables:", free_vars)
    best = None
    ranges = [range(0, search_range+1) for _ in free_vars]
    for values in product(*ranges):
        subs_map = dict(zip(free_vars, values))
        substituted = [e.subs(subs_map) for e in exprs]

        if all(val.is_integer and val > 0 for val in substituted):
            total = sum(substituted)
            if best is None or total < best[2]:
                best = (subs_map, substituted, total)

    return best



