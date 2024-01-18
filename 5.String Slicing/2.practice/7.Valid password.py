a=input()
bol=False
for i in a[:]:
    cap=i.upper()
    if i==cap:
        bol=True
    else:
        bol=False
if bol:
    print("Valid Password")
else:
    print("Invalid Password")