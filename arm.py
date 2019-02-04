kau=int(input())
ori=kau
s=0
n=0
while kau>0:
	n=kau%10
	s+=n**3
	kau=int(kau/10)
if(s==ori):
	print("yes")
else:
	print("no")
