a=int(input())
for i in range(1,a+1):
    space="  "*(a-i)
    num=((str(i)+" ")*((i*2)-1))
    print(space+(num))