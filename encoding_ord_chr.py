s=input()
r=""


for i in s:
    if ord(i)+3>90:
        r+=chr(ord(i)-23)  #ord to convert character into unicode,once 91 is reached 26 subtraction and 3 addition hence 3-26=-23 
    else:
        r+=chr(ord(i)+3)   #chr to convert into characeter

print(r)        
