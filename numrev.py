kau=int(input())
rev=0
while kau>0:
    n=kau%10
    rev=rev*10+n
    kau=int(kau/10)
print(rev)
