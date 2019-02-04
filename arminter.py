a,b=input().split()
a,b=int(a),int(b)
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
		print(ori,end=" ")
