#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    # print(ord("a")-97+1)
    dic=Counter(s)
    print(dic)
    l=[]
    ans=[]
    
    for k,v in dic.items():
        w=ord(k)-97+1
        for i  in range(1,v+1):
            l.append(w*i)
    print(l)  
    for i in queries:
        if i in l:
            ans.append( "Yes")   
        else:
            ans.append( "No"   )
    return ans        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
