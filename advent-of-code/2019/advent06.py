f = open('input06.txt')
d = f.read().splitlines()
#print(d)
dd = list(tuple(x.split(')')) for x in d)
#print(dd)
#d = list(map(int, d))

orbitor = [item[0] for item in dd]
orbitee = [item[1] for item in dd]
root = [x for x in orbitor if x not in orbitee][0]

from treelib import Node, Tree
tree = Tree()
tree.create_node(root, root)

### Part 2 start ###
you_list = ['YOU']
found_root = False
while not found_root:    
    par = [x for x in dd if x[1] == you_list[-1]][0]
    you_list.append(par[0])    
    if (par[0] == root):
        found_root = True 

san_list = ['SAN']
found_root = False
while not found_root:    
    par = [x for x in dd if x[1] == san_list[-1]][0]
    san_list.append(par[0])    
    if (par[0] == root):
        found_root = True 

while you_list[-1] == san_list[-1]:
    you_list.pop()
    san_list.pop()

print(len(you_list)+len(san_list)-2)
### Part 2 end ###

parent = [root]
cnt = 0
length = 0
i=0
while dd:    
    child_list_tree = [x for x in dd if x[0] in parent]
    for x in child_list_tree:
        tree.create_node(x[1], x[1], parent=x[0])
    
    child_list = [x[1] for x in dd if x[0] in parent]    
    length += 1
    cnt += len(child_list) * length
    dd = [x for x in dd if x[0] not in parent]
    parent = child_list
    
print(cnt)

#tree.show()
