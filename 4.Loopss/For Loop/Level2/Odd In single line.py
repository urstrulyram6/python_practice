a=int(input())
b=int(input())
sum=""
for i in range(a,b+1):
    if i%2!=0:
        sum=sum+str(i)+" "
print(sum)