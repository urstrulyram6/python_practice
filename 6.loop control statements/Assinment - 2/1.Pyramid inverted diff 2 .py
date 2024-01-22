a=int(input())
count=a*2 - 1
for i in range(a):
    print("  "*i*2+"* "*count)
    count-=2