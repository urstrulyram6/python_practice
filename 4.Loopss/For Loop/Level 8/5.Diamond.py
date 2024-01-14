a=int(input())
for i in range(1,a+1):
    sp=" "*(a-i)
    st=(str(i)+" ")*i
    print(sp+st)
for x in range(a-1,0,-1):
    sp=" "*(a-x)
    st=(str(x)+" ")*x
    print(sp+st)
    