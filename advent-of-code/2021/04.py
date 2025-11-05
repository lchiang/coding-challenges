f = open('in04.txt')
inputfile = f.read().splitlines()

board_num = (len(inputfile)-1)//6
draw = [int(x) for x in inputfile[0].split(',')]

# def print_board(b):    
#    for l in b:        
#        print('>',''.join(['{:4}'.format(c) for c in l]))
#    print()

def mark_board(b,m):    
    for i in range(len(b)):
        b[i] = [-1 if x==m else x for x in b[i]]

def check(b):
    for l in b:
        if sum(l) == -1*len(b):
            return True
    for i in range(len(b)):
        c = 0
        for l in b:
            c += l[i]
        if c == -1*len(b):
            return True
    return False

def score(b, draw):
    i = 0
    for l in b:
        for x in l:
            if x != -1:
                i += x
    return i*draw

boards = []
for i in range(board_num):
    b = []
    b.append([int(x) for x in inputfile[(6*i)+2].split()])
    b.append([int(x) for x in inputfile[(6*i)+3].split()])
    b.append([int(x) for x in inputfile[(6*i)+4].split()])
    b.append([int(x) for x in inputfile[(6*i)+5].split()])
    b.append([int(x) for x in inputfile[(6*i)+6].split()])    
    boards.append(b)

winning_board = {}
ii = 0
for d in draw:    
    i=0
    for b in boards:
        mark_board(b, d)
        if ((i not in winning_board) and check(b)):
            winning_board[i] = score(b,d)
            ii = i
        i+=1    
    #if winning_board: # part A
    if len(winning_board) == board_num: # part B
        break

print(ii, winning_board[ii])
