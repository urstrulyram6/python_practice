a=int(input())
for i in range(1,a+1):
    s1=" "*(a-i)
    st="* "*i
    print(s1+st)
for x in range(a-1,0,-1):
    s1=" "*(a-x)
    st="* "*x
    print(s1+st)
    