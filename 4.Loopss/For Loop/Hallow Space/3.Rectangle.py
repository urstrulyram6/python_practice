r=int(input())
c=int(input())
for i in range(0,r):
    if i==(0):
        print("* "*c)
    elif i==(r-1):
        print("* "*c)
    else:
        space="0 "*(c-2)
        print("* "+space+"* ")