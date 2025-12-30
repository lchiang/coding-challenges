with open('in11_test2.txt') as f:
    ll = f.read().splitlines()



class DAG:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest):
        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []
        self.graph[src].append(dest)

    def build_from_lines(self, lines):
        for line in lines:
            if ":" not in line:
                continue
            src, dests = line.split(":")
            src = src.strip()
            for dest in dests.strip().split():
                self.add_edge(src, dest)

    def pretty_print(self):
        for node, neighbors in self.graph.items():
            print(f"{node} -> {', '.join(neighbors)}")

def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:  # avoid cycles
            new_paths = find_all_paths(graph, neighbor, end, path)
            for p in new_paths:
                print(p)
                paths.append(p)

    return paths



dag = DAG()
dag.build_from_lines(ll)

print("Graph structure:")
dag.pretty_print()

# print("\nAll paths from aaa to out:")
# paths = find_all_paths(dag.graph, "svr", "out")
# for p in paths:
#     # if 'dac' in p and 'fft' in p:
#         print(" -> ".join(p))

# print('part 1: ', len(paths))


# svr,aaa,fft,ccc,eee,dac,fff,ggg,out
# svr,aaa,fft,ccc,eee,dac,fff,hhh,out
#
# svr,aaa,fft,ccc,ddd,hub,fff,ggg,out
# svr,aaa,fft,ccc,ddd,hub,fff,hhh,out
# svr,bbb,tty,ccc,ddd,hub,fff,ggg,out
# svr,bbb,tty,ccc,ddd,hub,fff,hhh,out
# svr,bbb,tty,ccc,eee,dac,fff,ggg,out
# svr,bbb,tty,ccc,eee,dac,fff,hhh,out

print(1)
paths = find_all_paths(dag.graph, "svr", "dac")
for p in paths:
    # if 'dac' in p and 'fft' in p:
        print(" -> ".join(p))
print(2)
paths = find_all_paths(dag.graph, "fft", "dac")
for p in paths:
    # if 'dac' in p and 'fft' in p:
        print(" -> ".join(p))
print(3)
paths = find_all_paths(dag.graph, "dac", "out")
for p in paths:
    # if 'dac' in p and 'fft' in p:
        print(" -> ".join(p))