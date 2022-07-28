#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack=[]
    op={"{":"}","[":"]","(":")"}
    
     

    
    for i in s:
        if not stack:
            stack.append(i)
        elif i == op.get(stack[-1]):
            stack.pop()
        else:
            stack.append(i)
    return "YES" if not stack else "NO"
        # if i in op:
            
    #     if(i ==op[stack[-1]]):
    #         print(i,"",op[stack[-1]])
    #         stack.pop()   
    # print(stack)        
    # print("                    ")                   
    # if(len(stack)==0):
    #     return "YES"
    # return "NO"        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
