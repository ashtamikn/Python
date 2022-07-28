#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    l=[]
    while(len(arr)>1):
        print(arr)

        x=min(arr)
        l.append(len(arr))
        arr=[i-x for i in arr]
        arr=list(filter((0).__ne__,arr))
        # c=arr.count(x)
        # for i in range(c):
        #     arr.remove(x)
        # print(arr)
    if(len(arr)!=0):
        l.append(len(arr))    
    return l   

    # c = test_list.count(item)
    # for i in range(c):
    #         test_list.remove(item)
 
    # return test_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
