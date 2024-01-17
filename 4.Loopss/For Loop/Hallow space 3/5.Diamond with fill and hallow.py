# a=int(input())
# for i in range(1,a+1):
#     sp=" "*(a-i)
#     st="* "*i
#     print(sp+st)
# for x in range(a-1,0,-1):
#     if x==1 or x==2:
#         sp=" "*(a-x)
#         st="* "*(x)
#         print(sp+st)
#     else:
#         sp=" "*(a-x)
#         st="* "
#         mid="  "*(x-2)
#         print(sp+st+mid+st)


n = int(input())

for i in range(1,n+1):
    print((" " * (n-i)) + ("* " *i))
for i in range(1,n-1):
    print((" "*i) + "* " + ((n-i-2)*"  ") + "*")
print((n-1) * " " + "*")