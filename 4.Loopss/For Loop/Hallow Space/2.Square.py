a=int(input())
for i in range(0,a):
    if i==0:
        print("* "*a)
    elif i==a-1:
        print("* "*a)
    else:
        stars="0 "*(a-2)
        print("* "+stars+"* ")