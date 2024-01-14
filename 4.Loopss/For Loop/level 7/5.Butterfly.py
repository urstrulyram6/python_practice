a=int(input())
for i in range(1,a+1):
    space="  "*((a-i)*2)
    star1="* "*i
    star2="* "*i 
    print(star1+space+star2)
for x in range(a-1,0,-1):
    space="  "*((a-x)*2)
    star1="* "*(x)
    star2="* "*(x) 
    print(star1+space+star2)
