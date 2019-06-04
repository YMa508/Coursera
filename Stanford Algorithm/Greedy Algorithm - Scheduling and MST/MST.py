# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:37:11 2019

@author: YM4558
"""

import numpy as np
import pandas as pd
import math
import time
import heap

text_file = open("edges.txt", "r")
lines = text_file.read().splitlines()
num_nodes = int(lines[0].split()[0])
num_edges = int(lines[0].split()[1])

node1 = []
node2 = []
costs = []

for line in lines[1:]:
    n1, n2, c = line.split()
    node1.append(int(n1))
    node2.append(int(n2))
    costs.append(int(c))

def naive(node1, node2, costs):
    X = [node1[0]]
    T = []
    totalcosts = 0
    while len(X) < num_nodes:
        mincost = math.inf
        for idx in range(num_edges):
            if (node1[idx] in X) and (node2[idx] not in X) and (costs[idx] < mincost):
                mincost = costs[idx]
                candidate = node2[idx]
                can_edge = (node1[idx], node2[idx], mincost)
            elif (node2[idx] in X) and (node1[idx] not in X) and (costs[idx] < mincost):
                mincost = costs[idx]
                candidate = node1[idx]
                can_edge = (node1[idx], node2[idx], mincost)
        totalcosts += mincost
        X.append(candidate)
        T.append(can_edge)
    return totalcosts, T

# initialize X
start_time = time.time()
a = naive(node1, node2, costs)
print(a[0])
print("--- %s seconds ---" % (time.time() - start_time))
pd.DataFrame(a[1]).to_csv("naive.csv")

start_time = time.time()
X = [node1[0]] # 1
T2 = []
mincosts = [math.inf] * (num_nodes)
# loop through all the edges to initialize the heap
for idx in range(num_edges):
    if (node1[idx] == X[0]) and (costs[idx] <= mincosts[node2[idx] - 1]):
        mincosts[node2[idx] - 1] = costs[idx]
    elif (node2[idx] == X[0]) and (costs[idx] <= mincosts[node1[idx] - 1]):
        mincosts[node1[idx] - 1] = costs[idx]
#print("initialization: --- %s seconds ---" % (time.time() - start_time))

msth = heap.Heap()
#for i in range(1, num_nodes):
for i in range(1, num_nodes):
    msth.insert(X[0], i + 1, mincosts[i])
#print(msth.nodes, msth.heap)

tocosts = 0
while len(msth.heap) > 0:
    c, xn, v = msth.extractMin()
    #print("after extract_min", msth.nodes, msth.heap)
    X.append(v)
    tocosts += c
    T2.append((xn, v, c))
    #print(v)
    # find the influenced vertex
    linked_nodes = list(np.array(node2)[np.array(node1) == v]) + list(np.array(node1)[np.array(node2) == v])
    #linked_nodes = list(set(linked_nodes) - set(X))
    #print(linked_nodes)
    cc = list(np.array(costs)[np.array(node1) == v]) + list(np.array(costs)[np.array(node2) == v])
    for idx, w in enumerate(linked_nodes):
        if w not in X:
            w_idx = msth.nodes.index(w)
            cost = min(msth.heap[w_idx], cc[idx])
            if cost == cc[idx]:
                xn = v
            else:
                xn = msth.Xns[w_idx]
            msth.delNode(w_idx)
            #print("after delete", w, ":",  msth.nodes, msth.heap)
            msth.insert(xn, w, cost)
            #print("reinsert", w_idx, ":",  msth.nodes, msth.heap)
print(tocosts)
print("--- %s seconds ---" % (time.time() - start_time))
pd.DataFrame(T2).to_csv("heap.csv")