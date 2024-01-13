a=int(input())
b=int(input())
sum=0
for i in range(1,b*2+1):
    if i%4==0:
        sum+=(-(a**i))
    elif i%2==0:
        sum+=(a**i) 
print(sum)