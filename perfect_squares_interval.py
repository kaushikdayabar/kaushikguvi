import math
l,h=list(map(int,input().split()))
h=h+1
c=0

for i in range(l,h):
	x=math.sqrt(i)
	x=int(x)
	if x*x==i:
		c+=1
		
print(c)		
	
