kau=input()
n=len(kau)

l=[]
for i in range(0,n):
    l.append(kau[i])


#odd length string leads to out of index and the last odd cant be swapped
if(n%2):
    n=n-1

#swapping
for i in range(0,n,2):
    l[i],l[i+1]=l[i+1],l[i]  #no need of temp variable in swapping in python

    
s=""
for i in range(0,n):
    s=s+l[i]
    
print(s)   
    
    

