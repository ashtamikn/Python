import collections

x=int(input())
sizes=list(map(int,input().split()))
shoes=collections.Counter(sizes)
cn=int(input())
income=0
for i in range(cn):
    size,price=map(int,input().split())
    if shoes[size]:
        income+=price
        shoes[size]-=1
        
        
print (income)        

# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

# from collections import Counter
# >>> 
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>