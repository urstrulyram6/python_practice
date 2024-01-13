a=int(input())
for i in range(a,0,-1):
    space=("  "*(a-i))
    n=((str(i)+" ")*i)
    print(space+n)