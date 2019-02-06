n=int(input())
kau=list(map(int,input().split()))
j=len(kau)
s=0
for i in range(0,j):
	s+=kau[i]
print(s)  
