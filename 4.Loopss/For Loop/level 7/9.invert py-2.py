a=int(input())
for i in range(a,0,-1):
    if i==a:
        print("+ "*i)
    else:
        space=" "*(a-i)
        star="* "*(i)
        print(space+star)