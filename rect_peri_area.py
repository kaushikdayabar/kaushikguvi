p,a=map(int,input().split())


l=p//2-1
f=0
b=1
while l>1:
	if l*b==a:
		f=1
		break
	l-=1
	b+=1


if f==1:
	print('yes')
else:
	print('no')
	
