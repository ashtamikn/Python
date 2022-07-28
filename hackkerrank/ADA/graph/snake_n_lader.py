#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    # Write your code here
    graph={}
    for x,y in ladders+snakes:
        graph[x]=y
    q=deque([(1,0)])
    visited=[False]*101
    while q:
        node,rolls=q.popleft()
        if node==100:
            return rolls
        
        visited[node]=True
        for i in range(1,7):
                nextNode=node+i
                if nextNode<=100 and visited[nextNode]==False:
                     if(nextNode  in graph) :
                        q.append((graph[nextNode],rolls+1))
                        # print(q)
                     else:     
                        q.append((nextNode,rolls+1))
                        # print(q)
                        
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
