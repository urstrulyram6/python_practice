a=int(input())
b=int(input())
for i in range(1,a+1):
    if i==1:
        print("* "*b)
    elif i==a:
        print("* "*b)
    else:
        sp="  "*(b-2)
        print("* "+sp+"* ")