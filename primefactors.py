def prime(n):
    lmt=n//2+1
    if n>1:
        for i in range(2,lmt):
            if n%i==0:
                return 0
        else:
            return 1
    else:
        return 0
                
            
kau=int(input())

limit=kau//2+1


i=1
l=[]
while(i<limit):
    if kau%i==0:  # checking for factors
        if prime(i):  # checking for prime numbers
            l.append(i)
    i+=1        
            
if prime(kau):   #checking whether the given number is prime,if so it appended as it is also a factor
    l.append(kau)
            
for j in l:
    print(j,end=" ") #printing the prime factors
