a=input()
al=len(a)
sq=0
x=0
for i in range(0,al):
    x=((int(a[i]))**al)
    sq=sq+x
print(sq)