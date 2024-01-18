a=int(input())
D=a//86400
H=((a)-D*86400)//3600
M=((a)-D*86400-H*3600)//60
S=((a)-D*86400-H*3600-M*60)
if D!=0 and H==0 and M==0 and S==0 :
    print(str(D)+" Days ")
if D!=0 and H!=0 and M==0 and S==0 :
    print(str(D)+" Days  "+str(H)+" Hours ")
if D!=0 and H!=0 and M!=0 and S==0 :
    print(str(D)+" Days"+str(H)+" Hours "+str(M)+" Minutes")
if D!=0 and H!=0 and M!=0 and S!=0 :
    print(str(D)+" Days "+str(H)+" Hours "+str(M)+" Minutes "+str(S)+" Seconds ")
if D==0 and H!=0 and M==0 and S==0 :
    print(str(H)+" Hours ")
if D==0 and H!=0 and M!=0 and S==0 :
    print(str(H)+" Hours "+str(M)+" Minutes")
if D==0 and H!=0 and M!=0 and S!=0 :
    print(str(H)+" Hours "+str(M)+" Minutes"+str(S)+" Seconds")
if D==0 and H==0 and M!=0 and S==0 :
    print(str(M)+" Minutes ")
if D==0 and H==0 and M!=0 and S!=0 :
    print(str(M)+" Minutes "+str(S)+" Seconds")
if D==0 and H==0 and M==0 and S!=0 :
    print(str(S)+" Seconds ")   