# input = "R3,R4,L3,L4,R3,R6,R9"
# input = "L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3"
# input = "L3,L6,L6,L6,R3,L6,L6,L3,R6,L6,R6,L3,L6,R3,L6,R3,L3,R6,L6,L6,L3,R6,R3,L3,R6,L3,L6,R6,R6,L6,L3,L3,R6,R6,L6,L6,R6,R6,L6,L3,R6,L3,L3,R6,R3,L6,R6,L6,L3,L3,R3,R3,L6,R6,L6,R3,L6,R6,L6,L3"
#input = "L44,L77,L33,R99,L99,L55,L44,L33,R44,R77,R99,L66,L44,R44,L33,R88,L88,L66,R77,L88,L33,R66,L55,R88,L88,R55,L22,L22,R44,L11,R77,L22,R88,L33,L77,R77,L44,R55,R66,L66,L33,L11,R66,R55,R88,L77,L11,L55,R77,R88,L55,L77,R22,R66,L11,R66,L55,L11,R77,L88,L22,R77,R44,R99,L99,L88,L11,R44,L22,L44,R33,R66,R99,L99,L77,R77,L33,R77,L55,R66,L11,L55,R66,R66,L11,L44,R99,R66,L11,L33,R88,L77,R88,L55,R11,L11,R99,L77,L11,L11,R77,L33,R22,R88,L55,R22,R88,L88,L99,R44,R33,L66,L66,R55,L55,L33,R11,R55,L66,R22,L11,R99,L11,L55,R66,L33,R66,L44,R88,L55,R33,R99,L66,L55,L44,R66,R22,L55,R55,L99,L11,L77,R11,R22,L77,R44,R77,L77,L33,R44,L55,R77,R88,L77,L88,R99,L99,L33,R22,R33,L77,R99,L66,L44,R66,L55,R99,L22,R44,L44,R99,L22,R44,L77,R66,L77,L22,R99,L66,R66,L22,R99,L99,R66,L33,R66,L99,R66,R99,L44"
input = "R9496295,R999230,R5995740,L3198752,R5099541,R8599054,R3697151,L9098999,R9892377,R3299043,R7294817,L8899199,L5999460,R6097621,R9596256,L6697387,R5197972,R8593378,R1299623,L9598944,L9097361,R7896919,R2997690,L8493455,R3698927,R8497535,R1998460,R399964,L899361,L1798614,L3097613,L2198438,R2498225,R899361,L7793994,L2399736,R5396166,R1599856,L4796304,R5499395,R1499835,L6799252,L5895457,R5595688,L9498955,R2198438,R1698793,L3499685,R1999420,R2698083,L6999370,L2499725,R9192916,R1598768,L3898869,L3199072,R3798518,L5299417,R3497515,L7094959,R5196308,R4296947,L8899021,R399956,R5799362,L4998050,R2698947,L7896919,L3299043,R7297883,L8097651,R7694071,R3498985,L7894391,R799432,R8296763,L699797,L5299417,R1699507,L9899109,R7099219,R6299433,L3799658,L6195226,R6997970,R799384,R4099549,L1699813,L6299307,L9896139,R6997270,R7197192,R2999130,L8096841,L5296237,R2599246,L9897129,R2199362,R199922,L5799478,R999290,R3397586,L1498935,L6399296,L9298977,R1798614,L8693823,R4698637,R2799692,L4698167,R3498985,L3599604,R2599714,R599766,R1999820,L5299417,L4299527,L8499065,R3397382,R6999230,L199858,L6795172,R8696607,R2599714,L3798898,L3397382,R6799388,L5598376,R8297593,L4598206,R6497465,R1699337,L8499065,R599538,R999230,L499645,L9199172,R7094533,R3297459,R1599824,L8699217,L8399244,L1499865,R8897419,L3198752,L8699217,R8396724,R399692,R1599536,L2099769,R4299613,L399884,L5195996,R1699337,R3098791,L2099181,R3598596,L2399784,L7896919,R4199622,L7199352,R8799032,R1598768,R4598666,L6794764,L8793752,R3397382,R5799478,R2399736,L5899351,L599934,R1199868,L2499775,L5199428,R699923,L8299253,R899919,L6295527,R7696997,L2198306,R4899559,L6498115,R8096841,R6095303,R799688,R5299523,L1099901,L4399604,R3299637,L2099811,L6899379,L7197192,R2898869,L2299333,R2798012,L4399516,R5299417,R7299197,L6199318,R7197192,R1899259,L3399694,R2899739,R4999450,L1499565,R2399784,L299913,L9197332,L8993070,R5298463,L2699703,L5199428,R5399406,R5899469,L5699373,R2499725,L6599406,R1299493,R1099901,L6994610,L8996490,R8993070,R9293397,L6297543,R2998830,L4696381,R299883,R3797074,L6097621,L3199712,R8199098,L7199352,R9398966,R899739,R2399304,L8599226,L1399874,L5995740,R4996450,R2099811"
ll = input.split(',')

