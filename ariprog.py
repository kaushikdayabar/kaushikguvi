n,a,d=input().split()
n=int(n)
a=int(a)
d=int(d)
s=0
for i in range(0,n):
	s=s+(a+i*d)
print(s)
