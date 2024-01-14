a=int(input())
for i in range(1,a+1):
    if i==1:
        print("* "*a)
    elif i==a:
        print("* "*a)
    else:
        sp="  "*(a-2)
        print("* "+sp+"* ")
    