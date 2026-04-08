with open('q2_input.txt', 'r') as file:
    grid = [list(line.rstrip('\n')) for line in file]

PADDING = 20
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Add padding left and right
for row in grid:
    row[:] = ['.'] * PADDING + row + ['.'] * PADDING

# Add padding top and bottom
empty_row = ['.'] * (cols + 2 * PADDING)
for _ in range(PADDING):
    grid.insert(0, empty_row[:])
    grid.append(empty_row[:])

# Find start and ALL targets (#)
start = None
targets = []                     # List of all vocal bones
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == '@':
            start = (r, c)
            grid[r][c] = '.'
        elif grid[r][c] == '#':
            targets.append((r, c))
            # keep # as is

if not start:
    print("Error: No @ found")
    exit(1)
if not targets:
    print("Error: No # found")
    exit(1)

directions = [(-1, 0), (-1, 0), (-1, 0), (0, 1), (0, 1), (0, 1), (1, 0), (1, 0), (1, 0), (0, -1), (0, -1), (0, -1)]  # ↑ ↑ ↑ → → → ↓ ↓ ↓ ← ← ←

visited = set([start])
pos = start
steps = 0
dir_idx = 0

max_steps = 10000

def all_targets_surrounded_2(targets, visited, rows, cols, padding):
    """Return True only if ALL vocal bones are fully surrounded.
    Flood fills from the border (outside). If no # is reachable from outside, they are all surrounded."""
    from collections import deque

    if not targets:
        return True

    q = deque()
    seen = set()

    # Start flood fill from all padding border cells
    for r in range(rows):
        for c in [0, cols-1]:                    # left and right edges
            if (r, c) not in visited:
                q.append((r, c))
                seen.add((r, c))
    for c in range(cols):
        for r in [0, rows-1]:                    # top and bottom edges
            if (r, c) not in visited:
                q.append((r, c))
                seen.add((r, c))

    # Flood fill from border
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in seen and
                (nr, nc) not in visited):
                seen.add((nr, nc))
                q.append((nr, nc))

    # Check if ANY target (#) is reachable from the border
    for target in targets:
        if target in seen:
            return False   # at least one # can escape → not all surrounded

    return True   # no # is reachable from outside → all are surrounded

def all_targets_surrounded(targets, visited, rows, cols, padding):
    """Return True only if ALL vocal bones are fully surrounded"""
    from collections import deque

    for target in targets:
        q = deque([target])
        seen = set([target])

        while q:
            r, c = q.popleft()

            # Can reach padding border → can escape
            if r < padding or r >= rows - padding or c < padding or c >= cols - padding:
                return False

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in seen and (nr, nc) not in visited):
                    seen.add((nr, nc))
                    q.append((nr, nc))
    return True

def fill_surrounded_regions_2(visited, padding):
    """Reverse flood fill: mark everything reachable from border as safe.
       Then add all unreachable empty cells to visited (surrounded)."""
    from collections import deque
    rows = len(grid)
    cols = len(grid[0])

    # Start flood fill from all border cells (the "outside")
    q = deque()
    seen = set()

    # Add all cells on the padding border to the queue
    for r in range(rows):
        for c in [0, cols-1]:                    # left and right border
            if (r, c) not in visited:
                q.append((r, c))
                seen.add((r, c))
    for c in range(cols):
        for r in [0, rows-1]:                    # top and bottom border
            if (r, c) not in visited:
                q.append((r, c))
                seen.add((r, c))

    # Flood fill from border
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited and
                (nr, nc) not in seen and
                (nr, nc) not in targets):        # don't go through #
                seen.add((nr, nc))
                q.append((nr, nc))

    # Now, any empty cell NOT in 'seen' is surrounded → add to visited
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited and (r, c) not in seen and (r, c) not in targets:
                visited.add((r, c))

