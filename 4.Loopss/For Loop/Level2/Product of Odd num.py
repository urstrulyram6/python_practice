a=int(input())
b=int(input())
sum=1
for i in range(a,b+1):
    if i%2==1:
        sum=sum*i
print(sum)