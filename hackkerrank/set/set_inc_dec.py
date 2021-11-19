# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
arr = [int(x) for x in input().split()]
A = set([int(y) for y in input().split()])
B = set([int(z) for z in input().split()])
count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]
print(sum(count))



# n,m=input().split(' ')
# l1=(map(int,input().split(' ')))
# a=set(map(int,input().split(' ')))
# b=set(map(int,input().split(' ')))
# j=0
# for i in l1:
#     if i in a:
#         j=j+1
#     elif i in b:
#         j=j-1
        
# print(j)        
# x=a.intersection(l1)
# y=b.intersection(l1)
# e=len(x)
# t=len(y)
# print(e-t)