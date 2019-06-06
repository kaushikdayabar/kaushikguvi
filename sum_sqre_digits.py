kau=int(input())
sum=0
while (kau>0):
	r=kau%10
	kau=kau//10
	sum+=r*r
print(sum)	
