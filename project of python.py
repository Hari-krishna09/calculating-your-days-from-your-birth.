#program for calculating days
date1=input("Enter your Date of Birth(DOB):").split("/")
date2=input("Enter Today's date:").split("/")
a=int(date1[0])
b=int(date1[1])
c=int(date1[-1])
x=int(date2[0])
y=int(date2[1])
z=int(date2[-1])
dif1=(a-x)
dif2=(b-y)
dif3=(c-z)
a= a>0 and b>0 and c>0 and x>0 and y>0 and z>0 
if a<=31 and x<=31 and b<=12 and y<=12 and c>0 and z>0 and a==True :
    if dif3%4==0:
        val=dif1+(dif2*30)+(dif3*7*30)+(dif3*4*31)+(29)
    else:
        val=dif1+(dif2*30)+(dif3*7*30)+(dif3*4*31)+28
    if val<=0:
        q=((-1)*val)
        print("no of days",q)
    else:
        print("no of days",val)  
    
else:
    print("enter a valid date")
