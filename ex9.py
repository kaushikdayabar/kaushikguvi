s=input()
l=s.split()
kau=int(l[1])
s=input()
l=s.split()
l=list(map(int,l))
sum=0
for i in range(0,kau):
    sum=sum+l[i]
print(sum)    
