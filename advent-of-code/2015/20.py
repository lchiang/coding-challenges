import math

def divSumA(n) :
    if(n == 1):
       return 1
    result = 0
    for i in range(2,(int)(math.sqrt(n))+1) :
        if (n % i == 0) :
            if (i == (n/i)) :
                result = result + i
            else :
                result = result + (i + n//i)
    return (result + n + 1)

def divSumB(n) :
    return sum([n // x for x in range(1, 51) if n % x == 0])

for x in range(830000, 900900):
    if (divSumA(x)*10 >= 36000000): # Part A
        print('A', x)
        break

for x in range(830000, 900900):
    if (divSumB(x)*11 >= 36000000): # Part B
        print('B', x)
        break
