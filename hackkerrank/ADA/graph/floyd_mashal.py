#!/bin/python3
# floyd washal
import math
import os
import random
import re
import sys



n,m=map(int,input().split())
dist_graph=[[math.inf for i in range(n+1)]for j in range (n+1)]
# math.inf works same as sys.maximie
for _ in range(m):
    x,y,w=map(int,input().split())
    dist_graph[x][y]=w
for i in range(1,n+1):
        dist_graph[i][i]=0
        
# main
for k in range(1,n+1):
    for i in range(1,n+1):
        for  j in range(1,n+1):
            dist_graph[i][j]=min(dist_graph[i][j],dist_graph[i][k]+dist_graph[k][j])

            
q=int(input())
for _ in range (q):
        x,y=map(int,input().split())
        if dist_graph[x][y]==math.inf:
            print(-1)
            
        else:
            print(dist_graph[x][y])    
            