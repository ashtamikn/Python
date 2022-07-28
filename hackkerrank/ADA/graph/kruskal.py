#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    def find(parent,node):
        if(parent[node]==node):
            return node
        else:
            return find(parent,parent[node])
        
    def union(u,v,parent,rank):
        xroot=find(parent,u)
        yroot=find(parent,v)
        if(rank[xroot]<rank[yroot]):
            parent[xroot]=yroot
            rank[yroot]+=rank[xroot]
            
            
        elif(rank[xroot]>rank[yroot]):
            parent[yroot]=xroot
            rank[xroot]+=rank[yroot]
        else:
             parent[yroot]=xroot  
             rank[xroot]+=1            
    
    graph=[]
    for u,v,w in zip(g_from,g_to,g_weight):
        graph.append([u,v,w])
        # based on weight graph is going to be sorted
    graph=sorted(graph,key=lambda x:x[2])
    # parent is initially assigned with parent node of eac node id node itself
    parent=[v for v in range(g_nodes+1)]
    # rank is used at later stage of union to decide parent.set with higher elements i sconsidered as parent
    rank=[0]*(g_nodes+1)
    tot_wgt=0 
    i=edges=0   
    # main
    while edges<g_nodes-1:
        u,v,w=graph[i]
        if(find(parent,u)!=find(parent,v)):
            edges+=1
            tot_wgt+=w
            union(u,v,parent,rank)
            
        i+=1
    return tot_wgt        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res))

    fptr.close()
