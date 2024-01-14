N = int(input())
sum = 0
for i in range(1 , N + 1):
    no_of_digits = len(str(i))
    sum = sum + no_of_digits
print(sum)