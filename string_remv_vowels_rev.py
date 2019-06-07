s=input()
l=['a','e','i','o','u','A','E','I','O','U']
r=""
for i in s:
    if i not in l:
        r+=i
print(r)        
r=r[::-1]
print(r)
