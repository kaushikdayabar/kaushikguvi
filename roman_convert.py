kau=input()


def get_value(x):
    if x=='I':
        return 1
    elif x==V:
        return 5
    else:
        return 10


res=0
if kau[0]=='I':
    for i in kau:
        if i=='I':
            res=res+1
        elif i=='V':
            res=5-res
        else:
            res=10-res
if kau[0]=='V':
    for i in kau:
        if i=='V':
            res=res+5
        elif i=='I':
            res=res+1
        else:
            res=10-res
if kau[0]=='X':
    for i in kau:
        if i=='X':
            res=res+10
        elif i=='V':
            res=res+5
        else:
            res=res+1
print(res)            
            
