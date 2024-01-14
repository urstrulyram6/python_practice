a=int(input())
count=0
for i in range(1,a+1):
    if a%i==0:
        count+=1
if count>2:
    print("Numbe has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")