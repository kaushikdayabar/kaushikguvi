s1,s2,k=input().split(' ')
k=int(k)
n=max(len(s1),len(s2))  #getting the range as max length out of 2 strings
d=0

for i in range(n):
    if s1[i]!=s2[i]:
        d+=1         #for each difference d is incremnted

if d==k:           #checking whether difference = given difference
    print('yes')
else:
    print('no')
