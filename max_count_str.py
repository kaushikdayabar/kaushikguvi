s=input()
mx=s[0]
for i in s:
    if s.count(mx)<s.count(i):
        mx=i
print(mx)        
