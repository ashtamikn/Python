#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'boardCutting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost_y
#  2. INTEGER_ARRAY cost_x
#

def boardCutting(cost_y, cost_x):
    # Write your code here
    h=v=1
    cost_x.sort()
    cost_y.sort()
    i=len(cost_y)-1
    j=len(cost_x)-1
    cost=0
    while i>=0 and j>=0:
        if(cost_y[i]>=cost_x[j]):
                cut=cost_y.pop()
                cost+=cut*h
                v+=1
                i-=1
        else:
            cut=cost_x.pop()
            cost+=cut*v
            h+=1
            j-=1    
    if(i>=0):
        cost+=sum(cost_y)*h
    if(j>=0):
        cost+=sum(  cost_x)*v
        
        
    return cost%(10**9+7)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()
