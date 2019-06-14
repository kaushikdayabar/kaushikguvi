#set 5 player 8    
n=int(input())
i=1                                      

lmt=n//2+1                              


while i<lmt:
	if n%i==0:
		if i%2!=0:                           #n%2!=0 because odd factors
			print(i,end=" ")
	i+=1

if n%2!=0:
	print (n)
