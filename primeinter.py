a,b=input().split()
s,b=int(a)+1,int(b)
l=[]
for dau in range(s,b):
    j,f=int(dau/2)+1,0
    for i in range(2,j):
    	if dau%i==0:
    		f=1
    		break
    if f==0 and dau!=1:
    	l.append(dau)
le=len(l)-1
for i in range(0,le):
	print(l[i],end=" ")
print(l[le],end="")	
