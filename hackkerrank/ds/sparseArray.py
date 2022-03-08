# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'matchingStrings' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. STRING_ARRAY strings
# #  2. STRING_ARRAY queries
# #

# def matchingStrings(strings, queries):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     strings_count = int(input().strip())

#     strings = []

#     for _ in range(strings_count):
#         strings_item = input()
#         strings.append(strings_item)

#     queries_count = int(input().strip())

#     queries = []

#     for _ in range(queries_count):
#         queries_item = input()
#         queries.append(queries_item)

#     res = matchingStrings(strings, queries)

#     fptr.write('\n'.join(map(str, res)))
#     fptr.write('\n')

#     fptr.close()


# import re

# no_strings = int(input())
# strings = []
# no_q = 0
# queries = []

# for _ in range(no_strings):
#     strings.append(input())

# no_q = int(input())
# for _ in range(no_q):
#     queries.append(re.compile(r'^'+input()+'$'))

# for pattern in queries:
#     found = 0
#     for s in strings:
#         found += len(pattern.findall(s))
#     print(found)

import collections
no_strings = int(input())
strings = []

queries = []

for _ in range(no_strings):
    strings.append(input())
    
words=collections.Counter(strings)   
# print(words) 
no_q = int(input())
for _ in range(no_q):
    queries.append(input())  
# print(queries)    
for i in queries:
    print(words[i])      
