a=int(input())
sum=0
for i in range(2,10):
    if a%i==0:
        sum+=1
if sum>=1:
    print("Divisible Number")
else:
    print("Indivisible Number")