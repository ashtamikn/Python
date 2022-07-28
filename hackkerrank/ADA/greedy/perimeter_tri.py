#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    print(sticks)
    s=list(combinations(sticks,3))
    print(s)
    ma=0
    l=[-1]
    for a in s:
        a=list(a)
        a.sort()
        if(a[0]+a[1]>a[2]):
            if(sum(a)>ma):
                ma=sum(a)
                l=a
    return l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
