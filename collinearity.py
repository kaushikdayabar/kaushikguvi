l1=list(map(int,input().split()))  #getting coordinates of each point
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))



a=0.5*(l1[0]*(l2[1]-l3[1])+l2[0]*(l1[1]-l3[1])+l3[0]*(l2[1]-l1[1]))
#calculating  area based on the 3 point 

if a==0:
    print("yes")
else:
    print("no")
