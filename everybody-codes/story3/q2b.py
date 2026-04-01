with open('q2_input.txt', 'r') as file:
    grid = [list(line.rstrip('\n')) for line in file]

PADDING = 50
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Add padding left and right
for row in grid:
    row[:] = (['.'] * PADDING) + row + (['.'] * PADDING)

# Add padding top and bottom
empty_row = ['.'] * (cols + 2 * PADDING)
for _ in range(PADDING):
    grid.insert(0, empty_row[:])
    grid.append(empty_row[:])

# Update start and target positions because of padding
start = None
target = None
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == '@':
            start = (r, c)
            grid[r][c] = '.'          # clear original @ (we use visited instead)
        elif grid[r][c] == '#':
            target = (r, c)
            # keep # as is


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # ↑ → ↓ ←

visited = set([start])          # cells occupied by the sound wave
pos = start
steps = 0
dir_idx = 0

# visited.add(target)

max_steps = 5000


def is_surrounded(target, visited, rows, cols, padding):
    """Return True if the vocal bone # is fully surrounded (no path to escape)"""
    if target in visited:
        return True

    from collections import deque
    q = deque([target])
    seen = set([target])

    while q:
        r, c = q.popleft()

        # Can escape → not surrounded (near the padded border means connected to infinity)
        if r < padding or r >= rows - padding or c < padding or c >= cols - padding:
            return False

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in seen and
                (nr, nc) not in visited):
                seen.add((nr, nc))
                q.append((nr, nc))
    return True


def fill_surrounded_regions(visited, new_pos, padding):
    """Fast version: only check areas around the newly added cell"""
    from collections import deque
    rows = len(grid)
    cols = len(grid[0])

    # Check the 4 neighbors of the new position (and the new cell itself)
    candidates = [new_pos]
    for dr, dc in directions:
        nr, nc = new_pos[0] + dr, new_pos[1] + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and (nr, nc) != target:
            candidates.append((nr, nc))

    for start_cell in candidates:
        if start_cell in visited or start_cell == target:
            continue

        q = deque([start_cell])
        seen = set([start_cell])
        can_escape = False

        while q and not can_escape:
            x, y = q.popleft()

            if x < padding or x >= rows - padding or y < padding or y >= cols - padding:
                can_escape = True
                break

            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and (nr, nc) != target and (nr, nc) not in seen):
                    seen.add((nr, nc))
                    q.append((nr, nc))

        if not can_escape and seen:
            visited.update(seen)

def print_map(grid, visited, pos, target, steps, next_dir_idx=None):
    """Print the current state of the grid with sound wave visualization"""
    print(f"\nStep: {steps}   ", end="")
    if next_dir_idx is not None:
        dir_symbols = ['↑', '→', '↓', '←']
        seq = ['↑', '→', '↓', '←']
        next_str = ''.join(['[' + d + ']' if i == next_dir_idx else d for i, d in enumerate(seq)])
        print(f"Next: {next_str}")
    else:
        print()

    for r in range(len(grid)):
        line = ""
        for c in range(len(grid[r])):
            cell = grid[r][c]

            if (r, c) == pos:
                line += "@"          # current head of the wave
            elif (r, c) == target:
                line += "#"          # vocal bone
            elif (r, c) in visited:
                line += "+"          # sound wave
            elif cell == '.' or cell == ' ':
                line += "."          # empty space
            else:
                line += cell         # keep original characters if any

        print(line)
    print("-" * len(grid[0]) if grid else "")


while steps < max_steps:

    moved = False
    for _ in range(4):
        dr, dc = directions[dir_idx]
        nr = pos[0] + dr
        nc = pos[1] + dc



        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and (nr, nc) != target):

            visited.add((nr, nc))
            pos = (nr, nc)
            steps += 1
            moved = True
            print(steps, pos, dir_idx, 'move')

            fill_surrounded_regions(visited, pos, PADDING)

            if steps > 3750:

                print_map(grid, visited, pos, target, steps)


            if is_surrounded(target, visited, len(grid), len(grid[0]), PADDING):
                # print_map(grid, visited, pos, target, steps)
                # print(target, visited)
                print(f"\nThe vocal bone is surrounded after {steps} steps!")
                exit(0)

        dir_idx = (dir_idx + 1) % 4

    if not moved:
        print("Stream got stuck")
        break


else:
    print("Target not surrounded within limit")