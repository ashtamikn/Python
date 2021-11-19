# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    m=int(input())
    a=set(input().split())
    n=int(input())
    b=set(input().split())
    x=a&b
    if x==a:
        print("True")
    else:
        print("False")

    #print(a.issubset(b))    