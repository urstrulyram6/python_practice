a=int(input())
for i in range(1,a+1):
    for x in range(a,i,-1):
        print(" ",end="")
    for y in range(1,i+1):
        print("*",end="")
    print()