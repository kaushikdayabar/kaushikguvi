s=input()
r=""  #empty string  required to prevent undefined error
n=len(s)

for i in range(n):
    if s[i]!=" ":  #checking for spaces
        r=r+s[i] #using another as strings are immutable
    elif s[i]==" ":
        if s[i-1]!=" ":
            r=r+s[i]
                
print(r)
