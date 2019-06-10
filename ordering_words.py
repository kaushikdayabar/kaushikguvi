n=int(input())-1  #to avoid out of bound error
l=input().split()

for i in range(n):
	if len(l[i])>len(l[i+1]):  #check the length of next element,for ordering based on length
		l[i],l[i+1]=l[i+1],l[i]  #single line swapping 
	elif len(l[i])==len(l[i+1]):
		sn=len(l[i])
		for j in range(sn):
			if ord(l[i][j])>ord(l[i+1][j]):#ord function used to sort them lexicographically
				l[i],l[i+1]=l[i+1],l[i]
				
for i in l:
	print(i,end=" ")
