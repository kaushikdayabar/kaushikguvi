a,b=input().split()
s,b=int(a)+1,int(b)
for kau in range(s,b):
    j,f=int(kau/2),0
    for i in range(2,j+1):
    	if kau%i==0:
    		f=1
    		break
    if f==0 and kau!=1:
    	print(" ",kau)
