a=int(input())
print("* "*(a*2 -1))
for i in range(a-1,0,-1):
    s=" "*(a-i)
    s1=" "*(((a-i)*2)-2)
    st="* "*(i)
    print(s+st+s1+st)


# a = int(input())
# print("* " * ( 2 *a - 1))
# for i in range(1,a):
#     spaces = " " * (i)
#     stars = "* " * (a - i)
#     middle_spaces = "  " * (i - 1)
#     print(spaces + stars + middle_spaces + stars)

# n = int(input()) 
# each_row = "* " * (n*2-1)
# print(each_row) 
# hollow_spaces = 0
# for i in range(1,n+1):
#     left_spaces = " " * i 
#     stars = "* " * (n-i) 
#     result = left_spaces+stars+" " * hollow_spaces +stars 
#     hollow_spaces = hollow_spaces+2 
#     print(result)
    