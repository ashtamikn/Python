#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    score=[0,0]
    for x,y in zip(a,b):
        if x>y:
            score[0]+=1
        elif y>x:
            score[1]+=1
    return score            

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
    print('\n')

#     zip() can be used to traverse 2 same sized lists simultaneously. If the 2 lists are of different sizes zip() won't work, for example:

# a = [1,2,3] b = [5,6,7,8,9]

# for i,j in zip(a,b): print i,j

# This will print till 3rd element as till there they both have same elements and will discard everything after. For unequal lists you will have to use zfill() alongwith zip().