a=int(input())
for i in range(1,a+1):
    if i==1 or i==2:
        print((str(i)+" ")*(i))
    else:
        sp="  "*(i-2)
        n=(str(i)+" ")
        print(n+sp+n)
for i in range(a-1,0,-1):
    if i==1 or i==2:
        print((str(i)+" ")*(i))
    else:
        sp="  "*(i-2)
        n=(str(i)+" ")
        print(n+sp+n)