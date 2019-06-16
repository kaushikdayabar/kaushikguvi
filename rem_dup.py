s=input()
r=[]
for i in s:
    if s.count(i)>1:
        r.append(i)
        s=s.replace(i,'')

for i in r:
    s+=i

print(s)    
