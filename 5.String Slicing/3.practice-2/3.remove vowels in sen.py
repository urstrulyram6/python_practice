a=input()
n=""
for i in a:
    if i.lower() in ["a","e","i","o","u"]:
        n=n+""
    else:
        n=n+i
print(n)