ll = open('./2022/07/test.txt').read().splitlines()
#ll = open('./2022/07/input.txt').read().splitlines()

class Node:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent
        self.is_file = size>0

    def add_dir(self, dir_name):
        self.children.append(Node(dir_name, 0, self))

    def add_file(self, file_name, size):
        self.children.append(Node(file_name, size, self))

    def get(self, dir_name):
        for c in self.children:
            if (c.name == dir_name):
                return c

    def print_filesystem(self):
        if (self.size == 0):
            print('=',self.name)
            for c in self.children:
                c.print_filesystem()
        else:
            print('==',self.name,self.size)

    def size_recur(self):
        if (self.is_file):
            return self.size
        else:
            c_size = 0
            for c in self.children:
                c_size += c.size_recur()
            return c_size

fs = Node('/', 0, None)
wd = fs
for l in ll:
    if (l.startswith('$')):
        if ('$ cd' in l):
            p = l[5:]
            if (p == '/'):
                wd = fs
            elif (p == '..'):
                wd = wd.parent
            else:
                wd = wd.get(p)
    else:
        if l.startswith('dir '):
            p = l.split()[1]
            wd.add_dir(p)
        else:
            p = l.split()
            wd.add_file(p[1],int(p[0]))
#fs.print_filesystem()

def file_size(node, l):
    if (not node.is_file):
        s = node.size_recur()
        l.append(s)
        for c in node.children:
            file_size(c,l)

li = []
file_size(fs,li)
to_free = 30000000-70000000+fs.size_recur()

pa = 0
pb = 70000000
for v in li:
    if (v <= 100000):
        pa += v
    if (v >= to_free) and (v < pb):
        pb = v

print('A', pa)
print('B', pb)
