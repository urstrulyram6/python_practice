a=int(input())
for i in range(1,a+1):
    if i<=1 or i<=2 or i==a:
        sp=" "*(a-i)
        star="* "*(i)
        print(sp+star)
    else:
        spcb="  "*(i-2)
        sp=" "*(a-i)
        print(sp+"* "+spcb+"* ")