a=input()
if (a.isdigit())==True:
    print("Digit")
elif (a.isupper())==True:
    print("Uppercase Letter")
elif (a.islower())==True:
    print("Lowercase Letter")
else:
    print("Special Character")