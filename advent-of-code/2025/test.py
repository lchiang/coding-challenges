import time

st = time.perf_counter()

ed = time.perf_counter()


print(f"Elapsed time: {ed-st:.4f} seconds")


import numpy as np

# Matrix a
a1 = np.array([
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0]
], dtype=int)


a2 = np.array([
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 0]
],dtype=int)

# Coefficients x
# (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# One way to do this is by pressing (3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice.

x, residuals, rank, singular_values = np.linalg.lstsq(a2, [3,5,4,7], rcond=None)

print("Solution x:", x, residuals, rank, singular_values)

print(np.linalg.solve(a2, [3,5,4,7]))

x = np.array([1, 3, 0, 3, 1, 2])
x = np.array([1, 3, 0, 3, 1, 2])

print("Result:", np.dot(x, a1))
print("Result:", np.dot(a2, x))
