n,k=list(map(int,input().split()))
l=[]
l=list(map(int,input().split()))

for i in range(0,k):
    l=l[-1:-2:-1]+l[0:-1]
n=n-1
for i in range(0,n):
    print(l[i],end=" ")
print(l[n])    
