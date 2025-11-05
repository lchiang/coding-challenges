ll = open('./2022/17/test.txt').read().splitlines()[0]
#ll = open('./2022/17/input.txt').read().splitlines()[0]

for j in ll:
    print(j)

'''
|3.@@@@.|
|2......|
|1......|
|0123456|
+-------+

0123

.1.
012
.1.

..2
..2
012

0
0
0
0

01
01

'''

current_block = 0

if (current_block == 0):
    print(1)
