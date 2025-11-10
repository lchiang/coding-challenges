
input = "4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77"
l = [int(s) for s in input.split(',')]
ll = sorted(set(l), reverse=True)
print("a", sum(ll))
print("b", sum(ll[-20:]))
from collections import Counter
c = Counter(l)
print("c", c.most_common(1)[0][1])
