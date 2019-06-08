l=list(map(int,input().split()))
if l[0]>l[1]:
	mx=lcm=l[0] #taking lcm to be the larger number
	mi=l[1]
else:
	mx=lcm=l[1]
	mi=l[0]
	
i=2

while(not(lcm%mi==0)):#checking whether the number is multiple of minimum number
	lcm=mx*i      #incrementing lcm in steps of larger number hence it is multiple of largernumber as well as results could be achieved with less computation 
	i+=1

print(lcm)	
