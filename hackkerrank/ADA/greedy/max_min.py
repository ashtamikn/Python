#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    
    arr.sort()
    min_dif=sys.maxsize
    for i in range(n-k+1):
        min_dif=min(min_dif,arr[i+k-1]-arr[i])
    return min_dif
#     arr.sort()
#     m=max(arr[:k])-min(arr[:k])
#     return m
# # m=arr[k-1]-arr[0]
#     # return m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
