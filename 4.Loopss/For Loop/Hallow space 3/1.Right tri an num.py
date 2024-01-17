a=int(input())
for i in range(1,a+1):
    if i==1 or i==2:
        sp="  "*(a-i)
        num=(str(i)+" ")*i
        print(sp+num)
    else:
        sp="  "*(a-i)
        mid="  "*(i-2)
        num=(str(i)+" ")
        print(sp+num+mid+num)
for x in range(a-1,0,-1):
    if x==1 or x==2:
        sp="  "*(a-x)
        num=(str(x)+" ")*x
        print(sp+num)
    else:
        sp="  "*(a-x)
        mid="  "*(x-2)
        num=(str(x)+" ")
        print(sp+num+mid+num)



# n=int(input())
# for i in range(n):
#     for j in range(1,n+1):
#         if j==n or j==n-i:
#             print(i+1,end=" ")
#         else:
#             print("  ",end="")
#     print() 
# for i in range(n-1):
#     for j in range(1,n+1):
#         if j==n or j==2+i:
#             print((n-1)-i,end=" ")
#         else:
#             print("  ",end="")
#     print()            