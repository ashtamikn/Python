#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    x=collections.Counter(ar)
    print(x)  
    y=0
    for i in x:
        print(x[i])  
        y=y+int(x[i]/2)
        
    return y    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

    # fptr.close()
