n=int(input())
i=2

lmt=n//2+1


while i<lmt:
	if n%i==0:
		if i%2==0:
			print(i,end=" ")
	i+=1

if n%2==0:
	print (n)	
