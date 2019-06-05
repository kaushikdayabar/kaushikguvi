n,k=list(map(int,input().split()))
l=[]
l=list(map(int,input().split()))
print(l)

for i in range(0,k):
    l=l[-1:-2:-1]+l[0:-1]

print(l)    
