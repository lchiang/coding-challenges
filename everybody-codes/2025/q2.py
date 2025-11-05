def trunc_div(a, b):
    q, r = divmod(a, b)
    return q + (1 if (a < 0) != (b < 0) and r != 0 else 0)

def add(a,b):
  return (a[0] + b[0], a[1] + b[1])
def mul(a,b):
  return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def div(a,b):
  #return (trunc_div(a[0],b[0]), trunc_div(a[1],b[1]))
  return (int(a[0] / b[0]), int(a[1] / b[1]))

def find_r(p):
  r = (0,0)
  for i in range(100):
    r = mul(r,r)
    #print(r)
    r = div(r,(100000,100000))
    #print(r)
    r = add(r,p)
    #print(r)
    if not in_range(r):
      return False
  return r

def in_range(r):
  return ((-1000000  < r[0] < 1000000) and (-1000000  < r[1] < 1000000))

# test 
a =(35300,-64910)
# part b
a = (-79097,14068)

from PIL import Image
img = Image.new('RGB', (1001, 1001))
pixels = img.load()

cnt = 0
eng = 0
px, py = 0, 0
for y in range(a[1], a[1]+1001, 1):
  for x in range(a[0], a[0]+1001, 1):
    r = find_r((x,y))
    if r and in_range(r):
      eng += 1
      pixels[px, py] = (255, 248, 212)
    else:
      pixels[px, py] = (49, 54, 71)
    cnt += 1
    px += 1
  px = 0
  py += 1
img.save('result.png')
print(cnt, eng)