a=int(input())
for i in range(a,0,-1):
    if i==a or i==1 or i==2:
        if i==a:
            print("# "*(i))
        else:
            print("+ "*(i))
    else:
        sp="  "*(i-2)
        print("+ "+sp+"+ ")