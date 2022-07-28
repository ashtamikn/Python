#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    ls=[]
    for i in range(p,q+1):
        x=i**2
        s=str(x)
        # print(s)
        l=len(s)
        if(int(s)==1):
            ls.append(1)
            
        if(l>=2):
            m=l//2
            y=s[:m]
            z=s[m:]
            q=int(y)+int(z)
            if(q==i):
                ls.append(i)
    if(len(ls)==0):   
        print("INVALID RANGE")  
    else:           
        print(*ls)        
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
    