n=int(input())
s=input()
l=['a','e','i','o','u','A','E','I','O','U']
r=""
for i in s:
    if i not in l:
        r+=i      
r=r[::-1]#single line to reverse a string
print(r)


