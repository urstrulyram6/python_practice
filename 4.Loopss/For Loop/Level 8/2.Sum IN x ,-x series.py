a=int(input())
b=int(input())
sum1=0
sum2=0
for i in range(1,b*2+1):
    if i%4==1:
        sum1+=((a**i))
    elif i%2==1:
        sum2+=(-(a**i)) 
print(sum1+sum2)

