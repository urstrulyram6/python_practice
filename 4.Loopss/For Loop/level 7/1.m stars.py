# a=int(input())
# for i in range(1,a+1):
#     ftst="* "*i
#     fts="  "*(a-i)
#     ft=ftst+fts

#     sts="  "*(a-i)
#     stst="* "*i
#     st=sts+stst
#     print(ft+st)

a=int(input())
for i in range(1,a+1):
    x="* "*i
    b=" "*((a-i)*4)
    c="* "*i
    print(x+b+c)


# a = int(input())

# for i in range(1, a + 1):
#     first_triangle_stars = "* " * i
#     first_triangle_spaces = "  " * (a - i)

#     first_triangle = first_triangle_stars + first_triangle_spaces
    
#     second_triangle_spaces = "  " * (a - i)
#     second_triangle_stars = "* " * i

#     second_triangle = second_triangle_spaces + second_triangle_stars

#     print(first_triangle + second_triangle)
    

# num=int(input())
# result=(num*2)-2
# for i in range(1,num+1):
#     print(("* "*i)+(" "*result)+(" "*result)+("* "*i))
#     result=result-2
    

# given_num = int(input())
# for i in range(1,given_num+1):
#     spaces = "  "*(2*(given_num-i))
#     stars = "* "*i + spaces + "* "*i
#     print(stars)
    