ll = open('in12a.txt').read().splitlines()

d = {}
for l in ll:
    l1, l2 = l.split('-')
    if l2 != 'start':
        if l1 not in d:
            d[l1] = [l2]
        else:
            d[l1].append(l2)
    if l1 != 'start':
        if l2 not in d:
            d[l2] = [l1]
        else:
            d[l2].append(l1)

print(d)

#d[a] = list of destination from a
ppath = []

def visit(path, a):
    for x in d[a]:
        if x == 'end':
            #print(path+[x])
            if (path[1:]+[x]) not in ppath:
                ppath.append(path[1:]+[x])
            '''
        # Part A
        elif x.isupper() or x not in path:
            p = path.copy()
            p.append(x)
            visit(p,x)
            '''

        elif x.isupper():
            p = path.copy()
            p.append(x)
            visit(p,x)

        elif x not in path:
            if not path[0]: # special one not visited
                print('first time', x, path)
                p1 = path.copy()
                p1.append(x)
                p1[0] = x
                visit(p1,x)

            p2 = path.copy()
            p2.append(x)
            visit(p2,x)
        elif x == path[0] and path.count(x)==2: # visit again
            p = path.copy()
            p.append(x)
            visit(p,x)

visit(['','start'],'start')
print(len(ppath))