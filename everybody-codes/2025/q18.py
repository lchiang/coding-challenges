f = open('in18c_test.txt')
f = open('in18c.txt')
ll = f.read().splitlines()

class Branch:
    def __init__(self, thickness, target=None):
        self.thickness = thickness
        self.target = target

    def __repr__(self):
        return f"Branch(thickness={self.thickness}, target=Plant {self.target.id if self.target else 'None'})"

class Plant:
    def __init__(self, id, thickness):
        self.id = id
        self.thickness = thickness
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def __repr__(self):
        return f"Plant(id={self.id}, thickness={self.thickness}, branches={self.branches})"

    def energy(self, c=None):
        if len(self.branches) == 1: #free branches
            return c[self.id]
        else:
            e = 0
            for branch in self.branches:
                e += branch.thickness * branch.target.energy(c)
            return 0 if e < self.thickness else e

plants = {}
test_cases = []

def parse_test_case(s):
    nums = list(map(int, s.split()))
    b = {}
    for i, val in enumerate(nums, start=1):
        b[i] = val
    return b

for l in ll:
    l = l.strip()
    if not l:
        continue
    if l.startswith("Plant"):
        parts = l.replace(":", "").split()
        pid = int(parts[1])
        thickness = int(parts[-1])
        plants[pid] = Plant(pid, thickness)
    elif l.startswith("- free branch"):
        thickness = int(l.split()[-1])
        plants[pid].add_branch(Branch(thickness))
    elif l.startswith("- branch to Plant"):
        parts = l.split()
        target_id = int(parts[4])
        thickness = int(parts[-1])
        if target_id in plants:
            plants[pid].add_branch(Branch(thickness, target=plants[target_id]))
    else:
        test_cases.append(l)

def plants_energy(s):
    tc = parse_test_case(s)
    for p in plants.values():
        last_energy = p.energy(tc)
    return last_energy

# max_energy = plants_energy("1 0 1 1")
max_energy = plants_energy("0 0 1 0 1 0 1 0 0 0 0 1 1 1 1 1 0 0 0 1 0 0 0 0 0 1 0 1 0 0 1 0 1 0 0 1 1 0 0 0 0 0 0 0 1 1 0 0 1 1 1 0 0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 1 1 1 1 1 0 0")

diff_energy = 0
for tc in test_cases:
    e = plants_energy(tc)
    if e:
        diff_energy += max_energy - e

print('Part 3:', diff_energy)