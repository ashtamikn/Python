#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
       
    maxHeight=0
    for i in range(len(word)):
        if(h[ord(word[i])-97] > maxHeight):
            maxHeight=h[ord(word[i])-97]
            # ord(word[i])-97 gives index of that letter in alphabets eg ord(t)-97=20
    return(len(word)*1*maxHeight)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
