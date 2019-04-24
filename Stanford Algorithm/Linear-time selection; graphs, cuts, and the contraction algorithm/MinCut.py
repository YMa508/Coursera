# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:37:02 2019

@author: ym4558
"""

import numpy as np
import copy

text_file = open("kargerMinCut.txt", "r")
#text_file = open("case2.txt", "r")
lines = text_file.read().splitlines()
graph1 = dict()
for line in lines:
    key, *val = line.split()
    graph1[key] = val

def diff(A, B):
    return [item for item in A if item != B]
#
#graph = dict()
#graph['1'] = ['2', '5', '6'] 
#graph['2'] = ['1', '3', '5', '6'] 
#graph['3'] = ['2', '4', '7', '8'] 
#graph['4'] = ['3', '7', '8']
#graph['5'] = ['1', '2', '6']
#graph['6'] = ['1', '2', '5', '7']
#graph['7'] = ['3', '4', '6', '8']
#graph['8'] = ['3', '4', '7']

def MinCut(graph0):
    graph = copy.deepcopy(graph0)
    while len(graph.keys()) > 2:
        #random choose the first vertex of the edge
        left = np.random.choice(list(graph.keys()))
        #random choose the second vertex of the edge
        right = np.random.choice(graph[left])
        #print(left, right)
        graph[left] = diff(graph[left], right) + diff(graph[right], left)
        
        graph.pop(right)
        
        for key, value in graph.items():
            if key!= left:
                graph[key] = [left if x == right else x for x in value]
        #print(graph)
    return len(graph[list(graph.keys())[0]])

#print(MinCut(graph1))

mincuts = []
N = len(graph1)
for i in range(int(N**2 * np.log(N))):
    #print(len(graph1.keys()))
    res = MinCut(graph1)
    mincuts.append(res)

print(min(mincuts))
#print(mincuts)