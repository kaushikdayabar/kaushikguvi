n=int(input())
i=c=0
l=[]
while(i<n):
    l.insert(0,input())
    i+=1
s="kabali"
for i in range(n): 
    le=len(l[i])
    for j in range(le):
        if l[i][j] not in s:
                        break #only in case of brek the else part is skipped
    else:
                c+=1
                
print(c)
 
