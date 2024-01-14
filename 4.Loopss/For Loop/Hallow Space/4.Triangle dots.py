a=int(input())
for i in range(1,a+1):
    if i==1:
        print(". ")
    elif i==2:
        print(". "*i)
    elif i==a:
        print(". "*a)
    else:
        dots="0 "*(i-2)
        print(". "+dots+". ")
        

# n=int(input())

# for i in range(1,n+1):
#     if i>2 and i<n:
#         print(". " + "0 "*(i-2) + ".")
#     else:    
#         print(". "*i) 
