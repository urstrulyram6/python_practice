a=input()
a=a.lower()
a=a.replace(" ","")
a=a.replace("'","")

rev=a[::-1]
if a==rev:
    print("True")
else:
    print("False")