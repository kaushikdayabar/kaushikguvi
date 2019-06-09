n=int(input())
i=c=0
l=[]
while(i<n):
    l.insert(0,input())
    i+=1
s="kabali"
le=len(s)
for i in range(n):
    if le!=len(l[i]):
        continue
    for j in range(le):
        if l[i][j] not in s:
                        break #only in case of brek the else part is skipped
        elif s[j] not in l[i]:
            break
    else:
                c+=1
                
print(c)
 
