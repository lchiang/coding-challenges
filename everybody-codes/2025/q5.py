


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.children = None
    def add(self, dd):
        if ((dd < self.data) and (self.left == None)):
            self.left = dd
        elif ((dd > self.data) and (self.right == None)):
            self.right = dd
        else:
            if (self.children == None):
                kid = TreeNode(dd)
                self.children = kid
            else:
                self.children.add(dd)
    def print(self):
        #print(self.left, self.data, self.right)
        print('{:3} {:3} {:3} '.format(self.left if self.left is not None else ' ', self.data, self.right if self.right is not None else ' '))
        if (not self.children == None):
            self.children.print()
    def spine(self):
        s = self.data
        if (not self.children == None):
            ks = self.children.spine()
            return str(s)+str(ks)
        else:
            return str(s)

from functools import cmp_to_key
sd = {}
def compare_by_name(x, y):
    print('compare', x, y)
    '''
    If two swords have different qualities, a higher quality score means a better sword.
    If the quality of both swords is the same, the numbers resulting from the subsequent levels of the fishbone should be compared, starting from the top. A higher score on the first level, which differs between swords, indicates a better sword.
    If the above conditions are not met, the sword with the higher identifier is considered better.
    '''
    x_quality = int(sd[x].spine())
    y_quality = int(sd[y].spine())
    if x_quality != y_quality:
        print('quality', x_quality, y_quality, x_quality - y_quality)
        return x_quality - y_quality
    else:
        
        stop_ind = False
        x_node = sd[x]
        y_node = sd[y]
        print('compare lv', x, y, x_node.data, y_node.data)
        x_node.print()
        y_node.print()
        while not stop_ind:
            
            x_lv = int((str(x_node.left) if x_node.left is not None else '') + str(x_node.data) + (str(x_node.right) if x_node.right is not None else ''))
            y_lv = int((str(y_node.left) if y_node.left is not None else '') + str(y_node.data) + (str(y_node.right) if y_node.right is not None else ''))
            print('lv', stop_ind, x_lv, y_lv,  x_lv - y_lv)
            if x_lv != y_lv:
                print('xllv', x_lv - y_lv)
                return x_lv - y_lv
            
            if x_node.children == None and y_node.children == None:
                stop_ind = True
                print('no kid')
            elif x_node.children != None and y_node.children == None:
                print('111')
                return 1
            elif x_node.children == None and y_node.children != None:                    
                print('-1-1-1')
                return -1
                
            else:
                x_node = x_node.children
                y_node = y_node.children
        print('order', x,y,x-y)
        return x-y
            

            





f = open('in_5c.txt')
ll = f.read().split()




for line in ll:
    #input = "58:5,3,7,8,9,10,4,5,7,8,8"
    #input = "70:7,4,3,7,8,4,2,8,6,8,8,5,1,2,9,5,6,1,6,1,7,8,4,4,7,6,7,4,9,1"
    name, l = line.split(':')
    
    s = [int(c) for c in l.split(',')]
    #print(name,s)
    root = TreeNode(s[0])
    for i in s[1:]:
        root.add(i)
        
    
    #print(spine)
    sd[int(name)] = root
    print('==', name, '==', root.spine())
    root.print()

sorted_numbers = sorted(sd.keys(), key=cmp_to_key(compare_by_name), reverse=True)

#To calculate the checksum, you need to multiply the sword identifiers by their position on the sorted list, starting from 1, and sum the resulting values.

for key, value in sd.items():
    print(f"{key}: {value}")
print(sorted_numbers)

print(sum([a*b for a,b in zip(sd.keys(),sorted_numbers)]))
