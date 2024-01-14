a=int(input())
for i in range(1,a+1):
    space="  "*(a-i)
    pl="+ "*(i-1)
    ha="#"
    print(space+pl+ha)
for x in range(a-1,0,-1):
    space="  "*(a-x)
    pl="+ "*(x-1)
    ha="#"
    print(space+pl+ha)
    