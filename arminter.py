a,b=input().split()
a,b=int(a),int(b)
l=[]
for i in range(a,b):
	kau=i
	ori=kau
	s=0
	n=0
	while kau>0:
		n=kau%10
		s+=n**3
		kau=int(kau/10)
	if(s==ori):
		l.append(ori)
le=len(l)
for i in range(0,le-1):
	print(l[i],end=" ")
print(l[le-1],end="")	
