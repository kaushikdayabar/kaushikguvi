#to print the retrieved string without spaces
s=input()
r=""  #empty string  required to prevent undefined error

for i in s:
	if i!=" ":  #checking for spaces
		r=r+i #using another as strings are immutable

print(r)
