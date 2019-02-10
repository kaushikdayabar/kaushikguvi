n=int(input())
l=[]
l=input().split()
l=list(map(int,l))
l.sort()
if n%2==0:
	print((l[int(n/2)-1]+l[int(n/2)])/2)
else:
	print(l[int(n/2)])
