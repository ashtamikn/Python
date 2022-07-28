#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#Given two arrays of integers, find which elements in the second array are missing from the first array.
# Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.

# missingNumbers has the following parameter(s):

# int arr[n]: the array with missing numbers
# int brr[m]: the original array of numbers
# difference between dictinary



def missingNumbers(arr, brr):
    # Write your code here
    a=Counter(arr)
    b=Counter(brr)
    c=b-a
    return (sorted(c.keys()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
