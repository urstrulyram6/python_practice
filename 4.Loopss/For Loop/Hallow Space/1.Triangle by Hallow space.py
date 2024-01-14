a=int(input())
for i in range(0,a):
    if i==0:
        print("  "*(a-1)+"*")
    elif i==a-1:
        print("* "*a)
    else:
        space="  "*(a-i-1)
        hallow="  "*(i-1)
        print(space+"* "+hallow+"* ")