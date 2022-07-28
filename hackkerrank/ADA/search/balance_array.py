#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    # for i in range(len(arr)):
    #     a=sum(arr[:i-1])
    #     print(a)
    #     b= sum(arr[i:])
    #     # print(b)
    #     if(a==b):
    #         return("YES")
       
    # return "NO"
    right=sum(arr)
    left=0
    for i in arr:
        right-=i
        if right==left:
            return "YES"
        left+=i
    return "NO"    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
