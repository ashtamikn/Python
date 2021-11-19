
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())#strip() is an inbuilt function in Python programming language that 
    # returns a copy of the string with both leading and trailing characters removed
if((n%2!=0) or (n>6 and n<20) ):
    print("Weird\n")
    
else:
    print("Not Weird\n")    