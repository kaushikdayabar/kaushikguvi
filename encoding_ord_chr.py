s=input()
r=""


for i in s:
    if ord(i)+3>90:
        r+=chr(ord(i)-23)
    else:
        r+=chr(ord(i)+3)

print(r)        
