#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    c=0
    if any(i.isdigit() for i in password)==False  :
        c+=1
        
    if any(i.islower() for i in  password)==False:
        c+=1
    if any(i.isupper() for i in password)==False:
        c+=1   
    if any(i in "!@#$%^&*()-+" for i in password)==False:
        c+=1
    return max(c,6-len(password))               
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
