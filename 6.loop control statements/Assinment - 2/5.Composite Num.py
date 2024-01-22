a=int(input())
count=0
for i in range(2,a):
    if a%i==0:
        count+=1
if count>=1:
    print("True")
else:
    print("False")