from itertools import combinations_with_replacement
s,k=(input().split())
k=int(k)
# a= (list(combinations_with_replacement(s,k)))
# b='\n'.join(sorted([''.join(i) for i in a]))
# print((b))
for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))
