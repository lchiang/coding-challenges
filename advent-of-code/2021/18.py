import math
from binarytree import Node, get_parent
from itertools import permutations

def explode(t):
    if t.height >=5:
        #print('explode')
        leaves = [x for x in t.levels[5] if x.value != -1]
        p = get_parent(t,leaves[0])
        ll = p.left.value
        rr = p.right.value
        p.left = None
        p.right = None
        p.value = 0

        all_leaves = [x for x in t.inorder if x.value != -1]
        p_index = all_leaves.index(p)

        if p_index > 0: # ripple left
            all_leaves[p_index-1].value += ll
        if p_index < len(all_leaves)-1: # ripple right
            all_leaves[p_index+1].value += rr
        #print(t)

def split(t):
    if t.max_node_value >= 10:
        #print('split')
        e = [x for x in t.inorder if x.value >= 10][0]
        e.left = Node(int(math.floor(e.value/2)))
        e.right = Node(int(math.ceil(e.value/2)))
        e.value = -1
        #print(t)

def reduction(t):
    reduced = False
    while not reduced:
        reduced = True
        if t.height >=5:
            explode(t)
            reduced = False
        elif t.max_node_value >= 10:
            split(t)
            reduced = False

def addition(tree1, tree2):
    r = Node(-1)
    r.left = tree1
    r.right = tree2
    return r

def read(line):
    r = Node(-1)
    n = r
    cc = ''
    for c in line:
        if c == '[':
            if len(cc) > 0:
                n.value = int(cc)
                cc = ''
            n.left = Node(-1)
            n = n.left
        elif c == ',':
            if len(cc) > 0:
                n.value = int(cc)
                cc = ''
            n = get_parent(r,n)
            n.right = Node(-1)
            n = n.right
        elif c == ']':
            if len(cc) > 0:
                n.value = int(cc)
                cc = ''
            n = get_parent(r,n)
        else:
            cc = cc + c
    return r

def magnitude(t):
    l = t.left.value
    r = t.right.value
    if l == -1:
        l = magnitude(t.left)
    if r == -1:
        r = magnitude(t.right)
    return l*3 + r*2

ll = open('in18t1.txt').read().splitlines()

# Part A
tt = read(ll[0])
for l in ll[1:]:
    tt = addition(tt, read(l))
    reduction(tt)
print('Part A', magnitude(tt))

# Part B
perm = permutations(ll, 2)
mm = 0
for x in list(perm):
    t = addition(read(x[0]), read(x[1]))
    reduction(t)
    mm = max(mm, magnitude(t))
print('Part B', mm)
