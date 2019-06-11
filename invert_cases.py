#invert the cases of letters in string i.e from uppercase to lower and viceversa
s=input()
r="" 

for i in s:
	if i.islower():#if lower 
		r=r+i.upper() #another string used as strings are immutable,append it as uppercase
	else:
		r+=i.lower()
		
print(r)
