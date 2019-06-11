s1,s2,k=input().split(' ')
k=int(k)
n=max(len(s1),len(s2))
d=0

for i in range(0,n):
    if s1[i]!=s2[i]:
        d+=1
if d==k:
    print('yes')
else:
    print('no')
