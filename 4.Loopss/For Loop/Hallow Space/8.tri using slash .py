a=int(input())
for i in range(a+1,0,-1):
    if i==a+1:
        print("_"*(a+1))
    else:
        space=" "*(i-1)
        print("|"+space+"/")
        
    