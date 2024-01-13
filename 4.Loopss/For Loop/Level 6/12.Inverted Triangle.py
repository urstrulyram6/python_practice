a=int(input())
for i in range(a,0,-1):
    space=" "*(a-i)
    s=("*"*((i*2)-1))
    print(space+s)