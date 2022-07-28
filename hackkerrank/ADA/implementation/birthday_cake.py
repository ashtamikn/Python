#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    m=max(candles)
    k=collections.Counter(candles)
    # height = [int(height_temp) for height_temp in input().strip().split(' ')]
    # print(height.count(max(height)))

    return(k[m])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(str(result) + '\n')

    # fptr.close()
