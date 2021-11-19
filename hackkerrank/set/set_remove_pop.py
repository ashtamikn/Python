n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    x=input().split()
    cmd=x[0]
    args=x[1:]
    cmd+="("+",".join(args)+")"
    eval("s."+cmd)
    
print(sum(s))