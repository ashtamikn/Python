#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app=0
    org=0
    x=[a+i for i in apples]
    y=[b+i for i in oranges]
    for i in x:
        if i in range(s,t):
            app+=1
    for i in y:
        if i in range(s,t):
            org+=1
    print(app)
    print(org) 

#     print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
# print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))   
# 
# print(sum(s <= a + d <= t for d in apples))
# print(sum(s <= b + d <= t for d in oranges))           
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
