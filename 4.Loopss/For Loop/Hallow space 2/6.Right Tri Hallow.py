a=int(input())
for i in range(a,0,-1):
    if i==1 or i==2 or i==a:
        sp="  "*(a-i)
        s="* "*(i)
        print(sp+s)
    else:
        sp="  "*(a-i)
        mid="  "*(i-2)
        print(sp+"* "+mid+"* ")


# n=int(input())
# for i in range(n):
#     space="  "*i
#     if i==0:
#         print("* "*n)
#     elif i==n-1:
#         print(space+"* ")
#     else:
#         hollow="  "*(n-i-2)
#         print(space+"* "+hollow+"* ")