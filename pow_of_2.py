n=int(input())
e=0


while n!=0:
	if n==1:
		e=1
		break
	else:
		n=n/2
		
if e==1:
	print('yes')
else:
	print('no')
