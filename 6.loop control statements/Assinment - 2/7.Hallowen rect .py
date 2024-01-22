a=int(input())
b=int(input())
sd="-"
bd="|"
pl="+"
space=" "
for i in range(a+2):
    if i==0 or i==a+1:
        print(pl+sd*b+pl)
    else:
        print(bd+space*b+bd)
    