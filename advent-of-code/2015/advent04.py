import hashlib
sk = 'bgvyzdsv'
for v in range(10000000):
    s = sk+str(v)
    result = hashlib.md5(s.encode()).hexdigest()
    # if result.startswith('00000'): # Part 1
    if result.startswith('000000'): # Part 2
        print('key', sk, 'num', v)
        print('md5', result)
        break
  
