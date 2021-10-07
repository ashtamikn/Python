# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t=int(input())
# pattern=
pattern=re.compile(r'^[7-9][0-9]{9}$')
for i in range(t):
    s=input()
    a=pattern.match(s)
    if a:
        print('YES')
    else:
        print("NO")    
        
        
#         if re.match(r'[789]\d{9}$',raw_input()):   
#     print 'YES'  
# else:  
#     print 'NO'  