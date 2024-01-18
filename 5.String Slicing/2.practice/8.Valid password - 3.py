a=input()
c1=False
c2=False
c3=False
for i in a[:]:
    if i==i.upper():
        c1=True
    elif i==i.lower():
        c2=True
    elif i==i.isdigit():
        c3=True
if c1 and c2 and c3:
    print("Valid Password")
else:
    print("Invalid Password")