def wall_image(w):
    from PIL import Image
    img = Image.new('RGB', (1001, 1001))
    pixels = img.load()

    min_x = min(x for x, _ in w)
    max_x = max(x for x, _ in w)
    min_y = min(y for _, y in w)
    max_y = max(y for _, y in w)

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) in w:
                pixels[x-min_x, y-min_y] = (49, 54, 71)
            else:
                pixels[x-min_x, y-min_y] = (255, 248, 212)
        
    img.save('wall_part3.png')

def print_wall(w, ex, ey):    
    min_x = min(x for x, _ in w)
    max_x = max(x for x, _ in w)
    min_y = min(y for _, y in w)
    max_y = max(y for _, y in w)

    for y in range(min_y, max_y+1):
        l = []
        for x in range(min_x, max_x+1):
            if (x,y) == (0,0):
                l.append('S')
            elif (x,y) == (ex,ey):
                l.append('E')
            elif (x,y) in w:
                l.append('#')
            else:
                l.append('.')
        print(''.join(l))
    print()



'''
direction

0: up
1: right
2: down    
3: left

'''
dir = 0
x, y = 0, 0
wall = set()
st = {}

for l in ll:
    
    turn = l[0]
    step = int(l[1:])
    if turn == 'R':
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

    if dir == 0:
        for i in range(1, step+1):
            wall.add((x, y-i))
        y -= step
    elif dir == 1:
        for i in range(1, step+1):
            wall.add((x+i, y))
        x += step
    elif dir == 2:
        for i in range(1, step+1):
            wall.add((x, y+i))
        y += step
    else:
        for i in range(1, step+1):
            wall.add((x-i, y))
        x -= step
    wall.add((x,y))
# print_wall(wall, x, y)
wall_image(wall)
#    print(f"dir: {dir}, x: {x}, y: {y}")    


min_x = min(x for x, _ in wall)
max_x = max(x for x, _ in wall)
min_y = min(y for _, y in wall)
max_y = max(y for _, y in wall)
print(f"min_x: {min_x}, max_x: {max_x}, min_y: {min_y}, max_y: {max_y}")

visited = {}
visited[(x,y)] = 0
last_step = {(x,y)}
NEIGHBORS = [(-1,0), (1,0), (0,-1), (0,1)]
found = False
for round in range(20000):

    for x,y in last_step.copy():
        last_step.remove((x,y))

        for dx,dy in NEIGHBORS:
            if (x+dx, y+dy) == (0,0):
                print(f"Found at round {round+1}")
                found = True
                break
            elif min_x <= x+dx <= max_x and min_y <= y+dy <= max_y and \
                (x+dx, y+dy) not in wall and (x+dx, y+dy) not in visited:
                visited[(x+dx, y+dy)] = round + 1
                last_step.add((x+dx, y+dy))
        if found:
            break
    if found:
        break   
    
def print_wall_w_step(w, v):    
    min_x = min(x for x, _ in w)
    max_x = max(x for x, _ in w)
    min_y = min(y for _, y in w)
    max_y = max(y for _, y in w)

    for y in range(min_y, max_y+1):
        l = []
        for x in range(min_x, max_x+1):
            if (x,y) == (0,0):
                l.append('S')
            elif (x,y) in v:
                l.append(str(v[(x,y)]%10))
            elif (x,y) in w:
                l.append('#')
            else:
                l.append('.')
        print(''.join(l))
    print() 
#print_wall_w_step(wall,  visited)

