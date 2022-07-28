#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    # Write your code here
    def find_min(weights,visited):
        min_wt=sys.maxsize
        for i in  range(1,len(weights)):
            if(weights[i]<min_wt and visited[i]==False):
                min_wt=weights[i]
                minindex=i
        return minindex    
    print(edges)
    graph=[[-1 for i in range (n+1)] for j in range (n+1)]
    for x,y,w in edges:
        graph[x][y]=w
        graph[y][x]=w
        
    visited=[False]*(n+1)
    # sys.maximize returns maximum integer value available
    weights=[sys.maxsize ] *(n+1)
    weights[start]=0
    for i in range( n):
        u=find_min(weights,visited)   
        visited[u]=True
        for v in range(1,n+1):
            if(graph[u][v]>=0 and visited[v]==False and weights[v]>graph[u][v]):
                weights[ v]=graph[u][v]
    return sum(weights[1:])            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
