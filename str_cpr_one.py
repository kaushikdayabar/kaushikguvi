s1,s2=input().split(' ')
n=len(s1)
d=0
for i in range(0,n):
    if s1[i]!=s2[i]:
        d+=1
if d>1:
    print('no')
else:
    print('yes')
