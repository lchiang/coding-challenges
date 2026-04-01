with open('q2_input.txt', 'r') as file:
    grid = [line.rstrip('\n') for line in file]

# Find starting position @ and target #
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

start = None
target = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            start = (r, c)
        elif grid[r][c] == '#':
            target = (r, c)

if not start or not target:
    print("Error: @ or # not found")
    exit(1)

# Directions: 0=↑, 1=→, 2=↓, 3=←
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = set([start])
pos = start
steps = 0
dir_idx = 0  # start trying ↑ first

max_steps = 1000000  # safety limit

while steps < max_steps:
    moved = False
    for _ in range(4):  # try next directions in cyclic order
        dr, dc = directions[dir_idx]
        nr = pos[0] + dr
        nc = pos[1] + dc

        # print(pos, dir_idx)
        if (0 <= nr < rows and 0 <= nc < cols and
            (nr, nc) not in visited):
            # valid empty cell → move there
            visited.add((nr, nc))
            pos = (nr, nc)
            steps += 1
            moved = True
            print(steps, pos, dir_idx, 'move')

            if (nr, nc) == target:
                print(steps)
                exit(0)  # found, output the answer

            # break  # successfully moved, continue from next step

        # try next direction in sequence
        dir_idx = (dir_idx + 1) % 4

    if not moved:
        # cannot move anywhere (should not happen in valid input)
        print("Stream got stuck")
        break

# If we reach here, target not found within limit
print("Target not reached")


# Your answer length is: correct
# The first character of your answer is: incorrect
