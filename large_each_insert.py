n,k=input().split()

l=list(map(int,input().split()))
i=list(map(int,input().split()))
for j in i:
	l.append(j)
	print(max(l),end=" ")
