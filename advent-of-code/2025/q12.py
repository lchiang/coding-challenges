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
                boxes[current_id] = [shape]
            current_id = int(line[:-1])
            shape = []
        elif "x" in line and ":" in line:
            if current_id is not None:
                boxes[current_id] = [shape]
            return boxes
        else:
            shape.append(line)
    if current_id is not None:
        boxes[current_id] = [shape]
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

# Suppose box_defs = {0: [...], 1: [...], ...} with ASCII shapes

def build_model(W, H, counts, box_defs):
    model = pulp.LpProblem("Packing", pulp.LpMaximize)
    placements = []
    x_vars = {}

    # Generate placements for all box types
    for box_id, shapes in box_defs.items():
        for shape in shapes:
            for orient in orientations(shape):
                coords = shape_coords(orient)
                max_x = max(x for x,y in coords)
                max_y = max(y for x,y in coords)
                for ox in range(W - max_x):
                    for oy in range(H - max_y):
                        placements.append((box_id, coords, ox, oy))

    # Decision variables
    for i,pl in enumerate(placements):
        x_vars[i] = pulp.LpVariable(f"x_{i}", cat="Binary")

    # Cell constraints
    for cx in range(W):
        for cy in range(H):
            model += pulp.lpSum(
                x_vars[i]
                for i,(box_id,coords,ox,oy) in enumerate(placements)
                if (cx-ox, cy-oy) in coords
            ) <= 1

    # Box count constraints
    for box_id, count in enumerate(counts):
        model += pulp.lpSum(
            x_vars[i]
            for i,(bid,coords,ox,oy) in enumerate(placements)
            if bid == box_id
        ) == count

    # Objective: maximize placed boxes
    model += pulp.lpSum(x_vars.values())
    return model, placements, x_vars


box_shapes = parse_boxes(ll)
regions = parse_region(ll)
# print(box_shapes)

for r in regions:
    w, h, requirements = r
    # print()
    # print(w, h, requirements)
    # print(box_shapes)


    model, placements, x_vars = build_model(w, h, requirements, box_shapes)
    model.solve(pulp.PULP_CBC_CMD(msg=False))
    print("Status:", pulp.LpStatus[model.status])

    # # Build all placements
    # placements = []
    # for box_id, shapes in box_shapes.items():
    #     for shape in shapes:
    #         for orient in orientations(shape):
    #             coords = shape_coords(orient)
    #             max_x = max(x for x,y in coords)
    #             max_y = max(y for x,y in coords)
    #             for ox in range(w - max_x):
    #                 for oy in range(h - max_y):
    #                     placements.append((box_id, coords, ox, oy))

    # # PuLP model
    # model = pulp.LpProblem("Packing", pulp.LpMaximize)

    # # Decision variables
    # x_vars = {}
    # for i,(box_id,coords,ox,oy) in enumerate(placements):
    #     x_vars[i] = pulp.LpVariable(f"x_{i}", cat="Binary")

    # # Constraint: each cell covered at most once
    # for cx in range(w):
    #     for cy in range(h):
    #         model += pulp.lpSum(
    #             x_vars[i]
    #             for i,(box_id,coords,ox,oy) in enumerate(placements)
    #             if (cx-ox, cy-oy) in coords
    #         ) <= 1

    # # Constraint: place exactly 2 copies of box 4
    # model += pulp.lpSum(
    #     x_vars[i]
    #     for i,(box_id,coords,ox,oy) in enumerate(placements)
    #     if box_id == 4
    # ) == 2

    # # Objective: just maximize number of placed boxes (feasibility)
    # model += pulp.lpSum(x_vars.values())

    # # Solve
    # model.solve(pulp.PULP_CBC_CMD(msg=False))

    # print("Status:", pulp.LpStatus[model.status])
    # for i,var in x_vars.items():
    #     if var.value() == 1:
    #         print("Placement chosen:", placements[i])
