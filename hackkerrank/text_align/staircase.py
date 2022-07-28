#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    pattern=[('#'*(i+1)).rjust(n,' ') for i in range(n)]
    # pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]

    print('\n'.join(pattern))
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
