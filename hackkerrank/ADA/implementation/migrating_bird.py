#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    k=Counter(arr)
    return(k.most_common(1)[0][0])
    # Return a list of the n most common elements and their counts from the most common to the least. 

        # m=max(k,key=k.get)    #to get highest value 
        # return m
         
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')

    # fptr.close()
