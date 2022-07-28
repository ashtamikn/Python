#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    n=len(s)//3
    sos=[]
    c=0
    for i in range(n):
        sos.append("S")
        sos.append("O")
        sos.append("S")
    print(sos) 
    for k,v in zip(s,sos):
        if(k!=v):
            c+=1  
    return c         


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
