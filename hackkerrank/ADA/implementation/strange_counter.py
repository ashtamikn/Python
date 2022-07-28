#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    # ini=3
    # x=3
    # for i in range(1,t):
    #     if(ini==1):
    #         ini=x*2
    #         x=x*2
    #         continue
    #     ini-=1 
    #     # print(ini)   
            
    # return ini
    # t = int(input())
    n = 0
    count = 0
    while n < t:
        n += 3*(2**count)
        count += 1
    return(n-t+1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
    