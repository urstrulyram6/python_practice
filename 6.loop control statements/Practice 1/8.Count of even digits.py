a=input()
al=len(a)
count=0
for i in range(al):
    if int(a[i])%2==0:
        count+=1
if count>2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
        
    