a=int(input())
for i in range(a,0,-1):
    n=(str(i)*i)
    s=(" "*(a-i))
    print(s+n)