a=int(input())
b=int(input())
sum=""
for i in range(a,b+1):
    if i%6==0:
        sum=sum+(str(i))+" "
if sum=="":
    print("No Numbers Found")
else:
    print(sum)