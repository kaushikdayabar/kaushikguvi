n=int(input())-1
kau=list(map(int,input().split()))
kau.sort()
for i in range(0,n):
	print(kau[i],end=" ")
print(kau[n])
