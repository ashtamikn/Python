#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    print(contests)
    a1=[]
    a2=[]
    su=0
    for a,b in contests:
        if(b==1):
            a1.append(a)
        else:
            a2.append(a)
    # for i in range(k):
    #     su+=a1[i]  
    a1.sort(reverse=True)
    t=sum(a1[:k])-sum(a1[k:])
    
    res=t+sum(a2)
    return res
    # print(tot)
    # tot=tot+sum(a2)
    # return tot
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
