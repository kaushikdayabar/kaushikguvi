n,k=input().split()
n=int(n)
k=int(k)

f,e=1,0
while f<=n:
	if f==n:
		e=1
		break
	f=f*k

if e==1:
	print('yes')
else:
	print('no')
	