def fill_surrounded_regions(visited, new_pos, padding):
    # TODO Debugging here when steps = 33, new_pos = (4,7), (5,7) should paint
    from collections import deque
    rows = len(grid)
    cols = len(grid[0])


    candidates = [new_pos]
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = new_pos[0] + dr, new_pos[1] + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and (nr, nc) not in targets and (nr, nc) != new_pos:
            candidates.append((nr, nc))
    # if new_pos == (4,7):
    #     print('candidates', candidates)

    for start_cell in candidates:

        if start_cell in visited:
            continue
        # if new_pos == (4,7): print('start_cell-start',  start_cell)

        q = deque([start_cell])
        seen = set([start_cell])
        can_escape = False

        while q and not can_escape:
            x, y = q.popleft()

            # if new_pos == (4,7) and start_cell == (5,7):
            #     print(x,y, x < 0 , x >= rows - 0 , y < 0 , y >= cols - 0, '|', x < padding or x >= rows - padding or y < padding or y >= cols - padding)
            if x < 0 or x >= rows -1 or y < 0 or y >= cols - 1 :
                # if new_pos == (4,7) and start_cell == (5,7):
                #     print('can escape', x,y, x < padding , x >= rows - padding , y < padding , y >= cols - padding)
                can_escape = True
                break

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = x + dr, y + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and (nr, nc) not in targets and (nr, nc) != new_pos and (nr, nc) not in seen):
                    seen.add((nr, nc))
                    q.append((nr, nc))
                    if new_pos == (4,7) and start_cell == (5,7):
                        print('seen', seen, can_escape, 'q', q)

        # if new_pos == (4,7):
        #     print('start_cell-end',  start_cell)
        #     print(q,seen,can_escape)

        if not can_escape and seen:
            visited.update(seen)
            # if new_pos == (4,7):
            #     print(seen)


def print_map(grid, visited, pos, targets, steps):
    """Print map with multiple #"""
    print(f"\nStep: {steps}")
    for r in range(len(grid)):
        line = []
        for c in range(len(grid[r])):
            if (r, c) == pos: line.append("@")
            elif (r, c) in targets: line.append("#")
            elif (r, c) in visited: line.append("+")
            else: line.append(".")
        print("".join(line))
    print("-" * len(grid[0]))


import time

start = time.perf_counter()

# ====================== MAIN SIMULATION ======================
while steps < max_steps:
    moved = False
    for _ in range(len(directions)):                                   # cycle through ↑ → ↓ ←
        dr, dc = directions[dir_idx]

        nr = pos[0] + dr
        nc = pos[1] + dc

        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and
            (nr, nc) not in visited and (nr, nc) not in targets):

            visited.add((nr, nc))
            pos = (nr, nc)
            steps += 1
            moved = True

            # fill_surrounded_regions(visited, pos, PADDING)
            fill_surrounded_regions_2(visited, PADDING)
            # if steps % 100 == 0:
            #     print_map(grid, visited, pos, targets, steps)

            if steps > 2300 or steps % 100 == 0:
                end = time.perf_counter()

                print(f"Execution time: {end - start:.6f} seconds")
                print(f"Step {steps, pos} | Surrounded: {all_targets_surrounded(targets, visited, len(grid), len(grid[0]), PADDING)}")
                print(f"Step {steps, pos} | Surrounded2: {all_targets_surrounded_2(targets, visited, rows, cols, PADDING)}")
                print_map(grid, visited, pos, targets, steps)

            if steps > 2300 and all_targets_surrounded(targets, visited, rows, cols, PADDING):
            # if all_targets_surrounded(targets, visited, len(grid), len(grid[0]), PADDING):
                print_map(grid, visited, pos, targets, steps)
                print(f"\nAll vocal bones are surrounded after {steps} steps!")
                exit(0)





        dir_idx = (dir_idx + 1) % len(directions)


    if not moved:
        print("Stream got stuck")
        print_map(grid, visited, pos, targets, steps)
        break

else:
    print("Max steps reached - not all bones surrounded")