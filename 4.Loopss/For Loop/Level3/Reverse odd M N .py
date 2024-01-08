a=int(input())
b=int(input())
sum=""
for i in range(b,a-1,-1):
    if i%2==1:
        sum=sum+str(i)+" "
print(sum)