a,b=input().split()
s,b=int(a)+1,int(b)
for dau in range(s,b):
    j,f=int(dau/2),0
    for i in range(2,j+1):
    	if dau%i==0:
    		f=1
    		break
    if f==0 and dau!=1:
    	print(" ",dau)
