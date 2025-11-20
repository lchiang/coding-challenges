f = open('in11c.txt')
input = [int(s) for s in f.read().splitlines()]
mean = sum(input) // len(input)
#print(mean)
print(sum([x-mean for x in input if x>mean]))

