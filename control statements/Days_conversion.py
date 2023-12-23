a=int(input())
years =a//365
weeks =(a-years*365)//7
days =(a- (years*365) - (weeks*7) )//1
print(str(years)+" years "+str(weeks)+" weeks "+str(days)+" days")