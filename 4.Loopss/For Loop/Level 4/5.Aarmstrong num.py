a=input()
al=len(a)
sq=0
sum=0
for i in range(al):
    sq=((int(a[i]))**al)
    sum=sum+sq
if sum==int(a):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
