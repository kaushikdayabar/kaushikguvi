#set 5 player 4
s,k=input().split()
k=int(k)

r=""
n=len(s)-1                       #to avoid out of bound error while using it as index
for i in range(k):               #rotated k number of times 
	s=s[n]+s[:n]                   
print(s)
