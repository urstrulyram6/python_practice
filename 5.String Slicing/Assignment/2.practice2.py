# a="4sl37".isdigit()
# print(a)

# a="!!Tulip!!"
# x=a[:8:]
# print(x)

# a="seventy6" * 2
# a=a[3::6]
# total=0

# for i in  a:
#     if i.isdigit():
#         total=total+1
# print(total)

# a=" Indira Gandhi"
# a=a.strip("I")
# print(a)


# s="Albert Einstein"
# r=s[5:11:]
# print(r)


# a=" banana"
# a=a.strip("a")
# print(a)


# c="I open at the end"
# x=c.endswith("I open at the end")
# print(x)



# c="Raining dogs"
# x=c.startswith("Rain")
# print(x)


# c="*VIOLET*"
# a=c[::3]
# print(a)


# n="jok3!"
# r=n * 2
# r=r[3:8:2]
# print(r)


# w="ZJAZZ"
# a=w.strip("ZZ")
# b=w.replace("Z","")
# print(a)

# a=" bb8888bb"
# a=a.strip("b")
# print(a)
# print(a.isdigit())



# a="purple is a colour"
# a=a.strip("p u r")
# print(a)

# a=input()
# for i in a:
#     if i.isdigit():
#         a=a.strip(i)
# a=a.upper()
# r=a.startswith("HI5BY3")
# print(r)
# print(a)




message = input()
updated_message = message

for i in updated_message:
    if i.isdigit():
        message = message.strip(i)
        print(message)

# print(message)
