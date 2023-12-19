# a=input()
# b=input()
# a1=a[0:3]
# b1=b[0:3]
# print(a1==b1)

# print((4/2)==(8/4))

# print(len("30")!=len("40"))

# a=input()
# l=len(a)-1
# # print(l)
# x=a[0]!=a[l]
# print(x)



#  <------first word is equal to second last word------>
# a=input()
# b=input()
# a1=len(a)
# b1=len(b)
# s1=a1-b1
# r=a[s1:]
# print(r==b)


# <----------------first letter and index valuse in the 1st word same or not comarision ------------------->
# a=input()
# b=input()   
# al=len(a)-len(b)
# c=int(input())
# temp=c+al
# re= a[c:temp]==b[0:]            <wrong>
# print(re)

# a=input()
# b=input()
# c=int(input())
# end=len(b)+c
# x=a[c:end]
# print(x==b)


#  greater and less

# a=int(input())
# b=str(a)
# c=int(b[0])>int(b[1])
# print(a>25)
# print(c)

# print(True =="True")


# a=input()
# c1=(a[0]=="1" or a[1]=="1")
# c2=(int(a[0])+int(a[1])+int(a[2])<12)
# c3=(a[2]=="5")
# print(c1 and c2 and c3)


# -------------------------------------greatest amoung 3---------------------------------
# a = int(input())
# b = int(input())
# c = int(input())

# if a > b:
#     number = a
# else:
#     number = b
# if c > number:
#     number = c
# print(number)



# a=int(input())
# b=int(input())
# c=int(input())
# if ((a>9 and a<21) or (b>9 and a<21) or (c>9 and c<21)):
#     print("True")
# else:
#     print("False")

# a=22
# b=13
# print(b%a)

# a=int(input())
# b=int(input())
# r=False and False
# if r:
#     an=(a%b)!=(a%b)
#     print(an)
# else:
#     an=(a**b)==(b**a)
#     print(an)

# print(an)


# # if 

# a=int(input())
# c1=a%9==0
# a=str(a)
# c2 =(int(a[0])==9 or int(a[1])==9)
# if (c1 or c2) :
#     print("Lucky Number")
# else:
#     print("Unlucky Number")
    

# divisible by 6 3 2 


# a=int(input())
# c1=(a%6==0)
# c2=(a%3==0)
# c3=(a%2==0)
# if c1:
#     print("Number is divisible by 6")
# elif c2:
#     print("Number is divisible by 3")
# elif c3:
#     print("Number is divisible by 2")
# else:
#     print("Number is not divisible by 2, 3 or 6")   


# # exponent 
# a=int(input())
# b=0.5
# print(a**b)

# a=int(input())
# b=int(input())
# if (a**2 + b**2)>=60:
#     print("Greater than or Equal to 60")
# else:
#     print("Less than 60")

# a=int(input())
# b=int(input())
# ap=a**b
# bp=b**a
# if ap>bp:
#     print(ap)
# else:
#     print(bp)

# a=input()
# al=len(a)-1
# ald=a[al]
# asq=str(int(a)**2)
# asql=len(asq)-1
# asqld=asq[asql]
# if ald==asqld:
#     print("Equal")
# else:
#     print("Not Equal")


# a=input()
# a1=int(a[0])
# a2=int(a[1])
# a3=int(a[2])
# arm=((a1**3)+(a2**3)+(a3**3))
# if a==str(arm):
#     print("True")
# else:
#     print("False")


# a=int(input())
# tri=a*3
# if tri%6==0:
#     print(tri)
# else:
#     print(a)

# a=int(input())
# y=int(a/365)
# w=int((a%365)/7)
# d=b%7

# print(str(y) +"Years")
# print(str(w) +"weeks")
# print(str(c) +"Days")

# a=((343)==(7**3))
# print(a)

# curent bill

a=int(input())
c1= (a>0 and a<=50)
c2=(a>50 and a<=150)
c3=(a>150 and a<=250)
c4=(a>251)
c5=(a==0)
if c1:
    bill1=2*a
    s_charge = 0.20*bill1
    total = bill1+s_charge
    print(total)
elif c2:
    a1=a-50
    bill1=3*a1+100
    s_charge = 0.20*(bill1)
    total = bill1+s_charge
    print(total)
elif c3:
    a1=a-150
    bill1=(5*a1)+400
    s_charge = 0.20*(bill1)
    total = bill1+s_charge
    print(total)
elif c4:
    a1=a-250
    bill1=(8*a1)+900
    s_charge = 0.20*(bill1)
    total = bill1+s_charge
    print(total)
elif (c5):
    print(0.0)
    
    
    
# Step 1: Reading inputs
number_of_units = int(input()) # Reading first line of input() and converted into integer

# Step 2: Logic of the code
if (number_of_units < 51) :
    total = (number_of_units * 2)
elif (number_of_units < 151) :
    total = (50 * 2) + (3 * (number_of_units - 50))
elif (number_of_units < 251) :
    total = (50 * 2) + (100 * 3) + (5 * (number_of_units - 150))
elif (number_of_units >= 251) :
    total = (50 * 2) + (100 * 3) + (100 * 5) + (8 * (number_of_units - 250))

# Step 3: Printing outputs
surcharge  = (total * 0.2)
total_bill = (total + surcharge)
print(total_bill)

# check whheather its leap year or not

y=int(input())
if (y%400==0) or ((y%4==0)and(y%100!=0)):
    print("True")
else:
    print("False")