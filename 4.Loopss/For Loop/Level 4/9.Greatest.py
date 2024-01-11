a=int(input())
gn=int(input())
for i in range(a-1):
    n=int(input())
    if n>gn:
        gn=n
print(gn)