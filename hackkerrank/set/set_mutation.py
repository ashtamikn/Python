# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a=set((input().split()))
other_sets=int(input())
for i in range(other_sets):
    x,l=input().split()
    b=set((input().split()))
    eval("a."+x+"(b)")
x=list(map(int,a)) 
print (sum(x))

# Enter your code here. Read input from STDIN. Print output to STDOUT
# m=int(input())
# a=set(map(int,input().split()))
# other_sets=int(input())
# for i in range(other_sets):
#     x,l=input().split()
#     b=set(map(int,input().split()))
#     eval("a."+x+"(b)")
    
# print (sum(a))