n=int(input())
r=0
kau=0
while n>0:
    r=n%10
    kau=kau*10+r
    n=n//10
print(kau)    
