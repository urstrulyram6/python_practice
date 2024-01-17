a=int(input())
for i in range(1,a+1):
    if i==1 or i==2:
        st="* "*(i)
        space="  "*((a-i)*2)
        print(st+space+st)
    else:
        st="* "
        space=("  "*(i-2))
        mid="  "*((a-i)*2)
        print(st+space+st+mid+st+space+st)
for x in range(a,0,-1):
    if x==1 or x==2:
        st="* "*(x)
        space="  "*((a-x)*2)
        print(st+space+st)
    else:
        st="* "
        space=("  "*(x-2))
        mid="  "*((a-x)*2)
        print(st+space+st+mid+st+space+st)
        
        