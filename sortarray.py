kau=list(map(int,input().split()))
kau.sort()
le=len(kau)-1
for i in range(0,le):
	print(kau[i],end=" ")
print(kau[le])
