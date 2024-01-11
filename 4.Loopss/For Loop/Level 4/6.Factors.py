a=int(input())
sum=""
for i in range(1,a+1):
    if a%i==0:
        sum=sum+(str(i))+" "
print(sum)

# def find_factors(n):