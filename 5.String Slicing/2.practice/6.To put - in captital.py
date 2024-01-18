a=input()
sum=""
for i in a[:]:
    cap=i.upper()
    if i==cap:
        sum=sum+"-"+i.lower()
    else:
        sum=sum+i
print(sum)
        