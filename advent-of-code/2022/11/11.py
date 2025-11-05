num = 8
m=[]
'''
#test input
m.append([79, 98])
m.append([54, 65, 75, 74])
m.append([79, 60, 97])
m.append([74])

def op0(o): return o*19
def op1(o): return o+6
def op2(o): return o*o
def op3(o): return o+3
op = [op0, op1, op2, op3]

def te0(o): return 2 if o%23==0 else 3
def te1(o): return 2 if o%19==0 else 0
def te2(o): return 1 if o%13==0 else 3
def te3(o): return 0 if o%17==0 else 1
te = [te0, te1, te2, te3]
'''
#real input
m.append([65, 58, 93, 57, 66])
m.append([76, 97, 58, 72, 57, 92, 82])
m.append([90, 89, 96])
m.append([72, 63, 72, 99])
m.append([65])
m.append([97, 71])
m.append([83, 68, 88, 55, 87, 67])
m.append([64, 81, 50, 96, 82, 53, 62, 92])

def op0(o): return o*7
def op1(o): return o+4
def op2(o): return o*5
def op3(o): return o*o
def op4(o): return o+1
def op5(o): return o+8
def op6(o): return o+2
def op7(o): return o+5
op = [op0, op1, op2, op3, op4, op5, op6, op7]

def te0(o): return 6 if o%19==0 else 4
def te1(o): return 7 if o%3==0 else 5
def te2(o): return 5 if o%13==0 else 1
def te3(o): return 0 if o%17==0 else 4
def te4(o): return 6 if o%2==0 else 2
def te5(o): return 7 if o%11==0 else 3
def te6(o): return 2 if o%5==0 else 1
def te7(o): return 3 if o%7==0 else 0
te = [te0, te1, te2, te3, te4, te5, te6, te7]

ins = [0]*num
turn = 0
while turn < 10000:
    next = [[] for i in range(num)]
    for i in range(num):
        for it in m[i]:
            ins[i] = ins[i] + 1
            w = op[i](it)
            #w = w // 3 # Part A

            #w = w % (23*19*13*17) # Part B test
            w = w % (19*3*13*17*2*11*5*7) # Part B real

            n = te[i](w)
            m[n].append(w)
        m[i] = []
    #print(turn, m)
    turn += 1
    if turn%1000 ==0:
        print(turn, ins)

print(ins, sorted(ins)[-2:][0]*sorted(ins)[-2:][1])

