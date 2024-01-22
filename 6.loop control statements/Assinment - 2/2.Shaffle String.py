a=input()
b=input()
al=len(a)
sum=""
for i in range(al):
    if i%2==0:
        sum+=a[i]
    elif i%2==1:
        sum+=b[i]
print(sum)