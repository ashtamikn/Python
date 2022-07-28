#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    k=sorted(arr)
    # print(k)
    mins=0
    maxs=0
    n=len(arr)
    for i in range(4):
        mins+=k[i]
    for i in range(4):
        maxs+=k[n-1-i]
    print(mins,maxs)    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
