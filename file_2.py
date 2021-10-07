f=open('fileone.txt','r')
content=f.read()
f.seek(0)
print(content)
print(len(content))

f=open('filethree.txt','r')
for s in f:#it prints line
    print(s,end=' ')
    for k in s:#prints letter by letter
        print(k,end=' ')
fname=input("enter file name ")    
try:
    fhand=open(fname)
except:
    print("file cant be opened:",fname)        
    quit()#quits ...doesnt go further   
d=fhand.read()    
print(d)