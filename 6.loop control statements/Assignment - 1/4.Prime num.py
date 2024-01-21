a=int(input())
x=0
for i in range(2,a):
    if a%i==0:
         x+=1
if x==0:
    print("Prime Number")
else:
    print("Not a prime Number")