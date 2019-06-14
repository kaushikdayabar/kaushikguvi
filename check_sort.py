#set 5 player 2
n=int(input())
l=list(map(int,input().split()))

le=len(l)-1
for i in range(le):
	if l[i]>l[i+1]:
		print('no')
		break
else:
	print('yes')
