#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    l=[]
    x=[]
    for i in s:
        # print(ord(i))
        l.append(ord(i))
        print(l)
    for i in range(len(l)-1):
        x.append(abs(l[i]-l[i+1])  )  
    
    print(x)
    if(x==x[::-1]):
        return "Funny"
    else:
        return "Not Funny"
    # y=x.reverse()
    # print()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
