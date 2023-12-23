# to retrive the denominations 
a=int(input())
no_of_100s=a//100
no_of_50s=(a%100)//50
no_of_10s=((a%100)%50)//10
no_of_1s=(((a%100)%50)%10)//1
print("100:"+str(no_of_100s))
print("50:"+str(no_of_50s))
print("10:"+str(no_of_10s))
print("1:"+str(no_of_1s))


M= int(input())

Note_500= int(M / 500)
Note_50= int((M - (Note_500 * 500) ) / 50)
Note_10= int((M - (Note_500 * 500) - (Note_50 * 50) ) / 10)
Note_1= int((M - (Note_500 * 500) - (Note_50 * 50) - (Note_10 * 10) ) / 1)

print( ("500:" + " " + str(Note_500)) + " " + ("50:" + " " + str(Note_50)) + " " + ("10:" + " " + str(Note_10)) + " " + ("1:" + " " + str(Note_1)) )


N=int(input())

H=int(N/100)
F=int((N-100*H)/50)
TW=int((N-100*H-50*F)/20)
T=int((N-100*H-50*F-20*TW)/10)
print("100 Notes: "+str(H))
print("50 Notes: "+str(F))
print("20 Notes: "+str(TW))
print("10 Notes: "+str(T))