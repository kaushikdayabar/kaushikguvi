def is_island(l,i,j):
    if l[i-1][j]==l[i][j-1]==l[i+1][j]==l[i][j+1]==0:
        return 1
    
n=int(input())
c=0           #inintialising number of islands to be 0


# to get matrix as input
l=[]
for i in range(n):
    l.append([0]+list(map(int,input().split()))+[0]) #the left and right are cocatenated with 0
n=n+2                     #for appending zeroes size is increased
l.insert(0,[0]*n)         #the topmost row is 0
l.insert(n+1,[0]*n)       #the bottomost row is 0

   

#counting number of islands
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            if is_island(l,i,j):
                c+=1
print(c)
            

        
