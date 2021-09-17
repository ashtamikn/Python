from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
#c is argument sent to anonymous function by itering C one by one
print("{0:.3}".format(len(list(F))/len(C)))