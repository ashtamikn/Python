# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

a=input()
b=[(len(list(c)), int(k)) for k, c in groupby(a)]
print(*b)

# '*' is used in Python 3 to open up a list when printing it.

# print(*[1,2,3,4])

# 1 2 3 4
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
