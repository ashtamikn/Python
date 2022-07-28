#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    ltr=0
    rtl=0
    for i in range(len(arr)):
        ltr+=arr[i][i]
    for i in range(len(arr),):
        rtl+=arr[i][n-1-i] 

#     d1 = sum([a[x][x] for x in range(n)]) 
# d2 = sum([a[x][n-1-x] for x in range (n)])    
    return (abs(ltr-rtl))      

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    print(str(result) + '\n')

    # fptr.close()
