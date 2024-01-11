a=input()
al=len(a)
count=0
for i in range(al):
    if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
        count+=1
if count>2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")