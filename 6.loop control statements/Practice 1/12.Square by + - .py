a=int(input())
pls="+ "
dsh="- "
an="| "
spac="  "
for i in range(a+2):
    if i==0 or i==(a+1):
        print(pls+dsh*a+pls)
    else:
        print(an+spac*a+an)