a=int(input())
b=int(input())
sum=""
count=0
for i in range(a,b+1):
    if i%9==0:
        sum+=(str(i))+" "
        count+=1
        
if count>=1:
    print(sum)
else:
    print("No Numbers found")