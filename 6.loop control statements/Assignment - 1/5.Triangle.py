n=int(input())
k=n 
for i in range(1,n+1):
    space=" "*k
    star="* "*i
    print(space+star)
    k=k-1
    