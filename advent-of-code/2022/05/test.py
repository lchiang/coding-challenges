mv = 3
s=[1,3,5,7,9]
k=[2]
k=k+s[-mv:]
s=s[:-mv]

print(s, k)
