#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alphabet_string = string.ascii_lowercase
    ha=s.lower()
    y=[]
    # print(ha)
    new=[alphabet_string[(ord(i)-97+k)%26] if i.isalpha() else i for i in ha    ]
    # y=("".join(new))
    # print(y)
    # for index in range(len(s)):
    #     if(s[index].isupper()):
    #         break
    for i in range(len(new)):
        if(s[i].isupper()):
            y.append(new[i].upper()) 
        else:
            y.append(new[i])  
    print(y)   
    y="".join(y)    
    print(y)   
    return y   
    # z=y[index].upper()  
    # print(z)  
    # for i in range(len(s)):
    #     if(i==index):
    #         y.upper()
    #     else:
    #         i
    # print(y)            
    # # return(''.join(new))

    # # print(s)
    # # print(ord(s[1])-97)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
