#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    graph=[[] for i in range(t_nodes+1)]
    # create adjacency list
    for x,y in zip(t_from,t_to):
        graph[x].append(y)
        graph[y].append(x)
    # count is like visited if 0 not visited else visited...it is also used to count number of edges for a node
    count=[0]*(t_nodes+1)    
    def dfs(u,graph,count):
        count[u]=1
        removed_edges=0
        for v in graph[u]:
            if count[v]==0:
                removed_edges+=dfs(v,graph,count)
                count[u]+=count[v]
                if(count[v]%2==0):
                    removed_edges+=1
        return removed_edges
    return dfs(1,graph,count)            
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
