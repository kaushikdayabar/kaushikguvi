a,b=input().split()
a,b=int(a),int(b)
s=0
if a%2==0:
	s=a+2
else:
	s=a+1
for kau in range(s,b,2):
	print(kau)
