a=int(input())
for i in range(a,0,-1):
    if i==a or i==1 or i==2:
        sp=" "*(a-i)
        st="* "*(i)
        print(sp+st)
    else:
        sp=" "*(a-i)
        mid="  "*(i-2)
        print(sp+"* "+mid+"* ")
        