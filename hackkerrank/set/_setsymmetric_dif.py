# a.union(b) == b.union(a)
# True
# >> a.intersection(b) == b.intersection(a)
# True
# >> a.difference(b) == b.difference(a)
# False

m=int(input())
l1=input().split()
#in string
# print(l1)
a=set(l1)
# print(a)
n=int(input())
l2=input().split()
b=set(l2)
p=a.difference(b) 
q=b.difference(a) 
r=p.union(q)

print ('\n'.join(sorted(r, key=int)))
#If the values in the sets are strings then "key = int" will make them sort like numbers instead of letters.