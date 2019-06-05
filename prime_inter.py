l,h=list(map(int,input().split()))
h=h+1
c,f=0,0


if l<=1:   #prevents 0,1
    l=2

    
for i in range(l,h):
    #code to check prime
    for j in range(2,i):  #for could be used as if
        if i%j==0:
            break
    else:
        c+=1
 
print(c)        
        
        
