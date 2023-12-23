# The input would be like entering 1 string ie Day Name with start of that month,other is  int value that is on the day we want to know
d = input()
n = int(input())
if d=="Sunday":
    Day=0
elif d=="Monday":
    Day=1
elif d=="Tuesday":
    Day=2
elif d=="Wednesday":
    Day=3
elif d=="Thursday":
    Day=4
elif d=="Friday":
    Day=5
elif d=="Saturday":
    Day=6
exday=Day+n-1
exday=exday%7
if exday==0:
    print("Sunday")
elif exday==1:
    print("Monday")
elif exday==2:
    print("Tuesday")
elif exday==3:
    print("Wednesday")
elif exday==4:
    print("Thursday")
elif exday==5:
    print("Friday")
elif exday==6:
    print("Saturday")
    
