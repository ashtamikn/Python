# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d=deque()
for i in range(int(input())):
    x=input().split()
    if(len(x)>1):
       a=x[0]+"("+x[1]+")"
       eval("d."+a)
    else:
       a=x[0]+"()"   
       eval("d."+a)
       
for i in d:
    print(i,end=" ")       