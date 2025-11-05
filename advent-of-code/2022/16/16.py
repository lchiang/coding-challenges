ll = open('./2022/16/test.txt').read().splitlines()
#ll = open('./2022/16/input.txt').read().splitlines()

import re


class Valve:
    def __init__(self, name, flow, to):
        self.name = name
        self.flow = flow
        self.to = to

    def print(self):
        print(self.name, self.flow, self.to)



valves = {}
for l in ll:
    result = re.search(r"Valve ([A-Z][A-Z]) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (([A-Z][A-Z])(,\s[A-Z][A-Z])*)", l)
    #print(result.group(1), result.group(2), result.group(3).split())
    v = Valve(result.group(1), int(result.group(2)), result.group(3).split())
    valves[v.name] = v


current_node = 'AA'

valves[current_node].print()

