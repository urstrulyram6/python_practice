a=int(input())
for i in range(1,a+1):
    if i==1 or i==2:
        sp=" "*(a-i)
        star="* "*(i)
        print(sp+star)
    else:
        sp=" "*(a-i)
        mid="  "*(i-2)
        print(sp+"* "+mid+"* ")
for x in range(a-1,0,-1):
    if x==1 or x==2:
        sp=" "*(a-x)
        star="* "*(x)
        print(sp+star)
    else:
        sp=" "*(a-x)
        mid="  "*(x-2)
        print(sp+"* "+mid+"* ")
    