a=int(input())
for i in range(a,0,-1):
    star="* "*i
    sp=" "*(a-i)
    print(sp+star)