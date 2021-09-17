# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

k=int(input())
a=list(map(int,input().split()))
b=Counter(a)
# print(b)
# print(b[1])
for i in b:
    if b[i]==1:
        print(i)