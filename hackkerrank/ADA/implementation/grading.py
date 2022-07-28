#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    res=[]
    for i in grades:
        if i<38:
            res.append(i)
        else:
            if i%5==3:
                i+=2
                res.append(i)
            elif(i%5==4):
                i+=1
                res.append(i) 
            else:
                res.append(i)      
    return res  

#     if grade >= 38:
#         if grade % 5 > 2:
#         grade += 5 - (grade % 5)
# print(grade)          

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
    print('\n')

    # fptr.close()
