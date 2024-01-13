a=int(input())
for i in range(1,a):
    space=" "*(a-i)
    star="*"*(i)
    print(space+star)
print("#"*a)