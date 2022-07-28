#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr,n):
    # Write your code here
    z=0
    p=0
    q=0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            q+=1
        else:
            z+=1
    # print(p,q,z)        
    print("{:.6f}".format(p/n))     
    print("{:.6f}".format(q/n))                

    print("{:.6f}".format(z/n))
#     arr = [1 if int(temp)>0 else -1 if int(temp)<0 else 0 for temp in input().strip().split(' ') ]
# print("{0:.6f}".format(arr.count(1)/n))
# print("{0:.6f}".format(arr.count(-1)/n))
# print("{0:.6f}".format(arr.count(0)/n))                


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)
