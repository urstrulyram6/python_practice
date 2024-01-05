a=input()
al=len(a)
sum=""
for i in range(al):
    if i<al-1:
        sum=sum+(a[i]+"-")
    else:
        sum=sum+(a[i])
print(sum)
    