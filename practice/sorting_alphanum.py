a=input()
l,e,o,u=[],[],[],[]
for i in sorted(a):
    if i.isalpha():
        if i.isupper():
            x=u
        else:
            x=l    
            
    else:
        if int(i)%2==0:
            x=e
        else:
            x=o
    x.append(i)         
    
print(''.join(l+u+o+e))    