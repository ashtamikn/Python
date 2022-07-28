#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    l=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine" ]
    if(m<=30):
        if(m==0):
            return(l[h]+" o' clock")
        elif(m==15):
            return("quarter past "+l[h])
        elif(m==30):
            return("half past "+l[h])
        elif(m==1):
            return(l[m]+" minute past "+l[h])

        else:
            return(l[m]+" minutes past "+l[h])
    else:    
        if(m==45):
            return("quarter to "+l[h+1])
        elif(m==59):
            return(l[60-59]+" minute to "+l[h+1])
        else:
            return(l[60-m]+" minutes to "+l[h+1])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
