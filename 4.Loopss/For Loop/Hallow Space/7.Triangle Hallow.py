a=int(input())
for i in range(1,a+1):
    if i<=1 or i<=2 or i==a:
        print("* "*i)
    else:
        sp="  "*(i-2)
        print("* "+sp+"* ")


# n = int(input())

# print("* ")

# for i in range(1, n - 1):
#     middle_spaces = " " * (2 * (i - 1))
#     row = "* " + middle_spaces + "* "
#     print(row)

# print("* " * n)