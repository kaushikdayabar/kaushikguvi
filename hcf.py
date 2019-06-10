def hcf(a,b):
    hcf=min(a,b)
    while hcf>0:
        if b%hcf==a%hcf==0:
            return hcf
        else:
            hcf-=1
    return 0        
l=list(map(int,input().split()))    
a=hcf(l[0],l[1])
print(a)
