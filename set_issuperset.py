# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(input().split())
n=int(input())
status=True
for i in range(n):
    b=set(input().split())
    if a.issuperset(b)==False:
        status=False
        break;
        
print(status)        