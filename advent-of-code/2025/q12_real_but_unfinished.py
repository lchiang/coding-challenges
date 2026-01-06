with open('in12.txt') as f:
    ll = f.read().splitlines()



import pulp

def parse_boxes(lines):
    boxes = {}
    current_id = None
    shape = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.endswith(":") and line[:-1].isdigit():
            if current_id is not None:
                boxes[current_id] = shape
            current_id = int(line[:-1])
            shape = []
        elif "x" in line and ":" in line:
            if current_id is not None:
                boxes[current_id] = shape
            return boxes
        else:
            shape.append(line)
    if current_id is not None:
        boxes[current_id] = shape
    return boxes

def parse_region(lines):
    regions = []
    for line in lines:
        if 'x' in line:
            l1 = line.split(':')

            w, h = [int(x) for x in l1[0].split('x')]
            l2 = [int(x) for x in l1[1].split()]
            regions.append((w,h,l2))
    return regions

# Function to rotate shape
def rotate(shape):
    rows, cols = len(shape), len(shape[0])
    return ["".join(shape[rows-1-r][c] for r in range(rows)) for c in range(cols)]

# Generate orientations
def orientations(shape):
    seen = []
    cur = shape
    for _ in range(4):
        if cur not in seen:
            seen.append(cur)
        cur = rotate(cur)
    return seen

# Convert shape to coordinates
def shape_coords(shape):
    coords = []
    for y,row in enumerate(shape):
        for x,ch in enumerate(row):
            if ch == "#":
                coords.append((x,y))
    return coords


def build_model(W, H, counts, box_defs):
    prob = pulp.LpProblem("Packing", pulp.LpMinimize)
    prob += 0  # feasibility
    cell_expr = [[pulp.LpAffineExpression() for _ in range(H)] for _ in range(W)]
    type_expr = [pulp.LpAffineExpression() for _ in counts]
    x_vars = {}
    placements = []
    pid = 0
    for box_id, ascii_shape in box_defs.items():
        for orient_id, shape in enumerate(orientations(ascii_shape)):
            coords = shape_coords(shape)
            if not coords:
                continue
            max_x = max(x for x,y in coords)
            max_y = max(y for x,y in coords)
            for ox in range(W - max_x):
                for oy in range(H - max_y):
                    var = pulp.LpVariable(f"x_{pid}", cat="Binary")
                    x_vars[pid] = var
                    type_expr[box_id] += var
                    for dx, dy in coords:
                        cx = ox + dx
                        cy = oy + dy
                        cell_expr[cx][cy] += var
                    placements.append((box_id, coords, ox, oy))
                    pid += 1

    # Add constraints
    for t, expr in enumerate(type_expr):
        prob += expr == counts[t]
    for cx in range(W):
        for cy in range(H):
            prob += cell_expr[cx][cy] <= 1

    return prob, placements, x_vars


box_shapes = parse_boxes(ll)

box_area = {}
for b, bv in box_shapes.items():
    box_area[b] = sum(s.count('#') for s in bv)

regions = parse_region(ll)
# print(box_shapes)

def print_placement(placement, w, h):
    (box_id, coords, ox, oy) = placement
    for y in range(h):
        l = []
        for x in range(w):
            if (x-ox,y-oy) in coords:
                l.append('#')
            else:
                l.append('.')
        print(''.join(l))


import time

can_fit = 0
for r in regions:
    start = time.perf_counter()

    w, h, requirements = r
    print()
    print(w, h, requirements)
    print(box_shapes)

    min_area_need = sum(box_area[i] * r for i, r in enumerate(requirements))
    if min_area_need > w*h:
        print('min area not meet')
        pass
    elif ((w//3) * (h//3)) > sum(requirements):
        print('ok even if not overlap', (w//3) * (h//3) , sum(requirements))
        can_fit += 1
    else:
        # can_fit += 1
        # problem of input case, answer still correct even if assume all non-obvious case can fit
        # check q12.py

        model, placements, x_vars = build_model(w, h, requirements, box_shapes)
        model.solve(pulp.PULP_CBC_CMD(msg=False))
        print("Status:", pulp.LpStatus[model.status])
        if model.status == pulp.constants.LpStatusOptimal:
            can_fit += 1



    # print(f"Elapsed time: {time.perf_counter() - start:.6f} seconds")

    # for i,var in x_vars.items():
    #     if var.value() == 1:
    #         # print_placement(placements[i], w, h)
    #         print("Placement chosen:", placements[i])

print('answer', can_fit)