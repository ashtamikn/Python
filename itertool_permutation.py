# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a,k=(input().split())
k=int(k)
l=(list(permutations(a,k)))

j=sorted(l) 
   
a1=[''.join(i) for i in j]

print('\n'.join(a1))

# print '\n'.join(sorted(''.join(p) for p in permutations(S,k)))
