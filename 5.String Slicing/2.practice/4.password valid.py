# password = input()
# contains_digit = False

# for i in password:
#   is_digit = i.isdigit()
#   if is_digit:
#     contains_digit = True
# if contains_digit:
#   print("Valid Password")
# else:
#   print("Invalid Password")


a=input()
c1=False
c2=False
c3=False
c4=False
for i in a[:]:
    if i.isdigit():
        c1=True
c2=a.lower()==a
c3=a.upper()==a
c4= (not c2) and (not c3)
if c1 and c4:
    print("Valid Password")
else:
    print("Invalid Password")



# password = input()

# contains_digit = False
# for character in password:
#     is_digit = character.isdigit()
#     if is_digit:
#         contains_digit = True

# is_all_lower = password.lower() == password
# is_all_upper = password.upper() == password
# contains_lower_and_upper = (not is_all_lower) and (not is_all_upper)

# is_valid_password = contains_digit and contains_lower_and_upper

# if is_valid_password:
#     print("Valid Password")
# else:
#     print("Invalid Password")