#set 5 player 7
l=list(map(int,input().split()))

if sum(l)==180 and 0 not in l:   #sum of interior angles in triangle is 180
	print('yes')
else:
	print('no')
