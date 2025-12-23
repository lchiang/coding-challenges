with open('in8.txt') as f:
    ll = f.read().splitlines()

import math
from collections import namedtuple
P = namedtuple('P', ['x', 'y', 'z'])

ps = [P(*map(int, line.split(','))) for line in ll]

cdict = {}
for i in range(len(ps)):
    cdict[ps[i]] = i

distances = []
for i in range(len(ps)):
    for j in range(i + 1, len(ps)):
        p1, p2 = ps[i], ps[j]
        dist = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)
        distances.append(((p1, p2), dist))
distances.sort(key=lambda x: x[1])

def merge_circuit(p1, p2):
    global cdict
    new_ciruit = max(cdict.values()) + 1
    keys_to_update = [k for k, v in cdict.items() if v in (cdict[p1], cdict[p2])]
    for k in keys_to_update:
        cdict[k] = new_ciruit

def three_largest(l):
    from collections import Counter
    counts = Counter(l)
    l1 = sorted(list(counts.values()), reverse=True)[:3]
    return math.prod(l1)

connect = 0
for (p1, p2), d in distances:
    merge_circuit(p1, p2)

    # For part 1
    # connect += 1
    # if connect == 10:
    #     from collections import Counter
    #     counts = Counter(list(cdict.values()))
    #     l1 = sorted(list(counts.values()), reverse=True)[:3]
    #     print('Part 1: ', math.prod(l1))
    #     break

    circuit_num = len(set(cdict.values()))
    print(circuit_num)
    if circuit_num == 1:
        print('Part 1: ', p1.x * p2.x)
        break
