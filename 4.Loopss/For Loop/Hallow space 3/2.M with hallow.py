a=int(input())
for i in range(1,a+1):
    if i==1 or i==2 or i==a:
        star="* "*i
        mid="  "*((a-i)*2)
        print(star+mid+star)
    else:
        st="* "
        sp="  "*(i-2)
        mid="  "*((a-i)*2)
        print(st+sp+st+mid+st+sp+st)


# a=int(input())
# for i in range(1,a+1):
#     if i==1:
#         print("* "+" " * 4 * (a-i) + "*")
#     elif i==a:
#         print("* "*(2*a))
#     else:
#         print('* '+"  "*(i-2)+"*"+" "*(4*(a-i))+" * "+"  "*(i-2)+"*")