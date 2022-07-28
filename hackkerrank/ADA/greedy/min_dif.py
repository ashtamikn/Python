#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    # a=combinations(arr,2)
    # x=[]
    # print(a)
    # for i,j in a:
    #     x.append(abs(i-j))
    # return min(x) 
    arr.sort()
    min_dif=sys.maxsize
    for i in range(1,len(arr)):
        min_dif=min(min_dif,abs(arr[i-1]-arr[i]))
    return min_dif      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
