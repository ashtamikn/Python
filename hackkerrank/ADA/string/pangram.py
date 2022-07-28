#!/bin/python3

import math
import os
import random
import re
import sys
import string
from collections import Counter
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    # alphabet_string=string.ascii_lowercase
    s=s.lower()
    # if(all(i in alphabet_string for i in s)):
    #     return "pangram"
    # else:
    #     return "not pangram"

    # print('pangram' if len(set(str.lower(input()))) == 27 else 'not pangram'

    c=Counter(s)
    if(len(c)==27):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
