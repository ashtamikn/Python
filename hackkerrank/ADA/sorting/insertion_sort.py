#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    # int i,key=0,j;
    # // int n=arr.size();
    for i in range(1,n):
        key=arr[i];
        j=i-1;
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j];
            j-=1
        
        arr[j+1]=key;
        # for i in range(0,n):
        print(*arr)
        # print(' '.join(arr))
        # }
        # cout<<endl;
    # }
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
